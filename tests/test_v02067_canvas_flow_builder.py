from pathlib import Path
from bs4 import BeautifulSoup

APP=Path('app.py').read_text(encoding='utf-8')

def template():
    start=APP.index('<div id="pk48"')
    end=APP.index('<script>',start)
    return APP[start:end]

def test_release_version():
    assert 'APP_VERSION = "' in APP

def test_next_step_is_exposed_as_primary_canvas_action():
    soup=BeautifulSoup(template(),'html.parser')
    btn=soup.select_one('#p48-node-quick-next')
    more=soup.select_one('#p48-node-quick-next-more')
    assert btn is not None and more is not None
    assert btn.get('aria-keyshortcuts') == 'Tab'
    assert more.get('aria-keyshortcuts') == 'Shift+Tab'
    assert 'display:inline-flex!important' in APP
    assert '#p48-node-quick-next{display:inline-flex!important' in APP

def test_decision_primary_action_creates_both_branches():
    assert "if(current==='decision')return'＋ Ja + Nej'" in APP
    assert "if(item&&item.data&&item.data.type==='decision'){addDecisionBranches(item.data.id);return;}" in APP

def test_quick_build_still_supports_keyboard_continuation():
    assert "if(e.key==='Tab'&&!mod&&selectedIds.size===1&&selectedId)" in APP
    assert "if(e.shiftKey&&item.nextBtn){item.nextBtn.click();return}" in APP
    assert "if(rapid){continueQuickBuild(el.dataset.id);return}" in APP
