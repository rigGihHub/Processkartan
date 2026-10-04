from pathlib import Path


APP = (Path(__file__).parents[1] / "app.py").read_text(encoding="utf-8")


def test_step_content_precedes_visible_formatting():
    assert 'APP_VERSION = "' in APP
    quick = APP.index('class="p48-quick-format p48-node-only"')
    process_info = APP.index('id="p48-process-info"')
    advanced = APP.index('class="p48-visual-details p48-node-only"')
    assert process_info < quick < advanced
    for control_id in (
        "p48-quick-bg",
        "p48-quick-text",
        "p48-quick-bold",
        "p48-quick-italic",
        "p48-quick-under",
        "p48-quick-size-down",
        "p48-quick-size-up",
    ):
        assert f'id="{control_id}"' in APP[quick:advanced]


def test_quick_formatting_uses_the_existing_style_update_path():
    assert "quickBg.addEventListener('change',()=>updateStyle({bgColor:quickBg.value}))" in APP
    assert "quickText.addEventListener('change',()=>updateStyle({textColor:quickText.value}))" in APP
    assert "quickBold.addEventListener('click',()=>bold.click())" in APP
    assert "quickItalic.addEventListener('click',()=>italic.click())" in APP
    assert "quickUnder.addEventListener('click',()=>under.click())" in APP
    assert "Math.max(10,Math.min(36,current+delta))" in APP


def test_quick_controls_are_synced_and_accessible():
    assert "quickSizeValue.value=`${sharedStyleValue(items,'fontSize')??s.fontSize} px`" in APP
    assert "button.setAttribute('aria-pressed',String(active))" in APP
    assert 'aria-label="Snabbformatering"' in APP
    assert "#pk48 .p48-quick-format-button.active" in APP
