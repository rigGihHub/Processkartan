from pathlib import Path

APP = Path('app.py').read_text(encoding='utf-8')

def test_version():
    assert 'APP_VERSION = "0.20.34"' in APP

def test_overview_is_opt_in_and_has_navigation_contract():
    assert 'id="p48-overview-toggle"' in APP
    assert 'id="p48-overview" class="p48-overview" hidden' in APP
    assert 'id="p48-overview-stage"' in APP
    assert 'id="p48-overview-viewport"' in APP
    assert 'Klicka på ett steg för att hoppa dit' in APP

def test_overview_uses_existing_node_geometry_and_does_not_mutate_process_data():
    assert 'function processOverviewBounds()' in APP
    assert 'function renderProcessOverview()' in APP
    assert 'selectedNodeRects()' in APP
    assert "b.dataset.overviewNodeId=d.id" in APP
    assert 'centerOverviewOnLogical' in APP
    assert "select(node.el);centerOverviewOnLogical" in APP

def test_overview_tracks_scroll_zoom_and_process_changes():
    assert "scroll.addEventListener('scroll',()=>{\n  updateOverviewViewport();" in APP
    assert 'scheduleOverviewRefresh();\n  return value;' in APP
    assert 'scheduleOverviewRefresh();\n    return st;' in APP
    assert 'clearRuntimeError();scheduleOverviewRefresh();' in APP

def test_overview_not_for_mobile_editor_surface():
    assert '@media(max-width:700px){#p48-overview-toggle,.p48-overview{display:none!important}}' in APP
