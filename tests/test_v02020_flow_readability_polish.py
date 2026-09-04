from pathlib import Path

APP = Path('app.py').read_text(encoding='utf-8')


def test_release_version_and_flow_readability_contract():
    assert 'APP_VERSION = "0.20.34"' in APP
    assert 'function flowReadabilityRole(link)' in APP
    assert "return branchContinuationLane(String(link[0]||''))?'branch':'main';" in APP
    assert "path.classList.add('p48-flow-main')" in APP
    assert "path.classList.add('p48-flow-branch')" in APP


def test_full_and_incremental_connector_rendering_apply_readability_roles():
    assert 'applyFlowReadabilityClass(v,link);' in APP
    assert 'applyFlowReadabilityClass(entry.visible,link);' in APP
    assert "v.classList.toggle('p48-auto-live',Boolean(st.autoManaged));" in APP


def test_selection_focus_mutes_only_unrelated_automatic_flows():
    assert "entry.visible.classList.toggle('p48-flow-context-active',on);" in APP
    assert "entry.visible.classList.toggle('p48-flow-context-muted',Boolean(active&&auto&&!on));" in APP
    assert "const link=links[index],auto=Boolean(link&&linkStyle(link).autoManaged);" in APP


def test_readability_polish_preserves_user_connector_colors():
    block = APP[APP.index('/* v0.20.20: flow readability hierarchy'):APP.index('.p48-node.selected~*{}')]
    assert 'stroke:' not in block
    assert 'p48-flow-main{opacity:.96}' in block
    assert 'p48-flow-branch{opacity:.84}' in block
