from pathlib import Path


APP = (Path(__file__).resolve().parents[1] / "app.py").read_text(encoding="utf-8")


def test_primary_step_labels_have_explicit_text_elements_before_controls():
    assert '<label><span class="p48-field-label">Vad händer?</span><textarea id="p48-info-description"' in APP
    assert '<label><span class="p48-field-label">Vem ansvarar?</span><input id="p48-info-role"' in APP


def test_primary_step_labels_enforce_vertical_reading_order():
    assert "#pk48.p48-side-context-node #p48-process-info>label{display:flex!important;flex-direction:column!important" in APP
    assert "#pk48.p48-side-context-node #p48-process-info .p48-field-label{display:block;order:-1}" in APP
