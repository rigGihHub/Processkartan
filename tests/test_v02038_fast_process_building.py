from pathlib import Path
APP = Path(__file__).resolve().parents[1].joinpath('app.py').read_text()

def test_version():
    assert 'APP_VERSION = "0.20.80"' in APP

def test_quick_build_transient_state_and_inference():
    assert 'const quickBuildNodeIds=new Set()' in APP
    assert 'function quickBuildInferredType' in APP
    assert "value.endsWith('?')" in APP
    assert "return'decision'" in APP
    assert "return'end'" in APP

def test_enter_continues_only_for_quick_build_nodes():
    assert "quickBuildNodeIds.has(String(el.dataset.id))" in APP
    assert 'continueQuickBuild(el.dataset.id)' in APP
    assert "addNextStepFromNode(item.data.id,'process')" in APP

def test_decision_quick_build_fills_both_branches_without_guessing():
    assert "addDecisionBranches(item.data.id,{quickBuild:true})" in APP
    assert 'quickBuildBranchQueue=created.map' in APP
    assert "Skriv den andra beslutsgrenen" in APP

def test_classic_tab_and_ctrl_enter_paths_remain():
    assert "if(e.key==='Tab'&&!mod&&selectedIds.size===1&&selectedId)" in APP
    assert "if(e.key==='Enter'&&(e.ctrlKey||e.metaKey))" in APP
