from playwright.sync_api import sync_playwright

from browser_interaction_smoke import extract_editor_html


def storage_safe_html():
    html = extract_editor_html()
    storage = """<script>(function(){function s(){const d={};return{getItem:k=>d[k]??null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>Object.keys(d).forEach(k=>delete d[k]),key:i=>Object.keys(d)[i]||null,get length(){return Object.keys(d).length}}}window.__mapliniTestLocalStorage=s();window.__mapliniTestSessionStorage=s();})();</script>"""
    return storage + html.replace("localStorage", "window.__mapliniTestLocalStorage").replace("sessionStorage", "window.__mapliniTestSessionStorage")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True, executable_path="/usr/bin/chromium", args=["--no-sandbox"])
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.set_content(storage_safe_html(), wait_until="load")
    page.wait_for_selector("#p48-canvas .p48-node")

    plus = page.locator(".p48-next-step-btn").first
    style = plus.evaluate("""el => { const s=getComputedStyle(el); return {width:s.width,height:s.height,background:s.backgroundColor,border:s.borderTopWidth,opacity:s.opacity} }""")
    assert style["width"] == "24px", style
    assert style["height"] == "24px", style
    assert style["background"] == "rgba(255, 255, 255, 0.96)", style
    assert style["border"] == "1px", style
    assert float(style["opacity"]) < 0.8, style
    assert page.locator("#p48-pdf-view").input_value() == "off"

    page.locator("#p48-canvas .p48-node").nth(1).click()
    summary = page.locator("#p48-step-understanding")
    assert not summary.is_visible()
    assert summary.locator(".p48-step-understanding-row").count() >= 5
    assert summary.locator(".p48-step-understanding-head").inner_text() == "Stegets sammanhang"

    browser.close()

print("browser_v02082_canvas_calm PASS")
