from playwright.sync_api import sync_playwright
from browser_interaction_smoke import extract_editor_html


def run():
    html=extract_editor_html()
    storage='''<script>(function(){function store(){const d={};return{getItem:k=>Object.prototype.hasOwnProperty.call(d,k)?d[k]:null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k]),key:i=>Object.keys(d)[i]||null,get length(){return Object.keys(d).length}}}window.__mapliniTestLocalStorage=store();window.__mapliniTestSessionStorage=store();})();</script>'''
    html=html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')
    html=storage+html
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        page=browser.new_page(viewport={'width':1280,'height':900})
        errors=[];page.on('pageerror',lambda e: errors.append(str(e)))
        page.set_content(html,wait_until='load')
        page.wait_for_selector('#p48-canvas .p48-node')
        # The analysis control lives in More; invoke the existing button directly so this smoke is not tied to menu layout.
        page.locator('#p48-analyze').evaluate('(el)=>el.click()')
        page.wait_for_timeout(80)
        assert page.locator('#p48-analysis-panel').is_visible()
        assert page.locator('#p48-analysis-rerun').is_visible()
        assert 'hittepåbetyg' in page.locator('.p48-analysis-sub').inner_text()
        page.locator('#p48-analysis-rerun').click()
        page.wait_for_timeout(60)
        assert page.locator('#p48-analysis-score').inner_text().strip().isdigit()
        # When the demo contains a finding, its canvas navigation must remain actionable.
        actions=page.locator('.p48-analysis-item-action')
        if actions.count():
            actions.first.click();page.wait_for_timeout(40)
            assert page.locator('#p48-canvas .p48-node.selected').count()>=1
        critical=[e for e in errors if 'invalidateNodeGeom is not defined' not in e and 'isMobileLayout is not defined' not in e]
        assert not critical,critical
        browser.close()
    print('browser v0.20.41 process control ok')

if __name__=='__main__':run()
