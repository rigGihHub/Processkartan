from pathlib import Path


APP = (Path(__file__).resolve().parents[1] / "app.py").read_text(encoding="utf-8")
UNDERSTANDING_CORE = (Path(__file__).resolve().parents[1] / "maplini_step_understanding_core.js").read_text(encoding="utf-8")


def test_edit_form_precedes_context_summary():
    assert 'APP_VERSION = "0.20.83"' in APP
    assert APP.index('id="p48-process-info"') < APP.index('id="p48-step-understanding"')


def test_nested_input_output_card_is_visually_removed():
    assert "#pk48.p48-side-context-node .p48-step-io-context{" in APP
    assert "padding:0!important;border:0!important" in APP


def test_context_summary_is_secondary_but_preserved():
    assert "Stegets sammanhang" in APP
    for label in ("Vad?", "Vem?", "Input", "Output", "Sedan"):
        assert label in UNDERSTANDING_CORE
    assert "Input och output hanteras separat och sparas med steget." not in APP


def test_wide_desktop_gets_readable_sidebar_without_harming_narrow_layout():
    assert "@media(min-width:1200px){#pk48 .p48-body{grid-template-columns:320px minmax(0,1fr)!important}}" in APP
