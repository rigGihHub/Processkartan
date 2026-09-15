from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
APP=(ROOT/'app.py').read_text(encoding='utf-8')

def test_version_and_preview_controls_exist():
    assert 'APP_VERSION = "' in APP
    for token in ['p48-export-preview','p48-export-preview-dialog','p48-export-preview-pages','Förhandsgranska sidor']:
        assert token in APP

def test_preview_uses_real_export_composition():
    assert 'composeExportPageCanvases(shot,count)' in APP
    assert 'exportBoundaryWarnings(shot,count)' in APP
    assert 'samma indelning för PDF och DOCX' in APP

def test_preview_does_not_mutate_process():
    body=APP.split('async function openExportPreview(){',1)[1].split('async function exportPdf(){',1)[0]
    assert 'renderMapSnapshot()' in body
    assert 'nodes.set(' not in body
    assert 'links.push(' not in body
