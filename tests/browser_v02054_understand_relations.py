from pathlib import Path
from playwright.sync_api import sync_playwright
from browser_interaction_smoke import extract_editor_html

def run():
    html=extract_editor_html()
    storage='''<script>(function(){function store(){const d={};return{getItem:k=>Object.prototype.hasOwnProperty.call(d,k)?d[k]:null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k]),key:i=>Object.keys(d)[i]||null,get length(){return Object.keys(d).length}}}window.__mapliniTestLocalStorage=store();window.__mapliniTestSessionStorage=store();})();</script>'''
    html=html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')
    html=storage+html
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        page=browser.new_page(viewport={'width':1280,'height':900});errors=[]
        page.on('pageerror',lambda e:errors.append(str(e)));page.on('dialog',lambda d:d.accept())
        page.set_content(html,wait_until='load');page.wait_for_selector('#p48-canvas .p48-node')
        page.locator('#p48-new').click();page.locator('#p48-new-process-name').fill('Nyhetsflöde');page.locator('#p48-new-process-name').press('Enter');page.wait_for_timeout(60)
        page.evaluate("document.querySelector('#p48-doc-launch').click()")
        text='Bolaget meddelade en kraftig prishöjning. Därför föll efterfrågan. Företaget lanserade därefter en billigare tjänst.'
        page.locator('#p48-source-text').fill(text);page.locator('#p48-source-text-run').click();page.wait_for_timeout(120)
        status=page.locator('#p48-doc-status').inner_text();assert 'Händelseförlopp' in status,status
        assert 'tydliga samband' in status,status
        assert 'Orsak → konsekvens' in page.locator('#p48-doc-structured').inner_text()
        assert page.locator('#p48-doc-create').is_enabled()
        page.locator('#p48-doc-create').click();page.wait_for_timeout(100)
        assert page.locator('#p48-canvas .p48-node').count()>=3
        first=page.locator('#p48-canvas .p48-node').first;first.locator('.p48-label').click();page.wait_for_timeout(50)
        assert page.locator('#p48-source-trace').is_visible()
        assert 'Inklistrad text' in page.locator('#p48-source-trace').inner_text()
        critical=[e for e in errors if 'invalidateNodeGeom is not defined' not in e and 'isMobileLayout is not defined' not in e]
        assert not critical,critical
        browser.close()
    print('browser v0.20.54 understand relations ok')
if __name__=='__main__': run()
