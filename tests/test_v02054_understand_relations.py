from pathlib import Path
APP=Path('app.py').read_text(encoding='utf-8')
CORE=Path('maplini_any_source_core.js').read_text(encoding='utf-8')
def test_version_and_relation_contract():
    assert 'APP_VERSION = "0.20.80"' in APP
    for label in ['Orsak → konsekvens','Beslut → effekt','Problem → åtgärd','Aktör → handling','Villkor → resultat','Händelse → reaktion']:
        assert label in CORE
    assert 'explicitRelation' in CORE and 'relationLabel' in CORE
    assert 'tydliga samband' in APP
