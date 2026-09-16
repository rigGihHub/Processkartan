from pathlib import Path


APP = (Path(__file__).parents[1] / "app.py").read_text(encoding="utf-8")
NAV = (Path(__file__).parents[1] / "maplini_navigation_core.js").read_text(encoding="utf-8")


def test_understand_outline_uses_graph_order_not_canvas_order():
    assert 'APP_VERSION = "0.20.93"' in APP
    assert "MapliniNavigationCore.orderedOutline" in APP
    assert "function orderedOutline(nodes,links)" in NAV
    assert "components.sort" in NAV


def test_outline_preserves_explicit_branches_and_disconnected_truth():
    assert "if(label==='ja')return 0;if(label==='nej')return 1" in NAV
    assert "branchLabel:text(branchLabel)" in NAV
    assert "disconnected:componentIndex>0" in NAV
    assert "label.textContent='Okopplade steg'" in APP
    assert "entry.branchLabel?entry.branchLabel+' · ':''" in APP


def test_merge_waits_for_all_incoming_branches():
    assert "const waiting=(incoming.get(ref.id)||[]).some" in NAV
    assert "if(!waiting)visit(ref.id" in NAV
