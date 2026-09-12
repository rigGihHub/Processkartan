from pathlib import Path

APP = (Path(__file__).resolve().parents[1] / "app.py").read_text(encoding="utf-8")


def test_v02044_first_process_flow_contract():
    assert 'APP_VERSION = "0.20.80"' in APP
    assert 'placeholder="Ex. Hantera kundfaktura"' in APP
    assert 'id="p48-empty-first-text"' in APP
    assert 'placeholder="Ex. Ta emot beställning"' in APP
    assert 'function createFirstActivityFromStarter()' in APP
    assert "addFirstStep('process',null,{text,edit:false})" in APP
    assert "msg('Första steget klart · tryck Tab för nästa steg')" in APP
    assert "if(emptyStart)emptyStart.addEventListener('click'" in APP
    assert "if(emptyObject)emptyObject.addEventListener('click'" in APP


def test_v02044_empty_state_is_only_for_editable_empty_processes():
    assert "const show=nodes.size===0&&!sharedView&&!readMode;" in APP
    assert "emptyState.setAttribute('aria-hidden',show?'false':'true')" in APP
    assert "setTimeout(()=>{refreshEmptyState();if(emptyFirstText&&!emptyState.hidden)emptyFirstText.focus()},0)" in APP


def test_v02044_first_activity_keeps_existing_tab_build_rhythm():
    assert "quickBuildNodeIds.add(item.data.id);" in APP
    assert "item.el.focus();" in APP
    assert "if(e.key==='Tab'&&!mod&&selectedIds.size===1&&selectedId)" in APP
    assert "else{const type=preferredNextType(item);if(type)addNextStepFromNode(item.data.id,type)}" in APP
