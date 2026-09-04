from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
APP=(ROOT/'app.py').read_text(encoding='utf-8')
CORE=(ROOT/'maplini_connector_core.js').read_text(encoding='utf-8')


def test_v02018_version_and_lane_overlap_scoring_contract():
    assert 'APP_VERSION = "0.20.34"' in APP
    assert 'function parallelSegmentOverlap(' in CORE
    assert 'function routeParallelOverlap(' in CORE
    assert 'parallelOverlap*7' in CORE
    assert 'sharedAllowance=30' in CORE


def test_lane_overlap_helpers_are_public_for_geometry_regressions():
    assert 'parallelSegmentOverlap,routeParallelOverlap,routeCrossingCount' in CORE
