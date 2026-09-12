from pathlib import Path
from playwright.sync_api import sync_playwright
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from browser_interaction_smoke import extract_editor_html

html=extract_editor_html()
store='''<script>(function(){function store(){const data={};return{getItem:k=>Object.prototype.hasOwnProperty.call(data,k)?data[k]:null,setItem:(k,v)=>{data[k]=String(v)},removeItem:k=>{delete data[k]},clear:()=>{},key:i=>Object.keys(data)[i]||null,get length(){return Object.keys(data).length}}}window.__mapliniTestLocalStorage=store();window.__mapliniTestSessionStorage=store();})();</script>'''
html=html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')
html=store+html
with sync_playwright() as p:
    b=p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox'])
    page=b.new_page(viewport={'width':1500,'height':1000})
    errors=[]; page.on('pageerror',lambda e:errors.append(str(e)))
    page.set_content(html,wait_until='load'); page.wait_for_selector('#p48-canvas .p48-node')
    assert page.locator('#p48-scroll').evaluate("e=>getComputedStyle(e).backgroundColor")=='rgb(242, 245, 247)'
    process=page.locator('#p48-canvas .p48-node.process').first
    assert process.count()==1
    assert process.evaluate("e=>getComputedStyle(e).fontSize")=='13px'
    start=page.locator('#p48-canvas .p48-node.start').first
    assert start.evaluate("e=>getComputedStyle(e).minHeight")=='52px'
    assert start.evaluate("e=>getComputedStyle(e).boxShadow")!='none'
    process.click(); page.wait_for_timeout(30)
    assert process.evaluate("e=>getComputedStyle(e).outlineOffset")=='3px'
    b.close()
print('v0.20.68 canvas visual hierarchy browser smoke ok')
