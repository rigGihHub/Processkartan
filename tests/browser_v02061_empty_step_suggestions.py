from playwright.sync_api import sync_playwright
from browser_interaction_smoke import extract_editor_html

def run():
    html=extract_editor_html()
    storage='''<script>(function(){function store(){const d={};return{getItem:k=>d[k]??null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k]),get length(){return Object.keys(d).length}}}window.__mapliniTestLocalStorage=store();window.__mapliniTestSessionStorage=store()})();</script>'''
    html=storage+html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')
    with sync_playwright() as p:
        b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1500,'height':1000});errs=[];page.on('pageerror',lambda e:errs.append(str(e)))
        page.set_content(html,wait_until='load');page.wait_for_selector('#p48-canvas .p48-node')
        # Add a process step through the real editor API exposed by test harness; default title is a placeholder.
        page.evaluate("window.__mapliniTestState.addNode('process',720,460)")
        pid=page.evaluate("window.__mapliniTestState.nodes().filter(n=>n.type==='process').slice(-1)[0].id")
        page.locator(f'#p48-canvas .p48-node[data-id="{pid}"]').click()
        # Provide an explicit input; suggestion must be derived from it and labelled as a suggestion.
        page.locator('#p48-add-input').click();inp=page.locator('#p48-inputs input').last;inp.fill('Order');inp.dispatch_event('change')
        page.wait_for_selector('#p48-empty-step-suggestions:not([hidden])')
        txt=page.locator('#p48-empty-step-suggestions').inner_text();assert 'kontrollera innan du använder' in txt.lower();assert 'Hantera Order' in txt
        page.locator('#p48-empty-step-suggestions button',has_text='Använd').first.click()
        title=page.locator(f'#p48-canvas .p48-node[data-id="{pid}"] .p48-label').inner_text();assert title=='Hantera Order'
        assert page.locator('#p48-empty-step-suggestions').is_hidden()
        # v0.20.66: process search finds a step and jumps back to the matching node.
        page.locator('#p48-find-menu summary').click();page.locator('#p48-find-input').fill('Hantera Order')
        page.wait_for_selector('#p48-find-results [data-find-id]')
        assert '1 träff' in page.locator('#p48-find-meta').inner_text()
        page.locator('#p48-find-results [data-find-id]').first.click()
        assert page.locator(f'#p48-canvas .p48-node[data-id="{pid}"]').evaluate("el=>el.classList.contains('selected')")
        assert not [e for e in errs if 'EmptyStep' in e or 'renderEmptyStep' in e],errs
        b.close()
    print('v0.20.67 empty step + process find browser smoke ok')
if __name__=='__main__':run()
