from pathlib import Path
S=Path('app.py').read_text()
def test_version(): assert 'APP_VERSION = "0.20.71"' in S
def test_responsibility_ui():
    for x in ['p48-responsibility-toggle','p48-responsibility-bar','p48-responsibility-legend']: assert x in S
def test_overlay_not_layout_mutation():
    assert 'function setResponsibilityMode' in S and 'p48-responsibility-mode' in S
    assert 'responsibilityRole' in S and 'responsibleRole' in S
def test_handoff_semantics(): assert 'p48-link-handoff' in S and 'överlämningar' in S
