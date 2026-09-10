from pathlib import Path
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
APP=(ROOT/"app.py").read_text(encoding="utf-8")

def template():
    start=APP.index('<div id="pk48"')
    end=APP.index('<script>',start)
    return BeautifulSoup(APP[start:end],"html.parser")

def test_release_version():
    assert 'APP_VERSION = "0.20.71"' in APP

def test_view_tools_are_grouped_without_losing_ids():
    soup=template()
    view=soup.select_one('#p48-view-menu')
    assert view is not None
    assert 'Visa' in view.get_text(' ',strip=True)
    for eid in ('p48-zoom-out','p48-zoom-reset','p48-zoom-in','p48-fit-screen','p48-overview-toggle','p48-responsibility-toggle'):
        assert len(view.select(f'#{eid}'))==1
    top=soup.select_one('.p48-top-simplified')
    direct={x.get('id') for x in top.find_all(recursive=False) if x.get('id')}
    assert 'p48-overview-toggle' not in direct
    assert 'p48-responsibility-toggle' not in direct

def test_more_menu_uses_core_language_and_demotes_deviations():
    soup=template()
    more=soup.select_one('#p48-more-menu')
    text=more.get_text(' ',strip=True)
    assert 'Dela & historik' in text
    assert 'Processkontroll' in text
    assert 'Övrigt' in text
    assert 'Analysera process' not in text
    quality=more.select_one('#p48-analyze')
    dev=more.select_one('#p48-deviation-launch')
    assert quality is not None and dev is not None
    # Deviations remain available but come after core quality/tools sections.
    assert str(more).find('p48-deviation-launch') > str(more).find('p48-analyze')

def test_canvas_menu_has_single_processyta_heading():
    soup=template()
    menu=soup.select_one('.p48-canvas-menu')
    headings=[x.get_text(' ',strip=True) for x in menu.select('.p48-pop-title')]
    assert headings.count('Processyta')==1
