from pathlib import Path

APP = (Path(__file__).resolve().parents[1] / "app.py").read_text()

def test_version():
    assert 'APP_VERSION = "' in APP

def test_more_is_fixed_overlay_on_desktop():
    assert 'position:fixed!important;top:138px!important;right:18px!important;left:auto!important' in APP
    assert 'grid-template-columns:minmax(0,1fr) minmax(0,1fr)!important' in APP

def test_page_quick_stays_hidden_while_mapping():
    assert '.p48-page-quick{display:none!important}' in APP


def test_brand_is_compact_on_desktop():
    assert ".p48-brand{height:72px!important;min-height:72px!important" in APP
