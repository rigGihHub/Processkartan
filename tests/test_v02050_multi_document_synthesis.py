from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SRC=(ROOT/'app.py').read_text(encoding='utf-8')
CORE=(ROOT/'maplini_document_interpretation_core.js').read_text(encoding='utf-8')

def test_version(): assert 'APP_VERSION = "0.20.71"' in SRC

def test_multi_file_input_and_handler():
    assert 'type="file" multiple accept=' in SRC
    assert 'handleDocumentFiles(docFile.files)' in SRC
    assert 'Välj ett eller flera dokument' in SRC
    assert 'Välj högst 8 dokument åt gången.' in SRC

def test_multi_document_core_is_used():
    assert 'function interpretDocuments(documents,limit=100)' in CORE
    assert 'MapliniDocumentInterpretationCore.interpretDocuments(docs,100)' in SRC
    for token in ['responsibility','system','order','conflictMessages','sourceNames']:
        assert token in CORE

def test_conflicts_are_visible_and_not_auto_connected():
    assert "if(e.conflict)continue" in SRC
    assert "['Konflikter',unresolvedDocumentConflictCount()]" in SRC
    assert 'Olika ordning' in CORE
    assert 'Olika ansvar' in CORE
    assert 'källdokumenten' in SRC

def test_no_schema_change_for_multi_document_import():
    schema=(ROOT/'supabase_schema.sql').read_text(encoding='utf-8').lower()
    assert 'multi_document' not in schema
    assert 'document_conflict' not in schema
