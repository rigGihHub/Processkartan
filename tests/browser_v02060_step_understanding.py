from pathlib import Path
from playwright.sync_api import sync_playwright
from browser_interaction_smoke import extract_editor_html

def run():
    html=extract_editor_html()
    storage='''<script>(function(){function store(){const d={};return{getItem:k=>d[k]??null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k]),get length(){return Object.keys(d).length}}}window.__mapliniTestLocalStorage=store();window.__mapliniTestSessionStorage=store()})();</script>'''
    html=html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')
    html=storage+html
    with sync_playwright() as p:
        b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        page=b.new_page(viewport={'width':1500,'height':1000});errs=[];page.on('pageerror',lambda e:errs.append(str(e)))
        page.set_content(html,wait_until='load');page.wait_for_selector('#p48-canvas .p48-node')
        # Use real editor UI. Pick the first activity/process node.
        process_id=page.evaluate("window.__mapliniTestState.nodes().find(n=>n.type==='process')?.id || ''")
        assert process_id
        node=page.locator(f'#p48-canvas .p48-node[data-id="{process_id}"]')
        assert node.count()==1
        node.click()
        page.wait_for_selector('#p48-step-understanding:not([hidden])')
        rows=page.locator('#p48-step-understanding-list .p48-step-understanding-row')
        assert rows.count()==5
        text=page.locator('#p48-step-understanding').inner_text()
        for label in ['VAD?','VEM?','INPUT','OUTPUT','SEDAN']:
            assert label in text
        # Populate actual step metadata and confirm the compact summary updates from it.
        page.locator('#p48-info-description').fill('Kontrollera att ordern är komplett.')
        page.locator('#p48-info-description').dispatch_event('change')
        page.locator('#p48-info-role').fill('Kundservice')
        page.locator('#p48-info-role').dispatch_event('change')
        text=page.locator('#p48-step-understanding').inner_text()
        assert 'Kontrollera att ordern är komplett.' in text
        assert 'Kundservice' in text
        relevant=[e for e in errs if 'StepUnderstanding' in e or 'renderStepUnderstanding' in e]
        assert not relevant, relevant
        b.close()
    print('v0.20.67 step understanding browser smoke ok')
if __name__=='__main__': run()
