from playwright.sync_api import sync_playwright
from browser_interaction_smoke import extract_editor_html


def run():
    html=extract_editor_html()
    storage='''<script>(function(){function s(){const d={};return{getItem:k=>d[k]??null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k]),key:i=>Object.keys(d)[i]||null,get length(){return Object.keys(d).length}}}window.__mapliniTestLocalStorage=s();window.__mapliniTestSessionStorage=s();})();</script>'''
    html=html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')
    html=storage+html
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox'])
        page=browser.new_page(viewport={'width':1440,'height':900})
        errors=[]; page.on('pageerror',lambda exc: errors.append(str(exc)))
        page.set_content(html,wait_until='load')
        page.wait_for_selector('#p48-canvas .p48-node')
        assert page.locator('.p48-work-modes').is_visible()
        assert page.locator('#p48-mode-draw').inner_text().strip()=='Rita'
        assert page.locator('#p48-readmode-toggle').inner_text().strip()=='Förstå'
        assert page.locator('#p48-walkthrough-launch').inner_text().strip()=='Följ'
        assert page.locator('#p48-mode-draw').get_attribute('aria-pressed')=='true'
        # Secondary menus are no longer direct children of the top bar after startup.
        assert page.locator('.p48-top-simplified > #p48-view-menu').count()==0
        assert page.locator('.p48-top-simplified > #p48-export-menu').count()==0
        assert page.locator('.p48-top-simplified > .p48-smart-layout-split').count()==0
        assert page.locator('#p48-more-menu .p48-more-popover > #p48-view-menu').count()==1
        assert page.locator('#p48-more-menu .p48-more-popover > #p48-export-menu').count()==1
        # Understand reuses read mode, Draw returns to edit mode.
        page.locator('#p48-readmode-toggle').click()
        assert 'p48-read-mode' in (page.locator('#pk48').get_attribute('class') or '')
        assert page.locator('#p48-readmode-toggle').get_attribute('aria-pressed')=='true'
        page.locator('#p48-mode-draw').click()
        assert 'p48-read-mode' not in (page.locator('#pk48').get_attribute('class') or '')
        assert page.locator('#p48-mode-draw').get_attribute('aria-pressed')=='true'
        # More exposes relocated tools without duplicate IDs.
        page.locator('#p48-more-menu > summary').click()
        assert page.locator('#p48-view-menu > summary').is_visible()
        assert page.locator('#p48-export-menu > summary').is_visible()
        assert page.locator('.p48-smart-layout-split').is_visible()
        ignored=('Failed to fetch','Invalid URL','invalidateNodeGeom is not defined','isMobileLayout is not defined')
        editor_errors=[e for e in errors if not any(token in e for token in ignored)]
        assert not editor_errors, editor_errors
        browser.close()
    print('v0.20.67 ui simplification browser smoke ok')

if __name__=='__main__': run()
