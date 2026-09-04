from pathlib import Path

APP = (Path(__file__).resolve().parents[1] / "app.py").read_text(encoding="utf-8")


def test_version_is_02011():
    assert 'APP_VERSION = "0.20.34"' in APP


def test_single_toolbar_does_not_duplicate_next_action():
    assert '.p48-node-quick[data-mode="single"] #p48-node-quick-next' in APP
    assert '.p48-node-quick[data-mode="single"] #p48-node-quick-next-more' in APP
    assert 'display:none!important' in APP


def test_direct_next_control_is_visually_polished():
    assert '/* v0.20.11 – Direct Manipulation Polish' in APP
    assert '.p48-next-step-btn:hover,.p48-next-step-btn:focus-visible' in APP
    assert 'transform:scale(1.08)' in APP


def test_connection_handles_stay_available_on_selected_node():
    assert '.p48-node.selected .p48-handle{opacity:.82!important' in APP
    assert '.p48-node.selected .p48-handle:hover{opacity:1!important;transform:scale(1.22)}' in APP
