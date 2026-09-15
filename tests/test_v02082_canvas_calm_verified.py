from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APP = (ROOT / "app.py").read_text(encoding="utf-8")
UI_CORE = (ROOT / "maplini_ui_core.js").read_text(encoding="utf-8")


def test_version_and_pdf_guide_default_are_consistent():
    assert 'APP_VERSION = "0.20.90"' in APP
    assert '<option value="off" selected>Ingen PDF-yta</option>' in APP
    assert "let pdfView='off',pageCountMode='auto'" in APP


def test_canvas_calm_rules_beat_legacy_css_order():
    assert "#pk48 .p48-next-step-btn{" in APP
    assert "#pk48 .p48-next-step-btn{" in UI_CORE
    assert "background:rgba(255,255,255,.96)!important" in APP
    assert "border:1px solid #9fc4b3!important" in APP
    assert "width:24px!important;height:24px!important" in APP


def test_selected_step_summary_remains_readable():
    assert "grid-template-columns:60px minmax(0,1fr)!important" in APP
    assert ".p48-step-understanding-head span{font-size:9px!important;white-space:nowrap}" in APP
