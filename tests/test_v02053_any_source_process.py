from pathlib import Path
APP = Path(__file__).resolve().parents[1] / 'app.py'
CORE = Path(__file__).resolve().parents[1] / 'maplini_any_source_core.js'

def test_version_and_any_source_ui():
    s=APP.read_text(encoding='utf-8')
    assert 'APP_VERSION = "0.20.71"' in s
    assert 'Källa → processförslag' in s
    assert 'p48-source-url' in s and 'p48-source-text' in s
    assert 'handleSourceUrl' in s and 'handlePastedSource' in s
    assert 'MapliniAnySourceCore.plan' in s

def test_any_source_core_present():
    s=CORE.read_text(encoding='utf-8')
    for x in ['classifySource','eventItems','readerUrl','markdownToText']:
        assert x in s
