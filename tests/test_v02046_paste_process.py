from pathlib import Path

APP = Path(__file__).parents[1].joinpath("app.py").read_text()

def test_release_version():
    assert 'APP_VERSION = "0.20.71"' in APP

def test_paste_process_ui_and_parser_exist():
    for token in [
        'id="p48-batch-launch"', 'id="p48-empty-import"', 'id="p48-batch-dialog"',
        'function parseBatchSteps(text)', 'function createProcessFromBatch()', 'function batchStepType(text,index,total)'
    ]:
        assert token in APP

def test_import_is_deterministic_and_bounded():
    assert '.slice(0,80)' in APP
    assert "quickBuildInferredType(text,'process')" in APP
    assert 'MapliniConnectorCore.create(prev,id' in APP
    assert 'confirm(`Det här ersätter den aktuella canvasen' in APP
