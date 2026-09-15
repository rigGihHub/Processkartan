from pathlib import Path
SRC=Path("app.py").read_text()

def test_version(): assert 'APP_VERSION = "' in SRC
def test_single_selection_toolbar_is_removed(): assert '.p48-node-quick[data-mode="single"]{display:none!important}' in SRC
def test_desktop_header_is_single_row():
    assert '.p48-brand{position:absolute!important' in SRC
    assert 'padding:6px 10px 6px 246px!important' in SRC
def test_contextual_sidebar_has_editor_hierarchy():
    assert '#pk48.p48-side-context-active #p48-format-panel{border:0!important' in SRC
    assert 'grid-template-columns:54px minmax(0,1fr)!important' in SRC
