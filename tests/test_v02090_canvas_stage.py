from pathlib import Path


APP = (Path(__file__).parents[1] / "app.py").read_text(encoding="utf-8")


def test_small_maps_are_never_magnified_by_fit():
    assert 'APP_VERSION = "0.20.90"' in APP
    assert "margin:72,minScale:.25,maxScale:1" in APP
    assert "maxScale:1.5" not in APP[APP.index("function fitProcessToScreen()"):APP.index("function mobileReadFocusRect")]


def test_node_presets_are_genuinely_compact():
    assert "compact:{process:[128,52]" in APP
    assert "normal:{process:[176,64]" in APP
    assert "large:{process:[232,82]" in APP


def test_single_step_palette_click_continues_the_flow():
    assert "(nodes.size===1?[...nodes.values()][0]:null)" in APP


def test_small_map_stage_removes_desktop_document_chrome():
    assert "#pk48.p48-small-map .p48-scroll{scrollbar-width:none!important" in APP
    assert "#p48-canvas.p48-default-surface" in APP
    assert "canvas.classList.toggle('p48-default-surface'" in APP
