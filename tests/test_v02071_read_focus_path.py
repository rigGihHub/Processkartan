from pathlib import Path
SRC=Path("app.py").read_text(encoding="utf-8")

def test_version(): assert 'APP_VERSION = "' in SRC
def test_focus_path_is_read_mode_only():
    assert 'p48-read-focus-active' in SRC
    assert 'readMode&&selectedId' in SRC
def test_focus_uses_real_adjacency():
    assert "if(to===String(selectedId)){prev.add(from);activeLinks.add(index)}" in SRC
    assert "if(from===String(selectedId)){next.add(to);activeLinks.add(index)}" in SRC
def test_focus_never_changes_process_data():
    body=SRC.split('function refreshReadFocusPath(){',1)[1].split('function jumpReadAnchor',1)[0]
    assert 'updateData' not in body and 'save' not in body
