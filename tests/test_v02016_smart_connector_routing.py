from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = (ROOT / "app.py").read_text(encoding="utf-8")
CORE = (ROOT / "maplini_connector_core.js").read_text(encoding="utf-8")


def test_v02016_release_and_smart_routing_contract():
    assert 'APP_VERSION = "0.20.34"' in APP
    assert 'function automaticRoutingObstacles(' in APP
    assert 'MapliniConnectorCore.smartOrthogonalRoute(' in APP
    assert "effective.autoManaged&&effective.anchorMode==='auto'" in APP
    assert 'function smartOrthogonalRoute(' in CORE
    assert 'function routeScore(' in CORE


def test_manual_connectors_are_not_obstacle_rerouted():
    call_block = APP.split("let points=MapliniConnectorCore.routePoints", 1)[1].split("const d=", 1)[0]
    assert "effective.autoManaged&&effective.anchorMode==='auto'" in call_block
