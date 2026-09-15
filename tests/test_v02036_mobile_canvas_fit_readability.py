from pathlib import Path
APP=(Path(__file__).resolve().parents[1]/'app.py').read_text(encoding='utf-8')

def test_version_and_mobile_readable_fit_contract():
    assert 'APP_VERSION = "' in APP
    assert 'function fitMobileReadProcess(options={})' in APP
    assert 'function mobileReadFocusRect(rects)' in APP
    assert 'const readableFloor=rects.length<=20?.76:rects.length<=80?.64:.52' in APP

def test_mobile_consumption_uses_readable_fit_not_desktop_fit():
    start=APP.index('function activateMobileConsumptionDefault()')
    snippet=APP[start:start+520]
    assert 'fitMobileReadProcess({announce:false})' in snippet
    assert 'fitProcessToScreen()' not in snippet

def test_mobile_read_css_reduces_chrome_and_canvas_height():
    assert '#pk48.p48-read-mode .p48-scroll{scroll-padding-top:64px;height:min(64dvh,540px)!important;min-height:430px!important;max-height:540px!important' in APP
    assert '.p48-mobile-reader-bar button{flex:0 0 auto;min-width:40px;min-height:40px' in APP
    assert '#pk48.p48-read-mode .p48-breadcrumbs{padding-top:56px}' in APP

def test_mobile_read_refits_after_orientation_or_resize():
    assert 'else if(mobile&&readMode&&nodes.size)setTimeout(()=>fitMobileReadProcess({announce:false}),0);' in APP
