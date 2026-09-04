from pathlib import Path
SRC=Path("app.py").read_text()

def test_version(): assert 'APP_VERSION = "0.20.34"' in SRC
def test_active_share_state_is_visible():
    assert 'p48-share-status' in SRC and 'Publik läslänk aktiv' in SRC
    assert "shareBtn.textContent=active?'Dela process · aktiv länk':'Dela process'" in SRC
def test_revoke_invalidates_public_link():
    assert 'async function revokeCurrentShare()' in SRC
    assert 'JSON.stringify({share_token:null,share_mode:null})' in SRC
    assert 'Den gamla länken slutar fungera direkt.' in SRC
def test_shared_loader_still_requires_view_mode():
    assert "&share_mode=eq.view&select=id,name,data" in SRC
