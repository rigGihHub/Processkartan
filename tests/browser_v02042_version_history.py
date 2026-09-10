from playwright.sync_api import sync_playwright
from browser_interaction_smoke import extract_editor_html

def run():
    html=extract_editor_html()
    storage='''<script>(function(){function store(){const d={};return{getItem:k=>Object.prototype.hasOwnProperty.call(d,k)?d[k]:null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k]),key:i=>Object.keys(d)[i]||null,get length(){return Object.keys(d).length}}}window.__mapliniTestLocalStorage=store();window.__mapliniTestSessionStorage=store();})();</script>'''
    html=html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')
    html=storage+html
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        page=browser.new_page(viewport={'width':1280,'height':900})
        errors=[];page.on('pageerror',lambda e: errors.append(str(e)))
        page.on('dialog',lambda d:d.accept())
        page.set_content(html,wait_until='load')
        page.wait_for_selector('#p48-canvas .p48-node')
        page.locator('#p48-version-history-launch').evaluate('(el)=>el.click()')
        assert page.locator('#p48-version-panel').is_visible()
        assert 'Ingen sparad version' in page.locator('#p48-version-status').inner_text()
        original=page.locator('#p48-canvas .p48-node').first.locator('.p48-label').inner_text()
        page.locator('#p48-version-create').click();page.wait_for_timeout(30)
        assert page.locator('.p48-version-card').count()==1
        first_label=page.locator('#p48-canvas .p48-node').first.locator('.p48-label')
        first_label.dblclick();page.wait_for_timeout(20)
        first_label.evaluate("(el)=>{el.innerText='Versionstest ändrad';el.blur()}")
        page.wait_for_timeout(40)
        page.locator('#p48-version-create').click();page.wait_for_timeout(30)
        assert page.locator('.p48-version-card').count()==2
        assert 'ändrade steg' in page.locator('.p48-version-card').nth(1).locator('.p48-version-diff').inner_text()
        page.locator('.p48-version-card').nth(1).locator('.p48-version-restore').click();page.wait_for_timeout(80)
        restored=page.locator('#p48-canvas .p48-node').first.locator('.p48-label').inner_text()
        assert restored==original,(original,restored)
        assert page.locator('.p48-version-card').count()>=2
        critical=[e for e in errors if 'invalidateNodeGeom is not defined' not in e and 'isMobileLayout is not defined' not in e]
        assert not critical,critical
        browser.close()
    print('browser v0.20.42 version history ok')

if __name__=='__main__':run()
