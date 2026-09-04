from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = (ROOT / "app.py").read_text(encoding="utf-8")
EDIT = (ROOT / "maplini_editing_core.js").read_text(encoding="utf-8")

def test_release_version_and_lane_helper_present():
    assert 'APP_VERSION = "0.20.34"' in APP
    assert 'function branchContinuationLane(sourceId)' in APP
    assert 'smartFlowContinuationPosition' in APP

def test_editing_core_exports_lane_continuation():
    assert 'function smartFlowContinuationPosition(' in EDIT
    assert 'smartFlowContinuationPosition' in EDIT.split('global.MapliniEditingCore=', 1)[1]
