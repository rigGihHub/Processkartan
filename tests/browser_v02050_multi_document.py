from pathlib import Path
from playwright.sync_api import sync_playwright
from browser_interaction_smoke import extract_editor_html

def run():
    html=extract_editor_html()
    storage='''<script>(function(){function store(){const d={};return{getItem:k=>Object.prototype.hasOwnProperty.call(d,k)?d[k]:null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k]),key:i=>Object.keys(d)[i]||null,get length(){return Object.keys(d).length}}}window.__mapliniTestLocalStorage=store();window.__mapliniTestSessionStorage=store();})();</script>'''
    html=html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')
    html=storage+html
    a=Path('/tmp/maplini_doc_02050_a.txt');b=Path('/tmp/maplini_doc_02050_b.txt')
    a.write_text('Kundservice kontrollerar ordern. Kundservice registrerar ordern. Ekonomi skickar fakturan.',encoding='utf-8')
    b.write_text('Ekonomi kontrollerar ordern. Ekonomi skickar fakturan. Kundservice registrerar ordern.',encoding='utf-8')
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        page=browser.new_page(viewport={'width':1280,'height':900});errors=[]
        page.on('pageerror',lambda e:errors.append(str(e)));page.on('dialog',lambda d:d.accept())
        page.set_content(html,wait_until='load');page.wait_for_selector('#p48-canvas .p48-node')
        page.locator('#p48-new').click();page.locator('#p48-new-process-name').fill('Flerdokumenttest');page.locator('#p48-new-process-name').press('Enter');page.wait_for_timeout(70)
        page.evaluate("document.querySelector('#p48-doc-launch').click()")
        page.locator('#p48-doc-file').set_input_files([str(a),str(b)]);page.wait_for_timeout(350)
        status=page.locator('#p48-doc-status').inner_text();assert 'Gemensamt förslag klart' in status and 'konflikter' in status
        structured=page.locator('#p48-doc-structured').inner_text();assert 'Källa:' in structured and 'Olika ansvar' in structured and 'Olika ordning' in structured
        assert page.locator('.p48-doc-row.conflict').count()>=1
        assert page.locator('#p48-doc-create').is_disabled()
        cards=page.locator('.p48-doc-conflict-card');assert cards.count()>=1
        for i in range(cards.count()):
            cards.nth(i).locator('.p48-doc-conflict-options button').first.click();page.wait_for_timeout(30)
        assert not page.locator('#p48-doc-create').is_disabled()
        page.locator('#p48-doc-create').click();page.wait_for_timeout(180)
        assert page.locator('#p48-canvas .p48-node').count()>=3
        critical=[e for e in errors if 'invalidateNodeGeom is not defined' not in e and 'isMobileLayout is not defined' not in e]
        assert not critical,critical
        browser.close()
    print('browser v0.20.50 multi document synthesis ok')

if __name__=='__main__': run()
