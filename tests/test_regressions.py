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
    assert "touch-action:pan-x pan-y" in html
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
    assert "components.html(html, height=1650" in APP


def test_connector_restore_is_normalized():
    assert "links=MapliniConnectorCore.normalizeLinks(d.links||[]);" in APP


def test_connector_create_delete_and_move_share_core_paths():
    assert "MapliniConnectorCore.create(el.dataset.id,target.dataset.id,side)" in APP
    assert "function deleteLinkAt(index,withUndo=true)" in APP
    assert "MapliniConnectorCore.removeAt(links,index)" in APP
    assert "MapliniConnectorCore.setVia(links,index,p.x,p.y)" in APP
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
    assert "const context=linkMode?'link':(enabled?'node':'none')" in APP


def test_v01015_step_io_only_visible_for_node_selection():
    html = _template()
    assert ".p48-step-io{display:none}" in html
    assert ".p48-step-io.on{display:block}" in html
    assert "stepIO.classList.toggle('on',enabled)" in APP


def test_v01015_mobile_palette_supports_tap_and_keyboard_add():
    html = _template()
    soup = BeautifulSoup(html, "html.parser")
    items = soup.select('.p48-item[role="button"][tabindex="0"]')
    assert len(items) == 7
    assert "function addFromPalette(item,{closeMobile=false}={})" in APP
    assert "if(isMobileLayout()){e.preventDefault();addFromPalette(i,{closeMobile:true})}" in APP
    assert "if(e.key==='Enter'||e.key===' ')" in APP
    assert "setMobileTools(false)" in APP


def test_v01015_mobile_palette_explains_tap_behavior():
    html = _template()
    assert "Tryck på en form för att lägga till den. På dator kan du även dra." in html
    assert "Lägg till på arbetsytan" in html


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
    assert 'APP_VERSION = "0.10.37"' in APP
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
    assert 'APP_VERSION = "0.10.37"' in APP
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
    assert 'APP_VERSION = "0.10.37"' in APP
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
    assert 'APP_VERSION = "0.10.37"' in APP
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
    assert 'APP_VERSION = "0.10.37"' in APP
    assert '_WORKFLOW_CORE_PATH' in APP
    assert '__MAPLINI_WORKFLOW_CORE__' in APP
    assert 'MapliniWorkflowCore.emptyProcess' in APP
    assert "function resetHistory(){undo=[];redo=[];lastUndoSnapshot='';lastUndoAt=0}" in APP
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
    assert 'APP_VERSION = "0.10.37"' in APP
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
    assert 'APP_VERSION = "0.10.37"' in APP
    assert '_MOBILE_CORE_PATH' in APP
    assert '__MAPLINI_MOBILE_CORE__' in APP
    assert 'MapliniMobileCore.clientToLocal' in APP
    assert 'MapliniMobileCore.movedEnough' in APP

def test_v01023_mobile_canvas_can_pan_until_selection_mode():
    html=_template()
    assert '#p48-canvas{touch-action:pan-x pan-y!important}' in html
    assert '#p48-canvas.p48-selection-mode{touch-action:none!important}' in html
    assert "canvas.classList.toggle('p48-selection-mode',selectionMode)" in APP
    assert "canvas.classList.remove('p48-selection-mode')" in APP

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
    assert "const p=clientToCanvas(e.clientX,e.clientY);addNode(type,p.x,p.y)" in APP

def test_v01023_touch_drag_uses_larger_threshold_and_cancel_cleanup():
    assert "MapliniMobileCore.movedEnough(screenDx,screenDy,pointerType)" in APP
    assert "document.addEventListener('pointercancel',cancel)" in APP
    assert "releasePointerCapture" in APP

def test_v01023_mobile_core_primitives():
    assert "function clientToLocal(clientX,clientY,rect)" in MOBILE_CORE
    assert "function dragThreshold(pointerType)" in MOBILE_CORE
    assert "function movedEnough(dx,dy,pointerType)" in MOBILE_CORE


def test_v01024_selection_core_loaded_and_used():
    assert 'APP_VERSION = "0.10.37"' in APP
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
    assert 'APP_VERSION = "0.10.37"' in APP
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
    assert 'APP_VERSION = "0.10.37"' in APP
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
    assert 'APP_VERSION = "0.10.37"' in APP
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
    assert 'APP_VERSION = "0.10.37"' in APP
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
    assert 'APP_VERSION = "0.10.37"' in APP
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
    assert 'APP_VERSION = "0.10.37"' in APP
    assert '_ACCESS_CORE_PATH' in APP
    assert '__MAPLINI_ACCESS_CORE__' in APP
    assert "function canEdit(){return MapliniAccessCore.canEdit" in APP
    assert "function requireEdit(show=true)" in APP

def test_v01030_canvas_mutation_entry_points_are_guarded():
    assert "function addNode(type,x,y){if(!requireEdit())return;" in APP
    assert "function updateStyle(patch){if(!requireEdit())return;" in APP
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
    assert 'APP_VERSION = "0.10.37"' in APP
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
    assert 'APP_VERSION = "0.10.37"' in APP
    chunk=APP[APP.index("function saveLocal(immediate=false)"):APP.index("function loadLocal()")]
    assert "if(!MapliniPrivacyCore.shouldPersistLocally({sharedView}))return true" in chunk

def test_v01032_shared_load_applies_central_readonly_ui():
    chunk=APP[APP.index("async function loadShared"):APP.index("async function deleteCloud")]
    assert "updateAccountUi();applyRoleUi();refreshControls();refreshLinkControls();updateSelectionUi();" in chunk
    assert "root.querySelector('#p48-new').disabled=true" not in chunk

def test_v01032_inline_input_does_not_mutate_state_before_commit():
    assert "label.addEventListener('input',()=>{const item=nodes.get(el.dataset.id);if(item&&canEdit())drawLinks();});" in APP
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
    assert 'APP_VERSION = "0.10.37"' in APP
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
    assert 'APP_VERSION = "0.10.37"' in APP
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
    assert 'APP_VERSION = "0.10.37"' in APP
    assert "function startSelectedLinkDrag(index,e)" in APP
    assert "if(selectedLinkIndex===hit&&canEdit())" in APP
    assert "startSelectedLinkDrag(hit,e)" in APP
    assert "linkHandle.addEventListener('pointerdown',e=>{if(selectedLinkIndex==null)return;startSelectedLinkDrag(selectedLinkIndex,e)})" in APP
    assert "MapliniConnectorCore.setVia(links,index,p.x,p.y)" in APP

def test_v01036_canvas_scale_controls_exist():
    html=_template()
    assert 'id="p48-zoom-out"' in html
    assert 'id="p48-zoom-reset"' in html
    assert 'id="p48-zoom-in"' in html
    assert "function applyCanvasScale(next,keepCenter=true)" in APP
    assert "Math.max(0.5,Math.min(1.5" in APP
    assert "transform:scale(var(--p48-canvas-scale,1))" in APP
    assert "screenDeltaToCanvas" in APP

def test_v01036_scaled_interactions_use_logical_canvas_coordinates():
    assert "return {x:p.x/canvasScale,y:p.y/canvasScale}" in APP
    assert "const {dx,dy}=screenDeltaToCanvas(screenDx,screenDy)" in APP
    assert "const p=clientToCanvas(ev.clientX,ev.clientY)" in APP


def test_v01037_background_library_controls():
    html=_template()
    assert 'APP_VERSION = "0.10.37"' in APP
    for value in ('dots','grid','lines','solid','gradient','image','watermark','texture-paper','texture-parchment','texture-canvas','texture-concrete'):
        assert f'value="{value}"' in html
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
