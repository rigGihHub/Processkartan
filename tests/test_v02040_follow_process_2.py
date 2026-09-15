from pathlib import Path
APP = Path(__file__).resolve().parents[1] / 'app.py'
SRC = APP.read_text(encoding='utf-8')

def test_version_02040():
    assert 'APP_VERSION = "' in SRC

def test_current_step_is_action_focused():
    assert 'class="p48-walkthrough-now">Gör nu</div>' in SRC
    assert 'p48-walkthrough-step-title' in SRC

def test_quick_question_uses_operational_labels():
    assert "q.quick?(answer==='yes'?'Klart':'Inte klart')" in SRC
    assert "Klart tar dig direkt vidare · Inte klart låter dig stanna upp" in SRC

def test_route_answers_preview_destination():
    assert 'function walkthroughAnswerTarget(question,answer,item)' in SRC
    assert "target.className='p48-walkthrough-answer-target'" in SRC
    assert '→ ${targetText}' in SRC

def test_single_next_step_uses_continue_language():
    assert 'Fortsätt: ${target?.data?.text' in SRC

def test_subprocess_return_is_explicit_and_continuous():
    assert 'function renderWalkthroughReturnNotice()' in SRC
    assert "walkthroughState.returnNotice={parentProcessId:" in SRC
    assert 'Tillbaka i huvudflödet.' in SRC
    assert "'Klar här – tillbaka till huvudflödet →'" in SRC

def test_mobile_or_small_screen_step_resets_to_current_content():
    assert 'function scrollWalkthroughToCurrentStep()' in SRC
    assert "walkthroughRun.scrollTo({top:0,behavior:'smooth'})" in SRC
