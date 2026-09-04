from pathlib import Path
APP=(Path(__file__).resolve().parents[1]/'app.py').read_text(encoding='utf-8')

def test_version_and_mobile_reader_controls():
    assert 'APP_VERSION = "0.20.34"' in APP
    for ident in ['p48-mobile-reader-bar','p48-mobile-reader-name','p48-mobile-reader-follow','p48-mobile-reader-fit','p48-mobile-reader-edit']:
        assert f'id="{ident}"' in APP

def test_mobile_defaults_to_consumption_and_keeps_edit_escape_hatch():
    assert 'function activateMobileConsumptionDefault()' in APP
    assert 'if(mobile&&!mobileConsumptionInitialized&&nodes.size)setTimeout(activateMobileConsumptionDefault,0)' in APP
    assert "mobileReaderEdit.addEventListener('click'" in APP
    assert 'MapliniAccessCore.canEdit({sharedView,currentRole})' in APP

def test_mobile_follow_temporarily_enters_read_mode_from_editor():
    assert 'if(isMobileLayout()&&!readMode){mobileWalkthroughForcedRead=true;setReadModeWithOptions(true,{silent:true})}' in APP
    assert 'if(mobileWalkthroughForcedRead){mobileWalkthroughForcedRead=false;setReadModeWithOptions(false,{silent:true})}' in APP

def test_mobile_read_and_follow_are_touch_optimized():
    assert '#pk48.p48-read-mode .p48-mobile-reader-bar{display:flex}' in APP
    assert 'max-height:62dvh' in APP
    assert 'height:min(68dvh,680px)' in APP
    assert '.p48-walkthrough-answer{min-height:60px;font-size:17px}' in APP
