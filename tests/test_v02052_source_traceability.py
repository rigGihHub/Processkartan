from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SRC=(ROOT/'app.py').read_text(encoding='utf-8')

def test_version():
    assert 'APP_VERSION = "0.20.80"' in SRC

def test_source_trace_panel_exists():
    for token in ['p48-source-trace','Källa till steget','p48-source-trace-list','KÄLLSPÅR']:
        assert token in SRC

def test_document_created_nodes_keep_sources_and_evidence():
    assert "kind:'document_import'" in SRC
    assert 'sourceNames.map(name=>({name,evidence:' in SRC
    assert 'sourceEvidence[name]||r.evidence' in SRC

def test_single_document_is_decorated_with_real_filename():
    assert 'item.sourceNames=[docs[0].name]' in SRC
    assert 'item.sourceEvidence={[docs[0].name]:item.evidence||\'\'}' in SRC

def test_trace_is_rendered_on_selection_and_is_read_only():
    assert 'function renderSourceTrace(item)' in SRC
    assert 'renderSourceTrace(item);' in SRC
    assert 'sourceTraceList.appendChild(card)' in SRC
    assert 'Kontrollera alltid mot originaldokumentet.' in SRC

def test_no_schema_change_for_source_traceability():
    schema=(ROOT/'supabase_schema.sql').read_text(encoding='utf-8').lower()
    assert 'source_trace' not in schema
    assert 'document_provenance' not in schema
