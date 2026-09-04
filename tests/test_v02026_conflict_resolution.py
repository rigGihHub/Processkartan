from pathlib import Path
APP=Path(__file__).resolve().parents[1]/'app.py'
TEXT=APP.read_text(encoding='utf-8')

def test_version(): assert 'APP_VERSION = "0.20.34"' in TEXT
def test_conflict_dialog_choices():
    for value in ['Behåll min version som en kopia','Läs in versionen från molnet','Ersätt molnversionen med min version']:
        assert value in TEXT
def test_conflict_fetches_both_versions():
    assert 'async function fetchCloudProcess(processId)' in TEXT
    assert 'conflictVersionSummary(local,cloud)' in TEXT
def test_local_copy_never_overwrites_cloud():
    assert "copy.id=newId" in TEXT
    assert "delete copy.cloudUpdatedAt" in TEXT
def test_cloud_load_is_explicit():
    assert 'function loadConflictCloudVersion()' in TEXT
    assert "msg('Molnversionen är inläst')" in TEXT
def test_force_overwrite_requires_confirmation_and_latest_cloud_guard():
    assert "if(!confirm('Ersätta molnversionen?" in TEXT
    assert "&updated_at=eq.'+encodeURIComponent(c.cloudUpdatedAt)" in TEXT
def test_conflict_opens_resolution():
    assert 'await openCloudConflictResolution();' in TEXT
