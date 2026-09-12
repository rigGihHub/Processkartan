from pathlib import Path
SRC=Path("app.py").read_text()

def test_version():
    assert 'APP_VERSION = "0.20.80"' in SRC

def test_canvas_hierarchy_css():
    assert 'v0.20.68 – canvas visual hierarchy' in SRC
    assert '.p48-scroll{background:#f2f5f7}' in SRC
    assert '.p48-node.start,.p48-node.end{' in SRC
    assert '.p48-node.decision .p48-label{font-size:13px' in SRC
    assert '#p48-links .p48-link-visible.p48-flow-main{opacity:.9;stroke-width:2.35px}' in SRC
    assert '.p48-link-label text{font:780 10.5px/1 Inter' in SRC
    assert 'outline-offset:4px!important' in SRC
