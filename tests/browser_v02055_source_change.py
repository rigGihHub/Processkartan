from pathlib import Path
from playwright.sync_api import sync_playwright
from browser_interaction_smoke import extract_editor_html

def run():
    html=extract_editor_html();storage='''<script>(function(){function store(){const d={};return{getItem:k=>Object.prototype.hasOwnProperty.call(d,k)?d[k]:null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k]),key:i=>Object.keys(d)[i]||null,get length(){return Object.keys(d).length}}}window.__mapliniTestLocalStorage=store();window.__mapliniTestSessionStorage=store();})();</script>'''
    html=storage+html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')
    newfile=Path('/tmp/maplini_new_source.txt');newfile.write_text('Bolaget meddelade en kraftig prishöjning. Därför minskade efterfrågan kraftigt. Företaget lanserade därefter en billigare tjänst.',encoding='utf-8')
    with sync_playwright() as p:
        b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':900});errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.on('dialog',lambda d:d.accept());page.set_content(html,wait_until='load');page.wait_for_selector('#p48-canvas .p48-node')
        page.locator('#p48-new').click();page.locator('#p48-new-process-name').fill('Ändringskontroll');page.locator('#p48-new-process-name').press('Enter');page.wait_for_timeout(60)
        page.evaluate("document.querySelector('#p48-doc-launch').click()")
        page.locator('#p48-source-text').fill('Bolaget meddelade en kraftig prishöjning. Därför föll efterfrågan. Företaget lanserade därefter en billigare tjänst.');page.locator('#p48-source-text-run').click();page.wait_for_timeout(120);page.locator('#p48-doc-create').click();page.wait_for_timeout(100)
        first=page.locator('#p48-canvas .p48-node').first;first.locator('.p48-label').click();page.wait_for_timeout(50);assert page.locator('#p48-source-change-btn').is_visible()
        page.locator('#p48-source-change-file').set_input_files(str(newfile));page.wait_for_timeout(250)
        txt=page.locator('#p48-source-change-results').inner_text();assert 'Processen är inte ändrad' in txt,txt;assert ('ändrade' in txt or 'saknas' in txt),txt
        critical=[e for e in errors if 'invalidateNodeGeom is not defined' not in e and 'isMobileLayout is not defined' not in e];assert not critical,critical;b.close()
    print('browser v0.20.55 source change ok')
if __name__=='__main__':run()
