"""Chromium smoke test for v0.20.34 mobile read/follow experience."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import importlib.util

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('browser_smoke', ROOT/'tests'/'browser_interaction_smoke.py')
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
html=mod.extract_editor_html()
storage_prelude = """<script>
(function(){
 function store(){const data={};return{getItem:k=>Object.prototype.hasOwnProperty.call(data,k)?data[k]:null,setItem:(k,v)=>{data[k]=String(v)},removeItem:k=>{delete data[k]},clear:()=>{for(const k of Object.keys(data))delete data[k]},key:i=>Object.keys(data)[i]||null,get length(){return Object.keys(data).length}}}
 window.__mapliniTestLocalStorage=store();window.__mapliniTestSessionStorage=store();
})();
</script>"""
html=html.replace("localStorage","window.__mapliniTestLocalStorage").replace("sessionStorage","window.__mapliniTestSessionStorage")
html=storage_prelude+html

with sync_playwright() as p:
    browser=p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox'])
    context=browser.new_context(viewport={"width":390,"height":844}, has_touch=True, is_mobile=True, device_scale_factor=2)
    page=context.new_page()
    page.set_content(html, wait_until='load')
    page.wait_for_selector('#p48-canvas .p48-node')
    page.wait_for_timeout(180)
    root=page.locator('#pk48')
    assert 'p48-read-mode' in (root.get_attribute('class') or '')
    assert page.locator('#p48-mobile-reader-bar').is_visible()
    assert not page.locator('#p48-mobile-bar').is_visible()
    assert page.locator('#p48-mobile-reader-follow').is_visible()
    assert page.locator('#p48-mobile-reader-fit').is_visible()
    # Read a step in the mobile bottom sheet.
    page.locator('#p48-canvas .p48-node').first.click()
    page.wait_for_timeout(30)
    assert page.locator('#p48-read-panel').is_visible()
    # Follow launches from the reader without exposing editing chrome.
    page.locator('#p48-mobile-reader-follow').click()
    page.wait_for_timeout(30)
    assert page.locator('#p48-walkthrough-panel').is_visible()
    assert 'p48-read-mode' in (root.get_attribute('class') or '')
    page.locator('#p48-walkthrough-close').click()
    page.wait_for_timeout(30)
    assert 'p48-read-mode' in (root.get_attribute('class') or '')
    # Explicit edit escape hatch restores mobile editing controls.
    if page.locator('#p48-mobile-reader-edit').is_visible():
        page.locator('#p48-mobile-reader-edit').click()
        page.wait_for_timeout(30)
        assert 'p48-read-mode' not in (root.get_attribute('class') or '')
        assert page.locator('#p48-mobile-bar').is_visible()
    context.close(); browser.close()
print('mobile read/follow browser smoke ok')
