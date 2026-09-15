from pathlib import Path
SRC=Path("app.py").read_text(encoding="utf-8")

def test_version():
    assert 'APP_VERSION = "' in SRC

def test_read_scan_anchor_css_exists():
    assert 'v0.20.70 – read scan guide' in SRC
    assert 'content:"BÖRJA HÄR"' in SRC
    assert 'content:"VÄGVAL"' in SRC
    assert 'content:"SLUT"' in SRC

def test_read_guide_is_explicit_not_inferred():
    assert 'function refreshReadScanGuide()' in SRC
    assert "item.data.type==='decision'" in SRC
    assert "id===g.startId" in SRC
    assert "id===g.endId" in SRC

def test_read_panel_shows_real_next_steps():
    assert "const next=stepUnderstandingNext(item);" in SRC
    assert "l.textContent='Därefter'" in SRC
    assert "Processen slutar här" in SRC

def test_glance_start_end_are_navigable():
    assert "jumpReadAnchor(processGlanceSummary().startId)" in SRC
    assert "jumpReadAnchor(processGlanceSummary().endId)" in SRC
