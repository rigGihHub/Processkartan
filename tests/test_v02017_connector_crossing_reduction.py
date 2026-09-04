from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = (ROOT / "app.py").read_text(encoding="utf-8")
CORE = (ROOT / "maplini_connector_core.js").read_text(encoding="utf-8")


def test_release_version():
    assert 'APP_VERSION = "0.20.34"' in APP


def test_auto_routing_receives_existing_connector_segments():
    assert "function automaticRoutingSegments(excludeLink)" in APP
    assert "useCrossingAvoidance?(Array.isArray(routingSegments)?routingSegments:automaticRoutingSegments(link)):[]" in APP
    assert "crossingSegments,{sourceId:String(link[0]),targetId:String(link[1])}" in APP


def test_connector_core_scores_real_crossings_below_node_collisions():
    assert "function routeCrossingCount(" in CORE
    assert "crossings*420" in CORE
    assert "hits*100000" in CORE
    assert "if(sourceId&&(ss===sourceId||tt===sourceId))continue" in CORE


def test_crossing_routes_add_corridor_candidates_from_existing_segments():
    assert "for(const s of segs)" in CORE
    assert "xs.push(x1-28,x1+28,x2-28,x2+28)" in CORE
    assert "ys.push(y1-28,y1+28,y2-28,y2+28)" in CORE
    assert "compactCorridors=(values,center,limit=18)" in CORE
