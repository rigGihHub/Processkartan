from pathlib import Path
APP=Path(__file__).resolve().parents[1].joinpath("app.py").read_text()

def test_version():
    assert 'APP_VERSION = "' in APP

def test_find_ui_and_fields():
    assert 'id="p48-find-menu"' in APP
    assert 'id="p48-find-input"' in APP
    assert 'Sök steg, ansvar, system eller dokument' in APP

def test_find_searches_process_metadata_and_jumps():
    assert 'function processFindHaystack' in APP
    assert 'info.responsibleRole' in APP and 'info.system' in APP
    assert 'function jumpToProcessFindResult' in APP
    assert 'ensureNodeVisible(item.el)' in APP
    assert "String(e.key).toLowerCase()!=='f'" in APP
