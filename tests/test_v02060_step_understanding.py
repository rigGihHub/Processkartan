from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
APP=(ROOT/'app.py').read_text(encoding='utf-8')
CORE=(ROOT/'maplini_step_understanding_core.js').read_text(encoding='utf-8')
def test_version_and_core_loaded():
    assert 'APP_VERSION = "' in APP
    assert '__MAPLINI_STEP_UNDERSTANDING_CORE__' in APP
    assert '_STEP_UNDERSTANDING_CORE_JS' in APP
    assert 'MapliniStepUnderstandingCore' in CORE
def test_compact_understanding_ui_present():
    for text in ['Förstå steget','Snabböverblick','p48-step-understanding-list']:
        assert text in APP
    assert 'renderStepUnderstanding(item)' in APP
    assert 'stepUnderstandingNext(item)' in APP
def test_summary_uses_existing_step_data_not_generated_truth():
    for field in ['description:info.description','responsibleRole:info.responsibleRole','inputs:item.data.inputs','outputs:item.data.outputs','next:stepUnderstandingNext(item)']:
        assert field in APP
    assert 'Inte angivet ännu' in CORE
    assert 'Ingen input angiven' in CORE
    assert 'Ingen output angiven' in CORE
