from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
APP=(ROOT/'app.py').read_text(encoding='utf-8')
CORE=(ROOT/'maplini_version_history_core.js').read_text(encoding='utf-8')

def test_version():
    assert 'APP_VERSION = "0.20.71"' in APP

def test_history_is_lightweight_and_schema_free():
    assert "const VERSION_HISTORY_KEY='maplini_version_history_v1'" in APP
    assert 'versionHistories[currentId]' in APP
    assert 'högst 20 versioner per process' in APP
    assert 'maplini_version_history_core.js' in APP
    assert 'create table' not in CORE.lower()

def test_save_creates_version_without_duplicates():
    assert "captureProcessVersion('Sparad version',false)" in APP
    assert 'fingerprint(normalized[0].data)===currentFingerprint' in CORE
    assert 'slice(0,Math.max(1,Number(limit)||20))' in CORE

def test_restore_is_safe_and_local_first():
    assert "captureProcessVersion('Före återställning',false)" in APP
    assert 'Din nuvarande version sparas först som en kontrollpunkt.' in APP
    assert 'tryck Spara för att uppdatera molnet' in APP
    assert 'versionHistories[currentId]=preserved' in APP

def test_history_shows_concrete_diff_summary():
    for token in ['addedNodes','removedNodes','changedNodes','addedLinks','removedLinks']:
        assert token in CORE
    assert 'MapliniVersionHistoryCore.diffLabel' in APP
