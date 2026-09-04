from pathlib import Path
APP = Path(__file__).resolve().parents[1] / 'app.py'
SRC = APP.read_text(encoding='utf-8')

def test_version():
    assert 'APP_VERSION = "0.20.34"' in SRC

def test_existing_cloud_process_uses_compare_and_swap_patch():
    assert "updated_at=eq.'+encodeURIComponent(expected)" in SRC
    assert "method:'PATCH'" in SRC
    assert "Prefer:'return=representation'" in SRC

def test_zero_row_patch_is_a_conflict_not_an_upsert():
    assert "rows.length!==1)throw cloudConflictError()" in SRC
    assert "?on_conflict=id" not in SRC[SRC.index('async function guardedProcessCloudWrite'):SRC.index('async function loadCloudProcesses')]

def test_unknown_base_checks_cloud_before_insert():
    assert 'const existing=await currentCloudVersion(currentId);' in SRC
    assert "if(existing)throw cloudConflictError" in SRC

def test_insert_race_becomes_conflict():
    assert "if(e?.status===409)throw cloudConflictError()" in SRC

def test_conflict_keeps_local_copy_and_surfaces_persistent_status():
    assert "const localOk=saveLocal(true);" in SRC
    assert "cloudBadge.textContent='Molnkonflikt'" in SRC
    assert "molnversionen har ändrats av någon annan" in SRC
