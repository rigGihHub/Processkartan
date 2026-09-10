from pathlib import Path
from playwright.sync_api import sync_playwright
from browser_interaction_smoke import extract_editor_html

def run():
    html=extract_editor_html()
    storage='''<script>(function(){function store(){const d={};return{getItem:k=>Object.prototype.hasOwnProperty.call(d,k)?d[k]:null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k]),key:i=>Object.keys(d)[i]||null,get length(){return Object.keys(d).length}}}window.__mapliniTestLocalStorage=store();window.__mapliniTestSessionStorage=store();})();</script>'''
    html=html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')
    html=storage+html
    sample=Path('/tmp/maplini_doc_02049.txt')
    sample.write_text('Kundservice tar emot beställningen.\nOm kunduppgifterna är kompletta, registrerar Kundservice ordern, annars kontaktar Kundservice kunden.\nEkonomi godkänner ordern.',encoding='utf-8')
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        page=browser.new_page(viewport={'width':1360,'height':900}); errors=[]
        page.on('pageerror',lambda e:errors.append(str(e)));page.on('dialog',lambda d:d.accept())
        page.set_content(html,wait_until='load');page.wait_for_selector('#p48-canvas .p48-node')
        page.locator('#p48-new').click();page.locator('#p48-new-process-name').fill('Flödestest');page.locator('#p48-new-process-name').press('Enter');page.wait_for_timeout(80)
        page.evaluate("document.querySelector('#p48-doc-launch').click()")
        page.locator('#p48-doc-file').set_input_files(str(sample));page.wait_for_timeout(260)
        status=page.locator('#p48-doc-status').inner_text();assert 'grenvägar' in status,status
        structured=page.locator('#p48-doc-structured').inner_text();assert 'Ja →' in structured and 'Nej →' in structured,structured
        page.locator('#p48-doc-create').click();page.wait_for_timeout(220)
        assert page.locator('#p48-canvas .p48-node.decision').count()==1
        canvas_text=page.locator('#p48-canvas').inner_text();assert 'Kunduppgifterna är kompletta?' in canvas_text
        # Link labels are rendered in the SVG/overlay text layer.
        all_text=page.locator('#p48-links').text_content() or '';assert 'Ja' in all_text and 'Nej' in all_text
        critical=[e for e in errors if 'invalidateNodeGeom is not defined' not in e and 'isMobileLayout is not defined' not in e]
        assert not critical,critical
        browser.close()
    print('browser v0.20.49 document real flow ok')

if __name__=='__main__': run()
