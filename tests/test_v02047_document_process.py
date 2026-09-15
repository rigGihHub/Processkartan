from pathlib import Path
APP=Path(__file__).resolve().parents[1]/"app.py"
SRC=APP.read_text(encoding="utf-8")

def test_version(): assert 'APP_VERSION = "' in SRC
def test_document_ui():
    for token in ['p48-doc-launch','p48-doc-file','p48-doc-steps','p48-doc-create','Dokument → processförslag']: assert token in SRC
def test_supported_document_extractors():
    assert 'mammoth.browser.min.js' in SRC and 'pdf.min.js' in SRC and "file.text()" in SRC
def test_review_before_draw():
    assert 'createProcessFromDocumentProposal' in SRC and ('docReview.hidden=false' in SRC or 'renderDocumentInterpretation' in SRC) and 'docCreate.disabled=unresolved>0' in SRC
def test_privacy_copy(): assert 'Filerna skickas inte till Maplinis server' in SRC
