from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
APP = (ROOT / "app.py").read_text(encoding="utf-8")

def template():
    start = APP.index('html = r"""') + len('html = r"""')
    end = APP.index('"""', start)
    return APP[start:end]

def test_desktop_dom_has_two_column_editor_contract():
    soup = BeautifulSoup(template(), "html.parser")
    body = soup.select_one(".p48-body")
    side = soup.select_one("aside.p48-side")
    scroll = soup.select_one("main#p48-scroll")
    controls = soup.select_one("#p48-controls")
    canvas = soup.select_one("#p48-canvas")
    assert all((body, side, scroll, controls, canvas))
    assert side.find_parent(class_="p48-body") is body
    assert scroll.find_parent(class_="p48-body") is body
    assert controls.find_parent("aside") is side
    assert canvas.find_parent(id="p48-scroll") is scroll

def test_desktop_guard_protects_sidebar_and_canvas_geometry():
    html = template()
    start = html.index("/* v0.10.25 desktop regression guard */")
    end = html.index("/* visible version */", start)
    guard = html[start:end]
    assert "grid-template-columns:220px minmax(0,1fr)!important" in guard
    assert "height:900px!important" in guard
    assert "transform:none!important" in guard
    assert "visibility:visible!important" in guard
    assert "overflow:auto!important" in guard
    assert ".p48-mobile-tools-btn,.p48-mobile-backdrop{display:none!important}" in guard

def test_dead_outer_iframe_layout_css_is_removed():
    # Editor selectors belong inside components.html, not the outer Streamlit page CSS.
    prefix = APP[:APP.index('html = r"""')]
    assert "v0.8.5: permanent horizontal navigation for wide process maps" not in prefix
    assert ".p48-main,.p48-stage,.p48-canvas-wrap" not in prefix
    assert "#p48-canvas{min-width:2400px}" not in prefix

def test_desktop_resize_cleanup_keeps_canvas_interaction_state():
    assert "const mobile=isMobileLayout()" in APP
    assert "if(!mobile){" in APP
    assert "setMobileTools(false)" in APP
    assert "canvas.classList.toggle('p48-selection-mode',selectionMode)" in APP
