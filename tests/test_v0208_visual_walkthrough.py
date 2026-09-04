from pathlib import Path

APP = Path(__file__).resolve().parents[1] / 'app.py'
TEXT = APP.read_text(encoding='utf-8')


def test_version_is_0208():
    assert 'APP_VERSION = "0.20.34"' in TEXT


def test_walkthrough_has_distinct_canvas_states():
    for token in ('p48-walk-active', 'p48-walk-past', 'p48-walk-next', 'p48-walk-link-route'):
        assert token in TEXT


def test_walkthrough_route_visuals_follow_current_answer():
    assert 'function walkthroughVisualEdges(item)' in TEXT
    assert "if(route.mode==='auto'&&route.edge)return[route.edge]" in TEXT
    assert 'updateWalkthroughCanvasPosition(item);' in TEXT


def test_walkthrough_focus_is_smooth_without_auto_zoom():
    assert 'function focusWalkthroughNode(el)' in TEXT
    assert "behavior:'smooth'" in TEXT
    focus_block = TEXT.split('function focusWalkthroughNode(el)', 1)[1].split('function walkthroughVisualEdges', 1)[0]
    assert 'canvasScale=' not in focus_block
    assert 'setZoom' not in focus_block
