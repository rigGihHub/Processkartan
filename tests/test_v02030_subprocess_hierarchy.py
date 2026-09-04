from pathlib import Path
APP = Path(__file__).resolve().parents[1] / 'app.py'
SRC = APP.read_text(encoding='utf-8')

def test_version_02030():
    assert 'APP_VERSION = "0.20.34"' in SRC

def test_breadcrumb_navigation_exists():
    assert 'id="p48-breadcrumbs"' in SRC
    assert 'function breadcrumbChain(processId)' in SRC
    assert 'function renderBreadcrumbs()' in SRC

def test_subprocess_open_action_exists():
    assert 'id="p48-node-quick-subprocess"' in SRC
    assert 'function openLinkedSubprocess(item)' in SRC
    assert "item.data.childProcessId=childId" in SRC

def test_child_process_keeps_parent_reference():
    assert 'child.parentProcessId=currentId' in SRC
    assert 'child.parentNodeId=item.data.id' in SRC
    assert 'parentProcessId:meta.parentProcessId||null' in SRC
    assert 'parentNodeId:meta.parentNodeId||null' in SRC

def test_existing_link_is_reused_not_duplicated():
    assert "if(childId&&!processes[childId])childId=''" in SRC
    assert "if(!childId){" in SRC
    assert "openProcess(childId);return true" in SRC


def test_duplicated_subprocess_does_not_share_child_implicitly():
    assert "if(d.type==='subprocess')delete d.childProcessId" in SRC
