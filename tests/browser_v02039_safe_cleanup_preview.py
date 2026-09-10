from playwright.sync_api import sync_playwright
from browser_interaction_smoke import extract_editor_html


def run():
    html=extract_editor_html()
    storage='''<script>(function(){function store(){const d={};return{getItem:k=>Object.prototype.hasOwnProperty.call(d,k)?d[k]:null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k]),key:i=>Object.keys(d)[i]||null,get length(){return Object.keys(d).length}}}window.__mapliniTestLocalStorage=store();window.__mapliniTestSessionStorage=store();})();</script>'''
    html=html.replace('localStorage','window.__mapliniTestLocalStorage').replace('sessionStorage','window.__mapliniTestSessionStorage')
    html=storage+html
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        page=browser.new_page(viewport={'width':1400,'height':900})
        errors=[];page.on('pageerror',lambda e: errors.append(str(e)))
        page.set_content(html,wait_until='load');page.wait_for_selector('#p48-canvas .p48-node')
        page.evaluate("()=>window.__mapliniTestState.clear()")
        page.evaluate("()=>window.__mapliniTestState.addNode('start',220,220)")
        page.evaluate("()=>window.__mapliniTestState.addNode('process',620,500)")
        page.evaluate("()=>window.__mapliniTestState.addNode('end',1040,180)")
        ns=page.evaluate("()=>window.__mapliniTestState.nodes()")
        a,b,c=[n['id'] for n in ns]
        page.evaluate("([a,b])=>window.__mapliniTestState.connect(a,b)",[a,b])
        page.evaluate("([a,b])=>window.__mapliniTestState.connect(a,b)",[b,c])
        before={n['id']:(n['x'],n['y']) for n in page.evaluate("()=>window.__mapliniTestState.nodes()")}
        undo_before=page.evaluate("()=>window.__mapliniTestState.undoCount()")
        assert page.evaluate("()=>window.__mapliniTestState.autoClean()") is True
        page.wait_for_timeout(100)
        assert page.locator('#p48-clean-preview-bar').is_visible()
        # Preview paints the DOM but persisted process coordinates remain untouched.
        during={n['id']:(n['x'],n['y']) for n in page.evaluate("()=>window.__mapliniTestState.nodes()")}
        assert during==before,(during,before)
        dom_xy=page.evaluate("(id)=>{const el=document.querySelector(`[data-id='${id}']`)||document.getElementById(id);return el?{x:parseFloat(el.style.left),y:parseFloat(el.style.top)}:null}",b)
        assert dom_xy and (round(dom_xy['x']),round(dom_xy['y']))!=tuple(map(round,before[b]))
        page.locator('#p48-clean-preview-cancel').click();page.wait_for_timeout(80)
        after_cancel={n['id']:(n['x'],n['y']) for n in page.evaluate("()=>window.__mapliniTestState.nodes()")}
        assert after_cancel==before
        assert page.evaluate("()=>window.__mapliniTestState.undoCount()") == undo_before
        # Apply commits one undoable layout change.
        assert page.evaluate("()=>window.__mapliniTestState.autoClean()") is True
        page.locator('#p48-clean-preview-apply').click();page.wait_for_timeout(100)
        after_apply={n['id']:(n['x'],n['y']) for n in page.evaluate("()=>window.__mapliniTestState.nodes()")}
        assert after_apply!=before
        assert page.evaluate("()=>window.__mapliniTestState.undoCount()") == undo_before+1
        assert not page.locator('#p48-clean-preview-bar').is_visible()
        browser.close()
    print('browser v0.20.39 safe cleanup preview ok')

if __name__=='__main__':run()
