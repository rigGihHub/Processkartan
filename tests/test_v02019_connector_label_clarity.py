from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def test_release_version_and_label_clarity_contract():
    app=(ROOT/'app.py').read_text(encoding='utf-8')
    core=(ROOT/'maplini_connector_core.js').read_text(encoding='utf-8')
    assert 'APP_VERSION = "0.20.34"' in app
    assert 'smartLabelPlacement' in core
    assert 'smartLabelPlacement(points,width,height,automaticRoutingObstacles([]),occupiedLabels' in app
    assert 'renderedLinkLabelRects' in app
