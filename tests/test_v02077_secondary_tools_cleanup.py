from pathlib import Path

TEXT=Path("app.py").read_text()

def test_version_and_more_hierarchy_contract():
    assert 'APP_VERSION = "0.20.80"' in TEXT
    assert 'v0.20.77 – Secondary Tools Cleanup' in TEXT
    assert "more.dataset.organized='1'" in TEXT
    assert "Snabbåtgärder" in TEXT
    assert "Redigering & struktur" in TEXT
    assert "Utseende, layout & export" in TEXT
    assert "p48-more-group" in TEXT

def test_existing_tool_ids_are_preserved():
    for tool_id in [
        'p48-batch-launch','p48-doc-launch','p48-analyze','p48-share',
        'p48-version-history-launch','p48-select-tool','p48-clear-canvas',
        'p48-scale-menu','p48-view-menu','p48-export-menu','p48-logo-menu',
        'p48-deviation-launch'
    ]:
        assert f'id="{tool_id}"' in TEXT
