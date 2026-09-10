"""Chromium geometry smoke for v0.20.36 mobile canvas fit/readability."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import importlib.util
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('browser_smoke',ROOT/'tests'/'browser_interaction_smoke.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
html=mod.extract_editor_html()
storage_prelude="""<script>(function(){function store(){const data={};return{getItem:k=>Object.prototype.hasOwnProperty.call(data,k)?data[k]:null,setItem:(k,v)=>{data[k]=String(v)},removeItem:k=>{delete data[k]},clear:()=>{for(const k of Object.keys(data))delete data[k]},key:i=>Object.keys(data)[i]||null,get length(){return Object.keys(data).length}}}window.__mapliniTestLocalStorage=store();window.__mapliniTestSessionStorage=store();})();</script>"""
html=html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')
html=storage_prelude+html
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    for width in (360,390,430):
        context=browser.new_context(viewport={'width':width,'height':844},has_touch=True,is_mobile=True,device_scale_factor=2)
        page=context.new_page();page.set_content(html,wait_until='load');page.wait_for_selector('#p48-canvas .p48-node');page.wait_for_timeout(240)
        assert 'p48-read-mode' in (page.locator('#pk48').get_attribute('class') or '')
        scale=float(page.locator('#p48-canvas').evaluate("el=>getComputedStyle(el).getPropertyValue('--p48-canvas-scale')||el.style.getPropertyValue('--p48-canvas-scale')||'1'"))
        assert scale>=.74,(width,scale)
        bar_box=page.locator('#p48-mobile-reader-bar').bounding_box();assert bar_box and bar_box['height']<=54,(width,bar_box)
        scroll_box=page.locator('#p48-scroll').bounding_box();assert scroll_box and 420<=scroll_box['height']<=545,(width,scroll_box)
        first=page.locator('#p48-canvas .p48-node').first.bounding_box();assert first
        assert first['x']<width-20 and first['x']+first['width']>8,(width,first)
        assert first['width']>=85,(width,first)
        context.close()
    browser.close()
print('mobile canvas fit/readability browser smoke ok')
