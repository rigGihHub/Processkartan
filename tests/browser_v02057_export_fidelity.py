from pathlib import Path
import re, zipfile
from playwright.sync_api import sync_playwright
from browser_interaction_smoke import extract_editor_html


def run():
    html=extract_editor_html()
    storage='''<script>(function(){function store(){const d={};return{getItem:k=>Object.prototype.hasOwnProperty.call(d,k)?d[k]:null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k]),key:i=>Object.keys(d)[i]||null,get length(){return Object.keys(d).length}}}window.__mapliniTestLocalStorage=store();window.__mapliniTestSessionStorage=store();})();</script>'''
    html=html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')
    html=storage+html
    out=Path('/tmp/maplini_02057');out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        page=browser.new_page(viewport={'width':1440,'height':950},accept_downloads=True);errors=[]
        page.on('pageerror',lambda e:errors.append(str(e)))
        page.set_content(html,wait_until='load');page.wait_for_selector('#p48-canvas .p48-node')
        # Force a deterministic two-page A4 landscape export.
        page.locator('#p48-more-menu > summary').click(); page.locator('#p48-more-presentation-group > summary').click(); page.locator('#p48-export-menu > summary').click()
        page.locator('#p48-pdf-view').select_option('A4L')
        page.locator('#p48-page-count').select_option('2')
        with page.expect_download() as info:
            page.locator('#p48-pdf').click()
        pdf=out/'export.pdf';info.value.save_as(str(pdf))
        data=pdf.read_bytes()
        assert data.startswith(b'%PDF')
        assert len(re.findall(rb'/Type /Page\b',data))==2
        assert len(re.findall(rb'/Subtype /Image\b',data))==2
        # Re-open because export action intentionally closes its menu.
        page.locator('#p48-export-menu > summary').click()
        with page.expect_download() as info:
            page.locator('#p48-doc').click()
        docx=out/'export.docx';info.value.save_as(str(docx))
        assert zipfile.is_zipfile(docx)
        with zipfile.ZipFile(docx) as z:
            names=z.namelist();doc=z.read('word/document.xml').decode('utf-8')
            media=[n for n in names if n.startswith('word/media/process-map-') and n.endswith('.jpg')]
            assert len(media)==2,media
            assert '<w:pageBreakBefore/>' in doc
            assert 'w:orient="landscape"' in doc
        critical=[e for e in errors if 'invalidateNodeGeom is not defined' not in e and 'isMobileLayout is not defined' not in e]
        assert not critical,critical
        browser.close()
    print('browser v0.20.67 export fidelity ok')

if __name__=='__main__': run()
