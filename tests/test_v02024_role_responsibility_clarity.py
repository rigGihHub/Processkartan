from pathlib import Path

APP = Path(__file__).resolve().parents[1] / 'app.py'
TEXT = APP.read_text(encoding='utf-8')

def test_version():
    assert 'APP_VERSION = "0.20.34"' in TEXT

def test_role_badge_is_contextual_not_required():
    assert "roleBadge.className='p48-node-role'" in TEXT
    assert "roleBadge.hidden=true" in TEXT
    assert "responsibleRole||''" in TEXT
    assert "item.roleBadge.hidden=!role" in TEXT

def test_role_change_updates_canvas_without_schema_change():
    assert 'refreshNodeResponsibility(item);invalidateNodeGeom' in TEXT
    assert "['process','subprocess','decision']" in TEXT
