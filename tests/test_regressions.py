from pathlib import Path
import re
import subprocess
import sys

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
APP = (ROOT / "app.py").read_text(encoding="utf-8")
GOOGLE_UI = (ROOT / "maplini_google_ui.py").read_text(encoding="utf-8")
CONNECTOR_CORE = (ROOT / "maplini_connector_core.js").read_text(encoding="utf-8")
UI_CORE = (ROOT / "maplini_ui_core.js").read_text(encoding="utf-8")
STATE_CORE = (ROOT / "maplini_state_core.js").read_text(encoding="utf-8")
RELIABILITY_CORE = (ROOT / "maplini_reliability_core.js").read_text(encoding="utf-8")
EXPORT_CORE = (ROOT / "maplini_export_core.js").read_text(encoding="utf-8")
WORKFLOW_CORE = (ROOT / "maplini_workflow_core.js").read_text(encoding="utf-8")
PERFORMANCE_CORE = (ROOT / "maplini_performance_core.js").read_text(encoding="utf-8")
MOBILE_CORE = (ROOT / "maplini_mobile_core.js").read_text(encoding="utf-8")
SELECTION_CORE = (ROOT / "maplini_selection_core.js").read_text(encoding="utf-8")
SYNC_CORE = (ROOT / "maplini_sync_core.js").read_text(encoding="utf-8")
SESSION_CORE = (ROOT / "maplini_session_core.js").read_text(encoding="utf-8")
RC_CORE = (ROOT / "maplini_rc_core.js").read_text(encoding="utf-8")
FLOW_CORE = (ROOT / "maplini_flow_core.js").read_text(encoding="utf-8")
ACCESS_CORE = (ROOT / "maplini_access_core.js").read_text(encoding="utf-8")
PRIVACY_CORE = (ROOT / "maplini_privacy_core.js").read_text(encoding="utf-8")


def _template():
    start = APP.index('html = r"""') + len('html = r"""')
    end = APP.index('"""', start)
    return APP[start:end]


def test_single_save_button_and_no_dead_cloud_save_reference():
    html = _template()
    soup = BeautifulSoup(html, "html.parser")
    assert len(soup.select("#p48-save")) == 1
    assert soup.select_one("#p48-cloud-save") is None
    assert "cloudSaveBtn" not in APP


def test_save_handler_preserves_local_and_cloud_semantics():
    assert "root.querySelector('#p48-save').addEventListener('click',async()=>{" in APP
    assert "if(ownerId())" in APP
    assert "await saveCurrentToCloud()" in APP
    assert "const result=await saveCurrentToCloud()" in APP
    assert "msg(localOk?'Sparad lokalt':'Lokal sparning misslyckades')" in APP


def test_google_oauth_is_extracted_and_not_duplicated_in_app():
    assert APP.count("maplini_google_ui.render_google_export_ui(st, google_docs)") == 1
    assert "google_docs.exchange(st, st.query_params" not in APP
    assert GOOGLE_UI.count("google_docs.exchange(st, code)") == 1


def test_editor_dom_contract():
    soup = BeautifulSoup(_template(), "html.parser")
    body = soup.select_one(".p48-body")
    side = soup.select_one("aside.p48-side")
    main = soup.select_one("main#p48-scroll")
    controls = soup.select_one("#p48-controls")
    canvas = soup.select_one("#p48-canvas")
    assert all((body, side, main, controls, canvas))
    assert side.find_parent(class_="p48-body") is body
    assert main.find_parent(class_="p48-body") is body
    assert controls.find_parent("aside") is side
    assert canvas.find_parent(id="p48-scroll") is main


def test_mobile_contract_is_present():
    html = _template()
    assert 'id="p48-mobile-tools"' in html
    assert 'id="p48-mobile-backdrop"' in html
    assert "min-height:44px" in html
    assert "touch-action:none!important" in html
    assert 'id="p48-mobile-bar"' in html
    assert "p48-link-hit-segment{height:44px" in html
    assert "safe-area-inset-bottom" in html
    assert "orientationchange" in html


def test_recent_canvas_features_do_not_regress():
    html = _template()
    for control in (
        'id="p48-link-color"',
        'id="p48-bg-type"',
        'id="p48-bg-pattern-color"',
        'id="p48-bg-density"',
        'id="p48-select-tool"',
        'id="p48-delete-selection"',
    ):
        assert control in html
    assert "selectedLinkIndices=new Set()" in APP
    assert "linksInSelectionRect" in APP
    assert "requestFullLinkRender(true)" in APP


def test_python_sources_compile():
    for file in (ROOT / "app.py", ROOT / "google_docs.py", ROOT / "maplini_google_ui.py"):
        result = subprocess.run([sys.executable, "-m", "py_compile", str(file)], capture_output=True, text=True)
        assert result.returncode == 0, result.stderr


def test_embedded_javascript_syntax_when_node_available():
    import shutil
    node = shutil.which("node")
    if not node:
        return
    match = re.search(r"<script>\s*(.*?)\s*</script>", APP, re.S)
    assert match
    check_file = ROOT / "tests" / "_embedded_check.js"
    try:
        check_file.write_text(match.group(1), encoding="utf-8")
        result = subprocess.run([node, "--check", str(check_file)], capture_output=True, text=True)
        assert result.returncode == 0, result.stderr
    finally:
        check_file.unlink(missing_ok=True)


def test_mobile_css_targets_real_dom_not_old_nonexistent_selectors():
    html = _template()
    soup = BeautifulSoup(html, "html.parser")
    assert soup.select_one(".p48-top") is not None
    assert soup.select_one(".p48-brand") is not None
    assert soup.select_one(".p48-logo-crop") is not None
    assert soup.select_one("#p48-name") is not None
    mobile = html[html.index("/* v0.10.12 mobile shell"):html.index(".p48-canvas-menu{")]
    assert ".p48-top{" in mobile
    assert ".p48-brand{" in mobile
    assert ".p48-logo-crop{" in mobile
    assert "#p48-name{" in mobile
    assert ".p48-toolbar{" not in mobile
    assert ".p48-header{" not in mobile
    assert "#p48-process-name" not in mobile

def test_mobile_toolbar_cannot_wrap_canvas_offscreen():
    html = _template()
    mobile = html[html.index("/* v0.10.12 mobile shell"):html.index(".p48-canvas-menu{")]
    assert "flex-wrap:nowrap!important" in mobile
    assert "overflow-x:auto!important" in mobile
    assert "#p48-mobile-tools{order:-30}" in mobile
    assert "height:auto!important" in mobile
    assert "overflow:visible!important" in mobile

def test_connector_core_is_extracted_and_wired():
    assert "MapliniConnectorCore" in CONNECTOR_CORE
    assert "function setStyle" in CONNECTOR_CORE
    assert "function removeSelected" in CONNECTOR_CORE
    assert '<script>__MAPLINI_CONNECTOR_CORE__</script>' in _template()
    assert 'html = html.replace("__MAPLINI_CONNECTOR_CORE__", _CONNECTOR_CORE_JS)' in APP
    assert "return MapliniConnectorCore.style(link)" in APP
    assert "MapliniConnectorCore.removeSelected" in APP

def test_connector_core_javascript_syntax_when_node_available():
    import shutil
    node = shutil.which("node")
    if not node:
        return
    result = subprocess.run([node, "--check", str(ROOT / "maplini_connector_core.js")], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_mobile_allows_vertical_page_scroll():
    html = _template()
    mobile = html[html.index("/* v0.10.12 mobile shell"):html.index(".p48-canvas-menu{")]
    assert "overflow-y:visible!important" in mobile
    assert "overscroll-behavior-y:auto" in mobile
    assert "height:auto!important" in mobile
    assert "overflow:visible!important" in mobile

def test_mobile_canvas_keeps_horizontal_pan_without_vertical_scroll_lock():
    html = _template()
    mobile = html[html.index("/* v0.10.12 mobile shell"):html.index(".p48-canvas-menu{")]
    assert "overflow-x:auto!important" in mobile
    assert "overflow-y:hidden!important" in mobile
    assert "-webkit-overflow-scrolling:touch" in mobile

def test_mobile_logo_uses_contain_and_is_not_crop_locked():
    html = _template()
    mobile = html[html.index("/* v0.10.12 mobile shell"):html.index(".p48-canvas-menu{")]
    assert "object-fit:contain!important" in mobile
    assert "overflow:visible!important" in mobile

def test_streamlit_component_is_tall_enough_for_mobile_page_scroll():
    assert "components.html(html, height=920, scrolling=False)" in APP


def test_connector_restore_is_normalized():
    assert "links=MapliniConnectorCore.normalizeLinks(d.links||[]);" in APP


def test_connector_create_delete_and_move_share_core_paths():
    assert "MapliniConnectorCore.create(el.dataset.id,target.dataset.id,side,{label:autoLabel})" in APP
    assert "function deleteLinkAt(index,withUndo=true)" in APP
    assert "MapliniConnectorCore.removeAt(links,index)" in APP
    assert "MapliniConnectorCore.setFreeOffset(links,index,baseFreeDx+dx,baseFreeDy+dy)" in APP
    assert "links.splice(selectedLinkIndex,1)" not in APP


def test_connector_lifecycle_node_test_when_available():
    import shutil
    node = shutil.which("node")
    if not node:
        return
    result = subprocess.run([node, str(ROOT / "tests" / "test_connector_core.js")], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert "connector lifecycle OK" in result.stdout


def test_v01015_contextual_format_panel_states():
    html = _template()
    soup = BeautifulSoup(html, "html.parser")
    panel = soup.select_one("#p48-format-panel")
    hint = soup.select_one("#p48-format-hint")
    assert panel is not None and panel.get("data-context") == "none"
    assert hint is not None
    assert '.p48-format[data-context="none"] #p48-controls{display:none}' in html
    assert '.p48-format[data-context="link"] .p48-node-only{display:none!important}' in html
    assert "formatPanel.dataset.context=context" in APP
    assert "const multiNodeMode=!linkMode&&selectedIds.size>1" in APP
    assert "const context=linkMode?'link':(multiNodeMode?'multi':(enabled?'node':'none'))" in APP


def test_v01015_step_io_only_visible_for_node_selection():
    html = _template()
    assert ".p48-step-io{display:none}" in html
    assert ".p48-step-io.on{display:block}" in html
    assert "stepIO.classList.toggle('on',enabled&&!multiNodeMode)" in APP


def test_v01015_mobile_palette_supports_tap_and_keyboard_add():
    html = _template()
    soup = BeautifulSoup(html, "html.parser")
    items = soup.select('.p48-item[role="button"][tabindex="0"]')
    assert len(items) == 9
    assert "function addFromPalette(item,{closeMobile=false}={})" in APP
    assert "if(isMobileLayout()){e.preventDefault();addFromPalette(i,{closeMobile:true})}" in APP
    assert "if(e.key==='Enter'||e.key===' ')" in APP
    assert "setMobileTools(false)" in APP


def test_v01015_mobile_palette_explains_tap_behavior():
    html = _template()
    assert "Grundflödet är <strong>Objekt → Aktivitet → Objekt</strong>" in html
    assert "Bygg processen" in html


def test_v01016_canvas_core_is_wired_and_syntax_tested():
    assert '_CANVAS_CORE_PATH' in APP
    assert '__MAPLINI_CANVAS_CORE__' in APP
    assert 'MapliniCanvasCore.place(' in APP
    assert 'MapliniCanvasCore.resize(' in APP
    assert 'MapliniCanvasCore.normalizeRect(' in APP


def test_v01016_link_only_area_selection_can_be_deleted():
    assert 'deleteSelectionBtn.disabled=selectedIds.size===0&&selectedLinkIndices.size===0' in APP
    assert 'if(!selectedIds.size&&!selectedLinkIndices.size)return' in APP


def test_v01016_gestures_are_cancel_safe_and_do_not_create_empty_undo_steps():
    assert APP.count("addEventListener('pointercancel',done)") >= 2
    assert "document.addEventListener('pointercancel',finish)" in APP
    assert 'MapliniMobileCore.movedEnough' in APP
    assert 'if(mutated)persist()' in APP


def test_v01016_keyboard_undo_redo_and_delete_shortcuts():
    assert "const mod=e.ctrlKey||e.metaKey,key=e.key.toLowerCase()" in APP
    assert "mod&&key==='z'" in APP
    assert "mod&&key==='y'" in APP
    assert "e.key==='Delete'||e.key==='Backspace'" in APP
    assert 'e.target.isContentEditable' in APP


def test_v01016_canvas_core_node_test_when_available():
    import shutil
    node = shutil.which('node')
    if not node:
        return
    result = subprocess.run([node, str(ROOT / 'tests' / 'test_canvas_core.js')], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert 'canvas core OK' in result.stdout


def test_v01017_ui_core_is_loaded_and_injected():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert '_UI_CORE_PATH' in APP
    assert '__MAPLINI_UI_CORE__' in APP
    assert 'MapliniUiCore.selectionHint' in APP


def test_v01017_selection_feedback_and_action_semantics():
    html = _template()
    assert 'id="p48-select-tool" aria-pressed="false"' in html
    assert "selectToolBtn.setAttribute('aria-pressed'" in APP
    assert 'id="p48-status" class="p48-status" role="status" aria-live="polite"' in html
    assert 'title="Ångra (Ctrl/Cmd+Z)"' in html
    assert 'title="Ta bort markerat (Delete/Backspace)"' in html


def test_v01017_palette_has_accessible_action_names():
    html = _template()
    for label in (
        'aria-label="Lägg till Start"',
        'aria-label="Lägg till Aktivitet"',
        'aria-label="Lägg till Beslut"',
        'aria-label="Lägg till Slut"',
        'aria-label="Lägg till Delprocess"',
        'aria-label="Lägg till Anteckning"',
    ):
        assert label in html


def test_v01017_focus_states_exist():
    html = _template()
    assert ".p48-btn:focus-visible" in html
    assert ".p48-item:focus-visible" in html
    assert "outline:3px solid rgba(37,99,235,.38)" in html


def test_v01017_ui_core_contains_selection_hint_logic():
    assert "function selectionHint(state)" in UI_CORE
    assert "objekt markerade" in UI_CORE
    assert "kopplingar markerade" in UI_CORE


def test_v01018_state_core_is_loaded_and_injected():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert '_STATE_CORE_PATH' in APP
    assert '__MAPLINI_STATE_CORE__' in APP
    assert 'MapliniStateCore.normalizeProcess' in APP
    assert 'MapliniStateCore.normalizeStore' in APP

def test_v01018_local_save_uses_backup_before_overwrite():
    assert "LOCAL_BACKUP_KEY='maplini_v050_backup'" in APP
    assert "const previous=localStorage.getItem(LOCAL_KEY)" in APP
    assert "localStorage.setItem(LOCAL_BACKUP_KEY,previous)" in APP

def test_v01018_load_falls_back_and_quarantines_corrupt_primary():
    assert "{key:LOCAL_BACKUP_KEY,raw:localStorage.getItem(LOCAL_BACKUP_KEY)}" in APP
    assert "LOCAL_CORRUPT_KEY='maplini_v050_corrupt'" in APP
    assert "localStorage.setItem(LOCAL_CORRUPT_KEY,candidate.raw)" in APP

def test_v01018_restore_normalizes_and_resets_history_between_processes():
    assert "MapliniStateCore.normalizeProcess(raw,raw?.id||currentId)" in APP
    assert "lastUndoSnapshot='';lastUndoAt=0" in APP

def test_v01018_visibility_and_unload_flush_state():
    assert "document.addEventListener('visibilitychange'" in APP
    assert "persist(false,false);saveLocal(true)" in APP

def test_v01018_state_core_drops_orphan_links():
    assert "nodeIds.has(l[0])&&nodeIds.has(l[1])" in STATE_CORE
    assert "schemaVersion:1" in STATE_CORE


def test_v01019_reliability_core_loaded():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert '_RELIABILITY_CORE_PATH' in APP
    assert '__MAPLINI_RELIABILITY_CORE__' in APP

def test_v01019_runtime_error_capture():
    html=_template()
    assert 'id="p48-runtime-error"' in html
    assert "window.addEventListener('error'" in APP
    assert "window.addEventListener('unhandledrejection'" in APP
    assert "maplini_last_runtime_error" in APP

def test_v01019_save_verification_and_emergency_recovery():
    assert "const verify=localStorage.getItem(LOCAL_KEY)" in APP
    assert "localStorage verification failed" in APP
    assert "sessionStorage.setItem('maplini_emergency_snapshot'" in APP
    assert "{key:'maplini_emergency_snapshot',raw:sessionStorage.getItem('maplini_emergency_snapshot')}" in APP

def test_v01019_restore_and_switch_rollback():
    assert "restore-parse" in APP
    assert "restore-validate" in APP
    assert "if(!restore(processes[id]))" in APP
    assert "currentId=previousId" in APP

def test_v01019_reliability_primitives():
    assert "function errorInfo(error,context)" in RELIABILITY_CORE
    assert "function parseJsonSafe(raw)" in RELIABILITY_CORE
    assert "function validateStoreShape(store)" in RELIABILITY_CORE


def test_v01020_export_core_is_loaded_and_injected():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert '_EXPORT_CORE_PATH' in APP
    assert '__MAPLINI_EXPORT_CORE__' in APP
    assert 'MapliniExportCore.validateBytes' in APP

def test_v01020_exports_flush_state_and_validate_signatures():
    assert "persist(false,false);saveLocal(true)" in APP
    assert "'application/pdf','pdf'" in APP
    assert "'application/vnd.openxmlformats-officedocument.wordprocessingml.document','zip'" in APP
    assert "'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'," in APP
    assert "reportRuntimeError(err,'export-pdf')" in APP
    assert "reportRuntimeError(err,'export-docx')" in APP
    assert "reportRuntimeError(err,'export-xlsx')" in APP

def test_v01020_download_bytes_uses_safe_filename_and_validation():
    assert "MapliniExportCore.validateBytes(bytes,kind)" in APP
    assert "MapliniExportCore.safeFileName(name)" in APP
    assert "Export validation failed" in APP

def test_v01020_process_delete_has_predelete_recovery_snapshot():
    assert "async function deleteProcess(id)" in APP
    assert "maplini_pre_delete_snapshot" in APP
    assert "MapliniReliabilityCore.makeEmergencySnapshot" in APP
    assert "saveLocal(true)" in APP
    assert "undo=[];redo=[];lastUndoSnapshot='';lastUndoAt=0" in APP

def test_v01020_cloud_delete_returns_status_and_reports_error():
    assert "async function deleteCloud(id)" in APP
    assert "return true" in APP
    assert "reportRuntimeError(e,'cloud-delete')" in APP
    assert "const cloudOk=await deleteCloud(id)" in APP

def test_v01020_export_core_validates_pdf_zip_and_filename():
    assert "bad-pdf-signature" in EXPORT_CORE
    assert "bad-zip-signature" in EXPORT_CORE
    assert "function safeFileName(name)" in EXPORT_CORE


def test_v01021_connector_persistence_format_is_preserved():
    assert "if(Array.isArray(l))" in STATE_CORE
    assert "return [sourceId,targetId,side,style]" in STATE_CORE
    assert "nodeIds.has(l[0])&&nodeIds.has(l[1])" in STATE_CORE

def test_v01021_workflow_core_loaded_and_history_centralized():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert '_WORKFLOW_CORE_PATH' in APP
    assert '__MAPLINI_WORKFLOW_CORE__' in APP
    assert 'MapliniWorkflowCore.emptyProcess' in APP
    assert "function resetHistory(){undo=[];redo=[];lastUndoSnapshot='';lastUndoAt=0;historyTransactionDepth=0;undoGestureSnapshot=null}" in APP
    assert APP.count("resetHistory();") >= 3

def test_v01021_critical_flow_e2e_when_node_available():
    import shutil
    node=shutil.which("node")
    if not node:return
    result=subprocess.run([node,str(ROOT/"tests"/"test_critical_flow_e2e.js")],cwd=ROOT,capture_output=True,text=True)
    assert result.returncode==0,result.stderr
    assert "critical flow E2E OK" in result.stdout

def test_v01021_workflow_core_when_node_available():
    import shutil
    node=shutil.which("node")
    if not node:return
    result=subprocess.run([node,str(ROOT/"tests"/"test_workflow_core.js")],cwd=ROOT,capture_output=True,text=True)
    assert result.returncode==0,result.stderr
    assert "workflow core OK" in result.stdout


def test_v01022_performance_core_is_loaded_and_injected():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert '_PERFORMANCE_CORE_PATH' in APP
    assert '__MAPLINI_PERFORMANCE_CORE__' in APP
    assert 'MapliniPerformanceCore.signature' in APP
    assert "MapliniPerformanceCore.rafOnce('responsive-layout'" in APP

def test_v01022_process_style_avoids_identical_rewrites():
    assert "let lastProcessStyleSignature=''" in APP
    assert "if(!force&&signature===lastProcessStyleSignature)return false" in APP
    assert "applyProcessStyle(true)" in APP

def test_v01022_process_list_render_is_signature_memoized():
    assert "let lastProcessListSignature=''" in APP
    assert "if(!force&&signature===lastProcessListSignature)return false" in APP
    assert "renderProcesses(true)" in APP

def test_v01022_resize_work_is_raf_coalesced():
    assert "function scheduleResponsiveLayout()" in APP
    assert "window.addEventListener('resize',scheduleResponsiveLayout,{passive:true})" in APP
    assert "requestAnimationFrame(syncResponsiveLayout)" not in APP

def test_v01022_performance_core_primitives_exist():
    assert "function signature(values)" in PERFORMANCE_CORE
    assert "function rafOnce(key,fn)" in PERFORMANCE_CORE
    assert "function debounce(fn,wait=120)" in PERFORMANCE_CORE


def test_v01023_mobile_core_is_loaded_and_injected():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert '_MOBILE_CORE_PATH' in APP
    assert '__MAPLINI_MOBILE_CORE__' in APP
    assert 'MapliniMobileCore.clientToLocal' in APP
    assert 'MapliniMobileCore.movedEnough' in APP

def test_v0130_mobile_canvas_uses_custom_pan_and_pinch():
    html=_template()
    assert '#p48-canvas{touch-action:none!important}' in html
    assert 'const mobilePointers=new Map()' in APP
    assert 'MapliniMobileCore.gestureMidpoint' in APP
    assert 'MapliniMobileCore.pinchScale' in APP
    assert "scroll.scrollLeft=Math.max(0,mobileGesture.left-(p.x-mobileGesture.x))" in APP
    assert "canvas.classList.toggle('p48-selection-mode',selectionMode)" in APP
    assert "canvas.classList.remove('p48-selection-mode')" in APP


def test_v0130_mobile_bottom_bar_and_touch_targets():
    html=_template()
    for control in ('p48-mobile-add','p48-mobile-undo','p48-mobile-fit','p48-mobile-more','p48-mobile-next','p48-mobile-format','p48-mobile-duplicate','p48-mobile-context','p48-mobile-delete'):
        assert f'id="{control}"' in html
    assert 'height:clamp(520px,68dvh,760px)!important' in html
    assert '.p48-link-hit-segment{height:44px!important;min-height:44px!important}' in html
    assert "if(!isMobileLayout()||selectionMode||e.pointerType!=='touch'||mobileGestureBlocked(e.target))return;" in APP
    assert "mobileBar.dataset.mode=selectedMode?'selected':'normal'" in APP

def test_v01023_real_resize_selector_gets_touch_behavior():
    html=_template()
    mobile=html[html.index("/* v0.10.12 mobile shell"):html.index(".p48-canvas-menu{")]
    assert ".p48-node,.p48-handle,.p48-resize,.p48-link-hit-segment{touch-action:none}" in mobile
    assert ".p48-resize-handle" not in mobile
    assert ".p48-resize::after" in mobile

def test_v01023_scrolled_canvas_coordinates_are_not_double_counted():
    assert "function clientToCanvas(clientX,clientY)" in APP
    assert "MapliniMobileCore.clientToLocal(clientX,clientY,canvas.getBoundingClientRect())" in APP
    assert "clientX-r.left+scroll.scrollLeft" not in APP
    assert "clientX-rect.left+scroll.scrollLeft" not in APP
    assert "const p=clientToCanvas(e.clientX,e.clientY);addNode(payload.type,p.x,p.y,{objectRole:payload.objectRole});" in APP

def test_v01023_touch_drag_uses_larger_threshold_and_cancel_cleanup():
    assert "MapliniMobileCore.movedEnough(screenDx,screenDy,pointerType)" in APP
    assert "document.addEventListener('pointercancel',cancel)" in APP
    assert "releasePointerCapture" in APP

def test_v01023_mobile_core_primitives():
    assert "function clientToLocal(clientX,clientY,rect)" in MOBILE_CORE
    assert "function dragThreshold(pointerType)" in MOBILE_CORE
    assert "function movedEnough(dx,dy,pointerType)" in MOBILE_CORE


def test_v01024_selection_core_loaded_and_used():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert '_SELECTION_CORE_PATH' in APP
    assert '__MAPLINI_SELECTION_CORE__' in APP
    assert 'MapliniSelectionCore.deleteAction' in APP
    assert 'MapliniSelectionCore.afterLinkDelete' in APP

def test_v01024_clear_canvas_clears_stale_link_selection():
    chunk=APP[APP.index("function clearCanvas()"):APP.index("function restore(s)")]
    assert "selectedLinkIndex=null;selectedLinkIndices.clear()" in chunk
    assert "refreshLinkControls()" in chunk

def test_v01024_link_delete_reindexes_remaining_selection():
    assert "MapliniSelectionCore.afterLinkDelete" in APP
    assert "selectedLinkIndices=new Set(next.selectedLinkIndices)" in APP

def test_v01024_keyboard_delete_is_deterministic():
    assert "const action=MapliniSelectionCore.deleteAction" in APP
    assert "if(action==='many'||action==='node')" in APP
    assert "else if(action==='link')" in APP

def test_v01024_escape_and_undo_redo_refresh_context():
    assert "const had=MapliniSelectionCore.hasAny" in APP
    assert "if(had){e.preventDefault();clearSelection()}" in APP
    assert "restore(undo.pop());refreshControls();refreshLinkControls();updateSelectionUi();persist()" in APP
    assert "restore(redo.pop());refreshControls();refreshLinkControls();updateSelectionUi();persist()" in APP


def test_v01025_desktop_guard_is_present_without_mobile_selector_regression():
    assert 'APP_VERSION = "0.18.2"' in APP
    html=_template()
    assert "/* v0.10.25 desktop regression guard */" in html
    assert "grid-template-columns:220px minmax(0,1fr)!important" in html
    assert "transform:none!important" in html
    mobile=html[html.index("/* v0.10.12 mobile shell"):html.index(".p48-canvas-menu{")]
    assert "width:min(88vw,350px)!important" in mobile
    assert "overflow-x:auto!important" in mobile

def test_v01025_dead_outer_canvas_css_removed():
    prefix=APP[:APP.index('html = r"""')]
    assert ".p48-main,.p48-stage,.p48-canvas-wrap" not in prefix
    assert "#p48-canvas{min-width:2400px}" not in prefix


def test_v01026_sync_core_is_loaded_and_used():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert '_SYNC_CORE_PATH' in APP
    assert '__MAPLINI_SYNC_CORE__' in APP
    assert 'MapliniSyncCore.contentChanged' in APP
    assert 'MapliniSyncCore.mergeCloudRows' in APP
    assert 'MapliniSyncCore.signOutPlan' in APP

def test_v01026_recovery_promotes_backup_and_uses_pre_delete_last():
    chunk=APP[APP.index("function loadLocal()"):APP.index("let lastProcessListSignature")]
    assert "{key:'maplini_pre_delete_snapshot'" in chunk
    assert "lastLocalPayload=''" in chunk
    assert "const promoted=saveLocal(true)" in chunk

def test_v01026_save_local_returns_verified_status():
    chunk=APP[APP.index("function saveLocal"):APP.index("function loadLocal")]
    assert "localSaveDirty=true" in chunk
    assert "return false" in chunk
    assert "if(immediate)return flush()" in chunk

def test_v01026_cloud_merge_is_conflict_aware():
    chunk=APP[APP.index("async function loadCloudProcesses"):APP.index("function shareToken")]
    assert "select=id,name,data,updated_at" in chunk
    assert "MapliniSyncCore.mergeCloudRows" in chunk
    assert "merged.preservedLocalIds.length" in chunk

def test_v01026_cloud_save_uses_stable_snapshot():
    chunk=APP[APP.index("async function saveCurrentToCloud"):APP.index("async function loadCloudProcesses")]
    assert "const st=clone(processes[currentId]||state())" in chunk
    assert "name:st.name,data:st" in chunk
    assert "cloudUpdatedAt:updatedAt" in chunk
    assert "return {localOk,cloudOk:true,updatedAt}" in chunk

def test_v01026_signout_removes_unmodified_cloud_copies():
    chunk=APP[APP.index("function signOut()"):APP.index("function ownerId()")]
    assert "MapliniSyncCore.signOutPlan" in chunk
    assert "cloudLoadedProcessIds.clear()" in chunk
    assert "lokalt ändrade processer behölls" in chunk


def test_v01027_session_core_loaded_and_used():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert '_SESSION_CORE_PATH' in APP
    assert '__MAPLINI_SESSION_CORE__' in APP
    assert 'MapliniSessionCore.chooseWorkspace' in APP
    assert 'MapliniSessionCore.scopeKey' in APP

def test_v01027_invalid_session_resets_workspace_state():
    chunk=APP[APP.index("async function validateSession()"):APP.index("async function signIn()")]
    assert "cloudLoadedProcessIds.clear();cloudLoadedProcessScopes.clear()" in chunk
    assert "saveCloudSession(null);resetWorkspaceState()" in chunk

def test_v01027_signin_does_not_continue_after_failed_validation():
    chunk=APP[APP.index("async function signIn()"):APP.index("async function signUp()")]
    assert "const valid=await validateSession()" in chunk
    assert "if(!valid)throw new Error('Sessionen kunde inte verifieras.')" in chunk
    assert "await loadWorkspaces()" in chunk

def test_v01027_workspace_preference_is_user_scoped_and_validated():
    assert "function workspacePrefKey()" in APP
    chunk=APP[APP.index("async function loadWorkspaces()"):APP.index("async function createWorkspace()")]
    assert "loadWorkspacePreference()" in chunk
    assert "MapliniSessionCore.chooseWorkspace" in chunk
    assert "saveWorkspacePreference(currentWorkspaceId)" in chunk

def test_v01027_workspace_switch_does_not_keep_other_scope_cloud_copies():
    chunk=APP[APP.index("async function loadCloudProcesses()"):APP.index("function shareToken")]
    assert "const scope=MapliniSessionCore.scopeKey(currentWorkspaceId)" in chunk
    assert "const staleIds=[...cloudLoadedProcessScopes.entries()]" in chunk
    assert "MapliniSyncCore.signOutPlan(processes,staleIds,currentId)" in chunk
    assert "cloudLoadedProcessScopes.set(id,scope)" in chunk

def test_v01027_workspace_change_is_async_and_persists_choice():
    chunk=APP[APP.index("workspaceSelect.addEventListener('change'"):APP.index("createWorkspaceBtn.addEventListener")]
    assert "async()=>{" in chunk
    assert "saveWorkspacePreference(currentWorkspaceId)" in chunk
    assert "await loadCloudProcesses()" in chunk

def test_v01027_session_core_primitives():
    for fn in ("workspacePrefKey","scopeKey","chooseWorkspace","sessionState","scopedIds"):
        assert f"function {fn}" in SESSION_CORE


def test_v01028_rc_core_loaded_and_used():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert '_RC_CORE_PATH' in APP
    assert '__MAPLINI_RC_CORE__' in APP
    assert 'MapliniRcCore.captureScopeState' in APP
    assert 'MapliniRcCore.restoreScopeState' in APP
    assert 'MapliniRcCore.ensureCurrentId' in APP

def test_v01028_cloud_load_rolls_back_on_failure():
    chunk=APP[APP.index("async function loadCloudProcesses()"):APP.index("function shareToken")]
    assert "const before=MapliniRcCore.captureScopeState" in chunk
    assert "const restored=MapliniRcCore.restoreScopeState(before)" in chunk
    assert "Kunde inte läsa molnet · tidigare läge återställt" in chunk
    assert "return false" in chunk
    assert "return true" in chunk

def test_v01028_workspace_switch_checks_cloud_load_result():
    chunk=APP[APP.index("workspaceSelect.addEventListener('change'"):APP.index("createWorkspaceBtn.addEventListener")]
    assert "const ok=await loadCloudProcesses()" in chunk
    assert "if(ok)" in chunk
    assert "tidigare workspace återställt" in chunk

def test_v01028_lifecycle_save_is_observable():
    assert "function flushLifecycleSave(context)" in APP
    assert "Local lifecycle save failed" in APP
    assert "visibility-save" in APP
    assert "beforeunload-save" in APP

def test_v01028_share_failures_use_runtime_error_channel():
    chunk=APP[APP.index("async function shareCurrent()"):APP.index("async function loadShared")]
    assert "reportRuntimeError(e,'share-current')" in chunk

def test_v01028_rc_core_primitives():
    for fn in ("captureScopeState","restoreScopeState","ensureCurrentId","validateStoreInvariant"):
        assert f"function {fn}" in RC_CORE


def test_v01029_flow_core_loaded_and_used():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert '_FLOW_CORE_PATH' in APP
    assert '__MAPLINI_FLOW_CORE__' in APP
    assert 'MapliniFlowCore.sharedProcess' in APP
    assert 'MapliniFlowCore.afterProcessDelete' in APP

def test_v01029_delete_requires_verified_pre_snapshot():
    chunk=APP[APP.index("async function deleteProcess"):APP.index("function nodeText")]
    assert "const beforeOk=saveLocal(true)" in chunk
    assert "Radering avbruten · lokal säkerhetskopia kunde inte sparas" in chunk
    assert "maplini_pre_delete_snapshot" in chunk
    assert "pre-delete-snapshot" in chunk

def test_v01029_delete_cleans_scope_tracking_and_rolls_back_local_failure():
    chunk=APP[APP.index("async function deleteProcess"):APP.index("function nodeText")]
    assert "cloudLoadedProcessIds.delete(id)" in chunk
    assert "cloudLoadedProcessScopes.delete(id)" in chunk
    assert "MapliniStateCore.normalizeStore(snapshot)" in chunk
    assert "tidigare läge återställt" in chunk

def test_v01029_shared_view_validates_and_reports_errors():
    chunk=APP[APP.index("async function loadShared"):APP.index("async function deleteCloud")]
    assert "MapliniFlowCore.sharedProcess" in chunk
    assert "MapliniReliabilityCore.isUsableProcess(candidate)" in chunk
    assert "reportRuntimeError(e,'shared-load')" in chunk

def test_v01029_cloud_save_button_avoids_duplicate_preflush():
    chunk=APP[APP.index("root.querySelector('#p48-save').addEventListener"):APP.index("shareBtn.addEventListener")]
    owner_branch=chunk[chunk.index("if(ownerId())"):chunk.index("return;",chunk.index("if(ownerId())"))]
    assert "const result=await saveCurrentToCloud()" in owner_branch
    assert "persist(false)" not in owner_branch

def test_v01029_copy_fallback_reports_failure():
    assert "reportRuntimeError(copyErr,'share-copy')" in APP

def test_v01029_flow_core_primitives():
    assert "function sharedProcess" in FLOW_CORE
    assert "function afterProcessDelete" in FLOW_CORE


def test_v01030_access_core_loaded_and_used():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert '_ACCESS_CORE_PATH' in APP
    assert '__MAPLINI_ACCESS_CORE__' in APP
    assert "function canEdit(){return MapliniAccessCore.canEdit" in APP
    assert "function requireEdit(show=true)" in APP

def test_v01030_canvas_mutation_entry_points_are_guarded():
    assert "function addNode(type,x,y,options={}){" in APP
    add_idx=APP.index("function addNode(type,x,y,options={})")
    assert "if(!requireEdit())return;" in APP[add_idx:add_idx+260]
    assert "function updateStyle(patch){" in APP
    assert "if(!requireEdit())return;" in APP[APP.index("function updateStyle(patch)"):APP.index("function beginInlineEdit(el)")]
    assert "function deleteSelectedMany(){\n  if(!requireEdit())return;" in APP
    assert "function deleteLinkAt(index,withUndo=true){\n  if(!requireEdit())return false;" in APP
    assert "function beginInlineEdit(el){\n  if(!requireEdit())return;" in APP
    assert "el.addEventListener('pointerdown',e=>{\n  if(!canEdit())return;" in APP
    assert "Object.values(resizeHandles).forEach(rh=>rh.addEventListener('pointerdown',e=>{\n  if(!canEdit())return;" in APP
    assert "Object.values(handles).forEach(h=>h.addEventListener('pointerdown',e=>{\n  if(!canEdit())return;" in APP
    assert "function startSelectedLinkDrag(index,e)" in APP
    assert "if(!canEdit()||index==null||!links[index])return false;" in APP
    assert "linkHandle.addEventListener('pointerdown',e=>{if(selectedLinkIndex==null)return;startSelectedLinkDrag(selectedLinkIndex,e)})" in APP

def test_v01030_role_ui_disables_mutation_controls():
    chunk=APP[APP.index("function applyRoleUi()"):APP.index("async function loadWorkspaces()")]
    for selector in ("#p48-name","#p48-new","#p48-save","#p48-undo","#p48-redo","#p48-delete-selection",
                     "#p48-canvas-bg","#p48-bg-type","#p48-logo-file","#p48-logo-remove"):
        assert selector in chunk
    assert "canvas.classList.toggle('p48-readonly',!editable)" in chunk

def test_v01030_keyboard_mutations_require_edit_permission():
    keychunk=APP[APP.index("root.addEventListener('keydown'"):APP.index("font.addEventListener")]
    assert "if(mod&&key==='z'){if(!canEdit())return;" in keychunk
    assert "if(mod&&key==='y'){if(!canEdit())return;" in keychunk
    assert "if(e.key==='Delete'||e.key==='Backspace'){if(!canEdit())return;" in keychunk

def test_v01030_readonly_visual_handles_hidden():
    assert "#p48-canvas.p48-readonly .p48-handle" in APP
    assert "#p48-canvas.p48-readonly .p48-resize" in APP

def test_v01030_access_core_role_rules():
    assert "if(Boolean(state.sharedView))return false" in ACCESS_CORE
    assert "role==='owner'||role==='editor'" in ACCESS_CORE


def test_v01031_privacy_core_loaded_and_used():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert '_PRIVACY_CORE_PATH' in APP
    assert '__MAPLINI_PRIVACY_CORE__' in APP
    assert "MapliniPrivacyCore.shouldPersistLocally" in APP

def test_v01031_shared_view_persist_is_ephemeral():
    chunk=APP[APP.index("function persist(show=false,refreshList=false)"):APP.index("let lastUndoAt")]
    assert "if(sharedView)" in chunk
    shared=chunk[chunk.index("if(sharedView)"):chunk.index("if(MapliniSyncCore.contentChanged")]
    assert "saveLocal(" not in shared
    assert "return st" in shared

def test_v01031_lifecycle_never_writes_shared_public_process():
    chunk=APP[APP.index("function flushLifecycleSave(context)"):APP.index("document.addEventListener('visibilitychange'")]
    assert "if(!MapliniPrivacyCore.shouldPersistLocally({sharedView}))return true" in chunk

def test_v01031_set_format_enabled_cannot_reenable_viewer_controls():
    chunk=APP[APP.index("function setFormatEnabled(enabled)"):APP.index("function refreshControls")]
    assert "const editable=canEdit()" in chunk
    assert "el.disabled=!editable||!commonForLink" in chunk
    assert "el.disabled=!editable||!enabled" in chunk

def test_v01031_remaining_io_and_border_mutations_are_hard_guarded():
    assert "inp.addEventListener('change',()=>{if(!requireEdit())return;" in APP
    assert "del.addEventListener('click',()=>{if(!requireEdit())return;" in APP
    assert "addInputBtn.addEventListener('click',()=>{if(!requireEdit())return;" in APP
    assert "addOutputBtn.addEventListener('click',()=>{if(!requireEdit())return;" in APP
    border=APP[APP.index("borderColor.addEventListener"):APP.index("bold.addEventListener")]
    assert border.count("if(!requireEdit())return;") >= 2

def test_v01031_inline_edit_cancels_if_access_changes():
    chunk=APP[APP.index("function finishInlineEdit(el)"):APP.index("function makeNode")]
    assert "if(!canEdit())" in chunk
    assert "item.label.textContent=item.data.text||'Nytt steg'" in chunk
    assert "return;" in chunk

def test_v01031_privacy_core_rules():
    assert "return !Boolean(state.sharedView)" in PRIVACY_CORE
    assert "'ephemeral'" in PRIVACY_CORE


def test_v01032_save_local_has_privacy_guard():
    assert 'APP_VERSION = "0.18.2"' in APP
    chunk=APP[APP.index("function saveLocal(immediate=false)"):APP.index("function loadLocal()")]
    assert "if(!MapliniPrivacyCore.shouldPersistLocally({sharedView}))return true" in chunk

def test_v01032_shared_load_applies_central_readonly_ui():
    chunk=APP[APP.index("async function loadShared"):APP.index("async function deleteCloud")]
    assert "updateAccountUi();applyRoleUi();refreshControls();refreshLinkControls();updateSelectionUi();" in chunk
    assert "root.querySelector('#p48-new').disabled=true" not in chunk

def test_v01032_inline_input_does_not_mutate_state_before_commit():
    assert "label.addEventListener('input',()=>{const item=nodes.get(el.dataset.id);if(item&&canEdit()){invalidateNodeGeom(item.data.id);markNodeLinksDirty(item.data.id);drawLinks()}});" in APP
    assert "label.addEventListener('input',()=>{const item=nodes.get(el.dataset.id);if(item){item.data.text=label.innerText" not in APP

def test_v01032_async_logo_callback_rechecks_permission():
    chunk=APP[APP.index("logoFile.addEventListener('change'"):APP.index("size.addEventListener")]
    assert "reader.onload=()=>{" in chunk
    assert "if(!canEdit()){logoFile.value='';msg('Endast visning');return}" in chunk

def test_v01032_export_preflight_is_centralized_and_privacy_safe():
    assert "function prepareExport()" in APP
    chunk=APP[APP.index("function prepareExport()"):APP.index("function exportGoogleSheets()")]
    assert "persist(false,false)" in chunk
    assert "const localOk=saveLocal(true)" in chunk
    assert "export-preflight" in chunk
    pdf=APP[APP.index("async function exportPdf()"):APP.index("async function exportDoc()")]
    doc=APP[APP.index("async function exportDoc()"):APP.index("selectToolBtn.addEventListener")]
    assert "prepareExport()" in pdf
    assert "prepareExport()" in doc
    assert "persist(false,false);saveLocal(true)" not in pdf
    assert "persist(false,false);saveLocal(true)" not in doc

def test_v01032_direct_google_export_reports_runtime_error():
    chunk=APP[APP.index("function createGoogleSheetDirect()"):APP.index("root.querySelector('#p48-pdf')")]
    assert "reportRuntimeError(e,'google-sheets-direct')" in chunk


def test_v01033_process_logo_is_selectable_and_draggable():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert ".p48-process-logo.selected" in APP
    assert "processLogo.addEventListener('pointerdown'" in APP
    chunk=APP[APP.index("processLogo.addEventListener('pointerdown'"):APP.index("logoSize.addEventListener")]
    assert "if(!canEdit()" in chunk
    assert "clientToCanvas" in chunk
    assert "pushUndo(true)" in chunk
    assert "processLogoX=" in chunk and "processLogoY=" in chunk
    assert "persist()" in chunk
    assert "pointercancel" in chunk

def test_v01033_process_logo_position_persists():
    state=APP[APP.index("function state()"):APP.index("const LOCAL_KEY")]
    restore=APP[APP.index("function restore(s)"):APP.index("function openProcess")]
    assert "processLogoX" in state and "processLogoY" in state
    assert "processLogoX=Number.isFinite" in restore
    assert "processLogoY=Number.isFinite" in restore


def test_v01034_document_node_palette_and_state():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert 'data-type="document"' in APP
    assert "document:'Dokument'" in APP
    assert ".p48-node.document" in APP

def test_v01034_document_link_editor_and_safe_open():
    assert 'id="p48-document-url"' in APP
    assert "function safeDocumentUrl(value)" in APP
    assert "u.protocol!=='http:'&&u.protocol!=='https:'" in APP
    assert "function renderDocumentLink(item)" in APP
    assert "btn=document.createElement('a')" in APP
    assert "btn.target='_blank';btn.rel='noopener noreferrer'" in APP
    assert "documentUrlInput.addEventListener('change'" in APP

def test_v01034_document_link_does_not_start_node_drag():
    make=APP[APP.index("function makeNode(data)"):APP.index("function addNode(type")]
    assert "p48-doc-open" in make
    assert "e.target.classList.contains('p48-doc-open')" in make

def test_v01034_document_url_exports_to_sheets():
    assert "'Dokumentlänk'" in APP
    assert "d.type==='document'?(d.documentUrl||''):''" in APP


def test_v01035_document_link_is_native_anchor():
    assert "btn=document.createElement('a')" in APP
    assert "btn.target='_blank';btn.rel='noopener noreferrer'" in APP
    assert "if(valid)btn.href=valid;else btn.removeAttribute('href')" in APP
    assert "window.open(url,'_blank'" not in APP
    assert 'id="p48-document-open-editor"' in APP

def test_v01035_selection_emphasis_is_thinner():
    assert ".p48-node.selected{outline:2px solid #2c7be5!important" in APP
    assert ".p48-link-selection{stroke-width:5px!important;opacity:.22!important}" in APP

def test_v01035_scroll_has_bottom_clearance():
    html=_template()
    assert 'class="p48-scroll-bottom-spacer"' in html
    assert ".p48-scroll-bottom-spacer{width:1px;height:56px" in html
    assert '.p48-side::after{content:"";display:block;height:56px' in html


def test_v01036_selected_connector_can_be_dragged():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert "function startSelectedLinkDrag(index,e)" in APP
    assert "if(canEdit()){\n      startSelectedLinkDrag(hit,e);" in APP
    assert "startSelectedLinkDrag(hit,e)" in APP
    assert "linkHandle.addEventListener('pointerdown',e=>{if(selectedLinkIndex==null)return;startSelectedLinkDrag(selectedLinkIndex,e)})" in APP
    assert "MapliniConnectorCore.setFreeOffset(links,index,baseFreeDx+dx,baseFreeDy+dy)" in APP

def test_v01036_canvas_scale_controls_exist():
    html=_template()
    assert 'id="p48-zoom-out"' in html
    assert 'id="p48-zoom-reset"' in html
    assert 'id="p48-zoom-in"' in html
    assert "function applyCanvasScale(next,keepCenter=true)" in APP
    assert "Math.max(0.25,Math.min(1.5" in APP
    assert "transform:scale(var(--p48-canvas-scale,1))" in APP
    assert "screenDeltaToCanvas" in APP

def test_v01036_scaled_interactions_use_logical_canvas_coordinates():
    assert "return {x:p.x/canvasScale,y:p.y/canvasScale}" in APP
    assert "const {dx,dy}=screenDeltaToCanvas(screenDx,screenDy)" in APP
    assert "const p=clientToCanvas(ev.clientX,ev.clientY)" in APP


def test_v01037_background_library_controls():
    html=_template()
    assert 'APP_VERSION = "0.18.2"' in APP
    # v0.18.2 keeps a focused picker while preserving rendering support for legacy types.
    for value in ('dots','grid','solid','image','watermark'):
        assert f'value="{value}"' in html
    for legacy in ('lines','gradient','texture-paper','texture-parchment','texture-canvas','texture-concrete'):
        assert f"type==='{legacy}'" in APP
    assert 'id="p48-gradient-start"' in html
    assert 'id="p48-gradient-end"' in html
    assert 'id="p48-bg-image-file"' in html
    assert 'id="p48-watermark-text"' in html
    assert 'id="p48-watermark-use-logo"' in html

def test_v01037_background_state_persists():
    state=APP[APP.index("function state()"):APP.index("const LOCAL_KEY")]
    restore=APP[APP.index("function restore(s)"):APP.index("function openProcess")]
    for key in ("processGradientStart","processGradientEnd","processGradientAngle","processBackgroundImageData","processBackgroundImageOpacity","processWatermarkText","processWatermarkOpacity","processWatermarkUseLogo"):
        assert key in state
        assert key in restore

def test_v01037_background_image_is_size_guarded():
    assert "file.size>1500000" in APP
    assert "Bakgrundsbilden får vara max 1,5 MB" in APP

def test_v01037_export_supports_new_backgrounds():
    assert "processBackgroundType==='image'&&processBackgroundImageData" in APP
    assert "processBackgroundType==='watermark'&&processWatermarkUseLogo&&processLogoData" in APP
    assert "type==='gradient'" in APP
    assert "type.startsWith('texture-')" in APP


def test_document_node_add_link_opens_inline_editor():
    assert "function openDocumentInlineEditor(item)" in APP
    assert "msg('Klistra in dokumentlänken direkt i dokumentrutan')" in APP
    assert "item.docInlineInput.focus({preventScroll:true})" in APP
    render = APP[APP.index("function renderDocumentLink(item){"):APP.index("function state(){")]
    assert "openDocumentInlineEditor(item)" in render

def test_global_font_and_size_control_applies_both_to_all_nodes():
    text = Path('app.py').read_text(encoding='utf-8')
    assert 'Använd typsnitt + storlek på all text' in text
    assert 'const globalFont=font.value;' in text
    assert 'const globalSize=Math.max(10,Math.min(36,Number(size.value)||13));' in text
    assert 'item.data.fontFamily=globalFont;' in text
    assert 'item.data.fontSize=globalSize;' in text
    assert "msg('Typsnitt och storlek uppdaterat på all text')" in text


def test_node_secondary_text_inherits_typography():
    text = Path('app.py').read_text(encoding='utf-8')
    assert 'item.io.style.fontFamily=ts.fontFamily' in text
    assert "item.docOpen.style.fontFamily=s.fontFamily" in text

def test_v01040_dropdown_menus_close_on_outside_click():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert 'function closeOpenMenus(exceptTarget=null)' in APP
    assert "details.p48-canvas-menu[open]" in APP
    assert "details.p48-sheets-menu[open]" in APP
    assert "document.addEventListener('pointerdown',e=>closeOpenMenus(e.target),true)" in APP


def test_v01040_node_visual_style_controls_exist():
    html=_template()
    assert 'id="p48-node-style"' in html
    assert 'value="standard"' in html
    assert 'value="raised"' in html
    assert 'value="flat"' in html
    # v0.18.2 keeps 3D/Glass rendering for legacy processes but no longer offers them by default.
    assert 'value="3d"' not in html
    assert 'value="glass"' not in html
    assert 'id="p48-node-style-all"' in html


def test_v01040_node_styles_are_persisted_and_applied():
    assert "nodeStyleSelect.addEventListener('change',()=>updateStyle({nodeStyle:nodeStyleSelect.value}))" in APP
    assert "item.data.nodeStyle=chosen" in APP
    assert "p48-style-3d" in APP
    assert "p48-style-glass" in APP
    state=Path('maplini_state_core.js').read_text(encoding='utf-8')
    assert "['standard','3d','raised','glass','flat'].includes(n.nodeStyle)" in state


def test_v01040_export_knows_visual_styles():
    assert "s.nodeStyle==='3d'" in APP
    assert "s.nodeStyle==='raised'" in APP
    assert "s.nodeStyle==='glass'" in APP
    assert "s.nodeStyle==='flat'" in APP


def test_v01041_document_link_is_edited_inline_on_canvas():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert "function openDocumentInlineEditor(item)" in APP
    assert "p48-doc-inline-editor" in APP
    render = APP[APP.index("function renderDocumentLink(item){"):APP.index("function state(){")]
    assert "openDocumentInlineEditor(item)" in render
    assert "documentUrlInput.focus" not in render
    assert "Klistra in dokumentlänken direkt i dokumentrutan" in APP

def test_v01041_node_formatting_preserves_active_selection():
    chunk = APP[APP.index("function updateStyle(patch)"):APP.index("function beginInlineEdit(el)")]
    assert "const items=selectedNodeItems();if(!items.length)return;" in chunk
    assert "const keepIds=[...selectedIds],keepSelectedId=selectedId;" in chunk
    assert "selectedIds=new Set(keepIds.length?keepIds:items.map(x=>x.data.id));" in chunk
    assert "refreshControls();updateSelectionUi()" in chunk

def test_v01041_simplified_vertical_scroll_contract():
    assert "components.html(html, height=920, scrolling=False)" in APP
    assert ".p48-side{scrollbar-width:thin;overscroll-behavior:contain;scrollbar-color:#aab5bf transparent}" in APP
    assert "@media(max-width:900px),(pointer:coarse){.p48-side{scrollbar-width:none}.p48-side::-webkit-scrollbar{width:0;height:0;display:none}}" in APP
    assert ".p48-scroll{overscroll-behavior:contain;scrollbar-gutter:auto}" in APP

def test_v01042_connectors_follow_node_geometry_changes():
    assert 'item.el.style.left=(start.x+delta.dx)' in APP
    assert 'sync(item.el);invalidateNodeGeom(start.id);markNodeLinksDirty(start.id);' in APP
    assert 'item.data.width=box.width;item.data.height=box.height;invalidateNodeGeom(el.dataset.id);markNodeLinksDirty(el.dataset.id);drawLinks();' in APP
    assert 'invalidateNodeGeom(item.data.id);markNodeLinksDirty(item.data.id);' in APP
    assert 'drawLinks();persist();' in APP
    assert 'invalidateNodeGeom(item.data.id);\n  markNodeLinksDirty(item.data.id);\n  drawLinks();' in APP


def test_v01042_connector_visual_polish_contract():
    assert '.p48-link-visible{stroke-linecap:round!important;stroke-linejoin:round!important}' in APP
    assert 'const p=document.createElementNS(ns,\'polygon\'),len=7.5+sw*1.15,w=3.2+sw*.72;' in APP
    assert '.p48-link-selection{stroke-width:4px!important;opacity:.18!important;' in APP


def test_v01043_smart_connector_routing_controls_and_geometry():
    assert 'APP_VERSION = "0.18.2"' in APP
    html=_template()
    assert 'id="p48-link-routing"' in html
    assert 'id="p48-link-anchor-mode"' in html
    assert "function linkSides(link,A,B)" in html
    assert "function linkGeometry(link,A,B)" in html
    connector=(ROOT/'maplini_connector_core.js').read_text(encoding='utf-8')
    assert "routing:'orthogonal'" in connector
    assert "anchorMode:'auto'" in connector
    assert 'function routePoints(' in connector
    assert 'function autoSides(' in connector


def test_v01044_connector_labels_and_decision_defaults():
    assert 'id="p48-link-label"' in APP
    assert 'function linkLabelElement(st,points,selected=false)' in APP
    assert 'function decisionAutoLabel(sourceId)' in APP
    assert "{label:autoLabel}" in APP
    assert "setLinkStyle(selectedLinkIndex,{label:value})" in APP
    assert "const linkHeaders=['Från ID','Från steg','Till ID','Till steg','Anslutning','Piltext'];" in APP
    connector = (ROOT / 'maplini_connector_core.js').read_text(encoding='utf-8')
    assert "label:''" in connector
    assert "function decisionLabel(outgoingCount)" in connector

def test_v01045_insert_step_on_link_is_wired():
    text = APP
    assert 'APP_VERSION = "0.18.2"' in text
    assert 'id="p48-insert-link-step"' in text
    assert "function insertStepOnSelectedLink(type='process')" in text
    assert 'MapliniConnectorCore.splitLink(links,index,id)' in text
    assert "requestAnimationFrame(()=>beginInlineEdit(el))" in text


def test_v01046_insert_step_type_chooser():
    html = _template()
    soup = BeautifulSoup(html, "html.parser")
    menu = soup.select_one("#p48-insert-step-menu")
    assert menu is not None
    assert menu.has_attr("hidden")
    types = [x.get("data-insert-type") for x in menu.select("[data-insert-type]")]
    assert types == ["object", "process", "decision", "document", "end"]
    assert "function insertStepOnSelectedLink(type='process')" in APP
    assert "const allowed=new Set(['object','process','decision','document','end'])" in APP
    assert "makeNode({id,type,text:nodeText(type)" in APP
    assert "insertStepOnSelectedLink(btn.dataset.insertType)" in APP

def test_v01046_insert_step_menu_closes_outside():
    assert "if(insertLinkStepMenu&&!insertLinkStepMenu.hidden" in APP
    assert "setInsertStepMenu(false)" in APP


def test_v0110_faster_editing_copy_paste_duplicate():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert 'maplini_editing_core.js' in APP
    assert '__MAPLINI_EDITING_CORE__' in APP
    assert 'id="p48-duplicate-selection"' in APP
    assert 'function copySelectedNodes' in APP
    assert 'function pasteEditingClipboard' in APP
    assert 'function duplicateSelectedNodes' in APP
    assert "if(mod&&key==='c')" in APP
    assert "if(mod&&key==='v')" in APP
    assert "if(mod&&key==='d')" in APP
    assert 'MapliniEditingCore.makeClipboard' in APP
    assert 'MapliniEditingCore.instantiate' in APP


def test_v0111_multi_select_group_move_contract():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert "const groupIds=(selectedIds.size>1&&selectedIds.has(el.dataset.id))?[...selectedIds]:null;" in APP
    assert 'MapliniEditingCore.groupMoveDelta(startItems' in APP
    assert 'MapliniEditingCore.movedInternalVias(links,activeIds,0,0)' in APP
    assert 'suppressSelectClick=Boolean(groupIds)' in APP
    assert 'base.viaX+delta.dx' in APP
    assert 'base.viaY+delta.dy' in APP


def test_v0112_quick_next_step_contract():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert "className='p48-next-step-wrap'" in APP
    assert "function addNextStepFromNode(sourceId,type='process')" in APP
    assert 'MapliniEditingCore.nextStepPosition' in APP
    assert "links.push(MapliniConnectorCore.create(sourceId,id,'right',{label:autoLabel}))" in APP
    assert "requestAnimationFrame(()=>beginInlineEdit(el))" in APP
    assert "if(e.key==='Enter'&&!e.shiftKey)" in APP


def test_v0113_fit_screen_and_arrange_contract():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert 'id="p48-fit-screen"' in APP
    assert 'id="p48-arrange-menu"' not in APP
    assert 'MapliniEditingCore.fitToScreen' in APP
    assert 'MapliniEditingCore.alignNodes' in APP
    assert 'MapliniEditingCore.distributeNodes' in APP
    assert 'pushUndo(true)' in APP
    assert 'minScale:.25' in APP


def test_v0115_link_quick_routing_contract():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert 'id="p48-link-quick"' in APP
    assert 'data-link-routing="straight"' in APP
    assert 'data-link-routing="orthogonal"' in APP
    assert 'function applySelectedLinkRouting(routing)' in APP
    assert "routing==='straight'" in APP
    assert "btn.classList.toggle('active'" in APP
    assert "linkQuick.style.left=qp.x+'px'" in APP


def test_v0116_multi_select_formatting_contract():
    html = _template()
    assert 'APP_VERSION = "0.18.2"' in APP
    assert '.p48-format[data-context="multi"] .p48-single-node-only{display:none!important}' in html
    assert 'function selectedNodeItems()' in APP
    assert 'function sharedStyleValue(items,key)' in APP
    assert 'const multiNodeMode=!linkMode&&selectedIds.size>1' in APP
    assert 'ändringar gäller alla markerade' in APP
    chunk = APP[APP.index('function updateStyle(patch)'):APP.index('function beginInlineEdit(el)')]
    assert 'for(const item of items)' in chunk
    assert 'pushUndo();' in chunk
    assert 'selectedIds=new Set(keepIds.length?keepIds:items.map(x=>x.data.id));' in chunk
    assert "textColor.addEventListener('change'" in APP
    assert "bgColor.addEventListener('change'" in APP
    assert "borderColor.addEventListener('change'" in APP
    assert '[data-text-align]' in APP


def test_v0117_contextual_node_toolbar_contract():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert 'id="p48-node-quick"' in APP
    assert 'id="p48-node-quick-next"' in APP
    assert 'id="p48-node-quick-format"' in APP
    assert 'id="p48-node-quick-color"' in APP
    assert 'id="p48-node-quick-duplicate"' in APP
    assert 'id="p48-node-quick-arrange"' not in APP
    assert 'id="p48-node-quick-delete"' in APP
    assert 'function refreshNodeQuickToolbar()' in APP
    assert "nodeQuick.dataset.mode=multi?'multi':'single'" in APP
    assert "nodeQuickColor.addEventListener('change'" in APP
    assert "nodeQuickNext.addEventListener('click'" in APP
    assert "nodeQuickDuplicate.addEventListener('click'" in APP
    assert "nodeQuickDelete.addEventListener('click'" in APP
    assert "data-node-quick-align=\"left\"" not in APP
    assert "data-node-quick-distribute=\"horizontal\"" not in APP
    assert 'scale(var(--p48-toolbar-inverse-scale,1))' in APP
    assert "canvas.style.setProperty('--p48-toolbar-inverse-scale',String(1/value))" in APP


def test_v0120_smart_layout_integration():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert '_LAYOUT_CORE_PATH' in APP
    assert '__MAPLINI_LAYOUT_CORE__' in APP
    assert 'id="p48-smart-layout-menu"' in APP
    assert 'data-layout-scope="all"' in APP
    assert 'data-layout-scope="selected"' in APP
    assert 'function smartLayout(scope,orientation)' in APP
    assert 'MapliniLayoutCore.smartLayout' in APP


def test_v0131_autosave_recovery_contract():
    assert 'maplini_autosave_core.js' in APP
    assert "LOCAL_RECOVERY_KEY='maplini_recovery_v1'" in APP
    assert 'stageRecoverySnapshot()' in APP
    assert 'p48-save-state' in APP
    assert 'p48-recovery-banner' in APP
    assert "window.addEventListener('pagehide'" in APP
    assert "document.addEventListener('visibilitychange'" in APP
    assert 'restorePendingRecovery' in APP


def test_v0132_mobile_context_sheet_and_fullscreen_contract():
    html=_template()
    for control in ('p48-mobile-sheet','p48-mobile-sheet-backdrop','p48-mobile-context','p48-mobile-open-tools','p48-mobile-more','p48-mobile-sheet-copy','p48-mobile-sheet-layout-h','p48-mobile-sheet-layout-v'):
        assert f'id="{control}"' in html
    for node_type in ('start','process','decision','document','subprocess','note','end'):
        assert f'data-mobile-add="{node_type}"' in html
    assert 'p48-mobile-canvas-fullscreen' in html
    assert 'height:100dvh!important' in html
    assert "function setMobileSheet(mode=null)" in APP
    assert "function setMobileFullscreen(on,{fromBrowser=false}={})" in APP
    assert "mobileAdd.addEventListener('click',()=>setMobileSheet('add'))" in APP
    assert "mobileContext.addEventListener('click',()=>setMobileSheet('context'))" in APP
    assert "root.querySelectorAll('[data-mobile-add]')" in APP
    assert "smartLayout('selected','horizontal')" in APP
    assert "smartLayout('selected','vertical')" in APP


def test_v0133_contextual_toolbars_are_hidden_and_styled_inside_editor_iframe():
    assert 'APP_VERSION = "0.18.2"' in APP
    # The editor is rendered by components.html in its own iframe. These rules must
    # therefore exist in the raw editor HTML stylesheet, not only in st.markdown CSS.
    raw_html_start = APP.index('html = r"""')
    raw_html_end = APP.index('"""', raw_html_start + len('html = r"""'))
    editor_html = APP[raw_html_start:raw_html_end]
    assert '.p48-link-quick{position:absolute;z-index:82;display:none;' in editor_html
    assert '.p48-link-quick.on{display:flex}' in editor_html
    assert '.p48-node-quick{position:absolute;z-index:84;display:none;' in editor_html
    assert '.p48-node-quick.on{display:flex}' in editor_html
    assert '.p48-node-quick button,.p48-node-quick summary,.p48-node-quick .p48-quick-color-label' in editor_html
    assert '@media(max-width:700px),(pointer:coarse)' in editor_html


def test_v0141_connector_drag_horizontal_pages_and_zoom_contract():
    assert "if(canEdit())" in APP
    assert "if(selectedLinkIndex!==index)selectLink(index)" in APP
    assert "startSelectedLinkDrag(index,e)" in APP
    assert "updateCanvasExtentForPages" in APP
    assert "canvasLogicalWidth" in APP
    assert "count*spec.w" in APP
    assert "MapliniCanvasCore.zoomStep(canvasScale,'out')" in APP
    assert "MapliniCanvasCore.zoomStep(canvasScale,'in')" in APP
    assert 'aria-label="Zooma ut"' in APP
    assert 'aria-label="Zooma in"' in APP


def test_v0143_ui_simplification_and_scale_contract():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert 'id="p48-arrange-menu"' not in APP
    assert 'id="p48-node-quick-arrange"' not in APP
    assert 'id="p48-scale-menu"' in APP
    assert 'id="p48-process-scale"' in APP
    assert 'id="p48-process-scale-value"' in APP
    assert 'id="p48-scale-fit-page"' in APP
    assert 'function scaleWholeProcess(' in APP
    assert "function applyProcessScaleSlider(next)" in APP
    assert "scaleWholeProcess(ratio,false,false)" in APP
    assert "scaleWholeProcess(1,true)" in APP

def test_v0143_compact_account_and_logo_contract():
    assert 'id="p48-account-panel"' in APP
    assert 'class="p48-account-summary"' in APP
    assert 'id="p48-account-summary-state"' in APP
    assert 'id="p48-logo-menu"' in APP
    assert 'id="p48-logo-file"' in APP
    assert 'id="p48-logo-remove"' in APP
    assert 'id="p48-logo-hide"' in APP


def test_v0144_connector_drag_single_gesture_contract():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert "function startSelectedLinkDrag(index,e)" in APP
    assert "if(selectedLinkIndex!==index)selectLink(index)" in APP
    assert "startSelectedLinkDrag(index,e);" in APP
    assert "setPointerCapture(e.pointerId)" in APP
    assert "MapliniConnectorCore.setFreeOffset(links,index,baseFreeDx+dx,baseFreeDy+dy)" in APP


def test_v0145_stability_cleanup_contract():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert "width:canvasLogicalWidth,height:canvasLogicalHeight" in APP
    assert "const maxToolbarX=Math.max(120,canvasLogicalWidth-80)" in APP
    assert "function closeTransientMenus(except=null)" in APP
    assert "if(e.key!=='Escape')return" in APP
    assert "updateCanvasExtentForPages();" in APP
    assert "refreshNodeQuickToolbar();" in APP
    assert "if(typeof refreshLinkControls==='function')refreshLinkControls();" in APP
    # Removed UI must not keep live click handlers.
    assert "alignChoices.forEach(btn=>btn.addEventListener('click'" not in APP
    assert "distributeChoices.forEach(btn=>btn.addEventListener('click'" not in APP
    assert "nodeQuickAlign.forEach(btn=>btn.addEventListener('click'" not in APP
    assert "nodeQuickDistribute.forEach(btn=>btn.addEventListener('click'" not in APP


def test_v0146_free_connector_and_visual_polish_contract():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert '<option value="free">Fri</option>' in APP
    assert 'data-link-routing="free"' in APP
    assert "MapliniConnectorCore.setFreeOffset(links,index,baseFreeDx+dx,baseFreeDy+dy)" in APP
    assert "setLinkStyle(i,{routing,anchorMode:'auto',viaX:null,viaY:null,freeDx:0,freeDy:0})" in APP
    assert "patch.freeDx=(Number(s.freeDx)||0)*actualFactor" in APP
    assert ".p48-link-hit{cursor:move}" in APP



def test_v0147_workspace_owner_integrity_contract():
    assert "let currentWorkspaceId=null,currentWorkspaceOwnerId=null,currentRole='owner'" in APP
    assert "workspaces(id,name,owner_id)" in APP
    assert "o.dataset.ownerId=row.workspaces.owner_id||''" in APP
    assert "const canonicalOwnerId=currentWorkspaceId?currentWorkspaceOwnerId:ownerId()" in APP
    assert "owner_id:canonicalOwnerId" in APP
    migration = (ROOT / "supabase_schema_v0147.sql").read_text(encoding="utf-8")
    assert "owner_id=(select w.owner_id from public.workspaces w where w.id=processes.workspace_id)" in migration
    assert migration.count('drop policy if exists "workspace editors') == 2


def test_v0147_connector_drag_uses_pointer_delta_without_jump():
    assert "const baseFreeDx=startStyle.routing==='free'" in APP
    assert "const baseFreeDy=startStyle.routing==='free'" in APP
    assert "const dx=screenDx/canvasScale,dy=screenDy/canvasScale" in APP
    assert "MapliniConnectorCore.setFreeOffset(links,index,baseFreeDx+dx,baseFreeDy+dy)" in APP
    assert "p.x-midX" not in APP


def test_v0147_google_sheet_document_link_column_contract():
    google = (ROOT / "google_docs.py").read_text(encoding="utf-8")
    assert '"Text","Dokumentlänk","Inputs"' in google
    assert '("Processsteg",13)' in google
    assert "d.type==='document'?(d.documentUrl||''):''" in APP


def test_v0148_simplified_command_surface_contract():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert 'id="p48-export-menu"' in APP
    assert 'id="p48-more-menu"' in APP
    assert '>Exportera ▾<' in APP
    assert '>••• Mer<' in APP
    assert 'id="p48-pdf-view"' in APP and 'id="p48-page-count"' in APP
    assert 'id="p48-analyze"' in APP
    assert 'id="p48-select-tool"' in APP
    assert 'id="p48-mobile-more"' in APP
    assert 'id="p48-mobile-redo"' not in APP
    assert 'id="p48-mobile-fullscreen"' not in APP
    assert "if(mobileMore)mobileMore.addEventListener('click',()=>setMobileTools(true))" in APP
    # Export/page settings are grouped rather than permanently occupying the command surface.
    export_pos=APP.index('id="p48-export-menu"')
    pdf_view_pos=APP.index('id="p48-pdf-view"')
    export_close=APP.index('</details>', pdf_view_pos)
    assert export_pos < pdf_view_pos < export_close


def test_v0149_nested_menus_and_mobile_secondary_actions_contract():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert "const isAncestor=Boolean(except&&menu!==except&&menu.contains&&menu.contains(except));" in APP
    assert "if(menu&&menu!==except&&!isAncestor&&menu.open)menu.open=false;" in APP
    assert 'id="p48-mobile-sheet-redo"' in APP
    assert 'id="p48-mobile-sheet-fullscreen"' in APP
    assert 'id="p48-mobile-fullscreen"' not in APP
    assert 'id="p48-mobile-redo"' not in APP
    assert "if(mobileSheetRedo)mobileSheetRedo.addEventListener" in APP
    assert "if(mobileSheetFullscreen)mobileSheetFullscreen.addEventListener" in APP
    assert "const exportMenu=root.querySelector('#p48-export-menu');" in APP


def test_v0150_process_check_is_actionable_not_feature_creep():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert 'Vad behöver förbättras – och vad gör du åt det?' in APP
    assert 'BÖRJA HÄR' in APP
    assert '>Åtgärda</div>' in APP
    assert '>Förbättra</div>' in APP
    assert "Processkontroll klar · ${result.findings.length} saker att gå igenom" in APP
    # Existing analysis remains deterministic/local; no AI/API layer was introduced.
    assert 'MapliniProcessIntelligenceCore.analyze' in APP


def test_v0151_first_time_empty_canvas_contract():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert 'id="p48-empty-state"' in APP
    assert 'id="p48-empty-object"' in APP
    assert 'id="p48-empty-activity"' in APP
    assert 'Vad startar processen?' in APP
    assert 'function refreshEmptyState()' in APP
    assert 'emptyState.hidden=sharedView||nodes.size>0;' in APP
    assert "if(emptyObject)emptyObject.addEventListener('click',()=>addFirstStep('object','input'))" in APP
    assert "if(emptyActivity)emptyActivity.addEventListener('click',()=>addFirstStep('process'))" in APP
    assert "requestAnimationFrame(()=>beginInlineEdit(item.el))" in APP
    assert '.p48-empty-state[hidden]{display:none!important}' in APP


def test_v0152_new_process_dialog_replaces_browser_prompt():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert 'id="p48-new-process-dialog"' in APP
    assert 'id="p48-new-process-backdrop"' in APP
    assert 'id="p48-new-process-name"' in APP
    assert 'id="p48-new-process-create"' in APP
    assert 'id="p48-new-process-cancel"' in APP
    assert 'function setNewProcessDialog(open)' in APP
    assert 'function createNewProcessFromDialog()' in APP
    assert "function newProcess(){if(!requireEdit())return;setNewProcessDialog(true)}" in APP
    assert "prompt('Namn på den nya processen:'" not in APP
    assert "if(e.key==='Enter'){e.preventDefault();createNewProcessFromDialog()}" in APP
    assert "else if(e.key==='Escape'){e.preventDefault();setNewProcessDialog(false)}" in APP
    assert "newProcessName.value='Ny process'" in APP
    assert "newProcessName.focus();newProcessName.select()" in APP


def test_v0153_connector_labels_and_delete_visibility_contract():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert 'function linkLabelPlacement(points,offset=22)' in APP
    assert "const width=Math.min(300,Math.max(42,value.length*7.8+22)),height=26;" in APP
    assert "if(deleteNodeBtn)deleteNodeBtn.hidden=!(context==='node'&&selectedIds.size===1&&selectedId!=null);" in APP
    assert "linkLabel.addEventListener('input',()=>{" in APP
    assert "setLinkStyle(selectedLinkIndex,{label:value});" in APP
    assert "dirtyLinks.add(selectedLinkIndex);drawLinks();persistAfterIdle();" in APP
    assert "Never inject a standard Ja/Nej label" in APP
    assert "return '';" in APP[APP.index('function decisionAutoLabel'):APP.index('function selectedLinkMidpoint')]
    assert ".p48-link-label rect{fill:#fff;stroke:#c7d2dc" in APP
    assert ".p48-link-label text{font:750 12px/1 Inter" in APP


def test_v0154_selected_connector_affordances_do_not_stack():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert 'function linkQuickPlacement(points,st)' in APP
    assert "return linkLabelPlacement(points,hasLabel?-42:-32);" in APP
    assert 'function updateSelectedLinkUi(points,st)' in APP
    assert "linkQuick.style.left=qp.x+'px';linkQuick.style.top=qp.y+'px';" in APP
    assert 'if(selectedLinkIndex===index)updateSelectedLinkUi(points,st);' in APP
    assert 'transform:translate(-50%,-50%)' in APP


def test_v0155_connector_formatting_panel_is_self_contained():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert 'id="p48-link-width"' in APP
    assert 'id="p48-format-title"' in APP and 'Pil / koppling</div>' not in APP
    assert 'Inställningarna gäller bara den markerade pilen.' in APP
    assert '>Pilform<select id="p48-link-routing">' in APP
    assert '>Fästning<select id="p48-link-anchor-mode">' in APP
    assert 'Skriv valfri text för just denna pil' in APP
    assert 'class="p48-node-only"><label>Kantfärg</label><input id="p48-bordercolor"' in APP
    assert 'class="p48-node-only"><label>Kanttjocklek</label><select id="p48-borderwidth"' in APP
    assert "const commonForLink=(el===linkColor||el===linkWidth" in APP
    assert "if(linkWidth)linkWidth.addEventListener('change'" in APP
    assert "setLinkStyle(selectedLinkIndex,{width});" in APP
    assert "borderColor.value=linkColor.value" not in APP


def test_v0156_context_panel_titles_match_selection():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert 'id="p48-format-title"' in APP
    assert "formatTitle.textContent=context==='link'?'Pil'" in APP
    assert "context==='multi'?'Flera rutor'" in APP
    assert "context==='node'?'Ruta':'Formatering'" in APP
    assert "Ändra text, utseende och beteende för den markerade pilen." in APP
    assert "Ändra text och utseende för den markerade rutan." in APP
    assert 'class="p48-link-context-note"' in APP
    assert 'Pil / koppling</div>' not in APP


def test_v0157_typography_cleanup_preserves_legacy_fonts():
    assert 'APP_VERSION = "0.18.2"' in APP
    html = _template()
    font_start = html.index('<select id="p48-font">')
    font_end = html.index('</select>', font_start)
    font_html = html[font_start:font_end]
    for name in ('Inter','DM Sans','Poppins','Montserrat','Roboto','Georgia','system-ui'):
        assert f'value="{name}"' in font_html
    for removed in ('Pacifico','Caveat','Bebas Neue','Courier New','Nunito','Rubik'):
        assert f'value="{removed}"' not in font_html
    assert font_html.count('<option ') == 7
    assert 'function syncFontSelect(value)' in APP
    assert "option.textContent=`Tidigare typsnitt: ${wanted}`" in APP
    assert "option.dataset.legacyFont='true'" in APP
    assert "syncFontSelect(sharedStyleValue(items,'fontFamily')||s.fontFamily);" in APP


def test_v0158_canvas_background_cleanup_preserves_legacy_types():
    assert 'APP_VERSION = "0.18.2"' in APP
    html = _template()
    start = html.index('<select id="p48-bg-type">')
    end = html.index('</select>', start)
    bg_html = html[start:end]
    for value in ('solid','dots','grid','image','watermark'):
        assert f'value="{value}"' in bg_html
    for removed in ('gradient','lines','crosshatch','diagonal','technical','texture-paper','texture-parchment','texture-canvas','texture-concrete','none'):
        assert f'value="{removed}"' not in bg_html
    assert bg_html.count('<option ') == 5
    assert "const standardBackgroundTypes=new Set(['solid','dots','grid','image','watermark']);" in APP
    assert 'function syncBackgroundTypeSelect(value)' in APP
    assert "option.textContent=`Tidigare bakgrund: ${legacyBackgroundLabels[wanted]||wanted}`" in APP
    assert "option.dataset.legacyBackground='true'" in APP
    assert 'syncBackgroundTypeSelect(type);' in APP


def test_v0159_node_style_cleanup_preserves_legacy_styles():
    assert 'APP_VERSION = "0.18.2"' in APP
    html = _template()
    start = html.index('<select id="p48-node-style">')
    end = html.index('</select>', start)
    node_style_html = html[start:end]
    for value in ('standard','raised','flat'):
        assert f'value="{value}"' in node_style_html
    for removed in ('3d','glass'):
        assert f'value="{removed}"' not in node_style_html
    assert node_style_html.count('<option ') == 3
    assert "const standardNodeStyles=new Set(['standard','raised','flat']);" in APP
    assert 'function syncNodeStyleSelect(value)' in APP
    assert "option.textContent=`Tidigare rutstil: ${legacyNodeStyleLabels[wanted]||wanted}`" in APP
    assert "option.dataset.legacyNodeStyle='true'" in APP
    assert "syncNodeStyleSelect(sharedStyleValue(items,'nodeStyle')||s.nodeStyle);" in APP
    # Legacy rendering support must remain.
    assert "['standard','3d','raised','glass','flat']" in APP
    assert "s.nodeStyle==='3d'" in APP
    assert "s.nodeStyle==='glass'" in APP


def test_v01510_zoom_scales_entire_canvas_and_ctrl_multiselect():
    assert 'APP_VERSION = "0.18.2"' in APP
    # The zoom CSS must be inside the embedded editor template, not only parent Streamlit CSS.
    html = _template()
    assert '#p48-canvas{' in html
    assert 'transform:scale(var(--p48-canvas-scale,1))' in html
    assert 'transform-origin:0 0' in html
    assert '.p48-canvas-wrap{' in html
    # Ctrl/Cmd click toggles nodes in the current multi-selection.
    assert 'function toggleNodeSelection(el)' in APP
    assert 'if(e.ctrlKey||e.metaKey){e.preventDefault();toggleNodeSelection(el)}else select(el)' in APP
    assert 'e.preventDefault();e.stopPropagation();toggleNodeSelection(el);suppressSelectClick=true;return;' in APP
    assert "selectedId=selectedIds.size===1?[...selectedIds][0]:null;" in APP
    # Link controls must never leak into the no-selection state.
    assert '<div id="p48-link-format" class="p48-link-format" hidden>' in APP
    assert 'linkFormat.hidden=!link;' in APP
    assert '.p48-link-format[hidden]{display:none!important}' in APP


def test_v01511_first_view_a4_portrait_and_runtime_banner_policy():
    assert 'APP_VERSION = "0.18.2"' in APP
    html = _template()
    # Empty-state styling must exist inside iframe template.
    assert '.p48-empty-state{' in html
    assert '.p48-empty-card{' in html
    assert 'place-items:start center' in html
    # A4 portrait is the default.
    pdf_start = html.index('<select id="p48-pdf-view"')
    pdf_end = html.index('</select>', pdf_start)
    pdf_html = html[pdf_start:pdf_end]
    assert '<option value="A4P" selected>A4 stående</option>' in pdf_html
    assert '<option value="A3L">A3 liggande</option>' in pdf_html
    assert "let pdfView='A4P',pageCountMode='auto'" in APP
    assert "return specs[pdfView]||specs.A4P;" in APP
    # Generic browser/iframe errors are logged but should not show the red data-safety banner.
    assert "function reportRuntimeError(error,context='runtime',showBanner=true)" in APP
    assert "reportRuntimeError(e.error||e.message,'window.error',false)" in APP
    assert "reportRuntimeError(e.reason,'unhandledrejection',false)" in APP
    # A healthy restore clears a stale banner.
    assert 'requestFullLinkRender(true);refreshEmptyState();clearRuntimeError();' in APP


def test_v0160_object_activity_object_method_is_core_model():
    assert 'APP_VERSION = "0.18.2"' in APP
    html=_template()
    assert 'Bygg processen' in html
    assert 'Objekt → Aktivitet → Objekt' in html
    assert 'aria-label="Lägg till Objekt in"' in html
    assert 'aria-label="Lägg till Objekt ut"' in html
    assert html.count('data-type="object"') >= 2
    assert '.p48-node.object{' in html
    assert "object:'Nytt objekt'" in APP
    assert "['start','object','process','decision','document','subprocess']" in APP
    assert "const allowed=new Set(['object','process','decision','document','end']);" in APP
    assert "d.type==='process'" in APP and "['object','▪ Objekt / resultat']" in APP
    assert "d.type==='object'" in APP and "['process','▭ Aktivitet']" in APP
    state=(ROOT/'maplini_state_core.js').read_text(encoding='utf-8')
    assert "'start','object','process'" in state


def test_v0161_dependency_coach_flags_direct_activity_links():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert 'data-insert-type="object">▪ Objekt / resultat</button>' in APP
    assert "const allowed=new Set(['object','process','decision','document','end']);" in APP
    assert 'function coachDirectActivityLink(index)' in APP
    assert "from.type!=='process'||to.type!=='process'" in APP
    assert "Två aktiviteter är kopplade direkt." in APP
    assert 'coachDirectActivityLink(newIndex);' in APP
    core=(ROOT/'maplini_process_intelligence_core.js').read_text(encoding='utf-8')
    assert "direct_activity:'Kontrollera vad den första aktiviteten producerar." in core
    assert "from.type==='process'&&to.type==='process'" in core
    assert "'direct_activity','warning'" in core
    assert "linkIndex:l.index" in core


def test_v0162_scale_process_is_top_level_and_stays_open():
    assert 'APP_VERSION = "0.18.2"' in APP
    html=_template()
    soup=BeautifulSoup(html,"html.parser")
    scale=soup.select_one("#p48-scale-menu")
    assert scale is not None
    assert "p48-scale-menu-top" in scale.get("class",[])
    # Scale must be a top-level toolbar sibling, not buried inside More.
    assert scale.find_parent(id="p48-more-menu") is None
    assert scale.find_previous("details", id="p48-smart-layout-menu") is not None
    assert scale.find_next("details", id="p48-export-menu") is not None
    assert "Skala hela processen" in scale.get_text(" ",strip=True)
    # v0.18.2 replaces +/- with a persistent slider that keeps the menu open.
    assert 'id="p48-process-scale"' in APP
    assert "processScaleSlider.addEventListener('input'" in APP
    assert "if(scaleMenu)scaleMenu.open=true" in APP


def test_v0163_canvas_pan_scale_slider_and_real_node_dimensions():
    assert 'APP_VERSION = "0.18.2"' in APP
    html=_template()
    soup=BeautifulSoup(html,"html.parser")
    slider=soup.select_one("#p48-process-scale")
    assert slider is not None
    assert slider.get("type")=="range"
    assert slider.get("min")=="50"
    assert slider.get("max")=="150"
    assert slider.get("step")=="5"
    assert soup.select_one("#p48-scale-down") is None
    assert soup.select_one("#p48-scale-up") is None
    assert 'id="p48-process-scale-value"' in html
    assert "function applyProcessScaleSlider(next)" in APP
    assert "const ratio=target/processScalePercent;" in APP
    assert "processScaleSlider.addEventListener('input'" in APP
    # Node physical dimensions must escape CSS minimum/maximum constraints.
    assert "el.style.boxSizing='border-box';el.style.minWidth='0px';el.style.maxWidth='none';el.style.minHeight='0px';" in APP
    assert "if(d.width){" in APP and "el.style.maxWidth='none';el.style.width=d.width+'px';" in APP
    # Desktop blank-canvas drag pan.
    assert "function desktopPanBlankTarget(target)" in APP
    assert "scroll.classList.add('p48-desktop-pan-ready')" in APP
    assert "scroll.scrollLeft=Math.max(0,desktopPan.left-dx);" in APP
    assert "scroll.scrollTop=Math.max(0,desktopPan.top-dy);" in APP
    assert "if(desktopPanMoved){desktopPanMoved=false;" in APP


def test_v0164_blank_canvas_click_clears_selection_without_breaking_pan():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert "const wasClick=!desktopPanMoved;" in APP
    assert "if(wasClick&&!selectionMode){" in APP
    assert "clearSelection();clearLinkSelection();finishTempArrow();" in APP
    assert "if(desktopPanMoved){desktopPanMoved=false;e.preventDefault();e.stopPropagation();return}" in APP
    assert "if(desktopPanBlankTarget(e.target)||e.target===linkLayer)" in APP


def test_v0165_magnetic_alignment_and_properties_label():
    assert 'APP_VERSION = "0.18.2"' in APP
    html=_template()
    soup=BeautifulSoup(html,"html.parser")
    quick=soup.select_one("#p48-node-quick-format")
    assert quick is not None
    assert quick.get_text(strip=True)=="Egenskaper"
    assert "Öppna egenskaper för markerad ruta" in quick.get("title","")
    assert soup.select_one("#p48-snap-guide-x") is not None
    assert soup.select_one("#p48-snap-guide-y") is not None
    assert "const SNAP_GRID=10,SNAP_TOLERANCE=8;" in APP
    assert "function magneticSnap(" in APP
    assert "Math.round(x/SNAP_GRID)*SNAP_GRID" in APP
    assert "function straightenAlignedConnectedLinks(movedIds)" in APP
    assert "const alignedH=Math.abs(ay-by)<=1,alignedV=Math.abs(ax-bx)<=1;" in APP
    assert "const routing=(alignedH||alignedV)?'straight':'orthogonal';" in APP
    assert "showSnapGuides(snapped)" in APP
    assert "hideSnapGuides();" in APP


def test_v0166_clear_entire_canvas_requires_confirmation_and_is_undoable():
    assert 'APP_VERSION = "0.18.2"' in APP
    html=_template()
    soup=BeautifulSoup(html,"html.parser")
    btn=soup.select_one("#p48-clear-canvas")
    assert btn is not None
    assert btn.get_text(strip=True)=="Rensa hela canvasen"
    assert "function clearEntireCanvas()" in APP
    assert "if(!confirm('Är du säker på att du vill rensa hela canvasen? Alla rutor och kopplingar tas bort.'))return false;" in APP
    assert "pushUndo(true);" in APP
    assert "clearCanvas();" in APP
    assert "persist();" in APP
    assert "Canvasen rensades · Ångra återställer innehållet" in APP
    assert "clearCanvasBtn.addEventListener('click'" in APP


def test_v0167_smart_connector_polish_prefers_straight_axis_and_preserves_manual_routes():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert "function polishAutomaticConnectedLinks(movedIds,{forceAuto=false}={})" in APP
    assert "if(!forceAuto&&(st.routing==='free'||st.anchorMode!=='auto'))continue;" in APP
    assert "const routing=(alignedH||alignedV)?'straight':'orthogonal';" in APP
    assert "setLinkStyle(i,{routing,anchorMode:'auto',viaX:null,viaY:null,freeDx:0,freeDy:0})" in APP
    assert "polishAutomaticConnectedLinks(ids,{forceAuto:true});" in APP
    assert "polishAutomaticConnectedLinks([el.dataset.id,target.dataset.id],{forceAuto:true});" in APP
    assert "polishAutomaticConnectedLinks([sourceId,id],{forceAuto:true});" in APP


def test_v0168_object_roles_are_semantic_hints_not_separate_types():
    assert 'APP_VERSION = "0.18.2"' in APP
    html=_template()
    soup=BeautifulSoup(html,"html.parser")
    object_items=soup.select('.p48-method-palette [data-type="object"]')
    roles=[x.get("data-object-role") for x in object_items]
    assert "input" in roles and "output" in roles
    assert "data-object-role=\"input\"" in html
    assert "data-object-role=\"output\"" in html
    assert "el.dataset.objectRole=d.objectRole" in APP
    assert "objectRole" in APP
    assert "function addNode(type,x,y,options={})" in APP
    assert "objectRole:item.dataset.objectRole||null" in APP
    assert "source.data.type==='process'?'output':'intermediate'" in APP
    state=(ROOT/'maplini_state_core.js').read_text(encoding='utf-8')
    assert "objectRole:type==='object'" in state
    assert "type==='object'?'intermediate':undefined" in state


def test_v0169_fast_next_step_flow_uses_recommended_type_and_keeps_alternatives():
    assert 'APP_VERSION = "0.18.2"' in APP
    html=_template()
    soup=BeautifulSoup(html,"html.parser")
    assert soup.select_one("#p48-node-quick-next") is not None
    assert soup.select_one("#p48-node-quick-next-more") is not None
    assert "function preferredNextType(item)" in APP
    assert "if(type==='process')return'object';" in APP
    assert "if(['start','object','decision','document','subprocess'].includes(type))return'process';" in APP
    assert "if(type==='object')return'＋ Objekt ut';" in APP
    assert "if(type==='process')return'＋ Aktivitet';" in APP
    assert "if(item&&type)addNextStepFromNode(item.data.id,type);" in APP
    assert "if(item&&isNextStepSource(item)&&item.nextBtn)item.nextBtn.click();" in APP
    assert "if(e.key==='Enter'&&(e.ctrlKey||e.metaKey))" in APP


def test_v0170_process_flow_assistant_direct_activity_fix_and_override():
    assert 'APP_VERSION = "0.18.2"' in APP
    html=_template()
    soup=BeautifulSoup(html,"html.parser")
    assert soup.select_one("#p48-flow-coach") is not None
    assert soup.select_one("#p48-flow-coach-insert").get_text(strip=True).endswith("Infoga Objekt / resultat")
    assert soup.select_one("#p48-flow-coach-keep").get_text(strip=True)=="Behåll direktkoppling"
    assert "function isDirectActivityLink(index)" in APP
    assert "st.methodOverride!=='direct_activity_ok'" in APP
    assert "insertStepOnSelectedLink('object')" in APP
    assert "setLinkStyle(selectedLinkIndex,{methodOverride:'direct_activity_ok'})" in APP
    assert "f.code==='direct_activity'" in APP
    intel=(ROOT/'maplini_process_intelligence_core.js').read_text(encoding='utf-8')
    assert "methodOverride:String(style.methodOverride||'')" in intel
    assert "l.methodOverride!=='direct_activity_ok'" in intel


def test_v0171_auto_clean_process_chooses_direction_and_preserves_logic():
    assert 'APP_VERSION = "0.18.2"' in APP
    html=_template()
    soup=BeautifulSoup(html,"html.parser")
    btn=soup.select_one("#p48-auto-clean")
    assert btn is not None
    assert "Ordna processen automatiskt" in btn.get_text(" ",strip=True)
    assert "function preferredLayoutOrientation(ids=[...nodes.keys()])" in APP
    assert "verticalWeight>horizontalWeight*1.15?'vertical':'horizontal'" in APP
    assert "function autoCleanProcess()" in APP
    assert "const ok=smartLayout('all',orientation);" in APP
    assert "polishAutomaticConnectedLinks(ids,{forceAuto:true});" in APP
    assert "if(autoCleanBtn)autoCleanBtn.addEventListener('click'" in APP


def test_v0172_atomic_undo_for_destructive_and_layout_operations():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert "function recordUndoSnapshot(snapshot,force=false)" in APP
    assert "function runAtomicUndoOperation(operation)" in APP
    assert "function beginUndoGesture()" in APP
    assert "function endUndoGesture()" in APP
    assert "if(historyTransactionDepth>0)return false;" in APP
    assert "const changed=runAtomicUndoOperation(()=>{clearCanvas();persist();return true});" in APP
    assert "return runAtomicUndoOperation(()=>{" in APP
    assert "applyNodePositions(positions,scope==='selected'?'Markerade rutor snyggades till':'Processen snyggades till',false)" in APP
    assert "beginUndoGesture();processScaleGesture=true" in APP
    assert "if(processScaleGesture)endUndoGesture();" in APP


def test_v0173_canvas_performance_uses_local_geometry_cache_and_link_adjacency():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert "const nodeGeomRevision=new Map();" in APP
    assert "nodeGeomRevision.set(key,(nodeGeomRevision.get(key)||0)+1);" in APP
    assert "if(cached&&cached.rev===rev)return cached;" in APP
    assert "const linkIndicesByNode=new Map();" in APP
    assert "function rebuildLinkAdjacency()" in APP
    assert "if(linkAdjacencyReady)return linkIndicesByNode.get(key)||[];" in APP
    assert "rebuildLinkAdjacency();" in APP
    assert "let fastGeometryInteraction=false;" in APP
    assert "if(fastGeometryInteraction){" in APP
    assert "fastGeometryInteraction=true;" in APP
    assert "fastGeometryInteraction=false;" in APP
    assert "requestFullLinkRender(true);persist()" in APP


def test_v0174_build_flow_ux_polish_recommends_and_keeps_next_node_visible():
    assert 'APP_VERSION = "0.18.2"' in APP
    html=_template()
    soup=BeautifulSoup(html,"html.parser")
    assert soup.select_one("#p48-node-quick-flow") is not None
    assert "function workflowCue(item)" in APP
    assert "function ensureNodeVisible(el)" in APP
    assert "Aktivitet → ${nextLabel}" not in APP
    assert "nodeQuickFlow.textContent=source?workflowCue(items[0]):'';" in APP
    assert "b.classList.add('recommended')" in APP
    assert "Objekt ut" in APP
    assert "Ctrl+Enter fortsätter" in APP
    assert "ensureNodeVisible(el);beginInlineEdit(el)" in APP


def test_v0180_process_information_is_structured_and_backward_compatible():
    assert 'APP_VERSION = "0.18.2"' in APP
    html=_template()
    soup=BeautifulSoup(html,"html.parser")
    assert soup.select_one("#p48-process-info") is not None
    for field_id in ["p48-info-description","p48-info-role","p48-info-system","p48-info-duration","p48-info-kpi","p48-info-instruction","p48-info-risk","p48-info-control"]:
        assert soup.select_one("#"+field_id) is not None
    assert "MapliniProcessInfoCore.normalize" in APP
    assert "function renderProcessInfoEditor(item)" in APP
    assert "function saveProcessInfoField(key,value)" in APP
    assert "processInfo:MapliniProcessInfoCore.normalize({})" in APP


def test_v0181_process_info_panel_prioritizes_essentials_and_reuses_role_system_values():
    assert 'APP_VERSION = "0.18.2"' in APP
    html=_template()
    soup=BeautifulSoup(html,"html.parser")
    assert soup.select_one("#p48-process-info-more") is not None
    assert soup.select_one("#p48-role-suggestions") is not None
    assert soup.select_one("#p48-system-suggestions") is not None
    assert soup.select_one("#p48-info-role").get("list") == "p48-role-suggestions"
    assert soup.select_one("#p48-info-system").get("list") == "p48-system-suggestions"
    assert "function processInfoSuggestions(key)" in APP
    assert "renderSuggestionList(roleSuggestions,processInfoSuggestions('responsibleRole'))" in APP
    assert "renderSuggestionList(systemSuggestions,processInfoSuggestions('system'))" in APP
    assert "Frivilligt – fyll bara i det som är relevant" in APP
    assert "controls.querySelectorAll('select,input,textarea,button')" in APP


def test_v0182_objects_have_no_canvas_type_badge_and_label_can_start_drag():
    assert 'APP_VERSION = "0.18.2"' in APP
    assert "role.className='p48-object-role'" not in APP
    assert "role.textContent=d.objectRole" not in APP
    assert "el.dataset.objectRole=d.objectRole" in APP
    assert "e.target.classList.contains('p48-label')&&e.target.isContentEditable" in APP
    assert ".p48-label{display:block;width:100%;white-space:pre-wrap;overflow-wrap:anywhere;word-break:break-word;line-height:1.28;cursor:grab" in APP
