from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = (ROOT / "app.py").read_text(encoding="utf-8")
EDIT = (ROOT / "maplini_editing_core.js").read_text(encoding="utf-8")

def test_v02014_release_and_rejoin_contract():
    assert 'APP_VERSION = "0.20.34"' in APP
    assert 'function branchRejoinContext(' in APP
    assert 'function addBranchRejoin(' in APP
    assert "dataset.branchRejoin='true'" in APP
    assert 'smartBranchRejoinPosition' in APP
    assert 'function smartBranchRejoinPosition(' in EDIT
    assert 'smartBranchRejoinPosition' in EDIT.split('global.MapliniEditingCore=', 1)[1]

def test_rejoin_is_explicit_and_does_not_move_existing_nodes():
    body = APP.split('function addBranchRejoin(', 1)[1].split('function celebrateCreatedNode', 1)[0]
    assert "links.push(MapliniConnectorCore.create(context.sourceId,id" in body
    assert "links.push(MapliniConnectorCore.create(context.siblingTipId,id" in body
    assert 'source.el.style.left=' not in body
    assert 'sibling.el.style.left=' not in body
