from pathlib import Path

APP = Path("app.py").read_text(encoding="utf-8")

def test_version():
    assert 'APP_VERSION = "0.20.34"' in APP

def test_open_deviation_has_improve_action():
    assert "processBtn.textContent=row.status==='open'?'Förbättra steg':'Visa i process'" in APP
    assert "startDeviationImprovement(row)" in APP

def test_improvement_context_links_back_to_node_and_properties():
    assert 'id="p48-improvement-context"' in APP
    assert 'id="p48-improvement-properties"' in APP
    assert "select(item.el);ensureNodeVisible(item.el)" in APP
    assert "focusFormattingPanel()" in APP

def test_resolution_reuses_existing_walkthrough_status_model():
    assert "updateWalkthroughDeviationStatus(row.runId,row.deviationIndex,'resolved')" in APP
    assert 'activeImprovementDeviation' in APP

def test_no_new_cloud_schema_for_improvement_context():
    assert 'improvement_context' not in APP.lower()
