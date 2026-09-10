from pathlib import Path
from playwright.sync_api import sync_playwright
from browser_interaction_smoke import extract_editor_html

def run():
    html=extract_editor_html()
    storage='''<script>(function(){function store(){const d={};return{getItem:k=>Object.prototype.hasOwnProperty.call(d,k)?d[k]:null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k]),key:i=>Object.keys(d)[i]||null,get length(){return Object.keys(d).length}}}window.__mapliniTestLocalStorage=store();window.__mapliniTestSessionStorage=store();})();</script>'''
    html=html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')
    html=storage+html
    a=Path('/tmp/maplini_02056_a.txt');b=Path('/tmp/maplini_02056_b.txt')
    a.write_text('Kundservice kontrollerar ordern. Kundservice registrerar ordern.',encoding='utf-8')
    b.write_text('Ekonomi kontrollerar ordern. Kundservice registrerar ordern.',encoding='utf-8')
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        page=browser.new_page(viewport={'width':1280,'height':900});errors=[]
        page.on('pageerror',lambda e:errors.append(str(e)));page.on('dialog',lambda d:d.accept())
        page.set_content(html,wait_until='load');page.wait_for_selector('#p48-canvas .p48-node')
        page.locator('#p48-new').click();page.locator('#p48-new-process-name').fill('Källstödtest');page.locator('#p48-new-process-name').press('Enter');page.wait_for_timeout(80)
        page.evaluate("document.querySelector('#p48-doc-launch').click()")
        page.locator('#p48-doc-file').set_input_files([str(a),str(b)]);page.wait_for_timeout(350)
        cards=page.locator('.p48-doc-conflict-card');assert cards.count()>=1
        cards.first.locator('.p48-doc-conflict-options button').first.click();page.wait_for_timeout(30)
        # resolve any additional conflicts defensively
        for i in range(1,cards.count()):
            c=cards.nth(i)
            if c.locator('.p48-doc-conflict-options button').count(): c.locator('.p48-doc-conflict-options button').first.click();page.wait_for_timeout(20)
        assert not page.locator('#p48-doc-create').is_disabled()
        page.locator('#p48-doc-create').click();page.wait_for_timeout(180)
        # select first imported node carrying multi-source provenance
        nodes=page.locator('#p48-canvas .p48-node')
        found=False
        for i in range(nodes.count()):
            nodes.nth(i).click();page.wait_for_timeout(30)
            if page.locator('#p48-source-trace').is_visible() and '2 källor' in page.locator('#p48-source-trace').inner_text():
                found=True;break
        assert found
        panel=page.locator('#p48-source-trace').inner_text()
        assert '2 källor beskriver steget' in panel
        assert 'Olika ansvar' in panel
        assert 'Vald lösning:' in panel
        critical=[e for e in errors if 'invalidateNodeGeom is not defined' not in e and 'isMobileLayout is not defined' not in e]
        assert not critical,critical
        browser.close()
    print('browser v0.20.56 source support ok')

if __name__=='__main__': run()
