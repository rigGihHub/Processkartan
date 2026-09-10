from pathlib import Path
APP = Path(__file__).parents[1] / 'app.py'

def test_understand_30_seconds_surface_and_logic():
    s=APP.read_text()
    assert 'APP_VERSION = "0.20.71"' in s
    for token in ['p48-process-glance','p48-glance-start','p48-glance-end','p48-glance-roles','p48-glance-scope','function processGlanceSummary()','function refreshProcessGlance()']:
        assert token in s
    assert "all.filter(item=>item.data.type==='decision').length" in s
    assert "responsibleRole" in s
