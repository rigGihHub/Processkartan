from pathlib import Path


APP = (Path(__file__).resolve().parents[1] / "app.py").read_text(encoding="utf-8")


def test_desktop_palette_click_is_an_actual_action():
    assert 'APP_VERSION = "0.20.92"' in APP
    assert "i.addEventListener('click',e=>{e.preventDefault();addFromPalette(i,{closeMobile:isMobileLayout()})})" in APP


def test_palette_continues_a_single_selected_flow_without_guessing_decisions():
    assert "const source=selectedIds.size===1?nodes.get([...selectedIds][0]):(nodes.size===1?[...nodes.values()][0]:null)" in APP
    assert "addNextStepFromNode(source.data.id,type);return" in APP
    assert "source.data.type==='decision'" in APP
    assert "Beslut behöver tydliga vägar" in APP


def test_semantically_standalone_palette_types_stay_standalone():
    assert "!['start','note'].includes(type)&&!explicitInput" in APP
    assert "addNode(type,x,y,{objectRole:item.dataset.objectRole||null})" in APP
    assert "addEventListener('dragstart'" in APP
