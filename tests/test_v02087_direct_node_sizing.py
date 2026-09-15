from pathlib import Path


APP = (Path(__file__).resolve().parents[1] / "app.py").read_text(encoding="utf-8")


def test_direct_size_presets_are_available_for_selected_nodes():
    assert 'APP_VERSION = "0.20.87"' in APP
    for preset, label in (("compact", "Kompakt"), ("normal", "Normal"), ("large", "Stor")):
        assert f'data-node-size-preset="{preset}">{label}</button>' in APP
    assert "Dra i hörnen för fri storlek" in APP


def test_presets_update_geometry_and_persistence_for_all_selected_nodes():
    assert "function applyNodeSizePreset(preset)" in APP
    assert "item.data.width=width;item.data.height=height;sync(item.el)" in APP
    assert "requestFullLinkRender(true);drawLinks();persist();refreshControls()" in APP
    assert "const items=selectedNodeItems()" in APP


def test_decision_presets_remain_square():
    assert "decision:[140,140]" in APP
    assert "decision:[180,180]" in APP
    assert "decision:[240,240]" in APP
