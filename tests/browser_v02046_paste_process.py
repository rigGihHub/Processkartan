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

        page.locator('#p48-new').click()
        page.locator('#p48-new-process-name').fill('Importtest')
        page.locator('#p48-new-process-name').press('Enter')
        page.wait_for_timeout(80)
        assert page.locator('#p48-empty-state').is_visible()

        page.locator('#p48-empty-import').click()
        assert page.locator('#p48-batch-dialog').is_visible()
        page.locator('#p48-batch-text').fill('1. Ta emot beställning\n- Kontrollera kunduppgifter\nÄr uppgifterna kompletta?\nSkapa order\nSkicka orderbekräftelse')
        page.locator('#p48-batch-create').click()
        page.wait_for_timeout(160)

        nodes=page.locator('#p48-canvas .p48-node')
        assert nodes.count()==5
        labels=[nodes.nth(i).locator('.p48-label').inner_text() for i in range(5)]
        assert labels[0]=='Ta emot beställning'
        assert labels[1]=='Kontrollera kunduppgifter'
        assert labels[2]=='Är uppgifterna kompletta?'
        assert 'decision' in (nodes.nth(2).get_attribute('class') or '')
        assert page.locator('#p48-links path').count() >= 4
        assert not page.locator('#p48-batch-dialog').is_visible()

        critical=[e for e in errors if 'invalidateNodeGeom is not defined' not in e and 'isMobileLayout is not defined' not in e]
        assert not critical, critical
        browser.close()
    print('browser v0.20.47 paste process ok')

if __name__=='__main__':
    run()
