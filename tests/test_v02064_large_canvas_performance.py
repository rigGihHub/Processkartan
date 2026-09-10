from pathlib import Path
SRC=Path('app.py').read_text(encoding='utf-8')
def test_version(): assert 'APP_VERSION = "0.20.71"' in SRC
def test_core_injected():
    assert '__MAPLINI_PERFORMANCE_CORE__' in SRC
    assert 'MapliniPerformanceCore.policy(nodes.size,links.length)' in SRC
def test_large_map_reduces_decorative_paint():
    assert '#pk48.p48-large-map .p48-node{box-shadow:none;will-change:auto}' in SRC
    assert '#pk48.p48-large-map #p48-canvas{background-image:none}' in SRC
def test_mode_refreshes_with_node_count(): assert 'refreshLargeMapMode();' in SRC
