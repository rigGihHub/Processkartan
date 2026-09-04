from pathlib import Path

APP = (Path(__file__).resolve().parents[1] / "app.py").read_text(encoding="utf-8")

def test_version_and_read_mode_controls():
    assert 'APP_VERSION = "0.20.34"' in APP
    assert 'id="p48-readmode-toggle"' in APP
    assert 'id="p48-read-panel"' in APP
    assert 'id="p48-read-hint"' in APP

def test_read_mode_is_non_editing_and_reversible():
    assert 'let readMode=false' in APP
    assert 'function canEdit(){return MapliniAccessCore.canEdit({sharedView,currentRole})&&!readMode}' in APP
    assert 'function setReadMode(on)' in APP
    assert "root.classList.toggle('p48-read-mode',readMode)" in APP
    assert "e.key==='Escape'" in APP

def test_read_panel_uses_existing_process_metadata():
    assert 'function renderReadPanel(item)' in APP
    for field in ['description','responsibleRole','system','instruction','duration','kpi','risk','control']:
        assert f'info.{field}' in APP
    assert "item.data.inputs" in APP
    assert "item.data.outputs" in APP

def test_read_mode_hides_editor_chrome_not_canvas():
    assert '#pk48.p48-read-mode .p48-side{display:none!important}' in APP
    assert '#pk48.p48-read-mode .p48-body{grid-template-columns:1fr!important}' in APP
    assert '#pk48.p48-read-mode .p48-node{cursor:pointer!important}' in APP
