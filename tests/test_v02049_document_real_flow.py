from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SRC=(ROOT/'app.py').read_text(encoding='utf-8')
CORE=(ROOT/'maplini_document_interpretation_core.js').read_text(encoding='utf-8')
def test_version(): assert 'APP_VERSION = "0.20.71"' in SRC
def test_real_flow_core_is_used():
    for token in ['interpretFlow','conditionalFromSentence','feedbackTarget','subprocessHint']:
        assert token in CORE
    assert 'MapliniDocumentInterpretationCore.interpretFlow(docs[0].text,80)' in SRC
def test_flow_preview_and_creation():
    for token in ['docFlowPlan','grenvägar','återkopplingar','Vägar','Loopar','Möjlig delprocess']:
        assert token in SRC
def test_labeled_edges_are_created():
    assert "label:e.label||''" in SRC
    assert "createdByDocId" in SRC
def test_guardrails_preserved():
    assert 'Allt markeras som förslag och ska kontrolleras mot källdokumenten.' in SRC
    assert 'document_flow' not in (ROOT/'supabase_schema.sql').read_text(encoding='utf-8').lower()
