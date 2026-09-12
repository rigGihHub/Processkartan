from pathlib import Path
import sys
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(Path(__file__).resolve().parent))
from browser_interaction_smoke import extract_editor_html

def prepared_html():
    html=extract_editor_html()
    pre='''<script>(function(){function s(){const d={};return{getItem:k=>d[k]??null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k])}};window.__mapliniTestLocalStorage=s();window.__mapliniTestSessionStorage=s();})();</script>'''
    return pre+html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')

with sync_playwright() as p:
    b=p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox'])
    page=b.new_page(viewport={'width':1500,'height':900})
    page.set_content(prepared_html(), wait_until='domcontentloaded', timeout=20000)
    page.wait_for_selector('#pk48', timeout=10000)
    page.locator('#p48-more-menu > summary').click()
    page.wait_for_timeout(50)
    assert page.locator('.p48-more-intro').is_visible()
    assert page.locator('#p48-doc-launch').is_visible()
    assert page.locator('#p48-batch-launch').is_visible()
    assert page.locator('#p48-analyze').is_visible()
    assert page.locator('#p48-share').is_visible()
    assert page.locator('#p48-version-history-launch').is_visible()
    assert not page.locator('#p48-select-tool').is_visible()
    assert not page.locator('#p48-view-menu > summary').is_visible()
    assert not page.locator('#p48-deviation-launch').is_visible()
    page.locator('#p48-more-edit-group > summary').click()
    assert page.locator('#p48-select-tool').is_visible()
    page.locator('#p48-more-presentation-group > summary').click()
    assert page.locator('#p48-view-menu > summary').is_visible()
    assert page.locator('#p48-export-menu > summary').is_visible()
    box=page.locator('.p48-more-popover').bounding_box()
    assert box and box['width'] <= 380 and box['height'] < 760
    b.close()
print('browser_v02077_secondary_tools_cleanup PASS')
