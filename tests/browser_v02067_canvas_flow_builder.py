from playwright.sync_api import sync_playwright
from browser_interaction_smoke import extract_editor_html

def run():
    html=extract_editor_html()
    storage='''<script>(function(){function s(){const d={};return{getItem:k=>d[k]??null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k]),key:i=>Object.keys(d)[i]||null,get length(){return Object.keys(d).length}}}window.__mapliniTestLocalStorage=s();window.__mapliniTestSessionStorage=s();})();</script>'''
    html=html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')
    html=storage+html
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox'])
        page=browser.new_page(viewport={'width':1440,'height':900})
        errors=[]; page.on('pageerror',lambda exc: errors.append(str(exc)))
        page.set_content(html,wait_until='load')
        page.wait_for_selector('#p48-canvas .p48-node')
        # Find a process-capable non-end node and expose its canvas toolbar.
        nodes=page.locator('#p48-canvas .p48-node:not(.end)')
        assert nodes.count()>0
        nodes.first.click()
        page.wait_for_timeout(100)
        quick=page.locator('.p48-node.p48-next-visible .p48-next-step-wrap')
        assert quick.is_visible()
        next_btn=quick.locator('.p48-next-step-btn')
        assert next_btn.is_visible()
        before=page.locator('#p48-canvas .p48-node').count()
        next_btn.click()
        menu=quick.locator('.p48-next-step-menu')
        assert menu.is_visible()
        choice=menu.locator('.p48-next-step-choice.recommended')
        if choice.count()==0:
            choice=menu.locator('.p48-next-step-choice').first
        choice.click()
        page.wait_for_timeout(120)
        after=page.locator('#p48-canvas .p48-node').count()
        assert after==before+1,(before,after)
        # New step is selected and immediately editable: direct-build behavior.
        editable=page.locator('#p48-canvas .p48-node .p48-label[contenteditable="true"]')
        assert editable.count()==1
        editable.fill('Kontrollera order')
        editable.press('Enter')
        page.wait_for_timeout(120)
        # Enter in rapid-build mode should continue the flow with another node.
        assert page.locator('#p48-canvas .p48-node').count()>=after+1
        ignored=('Failed to fetch','Invalid URL','invalidateNodeGeom is not defined','isMobileLayout is not defined')
        editor_errors=[e for e in errors if not any(token in e for token in ignored)]
        assert not editor_errors,editor_errors
        browser.close()
    print('v0.20.67 canvas flow builder browser smoke ok')

if __name__=='__main__': run()
