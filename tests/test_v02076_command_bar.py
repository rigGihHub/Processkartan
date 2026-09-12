from pathlib import Path

APP = Path(__file__).resolve().parents[1] / 'app.py'
TEXT = APP.read_text(encoding='utf-8')


def test_version_and_command_bar_contract():
    assert 'APP_VERSION = "0.20.80"' in TEXT
    assert 'p48-process-cluster' in TEXT
    assert 'p48-top-utilities' in TEXT
    assert 'v0.20.77 – Secondary Tools Cleanup' in TEXT
    assert 'p48-new-compact' in TEXT
    assert 'p48-save-quiet' in TEXT


def test_core_actions_keep_stable_ids():
    for id_ in ['p48-name','p48-new','p48-save','p48-mode-draw','p48-readmode-toggle','p48-walkthrough-launch','p48-find-menu','p48-undo','p48-redo','p48-more-menu']:
        assert f'id="{id_}"' in TEXT
