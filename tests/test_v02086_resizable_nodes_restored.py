from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APP = (ROOT / "app.py").read_text(encoding="utf-8")
CANVAS_CORE = (ROOT / "maplini_canvas_core.js").read_text(encoding="utf-8")


def test_activity_width_is_not_locked_by_css():
    assert 'APP_VERSION = "0.20.93"' in APP
    assert "#pk48 .p48-node.process{min-width:200px!important}" not in APP


def test_existing_resize_engine_still_allows_compact_nodes():
    assert "w=clamp(w,120,700)" in CANVAS_CORE
    assert "el.style.width=box.width+'px'" in APP
