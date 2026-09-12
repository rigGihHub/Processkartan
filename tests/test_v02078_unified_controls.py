from pathlib import Path
APP=Path(__file__).resolve().parents[1]/"app.py"
TEXT=APP.read_text(encoding="utf-8")

def test_version_and_unified_control_tokens():
    assert 'APP_VERSION = "0.20.80"' in TEXT
    assert 'v0.20.80 – Unified Controls' in TEXT
    for token in ['--p48-control-radius','--p48-control-border','--p48-control-hover','--p48-focus-ring']:
        assert token in TEXT

def test_unified_states_cover_core_controls():
    assert '#pk48 .p48-btn.primary' in TEXT
    assert '#pk48 .p48-btn.danger' in TEXT
    assert '#pk48 .p48-addio' in TEXT
    assert '#pk48 .p48-node-quick' in TEXT
    assert ':focus-visible' in TEXT
