from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
APP=(ROOT/'app.py').read_text(encoding='utf-8')


def test_version_and_large_map_routing_policy_present():
    assert 'APP_VERSION = "0.20.34"' in APP
    assert 'routingEnvelopeFilter' in APP
    assert 'links.length<=400' in APP
    assert 'fullRoutingObstacles=automaticRoutingObstacles([])' in APP
    assert 'renderedRoutingSegments=[]' in APP


def test_persist_only_computes_content_change_once():
    block=APP[APP.index('function persist(show=false,refreshList=false){'):APP.index('let lastUndoAt=', APP.index('function persist(show=false,refreshList=false){'))]
    assert block.count('MapliniSyncCore.contentChanged(previous,st)') == 1
    assert 'const changed=MapliniSyncCore.contentChanged(previous,st);' in block
