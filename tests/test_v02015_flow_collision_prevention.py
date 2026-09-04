from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = (ROOT / "app.py").read_text(encoding="utf-8")
EDIT = (ROOT / "maplini_editing_core.js").read_text(encoding="utf-8")

def test_v02015_release_and_flow_obstacle_contract():
    assert 'APP_VERSION = "0.20.34"' in APP
    assert 'function existingFlowSegments(' in APP
    assert 'linkSegments:existingFlowSegments([sourceId])' in APP
    assert 'function flowSegmentCollisionPenalty(' in EDIT
    assert 'flowSegmentCollisionPenalty' in EDIT.split('global.MapliniEditingCore=', 1)[1]

def test_collision_prevention_does_not_relayout_existing_nodes():
    body = APP.split('function existingFlowSegments(', 1)[1].split('function flowSpacingFor', 1)[0]
    assert '.style.left=' not in body
    assert '.style.top=' not in body
