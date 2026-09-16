from pathlib import Path


APP = (Path(__file__).parents[1] / "app.py").read_text(encoding="utf-8")


def test_editor_reset_version_and_quick_next_positioning():
    assert 'APP_VERSION = "0.20.93"' in APP
    assert "#pk48 .p48-node>.p48-next-step-wrap" in APP
    assert "position:absolute!important" in APP
    assert "transform:translateY(-50%)!important" in APP


def test_selected_node_uses_one_quiet_resize_affordance():
    assert ".p48-resize:not(.se)" in APP
    assert ".p48-resize.se" in APP
    assert "background:#2f8065!important" in APP


def test_draw_mode_does_not_repeat_step_summary():
    assert "#pk48:not(.p48-read-mode).p48-side-context-node #p48-step-understanding{display:none!important}" in APP
    assert "previousSelectedId!==selectedId" in APP
    assert "sidePanel.scrollTop=0" in APP


def test_responsive_and_lifecycle_hooks_stay_inside_editor_scope():
    scope_close = APP.rindex("})();\n</script>")
    assert APP.index("function syncResponsiveLayout()") < scope_close
    assert APP.index("function flushLifecycleSave(context)") < scope_close
    assert APP.index("function alignEditorTop()") < scope_close


def test_primary_work_modes_use_one_stable_delegated_switch():
    assert "closest('#p48-mode-draw,#p48-readmode-toggle,#p48-walkthrough-launch')" in APP
    assert "e.stopImmediatePropagation()" in APP
    assert "else if(mode.id==='p48-readmode-toggle')setReadMode(!readMode)" in APP
    assert "else openWalkthrough()" in APP
