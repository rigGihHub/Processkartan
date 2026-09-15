from pathlib import Path


APP = (Path(__file__).resolve().parents[1] / "app.py").read_text(encoding="utf-8")


def test_node_labels_keep_normal_word_boundaries():
    assert 'APP_VERSION = "0.20.88"' in APP
    assert "word-break:normal;overflow-wrap:break-word;hyphens:none" in APP
    assert "#pk48 .p48-node.process{min-width:200px!important}" not in APP


def test_small_maps_drop_duplicate_horizontal_navigator_only():
    assert "root.classList.toggle('p48-small-map',nodes.size>0&&nodes.size<=12)" in APP
    assert "#pk48.p48-small-map .p48-hnav{display:none!important}" in APP
    assert "#pk48.p48-large-map" in APP
