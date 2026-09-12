from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
APP=(ROOT/'app.py').read_text(encoding='utf-8')
CORE=(ROOT/'maplini_process_intelligence_core.js').read_text(encoding='utf-8')


def test_version():
    assert 'APP_VERSION = "0.20.80"' in APP


def test_process_control_is_concrete_not_score_based():
    assert 'Konkreta saker att kontrollera – utan hittepåbetyg.' in APP
    assert 'STRUKTURFYND' in APP
    assert 'PROCESSHÄLSA' not in APP
    assert 'score:Math.round' not in CORE


def test_new_rules_cover_reachability_decisions_and_responsibility():
    for code in ['decision_yes_no','decision_unlabeled','responsibility_missing','responsibility_absent','unreachable','start_incoming','end_outgoing']:
        assert f"{code}:" in CORE
    assert "responsibleRole:String((n.processInfo&&n.processInfo.responsibleRole)||'').trim()" in CORE
    assert "const reachable=new Set(),queue=starts.map(n=>n.id)" in CORE
    assert "yes!==no" in CORE


def test_findings_remain_clickable_and_can_be_rerun():
    assert 'id="p48-analysis-rerun"' in APP
    assert "analysisRerun.addEventListener('click',runProcessAnalysis)" in APP
    assert "focusAnalysisNodes(f.nodeIds)" in APP
    assert "analysisPanel.hidden=true" in APP
