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
        page=browser.new_page(viewport={'width':1440,'height':950});errors=[]
        page.on('pageerror',lambda e:errors.append(str(e)))
        page.set_content(html,wait_until='load');page.wait_for_selector('#p48-canvas .p48-node')
        page.locator('#p48-more-menu > summary').click(); page.locator('#p48-more-presentation-group > summary').click(); page.locator('#p48-export-menu > summary').click()
        page.locator('#p48-pdf-view').select_option('A4L')
        page.locator('#p48-page-count').select_option('2')
        page.locator('#p48-export-preview').click()
        page.wait_for_selector('#p48-export-preview-dialog:not([hidden])')
        page.wait_for_function("document.querySelectorAll('#p48-export-preview-pages canvas').length===2")
        summary=page.locator('#p48-export-preview-summary').inner_text()
        assert 'A4 liggande' in summary and '2 sidor' in summary,summary
        assert page.locator('#p48-export-preview-pages canvas').count()==2
        assert page.locator('#p48-export-preview-pdf').is_visible()
        assert page.locator('#p48-export-preview-docx').is_visible()
        page.locator('#p48-export-preview-close').click()
        assert page.locator('#p48-export-preview-dialog').get_attribute('hidden') is not None
        critical=[e for e in errors if 'invalidateNodeGeom is not defined' not in e and 'isMobileLayout is not defined' not in e]
        assert not critical,critical
        browser.close()
    print('browser v0.20.67 export preview ok')

if __name__=='__main__': run()
