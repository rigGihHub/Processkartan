from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SRC=(ROOT/'app.py').read_text(encoding='utf-8')
CORE=(ROOT/'maplini_document_interpretation_core.js').read_text(encoding='utf-8')
def test_version(): assert 'APP_VERSION = "' in SRC
def test_core_loaded(): assert '__MAPLINI_DOCUMENT_INTERPRETATION_CORE__' in SRC and 'MapliniDocumentInterpretationCore' in CORE
def test_structured_review_ui():
    for token in ['p48-doc-insights','p48-doc-structured','p48-doc-mode-structured','Strukturerat förslag']: assert token in SRC
def test_interpretation_fields():
    for token in ['responsibleRole','system','inputs','outputs','confidenceLabel','review']: assert token in CORE
def test_structured_process_creation():
    assert 'createProcessFromStructuredDocument' in SRC
    assert 'processInfo:info' in SRC and 'inputs:r.inputs||[]' in SRC and 'outputs:r.outputs||[]' in SRC
def test_no_schema_change():
    assert 'document_interpretation' not in (ROOT/'supabase_schema.sql').read_text(encoding='utf-8').lower()
