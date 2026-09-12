from pathlib import Path
import sys
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(Path(__file__).resolve().parent))
from browser_interaction_smoke import extract_editor_html

html=extract_editor_html()
pre='''<script>(function(){function s(){const d={};return{getItem:k=>d[k]??null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k])}};window.__mapliniTestLocalStorage=s();window.__mapliniTestSessionStorage=s();})();</script>'''
html=html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')
html=pre+html
with sync_playwright() as p:
    b=p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox'])
    page=b.new_page(viewport={'width':1440,'height':900})
    page.set_content(html, wait_until='domcontentloaded', timeout=20000)
    page.wait_for_selector('#pk48', timeout=10000)
    assert 'p48-side-context-active' not in (page.locator('#pk48').get_attribute('class') or '')
    assert not page.locator('#p48-format-panel').is_visible()
    assert page.locator('.p48-method-palette').is_visible()
    assert page.locator('.p48-item-core').count() == 3
    more=page.locator('#p48-palette-more')
    assert more.is_visible()
    assert not more.evaluate('(el)=>el.open')
    more.locator('summary').click()
    assert more.evaluate('(el)=>el.open')
    assert page.locator('#p48-palette-more .p48-item').count() == 6
    # select an actual node; inspector must return and editing context must become active
    page.locator('#p48-canvas .p48-node').first.click()
    page.wait_for_timeout(50)
    assert 'p48-side-context-active' in (page.locator('#pk48').get_attribute('class') or '')
    assert page.locator('#p48-format-panel').is_visible()
    b.close()
print('browser_v02075_calm_neutral_sidebar PASS')
