from pathlib import Path
from bs4 import BeautifulSoup

APP=Path("app.py").read_text(encoding="utf-8")

def template():
    start=APP.index('<div id="pk48"')
    end=APP.index('<script>',start)
    return APP[start:end]

def test_release_and_three_modes_are_primary():
    assert 'APP_VERSION = "0.20.80"' in APP
    soup=BeautifulSoup(template(),"html.parser")
    top=soup.select_one('.p48-top-simplified')
    modes=top.select_one('.p48-work-modes')
    assert modes is not None
    assert modes.select_one('#p48-mode-draw').get_text(strip=True)=='Rita'
    assert modes.select_one('#p48-readmode-toggle').get_text(strip=True)=='Förstå'
    assert modes.select_one('#p48-walkthrough-launch').get_text(strip=True)=='Följ'

def test_secondary_tools_are_relocated_not_duplicated():
    soup=BeautifulSoup(template(),"html.parser")
    for element_id in ('p48-view-menu','p48-export-menu','p48-smart-layout-menu'):
        assert len(soup.select(f'#{element_id}'))==1
    assert 'simplifyTopNavigation()' in APP
    assert "presentation.body.appendChild(el)" in APP

def test_draw_and_understand_modes_reuse_existing_read_mode():
    assert "modeDrawBtn.addEventListener('click',()=>setReadMode(false))" in APP
    assert "readModeToggle.addEventListener('click',()=>setReadMode(!readMode))" in APP
    assert "readModeToggle.textContent='Förstå'" in APP

def test_no_data_or_backend_schema_change_for_ui_pass():
    # This release should be UI/DOM organization only.
    assert 'v0.20.67 – Canvas Flow Builder' in APP
