from pathlib import Path
APP=Path('app.py').read_text(encoding='utf-8')
def test_v02061_version_and_core():
    assert 'APP_VERSION = "' in APP
    assert '__MAPLINI_EMPTY_STEP_SUGGESTIONS_CORE__' in APP
    assert 'Förslag utifrån stegen runt omkring' in APP
    assert "MapliniEmptyStepSuggestionsCore.suggest" in APP
    assert "Förslaget lades in – kontrollera att det stämmer" in APP
