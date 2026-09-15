from pathlib import Path
APP=Path(__file__).resolve().parents[1].joinpath('app.py').read_text()

def test_version_and_preview_contract():
    assert 'APP_VERSION = "' in APP
    assert 'id="p48-clean-preview-bar"' in APP
    assert 'id="p48-clean-preview-apply"' in APP
    assert 'id="p48-clean-preview-cancel"' in APP
    assert 'function cancelCleanPreview' in APP
    assert 'function applyCleanPreview' in APP
    assert 'cleanPreview={ids,positions,original,orientation,isolated}' in APP
    assert "renderCleanPreviewPositions(positions)" in APP
    assert "pushUndo(true)" in APP

def test_preview_does_not_use_sync_before_apply():
    preview_block=APP.split('function autoCleanProcess(){',1)[1].split('function smartLayout(',1)[0]
    before_apply=preview_block.split('function applyCleanPreview(){',1)[0] if 'function applyCleanPreview(){' in preview_block else preview_block
    # autoCleanProcess preview itself only paints DOM positions; persistence happens in applyCleanPreview.
    auto=APP.split('function autoCleanProcess(){',1)[1].split('function smartLayout(',1)[0]
    assert 'persist()' not in auto
