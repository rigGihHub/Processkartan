from pathlib import Path
APP = (Path(__file__).resolve().parents[1] / "app.py").read_text(encoding="utf-8")

def test_v0142_contract():
    assert 'APP_VERSION = "0.16.4"' in APP
    assert "syncDesktopViewportHeight" in APP
    assert "--p48-desktop-body-h" in APP
    assert "components.html(html, height=920, scrolling=False)" in APP

def test_smart_layout_recenters_connectors():
    assert "setLinkStyle(i,{routing:'orthogonal',anchorMode:'auto',viaX:null,viaY:null,freeDx:0,freeDy:0})" in APP
    assert "Smart Layout owns geometry" in APP

def test_typography_controls_are_grouped():
    start = APP.index('<div class="p48-text-format-block p48-node-only">')
    end = APP.index('</div>', APP.index('id="p48-font-all"', start)) + len('</div>')
    block = APP[start:end]
    for token in ['id="p48-font"','id="p48-size"','id="p48-bold"','id="p48-italic"','id="p48-under"','data-text-align="left"','data-text-align="center"','data-text-align="right"']:
        assert token in block

def test_node_styles_have_stronger_visual_differences():
    assert '.p48-node.p48-style-3d{box-shadow:0 9px 0' in APP
    assert '.p48-node.p48-style-raised{box-shadow:0 18px 38px' in APP
    assert 'backdrop-filter:blur(10px) saturate(1.18)' in APP
    assert '.p48-node.p48-style-flat{transform:none;box-shadow:none!important;border-radius:4px!important}' in APP
