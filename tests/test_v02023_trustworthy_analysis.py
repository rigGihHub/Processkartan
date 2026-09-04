from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
APP=(ROOT/'app.py').read_text(encoding='utf-8')
CORE=(ROOT/'maplini_process_intelligence_core.js').read_text(encoding='utf-8')

def test_version():
    assert 'APP_VERSION = "0.20.34"' in APP

def test_health_score_removed_from_ui_and_core():
    assert 'PROCESSHÄLSA' not in APP
    assert 'STRUKTURFYND' in APP
    assert 'const weights={error:1.8' not in CORE
    assert 'score:Math.round' not in CORE

def test_analysis_is_explicitly_rule_based():
    assert 'Regelbaserad strukturkontroll.' in APP
    assert 'inte om verksamhetsprocessen i verkligheten är effektiv eller korrekt' in APP
    assert "evidenceKind:ri.kind" in CORE
    assert "rule:ri.rule" in CORE
    assert "'Strukturfakta':'Bedömning'" in APP

def test_heuristics_are_not_presented_as_facts():
    for code in ['merge_bottleneck','fanout','loop','long_chain','direct_activity']:
        assert f"{code}:{{kind:'assessment'" in CORE
