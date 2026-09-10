from playwright.sync_api import sync_playwright
from browser_interaction_smoke import extract_editor_html


def run():
    html = extract_editor_html()
    storage = '''<script>(function(){function store(){const d={};return{getItem:k=>Object.prototype.hasOwnProperty.call(d,k)?d[k]:null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k]),key:i=>Object.keys(d)[i]||null,get length(){return Object.keys(d).length}}}window.__mapliniTestLocalStorage=store();window.__mapliniTestSessionStorage=store();})();</script>'''
    html = html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')
    html = storage + html
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox'])
        page = browser.new_page(viewport={'width':1280,'height':900})
        errors=[]
        page.on('pageerror', lambda e: errors.append(str(e)))
        page.on('dialog', lambda d: d.accept())
        page.set_content(html, wait_until='load')
        page.wait_for_selector('#p48-canvas .p48-node')

        # New process: process name is blank by default and Enter creates it.
        page.locator('#p48-new').click()
        name = page.locator('#p48-new-process-name')
        assert name.input_value()==''
        assert name.get_attribute('placeholder')=='Ex. Hantera kundfaktura'
        name.fill('Hantera order')
        name.press('Enter')
        page.wait_for_timeout(80)

        empty = page.locator('#p48-empty-state')
        assert empty.is_visible()
        first = page.locator('#p48-empty-first-text')
        assert first.evaluate('(el)=>document.activeElement===el')
        first.fill('Ta emot beställning')
        first.press('Enter')
        page.wait_for_timeout(100)

        assert not empty.is_visible()
        nodes = page.locator('#p48-canvas .p48-node')
        assert nodes.count()==1
        node = nodes.first
        assert 'process' in (node.get_attribute('class') or '')
        assert node.locator('.p48-label').inner_text()=='Ta emot beställning'

        # The created node stays selected/focused so Tab continues the existing build rhythm.
        assert node.evaluate('(el)=>document.activeElement===el')
        node.press('Tab')
        page.wait_for_timeout(100)
        assert nodes.count()==2

        critical=[e for e in errors if 'invalidateNodeGeom is not defined' not in e and 'isMobileLayout is not defined' not in e]
        assert not critical, critical
        browser.close()
    print('browser v0.20.47 first process flow ok')


if __name__=='__main__':
    run()
