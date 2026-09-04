from pathlib import Path
APP = Path(__file__).resolve().parents[1] / 'app.py'
SRC = APP.read_text(encoding='utf-8')

def test_version_02031():
    assert 'APP_VERSION = "0.20.34"' in SRC

def test_walkthrough_tracks_root_and_process_stack():
    assert 'walkthroughState.rootProcessId=String(currentId' in SRC
    assert 'walkthroughState.processStack=[]' in SRC
    assert 'rootProcessName' in SRC

def test_linked_subprocess_can_be_entered_from_walkthrough():
    assert 'function enterWalkthroughSubprocess(item,returnNextId)' in SRC
    assert "item.data.type==='subprocess'" in SRC
    assert 'return enterWalkthroughSubprocess(item,nextId)' in SRC

def test_subprocess_start_nodes_are_computed_from_child_process():
    assert 'function walkthroughProcessStartIds(processId)' in SRC
    assert 'MapliniWalkthroughCore.startNodeIds(nodeData,processLinks)' in SRC

def test_multiple_subprocess_starts_require_explicit_choice():
    assert 'function renderPendingSubprocessStart()' in SRC
    assert 'Den här delprocessen har flera startpunkter.' in SRC
    assert 'pendingSubprocessStarts={startIds:starts}' in SRC

def test_subprocess_completion_returns_to_parent_continuation():
    assert 'function returnFromWalkthroughSubprocess()' in SRC
    assert 'frame.returnNextId' in SRC
    assert 'openProcess(frame.parentProcessId)' in SRC

def test_walkthrough_history_records_process_context():
    assert "processId:String(currentId||'')" in SRC
    assert "processName:String(nameInput.value.trim()||'Namnlös process')" in SRC

def test_completed_run_belongs_to_root_process():
    assert "processId:String(walkthroughState.rootProcessId||currentId||'')" in SRC
    assert 'runProcessId=String(record.processId' in SRC

def test_closing_nested_walkthrough_returns_to_root_process():
    assert "const rootId=String(walkthroughState?.rootProcessId||'')" in SRC
    assert "if(rootId&&rootId!==String(currentId||'')&&processes[rootId])" in SRC
