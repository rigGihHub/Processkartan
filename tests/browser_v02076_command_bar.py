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
    for width in (1500, 1120):
        page=b.new_page(viewport={'width':width,'height':900})
        page.set_content(prepared_html(), wait_until='domcontentloaded', timeout=20000)
        page.wait_for_selector('#pk48', timeout=10000)
        top=page.locator('.p48-top-simplified').bounding_box()
        proc=page.locator('.p48-process-cluster').bounding_box()
        modes=page.locator('.p48-work-modes').bounding_box()
        utils=page.locator('.p48-top-utilities').bounding_box()
        assert top and proc and modes and utils
        assert proc['x']+proc['width'] <= modes['x']+2
        assert modes['x']+modes['width'] <= utils['x']+2
        assert abs((modes['y']+modes['height']/2)-(proc['y']+proc['height']/2)) < 5
        assert abs((utils['y']+utils['height']/2)-(proc['y']+proc['height']/2)) < 5
        assert page.locator('#p48-new').is_visible()
        assert page.locator('#p48-save').is_visible()
        # Search and More are icon-like utilities on desktop, but remain accessible by title/aria.
        assert page.locator('#p48-find-menu > summary').is_visible()
        assert page.locator('#p48-more-menu > summary').is_visible()
        page.close()
    b.close()
print('browser_v02076_command_bar PASS')
