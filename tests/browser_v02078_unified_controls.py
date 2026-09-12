from pathlib import Path
import sys
from playwright.sync_api import sync_playwright
sys.path.insert(0,str(Path(__file__).resolve().parent))
from browser_interaction_smoke import extract_editor_html

def prepared_html():
    html=extract_editor_html()
    pre="<script>(function(){function s(){const d={};return{getItem:k=>d[k]??null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k])}};window.__mapliniTestLocalStorage=s();window.__mapliniTestSessionStorage=s();})();</script>"
    return pre+html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')

with sync_playwright() as p:
    b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    page=b.new_page(viewport={'width':1500,'height':900})
    page.set_content(prepared_html(),wait_until='domcontentloaded',timeout=20000)
    page.wait_for_selector('#pk48',timeout=10000)
    new=page.locator('#p48-new'); save=page.locator('#p48-save')
    assert new.evaluate("e=>getComputedStyle(e).borderRadius") == save.evaluate("e=>getComputedStyle(e).borderRadius")
    page.locator('#p48-name').focus()
    style=page.locator('#p48-name').evaluate("e=>({outline:getComputedStyle(e).outlineStyle,shadow:getComputedStyle(e).boxShadow})")
    assert style['outline'] == 'none'
    assert style['shadow'] != 'none'
    page.locator('#p48-more-menu > summary').click()
    assert page.locator('.p48-more-intro').is_visible()
    b.close()
print('browser_v02078_unified_controls PASS')
