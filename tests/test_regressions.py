from pathlib import Path
import re
import subprocess
import sys

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
APP = (ROOT / "app.py").read_text(encoding="utf-8")
GOOGLE_UI = (ROOT / "maplini_google_ui.py").read_text(encoding="utf-8")
CONNECTOR_CORE = (ROOT / "maplini_connector_core.js").read_text(encoding="utf-8")


def _template():
    start = APP.index('html = r"""') + len('html = r"""')
    end = APP.index('"""', start)
    return APP[start:end]


def test_single_save_button_and_no_dead_cloud_save_reference():
    html = _template()
    soup = BeautifulSoup(html, "html.parser")
    assert len(soup.select("#p48-save")) == 1
    assert soup.select_one("#p48-cloud-save") is None
    assert "cloudSaveBtn" not in APP


def test_save_handler_preserves_local_and_cloud_semantics():
    assert "root.querySelector('#p48-save').addEventListener('click',async()=>{" in APP
    assert "if(ownerId())" in APP
    assert "await saveCurrentToCloud()" in APP
    assert "saveLocal(true);msg('Sparad lokalt')" in APP


def test_google_oauth_is_extracted_and_not_duplicated_in_app():
    assert APP.count("maplini_google_ui.render_google_export_ui(st, google_docs)") == 1
    assert "google_docs.exchange(st, st.query_params" not in APP
    assert GOOGLE_UI.count("google_docs.exchange(st, code)") == 1


def test_editor_dom_contract():
    soup = BeautifulSoup(_template(), "html.parser")
    body = soup.select_one(".p48-body")
    side = soup.select_one("aside.p48-side")
    main = soup.select_one("main#p48-scroll")
    controls = soup.select_one("#p48-controls")
    canvas = soup.select_one("#p48-canvas")
    assert all((body, side, main, controls, canvas))
    assert side.find_parent(class_="p48-body") is body
    assert main.find_parent(class_="p48-body") is body
    assert controls.find_parent("aside") is side
    assert canvas.find_parent(id="p48-scroll") is main


def test_mobile_contract_is_present():
    html = _template()
    assert 'id="p48-mobile-tools"' in html
    assert 'id="p48-mobile-backdrop"' in html
    assert "min-height:44px" in html
    assert "touch-action:pan-x pan-y" in html
    assert "safe-area-inset-bottom" in html
    assert "orientationchange" in html


def test_recent_canvas_features_do_not_regress():
    html = _template()
    for control in (
        'id="p48-link-color"',
        'id="p48-bg-type"',
        'id="p48-bg-pattern-color"',
        'id="p48-bg-density"',
        'id="p48-select-tool"',
        'id="p48-delete-selection"',
    ):
        assert control in html
    assert "selectedLinkIndices=new Set()" in APP
    assert "linksInSelectionRect" in APP
    assert "requestFullLinkRender(true)" in APP


def test_python_sources_compile():
    for file in (ROOT / "app.py", ROOT / "google_docs.py", ROOT / "maplini_google_ui.py"):
        result = subprocess.run([sys.executable, "-m", "py_compile", str(file)], capture_output=True, text=True)
        assert result.returncode == 0, result.stderr


def test_embedded_javascript_syntax_when_node_available():
    import shutil
    node = shutil.which("node")
    if not node:
        return
    match = re.search(r"<script>\s*(.*?)\s*</script>", APP, re.S)
    assert match
    check_file = ROOT / "tests" / "_embedded_check.js"
    try:
        check_file.write_text(match.group(1), encoding="utf-8")
        result = subprocess.run([node, "--check", str(check_file)], capture_output=True, text=True)
        assert result.returncode == 0, result.stderr
    finally:
        check_file.unlink(missing_ok=True)


def test_mobile_css_targets_real_dom_not_old_nonexistent_selectors():
    html = _template()
    soup = BeautifulSoup(html, "html.parser")
    assert soup.select_one(".p48-top") is not None
    assert soup.select_one(".p48-brand") is not None
    assert soup.select_one(".p48-logo-crop") is not None
    assert soup.select_one("#p48-name") is not None
    mobile = html[html.index("/* v0.10.11 mobile shell"):html.index(".p48-canvas-menu{")]
    assert ".p48-top{" in mobile
    assert ".p48-brand{" in mobile
    assert ".p48-logo-crop{" in mobile
    assert "#p48-name{" in mobile
    assert ".p48-toolbar{" not in mobile
    assert ".p48-header{" not in mobile
    assert "#p48-process-name" not in mobile

def test_mobile_toolbar_cannot_wrap_canvas_offscreen():
    html = _template()
    mobile = html[html.index("/* v0.10.11 mobile shell"):html.index(".p48-canvas-menu{")]
    assert "flex-wrap:nowrap!important" in mobile
    assert "overflow-x:auto!important" in mobile
    assert "#p48-mobile-tools{order:-30}" in mobile
    assert "height:820px!important" in mobile

def test_connector_core_is_extracted_and_wired():
    assert "MapliniConnectorCore" in CONNECTOR_CORE
    assert "function setStyle" in CONNECTOR_CORE
    assert "function removeSelected" in CONNECTOR_CORE
    assert '<script>__MAPLINI_CONNECTOR_CORE__</script>' in _template()
    assert 'html = html.replace("__MAPLINI_CONNECTOR_CORE__", _CONNECTOR_CORE_JS)' in APP
    assert "return MapliniConnectorCore.style(link)" in APP
    assert "MapliniConnectorCore.removeSelected" in APP

def test_connector_core_javascript_syntax_when_node_available():
    import shutil
    node = shutil.which("node")
    if not node:
        return
    result = subprocess.run([node, "--check", str(ROOT / "maplini_connector_core.js")], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
