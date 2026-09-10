from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SRC=(ROOT/'app.py').read_text(encoding='utf-8')
CORE=(ROOT/'maplini_document_interpretation_core.js').read_text(encoding='utf-8')

def test_version():
    assert 'APP_VERSION = "0.20.71"' in SRC

def test_conflict_resolution_ui_exists():
    for token in ['p48-doc-conflicts','Lös konflikter före ritning','p48-doc-conflict-options','p48-doc-conflict-custom']:
        assert token in SRC

def test_conflicts_block_drawing_until_resolved():
    assert 'unresolvedDocumentConflictCount()>0' in SRC
    assert "Lös dokumentkonflikterna innan processen ritas" in SRC
    assert 'docCreate.disabled=unresolved>0' in SRC

def test_resolutions_cover_role_system_type_and_order():
    for token in ["conflict.type==='responsibility'","conflict.type==='system'","conflict.type==='type'","conflict.type==='order'"]:
        assert token in SRC
    assert "Ingen direkt koppling" in SRC
    assert "Skriv annat ansvar" in SRC
    assert "Skriv annat system" in SRC

def test_core_exposes_resolution_options_and_direction_pairs():
    assert "options:[]" in CORE
    assert "directions:[" in CORE
    assert "pairKey" in CORE
    assert "id:'c'+(++conflictSeq)" in CORE

def test_no_schema_change():
    schema=(ROOT/'supabase_schema.sql').read_text(encoding='utf-8').lower()
    assert 'conflict_resolution' not in schema
    assert 'document_resolution' not in schema
