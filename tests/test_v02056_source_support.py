from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SRC=(ROOT/'app.py').read_text(encoding='utf-8')

def test_version(): assert 'APP_VERSION = "0.20.80"' in SRC

def test_compact_source_support_ui():
    for token in ['p48-source-support','p48-source-disagreements','MapliniSourceSupportCore.summarize','källor stödjer samma steg']:
        assert token in SRC or token in (ROOT/'maplini_source_support_core.js').read_text(encoding='utf-8')

def test_conflicts_are_preserved_as_trace_metadata_after_resolution():
    assert 'relevantConflicts=documentConflictList().filter' in SRC
    assert 'disagreements=relevantConflicts.map' in SRC
    assert 'docConflictResolutions[c.id]' in SRC
    assert 'disagreements};const sourceTrace' in SRC

def test_no_schema_change():
    schema=(ROOT/'supabase_schema.sql').read_text(encoding='utf-8').lower()
    assert 'source_disagreement' not in schema
