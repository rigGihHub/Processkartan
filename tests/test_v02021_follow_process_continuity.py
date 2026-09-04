from pathlib import Path

APP = Path(__file__).resolve().parents[1] / "app.py"
TEXT = APP.read_text(encoding="utf-8")

def test_version_and_transition_contract():
    assert 'APP_VERSION = "0.20.34"' in TEXT
    assert 'function prepareWalkthroughTransition(fromId,toId)' in TEXT
    assert 'p48-walk-link-transition' in TEXT
    assert 'p48-walk-arriving' in TEXT
    assert '},360);' in TEXT

def test_transition_is_cleared_on_commit():
    start = TEXT.index('function commitWalkthroughStep(nextId)')
    assert 'clearWalkthroughTransition();' in TEXT[start:start+300]
