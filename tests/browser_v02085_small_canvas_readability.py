from playwright.sync_api import sync_playwright

from browser_v02082_canvas_calm import storage_safe_html


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True, executable_path="/usr/bin/chromium", args=["--no-sandbox"])
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.set_content(storage_safe_html(), wait_until="load")
    page.wait_for_selector("#p48-canvas .p48-node.process")

    process = page.locator("#p48-canvas .p48-node.process").first
    style = process.evaluate("el => { const node=getComputedStyle(el),label=getComputedStyle(el.querySelector('.p48-label')); return {width:node.width,font:label.fontFamily,wordBreak:label.wordBreak,overflowWrap:label.overflowWrap} }")
    assert style["wordBreak"] == "normal", style
    assert style["overflowWrap"] == "break-word", style
    assert "sans-serif" in style["font"], style

    assert page.locator("#pk48").evaluate("el => el.classList.contains('p48-small-map')")
    assert page.locator("#p48-hnav").evaluate("el => getComputedStyle(el).display") == "none"
    browser.close()

print("browser_v02085_small_canvas_readability PASS")
