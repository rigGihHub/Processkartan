from pathlib import Path
from bs4 import BeautifulSoup

APP=Path('app.py').read_text(encoding='utf-8')

def template():
    start=APP.index('<div id="pk48"')
    end=APP.index('<script>',start)
    return APP[start:end]

def test_release_and_context_classes():
    assert 'APP_VERSION = "' in APP
    assert "p48-side-context-active" in APP
    assert "p48-side-context-node" in APP
    assert "p48-side-context-link" in APP
    assert "p48-side-context-multi" in APP

def test_io_belongs_to_step_editor_not_build_palette():
    soup=BeautifulSoup(template(),'html.parser')
    assert soup.select_one('.p48-method-palette .p48-step-io') is None
    info=soup.select_one('#p48-process-info')
    assert info.select_one('.p48-step-io-context') is not None
    assert info.select_one('#p48-inputs') is not None
    assert info.select_one('#p48-outputs') is not None

def test_primary_step_fields_are_quiet_and_advanced_fields_collapsed():
    soup=BeautifulSoup(template(),'html.parser')
    info=soup.select_one('#p48-process-info')
    more=info.select_one('#p48-process-info-more')
    assert info.select_one('#p48-info-description') is not None
    assert info.select_one('#p48-info-role') is not None
    assert more.select_one('#p48-info-system') is not None
    assert more.select_one('#p48-info-duration') is not None
    assert 'Mer om steget' in more.select_one('summary').get_text(' ',strip=True)

def test_contextual_editor_titles_are_explicit():
    assert "context==='link'?'Redigera pil'" in APP
    assert "context==='multi'?'Redigera markering'" in APP
    assert "context==='node'?'Redigera steg'" in APP
