from pathlib import Path
from bs4 import BeautifulSoup

APP = Path("app.py").read_text(encoding="utf-8")

def template():
    start = APP.index('<div id="pk48"')
    end = APP.index('<script>', start)
    return APP[start:end]

def test_release_version():
    assert 'APP_VERSION = "0.20.80"' in APP

def test_primary_topbar_keeps_core_work_modes_and_hides_secondary_direct_children():
    soup=BeautifulSoup(template(),"html.parser")
    top=soup.select_one(".p48-top-simplified")
    assert top is not None
    direct_ids={x.get("id") for x in top.find_all(recursive=False) if x.get("id")}
    modes=top.select_one(".p48-work-modes")
    assert modes is not None
    assert [x.get_text(" ",strip=True) for x in modes.select(".p48-mode-btn")] == ["Rita","Förstå","Följ"]
    assert modes.select_one("#p48-walkthrough-launch") is not None
    assert "p48-share" not in direct_ids
    assert "p48-deviation-launch" not in direct_ids
    assert "p48-scale-menu" not in direct_ids

def test_secondary_actions_remain_available_under_more():
    soup=BeautifulSoup(template(),"html.parser")
    more=soup.select_one("#p48-more-menu")
    assert more is not None
    assert more.select_one("#p48-share") is not None
    assert more.select_one("#p48-deviation-launch") is not None
    assert more.select_one("#p48-scale-menu") is not None
    assert more.select_one("#p48-analyze") is not None
    text=more.get_text(" ",strip=True)
    assert "Dela & historik" in text
    assert "Kontroll" in text
    assert "Avancerade verktyg" in text

def test_secondary_tools_keep_unique_dom_ids():
    soup=BeautifulSoup(template(),"html.parser")
    for element_id in ("p48-share","p48-sharebox","p48-deviation-launch","p48-scale-menu"):
        assert len(soup.select(f"#{element_id}")) == 1
