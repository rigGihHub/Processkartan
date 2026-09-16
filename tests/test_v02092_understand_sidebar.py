from pathlib import Path


APP = (Path(__file__).parents[1] / "app.py").read_text(encoding="utf-8")


def test_understand_keeps_a_contextual_desktop_sidebar():
    assert 'APP_VERSION = "0.20.93"' in APP
    assert '#pk48.p48-read-mode .p48-side{display:flex!important' in APP
    assert '#pk48.p48-read-mode .p48-body{grid-template-columns:240px minmax(0,1fr)!important}' in APP
    assert 'class="p48-read-sidebar"' in APP
    assert 'id="p48-read-sidebar-list"' in APP


def test_understand_sidebar_is_navigation_not_editing_tools():
    assert '.p48-side>*:not(.p48-read-sidebar){display:none!important}' in APP
    assert "button.addEventListener('click',()=>jumpToProcessNode(item.data.id))" in APP
    assert "readSidebarStart.addEventListener('click',()=>navigateProcess('start'))" in APP
    assert "readSidebarFit.addEventListener('click',fitProcessToScreen)" in APP
    assert "if(selectedIds.has(item.data.id))button.classList.add('active')" in APP


def test_mobile_understand_remains_canvas_focused():
    mobile = APP[APP.index('@media(max-width:700px){#pk48.p48-read-mode .p48-side'):]
    assert '#pk48.p48-read-mode .p48-side{display:none!important}' in mobile
    assert '#pk48.p48-read-mode .p48-body{grid-template-columns:1fr!important}' in mobile
