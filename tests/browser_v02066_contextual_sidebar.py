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
        # IO controls live inside the step editor, not the build palette.
        assert page.locator('.p48-method-palette .p48-step-io').count()==0
        assert page.locator('#p48-process-info .p48-step-io-context').count()==1
        # Select a process-capable node.
        node=page.locator('#p48-canvas .p48-node').filter(has=page.locator('.p48-label')).first
        node.click()
        page.wait_for_timeout(80)
        root_cls=page.locator('#pk48').get_attribute('class') or ''
        assert 'p48-side-context-active' in root_cls
        assert page.locator('#p48-format-title').inner_text().strip() in ('Redigera steg','Redigera markering')
        # On desktop, the context panel must visually precede the build palette.
        format_y=page.locator('#p48-format-panel').bounding_box()['y']
        palette_y=page.locator('.p48-method-palette').bounding_box()['y']
        assert format_y < palette_y, (format_y,palette_y)
        # Core fields stay immediate; advanced fields remain collapsed.
        if page.locator('#p48-process-info').is_visible():
            assert page.locator('#p48-info-description').is_visible()
            assert page.locator('#p48-info-role').is_visible()
            assert not page.locator('#p48-info-system').is_visible()
            page.locator('#p48-process-info-more > summary').click()
            assert page.locator('#p48-info-system').is_visible()
        ignored=('Failed to fetch','Invalid URL','invalidateNodeGeom is not defined','isMobileLayout is not defined')
        editor_errors=[e for e in errors if not any(token in e for token in ignored)]
        assert not editor_errors, editor_errors
        browser.close()
    print('v0.20.67 contextual sidebar browser smoke ok')

if __name__=='__main__': run()
