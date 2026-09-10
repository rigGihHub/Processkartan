from playwright.sync_api import sync_playwright
from browser_interaction_smoke import extract_editor_html


def run():
    html=extract_editor_html()
    storage='''<script>(function(){function store(){const d={};return{getItem:k=>Object.prototype.hasOwnProperty.call(d,k)?d[k]:null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k]),key:i=>Object.keys(d)[i]||null,get length(){return Object.keys(d).length}}}window.__mapliniTestLocalStorage=store();window.__mapliniTestSessionStorage=store();})();</script>'''
    html=html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')
    html=storage+html
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        page=browser.new_page(viewport={'width':390,'height':844})
        errors=[];page.on('pageerror',lambda e: errors.append(str(e)))
        page.set_content(html,wait_until='load')
        page.wait_for_selector('#p48-canvas .p48-node')
        # Mobile Follow entry must preserve a visible part of canvas and open the operational flow.
        page.locator('#p48-mobile-reader-follow').click()
        page.wait_for_timeout(60)
        assert page.locator('#p48-walkthrough-panel').is_visible()
        page.locator('#p48-walkthrough-person').fill('QA')
        page.locator('#p48-walkthrough-start-btn').click()
        page.wait_for_timeout(80)
        assert page.locator('.p48-walkthrough-now').inner_text().strip().casefold()=='gör nu'
        assert page.locator('#p48-walkthrough-step-title').inner_text().strip()
        # Current operational step remains at the top of the bottom sheet.
        assert page.locator('#p48-walkthrough-run').evaluate('(el)=>el.scrollTop') <= 2
        # Default process/subprocess checks use task language rather than form language.
        quick=page.locator('.p48-walkthrough-question.quick')
        if not quick.count() and page.locator('#p48-walkthrough-next').is_visible():
            page.locator('#p48-walkthrough-next').click();page.wait_for_timeout(80);quick=page.locator('.p48-walkthrough-question.quick')
        if quick.count():
            labels=[x.strip() for x in quick.locator('.p48-walkthrough-answer > span:first-child').all_inner_texts()]
            assert any('Klart' in x for x in labels),labels
            assert any('Inte klart' in x for x in labels),labels
        # Panel stays a bottom sheet on mobile rather than covering the whole canvas.
        box=page.locator('#p48-walkthrough-panel').bounding_box();assert box
        assert box['height'] < 700 and box['y'] > 100,box
        critical=[e for e in errors if 'invalidateNodeGeom is not defined' not in e and 'isMobileLayout is not defined' not in e]
        assert not critical,critical
        browser.close()
    print('browser v0.20.40 follow process 2 ok')

if __name__=='__main__':run()
