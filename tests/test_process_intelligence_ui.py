from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = (ROOT / 'app.py').read_text(encoding='utf-8')
CORE = (ROOT / 'maplini_process_intelligence_core.js').read_text(encoding='utf-8')


def test_process_intelligence_is_embedded_and_exposed():
    assert 'APP_VERSION = "0.14.3"' in APP
    assert '_PROCESS_INTELLIGENCE_CORE_PATH' in APP
    assert '__MAPLINI_PROCESS_INTELLIGENCE_CORE__' in APP
    assert 'id="p48-analyze"' in APP
    assert 'id="p48-analysis-panel"' in APP
    assert 'function runProcessAnalysis()' in APP
    assert 'function focusAnalysisNodes(ids)' in APP
    assert 'MapliniProcessIntelligenceCore.analyze' in APP
    assert 'global.MapliniProcessIntelligenceCore={analyze}' in CORE


def test_analysis_panel_starts_hidden_and_findings_are_canvas_clickable():
    assert 'class="p48-analysis-panel" aria-label="Processkontroll" hidden' in APP
    assert "btn.addEventListener('click',()=>focusAnalysisNodes(f.nodeIds))" in APP
    assert "analysisClose.addEventListener('click',()=>{analysisPanel.hidden=true})" in APP
