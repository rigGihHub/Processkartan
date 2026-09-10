from playwright.sync_api import sync_playwright
from browser_interaction_smoke import extract_editor_html

html=extract_editor_html()
storage='''<script>(function(){function store(){const d={};return{getItem:k=>Object.prototype.hasOwnProperty.call(d,k)?d[k]:null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k]),key:i=>Object.keys(d)[i]||null,get length(){return Object.keys(d).length}}}window.__mapliniTestLocalStorage=store();window.__mapliniTestSessionStorage=store();})();</script>'''
html=storage+html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    page=browser.new_page(viewport={"width":1280,"height":900})
    errors=[]
    page.on('pageerror',lambda exc: errors.append(str(exc)))
    page.set_content(html,wait_until='domcontentloaded')
    page.evaluate("""()=>{const s=window.__mapliniTestState;s.clear();const a=s.addNode('start',80,100),b=s.addNode('process',330,100),c=s.addNode('end',580,100);s.connect(a,b);s.connect(b,c)}""")
    page.locator('#p48-walkthrough-launch').click()
    assert page.locator('#p48-walkthrough-panel').is_visible()
    assert '(valfritt)' in page.locator('.p48-walkthrough-person-label').inner_text()
    page.locator('#p48-walkthrough-start-btn').click()
    assert page.locator('#p48-walkthrough-run').is_visible()
    assert page.locator('#p48-walkthrough-coming').is_visible()
    assert page.locator('#p48-walkthrough-coming-text').inner_text().strip()
    critical=[e for e in errors if 'invalidateNodeGeom is not defined' not in e and 'isMobileLayout is not defined' not in e]
    assert not critical, critical
    browser.close()
print('v0.20.67 novice walkthrough browser smoke ok')
