import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64
import google_docs
import maplini_google_ui

st.set_page_config(page_title="Maplini", page_icon="🧭", layout="wide", initial_sidebar_state="collapsed")
APP_VERSION = "0.18.3"
_LOGO_PATH = Path(__file__).resolve().parent / "assets" / "maplini_logo.png"
_LOGO_B64 = base64.b64encode(_LOGO_PATH.read_bytes()).decode("ascii") if _LOGO_PATH.exists() else ""
_SUPABASE = st.secrets.get("supabase", {})
_SUPABASE_URL = _SUPABASE.get("url", "")
_SUPABASE_ANON_KEY = _SUPABASE.get("publishable_key", _SUPABASE.get("anon_key", ""))
_PUBLIC_APP_URL = st.secrets.get("app", {}).get("public_url", "https://processkartan.streamlit.app")
_CLOUD_ENABLED = bool(_SUPABASE_URL and _SUPABASE_ANON_KEY)
_CONNECTOR_CORE_PATH = Path(__file__).resolve().parent / "maplini_connector_core.js"
_CONNECTOR_CORE_JS = _CONNECTOR_CORE_PATH.read_text(encoding="utf-8") if _CONNECTOR_CORE_PATH.exists() else ""
_CANVAS_CORE_PATH = Path(__file__).resolve().parent / "maplini_canvas_core.js"
_CANVAS_CORE_JS = _CANVAS_CORE_PATH.read_text(encoding="utf-8") if _CANVAS_CORE_PATH.exists() else ""
_UI_CORE_PATH = Path(__file__).resolve().parent / "maplini_ui_core.js"
_UI_CORE_JS = _UI_CORE_PATH.read_text(encoding="utf-8") if _UI_CORE_PATH.exists() else ""
_STATE_CORE_PATH = Path(__file__).resolve().parent / "maplini_state_core.js"
_STATE_CORE_JS = _STATE_CORE_PATH.read_text(encoding="utf-8") if _STATE_CORE_PATH.exists() else ""
_PROCESS_INFO_CORE_PATH = Path(__file__).resolve().parent / "maplini_process_info_core.js"
_PROCESS_INFO_CORE_JS = _PROCESS_INFO_CORE_PATH.read_text(encoding="utf-8") if _PROCESS_INFO_CORE_PATH.exists() else ""
_RELIABILITY_CORE_PATH = Path(__file__).resolve().parent / "maplini_reliability_core.js"
_RELIABILITY_CORE_JS = _RELIABILITY_CORE_PATH.read_text(encoding="utf-8") if _RELIABILITY_CORE_PATH.exists() else ""
_EXPORT_CORE_PATH = Path(__file__).resolve().parent / "maplini_export_core.js"
_EXPORT_CORE_JS = _EXPORT_CORE_PATH.read_text(encoding="utf-8") if _EXPORT_CORE_PATH.exists() else ""
_WORKFLOW_CORE_PATH = Path(__file__).resolve().parent / "maplini_workflow_core.js"
_WORKFLOW_CORE_JS = _WORKFLOW_CORE_PATH.read_text(encoding="utf-8") if _WORKFLOW_CORE_PATH.exists() else ""
_PERFORMANCE_CORE_PATH = Path(__file__).resolve().parent / "maplini_performance_core.js"
_PERFORMANCE_CORE_JS = _PERFORMANCE_CORE_PATH.read_text(encoding="utf-8") if _PERFORMANCE_CORE_PATH.exists() else ""
_MOBILE_CORE_PATH = Path(__file__).resolve().parent / "maplini_mobile_core.js"
_MOBILE_CORE_JS = _MOBILE_CORE_PATH.read_text(encoding="utf-8") if _MOBILE_CORE_PATH.exists() else ""
_SELECTION_CORE_PATH = Path(__file__).resolve().parent / "maplini_selection_core.js"
_SELECTION_CORE_JS = _SELECTION_CORE_PATH.read_text(encoding="utf-8") if _SELECTION_CORE_PATH.exists() else ""
_SYNC_CORE_PATH = Path(__file__).resolve().parent / "maplini_sync_core.js"
_SYNC_CORE_JS = _SYNC_CORE_PATH.read_text(encoding="utf-8") if _SYNC_CORE_PATH.exists() else ""
_SESSION_CORE_PATH = Path(__file__).resolve().parent / "maplini_session_core.js"
_SESSION_CORE_JS = _SESSION_CORE_PATH.read_text(encoding="utf-8") if _SESSION_CORE_PATH.exists() else ""
_RC_CORE_PATH = Path(__file__).resolve().parent / "maplini_rc_core.js"
_RC_CORE_JS = _RC_CORE_PATH.read_text(encoding="utf-8") if _RC_CORE_PATH.exists() else ""
_FLOW_CORE_PATH = Path(__file__).resolve().parent / "maplini_flow_core.js"
_FLOW_CORE_JS = _FLOW_CORE_PATH.read_text(encoding="utf-8") if _FLOW_CORE_PATH.exists() else ""
_ACCESS_CORE_PATH = Path(__file__).resolve().parent / "maplini_access_core.js"
_ACCESS_CORE_JS = _ACCESS_CORE_PATH.read_text(encoding="utf-8") if _ACCESS_CORE_PATH.exists() else ""
_PRIVACY_CORE_PATH = Path(__file__).resolve().parent / "maplini_privacy_core.js"
_PRIVACY_CORE_JS = _PRIVACY_CORE_PATH.read_text(encoding="utf-8") if _PRIVACY_CORE_PATH.exists() else ""
_EDITING_CORE_PATH = Path(__file__).resolve().parent / "maplini_editing_core.js"
_EDITING_CORE_JS = _EDITING_CORE_PATH.read_text(encoding="utf-8") if _EDITING_CORE_PATH.exists() else ""
_LAYOUT_CORE_PATH = Path(__file__).resolve().parent / "maplini_layout_core.js"
_LAYOUT_CORE_JS = _LAYOUT_CORE_PATH.read_text(encoding="utf-8") if _LAYOUT_CORE_PATH.exists() else ""
_AUTOSAVE_CORE_PATH = Path(__file__).resolve().parent / "maplini_autosave_core.js"
_AUTOSAVE_CORE_JS = _AUTOSAVE_CORE_PATH.read_text(encoding="utf-8") if _AUTOSAVE_CORE_PATH.exists() else ""
_PROCESS_INTELLIGENCE_CORE_PATH = Path(__file__).resolve().parent / "maplini_process_intelligence_core.js"
_PROCESS_INTELLIGENCE_CORE_JS = _PROCESS_INTELLIGENCE_CORE_PATH.read_text(encoding="utf-8") if _PROCESS_INTELLIGENCE_CORE_PATH.exists() else ""


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Caveat:wght@400;700&family=DM+Sans:wght@400;600;700&family=Fira+Sans:wght@400;600;700&family=Inter:wght@400;600;700;800&family=Lato:wght@400;700&family=Manrope:wght@400;600;700&family=Merriweather:wght@400;700&family=Montserrat:wght@400;600;700&family=Nunito:wght@400;600;700&family=Open+Sans:wght@400;600;700&family=Oswald:wght@400;600;700&family=Pacifico&family=Playfair+Display:wght@400;600;700&family=Poppins:wght@400;600;700&family=Quicksand:wght@400;600;700&family=Raleway:wght@400;600;700&family=Roboto:wght@400;500;700&family=Rubik:wght@400;600;700&family=Space+Grotesk:wght@400;600;700&family=Ubuntu:wght@400;500;700&display=swap');

.block-container{padding:0.35rem 0.45rem 0.8rem;max-width:none}
header[data-testid="stHeader"]{height:2rem}
#MainMenu,footer{visibility:hidden}


.p48-account-unified{background:#fff}
.p48-userline{display:flex;align-items:center;justify-content:space-between;gap:8px}
.p48-userline #p48-logout{min-height:30px;padding:5px 8px;white-space:nowrap}
.p48-account-divider{height:1px;background:#e2e7ec;margin:10px 0}
.p48-account-unified select{width:100%;border:1px solid #cfd7df;border-radius:7px;padding:7px 8px;font:12px system-ui;margin-top:5px;background:#fff}
.p48-new-workspace{margin-top:8px;border-top:1px solid #e7ebef;padding-top:7px}
.p48-new-workspace summary{cursor:pointer;font:700 11px system-ui;color:#445565;user-select:none}
.p48-new-workspace input{margin-top:7px}


/* v0.8.6: the main work area owns scrolling; a sticky horizontal navigator
   remains visible at the bottom of the editor viewport. */
.p48-scroll{
  overflow:auto !important;
  position:relative;
  height:var(--p48-desktop-body-h,640px);
  background:#e9eef3;
  scrollbar-gutter:stable;
}
.p48-canvas-wrap{
  overflow:visible !important;
  max-width:none !important;
  padding-bottom:0 !important;
}
.p48-hnav{
  position:sticky;
  left:0;
  bottom:0;
  z-index:90;
  height:22px;
  overflow-x:scroll;
  overflow-y:hidden;
  background:#f6f8fa;
  border-top:1px solid #cfd7df;
  box-shadow:0 -2px 6px rgba(28,43,58,.08);
}
.p48-hnav-inner{height:1px;width:2400px}
.p48-hnav::-webkit-scrollbar{height:16px}
.p48-hnav::-webkit-scrollbar-track{background:#e8edf1}
.p48-hnav::-webkit-scrollbar-thumb{background:#8797a5;border-radius:8px;border:3px solid #e8edf1}
.p48-hnav::-webkit-scrollbar-thumb:hover{background:#657684}


/* v0.8.7: editable node borders and connectors */
.p48-link-visible{fill:none;pointer-events:stroke}
.p48-link-hit{fill:none;stroke:transparent;stroke-width:16;pointer-events:stroke;cursor:pointer}
.p48-link-selected{filter:drop-shadow(0 0 2px rgba(44,123,229,.55))}
.p48-link-handle{position:absolute;width:15px;height:15px;border-radius:50%;background:#fff;border:2px solid #2c7be5;z-index:36;display:none;transform:translate(-50%,-50%);cursor:move}
.p48-link-handle.on{display:block}
.p48-link-quick{position:absolute;z-index:82;display:none;align-items:center;gap:4px;transform:translate(-50%,-50%);padding:4px;border:1px solid #c8d5e1;border-radius:9px;background:rgba(255,255,255,.98);box-shadow:0 5px 16px rgba(31,52,70,.16);pointer-events:auto;white-space:nowrap}
.p48-link-quick.on{display:flex}
.p48-link-quick button{border:1px solid transparent;border-radius:6px;background:transparent;color:#40556a;padding:5px 8px;font:700 10px system-ui;cursor:pointer}
.p48-link-quick button:hover{background:#eef5fb;border-color:#c7dced}
.p48-link-quick button.active{background:#e7f2fc;border-color:#86b3d8;color:#17639d}
.p48-link-quick button:disabled{opacity:.45;cursor:default}

.p48-node-quick{position:absolute;z-index:84;display:none;align-items:center;gap:4px;transform:translate(-50%,calc(-100% - 12px)) scale(var(--p48-toolbar-inverse-scale,1));transform-origin:50% 100%;padding:4px;border:1px solid #c8d5e1;border-radius:10px;background:rgba(255,255,255,.98);box-shadow:0 6px 18px rgba(31,52,70,.16);pointer-events:auto;white-space:nowrap}
.p48-node-quick.on{display:flex}
.p48-node-quick button,.p48-node-quick summary,.p48-node-quick .p48-quick-color-label{border:1px solid transparent;border-radius:7px;background:transparent;color:#40556a;padding:6px 8px;font:700 10px system-ui;cursor:pointer;list-style:none;display:inline-flex;align-items:center;gap:5px;min-height:30px;box-sizing:border-box}
.p48-node-quick button:hover,.p48-node-quick summary:hover,.p48-node-quick .p48-quick-color-label:hover{background:#eef5fb;border-color:#c7dced}
.p48-node-quick button.danger:hover{background:#fff1f2;border-color:#fecdd3;color:#b42318}
.p48-node-quick details{position:relative}
.p48-node-quick summary::-webkit-details-marker{display:none}
.p48-node-quick-arrange-pop{position:absolute;left:50%;top:calc(100% + 7px);transform:translateX(-50%);width:220px;padding:8px;border:1px solid #cbd7e3;border-radius:10px;background:#fff;box-shadow:0 10px 24px rgba(34,52,70,.18);display:grid;grid-template-columns:repeat(3,1fr);gap:5px;z-index:86}
.p48-node-quick-arrange-pop button{white-space:normal;justify-content:center;padding:6px 5px}
.p48-node-quick-arrange-pop .wide{grid-column:span 3}
.p48-quick-color-label input{width:18px;height:18px;border:0;padding:0;background:none;cursor:pointer}
.p48-node-quick[data-mode="single"] [data-multi-only],.p48-node-quick[data-mode="multi"] [data-single-only]{display:none!important}
@media(max-width:700px),(pointer:coarse){.p48-node-quick{gap:5px;padding:5px;transform:translate(-50%,calc(-100% - 16px)) scale(var(--p48-toolbar-inverse-scale,1));max-width:calc(100vw - 24px)}.p48-node-quick button,.p48-node-quick summary,.p48-node-quick .p48-quick-color-label{min-height:38px;padding:8px 10px;font-size:11px}.p48-node-quick-arrange-pop{width:236px}}
@media(max-width:700px),(pointer:coarse){.p48-link-quick{gap:5px;padding:5px;transform:translate(-50%,-50%)}.p48-link-quick button{min-height:36px;padding:7px 10px;font-size:11px}}

.p48-section{padding-top:12px;padding-bottom:12px}
.p48-section+.p48-section{border-top:1px solid #e9eef2}
.p48-title{letter-spacing:.01em}
.p48-toolbar .p48-btn,.p48-top .p48-btn{transition:background .12s ease,border-color .12s ease,box-shadow .12s ease}
.p48-btn:focus-visible,.p48-mini:focus-visible{outline:2px solid #2c7be5;outline-offset:2px}
.p48-link-hit-segment.p48-selected-link-hit{cursor:move}
.p48-link-hit{cursor:move}


/* v0.14.8 – simplified command surface */
.p48-top-simplified{gap:7px}
.p48-top-simplified .p48-icon-action{width:36px;padding-left:0;padding-right:0;font-size:17px}
.p48-export-menu,.p48-more-menu{position:relative}
.p48-export-menu>summary,.p48-more-menu>summary{list-style:none}
.p48-export-menu>summary::-webkit-details-marker,.p48-more-menu>summary::-webkit-details-marker{display:none}
.p48-export-popover,.p48-more-popover{position:absolute;top:calc(100% + 7px);right:0;z-index:190;background:#fff;border:1px solid #cbd7e3;border-radius:12px;box-shadow:0 12px 30px rgba(31,52,70,.18);padding:10px}
.p48-export-popover{width:270px;display:grid;gap:8px}
.p48-export-actions{display:grid;grid-template-columns:1fr 1fr;gap:7px}
.p48-export-popover select{width:100%;text-align:left}
.p48-export-page-title{margin-top:4px;padding-top:8px;border-top:1px solid #e5ebf0}
.p48-page-quick{position:sticky;top:10px;left:12px;z-index:175;width:max-content;margin:10px 0 -48px 12px}
.p48-page-quick>summary{list-style:none;cursor:pointer;min-height:34px;display:flex;align-items:center;padding:0 11px;border:1px solid #b9cbc4;border-radius:9px;background:rgba(255,255,255,.96);box-shadow:0 3px 12px rgba(31,52,70,.10);font:750 11px/1 Inter,system-ui;color:#315c4d;backdrop-filter:blur(6px)}
.p48-page-quick>summary::-webkit-details-marker{display:none}
.p48-page-quick[open]>summary{border-color:#74a391;box-shadow:0 4px 16px rgba(31,52,70,.14)}
.p48-page-quick-popover{position:absolute;top:calc(100% + 6px);left:0;width:220px;display:grid;gap:8px;padding:10px;background:#fff;border:1px solid #cbd7e3;border-radius:11px;box-shadow:0 12px 28px rgba(31,52,70,.17)}
.p48-page-quick-title{font:800 11px/1.2 Inter,system-ui;color:#243e35}
.p48-page-quick-popover label{display:grid;gap:4px;font:700 9px/1.2 Inter,system-ui;color:#64756e}
.p48-page-quick-popover select{width:100%;padding:7px 8px;border:1px solid #ccd8d2;border-radius:7px;background:#fff;font:600 11px Inter,system-ui;color:#273d35}
.p48-page-quick-hint{font:500 9px/1.4 Inter,system-ui;color:#73817b}
@media(max-width:700px){.p48-page-quick{top:7px;left:7px;margin-left:7px}.p48-page-quick>summary{min-height:32px;font-size:10px}.p48-page-quick-popover{width:205px}}
.p48-more-popover{width:300px;display:grid;gap:7px;max-height:min(70vh,620px);overflow:auto}
.p48-more-wide{width:100%;text-align:left}
.p48-more-selection-actions{display:grid;grid-template-columns:1fr 1fr;gap:7px}
.p48-more-popover>.p48-canvas-menu,.p48-more-popover>.p48-logo-menu,.p48-more-popover>.p48-scale-menu{position:relative;width:100%}
.p48-more-popover>.p48-canvas-menu>summary,.p48-more-popover>.p48-logo-menu>summary,.p48-more-popover>.p48-scale-menu>summary{width:100%;box-sizing:border-box;text-align:left}
.p48-more-popover .p48-canvas-popover,.p48-more-popover .p48-logo-popover,.p48-more-popover .p48-scale-popover{position:relative;top:auto;left:auto;right:auto;margin-top:6px;width:auto;min-width:0;box-shadow:none;border-color:#dbe3ea}
@media(max-width:900px){.p48-top-simplified .p48-spacer{display:none}.p48-export-popover,.p48-more-popover{right:auto;left:0}}


/* v0.15.6 contextual formatting panel */
.p48-format-context-title{margin-bottom:3px;font-size:13px}
.p48-format-context-hint{margin-bottom:10px}
.p48-link-context-note{margin:0 0 9px;padding:7px 8px;border-radius:7px;background:#f4f7f9;color:#60717f;font:600 10px/1.35 Inter,system-ui}
.p48-format[data-context="link"] .p48-format-context-title{color:#245f8e}
.p48-format[data-context="node"] .p48-format-context-title,.p48-format[data-context="multi"] .p48-format-context-title{color:#245e4b}
.p48-format[data-context="none"] .p48-format-context-hint{margin-bottom:0}

.p48-link-format{display:none;margin-top:12px;padding-top:10px;border-top:1px solid #e1e7ed}
.p48-link-format.on{display:block}
/* v0.15.10 selection-context safety */
.p48-link-format[hidden]{display:none!important}

/* v0.10.15 contextual formatting: show only controls relevant to current selection */
.p48-format[data-context="none"] #p48-controls{display:none}
.p48-format[data-context="node"] .p48-link-format,.p48-format[data-context="multi"] .p48-link-format{display:none!important}
.p48-format[data-context="multi"] .p48-single-node-only{display:none!important}
.p48-format[data-context="link"] .p48-node-only{display:none!important}
.p48-format[data-context="link"] .p48-link-format{display:block!important;margin-top:0;padding-top:0;border-top:0}
.p48-step-io{display:none}
.p48-step-io.on{display:block}
.p48-palette-hint{display:none;font:600 10px system-ui;color:#71808f;margin:-2px 0 8px}
@media(max-width:900px), (pointer:coarse) and (max-width:1100px){.p48-palette-hint{display:block}}
.p48-link-format-grid{display:grid;grid-template-columns:1fr 1fr;gap:7px}
.p48-link-format label{font:700 10px system-ui;color:#657281}
.p48-link-format input,.p48-link-format select{width:100%;margin-top:4px;border:1px solid #cfd7df;border-radius:7px;padding:6px;font:12px system-ui;background:#fff}
.p48-link-format .p48-link-label-field{grid-column:1/-1}
 .p48-flow-coach{margin:9px 0;padding:10px;border:1px solid #b9d8cc;border-radius:10px;background:#f2faf6;display:grid;gap:6px}
.p48-flow-coach[hidden]{display:none!important}
.p48-flow-coach-kicker{font:800 8px/1 Inter,system-ui;letter-spacing:.09em;color:#28715c}
.p48-flow-coach strong{font:800 11px/1.35 Inter,system-ui;color:#20364f}
.p48-flow-coach>span{font:500 10px/1.4 Inter,system-ui;color:#566b63}
.p48-flow-coach-actions{display:grid;grid-template-columns:1fr;gap:6px;margin-top:2px}
.p48-flow-coach-actions .p48-btn{width:100%;text-align:left}
.p48-insert-link-step{width:100%;margin-top:9px;border:1px solid #b9c8d8;border-radius:8px;padding:7px 9px;background:#f7fafc;color:#30445a;font:700 11px system-ui;cursor:pointer}
.p48-insert-link-step:hover{background:#eef5fb;border-color:#8eb4d8}
.p48-insert-step-wrap{position:relative}
.p48-insert-step-menu{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-top:6px;padding:7px;border:1px solid #cbd7e3;border-radius:9px;background:#fff;box-shadow:0 8px 20px rgba(34,52,70,.12)}
.p48-insert-step-menu[hidden]{display:none}
.p48-insert-step-choice{border:1px solid #d7e0e8;border-radius:7px;background:#f8fafc;color:#30445a;padding:8px 6px;font:700 11px system-ui;cursor:pointer;text-align:left}
.p48-insert-step-choice:hover{background:#eef5fb;border-color:#9bbbd8}
.p48-insert-step-choice:disabled{opacity:.45;cursor:not-allowed}
.p48-next-step-wrap{position:absolute;left:calc(100% + 10px);top:50%;transform:translateY(-50%);z-index:34;display:none;align-items:center;gap:6px;pointer-events:auto}
.p48-node.p48-next-visible .p48-next-step-wrap{display:flex}
.p48-next-step-btn{width:30px;height:30px;border:1px solid #9db8d2;border-radius:50%;background:#fff;color:#23679f;box-shadow:0 3px 10px rgba(35,61,84,.14);font:800 19px/1 system-ui;cursor:pointer;display:grid;place-items:center;padding:0}
.p48-next-step-btn:hover{background:#eef6fd;border-color:#6e9fc8}
.p48-next-step-menu{position:absolute;left:36px;top:50%;transform:translateY(-50%);width:178px;display:grid;grid-template-columns:1fr 1fr;gap:5px;padding:7px;border:1px solid #cbd7e3;border-radius:10px;background:#fff;box-shadow:0 10px 24px rgba(34,52,70,.16);z-index:35}
.p48-next-step-menu[hidden]{display:none}
.p48-next-step-choice{border:1px solid #d7e0e8;border-radius:7px;background:#f8fafc;color:#30445a;padding:8px 6px;font:700 11px system-ui;cursor:pointer;text-align:left;white-space:nowrap}
.p48-next-step-choice:hover{background:#eef5fb;border-color:#9bbbd8}
#p48-node-quick-next+#p48-node-quick-next-more{margin-left:-6px;min-width:28px;padding-left:6px;padding-right:6px;border-left-color:#dbe4ec}
.p48-node-quick-flow{display:inline-flex;align-items:center;min-height:30px;padding:0 8px;border:1px solid #d7e3dd;border-radius:8px;background:#f4faf7;color:#426658;font:750 9px/1.2 Inter,system-ui;white-space:nowrap}
.p48-next-step-choice.recommended{grid-column:1/-1;background:#f1f8f5;border-color:#a9cbbd;color:#245d4b;font-weight:800}
.p48-next-step-choice.recommended::after{content:"Rekommenderas";float:right;margin-left:8px;color:#618074;font:700 8px/1.2 Inter,system-ui;text-transform:uppercase;letter-spacing:.04em}
@media(max-width:700px){.p48-node-quick-flow{display:none!important}}


@media (max-width:700px){.p48-next-step-wrap{left:calc(100% + 6px)}.p48-next-step-btn{width:38px;height:38px;font-size:22px}.p48-next-step-menu{left:44px;width:188px}.p48-next-step-choice{min-height:38px}}
.p48-link-label rect{fill:#fff;stroke:#c7d2dc;stroke-width:1.2;filter:drop-shadow(0 2px 3px rgba(31,52,70,.14))}
.p48-link-label text{font:750 12px/1 Inter,system-ui,sans-serif;fill:#263b4d;dominant-baseline:middle;text-anchor:middle}.p48-link-selected .p48-link-label rect{filter:drop-shadow(0 2px 4px rgba(31,52,70,.18))}


/* v0.8.8 interaction cleanup */
.p48-handle{opacity:0;pointer-events:none;transition:opacity .12s ease}
.p48-node.selected .p48-handle,
.p48-node.multi-selected .p48-handle{opacity:1;pointer-events:auto}

/* Make connector hit area unambiguously clickable and above visible SVG path */
.p48-link-visible{pointer-events:none}
.p48-link-hit{
  fill:none;
  stroke:rgba(0,0,0,0.001);
  stroke-width:20;
  pointer-events:stroke;
  cursor:pointer;
}
#p48-links{pointer-events:auto}


.p48-link-selection{
  fill:none;
  stroke:#2c7be5;
  stroke-width:8;
  opacity:.28;
  pointer-events:none;
}


/* v0.9.0: robust HTML hit layer for connectors */
.p48-link-hit-layer{
  position:absolute;
  inset:0;
  z-index:4;
  pointer-events:none;
}
.p48-link-hit-segment{
  position:absolute;
  height:24px;
  transform-origin:0 50%;
  pointer-events:auto;
  cursor:pointer;
  background:transparent;
}
.p48-link-hit-segment:hover{
  background:rgba(44,123,229,.07);
}

/* Smaller configurable connection points */
/* v0.15.1 first-time empty canvas */
.p48-empty-state{position:absolute;inset:0;z-index:18;display:grid;place-items:center;pointer-events:none;padding:28px}
.p48-empty-state[hidden]{display:none!important}
.p48-empty-card{width:min(430px,calc(100% - 40px));padding:22px;border:1px solid #cddbe5;border-radius:16px;background:rgba(255,255,255,.96);box-shadow:0 16px 38px rgba(36,58,78,.14);text-align:center;pointer-events:auto}
.p48-empty-kicker{font:800 9px/1 Inter,system-ui;letter-spacing:.12em;color:#28715c;margin-bottom:7px}
.p48-empty-title{font:800 21px/1.2 Inter,system-ui;color:#20364f}
.p48-empty-copy{font:500 12px/1.5 Inter,system-ui;color:#60717f;margin:8px auto 15px;max-width:360px}
.p48-empty-actions{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.p48-empty-actions button{border:1px solid #b9c8d5;border-radius:9px;background:#fff;color:#294052;padding:10px 11px;min-height:42px;font:750 12px Inter,system-ui;cursor:pointer}
.p48-empty-actions button.primary{background:#1f6f55;border-color:#1f6f55;color:#fff}
.p48-empty-actions button:hover{filter:brightness(.98)}
.p48-empty-tip{margin-top:12px;padding-top:10px;border-top:1px solid #e5ebef;font:500 10px/1.45 Inter,system-ui;color:#74828e}
@media(max-width:700px),(pointer:coarse){.p48-empty-state{padding:14px;align-items:start;padding-top:72px}.p48-empty-card{width:min(100%,380px);padding:18px}.p48-empty-title{font-size:18px}.p48-empty-actions{grid-template-columns:1fr}.p48-empty-actions button{min-height:46px}}

#p48-canvas{
  --p48-point-size:8px;
  --p48-point-color:#1f6f55;
}
.p48-handle{
  box-sizing:border-box!important;
  width:var(--p48-point-size)!important;
  height:var(--p48-point-size)!important;
  background:var(--p48-point-color)!important;
  border:1px solid #fff!important;
  box-shadow:0 0 0 1px var(--p48-point-color)!important;
}
.p48-node .p48-handle.right{
  right:calc(var(--p48-point-size) / -2)!important;
}
.p48-node .p48-handle.left{
  left:calc(var(--p48-point-size) / -2)!important;
}
.p48-node .p48-handle.top{
  top:calc(var(--p48-point-size) / -2)!important;
}
.p48-node .p48-handle.bottom{
  bottom:calc(var(--p48-point-size) / -2)!important;
}
#p48-canvas.p48-hide-points .p48-handle{
  display:none!important;
}
.p48-point-settings{
  margin-top:10px;
  padding-top:10px;
  border-top:1px solid #e1e7ed;
}
.p48-point-settings .p48-point-grid{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:7px;
}
.p48-point-settings label{
  font:700 10px system-ui;
  color:#657281;
}
.p48-point-settings input,
.p48-point-settings select{
  width:100%;
  margin-top:4px;
  border:1px solid #cfd7df;
  border-radius:7px;
  padding:6px;
  font:12px system-ui;
  background:#fff;
}
.p48-hide-row{
  display:flex!important;
  align-items:center;
  gap:7px;
  margin-top:8px;
  font:600 11px system-ui!important;
  color:#445565!important;
}
.p48-hide-row input{
  width:auto!important;
  margin:0!important;
}


.p48-node .p48-handle{opacity:0!important;pointer-events:none!important}
.p48-node.selected .p48-handle{opacity:1!important;pointer-events:auto!important}
.p48-node.multi-selected:not(.selected) .p48-handle{opacity:0!important;pointer-events:none!important}


/* v0.10.42: connector follow + visual polish. Keep the visible line refined while preserving generous invisible hit targets. */
.p48-link-visible{stroke-linecap:round!important;stroke-linejoin:round!important}
.p48-link-hit-segment:hover{background:rgba(44,123,229,.035)!important}
.p48-link-selection{stroke-width:4px!important;opacity:.18!important;stroke-linecap:round!important;stroke-linejoin:round!important}
.p48-link-handle{width:12px!important;height:12px!important;border-width:2px!important;box-shadow:0 1px 4px rgba(31,42,55,.14)}
@media(max-width:900px),(pointer:coarse){.p48-link-handle{width:18px!important;height:18px!important}}

/* v0.10.35 fixes */
.p48-node.selected{outline:2px solid #2c7be5!important;outline-offset:2px!important;box-shadow:0 0 0 1px rgba(37,99,235,.10)!important}
.p48-node.multi-selected{outline:2px solid #2c7be5!important;outline-offset:2px!important;box-shadow:0 0 0 1px rgba(14,165,233,.08)!important}
.p48-node.decision.selected,.p48-node.decision.multi-selected{outline:none!important}
.p48-node.decision.selected::before{border-color:#2c7be5!important;box-shadow:0 0 0 1px rgba(44,123,229,.16)!important}
.p48-link-selection{stroke-width:5px!important;opacity:.22!important}
.p48-scroll-bottom-spacer{width:1px;height:56px;pointer-events:none}
.p48-side::after{content:"";display:block;height:56px;pointer-events:none}
.p48-document-open-editor{display:inline-block;margin-top:7px;color:#245d8d;font:700 11px system-ui;text-decoration:none}
.p48-document-open-editor:hover{text-decoration:underline}

/* v0.10.36 canvas scale + connector dragging */
.p48-zoom-controls{display:inline-flex;align-items:center;gap:3px}
.p48-zoom-controls .p48-btn{min-width:38px;padding-left:8px;padding-right:8px}
.p48-zoom-controls .p48-zoom-value{min-width:58px;font-variant-numeric:tabular-nums}
.p48-arrange-menu,.p48-smart-layout-menu{position:relative}.p48-arrange-menu>summary,.p48-smart-layout-menu>summary{list-style:none}.p48-arrange-menu>summary::-webkit-details-marker,.p48-smart-layout-menu>summary::-webkit-details-marker{display:none}
.p48-arrange-popover,.p48-smart-layout-popover{position:absolute;top:calc(100% + 7px);left:0;z-index:230;width:250px;padding:10px;background:#fff;border:1px solid #ccd6df;border-radius:10px;box-shadow:0 10px 30px rgba(30,45,60,.18)}
.p48-smart-layout-popover{width:230px}.p48-smart-layout-popover .p48-mini{width:100%;min-height:34px;margin-top:5px;text-align:left}.p48-smart-layout-popover .p48-mini:disabled{opacity:.42;cursor:not-allowed}.p48-smart-layout-popover #p48-auto-clean{min-height:40px;background:#1f6f55;color:#fff;border-color:#1f6f55;font-weight:800}
.p48-smart-layout-popover #p48-auto-clean:hover{filter:brightness(.98)}
.p48-auto-clean-hint{margin:6px 2px 1px;font-size:9px;line-height:1.35}
.p48-process-info{margin:0 0 10px;padding:10px;border:1px solid #dbe7e1;border-radius:11px;background:#f8fbf9}
.p48-process-info-head{display:flex;justify-content:space-between;gap:8px;align-items:flex-start;margin-bottom:8px}
.p48-process-info-progress{flex:0 0 auto;padding:3px 6px;border-radius:999px;background:#e6f1ec;color:#315f4e;font:800 9px/1 Inter,system-ui}
.p48-process-info label{display:grid;gap:4px;margin-top:7px;font-size:10px;font-weight:750;color:#44515d}
.p48-process-info input,.p48-process-info textarea{width:100%;box-sizing:border-box;border:1px solid #d3dce3;border-radius:7px;background:#fff;padding:7px 8px;font:500 11px/1.35 Inter,system-ui;color:#1f2933;resize:vertical}
.p48-process-info-grid{display:grid;grid-template-columns:1fr 1fr;gap:0 7px}
.p48-process-info-grid label:last-child{grid-column:1/-1}
.p48-process-info-more{margin-top:9px;border-top:1px solid #dfe9e4;padding-top:2px}
.p48-process-info-more>summary{cursor:pointer;list-style:none;padding:8px 0 5px;font:800 10px/1.3 Inter,system-ui;color:#345b4c}
.p48-process-info-more>summary::-webkit-details-marker{display:none}
.p48-process-info-more>summary::before{content:"＋";display:inline-block;width:16px;color:#4f7a69}
.p48-process-info-more[open]>summary::before{content:"−"}
.p48-process-info-more>summary span{font-weight:600;color:#718079}
.p48-process-info-foot{margin-top:8px;padding-top:7px;border-top:1px solid #e5ece8;font:500 9px/1.4 Inter,system-ui;color:#77847e}
@media(max-width:700px){.p48-process-info-grid{grid-template-columns:1fr}}
.p48-visual-details{margin:0 0 9px;border:1px solid #e0e6eb;border-radius:9px;padding:0 8px 8px;background:#fff}
.p48-visual-details>summary{cursor:pointer;padding:8px 0;font-size:10px;font-weight:800;color:#52606d}


.p48-arrange-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:5px}.p48-arrange-grid-two{grid-template-columns:repeat(2,1fr)}
.p48-arrange-grid .p48-mini{width:100%;height:auto;min-height:32px;padding:5px 6px}.p48-arrange-grid .p48-mini:disabled{opacity:.42;cursor:not-allowed}

.p48-canvas-wrap{width:var(--p48-canvas-visual-width,2400px)!important;height:var(--p48-canvas-visual-height,1400px)!important}
#p48-canvas{width:2400px!important;height:1400px!important;transform:scale(var(--p48-canvas-scale,1));transform-origin:0 0}
.p48-link-handle{width:18px;height:18px;z-index:80;touch-action:none;pointer-events:auto}
.p48-link-hit-segment.p48-selected-link-hit{cursor:move!important}
</style>
""", unsafe_allow_html=True)


html = r"""
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, maximum-scale=1">
<div id="pk48">
<style>
/* v0.10.12 mobile shell — real DOM + vertical scrolling */
.p48-mobile-tools-btn,.p48-mobile-backdrop,.p48-mobile-bar,.p48-mobile-sheet,.p48-mobile-sheet-backdrop{display:none}
.p48-node,.p48-handle,.p48-resize,.p48-link-hit-segment{touch-action:none}
.p48-scroll{overscroll-behavior:contain;-webkit-overflow-scrolling:touch}
button,summary,select,input{-webkit-tap-highlight-color:transparent}

/* v0.16.5 magnetic alignment — invisible grid with temporary snap guides */
.p48-snap-guide{position:absolute;z-index:4;pointer-events:none;background:rgba(31,111,85,.52)}
.p48-snap-guide[hidden]{display:none!important}
.p48-snap-guide-x{left:0;width:100%;height:1px}
.p48-snap-guide-y{top:0;height:100%;width:1px}

/* v0.16.2 process scale quick access */
.p48-scale-menu-top>summary{font-weight:750}
.p48-scale-menu-top[open]>summary{border-color:#9bb9ae;background:#f3f8f6}
.p48-scale-slider-label{display:flex;align-items:center;justify-content:space-between;margin:3px 0 7px;color:#405363;font:700 11px Inter,system-ui}
.p48-scale-slider-label strong{color:#176c52;font-size:12px}
.p48-process-scale-slider{width:100%;accent-color:#1f6f55;cursor:pointer}
.p48-scale-slider-marks{display:flex;justify-content:space-between;margin-top:3px;color:#83909a;font:600 9px Inter,system-ui}
.p48-scale-popover{min-width:245px}
.p48-scroll.p48-desktop-pan-ready{cursor:grab}
.p48-scroll.p48-desktop-panning{cursor:grabbing!important;user-select:none}
.p48-scroll.p48-desktop-panning *{cursor:grabbing!important}

/* v0.16.0 method-first palette */
.p48-method-flow{display:flex;align-items:center;justify-content:center;gap:5px;margin:8px 0 10px;padding:7px 5px;border-radius:8px;background:#f1f7f5;color:#315d51;font:700 9px/1.2 Inter,system-ui}
.p48-method-flow b{color:#83948f}
.p48-item-core{min-height:48px!important}
.p48-item-core>span:last-child{display:flex;flex-direction:column;gap:2px}
.p48-item-core small{display:block;font:500 9px/1.2 Inter,system-ui;color:#6d7b86}
.p48-item-object{border-color:#a9c8cf!important;background:#f8fbfc!important}
.p48-palette-more-label{margin:12px 0 5px;padding-top:9px;border-top:1px solid #e3e9ed;color:#71808b;font:800 9px/1 Inter,system-ui;text-transform:uppercase;letter-spacing:.08em}

/* v0.15.11 empty-process first view — must live inside the editor iframe. */
.p48-empty-state{
  position:absolute;
  inset:0;
  z-index:18;
  display:grid;
  place-items:start center;
  pointer-events:none;
  padding:72px 32px 32px;
  box-sizing:border-box;
}
.p48-empty-state[hidden]{display:none!important}
.p48-empty-card{
  width:min(460px,calc(100% - 48px));
  box-sizing:border-box;
  padding:24px;
  border:1px solid #cddbe5;
  border-radius:16px;
  background:rgba(255,255,255,.97);
  box-shadow:0 16px 38px rgba(36,58,78,.14);
  text-align:center;
  pointer-events:auto;
}
.p48-empty-kicker{font:800 10px/1 Inter,system-ui;letter-spacing:.12em;color:#28715c;margin-bottom:8px}
.p48-empty-title{font:800 22px/1.2 Inter,system-ui;color:#20364f;margin:0}
.p48-empty-copy{font:500 13px/1.5 Inter,system-ui;color:#60717f;margin:9px auto 17px;max-width:380px}
.p48-empty-actions{display:grid;grid-template-columns:1fr 1fr;gap:9px}
.p48-empty-actions button{
  border:1px solid #b9c8d5;border-radius:9px;background:#fff;color:#294052;
  padding:10px 12px;min-height:44px;font:750 12px Inter,system-ui;cursor:pointer;
}
.p48-empty-actions button.primary{background:#1f6f55;border-color:#1f6f55;color:#fff}
.p48-empty-actions button:hover{filter:brightness(.98)}
.p48-empty-tip{margin-top:13px;padding-top:11px;border-top:1px solid #e5ebef;font:500 11px/1.45 Inter,system-ui;color:#74828e}
@media(max-width:700px),(pointer:coarse){
  .p48-empty-state{padding:54px 14px 18px}
  .p48-empty-card{width:min(100%,390px);padding:19px}
  .p48-empty-title{font-size:19px}
  .p48-empty-actions{grid-template-columns:1fr}
  .p48-empty-actions button{min-height:46px}
}

/* v0.15.10 real canvas zoom — this MUST live inside the editor iframe.
   Scaling the canvas itself makes nodes, text, connectors, labels, logos and print guides
   grow/shrink as one visual unit. The wrapper carries the scaled scroll dimensions. */
.p48-canvas-wrap{
  width:var(--p48-canvas-visual-width,2400px)!important;
  height:var(--p48-canvas-visual-height,1400px)!important;
}
#p48-canvas{
  width:2400px!important;
  height:1400px!important;
  transform:scale(var(--p48-canvas-scale,1));
  transform-origin:0 0;
}

/* v0.13.3 contextual toolbar regression fix — these controls live inside the editor iframe.
   Keep their visibility and presentation rules in this iframe stylesheet, not only in Streamlit's parent document. */
.p48-link-quick{position:absolute;z-index:82;display:none;align-items:center;gap:4px;transform:translate(-50%,-50%);padding:4px;border:1px solid #c8d5e1;border-radius:9px;background:rgba(255,255,255,.98);box-shadow:0 5px 16px rgba(31,52,70,.16);pointer-events:auto;white-space:nowrap}
.p48-link-quick.on{display:flex}
.p48-link-quick button{border:1px solid transparent;border-radius:6px;background:transparent;color:#40556a;padding:5px 8px;font:700 10px system-ui;cursor:pointer}
.p48-link-quick button:hover{background:#eef5fb;border-color:#c7dced}
.p48-link-quick button.active{background:#e7f2fc;border-color:#86b3d8;color:#17639d}
.p48-link-quick button:disabled{opacity:.45;cursor:default}
.p48-node-quick{position:absolute;z-index:84;display:none;align-items:center;gap:4px;transform:translate(-50%,calc(-100% - 12px)) scale(var(--p48-toolbar-inverse-scale,1));transform-origin:50% 100%;padding:4px;border:1px solid #c8d5e1;border-radius:10px;background:rgba(255,255,255,.98);box-shadow:0 6px 18px rgba(31,52,70,.16);pointer-events:auto;white-space:nowrap}
.p48-node-quick.on{display:flex}
.p48-node-quick button,.p48-node-quick summary,.p48-node-quick .p48-quick-color-label{border:1px solid transparent;border-radius:7px;background:transparent;color:#40556a;padding:6px 8px;font:700 10px system-ui;cursor:pointer;list-style:none;display:inline-flex;align-items:center;gap:5px;min-height:30px;box-sizing:border-box}
.p48-node-quick button:hover,.p48-node-quick summary:hover,.p48-node-quick .p48-quick-color-label:hover{background:#eef5fb;border-color:#c7dced}
.p48-node-quick button.danger:hover{background:#fff1f2;border-color:#fecdd3;color:#b42318}
.p48-node-quick details{position:relative}
.p48-node-quick summary::-webkit-details-marker{display:none}
.p48-node-quick-arrange-pop{position:absolute;left:50%;top:calc(100% + 7px);transform:translateX(-50%);width:220px;padding:8px;border:1px solid #cbd7e3;border-radius:10px;background:#fff;box-shadow:0 10px 24px rgba(34,52,70,.18);display:grid;grid-template-columns:repeat(3,1fr);gap:5px;z-index:86}
.p48-node-quick-arrange-pop button{white-space:normal;justify-content:center;padding:6px 5px}
.p48-node-quick-arrange-pop .wide{grid-column:span 3}
.p48-quick-color-label input{width:18px;height:18px;border:0;padding:0;background:none;cursor:pointer}
.p48-node-quick[data-mode="single"] [data-multi-only],.p48-node-quick[data-mode="multi"] [data-single-only]{display:none!important}
@media(max-width:700px),(pointer:coarse){.p48-node-quick{gap:5px;padding:5px;transform:translate(-50%,calc(-100% - 16px)) scale(var(--p48-toolbar-inverse-scale,1));max-width:calc(100vw - 24px)}.p48-node-quick button,.p48-node-quick summary,.p48-node-quick .p48-quick-color-label{min-height:38px;padding:8px 10px;font-size:11px}.p48-node-quick-arrange-pop{width:236px}.p48-link-quick{gap:5px;padding:5px;transform:translate(-50%,-50%)}.p48-link-quick button{min-height:36px;padding:7px 10px;font-size:11px}}

/* v0.10.15 contextual sidebar */
.p48-format[data-context="none"] #p48-controls{display:none}
.p48-format[data-context="node"] .p48-link-format,.p48-format[data-context="multi"] .p48-link-format{display:none!important}
.p48-format[data-context="multi"] .p48-single-node-only{display:none!important}
.p48-format[data-context="link"] .p48-node-only{display:none!important}
.p48-format[data-context="link"] .p48-link-format{display:block!important;margin-top:0;padding-top:0;border-top:0}
.p48-step-io{display:none}
.p48-step-io.on{display:block}
.p48-palette-hint{display:none;font:600 10px system-ui;color:#71808f;margin:-2px 0 8px}

@media (max-width:900px), (pointer:coarse) and (max-width:1100px){
  html,body{
    width:100%;
    max-width:100%;
    overflow-x:hidden;
    overflow-y:visible!important;
    overscroll-behavior-y:auto;
    touch-action:pan-y;
  }
  #pk48{
    width:100%;
    max-width:100%;
    overflow-x:hidden;
    overflow-y:visible!important;
  }

  .p48-brand{height:68px!important;min-height:68px!important;padding:5px max(8px,env(safe-area-inset-right)) 5px max(8px,env(safe-area-inset-left))!important}
  .p48-logo-crop{width:205px!important;height:46px!important;overflow:visible!important}
  .p48-logo-crop img{width:205px!important;height:auto!important;object-fit:contain!important;transform:none!important}
  .p48-tagline{font-size:9px!important;line-height:1!important}
  .p48-version{font-size:9px!important;line-height:1!important}

  .p48-top{
    position:relative!important;z-index:180!important;display:flex!important;align-items:center!important;
    flex-wrap:nowrap!important;gap:7px!important;width:100%!important;max-width:100%!important;min-height:56px!important;
    overflow-x:auto!important;overflow-y:hidden!important;
    padding:6px max(8px,env(safe-area-inset-right)) 6px max(8px,env(safe-area-inset-left))!important;
    scrollbar-width:none;-webkit-overflow-scrolling:touch;background:#fff;
  }
  .p48-top::-webkit-scrollbar{display:none}
  .p48-top>*{flex:0 0 auto!important}
  .p48-top>strong{display:none!important}
  .p48-top .p48-btn,.p48-top select,.p48-top input{min-height:44px!important;font-size:16px!important}

  #p48-mobile-tools{order:-30}
  #p48-name{order:-29;width:145px!important;min-width:145px!important;max-width:145px!important}
  #p48-save{order:-28}
  #p48-new{order:-27}

  .p48-mobile-tools-btn{
    display:inline-flex!important;align-items:center!important;justify-content:center!important;
    position:sticky!important;left:0!important;z-index:8!important;background:#fff!important;
    box-shadow:5px 0 8px rgba(255,255,255,.95);
  }

  .p48-body{
    display:block!important;
    position:relative!important;
    width:100%!important;
    height:auto!important;
    min-height:0!important;
    overflow:visible!important;
  }
  .p48-scroll{
    position:relative!important;
    inset:auto!important;
    width:100%!important;
    height:clamp(520px,68dvh,760px)!important;
    min-height:520px!important;
    max-height:760px!important;
    overflow-x:auto!important;
    overflow-y:auto!important;
    background:#e9eef3!important;
    touch-action:none!important;
    -webkit-overflow-scrolling:touch;
    scrollbar-gutter:auto;
    z-index:1!important;
  }
  .p48-canvas-wrap{width:var(--p48-canvas-visual-width,2400px)!important;min-width:0!important;height:var(--p48-canvas-visual-height,1400px)!important;min-height:0!important} #p48-canvas{width:2400px!important;min-width:2400px!important;height:1400px!important;min-height:1400px!important}
  #p48-canvas{touch-action:none!important}
  #p48-canvas.p48-selection-mode{touch-action:none!important}
  .p48-canvas-wrap{padding-bottom:24px!important}

  .p48-side{
    display:block!important;position:absolute!important;top:0!important;left:0!important;bottom:0!important;
    width:min(88vw,350px)!important;height:100%!important;max-height:none!important;box-sizing:border-box!important;
    transform:translateX(-102%);visibility:hidden;pointer-events:none;
    transition:transform .18s ease,visibility 0s linear .18s;z-index:250!important;
    overflow-y:auto!important;overflow-x:hidden!important;
    padding-bottom:calc(20px + env(safe-area-inset-bottom))!important;background:#fff!important;
    box-shadow:0 12px 40px rgba(20,35,50,.24);
  }
  .p48-side.p48-mobile-open{transform:translateX(0);visibility:visible;pointer-events:auto;transition:transform .18s ease,visibility 0s}

  .p48-mobile-backdrop{display:none;position:absolute;inset:0;z-index:240;border:0;padding:0;margin:0;background:rgba(18,35,50,.28)}
  .p48-mobile-backdrop.on{display:block}

  .p48-side button,.p48-side select,.p48-side input{min-height:44px;font-size:16px!important}
  .p48-side input[type="color"]{min-height:44px}
  .p48-item{min-height:48px}
  .p48-palette-hint{display:block}
  .p48-node.selected .p48-handle{min-width:12px!important;min-height:12px!important}
  .p48-node.selected .p48-handle::after{content:"";position:absolute;inset:-8px;border-radius:50%}
  .p48-resize{min-width:16px!important;min-height:16px!important}
  .p48-resize::after{content:"";position:absolute;inset:-7px}

  .p48-canvas-popover,.p48-sheets-popover{
    position:fixed!important;left:10px!important;right:10px!important;top:auto!important;
    bottom:max(12px,env(safe-area-inset-bottom))!important;width:auto!important;max-width:none!important;
    max-height:70vh!important;max-height:70dvh!important;overflow:auto!important;z-index:320!important;
  }
  .p48-link-hit-segment{height:44px!important;min-height:44px!important}
  .p48-link-handle{width:24px!important;height:24px!important}
  .p48-link-handle::after{content:"";position:absolute;inset:-10px;border-radius:50%}
  .p48-mobile-bar{
    display:flex!important;position:fixed;left:max(8px,env(safe-area-inset-left));right:max(8px,env(safe-area-inset-right));
    bottom:max(8px,env(safe-area-inset-bottom));z-index:220;align-items:center;justify-content:space-between;gap:6px;
    padding:7px;border:1px solid #cbd6df;border-radius:14px;background:rgba(255,255,255,.97);
    box-shadow:0 8px 28px rgba(24,42,58,.22);backdrop-filter:blur(8px)
  }
  .p48-mobile-bar button{flex:1 1 0;min-width:0;min-height:46px;border:0;border-radius:9px;background:transparent;color:#31475b;font:750 11px system-ui;padding:5px 4px}
  .p48-mobile-bar button:active{background:#eaf2f8}
  .p48-mobile-bar .primary{background:#e9f4ef;color:#1f6f55}
  .p48-mobile-bar .danger{color:#a43d34}
  .p48-mobile-bar [data-mobile-group]{display:none}
  .p48-mobile-bar button[hidden]{display:none!important}
  .p48-mobile-bar[data-mode="normal"] [data-mobile-group="normal"],.p48-mobile-bar[data-mode="selected"] [data-mobile-group="selected"]{display:inline-flex;align-items:center;justify-content:center}
  .p48-mobile-sheet-backdrop{position:fixed!important;inset:0!important;z-index:330!important;border:0!important;background:rgba(18,35,50,.32)!important;padding:0!important;margin:0!important}
  .p48-mobile-sheet-backdrop.on{display:block!important}
  .p48-mobile-sheet{position:fixed!important;display:none;left:max(8px,env(safe-area-inset-left));right:max(8px,env(safe-area-inset-right));bottom:calc(72px + env(safe-area-inset-bottom));z-index:340;padding:12px;border:1px solid #cbd6df;border-radius:16px;background:#fff;box-shadow:0 14px 40px rgba(24,42,58,.28);max-height:min(62dvh,520px);overflow:auto}
  .p48-mobile-sheet.on{display:block!important}
  .p48-mobile-sheet-head{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:10px;font:800 14px system-ui;color:#263b4e}
  .p48-mobile-sheet-close{width:44px;height:44px;border:0;border-radius:10px;background:#eef3f7;font-size:20px}
  .p48-mobile-sheet-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
  .p48-mobile-sheet-grid button{min-height:48px;border:1px solid #d6e0e8;border-radius:11px;background:#f8fafc;color:#31475b;font:750 13px system-ui;padding:8px}
  .p48-mobile-sheet-grid button.primary{background:#e9f4ef;color:#1f6f55;border-color:#c8e1d7}
  .p48-mobile-sheet-grid button.danger{color:#a43d34;background:#fff8f7;border-color:#efcfcb}
  .p48-mobile-sheet-grid .wide{grid-column:1/-1}
  #pk48.p48-mobile-canvas-fullscreen{position:fixed!important;inset:0!important;z-index:9990!important;background:#e9eef3!important;width:100vw!important;height:100dvh!important;max-width:none!important;overflow:hidden!important}
  #pk48.p48-mobile-canvas-fullscreen .p48-brand,#pk48.p48-mobile-canvas-fullscreen .p48-top{display:none!important}
  #pk48.p48-mobile-canvas-fullscreen .p48-body{height:100dvh!important;overflow:hidden!important}
  #pk48.p48-mobile-canvas-fullscreen .p48-scroll{height:100dvh!important;min-height:100dvh!important;max-height:100dvh!important;padding-bottom:88px!important}
  #pk48.p48-mobile-canvas-fullscreen .p48-side{height:100dvh!important}
  #pk48.p48-mobile-canvas-fullscreen .p48-mobile-bar{bottom:max(8px,env(safe-area-inset-bottom))}
  .p48-scroll{padding-bottom:76px!important}
  .p48-hnav{display:none!important}
}
@media (max-width:480px){
  .p48-brand{height:62px!important;min-height:62px!important}
  .p48-logo-crop{width:180px!important;height:42px!important;overflow:visible!important}
  .p48-logo-crop img{width:180px!important;height:auto!important;object-fit:contain!important;transform:none!important}
  #p48-name{width:125px!important;min-width:125px!important;max-width:125px!important}
  .p48-body{height:auto!important;min-height:0!important}
  .p48-scroll{min-height:560px!important}
}

.p48-canvas-menu{position:relative;display:inline-block}
.p48-canvas-menu>summary{list-style:none;cursor:pointer;user-select:none}
.p48-canvas-menu>summary::-webkit-details-marker{display:none}
.p48-canvas-popover{position:absolute;top:calc(100% + 7px);left:0;z-index:220;width:260px;padding:12px;background:#fff;border:1px solid #ccd6df;border-radius:10px;box-shadow:0 10px 30px rgba(30,45,60,.18)}
.p48-pop-title{font-weight:800;margin-bottom:9px}

/* v0.10.2 — DOM-correct editor layout */
.p48-body{
  display:grid;
  grid-template-columns:220px minmax(0,1fr);
  height:var(--p48-desktop-body-h,640px);
  min-height:var(--p48-desktop-body-h,640px);
  overflow:hidden;
}
.p48-side{
  grid-column:1;
  min-width:0;
  height:var(--p48-desktop-body-h,640px);
  max-height:var(--p48-desktop-body-h,640px);
  box-sizing:border-box;
  overflow-y:auto;
  overflow-x:hidden;
  scroll-padding-bottom:72px;
}
.p48-scroll{
  grid-column:2;
  min-width:0;
  height:var(--p48-desktop-body-h,640px);
  overflow:auto;
  background:#e9eef3;
}
/* v0.10.41: one visible vertical editor scrollbar. The sidebar still scrolls with wheel/touch,
   but its duplicate scrollbar is hidden; scroll chaining to the iframe is prevented. */
.p48-side{scrollbar-width:thin;overscroll-behavior:contain;scrollbar-color:#aab5bf transparent}
.p48-side::-webkit-scrollbar{width:8px}
.p48-side::-webkit-scrollbar-track{background:transparent}
.p48-side::-webkit-scrollbar-thumb{background:#aab5bf;border-radius:8px;border:2px solid #fff}
@media(max-width:900px),(pointer:coarse){.p48-side{scrollbar-width:none}.p48-side::-webkit-scrollbar{width:0;height:0;display:none}}
.p48-scroll{overscroll-behavior:contain;scrollbar-gutter:auto}
.p48-canvas-wrap{
  position:relative;
  width:2400px;
  height:1400px;
  margin:0;
  padding:0;
}
#p48-canvas{
  position:relative;
  width:2400px;
  height:1400px;
  margin:0;
  padding:0;
}

/* v0.10.25 desktop regression guard */
@media (min-width:1101px), (min-width:901px) and (pointer:fine){
  .p48-mobile-tools-btn,.p48-mobile-backdrop{display:none!important}
  .p48-top{
    position:relative!important;
    display:flex!important;
    align-items:center!important;
    flex-wrap:wrap!important;
    overflow:visible!important;
    width:auto!important;
    max-width:none!important;
    min-height:0!important;
  }
  .p48-body{
    display:grid!important;
    grid-template-columns:220px minmax(0,1fr)!important;
    position:relative!important;
    width:auto!important;
    height:var(--p48-desktop-body-h,640px)!important;
    min-height:var(--p48-desktop-body-h,640px)!important;
    overflow:hidden!important;
  }
  .p48-side{
    grid-column:1!important;
    position:relative!important;
    inset:auto!important;
    width:auto!important;
    height:var(--p48-desktop-body-h,640px)!important;
    max-height:var(--p48-desktop-body-h,640px)!important;
    min-height:0!important;
    box-sizing:border-box!important;
    transform:none!important;
    visibility:visible!important;
    pointer-events:auto!important;
    overflow-y:scroll!important;
    overflow-x:hidden!important;
    overscroll-behavior:contain;
    scrollbar-gutter:stable;
    padding-bottom:72px!important;
    z-index:auto!important;
    box-shadow:none!important;
  }
  .p48-scroll{
    grid-column:2!important;
    position:relative!important;
    inset:auto!important;
    width:auto!important;
    height:var(--p48-desktop-body-h,640px)!important;
    min-height:var(--p48-desktop-body-h,640px)!important;
    max-height:var(--p48-desktop-body-h,640px)!important;
    overflow:auto!important;
    visibility:visible!important;
    pointer-events:auto!important;
    z-index:auto!important;
  }
}

/* visible version */
.p48-version{
  margin-top:2px;
  font:700 10px system-ui;
  color:#7a8792;
  letter-spacing:.03em;
}

/* v0.9.8: safe toolbar/dropdown additions only — no editor geometry overrides */
.p48-sheets-menu{
  position:relative;
  display:inline-block;
}
.p48-sheets-menu > summary{
  list-style:none;
  cursor:pointer;
  user-select:none;
}
.p48-sheets-menu > summary::-webkit-details-marker{display:none}
.p48-sheets-popover{
  position:absolute;
  right:0;
  top:calc(100% + 6px);
  z-index:150;
  min-width:210px;
  padding:7px;
  background:#fff;
  border:1px solid #cfd7df;
  border-radius:9px;
  box-shadow:0 8px 24px rgba(35,50,65,.16);
  display:grid;
  gap:6px;
}
.p48-sheets-popover .p48-btn{
  width:100%;
  text-align:left;
  white-space:nowrap;
}

/* v0.9.4 deeper performance pass */
.p48-node{transform:translateZ(0);backface-visibility:hidden}
.p48-link-visible,.p48-link-selection{vector-effect:non-scaling-stroke}
#p48-canvas{contain:layout paint style}

/* v0.9.3 performance hints */
.p48-node{contain:layout style;will-change:transform,left,top}
#p48-links{shape-rendering:geometricPrecision}
.p48-link-hit-segment{will-change:transform}

/* v0.9.2 formatting cleanup */
.p48-format-grid-clean{display:grid;grid-template-columns:1fr 1fr;gap:8px;align-items:end}
.p48-format-grid-clean label{font:700 10px system-ui;color:#657281}
.p48-format-grid-clean input,.p48-format-grid-clean select{width:100%;margin-top:4px}
.p48-text-format-block{margin-top:2px;padding:10px;border:1px solid #dbe3ea;border-radius:10px;background:#f8fafc}
.p48-text-format-block .p48-format-grid-clean{margin:0}
.p48-text-format-block .p48-actions{margin-top:8px}
.p48-text-format-block .p48-mini{background:#fff}
.p48-text-format-block .p48-text-tools-label{font:800 10px system-ui;color:#657281;margin:8px 0 2px}
.p48-process-style{margin-top:12px;padding-top:10px;border-top:1px solid #e1e7ed}
.p48-logo-controls{display:grid;grid-template-columns:1fr 1fr;gap:7px;margin-top:7px}
.p48-logo-controls button,.p48-logo-controls label{font:700 11px system-ui}
.p48-logo-upload{display:block;border:1px dashed #b9c5cf;border-radius:7px;padding:7px;text-align:center;cursor:pointer}
.p48-logo-upload input{display:none}
.p48-process-logo{position:absolute;left:28px;top:28px;max-width:220px;max-height:90px;object-fit:contain;z-index:6;pointer-events:none;display:none;user-select:none;-webkit-user-drag:none;touch-action:none}
.p48-process-logo.on{display:block;pointer-events:auto;cursor:grab}
.p48-process-logo.selected{outline:2px solid #2c7be5;outline-offset:5px;cursor:grabbing}
#p48-canvas.p48-readonly .p48-process-logo.on{pointer-events:none;cursor:default}

/* v0.9.1 critical editor rules inside iframe */
.p48-link-hit-layer{position:absolute;inset:0;z-index:4;pointer-events:none}
.p48-link-hit-segment{position:absolute;height:28px;transform-origin:0 50%;pointer-events:auto!important;cursor:pointer!important;background:transparent}
.p48-link-hit-segment:hover{background:rgba(44,123,229,.10)}
.p48-link-selection{fill:none;stroke:#2c7be5;stroke-width:10;opacity:.32;pointer-events:none}
.p48-node .p48-handle{opacity:0!important;pointer-events:none!important}
.p48-node.selected .p48-handle{opacity:1!important;pointer-events:auto!important}
.p48-node.multi-selected:not(.selected) .p48-handle{opacity:0!important;pointer-events:none!important}
#p48-canvas.p48-hide-points .p48-handle{display:none!important}
#p48-canvas.p48-readonly .p48-handle,#p48-canvas.p48-readonly .p48-resize{display:none!important}
#p48-canvas.p48-readonly .p48-node{cursor:default!important}
.p48-point-settings{margin-top:10px;padding-top:10px;border-top:1px solid #e1e7ed}
.p48-point-settings .p48-point-grid{display:grid;grid-template-columns:1fr 1fr;gap:7px}
.p48-point-settings label{font:700 10px system-ui;color:#657281}
.p48-point-settings input,.p48-point-settings select{width:100%;margin-top:4px;border:1px solid #cfd7df;border-radius:7px;padding:6px;font:12px system-ui;background:#fff}
.p48-hide-row{display:flex!important;align-items:center;gap:7px;margin-top:8px;font:600 11px system-ui!important;color:#445565!important}
.p48-hide-row input{width:auto!important;margin:0!important}

#pk48{font-family:Inter,system-ui,sans-serif;color:#17202a;background:#eef2f6;border:1px solid #dce2e8;border-radius:12px;overflow:hidden}
#pk48{position:relative}
.p48-analysis-panel{position:fixed;z-index:240;top:118px;right:18px;bottom:22px;width:min(380px,calc(100vw - 36px));display:flex;flex-direction:column;background:#fff;border:1px solid #cfd9e2;border-radius:14px;box-shadow:0 14px 38px rgba(31,52,70,.22);overflow:hidden}
.p48-analysis-panel[hidden]{display:none!important}
.p48-analysis-head{display:flex;align-items:flex-start;justify-content:space-between;gap:12px;padding:14px 14px 10px;border-bottom:1px solid #e2e8ee}
.p48-analysis-title{font:800 15px/1.2 Inter,system-ui,sans-serif;color:#20364f}.p48-analysis-sub{font:500 10px/1.35 Inter,system-ui,sans-serif;color:#6b7986;margin-top:3px}
.p48-analysis-close{border:1px solid #d7dfe6;background:#fff;border-radius:8px;width:32px;height:32px;cursor:pointer;font-size:18px;color:#526373}
.p48-analysis-summary{display:grid;grid-template-columns:92px 1fr;gap:12px;padding:12px 14px;background:#f7fafc;border-bottom:1px solid #e2e8ee}
.p48-analysis-score{display:flex;flex-direction:column;align-items:center;justify-content:center;border:1px solid #d4e1dc;border-radius:12px;background:#fff;padding:9px}.p48-analysis-score strong{font:800 24px/1 Inter,system-ui;color:#176c52}.p48-analysis-score span{font:700 9px/1.2 Inter,system-ui;color:#6c7a87;margin-top:4px}
.p48-analysis-counts{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;align-content:center}.p48-analysis-count{border-radius:9px;padding:7px 5px;text-align:center;font:700 10px Inter,system-ui;background:#fff;border:1px solid #e0e6eb}.p48-analysis-count strong{display:block;font-size:15px;margin-bottom:2px}.p48-analysis-count.error strong{color:#b42318}.p48-analysis-count.warning strong{color:#b25e09}.p48-analysis-count.info strong{color:#2c67a0}
.p48-analysis-next{margin:10px 10px 0;padding:11px 12px;border:1px solid #b9d8cc;border-radius:11px;background:#f2faf6;display:grid;gap:4px}
.p48-analysis-next[hidden]{display:none!important}.p48-analysis-next-label{font:800 9px/1 Inter,system-ui;color:#28715c;letter-spacing:.08em}.p48-analysis-next strong{font:800 12px/1.3 Inter,system-ui;color:#20364f}.p48-analysis-next>span:not(.p48-analysis-next-label){font:500 10px/1.4 Inter,system-ui;color:#536574}.p48-analysis-next button{justify-self:start;margin-top:4px}
.p48-analysis-list{overflow:auto;padding:10px 10px 18px;display:grid;gap:8px}.p48-analysis-empty{padding:22px 16px;text-align:center;color:#536574;font:600 12px/1.5 Inter,system-ui;display:grid;gap:5px}.p48-analysis-empty strong{color:#28715c;font-size:13px}.p48-analysis-empty span{font-weight:500;font-size:10px}.p48-analysis-item{width:100%;text-align:left;border:1px solid #dde4ea;border-left-width:4px;border-radius:10px;background:#fff;padding:10px;color:#273846}.p48-analysis-item:hover{background:#f7fafc}.p48-analysis-item.error{border-left-color:#d92d20}.p48-analysis-item.warning{border-left-color:#e68a17}.p48-analysis-item.info{border-left-color:#3978b7}.p48-analysis-item-head{display:flex;align-items:flex-start;gap:7px}.p48-analysis-priority{flex:0 0 auto;border-radius:999px;padding:3px 6px;font:800 8px/1.2 Inter,system-ui}.p48-analysis-priority.error{background:#fff0ee;color:#b42318}.p48-analysis-priority.warning{background:#fff6e8;color:#9a550d}.p48-analysis-priority.info{background:#eef6fd;color:#2c67a0}.p48-analysis-item-title{font:750 11px/1.3 Inter,system-ui;flex:1}.p48-analysis-item-detail{font:500 10px/1.35 Inter,system-ui;color:#687887;margin-top:4px}.p48-analysis-item-fix{margin-top:7px;padding:7px 8px;border-radius:8px;background:#f7f9fb;display:grid;gap:2px;font:500 10px/1.4 Inter,system-ui;color:#506271}.p48-analysis-item-fix strong{font-size:9px;color:#2d4558}.p48-analysis-item-action{border:0;background:transparent;padding:5px 0 0;font:700 9px/1.2 Inter,system-ui;color:#28715c;margin-top:3px;cursor:pointer}.p48-analysis-item-action:hover{text-decoration:underline}
@media(max-width:700px),(pointer:coarse){.p48-analysis-panel{top:72px;right:8px;left:8px;bottom:82px;width:auto;border-radius:14px}.p48-analysis-close{min-width:44px;min-height:44px}.p48-analysis-item{min-height:54px;padding:11px 12px}.p48-analysis-summary{grid-template-columns:82px 1fr}}
#pk48 *{box-sizing:border-box}
.p48-brand{height:94px;background:#fff;border-bottom:1px solid #e1e7ed;display:flex;align-items:center;padding:8px 18px}
.p48-brand-inner{display:flex;flex-direction:column;align-items:flex-start;justify-content:center;gap:2px}
.p48-logo-crop{height:52px;width:315px;overflow:hidden;display:flex;align-items:flex-start}
.p48-logo-crop img{width:315px!important;height:auto!important;max-width:none!important;display:block;transform:translateY(-1px)}
.p48-tagline{font:800 13px/1.1 Inter,system-ui,sans-serif;letter-spacing:2.2px;color:#20364f;margin-left:83px;white-space:nowrap}
.p48-resize{position:absolute;width:13px;height:13px;background:#fff;border:2px solid #2c7be5;border-radius:3px;z-index:10;display:none}
.p48-node.selected .p48-resize{display:block}
.p48-resize.se{right:-7px;bottom:-7px;cursor:nwse-resize}.p48-resize.sw{left:-7px;bottom:-7px;cursor:nesw-resize}
.p48-resize.ne{right:-7px;top:-7px;cursor:nesw-resize}.p48-resize.nw{left:-7px;top:-7px;cursor:nwse-resize}
.p48-step-io{margin-top:10px;padding-top:10px;border-top:1px solid #e1e7ed}.p48-step-io .p48-io-wrap{margin-top:0}
.p48-io-wrap{margin-top:12px;border-top:1px solid #e3e8ed;padding-top:10px}
.p48-io-title{font-size:10px;font-weight:800;color:#64717d;margin:6px 0}
.p48-io-list{display:grid;gap:5px}.p48-io-row{display:flex;gap:5px;align-items:center}
.p48-io-row input{min-width:0;flex:1;border:1px solid #cfd7df;border-radius:7px;padding:6px 7px;font:12px system-ui}
.p48-io-row button{border:1px solid #d7dde3;background:#fff;border-radius:6px;width:28px;height:28px;cursor:pointer}
.p48-addio{width:100%;margin-top:5px;border:1px dashed #9fb0bf;background:#f8fafc;border-radius:7px;padding:6px;font:700 11px system-ui;cursor:pointer}
.p48-node-io{width:100%;margin-top:6px;display:grid;gap:2px;font-size:10px;font-weight:500;opacity:.8;text-align:left}
.p48-node-io span{display:block;white-space:pre-wrap;overflow-wrap:anywhere}
.p48-brand img{height:56px;width:auto;max-width:310px;object-fit:contain;display:block}
.p48-top{display:flex;gap:8px;align-items:center;flex-wrap:wrap;padding:10px;background:#fff;border-bottom:1px solid #dce2e8}
.p48-btn{border:1px solid #ccd4dc;background:#fff;color:#24303d;border-radius:8px;min-height:38px;padding:8px 11px;font:600 13px system-ui;cursor:pointer}
.p48-btn:hover{background:#f2f5f7}.p48-btn.primary{background:#1f6f55;color:#fff;border-color:#1f6f55}
.p48-name{font:800 14px system-ui;border:2px solid #8aa2b8;border-radius:8px;padding:8px 10px;min-width:290px;background:#fbfdff}
.p48-spacer{flex:1}.p48-status{font-size:12px;color:#667382;min-width:70px}
.p48-save-state{font:700 11px system-ui;color:#4b6b5c;white-space:nowrap;padding:4px 7px;border-radius:999px;background:#edf7f1;border:1px solid #d5eadc}
.p48-save-state[data-state="saving"]{color:#6a5b2d;background:#fff8df;border-color:#eee0a6}
.p48-save-state[data-state="error"]{color:#9c3029;background:#fff1ef;border-color:#efc6c1}
/* v0.15.2 new-process dialog */
.p48-new-process-backdrop{position:fixed;inset:0;z-index:9900;background:rgba(28,43,56,.28);backdrop-filter:blur(1px)}
.p48-new-process-backdrop[hidden],.p48-new-process-dialog[hidden]{display:none!important}
.p48-new-process-dialog{position:fixed;z-index:9901;left:50%;top:50%;transform:translate(-50%,-50%);width:min(430px,calc(100vw - 28px));padding:22px;border:1px solid #cbd8e2;border-radius:16px;background:#fff;box-shadow:0 22px 60px rgba(27,45,61,.25);color:#22384b}
.p48-new-process-kicker{font:800 9px/1 Inter,system-ui;letter-spacing:.12em;color:#28715c;margin-bottom:7px}
.p48-new-process-title{font:800 20px/1.25 Inter,system-ui;color:#20364f}
.p48-new-process-sub{font:500 11px/1.45 Inter,system-ui;color:#6b7a87;margin:5px 0 16px}
.p48-new-process-label{display:block;font:750 10px/1.2 Inter,system-ui;color:#516575;margin-bottom:5px}
.p48-new-process-dialog input{width:100%;border:2px solid #9eb2c3;border-radius:9px;padding:10px 11px;font:700 14px Inter,system-ui;color:#24394c;background:#fbfdff}
.p48-new-process-dialog input:focus{outline:2px solid rgba(44,123,229,.22);outline-offset:1px;border-color:#2c7be5}
.p48-new-process-error{margin-top:7px;border-radius:7px;padding:7px 8px;background:#fff1ef;color:#a23a31;font:650 10px/1.35 Inter,system-ui}
.p48-new-process-actions{display:flex;justify-content:flex-end;gap:8px;margin-top:16px}
.p48-new-process-actions button{min-height:40px;border:1px solid #c7d2dc;border-radius:9px;background:#fff;color:#304659;padding:8px 13px;font:750 12px Inter,system-ui;cursor:pointer}
.p48-new-process-actions button.primary{background:#1f6f55;border-color:#1f6f55;color:#fff}
@media(max-width:700px),(pointer:coarse){.p48-new-process-dialog{top:auto;bottom:18px;transform:translateX(-50%);padding:19px}.p48-new-process-actions{display:grid;grid-template-columns:1fr 1fr}.p48-new-process-actions button{min-height:46px}}

.p48-recovery-banner{position:fixed;top:12px;left:50%;transform:translateX(-50%);z-index:9999;max-width:min(620px,calc(100vw - 24px));display:flex;align-items:center;gap:10px;padding:10px 12px;border:1px solid #a9c8df;border-radius:11px;background:#f7fbff;box-shadow:0 8px 26px rgba(32,54,72,.18);font:600 12px system-ui;color:#30465a}
.p48-recovery-banner[hidden]{display:none}.p48-recovery-banner .p48-recovery-actions{display:flex;gap:6px;margin-left:auto}.p48-recovery-banner button{border:1px solid #adc5d8;border-radius:7px;background:#fff;padding:6px 9px;font:700 11px system-ui;cursor:pointer}.p48-recovery-banner button.primary{background:#e7f3fc;border-color:#77a9ce;color:#175f95}
@media(max-width:700px){.p48-save-state{font-size:10px;padding:3px 6px}.p48-recovery-banner{top:8px;align-items:flex-start;flex-wrap:wrap}.p48-recovery-banner .p48-recovery-actions{width:100%;margin-left:0}.p48-recovery-banner button{min-height:38px;flex:1}}
.p48-body{display:grid;grid-template-columns:220px minmax(0,1fr);min-height:var(--p48-desktop-body-h,640px)}
.p48-side{background:#fff;border-right:1px solid #dce2e8;padding:10px}
.p48-section{margin-bottom:16px}
.p48-account-collapsible{padding:0!important;overflow:visible}
.p48-account-summary{list-style:none;cursor:pointer;display:flex;align-items:center;justify-content:space-between;gap:8px;padding:10px;font-weight:800;color:#17364b}
.p48-account-summary::-webkit-details-marker{display:none}
.p48-account-summary::after{content:"▾";font-size:11px;color:#607586}
.p48-account-collapsible[open] .p48-account-summary{border-bottom:1px solid #e1e8ed;margin-bottom:8px}
.p48-account-collapsible>div{margin-left:10px;margin-right:10px}
#p48-account-summary-state{font-size:10px;font-weight:700;color:#667b89;margin-left:auto}
.p48-logo-menu,.p48-scale-menu{position:relative}
.p48-logo-popover,.p48-scale-popover{position:absolute;z-index:80;top:calc(100% + 6px);left:0;width:260px;background:#fff;border:1px solid #cbd7df;border-radius:10px;padding:10px;box-shadow:0 10px 28px rgba(31,55,70,.16)}
.p48-scale-actions{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin:7px 0}
.p48-scale-fit{width:100%;margin-bottom:7px}
.p48-account{border:1px solid #d8e0e7;background:#f8fafc;border-radius:10px;padding:9px;margin-bottom:12px}
.p48-account input{width:100%;border:1px solid #cfd7df;border-radius:7px;padding:7px 8px;font:12px system-ui;margin-top:5px}
.p48-account-actions{display:grid;grid-template-columns:1fr 1fr;gap:5px;margin-top:7px}
.p48-cloud-badge{display:inline-flex;font-size:10px;font-weight:800;border-radius:999px;padding:4px 7px;background:#edf7f2;color:#1f6f55;margin-top:5px}
.p48-cloud-badge.off{background:#f4f4f4;color:#777}
.p48-sharebox{display:none;border:1px solid #cfdbe6;background:#f8fbfe;border-radius:9px;padding:7px}
.p48-sharebox input{width:260px;border:1px solid #cfd7df;border-radius:7px;padding:6px;font-size:11px}
.p48-small{font-size:10.5px;color:#6b7885;line-height:1.35}.p48-title{font-size:12px;font-weight:800;margin-bottom:8px}.p48-sub{font-size:11px;color:#6c7784;line-height:1.45;margin-bottom:9px}
.p48-list{display:grid;gap:6px}
.p48-proc-row{display:grid;grid-template-columns:minmax(0,1fr) 34px;gap:5px;align-items:stretch}
.p48-proc-row .p48-proc{min-width:0}
.p48-proc-delete{border:1px solid #e0c4c1;background:#fff;color:#a43d34;border-radius:8px;cursor:pointer;font-size:14px;font-weight:800}
.p48-proc-delete:hover{background:#fff1ef;border-color:#d58f88}
.p48-proc{width:100%;text-align:left;border:1px solid #d5dce3;background:#fff;border-radius:8px;padding:9px;font:700 12px system-ui;cursor:pointer;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.p48-proc:hover{background:#f3f6f8}.p48-proc.active{border-color:#1f6f55;background:#eef7f3;color:#175540}
.p48-item{display:flex;align-items:center;gap:8px;border:1px solid #d0d7df;background:#fff;border-radius:9px;padding:9px;margin-bottom:7px;cursor:grab;font-size:12.5px;font-weight:700;user-select:none}
.p48-icon{width:23px;height:23px;border-radius:6px;background:#edf2f6;display:grid;place-items:center;font-size:11px}
.p48-format{border-top:1px solid #e2e7ec;padding-top:12px}
.p48-focus-flash{box-shadow:0 0 0 3px rgba(37,99,235,.16);border-radius:8px;transition:box-shadow .2s ease}
.p48-format-grid{display:grid;grid-template-columns:1fr 1fr;gap:7px}
.p48-format label{display:block;font-size:10px;font-weight:800;color:#65717e;margin-bottom:3px}
.p48-format select,.p48-format input[type="number"]{width:100%;min-height:34px;border:1px solid #cfd7df;border-radius:7px;padding:5px 7px;font:12px system-ui;background:#fff}
.p48-format input[type="color"]{width:100%;height:34px;border:1px solid #cfd7df;border-radius:7px;padding:2px;background:#fff}
.p48-actions{display:grid;grid-template-columns:repeat(3,1fr);gap:5px;margin-top:7px}
.p48-mini{min-height:33px;border:1px solid #cfd7df;border-radius:7px;background:#fff;font:700 12px system-ui;cursor:pointer}.p48-mini.active{background:#eaf1f8;border-color:#7c9ab5}
.p48-empty{font-size:11px;color:#75818d;line-height:1.4}
.p48-scroll{overflow:auto;background:#e9eef3}
#p48-canvas{position:relative;width:2400px;height:1400px;background:#fff;touch-action:none;background-image:radial-gradient(#dce2e8 1px,transparent 1px);background-size:20px 20px}
.p48-print-frame{position:absolute;pointer-events:none;z-index:1;display:none;border:2px dashed rgba(31,111,85,.55);background:rgba(31,111,85,.018)}
.p48-print-frame.on{display:block}
.p48-print-frame::before{content:attr(data-label);position:absolute;left:10px;top:8px;font:800 11px system-ui;color:#1f6f55;background:#fff;padding:3px 6px;border-radius:5px}
.p48-print-page{position:absolute;border:2px dashed rgba(31,111,85,.55);background:rgba(31,111,85,.018);pointer-events:none;z-index:1}
.p48-print-page::before{content:attr(data-label);position:absolute;left:10px;top:8px;font:800 11px system-ui;color:#1f6f55;background:#fff;padding:3px 6px;border-radius:5px}
.p48-workspace{border:1px solid #d8e0e7;background:#fff;border-radius:10px;padding:9px;margin-bottom:12px}
.p48-workspace select,.p48-workspace input{width:100%;border:1px solid #cfd7df;border-radius:7px;padding:7px 8px;font:12px system-ui;margin-top:5px}
.p48-role{display:inline-flex;font-size:10px;font-weight:800;padding:3px 7px;border-radius:999px;background:#eef3f7;color:#425466;margin-top:5px}

.p48-marquee{position:absolute;border:2px dashed #2c7be5;background:rgba(44,123,229,.10);z-index:20;pointer-events:none;display:none}
.p48-node.multi-selected{outline:3px solid #2c7be5;outline-offset:3px}
.p48-node.decision.multi-selected{outline:none}
.p48-node.decision.multi-selected::before{border-color:#2c7be5;box-shadow:none}

#p48-svg{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:2}
#p48-links{pointer-events:all!important}
#p48-links *{pointer-events:visibleStroke}
.p48-link{stroke:#687584;stroke-width:2.2;fill:none}.p48-temp{stroke:#df941e;stroke-width:2.4;fill:none;stroke-dasharray:6 5}
.p48-node{position:absolute;min-width:160px;max-width:360px;width:max-content;min-height:64px;height:auto;padding:14px 26px;border:2px solid #637387;border-radius:10px;background:#fff;box-shadow:0 3px 9px rgba(31,42,55,.10);z-index:5;user-select:none;touch-action:none;display:flex;align-items:center;justify-content:center}
/* v0.10.40: selectable node visual styles */
.p48-node.p48-style-3d{box-shadow:0 9px 0 rgba(31,42,55,.28),0 18px 28px rgba(31,42,55,.20)}
.p48-node.p48-style-raised{box-shadow:0 18px 38px rgba(31,42,55,.28),0 5px 12px rgba(31,42,55,.14)}
.p48-node.p48-style-glass{backdrop-filter:blur(10px) saturate(1.18);-webkit-backdrop-filter:blur(10px) saturate(1.18);box-shadow:inset 0 2px 0 rgba(255,255,255,.88),inset 0 -1px 0 rgba(90,110,130,.13),0 14px 32px rgba(31,42,55,.18)}
.p48-node.p48-style-flat{transform:none;box-shadow:none!important;border-radius:4px!important}
.p48-node.decision.p48-style-3d::before{box-shadow:9px 9px 0 rgba(31,42,55,.28),14px 15px 24px rgba(31,42,55,.18)}
.p48-node.decision.p48-style-raised::before{box-shadow:10px 12px 30px rgba(31,42,55,.28)}
.p48-node.decision.p48-style-glass::before{box-shadow:inset 2px 2px 0 rgba(255,255,255,.82),8px 10px 24px rgba(31,42,55,.17)}
.p48-node.decision.p48-style-flat::before{box-shadow:none!important}
.p48-label{display:block;width:100%;white-space:pre-wrap;overflow-wrap:anywhere;word-break:break-word;line-height:1.28;cursor:grab;outline:none}.p48-node:active .p48-label{cursor:grabbing}
.p48-label[contenteditable="true"]{user-select:text;-webkit-user-select:text;cursor:text;min-width:40px}
.p48-node.object{
  min-width:150px;max-width:280px;min-height:42px;padding:10px 14px;
  border:2px solid #0d596c;border-radius:8px;background:#f7fbfc;color:#173e49;
  font-weight:700;
}
.p48-node.object::before{
  content:"";position:absolute;left:-7px;top:50%;width:12px;height:12px;
  transform:translateY(-50%);border-radius:2px;background:#0d596c;
}
.p48-node.object .p48-label{text-align:center}
.p48-node.process{border-radius:12px}

.p48-node.start,.p48-node.end{border-radius:38px}.p48-node.start{border-color:#2b7b61}.p48-node.end{border-color:#985148}
.p48-node.decision{
  min-width:150px;
  max-width:320px;
  min-height:150px;
  width:170px;
  height:170px;
  padding:38px;
  border:0;
  background:transparent!important;
  border-radius:0;
  overflow:visible;
  display:flex;
  align-items:center;
  justify-content:center;
}
.p48-node.decision::before{
  content:"";
  position:absolute;
  left:50%;
  top:50%;
  width:70.71%;
  height:70.71%;
  transform:translate(-50%,-50%) rotate(45deg);
  transform-origin:center;
  background:var(--decision-bg,#fff8df);
  border:var(--decision-border-width,2px) solid var(--decision-border,#d69a18);
  box-sizing:border-box;
  z-index:-1;
}
.p48-node.decision .p48-label,.p48-node.decision .p48-node-io{position:relative;z-index:2;text-align:center}
.p48-node.subprocess{border-style:double;border-width:4px;border-color:#7556a6}.p48-node.note{border-color:#b8973e}.p48-node.group{min-width:240px;max-width:440px;min-height:120px;border-style:dashed;color:#536171}
.p48-node.document{border-color:#3b6f9c;background:#f3f8fc;min-width:180px;padding-bottom:38px}
.p48-node.document::before{content:"📄";position:absolute;left:12px;top:10px;font-size:18px;line-height:1}
.p48-doc-open{position:absolute;left:12px;right:12px;bottom:8px;min-height:24px;border:0;border-top:1px solid rgba(59,111,156,.22);background:transparent;color:#245d8d;font:700 11px system-ui;cursor:pointer;padding-top:6px;text-align:center}
.p48-doc-open:hover{text-decoration:underline}
.p48-doc-open[hidden]{display:none!important}
/* v0.10.41: document URLs are entered directly inside the document node. */
.p48-node.document.p48-doc-editing{min-height:104px;padding-bottom:58px}
.p48-doc-inline-editor{position:absolute;left:10px;right:10px;bottom:8px;z-index:12;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:6px;align-items:center;padding-top:7px;border-top:1px solid rgba(59,111,156,.22);background:inherit}
.p48-doc-inline-editor[hidden]{display:none!important}
.p48-doc-inline-input{min-width:0;width:100%;height:32px;border:1px solid #9bb7cf;border-radius:7px;padding:5px 7px;background:#fff;color:#17202a;font:11px system-ui;user-select:text;-webkit-user-select:text;touch-action:manipulation}
.p48-doc-inline-save{height:32px;border:1px solid #3b6f9c;border-radius:7px;background:#eef6fc;color:#245d8d;padding:0 9px;font:800 10px system-ui;cursor:pointer}
.p48-document-link-editor{margin-top:10px;padding:10px;border:1px solid #d8e3ec;border-radius:8px;background:#f8fbfd}
.p48-document-link-editor label{display:block;font:700 10px system-ui;color:#657281;margin:5px 0 3px}
.p48-document-link-editor input{width:100%;border:1px solid #cfd7df;border-radius:7px;padding:7px;font:12px system-ui}

/* v0.10.35 fixes */
.p48-node.selected{outline:2px solid #2c7be5!important;outline-offset:2px!important;box-shadow:0 0 0 1px rgba(37,99,235,.10)!important}
.p48-node.multi-selected{outline:2px solid #2c7be5!important;outline-offset:2px!important;box-shadow:0 0 0 1px rgba(14,165,233,.08)!important}
.p48-node.decision.selected,.p48-node.decision.multi-selected{outline:none!important}
.p48-node.decision.selected::before{border-color:#2c7be5!important;box-shadow:0 0 0 1px rgba(44,123,229,.16)!important}
.p48-link-selection{stroke-width:5px!important;opacity:.22!important}
.p48-scroll-bottom-spacer{width:1px;height:56px;pointer-events:none}
.p48-side::after{content:"";display:block;height:56px;pointer-events:none}
.p48-document-open-editor{display:inline-block;margin-top:7px;color:#245d8d;font:700 11px system-ui;text-decoration:none}
.p48-document-open-editor:hover{text-decoration:underline}

.p48-node.selected{outline:3px solid #2c7be5;outline-offset:3px}
.p48-node.decision.selected{outline:none}
.p48-node.decision.selected::before{
  border-color:#2c7be5;
  box-shadow:0 0 0 2px rgba(44,123,229,.22);
}
.p48-handle{position:absolute;width:16px;height:16px;border-radius:50%;background:#1f6f55;border:3px solid #fff;box-shadow:0 0 0 1px #1f6f55;cursor:crosshair;z-index:8}
.p48-handle.right{right:-8px;top:50%;transform:translateY(-50%)}.p48-handle.left{left:-8px;top:50%;transform:translateY(-50%)}.p48-handle.top{top:-8px;left:50%;transform:translateX(-50%)}.p48-handle.bottom{bottom:-8px;left:50%;transform:translateX(-50%)}
.p48-node.decision .p48-handle.right{right:-8px;top:50%;transform:translateY(-50%)}
.p48-node.decision .p48-handle.left{left:-8px;top:50%;transform:translateY(-50%)}
.p48-node.decision .p48-handle.top{top:-8px;left:50%;transform:translateX(-50%)}
.p48-node.decision .p48-handle.bottom{bottom:-8px;left:50%;transform:translateX(-50%)}
.p48-node.decision.selected .p48-resize{display:block}
.p48-node.decision .p48-resize.se{right:5px;bottom:5px}
.p48-node.decision .p48-resize.sw{left:5px;bottom:5px}
.p48-node.decision .p48-resize.ne{right:5px;top:5px}
.p48-node.decision .p48-resize.nw{left:5px;top:5px}
@media(max-width:850px){.p48-body{grid-template-columns:1fr}.p48-side{border-right:0;border-bottom:1px solid #dce2e8}}
.p48-btn:focus-visible,.p48-mini:focus-visible,.p48-addio:focus-visible,.p48-item:focus-visible,
.p48-side input:focus-visible,.p48-side select:focus-visible,.p48-name:focus-visible{
  outline:3px solid rgba(37,99,235,.38);
  outline-offset:2px;
}
.p48-item:focus-visible{cursor:pointer}
.p48-node.selected{box-shadow:0 0 0 3px rgba(37,99,235,.16)}
.p48-node.multi-selected{box-shadow:0 0 0 3px rgba(14,165,233,.14)}
.p48-runtime-error{display:inline-flex;align-items:center;max-width:520px;padding:6px 9px;border:1px solid #fecaca;border-radius:8px;background:#fff7f7;color:#991b1b;font-size:12px;font-weight:600;white-space:normal}
.p48-runtime-error[hidden]{display:none!important}

.p48-bg-advanced{display:none;margin-top:10px;padding-top:10px;border-top:1px solid #e1e7ed}
.p48-bg-advanced.on{display:block}
.p48-bg-wide{display:block;font:700 10px system-ui;color:#657281}
.p48-bg-wide input{width:100%;margin-top:4px;border:1px solid #cfd7df;border-radius:7px;padding:7px;font:12px system-ui}
.p48-bg-range{display:grid;grid-template-columns:auto 1fr auto;align-items:center;gap:8px;margin-top:8px;font:700 10px system-ui;color:#657281}
.p48-bg-range input{width:100%}
.p48-bg-separator{height:1px;background:#e1e7ed;margin:11px 0}
.p48-canvas-watermark{position:absolute;inset:0;z-index:1;pointer-events:none;display:none;align-items:center;justify-content:center;overflow:hidden}
.p48-canvas-watermark.on{display:flex}
.p48-canvas-watermark span{font:800 76px/1.05 Inter,system-ui,sans-serif;letter-spacing:.08em;transform:rotate(-28deg);white-space:nowrap;text-align:center;max-width:80%;overflow:hidden;text-overflow:ellipsis}
.p48-canvas-watermark img{max-width:42%;max-height:36%;object-fit:contain;transform:rotate(-18deg)}
</style>

<div class="p48-brand">
  <div class="p48-brand-inner">
    <div class="p48-logo-crop"><img src="__MAPLINI_LOGO__" alt="Maplini"></div>
    <div class="p48-tagline">MAP · UNDERSTAND · IMPROVE</div>
    <div class="p48-version">v. __MAPLINI_VERSION__</div>
  </div>
</div>
<div class="p48-top p48-top-simplified">
  <strong>Process</strong>
  <input id="p48-name" class="p48-name" value="Exempel – upphandlingsprocess" aria-label="Processnamn">
  <button type="button" class="p48-btn primary" id="p48-new" title="Skapa ny process">+ Ny process</button>
  <button type="button" class="p48-btn p48-mobile-tools-btn" id="p48-mobile-tools" aria-expanded="false" aria-controls="p48-side">☰ Verktyg</button>
  <button type="button" class="p48-btn" id="p48-save" title="Spara process">Spara</button>
  <button type="button" class="p48-btn" id="p48-share" title="Dela aktuell process">Dela</button>
  <div class="p48-sharebox" id="p48-sharebox"><input id="p48-share-url" readonly><button type="button" class="p48-mini" id="p48-copy-share">Kopiera länk</button></div>
  <button type="button" class="p48-btn p48-icon-action" id="p48-undo" title="Ångra (Ctrl/Cmd+Z)" aria-label="Ångra">↶</button>
  <button type="button" class="p48-btn p48-icon-action" id="p48-redo" title="Gör om (Ctrl/Cmd+Shift+Z eller Ctrl/Cmd+Y)" aria-label="Gör om">↷</button>
  <div class="p48-zoom-controls" role="group" aria-label="Storlek på canvasinnehåll">
    <button type="button" class="p48-btn" id="p48-zoom-out" aria-label="Zooma ut" title="Zooma ut">−</button>
    <button type="button" class="p48-btn p48-zoom-value" id="p48-zoom-reset" title="Återställ till 100%">100%</button>
    <button type="button" class="p48-btn" id="p48-zoom-in" aria-label="Zooma in" title="Zooma in">+</button>
    <button type="button" class="p48-btn" id="p48-fit-screen" title="Anpassa hela processen till fönstret">⊡ Anpassa</button>
  </div>
  <details class="p48-smart-layout-menu" id="p48-smart-layout-menu">
    <summary class="p48-btn" title="Ordna processen automatiskt">✨ Snygga till ▾</summary>
    <div class="p48-smart-layout-popover">
      <button type="button" class="p48-mini primary" id="p48-auto-clean" title="Räta upp rutor, jämna avstånd och snygga till pilar utan att ändra processens logik">✨ Ordna processen automatiskt</button>
      <div class="p48-muted p48-auto-clean-hint">Maplini behåller flödet men väljer riktning, avstånd och pilbanor åt dig.</div>
      <div class="p48-pop-title" style="margin-top:10px">Manuell riktning</div>
      <button type="button" class="p48-mini p48-smart-layout-choice" data-layout-scope="all" data-layout-orientation="horizontal">Horisontellt →</button>
      <button type="button" class="p48-mini p48-smart-layout-choice" data-layout-scope="all" data-layout-orientation="vertical">Vertikalt ↓</button>
      <div class="p48-pop-title" style="margin-top:9px">Markerade rutor</div>
      <button type="button" class="p48-mini p48-smart-layout-choice" data-layout-scope="selected" data-layout-orientation="horizontal">Markerat horisontellt →</button>
      <button type="button" class="p48-mini p48-smart-layout-choice" data-layout-scope="selected" data-layout-orientation="vertical">Markerat vertikalt ↓</button>
      <div class="p48-muted" id="p48-smart-layout-hint">Pilarna används för att förstå flödet.</div>
    </div>
  </details>

  <details class="p48-scale-menu p48-scale-menu-top" id="p48-scale-menu">
    <summary class="p48-btn" title="Ändra storlek på hela processen">↔ Skala process ▾</summary>
    <div class="p48-scale-popover">
      <div class="p48-pop-title">Skala hela processen</div>
      <label class="p48-scale-slider-label" for="p48-process-scale">Storlek <strong id="p48-process-scale-value">100 %</strong></label>
      <input id="p48-process-scale" class="p48-process-scale-slider" type="range" min="50" max="150" step="5" value="100" aria-label="Skala hela processen">
      <div class="p48-scale-slider-marks" aria-hidden="true"><span>50 %</span><span>100 %</span><span>150 %</span></div>
      <button type="button" class="p48-mini p48-scale-fit" id="p48-scale-fit-page">Passa till vald sida</button>
      <div class="p48-muted">Reglaget ändrar rutor, text, avstånd och hela processens innehåll proportionellt.</div>
    </div>
  </details>

  <details class="p48-export-menu" id="p48-export-menu">
    <summary class="p48-btn primary" title="Exportera processen">Exportera ▾</summary>
    <div class="p48-export-popover">
      <div class="p48-pop-title">Exportera</div>
      <div class="p48-export-actions">
        <button type="button" class="p48-btn primary" id="p48-pdf">PDF</button>
        <button type="button" class="p48-btn" id="p48-doc">DOCX</button>
      </div>
      <details class="p48-sheets-menu">
        <summary class="p48-btn">Excel / Google Sheets ▾</summary>
        <div class="p48-sheets-popover">
          <button type="button" class="p48-btn primary" id="p48-sheets-direct">Skapa i Google Drive</button>
          <button type="button" class="p48-btn" id="p48-sheets">Ladda ner .xlsx</button>
        </div>
      </details>
      <div class="p48-pop-title p48-export-page-title">Sidformat</div>
      <select id="p48-pdf-view" class="p48-btn" title="PDF-yta">
        <option value="off">Ingen PDF-yta</option>
        <option value="A4P" selected>A4 stående</option>
        <option value="A4L">A4 liggande</option>
        <option value="A3P">A3 stående</option>
        <option value="A3L">A3 liggande</option>
      </select>
      <select id="p48-page-count" class="p48-btn" title="Antal PDF-sidor">
        <option value="auto" selected>Automatiskt antal sidor</option>
        <option value="1">1 sida</option><option value="2">2 sidor</option><option value="3">3 sidor</option><option value="4">4 sidor</option>
        <option value="5">5 sidor</option><option value="6">6 sidor</option><option value="7">7 sidor</option><option value="8">8 sidor</option>
      </select>
    </div>
  </details>

  <details class="p48-more-menu" id="p48-more-menu">
    <summary class="p48-btn" title="Fler verktyg">••• Mer</summary>
    <div class="p48-more-popover">
      <button type="button" class="p48-btn p48-more-wide" id="p48-analyze" title="Kontrollera processens struktur">🔍 Analysera process</button>
      <button type="button" class="p48-btn p48-more-wide" id="p48-select-tool" aria-pressed="false" title="Markera flera objekt eller kopplingar">Markera område</button>
      <div class="p48-more-selection-actions">
        <button type="button" class="p48-btn" id="p48-duplicate-selection" disabled title="Duplicera markerade rutor (Ctrl/Cmd+D)">Duplicera</button>
        <button type="button" class="p48-btn danger" id="p48-delete-selection" disabled title="Ta bort markerat (Delete/Backspace)">Ta bort</button>
      </div>
      <button type="button" class="p48-btn p48-more-wide danger" id="p48-clear-canvas" title="Ta bort alla rutor och kopplingar från canvasen">Rensa hela canvasen</button>
      <details class="p48-canvas-menu">
  <summary class="p48-btn">Processyta ▾</summary>
  <div class="p48-canvas-popover">
    <div class="p48-pop-title">Processyta</div>
    
          
          <div class="p48-format-grid-clean">
            <label>Bakgrundstyp
              <select id="p48-bg-type">
                <option value="solid" selected>Enfärgad</option>
                <option value="dots">Prickar</option>
                <option value="grid">Rutnät</option>
                <option value="image">Bild</option>
                <option value="watermark">Vattenstämpel</option>
              </select>
            </label>
            <label>Bakgrundsfärg
              <input id="p48-canvas-bg" type="color" value="#ffffff">
            </label>
            <label>Mönsterfärg
              <input id="p48-bg-pattern-color" type="color" value="#d7e1e8">
            </label>
            <label>Täthet
              <select id="p48-bg-density">
                <option value="12">Tät</option>
                <option value="20" selected>Normal</option>
                <option value="32">Gles</option>
              </select>
            </label>
          </div>
          <div id="p48-gradient-controls" class="p48-bg-advanced">
            <div class="p48-title">Gradient</div>
            <div class="p48-format-grid-clean">
              <label>Från färg<input id="p48-gradient-start" type="color" value="#ffffff"></label>
              <label>Till färg<input id="p48-gradient-end" type="color" value="#e7f1ff"></label>
              <label>Riktning
                <select id="p48-gradient-angle">
                  <option value="0">Nedifrån → upp</option>
                  <option value="45" selected>Diagonal</option>
                  <option value="90">Vänster → höger</option>
                  <option value="135">Diagonal omvänd</option>
                  <option value="180">Uppifrån → ned</option>
                </select>
              </label>
            </div>
          </div>
          <div id="p48-image-bg-controls" class="p48-bg-advanced">
            <div class="p48-title">Bakgrundsbild</div>
            <div class="p48-logo-controls">
              <label class="p48-logo-upload">Ladda upp bild<input id="p48-bg-image-file" type="file" accept="image/png,image/jpeg,image/webp"></label>
              <button type="button" class="p48-btn" id="p48-bg-image-remove">Ta bort bild</button>
            </div>
            <label class="p48-bg-range">Opacitet <input id="p48-bg-image-opacity" type="range" min="5" max="100" step="5" value="25"><span id="p48-bg-image-opacity-value">25%</span></label>
          </div>
          <div id="p48-watermark-controls" class="p48-bg-advanced">
            <div class="p48-title">Vattenstämpel</div>
            <label class="p48-bg-wide">Text<input id="p48-watermark-text" type="text" maxlength="80" placeholder="UTKAST / KONFIDENTIELLT"></label>
            <label class="p48-hide-row"><input id="p48-watermark-use-logo" type="checkbox">Använd uppladdad processlogga som vattenstämpel</label>
            <label class="p48-bg-range">Opacitet <input id="p48-watermark-opacity" type="range" min="5" max="40" step="5" value="15"><span id="p48-watermark-opacity-value">15%</span></label>
          </div>
  </div>
</details>
      <details class="p48-logo-menu" id="p48-logo-menu">
    <summary class="p48-btn" title="Lägg till eller ändra processlogga">🖼 Logotyp ▾</summary>
    <div class="p48-logo-popover">
      <div class="p48-pop-title">Processlogga</div>
      <div class="p48-format-grid-clean">
        <label>Storlek
          <select id="p48-logo-size">
            <option value="120">Liten</option>
            <option value="180" selected>Normal</option>
            <option value="240">Stor</option>
          </select>
        </label>
      </div>
      <div class="p48-logo-controls">
        <label class="p48-logo-upload">Ladda upp logotype
          <input id="p48-logo-file" type="file" accept="image/png,image/jpeg,image/webp">
        </label>
        <button type="button" class="p48-btn" id="p48-logo-remove">Ta bort logotype</button>
      </div>
      <label class="p48-hide-row"><input id="p48-logo-hide" type="checkbox">Dölj logotype</label>
    </div>
  </details>

    </div>
  </details>

  <span class="p48-spacer"></span>
  <span id="p48-save-state" class="p48-save-state" data-state="saved" aria-live="polite">Autosparad</span>
  <span id="p48-status" class="p48-status" role="status" aria-live="polite"></span>
  <span id="p48-runtime-error" class="p48-runtime-error" role="alert" aria-live="assertive" hidden></span>
</div>

<div id="p48-recovery-banner" class="p48-recovery-banner" role="status" aria-live="polite" hidden>
  <span>Maplini hittade ändringar från en avbruten session.</span>
  <div class="p48-recovery-actions"><button type="button" class="primary" id="p48-recovery-restore">Återställ</button><button type="button" id="p48-recovery-ignore">Ignorera</button></div>
</div>

<div id="p48-new-process-backdrop" class="p48-new-process-backdrop" hidden></div>
<section id="p48-new-process-dialog" class="p48-new-process-dialog" role="dialog" aria-modal="true" aria-labelledby="p48-new-process-title" hidden>
  <div class="p48-new-process-kicker">NY PROCESS</div>
  <div id="p48-new-process-title" class="p48-new-process-title">Vad ska processen heta?</div>
  <div class="p48-new-process-sub">Namnet kan ändras när som helst senare.</div>
  <label class="p48-new-process-label" for="p48-new-process-name">Processnamn</label>
  <input id="p48-new-process-name" type="text" maxlength="120" value="Ny process" autocomplete="off" spellcheck="true">
  <div id="p48-new-process-error" class="p48-new-process-error" role="alert" hidden></div>
  <div class="p48-new-process-actions">
    <button type="button" id="p48-new-process-cancel">Avbryt</button>
    <button type="button" class="primary" id="p48-new-process-create">Skapa process</button>
  </div>
</section>

<section id="p48-analysis-panel" class="p48-analysis-panel" aria-label="Processkontroll" hidden>
  <div class="p48-analysis-head"><div><div class="p48-analysis-title">Processkontroll</div><div class="p48-analysis-sub">Vad behöver förbättras – och vad gör du åt det?</div></div><button type="button" id="p48-analysis-close" class="p48-analysis-close" aria-label="Stäng analys">×</button></div>
  <div class="p48-analysis-summary"><div class="p48-analysis-score"><strong id="p48-analysis-score">–</strong><span>PROCESSHÄLSA</span></div><div class="p48-analysis-counts"><div class="p48-analysis-count error"><strong id="p48-analysis-errors">0</strong>Åtgärda</div><div class="p48-analysis-count warning"><strong id="p48-analysis-warnings">0</strong>Kontrollera</div><div class="p48-analysis-count info"><strong id="p48-analysis-info">0</strong>Förbättra</div></div></div>
  <div id="p48-analysis-next" class="p48-analysis-next" hidden>
    <span class="p48-analysis-next-label">BÖRJA HÄR</span>
    <strong id="p48-analysis-next-title"></strong>
    <span id="p48-analysis-next-action"></span>
    <button type="button" id="p48-analysis-next-show" class="p48-mini">Visa på canvasen →</button>
  </div>
  <div id="p48-analysis-list" class="p48-analysis-list"></div>
</section>

<div class="p48-body">
  <aside class="p48-side" id="p48-side">
    <details class="p48-account p48-account-unified p48-account-collapsible" id="p48-account-panel">
      <summary class="p48-account-summary"><span>👤 Konto</span><span id="p48-account-summary-state">Ej inloggad</span></summary>

      <div id="p48-account-signedout">
        <div class="p48-small" style="margin-bottom:5px">Logga in för molnlagring, delning och workspaces.</div>
        <input id="p48-email" type="email" placeholder="E-post">
        <input id="p48-password" type="password" placeholder="Lösenord">
        <div class="p48-account-actions">
          <button type="button" class="p48-mini" id="p48-login">Logga in</button>
          <button type="button" class="p48-mini" id="p48-signup">Skapa konto</button>
        </div>
      </div>

      <div id="p48-account-signedin" hidden>
        <div class="p48-userline">
          <div>
            <div class="p48-small">Inloggad som</div>
            <div id="p48-user-email" style="font-size:12px;font-weight:800"></div>
          </div>
          <button type="button" class="p48-mini" id="p48-logout">Logga ut</button>
        </div>

        <div class="p48-account-divider"></div>
        <div class="p48-small">Aktuellt workspace</div>
        <select id="p48-workspace-select"><option value="">Personligt</option></select>
        <div id="p48-role" class="p48-role">Owner</div>

        <details class="p48-new-workspace">
          <summary>+ Nytt workspace</summary>
          <input id="p48-workspace-name" placeholder="Namn på workspace">
          <button type="button" class="p48-mini" id="p48-create-workspace" style="width:100%;margin-top:6px">Skapa workspace</button>
        </details>
      </div>

      <div id="p48-cloud-badge" class="p48-cloud-badge off">Ej inloggad</div>
      <div id="p48-cloud-help" class="p48-small">Ett Maplini-konto räcker. Google används bara som exportintegration.</div>
      <div id="p48-auth-error" class="p48-small" style="display:none;margin-top:7px;padding:7px;border-radius:7px;background:#fff1ef;color:#8c3029;border:1px solid #efc6c1"></div>
    </details>

    <div class="p48-section">
      <div class="p48-title">Sparade processer</div>
      <div id="p48-processes" class="p48-list"></div>
    </div>

    <div class="p48-section p48-method-palette">
      <div class="p48-title">Bygg processen</div>
      <div class="p48-palette-hint">Grundflödet är <strong>Objekt → Aktivitet → Objekt</strong>. Ett resultat kan bli nästa aktivitets input.</div>
      <div class="p48-method-flow" aria-label="Processens grundmodell"><span>▪ Objekt in</span><b>→</b><span>▭ Aktivitet</span><b>→</b><span>▪ Objekt ut</span></div>
      <div class="p48-item p48-item-core p48-item-object" draggable="true" role="button" tabindex="0" aria-label="Lägg till Objekt in" title="Det som triggar eller behövs före en aktivitet" data-type="object" data-object-role="input"><span class="p48-icon">▪</span><span><strong>Objekt in</strong><small>Trigger / det som behövs</small></span></div>
      <div class="p48-item p48-item-core" draggable="true" role="button" tabindex="0" aria-label="Lägg till Aktivitet" title="Det som görs och transformerar objekt" data-type="process"><span class="p48-icon">▭</span><span><strong>Aktivitet</strong><small>Det som görs</small></span></div>
      <div class="p48-item p48-item-core p48-item-object" draggable="true" role="button" tabindex="0" aria-label="Lägg till Objekt ut" title="Resultatet från en aktivitet" data-type="object" data-object-role="output"><span class="p48-icon">▪</span><span><strong>Objekt ut</strong><small>Resultat / det som blir</small></span></div>
      <div class="p48-palette-more-label">Fler typer</div>
      <div class="p48-item" draggable="true" role="button" tabindex="0" aria-label="Lägg till Start" title="Markera processens gräns" data-type="start"><span class="p48-icon">▶</span>Start</div>
      <div class="p48-item" draggable="true" role="button" tabindex="0" aria-label="Lägg till Beslut" title="Dra eller tryck för att lägga till" data-type="decision"><span class="p48-icon">◇</span>Beslut</div>
      <div class="p48-item" draggable="true" role="button" tabindex="0" aria-label="Lägg till Slut" title="Markera processens gräns" data-type="end"><span class="p48-icon">■</span>Slut</div>
      <div class="p48-item" draggable="true" role="button" tabindex="0" aria-label="Lägg till Delprocess" title="Dra eller tryck för att lägga till" data-type="subprocess"><span class="p48-icon">▣</span>Delprocess</div>
      <div class="p48-item" draggable="true" role="button" tabindex="0" aria-label="Lägg till Anteckning" title="Dra eller tryck för att lägga till" data-type="note"><span class="p48-icon">N</span>Anteckning</div>
      <div class="p48-item" draggable="true" role="button" tabindex="0" aria-label="Lägg till Dokument" title="Dra eller tryck för att lägga till" data-type="document"><span class="p48-icon">📄</span>Dokument</div>
      <div class="p48-step-io">
        <div class="p48-io-wrap">
          <div class="p48-io-title">Inputs</div>
          <div id="p48-inputs" class="p48-io-list"></div>
          <button type="button" class="p48-addio" id="p48-add-input">+ Lägg till input</button>
          <div class="p48-io-title">Outputs</div>
          <div id="p48-outputs" class="p48-io-list"></div>
          <button type="button" class="p48-addio" id="p48-add-output">+ Lägg till output</button>
        </div>
      </div>
    </div>

    <div class="p48-format" id="p48-format-panel" data-context="none">
      <div class="p48-title p48-format-context-title" id="p48-format-title">Formatering</div>
      <div class="p48-sub p48-format-context-hint" id="p48-format-hint">Markera en ruta eller pil för att visa relevanta inställningar.</div>
      <div id="p48-controls">
        <div id="p48-process-info" class="p48-process-info p48-node-only p48-single-node-only" hidden>
          <div class="p48-process-info-head">
            <div><div class="p48-title">Om steget</div><div class="p48-small">Beskriv arbetet – utan att belasta canvasen.</div></div>
            <span id="p48-process-info-progress" class="p48-process-info-progress">0 av 8</span>
          </div>
          <label>Vad händer?<textarea id="p48-info-description" rows="3" maxlength="12000" placeholder="Beskriv kort vad som görs och varför."></textarea></label>
          <div class="p48-process-info-grid">
            <label>Vem ansvarar?<input id="p48-info-role" type="text" maxlength="300" list="p48-role-suggestions" placeholder="Ex. Kundtjänst"></label>
            <label>Vilket system?<input id="p48-info-system" type="text" maxlength="500" list="p48-system-suggestions" placeholder="Ex. CRM"></label>
            <label>Tidsåtgång<input id="p48-info-duration" type="text" maxlength="300" placeholder="Ex. 10 min"></label>
          </div>
          <datalist id="p48-role-suggestions"></datalist>
          <datalist id="p48-system-suggestions"></datalist>
          <details id="p48-process-info-more" class="p48-process-info-more">
            <summary>Fördjupa beskrivningen <span id="p48-process-info-more-count"></span></summary>
            <label>Instruktion<textarea id="p48-info-instruction" rows="2" maxlength="4000" placeholder="Kort instruktion eller arbetssätt"></textarea></label>
            <label>Risk<textarea id="p48-info-risk" rows="2" maxlength="4000" placeholder="Vad kan gå fel?"></textarea></label>
            <label>Kontroll<textarea id="p48-info-control" rows="2" maxlength="4000" placeholder="Hur förebyggs eller upptäcks risken?"></textarea></label>
            <label>KPI / mått<input id="p48-info-kpi" type="text" maxlength="1000" placeholder="Ex. svarstid"></label>
          </details>
          <div class="p48-process-info-foot">Input och output hanteras separat och sparas med steget.</div>
        </div>
        <details class="p48-visual-details p48-node-only">
          <summary>Utseende</summary>
          <div class="p48-text-format-block p48-node-only">
        <div class="p48-format-grid-clean">
          <label>Typsnitt
            <select id="p48-font">
<option value="Inter">Inter</option>
<option value="DM Sans">DM Sans</option>
<option value="Poppins">Poppins</option>
<option value="Montserrat">Montserrat</option>
<option value="Roboto">Roboto</option>
<option value="Georgia">Georgia</option>
<option value="system-ui">System</option>
</select>
          </label>
          <label>Textstorlek
            <input id="p48-size" type="number" min="10" max="36" value="13">
          </label>
        </div>
        <div class="p48-text-tools-label">Stil</div>
        <div class="p48-actions">
          <button type="button" class="p48-mini" id="p48-bold" title="Fet text"><b>B</b></button>
          <button type="button" class="p48-mini" id="p48-italic" title="Kursiv text"><i>I</i></button>
          <button type="button" class="p48-mini" id="p48-under" title="Understruken text"><u>U</u></button>
        </div>
        <div class="p48-text-tools-label">Justering</div>
        <div class="p48-actions">
          <button type="button" class="p48-mini" data-text-align="left">Vänster</button>
          <button type="button" class="p48-mini" data-text-align="center">Centrera</button>
          <button type="button" class="p48-mini" data-text-align="right">Höger</button>
        </div>
        <button type="button" class="p48-btn p48-single-node-only" id="p48-font-all" style="width:100%;margin-top:9px">Använd typsnitt + storlek på all text</button>
        </div>
        <div class="p48-format-grid-clean p48-node-only" style="margin-top:8px">
          <label>Rutstil
            <select id="p48-node-style">
              <option value="standard" selected>Standard</option>
              <option value="raised">Upphöjd</option>
              <option value="flat">Minimal</option>
            </select>
          </label>
        </div>
        <button type="button" class="p48-btn p48-node-only p48-single-node-only" id="p48-node-style-all" style="width:100%;margin-top:7px">Använd rutstil på alla rutor</button>
        
        <div class="p48-point-settings p48-node-only p48-single-node-only">
          <div class="p48-title">Kopplingspunkter</div>
          <div class="p48-point-grid">
            <label>Storlek
              <select id="p48-point-size">
                <option value="6">6 px</option>
                <option value="8" selected>8 px</option>
                <option value="10">10 px</option>
                <option value="12">12 px</option>
                <option value="14">14 px</option>
              </select>
            </label>
            <label>Färg
              <input id="p48-point-color" type="color" value="#1f6f55">
            </label>
          </div>
          <label class="p48-hide-row">
            <input id="p48-hide-points" type="checkbox">
            Dölj kopplingspunkter
          </label>
        </div>
          
          <div class="p48-node-only"><label>Textfärg</label><input id="p48-textcolor" type="color" value="#17202a"></div>
          <div class="p48-node-only"><label>Bakgrund</label><input id="p48-bgcolor" type="color" value="#ffffff"></div>
          <div class="p48-node-only"><label>Kantfärg</label><input id="p48-bordercolor" type="color" value="#637387"></div>
          <div class="p48-node-only"><label>Kanttjocklek</label><select id="p48-borderwidth"><option value="1">1 px</option><option value="2" selected>2 px</option><option value="3">3 px</option><option value="4">4 px</option><option value="6">6 px</option></select></div>
        </div>
        </details>
        <div id="p48-document-link-editor" class="p48-document-link-editor p48-node-only p48-single-node-only" hidden>
          <div class="p48-title">Dokument</div>
          <label for="p48-document-url">Dokumentlänk</label>
          <input id="p48-document-url" type="url" inputmode="url" autocomplete="off" placeholder="https://…">
          <a id="p48-document-open-editor" class="p48-document-open-editor" target="_blank" rel="noopener noreferrer" hidden>↗ Öppna dokumentlänk</a>
          <div class="p48-small">Länka till exempelvis Google Drive, SharePoint, OneDrive eller annan webbadress.</div>
        </div>
        <button type="button" class="p48-btn p48-node-only p48-single-node-only" id="p48-delete-node" style="width:100%;margin-top:10px;color:#a43d34;border-color:#e0c4c1">Ta bort markerad ruta</button>

        <div id="p48-link-format" class="p48-link-format" hidden>
          <div class="p48-link-context-note">Inställningarna gäller bara den markerade pilen.</div>
          <div class="p48-link-format-grid">
            <label>Pilfärg<input id="p48-link-color" type="color" value="#687584"></label>
            <label>Tjocklek<select id="p48-link-width"><option value="1">1 px</option><option value="2" selected>2 px</option><option value="3">3 px</option><option value="4">4 px</option><option value="6">6 px</option></select></label>
            <label>Linjetyp<select id="p48-link-dash"><option value="solid" selected>Heldragen</option><option value="dashed">Streckad</option><option value="dotted">Prickad</option></select></label>
            <label>Pilform<select id="p48-link-routing"><option value="straight">Rak</option><option value="orthogonal">Vinkelrät</option><option value="free">Fri</option></select></label>
            <label>Slutmarkör<select id="p48-link-end"><option value="arrow" selected>Pil</option><option value="none">Ingen</option><option value="circle">Cirkel</option><option value="diamond">Diamant</option></select></label>
            <label>Fästning<select id="p48-link-anchor-mode"><option value="auto">Automatisk</option><option value="manual">Behåll startpunkt</option></select></label>
            <label class="p48-link-label-field">Text på pil<input id="p48-link-label" type="text" maxlength="60" autocomplete="off" placeholder="Skriv valfri text för just denna pil"></label>
          </div>
          <div id="p48-flow-coach" class="p48-flow-coach" hidden>
            <div class="p48-flow-coach-kicker">PROCESSFLÖDE</div>
            <strong>Vad lämnar den första aktiviteten efter sig?</strong>
            <span>Ett resultat eller objekt mellan aktiviteterna gör beroendet tydligt och visar vad som faktiskt startar nästa aktivitet.</span>
            <div class="p48-flow-coach-actions">
              <button type="button" class="p48-btn primary" id="p48-flow-coach-insert">＋ Infoga Objekt / resultat</button>
              <button type="button" class="p48-btn" id="p48-flow-coach-keep">Behåll direktkoppling</button>
            </div>
          </div>
          <div class="p48-insert-step-wrap" id="p48-insert-step-wrap">
            <button id="p48-insert-link-step" class="p48-insert-link-step" type="button" aria-haspopup="true" aria-expanded="false">＋ Infoga steg</button>
            <div id="p48-insert-step-menu" class="p48-insert-step-menu" hidden>
              <button type="button" class="p48-insert-step-choice" data-insert-type="object">▪ Objekt / resultat</button>
              <button type="button" class="p48-insert-step-choice" data-insert-type="process">▭ Aktivitet</button>
              <button type="button" class="p48-insert-step-choice" data-insert-type="decision">◇ Beslut</button>
              <button type="button" class="p48-insert-step-choice" data-insert-type="document">📄 Dokument</button>
              <button type="button" class="p48-insert-step-choice" data-insert-type="end">■ Slut</button>
            </div>
          </div>
          <button type="button" class="p48-btn" id="p48-delete-link" style="width:100%;margin-top:8px;color:#a43d34;border-color:#e0c4c1">Ta bort koppling</button>
        </div>

      </div>
  </aside>

  <button type="button" class="p48-mobile-backdrop" id="p48-mobile-backdrop" aria-label="Stäng verktyg"></button>
  <main class="p48-scroll" id="p48-scroll">
    <details class="p48-page-quick" id="p48-page-quick">
      <summary id="p48-page-quick-summary" title="Ändra pappersformat och antal sidor">A4 stående · Auto ▾</summary>
      <div class="p48-page-quick-popover">
        <div class="p48-page-quick-title">Sidinställningar</div>
        <label>Format
          <select id="p48-page-format-quick">
            <option value="off">Ingen sidyta</option>
            <option value="A4P" selected>A4 stående</option>
            <option value="A4L">A4 liggande</option>
            <option value="A3P">A3 stående</option>
            <option value="A3L">A3 liggande</option>
          </select>
        </label>
        <label>Antal sidor
          <select id="p48-page-count-quick">
            <option value="auto" selected>Automatiskt</option>
            <option value="1">1 sida</option><option value="2">2 sidor</option><option value="3">3 sidor</option><option value="4">4 sidor</option>
            <option value="5">5 sidor</option><option value="6">6 sidor</option><option value="7">7 sidor</option><option value="8">8 sidor</option>
          </select>
        </label>
        <div class="p48-page-quick-hint">Sidgränserna visar hur processen delas vid export.</div>
      </div>
    </details>
    <div class="p48-canvas-wrap" id="p48-canvas-scroll"><div id="p48-canvas"><div id="p48-empty-state" class="p48-empty-state" hidden>
      <div class="p48-empty-card">
        <div class="p48-empty-kicker">NY PROCESS</div>
        <div class="p48-empty-title">Vad startar processen?</div>
        <div class="p48-empty-copy">Börja med det som triggar processen. Bygg sedan <strong>Objekt → Aktivitet → Objekt</strong>.</div>
        <div class="p48-empty-actions">
          <button type="button" class="primary" id="p48-empty-object">▪ Lägg till Objekt in</button>
          <button type="button" id="p48-empty-activity">▭ Börja med Aktivitet</button>
        </div>
        <div class="p48-empty-tip">Tips: ett objekts resultat kan bli input till nästa aktivitet. <strong>＋ Nästa</strong> föreslår rätt typ.</div>
      </div>
    </div><div id="p48-canvas-watermark" class="p48-canvas-watermark" aria-hidden="true"></div><img id="p48-process-logo" class="p48-process-logo" alt="Processlogotype"><div id="p48-link-hit-layer" class="p48-link-hit-layer"></div><div id="p48-link-handle" class="p48-link-handle" title="Dra för att ändra kopplingens bana"></div><div id="p48-link-quick" class="p48-link-quick" role="toolbar" aria-label="Snabbval för pil"><button type="button" data-link-routing="straight" title="Gör pilen rak">— Rak</button><button type="button" data-link-routing="orthogonal" title="Gör pilen vinkelrät">⌜ Vinkelrät</button><button type="button" data-link-routing="free" title="Flytta pilens bana fritt">↝ Fri</button></div><div id="p48-node-quick" class="p48-node-quick" role="toolbar" aria-label="Snabbval för markerade rutor" data-mode="single"><span id="p48-node-quick-flow" class="p48-node-quick-flow" data-single-only></span><button type="button" id="p48-node-quick-next" data-single-only title="Lägg till rekommenderat nästa steg">＋ Nästa</button><button type="button" id="p48-node-quick-next-more" data-single-only title="Välj en annan typ av nästa steg" aria-label="Välj annan typ av nästa steg">▾</button><button type="button" id="p48-node-quick-format" title="Öppna egenskaper för markerad ruta">Egenskaper</button><label class="p48-quick-color-label" data-multi-only title="Ändra bakgrundsfärg för markerade"><input type="color" id="p48-node-quick-color" value="#ffffff"> Färg</label><button type="button" id="p48-node-quick-duplicate" title="Duplicera markerade">Duplicera</button><button type="button" id="p48-node-quick-delete" class="danger" title="Ta bort markerade">Ta bort</button></div><div id="p48-print-frame" class="p48-print-frame"></div>
      <div id="p48-snap-guide-x" class="p48-snap-guide p48-snap-guide-x" hidden></div><div id="p48-snap-guide-y" class="p48-snap-guide p48-snap-guide-y" hidden></div>
      <div id="p48-marquee" class="p48-marquee"></div>
      <svg id="p48-svg" viewBox="0 0 2400 1400">
        <defs><marker id="p48-arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><polygon points="0,0 10,4 0,8" fill="#687584"></polygon></marker></defs>
        <g id="p48-links"></g>
        <path id="p48-temp" class="p48-temp" hidden></path>
      </svg>
    </div>
  </div>
  <div class="p48-scroll-bottom-spacer" aria-hidden="true"></div>
  <div id="p48-hnav" class="p48-hnav" aria-label="Horisontell navigering">
    <div id="p48-hnav-inner" class="p48-hnav-inner"></div>
  </div>
</main>
  <nav id="p48-mobile-bar" class="p48-mobile-bar" data-mode="normal" aria-label="Mobil snabbmeny">
    <button type="button" class="primary" data-mobile-group="normal" id="p48-mobile-add">＋ Lägg till</button>
    <button type="button" data-mobile-group="normal" id="p48-mobile-undo">↶ Ångra</button>
    <button type="button" data-mobile-group="normal" id="p48-mobile-fit">⊡ Anpassa</button>
    <button type="button" data-mobile-group="normal" id="p48-mobile-more">☰ Verktyg</button>
    <button type="button" class="primary" data-mobile-group="selected" id="p48-mobile-next">＋ Nästa</button>
    <button type="button" data-mobile-group="selected" id="p48-mobile-format">Egenskaper</button>
    <button type="button" data-mobile-group="selected" id="p48-mobile-duplicate">Duplicera</button>
    <button type="button" data-mobile-group="selected" id="p48-mobile-context">••• Mer</button>
    <button type="button" class="danger" data-mobile-group="selected" id="p48-mobile-delete">Ta bort</button>
  </nav>
  <button type="button" id="p48-mobile-sheet-backdrop" class="p48-mobile-sheet-backdrop" aria-label="Stäng snabbmeny"></button>
  <section id="p48-mobile-sheet" class="p48-mobile-sheet" aria-label="Mobil snabbmeny" aria-hidden="true">
    <div class="p48-mobile-sheet-head"><span id="p48-mobile-sheet-title">Lägg till</span><button type="button" class="p48-mobile-sheet-close" id="p48-mobile-sheet-close" aria-label="Stäng">×</button></div>
    <div class="p48-mobile-sheet-grid" id="p48-mobile-add-sheet">
      <button type="button" data-mobile-add="start">▶ Start</button><button type="button" class="primary" data-mobile-add="process">□ Aktivitet</button>
      <button type="button" data-mobile-add="decision">◇ Beslut</button><button type="button" data-mobile-add="document">📄 Dokument</button>
      <button type="button" data-mobile-add="subprocess">▣ Delprocess</button><button type="button" data-mobile-add="note">N Anteckning</button>
      <button type="button" class="wide" data-mobile-add="end">■ Slut</button>
      <button type="button" id="p48-mobile-sheet-redo">↷ Gör om</button>
      <button type="button" id="p48-mobile-sheet-fullscreen">⛶ Helskärm</button>
      <button type="button" class="wide" id="p48-mobile-open-tools">☰ Alla verktyg och inställningar</button>
    </div>
    <div class="p48-mobile-sheet-grid" id="p48-mobile-context-sheet" hidden>
      <button type="button" id="p48-mobile-sheet-copy">Kopiera</button><button type="button" id="p48-mobile-sheet-format">Egenskaper</button>
      <button type="button" id="p48-mobile-sheet-layout-h">✨ Snygga till →</button><button type="button" id="p48-mobile-sheet-layout-v">✨ Snygga till ↓</button>
      <button type="button" class="wide" id="p48-mobile-sheet-tools">☰ Fler egenskaper</button>
      <button type="button" class="wide danger" id="p48-mobile-sheet-delete">Ta bort markerade</button>
    </div>
  </section>
</div>

<script>__MAPLINI_CONNECTOR_CORE__</script>
<script>__MAPLINI_CANVAS_CORE__</script>
<script>__MAPLINI_UI_CORE__</script>
<script>__MAPLINI_STATE_CORE__</script>
<script>__MAPLINI_PROCESS_INFO_CORE__</script>
<script>__MAPLINI_RELIABILITY_CORE__</script>
<script>__MAPLINI_EXPORT_CORE__</script>
<script>__MAPLINI_WORKFLOW_CORE__</script>
<script>__MAPLINI_PERFORMANCE_CORE__</script>
<script>__MAPLINI_MOBILE_CORE__</script>
<script>__MAPLINI_SELECTION_CORE__</script>
<script>__MAPLINI_SYNC_CORE__</script>
<script>__MAPLINI_SESSION_CORE__</script>
<script>__MAPLINI_RC_CORE__</script>
<script>__MAPLINI_FLOW_CORE__</script>
<script>__MAPLINI_ACCESS_CORE__</script>
<script>__MAPLINI_PRIVACY_CORE__</script>
<script>__MAPLINI_EDITING_CORE__</script>
<script>__MAPLINI_LAYOUT_CORE__</script>
<script>__MAPLINI_AUTOSAVE_CORE__</script>
<script>__MAPLINI_PROCESS_INTELLIGENCE_CORE__</script>
<script>
(()=>{
const root=document.getElementById('pk48'); if(!root||root.dataset.ready==='1')return; root.dataset.ready='1';
function syncDesktopViewportHeight(){
  const screenH=Number((window.screen&&window.screen.availHeight)||900);
  let parentH=screenH;
  try{if(window.parent&&window.parent!==window&&window.parent.innerHeight)parentH=Math.min(parentH,Number(window.parent.innerHeight)||parentH)}catch(_){ }
  const h=Math.max(500,Math.min(900,Math.floor(parentH-245)));
  root.style.setProperty('--p48-desktop-body-h',h+'px');
}
syncDesktopViewportHeight();window.addEventListener('resize',syncDesktopViewportHeight);
const runtimeErrorEl=root.querySelector('#p48-runtime-error');
function reportRuntimeError(error,context='runtime',showBanner=true){
  const info=MapliniReliabilityCore.errorInfo(error,context);
  console.error('[Maplini]',info.context,info.message,error);
  if(showBanner&&runtimeErrorEl){
    runtimeErrorEl.textContent='Ett fel inträffade. Ditt senaste lokala läge har inte raderats.';
    runtimeErrorEl.hidden=false;
  }
  try{localStorage.setItem('maplini_last_runtime_error',JSON.stringify(info))}catch(ignore){}
  return info;
}
function clearRuntimeError(){if(runtimeErrorEl){runtimeErrorEl.hidden=true;runtimeErrorEl.textContent='';}}
/* Browser/iframe noise is logged for diagnostics but must not present a data-safety warning.
   Explicit Maplini operations still call reportRuntimeError() with the banner enabled. */
window.addEventListener('error',e=>reportRuntimeError(e.error||e.message,'window.error',false));
window.addEventListener('unhandledrejection',e=>reportRuntimeError(e.reason,'unhandledrejection',false));
const canvas=root.querySelector('#p48-canvas'),scroll=root.querySelector('#p48-scroll'),emptyState=root.querySelector('#p48-empty-state'),emptyObject=root.querySelector('#p48-empty-object'),emptyActivity=root.querySelector('#p48-empty-activity'),linkLayer=root.querySelector('#p48-links'),temp=root.querySelector('#p48-temp'),snapGuideX=root.querySelector('#p48-snap-guide-x'),snapGuideY=root.querySelector('#p48-snap-guide-y');
const mobileToolsBtn=root.querySelector('#p48-mobile-tools'),mobileBackdrop=root.querySelector('#p48-mobile-backdrop'),sidePanel=root.querySelector('#p48-side');
const mobileBar=root.querySelector('#p48-mobile-bar'),mobileAdd=root.querySelector('#p48-mobile-add'),mobileUndo=root.querySelector('#p48-mobile-undo'),mobileRedo=root.querySelector('#p48-mobile-redo'),mobileFit=root.querySelector('#p48-mobile-fit'),mobileFullscreen=root.querySelector('#p48-mobile-fullscreen'),mobileMore=root.querySelector('#p48-mobile-more'),mobileNext=root.querySelector('#p48-mobile-next'),mobileFormat=root.querySelector('#p48-mobile-format'),mobileDuplicate=root.querySelector('#p48-mobile-duplicate'),mobileContext=root.querySelector('#p48-mobile-context'),mobileDelete=root.querySelector('#p48-mobile-delete');
const mobileSheet=root.querySelector('#p48-mobile-sheet'),mobileSheetBackdrop=root.querySelector('#p48-mobile-sheet-backdrop'),mobileSheetClose=root.querySelector('#p48-mobile-sheet-close'),mobileSheetTitle=root.querySelector('#p48-mobile-sheet-title'),mobileAddSheet=root.querySelector('#p48-mobile-add-sheet'),mobileSheetRedo=root.querySelector('#p48-mobile-sheet-redo'),mobileSheetFullscreen=root.querySelector('#p48-mobile-sheet-fullscreen'),mobileContextSheet=root.querySelector('#p48-mobile-context-sheet'),mobileOpenTools=root.querySelector('#p48-mobile-open-tools'),mobileSheetTools=root.querySelector('#p48-mobile-sheet-tools'),mobileSheetCopy=root.querySelector('#p48-mobile-sheet-copy'),mobileSheetFormat=root.querySelector('#p48-mobile-sheet-format'),mobileSheetLayoutH=root.querySelector('#p48-mobile-sheet-layout-h'),mobileSheetLayoutV=root.querySelector('#p48-mobile-sheet-layout-v'),mobileSheetDelete=root.querySelector('#p48-mobile-sheet-delete');
const linkHitLayer=root.querySelector('#p48-link-hit-layer');
const hnav=root.querySelector('#p48-hnav'),hnavInner=root.querySelector('#p48-hnav-inner');
const nameInput=root.querySelector('#p48-name'),status=root.querySelector('#p48-status'),processBox=root.querySelector('#p48-processes');
const newProcessDialog=root.querySelector('#p48-new-process-dialog'),newProcessBackdrop=root.querySelector('#p48-new-process-backdrop'),newProcessName=root.querySelector('#p48-new-process-name'),newProcessCreate=root.querySelector('#p48-new-process-create'),newProcessCancel=root.querySelector('#p48-new-process-cancel'),newProcessError=root.querySelector('#p48-new-process-error');
const saveState=root.querySelector('#p48-save-state'),recoveryBanner=root.querySelector('#p48-recovery-banner'),recoveryRestore=root.querySelector('#p48-recovery-restore'),recoveryIgnore=root.querySelector('#p48-recovery-ignore');
const analyzeBtn=root.querySelector('#p48-analyze'),analysisPanel=root.querySelector('#p48-analysis-panel'),analysisClose=root.querySelector('#p48-analysis-close'),analysisScore=root.querySelector('#p48-analysis-score'),analysisErrors=root.querySelector('#p48-analysis-errors'),analysisWarnings=root.querySelector('#p48-analysis-warnings'),analysisInfo=root.querySelector('#p48-analysis-info'),analysisNext=root.querySelector('#p48-analysis-next'),analysisNextTitle=root.querySelector('#p48-analysis-next-title'),analysisNextAction=root.querySelector('#p48-analysis-next-action'),analysisNextShow=root.querySelector('#p48-analysis-next-show'),analysisList=root.querySelector('#p48-analysis-list');
const controls=root.querySelector('#p48-controls'),formatPanel=root.querySelector('#p48-format-panel'),formatTitle=root.querySelector('#p48-format-title'),formatHint=root.querySelector('#p48-format-hint'),font=root.querySelector('#p48-font'),size=root.querySelector('#p48-size'),textColor=root.querySelector('#p48-textcolor'),bgColor=root.querySelector('#p48-bgcolor');
const bold=root.querySelector('#p48-bold'),italic=root.querySelector('#p48-italic'),under=root.querySelector('#p48-under');
const documentLinkEditor=root.querySelector('#p48-document-link-editor'),documentUrlInput=root.querySelector('#p48-document-url'),documentOpenEditor=root.querySelector('#p48-document-open-editor');
const fontAllBtn=root.querySelector('#p48-font-all');
const nodeStyleSelect=root.querySelector('#p48-node-style'),nodeStyleAllBtn=root.querySelector('#p48-node-style-all');
const pointSize=root.querySelector('#p48-point-size'),pointColor=root.querySelector('#p48-point-color'),hidePoints=root.querySelector('#p48-hide-points');
const canvasBg=root.querySelector('#p48-canvas-bg'),bgType=root.querySelector('#p48-bg-type'),bgPatternColor=root.querySelector('#p48-bg-pattern-color'),bgDensity=root.querySelector('#p48-bg-density'),logoFile=root.querySelector('#p48-logo-file'),logoRemove=root.querySelector('#p48-logo-remove'),logoHide=root.querySelector('#p48-logo-hide'),logoSize=root.querySelector('#p48-logo-size'),processLogo=root.querySelector('#p48-process-logo');
const gradientControls=root.querySelector('#p48-gradient-controls'),gradientStart=root.querySelector('#p48-gradient-start'),gradientEnd=root.querySelector('#p48-gradient-end'),gradientAngle=root.querySelector('#p48-gradient-angle');
const imageBgControls=root.querySelector('#p48-image-bg-controls'),bgImageFile=root.querySelector('#p48-bg-image-file'),bgImageRemove=root.querySelector('#p48-bg-image-remove'),bgImageOpacity=root.querySelector('#p48-bg-image-opacity'),bgImageOpacityValue=root.querySelector('#p48-bg-image-opacity-value');
const watermarkControls=root.querySelector('#p48-watermark-controls'),watermarkText=root.querySelector('#p48-watermark-text'),watermarkUseLogo=root.querySelector('#p48-watermark-use-logo'),watermarkOpacity=root.querySelector('#p48-watermark-opacity'),watermarkOpacityValue=root.querySelector('#p48-watermark-opacity-value'),canvasWatermark=root.querySelector('#p48-canvas-watermark');
const emailInput=root.querySelector('#p48-email'),passwordInput=root.querySelector('#p48-password');
const loginBtn=root.querySelector('#p48-login'),signupBtn=root.querySelector('#p48-signup'),logoutBtn=root.querySelector('#p48-logout');
const signedOut=root.querySelector('#p48-account-signedout'),signedIn=root.querySelector('#p48-account-signedin'),userEmail=root.querySelector('#p48-user-email');
const cloudBadge=root.querySelector('#p48-cloud-badge'),cloudHelp=root.querySelector('#p48-cloud-help');
const printFrame=root.querySelector('#p48-print-frame');
const pdfViewSelect=root.querySelector('#p48-pdf-view'),pageCountSelect=root.querySelector('#p48-page-count'),pageQuick=root.querySelector('#p48-page-quick'),pageQuickSummary=root.querySelector('#p48-page-quick-summary'),pageFormatQuick=root.querySelector('#p48-page-format-quick'),pageCountQuick=root.querySelector('#p48-page-count-quick');
const workspaceSelect=root.querySelector('#p48-workspace-select'),workspaceName=root.querySelector('#p48-workspace-name'),createWorkspaceBtn=root.querySelector('#p48-create-workspace'),roleBadge=root.querySelector('#p48-role');
const authError=root.querySelector('#p48-auth-error');
const shareBtn=root.querySelector('#p48-share'),shareBox=root.querySelector('#p48-sharebox'),shareUrlInput=root.querySelector('#p48-share-url'),copyShareBtn=root.querySelector('#p48-copy-share');
const marquee=root.querySelector('#p48-marquee');
const selectToolBtn=root.querySelector('#p48-select-tool');
const deleteSelectionBtn=root.querySelector('#p48-delete-selection'),duplicateSelectionBtn=root.querySelector('#p48-duplicate-selection'),clearCanvasBtn=root.querySelector('#p48-clear-canvas');
const zoomOutBtn=root.querySelector('#p48-zoom-out'),zoomResetBtn=root.querySelector('#p48-zoom-reset'),zoomInBtn=root.querySelector('#p48-zoom-in');
const fitScreenBtn=root.querySelector('#p48-fit-screen'),arrangeMenu=root.querySelector('#p48-arrange-menu'),arrangeHint=root.querySelector('#p48-arrange-hint'),alignChoices=[...root.querySelectorAll('.p48-align-choice')],distributeChoices=[...root.querySelectorAll('.p48-distribute-choice')];
const scaleMenu=root.querySelector('#p48-scale-menu'),processScaleSlider=root.querySelector('#p48-process-scale'),processScaleValue=root.querySelector('#p48-process-scale-value'),scaleFitPageBtn=root.querySelector('#p48-scale-fit-page');
const accountPanel=root.querySelector('#p48-account-panel'),accountSummaryState=root.querySelector('#p48-account-summary-state');
const smartLayoutMenu=root.querySelector('#p48-smart-layout-menu'),autoCleanBtn=root.querySelector('#p48-auto-clean'),smartLayoutHint=root.querySelector('#p48-smart-layout-hint'),smartLayoutChoices=[...root.querySelectorAll('.p48-smart-layout-choice')];
const inputsBox=root.querySelector('#p48-inputs'),outputsBox=root.querySelector('#p48-outputs');
const processInfoPanel=root.querySelector('#p48-process-info'),processInfoProgress=root.querySelector('#p48-process-info-progress'),processInfoMore=root.querySelector('#p48-process-info-more'),processInfoMoreCount=root.querySelector('#p48-process-info-more-count'),roleSuggestions=root.querySelector('#p48-role-suggestions'),systemSuggestions=root.querySelector('#p48-system-suggestions');
const processInfoFields={
  description:root.querySelector('#p48-info-description'),
  responsibleRole:root.querySelector('#p48-info-role'),
  system:root.querySelector('#p48-info-system'),
  duration:root.querySelector('#p48-info-duration'),
  kpi:root.querySelector('#p48-info-kpi'),
  instruction:root.querySelector('#p48-info-instruction'),
  risk:root.querySelector('#p48-info-risk'),
  control:root.querySelector('#p48-info-control')
};
const borderColor=root.querySelector('#p48-bordercolor'),borderWidth=root.querySelector('#p48-borderwidth');
const linkFormat=root.querySelector('#p48-link-format'),linkColor=root.querySelector('#p48-link-color'),linkWidth=root.querySelector('#p48-link-width'),linkEnd=root.querySelector('#p48-link-end'),linkDash=root.querySelector('#p48-link-dash'),linkRouting=root.querySelector('#p48-link-routing'),linkAnchorMode=root.querySelector('#p48-link-anchor-mode'),linkLabel=root.querySelector('#p48-link-label'),flowCoach=root.querySelector('#p48-flow-coach'),flowCoachInsert=root.querySelector('#p48-flow-coach-insert'),flowCoachKeep=root.querySelector('#p48-flow-coach-keep'),insertLinkStepBtn=root.querySelector('#p48-insert-link-step'),insertLinkStepWrap=root.querySelector('#p48-insert-step-wrap'),insertLinkStepMenu=root.querySelector('#p48-insert-step-menu'),insertLinkStepChoices=[...root.querySelectorAll('.p48-insert-step-choice')],deleteLinkBtn=root.querySelector('#p48-delete-link'),linkHandle=root.querySelector('#p48-link-handle'),linkQuick=root.querySelector('#p48-link-quick'),linkQuickRouting=[...root.querySelectorAll('[data-link-routing]')];
const addInputBtn=root.querySelector('#p48-add-input'),addOutputBtn=root.querySelector('#p48-add-output'),deleteNodeBtn=root.querySelector('#p48-delete-node');
const nodeQuick=root.querySelector('#p48-node-quick'),nodeQuickFlow=root.querySelector('#p48-node-quick-flow'),nodeQuickNext=root.querySelector('#p48-node-quick-next'),nodeQuickNextMore=root.querySelector('#p48-node-quick-next-more'),nodeQuickFormat=root.querySelector('#p48-node-quick-format'),nodeQuickColor=root.querySelector('#p48-node-quick-color'),nodeQuickDuplicate=root.querySelector('#p48-node-quick-duplicate'),nodeQuickArrange=root.querySelector('#p48-node-quick-arrange'),nodeQuickDelete=root.querySelector('#p48-node-quick-delete'),nodeQuickAlign=[...root.querySelectorAll('[data-node-quick-align]')],nodeQuickDistribute=[...root.querySelectorAll('[data-node-quick-distribute]')];

let nodes=new Map(),links=[],selectedId=null,selectedIds=new Set(),selectionMode=false,seq=8,undo=[],redo=[],currentId='proc-1',processes={};
let editingClipboard=null,clipboardPasteOffset=28;
let selectedLinkIndex=null,selectedLinkIndices=new Set();
const nodeGeomCache=new Map();
let geomVersion=0;
let connectorPointSize=8,connectorPointColor='#1f6f55',connectorPointsHidden=false;
let processBackground='#ffffff',processBackgroundType='solid',processPatternColor='#d7e1e8',processPatternDensity=20,processGradientStart='#ffffff',processGradientEnd='#e7f1ff',processGradientAngle=45,processBackgroundImageData='',processBackgroundImageOpacity=.25,processWatermarkText='UTKAST',processWatermarkOpacity=.15,processWatermarkUseLogo=false,processLogoData='',processLogoHidden=false,processLogoWidth=180,processLogoX=28,processLogoY=28;
const SUPABASE_URL="__SUPABASE_URL__", SUPABASE_ANON_KEY="__SUPABASE_ANON_KEY__", PUBLIC_APP_URL="__PUBLIC_APP_URL__";
const CLOUD_ENABLED=SUPABASE_URL.length>0&&SUPABASE_ANON_KEY.length>0;
let cloudSession=null,sharedView=false;
let cloudLoadedProcessIds=new Set();
let cloudLoadedProcessScopes=new Map();
let currentWorkspaceId=null,currentWorkspaceOwnerId=null,currentRole='owner',printPreview=false;
let pdfView='A4P',pageCountMode='auto',canvasScale=1,canvasLogicalWidth=2400,canvasLogicalHeight=1400,processScalePercent=100,processScaleGesture=false;


function clampCanvasScale(value){return Math.max(0.25,Math.min(1.5,Math.round(Number(value)*100)/100))}
function applyCanvasScale(next,keepCenter=true){
  const old=canvasScale;
  const value=clampCanvasScale(next);
  if(value===old&&canvas.style.getPropertyValue('--p48-canvas-scale'))return value;
  let logicalCenterX=0,logicalCenterY=0;
  if(keepCenter&&scroll){
    logicalCenterX=(scroll.scrollLeft+scroll.clientWidth/2)/old;
    logicalCenterY=(scroll.scrollTop+scroll.clientHeight/2)/old;
  }
  canvasScale=value;
  canvas.style.setProperty('--p48-canvas-scale',String(value));
  canvas.style.setProperty('--p48-toolbar-inverse-scale',String(1/value));
  const wrap=canvas.parentElement;
  if(wrap){
    wrap.style.setProperty('--p48-canvas-visual-width',(canvasLogicalWidth*value)+'px');
    wrap.style.setProperty('--p48-canvas-visual-height',(canvasLogicalHeight*value)+'px');
  }
  if(zoomResetBtn)zoomResetBtn.textContent=Math.round(value*100)+'%';
  if(zoomOutBtn)zoomOutBtn.disabled=value<=0.25;
  if(zoomInBtn)zoomInBtn.disabled=value>=1.5;
  if(keepCenter&&scroll){
    requestAnimationFrame(()=>{
      scroll.scrollLeft=Math.max(0,logicalCenterX*value-scroll.clientWidth/2);
      scroll.scrollTop=Math.max(0,logicalCenterY*value-scroll.clientHeight/2);
      if(hnav)hnav.scrollLeft=scroll.scrollLeft;
    });
  }
  scheduleHorizontalNavSync();
  refreshMobileBar();
  return value;
}
function screenDeltaToCanvas(dx,dy){return{dx:dx/canvasScale,dy:dy/canvasScale}}

function syncHorizontalNavWidth(){
  if(!hnav||!hnavInner)return;
  const w=Math.max(canvasLogicalWidth*canvasScale,scroll?.clientWidth||0);
  hnavInner.style.width=w+'px';
}
let hnavSyncRaf=0;
function scheduleHorizontalNavSync(){
  if(hnavSyncRaf)return;
  hnavSyncRaf=requestAnimationFrame(()=>{
    hnavSyncRaf=0;
    syncHorizontalNavWidth();
  });
}
let syncingH=false;
if(hnav){
  hnav.addEventListener('scroll',()=>{
    if(syncingH)return;
    syncingH=true;
    scroll.scrollLeft=hnav.scrollLeft;
    requestAnimationFrame(()=>{syncingH=false});
  });
}
scroll.addEventListener('scroll',()=>{
  if(!hnav||syncingH)return;
  syncingH=true;
  hnav.scrollLeft=scroll.scrollLeft;
  requestAnimationFrame(()=>{syncingH=false});
});
scroll.addEventListener('wheel',(e)=>{
  if(e.shiftKey){
    e.preventDefault();
    scroll.scrollLeft += (Math.abs(e.deltaY)>Math.abs(e.deltaX)?e.deltaY:e.deltaX);
    if(hnav)hnav.scrollLeft=scroll.scrollLeft;
  }
},{passive:false});
window.addEventListener('resize',()=>{
  if(typeof updateCanvasExtentForPages==='function')updateCanvasExtentForPages();
  if(typeof scheduleHorizontalNavSync==='function')scheduleHorizontalNavSync();
  if(typeof refreshNodeQuickToolbar==='function')refreshNodeQuickToolbar();
  if(typeof refreshLinkControls==='function')refreshLinkControls();
});
setTimeout(scheduleHorizontalNavSync,0);




const starter={id:'proc-1',name:'Exempel – upphandlingsprocess',nodes:[
{id:'n1',type:'start',text:'Upphandling identifieras',x:100,y:130},{id:'n2',type:'process',text:'Första bedömning',x:390,y:130},{id:'n3',type:'decision',text:'Relevant?',x:680,y:110},{id:'n4',type:'process',text:'Kvalificera upphandling',x:950,y:130}
],links:[['n1','n2','right'],['n2','n3','right'],['n3','n4','right']]};


function cloudKey(){return'maplini_supabase_session'}
function workspacePrefKey(){return MapliniSessionCore.workspacePrefKey(ownerId())}
function loadWorkspacePreference(){
  if(!ownerId())return null;
  try{return localStorage.getItem(workspacePrefKey())||null}catch(e){return null}
}
function saveWorkspacePreference(id){
  if(!ownerId())return;
  try{
    const key=workspacePrefKey();
    if(id)localStorage.setItem(key,id);else localStorage.removeItem(key);
  }catch(e){}
}
function resetWorkspaceState(){
  currentWorkspaceId=null;currentWorkspaceOwnerId=null;currentRole='owner';
  if(workspaceSelect){workspaceSelect.innerHTML='<option value="">Personligt</option>';workspaceSelect.value=''}
  if(roleBadge)roleBadge.textContent='Owner';
  applyRoleUi();
}

function updateAccountUi(){
 const logged=!!(cloudSession?.access_token&&cloudSession?.user);
 signedOut.hidden=logged;signedIn.hidden=!logged;
 if(logged)userEmail.textContent=cloudSession.user.email||'Inloggad';
 shareBtn.disabled=!logged||!CLOUD_ENABLED||sharedView||!MapliniAccessCore.canEdit({sharedView,currentRole});
 if(CLOUD_ENABLED&&logged){cloudBadge.className='p48-cloud-badge';cloudBadge.textContent='Moln anslutet';cloudHelp.textContent='Spara och dela mellan enheter.'}
 else if(CLOUD_ENABLED){cloudBadge.className='p48-cloud-badge off';cloudBadge.textContent='Ej inloggad';cloudHelp.textContent='Logga in för molnlagring.'}
 else{cloudBadge.className='p48-cloud-badge off';cloudBadge.textContent='Lokal lagring';cloudHelp.textContent='Lägg in Supabase i Streamlit Secrets.'}
}
function loadCloudSession(){try{cloudSession=JSON.parse(localStorage.getItem(cloudKey())||'null')}catch(e){cloudSession=null}updateAccountUi()}
function saveCloudSession(v){cloudSession=v||null;try{cloudSession?localStorage.setItem(cloudKey(),JSON.stringify(cloudSession)):localStorage.removeItem(cloudKey())}catch(e){}updateAccountUi()}
function clearAuthError(){authError.style.display='none';authError.textContent=''}
function showAuthError(prefix,err){
  const detail=(err&&err.message)?err.message:String(err||'Okänt fel');
  authError.textContent=prefix+': '+detail;
  authError.style.display='block';
}
function friendlyAuthMessage(err){
  const t=((err&&err.message)||String(err||'')).toLowerCase();
  if(t.includes('already registered')||t.includes('already exists')||t.includes('user already'))return 'Kontot finns redan. Använd Logga in.';
  if(t.includes('invalid login credentials'))return 'Fel e-postadress eller lösenord.';
  if(t.includes('email not confirmed'))return 'E-postadressen är inte bekräftad ännu.';
  if(t.includes('signup is disabled'))return 'Registrering är avstängd i Supabase Authentication.';
  if(t.includes('invalid api key')||t.includes('apikey'))return 'Den publika Supabase-nyckeln verkar vara fel.';
  if(t.includes('failed to fetch')||t.includes('network'))return 'Maplini kunde inte nå Supabase. Kontrollera Project URL och internetanslutning.';
  return (err&&err.message)?err.message:String(err||'Okänt fel');
}
async function sb(path,opt={},auth=true){
  if(!CLOUD_ENABLED)throw new Error('Supabase är inte konfigurerat i Streamlit Secrets.');
  const headers=Object.assign({
    'apikey':SUPABASE_ANON_KEY,
    'Accept':'application/json',
    'Content-Type':'application/json'
  },opt.headers||{});
  if(auth&&cloudSession?.access_token)headers.Authorization='Bearer '+cloudSession.access_token;
  const r=await fetch(SUPABASE_URL+path,Object.assign({},opt,{headers}));
  const raw=await r.text();
  let d=null;
  try{d=raw?JSON.parse(raw):null}catch(e){d=raw}
  if(!r.ok){
    const detail=(d&&(
      d.msg||d.message||d.error_description||d.error||
      (Array.isArray(d.errors)&&d.errors.map(x=>x.message||x).join(', '))
    ))||raw||('HTTP '+r.status);
    const err=new Error(detail);
    err.status=r.status;
    err.payload=d;
    throw err;
  }
  return d;
}
async function testSupabaseConnection(){
  clearAuthError();
  if(!CLOUD_ENABLED){showAuthError('Supabase-test',new Error('Supabase saknas i Streamlit Secrets.'));return}
  try{
    await sb('/auth/v1/settings',{method:'GET'},false);
    cloudBadge.className='p48-cloud-badge';
    cloudBadge.textContent='Supabase nåbar';
    cloudHelp.textContent='Project URL och publishable key fungerar.';
    msg('Supabase-anslutning OK');
  }catch(e){
    console.error(e);
    showAuthError('Supabase-test',new Error(friendlyAuthMessage(e)));
    msg('Supabase-test misslyckades');
  }
}
async function validateSession(){
  if(!cloudSession?.access_token){
    resetWorkspaceState();
    return false;
  }
  try{
    const u=await sb('/auth/v1/user',{method:'GET'},true);
    if(u&&u.id){
      cloudSession.user=u;
      saveCloudSession(cloudSession);
      return true;
    }
  }catch(e){
    console.warn('Session invalid',e);
  }
  cloudLoadedProcessIds.clear();cloudLoadedProcessScopes.clear();
  saveCloudSession(null);resetWorkspaceState();
  return false;
}
async function signIn(){
  clearAuthError();
  const email=emailInput.value.trim(),password=passwordInput.value;
  if(!email||!password){msg('Fyll i e-post och lösenord');return}
  try{
    const d=await sb('/auth/v1/token?grant_type=password',{
      method:'POST',
      body:JSON.stringify({email,password})
    },false);
    if(!d?.access_token)throw new Error('Supabase returnerade ingen access token.');
    saveCloudSession(d);
    const valid=await validateSession();
    if(!valid)throw new Error('Sessionen kunde inte verifieras.');
    await loadWorkspaces();
    applyRoleUi();
    msg('Inloggad');
    await loadCloudProcesses();
  }catch(e){
    console.error(e);
    const text=friendlyAuthMessage(e);
    showAuthError('Inloggning',new Error(text));
    msg(text);
  }
}
async function signUp(){
  clearAuthError();
  const email=emailInput.value.trim(),password=passwordInput.value;
  if(!email||password.length<6){msg('Ange e-post och minst 6 tecken');return}
  try{
    const d=await sb('/auth/v1/signup',{
      method:'POST',
      body:JSON.stringify({email,password})
    },false);
    if(d?.access_token){
      saveCloudSession(d);
      const valid=await validateSession();
      if(!valid)throw new Error('Sessionen kunde inte verifieras.');
      await loadWorkspaces();
      applyRoleUi();
      msg('Konto skapat och inloggat');
      await loadCloudProcesses();
    }else if(d?.user){
      msg('Konto skapat – kontrollera din e-post innan du loggar in');
      cloudHelp.textContent='Konto skapat. Bekräfta e-postadressen om Supabase kräver det.';
    }else{
      throw new Error('Supabase skapade inget konto och returnerade ingen användare.');
    }
  }catch(e){
    console.error(e);
    const text=friendlyAuthMessage(e);
    showAuthError('Skapa konto',new Error(text));
    msg(text);
  }
}
function signOut(){
  clearAuthError();
  persist(false,false);saveLocal(true);
  const plan=MapliniSyncCore.signOutPlan(processes,[...cloudLoadedProcessIds],currentId);
  processes=plan.processes;currentId=plan.currentId||currentId;
  cloudLoadedProcessIds.clear();cloudLoadedProcessScopes.clear();
  saveCloudSession(null);resetWorkspaceState();
  if(plan.removedIds.length){
    if(processes[currentId])restore(processes[currentId]);
    else{
      currentId=uid();
      processes[currentId]=MapliniWorkflowCore.emptyProcess(currentId,'Ny process');
      processes[currentId].localModifiedAt=Date.now();
      restore(processes[currentId]);
    }
    saveLocal(true);renderProcesses(true);
  }
  msg(plan.preservedModifiedIds.length?'Utloggad · lokalt ändrade processer behölls':'Utloggad');
}
function ownerId(){return cloudSession?.user?.id||null}
async function saveCurrentToCloud(){
  if(!requireEdit())throw new Error('Endast visning');
  if(!ownerId())throw new Error('Logga in först');
  persist(false,false);
  const localOk=saveLocal(true);
  const st=clone(processes[currentId]||state());
  const updatedAt=new Date().toISOString();
  const canonicalOwnerId=currentWorkspaceId?currentWorkspaceOwnerId:ownerId();
  if(currentWorkspaceId&&!canonicalOwnerId)throw new Error('Workspace-ägaren kunde inte verifieras. Ladda om workspace och försök igen.');
  await sb('/rest/v1/processes?on_conflict=id',{
    method:'POST',
    headers:{Prefer:'resolution=merge-duplicates,return=minimal'},
    body:JSON.stringify({id:currentId,owner_id:canonicalOwnerId,workspace_id:currentWorkspaceId,name:st.name,data:st,updated_at:updatedAt})
  });
  processes[currentId]=Object.assign({},st,{cloudUpdatedAt:updatedAt});
  cloudLoadedProcessIds.add(currentId);
  cloudLoadedProcessScopes.set(currentId,MapliniSessionCore.scopeKey(currentWorkspaceId));
  saveLocal(true);
  return {localOk,cloudOk:true,updatedAt};
}
async function loadCloudProcesses(){
  if(!ownerId())return false;
  persist(false,false);saveLocal(true);
  const before=MapliniRcCore.captureScopeState(processes,currentId,cloudLoadedProcessIds,cloudLoadedProcessScopes);
  try{
    const scope=MapliniSessionCore.scopeKey(currentWorkspaceId);
    const staleIds=[...cloudLoadedProcessScopes.entries()].filter(([,s])=>s!==scope).map(([id])=>id);
    if(staleIds.length){
      const plan=MapliniSyncCore.signOutPlan(processes,staleIds,currentId);
      processes=plan.processes;currentId=plan.currentId||currentId;
      for(const id of staleIds){cloudLoadedProcessIds.delete(id);cloudLoadedProcessScopes.delete(id)}
      if(!processes[currentId]){
        currentId=uid();processes[currentId]=MapliniWorkflowCore.emptyProcess(currentId,'Ny process');
        processes[currentId].localModifiedAt=Date.now();
      }
      restore(processes[currentId]);
    }
    const q=currentWorkspaceId
      ?('/rest/v1/processes?select=id,name,data,updated_at&workspace_id=eq.'+encodeURIComponent(currentWorkspaceId)+'&order=updated_at.desc')
      :('/rest/v1/processes?select=id,name,data,updated_at&workspace_id=is.null&order=updated_at.desc');
    const rows=await sb(q);
    const merged=MapliniSyncCore.mergeCloudRows(processes,rows||[]);
    processes=merged.processes;
    for(const id of merged.cloudLoadedIds){cloudLoadedProcessIds.add(id);cloudLoadedProcessScopes.set(id,scope)}
    currentId=MapliniRcCore.ensureCurrentId(processes,currentId,merged.cloudLoadedIds);
    if(processes[currentId])restore(processes[currentId]);
    saveLocal(true);renderProcesses(true);refreshControls();refreshLinkControls();updateSelectionUi();
    if(merged.preservedLocalIds.length)msg('Molnet läst · nyare lokala ändringar behölls');
    return true;
  }catch(e){
    const restored=MapliniRcCore.restoreScopeState(before);
    processes=restored.processes;currentId=restored.currentId;
    cloudLoadedProcessIds=new Set(restored.cloudLoadedIds);
    cloudLoadedProcessScopes=new Map(restored.cloudLoadedScopes);
    if(processes[currentId])restore(processes[currentId]);
    saveLocal(true);renderProcesses(true);refreshControls();refreshLinkControls();updateSelectionUi();
    console.error(e);reportRuntimeError(e,'cloud-load');msg('Kunde inte läsa molnet · tidigare läge återställt');
    return false;
  }
}
function shareToken(){return crypto?.randomUUID?crypto.randomUUID().replace(/-/g,''):Math.random().toString(36).slice(2)+Date.now().toString(36)}
async function shareCurrent(){try{await saveCurrentToCloud();const rows=await sb('/rest/v1/processes?id=eq.'+encodeURIComponent(currentId)+'&select=share_token');const token=rows?.[0]?.share_token||shareToken();await sb('/rest/v1/processes?id=eq.'+encodeURIComponent(currentId),{method:'PATCH',headers:{Prefer:'return=minimal'},body:JSON.stringify({share_token:token,share_mode:'view'})});shareUrlInput.value=PUBLIC_APP_URL.replace(/\/$/,'')+'?share='+token;shareBox.style.display='block';msg('Delningslänk skapad')}catch(e){console.error(e);reportRuntimeError(e,'share-current');msg('Delning misslyckades')}}
async function loadShared(token){
  if(!CLOUD_ENABLED||!token)return false;
  try{
    const rows=await sb('/rest/v1/processes?share_token=eq.'+encodeURIComponent(token)+'&share_mode=eq.view&select=id,name,data',{},false);
    if(!rows?.length){msg('Delningslänken är ogiltig eller inte längre aktiv');return false}
    const row=rows[0];
    const candidate=MapliniFlowCore.sharedProcess(row);
    if(!candidate||!MapliniReliabilityCore.isUsableProcess(candidate)){
      reportRuntimeError(new Error('Invalid shared process payload'),'shared-load');
      msg('Den delade processen kunde inte läsas');
      return false;
    }
    sharedView=true;currentId=candidate.id;processes={[candidate.id]:candidate};
    if(!restore(candidate)){
      sharedView=false;processes={};
      msg('Den delade processen kunde inte öppnas');
      return false;
    }
    renderProcesses();
    updateAccountUi();applyRoleUi();refreshControls();refreshLinkControls();updateSelectionUi();
    msg('Delad process – endast visning');return true;
  }catch(e){
    console.error(e);reportRuntimeError(e,'shared-load');msg('Kunde inte läsa delningslänken');return false;
  }
}
async function deleteCloud(id){
  if(!ownerId())return true;
  try{
    await sb('/rest/v1/processes?id=eq.'+encodeURIComponent(id),{method:'DELETE',headers:{Prefer:'return=minimal'}});
    return true;
  }catch(e){
    reportRuntimeError(e,'cloud-delete');
    return false;
  }
}


function canEdit(){return MapliniAccessCore.canEdit({sharedView,currentRole})}
function requireEdit(show=true){
  if(canEdit())return true;
  if(show)msg('Endast visning');
  return false;
}
function applyRoleUi(){
  if(roleBadge)roleBadge.textContent=currentRole.charAt(0).toUpperCase()+currentRole.slice(1);
  const editable=canEdit();
  root.querySelectorAll('.p48-item,.p48-format input,.p48-format select,.p48-format button,.p48-step-io input,.p48-step-io button').forEach(el=>{
    el.style.pointerEvents=editable?'':'none';el.style.opacity=editable?'':'0.5';
  });
  const mutationSelectors=[
    '#p48-name','#p48-new','#p48-save','#p48-undo','#p48-redo','#p48-delete-selection',
    '#p48-canvas-bg','#p48-bg-type','#p48-bg-pattern-color','#p48-bg-density',
    '#p48-logo-file','#p48-logo-remove','#p48-logo-hide','#p48-logo-size',
    '#p48-gradient-start','#p48-gradient-end','#p48-gradient-angle','#p48-bg-image-file','#p48-bg-image-remove','#p48-bg-image-opacity','#p48-watermark-text','#p48-watermark-use-logo','#p48-watermark-opacity'
  ];
  mutationSelectors.forEach(sel=>{const el=root.querySelector(sel);if(el)el.disabled=!editable});
  if(shareBtn)shareBtn.disabled=!editable||!ownerId()||!CLOUD_ENABLED||sharedView;
  canvas.classList.toggle('p48-readonly',!editable);
  if(!editable){
    selectionMode=false;
    canvas.classList.remove('p48-selection-mode');
    marquee.style.display='none';
    finishTempArrow();
  }
}
async function loadWorkspaces(){
  if(!ownerId()){resetWorkspaceState();return false}
  try{
    const rows=await sb('/rest/v1/workspace_members?select=role,workspace_id,workspaces(id,name,owner_id)&user_id=eq.'+encodeURIComponent(ownerId()));
    const entries=(rows||[]).filter(row=>row&&row.workspaces&&row.workspace_id);
    const preferred=currentWorkspaceId||loadWorkspacePreference();
    const chosen=MapliniSessionCore.chooseWorkspace(preferred,entries);
    workspaceSelect.innerHTML='<option value="">Personligt</option>';
    for(const row of entries){
      const o=document.createElement('option');o.value=row.workspace_id;o.textContent=row.workspaces.name;o.dataset.role=row.role;o.dataset.ownerId=row.workspaces.owner_id||'';workspaceSelect.appendChild(o);
    }
    currentWorkspaceId=chosen.id;
    currentRole=chosen.role;
    workspaceSelect.value=currentWorkspaceId||'';
    currentWorkspaceOwnerId=currentWorkspaceId?(workspaceSelect.selectedOptions[0]?.dataset.ownerId||null):ownerId();
    saveWorkspacePreference(currentWorkspaceId);
    applyRoleUi();
    return true;
  }catch(e){
    console.error(e);reportRuntimeError(e,'workspace-load');resetWorkspaceState();return false;
  }
}
async function createWorkspace(){
  if(!ownerId())return msg('Logga in först');
  const name=workspaceName.value.trim();if(!name)return msg('Ange namn');
  try{
    const id=crypto?.randomUUID?crypto.randomUUID():('ws-'+Date.now());
    await sb('/rest/v1/workspaces',{method:'POST',headers:{Prefer:'return=minimal'},body:JSON.stringify({id,name,owner_id:ownerId()})});
    await sb('/rest/v1/workspace_members',{method:'POST',headers:{Prefer:'return=minimal'},body:JSON.stringify({workspace_id:id,user_id:ownerId(),role:'owner'})});
    currentWorkspaceId=id;currentWorkspaceOwnerId=ownerId();currentRole='owner';saveWorkspacePreference(id);workspaceName.value='';await loadWorkspaces();workspaceSelect.value=id;applyRoleUi();
    const loaded=await loadCloudProcesses();
    msg(loaded?'Workspace skapat':'Workspace skapat · molndata kunde inte läsas');
  }catch(e){console.error(e);msg('Kunde inte skapa workspace')}
}
workspaceSelect.addEventListener('change',async()=>{
  const previousId=currentWorkspaceId,previousOwnerId=currentWorkspaceOwnerId,previousRole=currentRole;
  const nextId=workspaceSelect.value||null;
  const opt=workspaceSelect.selectedOptions[0];
  currentWorkspaceId=nextId;
  currentWorkspaceOwnerId=currentWorkspaceId?(opt?.dataset.ownerId||null):ownerId();
  currentRole=currentWorkspaceId?(opt?.dataset.role||'viewer'):'owner';
  saveWorkspacePreference(currentWorkspaceId);applyRoleUi();
  const ok=await loadCloudProcesses();
  if(ok){
    msg(currentWorkspaceId?'Workspace öppnat':'Personligt workspace öppnat');
    return;
  }
  currentWorkspaceId=previousId;currentWorkspaceOwnerId=previousOwnerId;currentRole=previousRole;workspaceSelect.value=previousId||'';
  saveWorkspacePreference(currentWorkspaceId);applyRoleUi();
  msg('Workspacebyte misslyckades · tidigare workspace återställt');
});
createWorkspaceBtn.addEventListener('click',createWorkspace);


function applyConnectorPointSettings(){
  for(const item of nodes.values()){
    for(const h of Object.values(item.handles||{})){
      h.style.width=connectorPointSize+'px';
      h.style.height=connectorPointSize+'px';
      h.style.background=connectorPointColor;
      h.style.border='1px solid #fff';
      h.style.boxShadow='0 0 0 1px '+connectorPointColor;
      h.style.display=connectorPointsHidden?'none':'';
    }
  }
  canvas.style.setProperty('--p48-point-size',connectorPointSize+'px');
  canvas.style.setProperty('--p48-point-color',connectorPointColor);
  canvas.classList.toggle('p48-hide-points',connectorPointsHidden);
  if(pointSize)pointSize.value=String(connectorPointSize);
  if(pointColor)pointColor.value=connectorPointColor;
  if(hidePoints)hidePoints.checked=connectorPointsHidden;
}


let lastProcessStyleSignature='';
const standardBackgroundTypes=new Set(['solid','dots','grid','image','watermark']);
const legacyBackgroundLabels={
  lines:'Linjer',gradient:'Gradient',crosshatch:'Korslinjer',diagonal:'Diagonalt rutmönster',
  technical:'Tekniskt rutnät',none:'Ingen bakgrund','texture-paper':'Gammalt papper',
  'texture-parchment':'Pergament','texture-canvas':'Canvas-textur','texture-concrete':'Betong'
};
function syncBackgroundTypeSelect(value){
  if(!bgType)return;
  const wanted=String(value||'solid');
  for(const option of [...bgType.querySelectorAll('option[data-legacy-background="true"]')])option.remove();
  if(!standardBackgroundTypes.has(wanted)){
    const option=document.createElement('option');
    option.value=wanted;
    option.textContent=`Tidigare bakgrund: ${legacyBackgroundLabels[wanted]||wanted}`;
    option.dataset.legacyBackground='true';
    bgType.appendChild(option);
  }
  bgType.value=wanted;
}
function applyProcessStyle(force=false){
  const signature=MapliniPerformanceCore.signature([
    processBackground,processBackgroundType,processPatternColor,processPatternDensity,
    processGradientStart,processGradientEnd,processGradientAngle,processBackgroundImageData,processBackgroundImageOpacity,
    processWatermarkText,processWatermarkOpacity,processWatermarkUseLogo,
    processLogoData,processLogoHidden,processLogoWidth,processLogoX,processLogoY
  ]);
  if(!force&&signature===lastProcessStyleSignature)return false;
  lastProcessStyleSignature=signature;
  const d=Math.max(8,Number(processPatternDensity)||20);
  const c=processPatternColor||'#d7e1e8';
  const bg=processBackground||'#ffffff';
  const type=processBackgroundType||'solid';

  canvas.style.backgroundColor=(type==='none')?'transparent':bg;
  canvas.style.backgroundImage='none';
  canvas.style.backgroundSize='';
  canvas.style.backgroundPosition='';
  canvas.style.backgroundRepeat='';

  if(type==='dots'){
    canvas.style.backgroundImage=`radial-gradient(circle, ${c} 1.2px, transparent 1.3px)`;
    canvas.style.backgroundSize=`${d}px ${d}px`;
  }else if(type==='grid'){
    canvas.style.backgroundImage=`linear-gradient(${c} 1px, transparent 1px),linear-gradient(90deg, ${c} 1px, transparent 1px)`;
    canvas.style.backgroundSize=`${d}px ${d}px`;
  }else if(type==='lines'){
    canvas.style.backgroundImage=`linear-gradient(${c} 1px, transparent 1px)`;
    canvas.style.backgroundSize=`100% ${d}px`;
  }else if(type==='crosshatch'){
    canvas.style.backgroundImage=`linear-gradient(${c} 1px, transparent 1px),linear-gradient(90deg, ${c} 1px, transparent 1px)`;
    canvas.style.backgroundSize=`${d*2}px ${d}px`;
  }else if(type==='diagonal'){
    canvas.style.backgroundImage=`repeating-linear-gradient(45deg, transparent 0, transparent ${d-1}px, ${c} ${d-1}px, ${c} ${d}px),
                                  repeating-linear-gradient(-45deg, transparent 0, transparent ${d-1}px, ${c} ${d-1}px, ${c} ${d}px)`;
  }else if(type==='technical'){
    const major=d*5;
    canvas.style.backgroundImage=`linear-gradient(${c} 1px, transparent 1px),
                                  linear-gradient(90deg, ${c} 1px, transparent 1px),
                                  linear-gradient(${c} 1.5px, transparent 1.5px),
                                  linear-gradient(90deg, ${c} 1.5px, transparent 1.5px)`;
    canvas.style.backgroundSize=`${d}px ${d}px,${d}px ${d}px,${major}px ${major}px,${major}px ${major}px`;
  }else if(type==='gradient'){
    canvas.style.backgroundImage=`linear-gradient(${Number(processGradientAngle)||0}deg, ${processGradientStart}, ${processGradientEnd})`;
  }else if(type==='image'&&processBackgroundImageData){
    const a=Math.max(.05,Math.min(1,Number(processBackgroundImageOpacity)||.25));
    canvas.style.backgroundImage=`linear-gradient(rgba(255,255,255,${1-a}),rgba(255,255,255,${1-a})),url("${processBackgroundImageData}")`;
    canvas.style.backgroundSize='cover';
    canvas.style.backgroundPosition='center';
    canvas.style.backgroundRepeat='no-repeat';
  }else if(type==='texture-paper'){
    canvas.style.backgroundColor='#f4efe4';
    canvas.style.backgroundImage='radial-gradient(circle at 20% 20%,rgba(126,93,55,.08) 0 1px,transparent 1.5px),radial-gradient(circle at 70% 65%,rgba(92,67,40,.06) 0 1px,transparent 1.5px),linear-gradient(90deg,rgba(111,82,47,.035),transparent 35%,rgba(111,82,47,.025))';
    canvas.style.backgroundSize='17px 19px,23px 29px,100% 100%';
  }else if(type==='texture-parchment'){
    canvas.style.backgroundColor='#f3dfb2';
    canvas.style.backgroundImage='radial-gradient(ellipse at center,rgba(255,255,255,.42),rgba(132,84,31,.12)),repeating-linear-gradient(8deg,rgba(123,84,40,.025) 0 1px,transparent 1px 7px)';
  }else if(type==='texture-canvas'){
    canvas.style.backgroundColor='#ece8dc';
    canvas.style.backgroundImage='repeating-linear-gradient(0deg,rgba(93,85,66,.07) 0 1px,transparent 1px 4px),repeating-linear-gradient(90deg,rgba(93,85,66,.055) 0 1px,transparent 1px 5px)';
  }else if(type==='texture-concrete'){
    canvas.style.backgroundColor='#dedfdf';
    canvas.style.backgroundImage='radial-gradient(circle at 15% 25%,rgba(70,75,78,.08) 0 1px,transparent 2px),radial-gradient(circle at 72% 44%,rgba(255,255,255,.28) 0 2px,transparent 3px),linear-gradient(135deg,rgba(85,90,92,.07),transparent 35%,rgba(255,255,255,.18))';
    canvas.style.backgroundSize='31px 27px,41px 37px,100% 100%';
  }

  if(canvasWatermark){
    canvasWatermark.innerHTML='';
    const show=type==='watermark';
    canvasWatermark.classList.toggle('on',show);
    canvasWatermark.style.opacity=String(Math.max(.05,Math.min(.4,Number(processWatermarkOpacity)||.15)));
    if(show){
      if(processWatermarkUseLogo&&processLogoData){
        const img=document.createElement('img');img.src=processLogoData;img.alt='';canvasWatermark.appendChild(img);
      }else{
        const span=document.createElement('span');span.textContent=(processWatermarkText||'UTKAST').slice(0,80);span.style.color=processPatternColor||'#64748b';canvasWatermark.appendChild(span);
      }
    }
  }

  if(canvasBg)canvasBg.value=processBackground;
  syncBackgroundTypeSelect(type);
  if(bgPatternColor)bgPatternColor.value=processPatternColor;
  if(bgDensity)bgDensity.value=String(processPatternDensity);
  if(gradientStart)gradientStart.value=processGradientStart;
  if(gradientEnd)gradientEnd.value=processGradientEnd;
  if(gradientAngle)gradientAngle.value=String(processGradientAngle);
  if(bgImageOpacity)bgImageOpacity.value=String(Math.round(processBackgroundImageOpacity*100));
  if(bgImageOpacityValue)bgImageOpacityValue.textContent=Math.round(processBackgroundImageOpacity*100)+'%';
  if(watermarkText)watermarkText.value=processWatermarkText;
  if(watermarkUseLogo)watermarkUseLogo.checked=processWatermarkUseLogo;
  if(watermarkOpacity)watermarkOpacity.value=String(Math.round(processWatermarkOpacity*100));
  if(watermarkOpacityValue)watermarkOpacityValue.textContent=Math.round(processWatermarkOpacity*100)+'%';
  if(gradientControls)gradientControls.classList.toggle('on',type==='gradient');
  if(imageBgControls)imageBgControls.classList.toggle('on',type==='image');
  if(watermarkControls)watermarkControls.classList.toggle('on',type==='watermark');
  if(logoSize)logoSize.value=String(processLogoWidth);
  if(logoHide)logoHide.checked=processLogoHidden;

  if(processLogoData){
    processLogo.src=processLogoData;
    processLogo.style.maxWidth=processLogoWidth+'px';
    processLogo.style.left=processLogoX+'px';
    processLogo.style.top=processLogoY+'px';
    processLogo.classList.toggle('on',!processLogoHidden);
  }else{
    processLogo.removeAttribute('src');
    processLogo.classList.remove('on');
  }
  return true;
}

const nodeGeomRevision=new Map();
function invalidateNodeGeom(id=null){
  if(id==null){
    nodeGeomCache.clear();nodeGeomRevision.clear();geomVersion++;
    return;
  }
  const key=String(id);
  nodeGeomRevision.set(key,(nodeGeomRevision.get(key)||0)+1);
  nodeGeomCache.delete(key);
}
function nodeGeom(id){
  const key=String(id),rev=nodeGeomRevision.get(key)||0;
  const cached=nodeGeomCache.get(key);
  if(cached&&cached.rev===rev)return cached;
  const el=nodes.get(key)?.el;
  if(!el)return null;
  const g={
    rev,
    left:el.offsetLeft,
    top:el.offsetTop,
    width:el.offsetWidth,
    height:el.offsetHeight
  };
  nodeGeomCache.set(key,g);
  return g;
}
function anchorCached(id,side){
  const g=nodeGeom(id);if(!g)return[0,0];
  if(side==='left')return[g.left,g.top+g.height/2];
  if(side==='right')return[g.left+g.width,g.top+g.height/2];
  if(side==='top')return[g.left+g.width/2,g.top];
  return[g.left+g.width/2,g.top+g.height];
}

function clone(v){return JSON.parse(JSON.stringify(v))}
function uid(){return 'proc-'+Date.now().toString(36)+'-'+Math.random().toString(36).slice(2,7)}
function msg(t){status.textContent=t;setTimeout(()=>{if(status.textContent===t)status.textContent=''},1800)}
function safeRun(label,fn){try{const r=fn();if(r&&typeof r.then==='function')return r.catch(e=>{reportRuntimeError(e,label);return null});return r}catch(e){reportRuntimeError(e,label);return null}}
function defBg(type){return {start:'#edf8f3',end:'#fff3f1',decision:'#fff8df',subprocess:'#f7f3ff',note:'#fffbe8',group:'#f8fafc',document:'#f3f8fc'}[type]||'#ffffff'}
function styleOf(d){
  const allowedNodeStyles=new Set(['standard','3d','raised','glass','flat']);
  const nodeStyle=allowedNodeStyles.has(d.nodeStyle)?d.nodeStyle:'standard';
  return{fontFamily:d.fontFamily||'Inter',fontSize:Number(d.fontSize||13),textColor:d.textColor||'#17202a',bgColor:d.bgColor||defBg(d.type),fontWeight:d.fontWeight||'700',fontStyle:d.fontStyle||'normal',textDecoration:d.textDecoration||'none',textAlign:d.textAlign||'center',borderColor:d.borderColor||'#637387',borderWidth:Number(d.borderWidth||2),nodeStyle}
}
function applyStyle(item){
  const s=styleOf(item.data);Object.assign(item.data,s);
  item.el.classList.remove('p48-style-3d','p48-style-raised','p48-style-glass','p48-style-flat');
  if(s.nodeStyle!=='standard')item.el.classList.add('p48-style-'+s.nodeStyle);
  item.el.style.fontFamily=s.fontFamily;item.label.style.fontFamily=s.fontFamily;item.label.style.fontSize=s.fontSize+'px';item.label.style.color=s.textColor;item.label.style.fontWeight=s.fontWeight;item.label.style.fontStyle=s.fontStyle;item.label.style.textDecoration=s.textDecoration;item.label.style.textAlign=s.textAlign;
  if(item.io){item.io.style.fontFamily=s.fontFamily;item.io.style.fontSize=Math.max(9,Math.round(s.fontSize*.72))+'px'}if(item.docOpen){item.docOpen.style.fontFamily=s.fontFamily;item.docOpen.style.fontSize=Math.max(9,Math.round(s.fontSize*.85))+'px'}
  let visualBg=s.bgColor;
  if(s.nodeStyle==='3d')visualBg=`linear-gradient(145deg,rgba(255,255,255,.78) 0%,rgba(255,255,255,.18) 42%,rgba(0,0,0,.14) 100%),${s.bgColor}`;
  else if(s.nodeStyle==='raised')visualBg=`linear-gradient(180deg,rgba(255,255,255,.72) 0%,rgba(255,255,255,.10) 55%,rgba(0,0,0,.05) 100%),${s.bgColor}`;
  else if(s.nodeStyle==='glass')visualBg=`linear-gradient(135deg,rgba(255,255,255,.88) 0%,rgba(255,255,255,.30) 48%,rgba(180,215,230,.32) 100%),${s.bgColor}`;
  item.el.style.background=visualBg;item.el.style.setProperty('--decision-bg',visualBg);
  if(item.data.type==='decision'){item.el.style.setProperty('--decision-border',s.borderColor);item.el.style.setProperty('--decision-border-width',s.borderWidth+'px')}else{item.el.style.borderColor=s.borderColor;item.el.style.borderWidth=s.borderWidth+'px'}
}
function safeDocumentUrl(value){
  const raw=String(value||'').trim();
  if(!raw)return '';
  try{
    const u=new URL(raw,window.location.href);
    if(u.protocol!=='http:'&&u.protocol!=='https:')return '';
    return u.href;
  }catch(e){return ''}
}
function closeDocumentInlineEditor(item){
  if(!item)return;
  item.el.classList.remove('p48-doc-editing');
  if(item.docInlineEditor)item.docInlineEditor.hidden=true;
  if(item.docOpen)item.docOpen.hidden=false;
}
function commitDocumentInlineUrl(item){
  if(!item||!item.docInlineInput)return false;
  const raw=String(item.docInlineInput.value||'').trim();
  const normalized=safeDocumentUrl(raw);
  if(raw&&!normalized){
    msg('Ange en giltig http- eller https-länk');
    item.docInlineInput.focus({preventScroll:true});
    return false;
  }
  const previous=String(item.data.documentUrl||'');
  if(previous!==raw){
    pushUndo();
    item.data.documentUrl=raw;
    persist();
  }
  closeDocumentInlineEditor(item);
  renderDocumentLink(item);
  selectedId=item.data.id;selectedIds=new Set([item.data.id]);
  refreshControls();updateSelectionUi();
  if(raw)msg('Dokumentlänk sparad');
  return true;
}
function openDocumentInlineEditor(item){
  if(!item||item.data.type!=='document'||!requireEdit())return;
  select(item.el);
  if(!item.docInlineEditor){
    const editor=document.createElement('div');editor.className='p48-doc-inline-editor';editor.hidden=true;
    const input=document.createElement('input');input.type='url';input.inputMode='url';input.autocomplete='off';input.className='p48-doc-inline-input';input.placeholder='https://…';input.setAttribute('aria-label','Dokumentlänk');
    const save=document.createElement('button');save.type='button';save.className='p48-doc-inline-save';save.textContent='Spara';
    editor.append(input,save);item.el.appendChild(editor);item.docInlineEditor=editor;item.docInlineInput=input;
    editor.addEventListener('pointerdown',e=>e.stopPropagation());editor.addEventListener('click',e=>e.stopPropagation());
    save.addEventListener('click',e=>{e.preventDefault();e.stopPropagation();commitDocumentInlineUrl(item)});
    input.addEventListener('keydown',e=>{
      if(e.key==='Enter'){e.preventDefault();commitDocumentInlineUrl(item)}
      else if(e.key==='Escape'){e.preventDefault();closeDocumentInlineEditor(item);renderDocumentLink(item);item.el.focus();}
    });
  }
  item.docInlineInput.value=item.data.documentUrl||'';
  item.el.classList.add('p48-doc-editing');
  item.docInlineEditor.hidden=false;
  if(item.docOpen)item.docOpen.hidden=true;
  requestAnimationFrame(()=>{item.docInlineInput.focus({preventScroll:true});item.docInlineInput.select();});
  msg('Klistra in dokumentlänken direkt i dokumentrutan');
}
function renderDocumentLink(item){
  if(!item||item.data.type!=='document')return;
  let btn=item.docOpen;
  if(!btn){
    btn=document.createElement('a');
    btn.className='p48-doc-open';
    btn.target='_blank';btn.rel='noopener noreferrer';
    btn.addEventListener('pointerdown',e=>{e.stopPropagation()});
    btn.addEventListener('click',e=>{
      e.stopPropagation();
      const url=safeDocumentUrl(item.data.documentUrl);
      if(!url){
        e.preventDefault();
        openDocumentInlineEditor(item);
      }
    });
    item.el.appendChild(btn);item.docOpen=btn;
  }
  const valid=safeDocumentUrl(item.data.documentUrl);
  if(valid)btn.href=valid;else btn.removeAttribute('href');
  btn.textContent=valid?'↗ Öppna dokument':'+ Lägg till dokumentlänk';
  btn.title=valid?valid:'Lägg till dokumentlänk direkt i rutan';
  btn.hidden=Boolean(item.docInlineEditor&&!item.docInlineEditor.hidden);
  const ts=styleOf(item.data);btn.style.fontFamily=ts.fontFamily;btn.style.fontSize=Math.max(9,Math.round(ts.fontSize*.85))+'px';
}

function state(){
  const meta=processes[currentId]||{};
  return MapliniStateCore.normalizeProcess({
    id:currentId,
    name:nameInput.value.trim()||'Namnlös process',
    nodes:[...nodes.values()].map(x=>clone(x.data)),
    links:clone(links),
    connectorPointSize,
    connectorPointColor,
    connectorPointsHidden,
    processBackground,
    processBackgroundType,
    processPatternColor,
    processPatternDensity,
    processGradientStart,
    processGradientEnd,
    processGradientAngle,
    processBackgroundImageData,
    processBackgroundImageOpacity,
    processWatermarkText,
    processWatermarkOpacity,
    processWatermarkUseLogo,
    processLogoData,
    processLogoHidden,
    processLogoWidth,
    processLogoX,
    processLogoY,
    localModifiedAt:Number(meta.localModifiedAt||0),
    cloudUpdatedAt:meta.cloudUpdatedAt||null
  },currentId);
}
const LOCAL_KEY='maplini_v050',LOCAL_BACKUP_KEY='maplini_v050_backup',LOCAL_CORRUPT_KEY='maplini_v050_corrupt',LOCAL_RECOVERY_KEY='maplini_recovery_v1';
let localSaveTimer=null,localSaveDirty=false,lastLocalPayload='',pendingRecoveryStore=null;
function localTimeLabel(ts=Date.now()){try{return new Intl.DateTimeFormat('sv-SE',{hour:'2-digit',minute:'2-digit'}).format(new Date(ts))}catch(e){return ''}}
function setSaveState(next,ts=Date.now()){if(!saveState)return;saveState.dataset.state=next;saveState.textContent=MapliniAutosaveCore.saveLabel(next,localTimeLabel(ts));}
function normalizedStore(){return MapliniStateCore.normalizeStore({schemaVersion:1,currentId,processes})}
function stageRecoverySnapshot(){
  if(!MapliniPrivacyCore.shouldPersistLocally({sharedView}))return true;
  try{const snapshot=MapliniAutosaveCore.makeRecoverySnapshot(normalizedStore(),Date.now());localStorage.setItem(LOCAL_RECOVERY_KEY,JSON.stringify(snapshot));setSaveState('saving');return true}catch(e){reportRuntimeError(e,'recovery-stage');return false}
}
function clearRecoveryIfSaved(payload){try{const snap=MapliniAutosaveCore.parseRecovery(localStorage.getItem(LOCAL_RECOVERY_KEY));if(!snap)return;if(JSON.stringify(MapliniStateCore.normalizeStore(snap.store))===payload)localStorage.removeItem(LOCAL_RECOVERY_KEY)}catch(ignore){}}
function saveLocal(immediate=false){
  if(!MapliniPrivacyCore.shouldPersistLocally({sharedView}))return true;
  localSaveDirty=true;
  const flush=()=>{
    if(!localSaveDirty)return true;
    localSaveDirty=false;
    if(localSaveTimer){clearTimeout(localSaveTimer);localSaveTimer=null;}
    try{
      const normalized=normalizedStore();
      const payload=JSON.stringify(normalized);
      if(payload!==lastLocalPayload){
        const previous=localStorage.getItem(LOCAL_KEY);
        if(previous&&previous!==payload)localStorage.setItem(LOCAL_BACKUP_KEY,previous);
        localStorage.setItem(LOCAL_KEY,payload);
        const verify=localStorage.getItem(LOCAL_KEY);
        if(verify!==payload)throw new Error('localStorage verification failed');
        lastLocalPayload=payload;clearRecoveryIfSaved(payload);setSaveState('saved');clearRuntimeError();
      }
      return true;
    }catch(e){
      localSaveDirty=true;
      setSaveState('error');reportRuntimeError(e,'local-save');
      try{sessionStorage.setItem('maplini_emergency_snapshot',JSON.stringify(MapliniReliabilityCore.makeEmergencySnapshot({schemaVersion:1,currentId,processes})))}catch(ignore){}
      return false;
    }
  };
  if(immediate)return flush();
  if(localSaveTimer)clearTimeout(localSaveTimer);
  localSaveTimer=setTimeout(flush,180);
  return true;
}
function loadLocal(){
  let primaryStore=null;
  try{const raw=localStorage.getItem(LOCAL_KEY);if(raw)primaryStore=MapliniStateCore.normalizeStore(JSON.parse(raw))}catch(ignore){}
  try{
    const recovery=MapliniAutosaveCore.parseRecovery(localStorage.getItem(LOCAL_RECOVERY_KEY));
    if(recovery){
      const normalizedRecovery=MapliniStateCore.normalizeStore(recovery.store);
      if(MapliniAutosaveCore.shouldOfferRecovery({store:normalizedRecovery},primaryStore))pendingRecoveryStore=normalizedRecovery;
      else localStorage.removeItem(LOCAL_RECOVERY_KEY);
    }
  }catch(ignore){}
  const candidates=[
    {key:LOCAL_KEY,raw:localStorage.getItem(LOCAL_KEY)},
    {key:LOCAL_BACKUP_KEY,raw:localStorage.getItem(LOCAL_BACKUP_KEY)},
    {key:'maplini_emergency_snapshot',raw:sessionStorage.getItem('maplini_emergency_snapshot')},
    {key:'processkartan_v048',raw:localStorage.getItem('processkartan_v048')},
    {key:'maplini_pre_delete_snapshot',raw:sessionStorage.getItem('maplini_pre_delete_snapshot')}
  ];
  for(const candidate of candidates){
    if(!candidate.raw)continue;
    try{
      const normalized=MapliniStateCore.normalizeStore(JSON.parse(candidate.raw));
      if(!Object.keys(normalized.processes).length)continue;
      processes=normalized.processes;
      currentId=normalized.currentId;
      resetHistory();
      if(candidate.key===LOCAL_KEY){
        lastLocalPayload=JSON.stringify(normalized);
      }else{
        lastLocalPayload='';
        const promoted=saveLocal(true);
        if(!promoted)console.warn('Recovered data loaded but could not be promoted to primary storage');
      }
      return true;
    }catch(e){
      if(candidate.key===LOCAL_KEY){
        try{localStorage.setItem(LOCAL_CORRUPT_KEY,candidate.raw)}catch(ignore){}
        console.error('Maplini local data invalid; trying backup',e);
      }
    }
  }
  return false;
}
let lastProcessListSignature='';
function renderProcesses(force=false){
  const sorted=Object.values(processes).sort((a,b)=>(a.name||'').localeCompare(b.name||'','sv'));
  const signature=MapliniPerformanceCore.signature([currentId,...sorted.map(p=>p.id+'\u0000'+(p.name||''))]);
  if(!force&&signature===lastProcessListSignature)return false;
  lastProcessListSignature=signature;
  processBox.innerHTML='';
  sorted.forEach(p=>{
    const row=document.createElement('div');row.className='p48-proc-row';
    const b=document.createElement('button');b.type='button';b.className='p48-proc'+(p.id===currentId?' active':'');
    b.textContent=p.name||'Namnlös process';b.title=p.name||'Namnlös process';
    b.addEventListener('click',()=>{if(p.id!==currentId){persist();openProcess(p.id)}});
    const del=document.createElement('button');del.type='button';del.className='p48-proc-delete';del.textContent='×';del.title='Radera process';
    del.addEventListener('click',e=>{e.stopPropagation();deleteProcess(p.id)});
    row.append(b,del);processBox.appendChild(row);
  });
  return true;
}
let lastProcessListName='';

let idlePersistTimer=null;
function persistAfterIdle(){
  if(idlePersistTimer)clearTimeout(idlePersistTimer);
  idlePersistTimer=setTimeout(()=>persist(false,false),120);
}

function persist(show=false,refreshList=false){
  const previous=processes[currentId]||null;
  const st=state();
  if(sharedView){
    // Public shared links are ephemeral: never copy their process payload into localStorage.
    processes[currentId]=st;
    scheduleHorizontalNavSync();
    return st;
  }
  if(MapliniSyncCore.contentChanged(previous,st))st.localModifiedAt=Date.now();
  processes[currentId]=st;
  if(MapliniSyncCore.contentChanged(previous,st))stageRecoverySnapshot();
  saveLocal(false);
  const currentName=st.name||'';
  if(refreshList||currentName!==lastProcessListName){
    lastProcessListName=currentName;
    renderProcesses();
  }
  if(show)msg('Sparad');
  scheduleHorizontalNavSync();
  return st;
}
let lastUndoAt=0,lastUndoSnapshot='',historyTransactionDepth=0,undoGestureSnapshot=null;
function resetHistory(){undo=[];redo=[];lastUndoSnapshot='';lastUndoAt=0;historyTransactionDepth=0;undoGestureSnapshot=null}
function recordUndoSnapshot(snapshot,force=false){
  const now=performance.now();
  snapshot=String(snapshot||'');if(!snapshot)return false;
  if(!force && now-lastUndoAt<220 && lastUndoSnapshot)return false;
  if(undo.length&&undo[undo.length-1]===snapshot)return false;
  undo.push(snapshot);lastUndoSnapshot=snapshot;lastUndoAt=now;
  if(undo.length>50)undo.shift();redo=[];return true;
}
function pushUndo(force=false){
  if(historyTransactionDepth>0)return false;
  return recordUndoSnapshot(JSON.stringify(state()),force);
}
function runAtomicUndoOperation(operation){
  if(typeof operation!=='function')return false;
  const before=JSON.stringify(state());historyTransactionDepth++;
  let result=false;
  try{result=operation()}
  finally{historyTransactionDepth=Math.max(0,historyTransactionDepth-1)}
  const after=JSON.stringify(state());
  if(before!==after)recordUndoSnapshot(before,true);
  return result;
}
function beginUndoGesture(){
  if(undoGestureSnapshot!=null)return false;
  undoGestureSnapshot=JSON.stringify(state());historyTransactionDepth++;return true;
}
function endUndoGesture(){
  if(undoGestureSnapshot==null)return false;
  const before=undoGestureSnapshot;undoGestureSnapshot=null;
  historyTransactionDepth=Math.max(0,historyTransactionDepth-1);
  if(before!==JSON.stringify(state()))return recordUndoSnapshot(before,true);
  return false;
}
function refreshEmptyState(){
  if(!emptyState)return;
  emptyState.hidden=sharedView||nodes.size>0;
}
function addFirstStep(type,objectRole=null){
  if(!requireEdit())return false;
  const x=Math.max(240,Math.min(canvasLogicalWidth*.32,620));
  const y=Math.max(180,Math.min(canvasLogicalHeight*.28,360));
  addNode(type,x,y,{objectRole});
  const item=selectedId?nodes.get(selectedId):null;
  if(item)requestAnimationFrame(()=>beginInlineEdit(item.el));
  return true;
}
function clearCanvas(){hideSnapGuides();for(const x of nodes.values())x.el.remove();nodes.clear();links=[];selectedId=null;selectedIds.clear();selectedLinkIndex=null;selectedLinkIndices.clear();linkLayer.innerHTML='';clearLinkHitLayer();linkDomByIndex.clear();finishTempArrow();setFormatEnabled(false);refreshControls();refreshLinkControls();updateSelectionUi();refreshEmptyState()}
function clearEntireCanvas(){
  if(!requireEdit())return false;
  if(nodes.size===0&&links.length===0){msg('Canvasen är redan tom');return false}
  if(!confirm('Är du säker på att du vill rensa hela canvasen? Alla rutor och kopplingar tas bort.'))return false;
  const changed=runAtomicUndoOperation(()=>{clearCanvas();persist();return true});
  if(changed)msg('Canvasen rensades · Ångra återställer innehållet');
  return changed;
}
function restore(s){
  let raw;
  try{raw=typeof s==='string'?JSON.parse(s):clone(s)}
  catch(e){reportRuntimeError(e,'restore-parse');return false}
  const d=MapliniStateCore.normalizeProcess(raw,raw?.id||currentId);
  if(!MapliniReliabilityCore.isUsableProcess(d)){reportRuntimeError(new Error('Invalid process payload'),'restore-validate');return false}
  clearCanvas();
  processScalePercent=100;
  if(processScaleSlider)processScaleSlider.value='100';
  if(processScaleValue)processScaleValue.textContent='100 %';
  currentId=d.id||currentId;
  nameInput.value=d.name||'Namnlös process';
  connectorPointSize=Number(d.connectorPointSize||8);
  connectorPointColor=d.connectorPointColor||'#1f6f55';
  connectorPointsHidden=Boolean(d.connectorPointsHidden);
  processBackground=d.processBackground||'#ffffff';
  processBackgroundType=d.processBackgroundType||'solid';
  processPatternColor=d.processPatternColor||'#d7e1e8';
  processPatternDensity=Number(d.processPatternDensity||20);
  processGradientStart=d.processGradientStart||'#ffffff';
  processGradientEnd=d.processGradientEnd||'#e7f1ff';
  processGradientAngle=Number(d.processGradientAngle||45);
  processBackgroundImageData=d.processBackgroundImageData||'';
  processBackgroundImageOpacity=Math.max(.05,Math.min(1,Number(d.processBackgroundImageOpacity||.25)));
  processWatermarkText=d.processWatermarkText||'UTKAST';
  processWatermarkOpacity=Math.max(.05,Math.min(.4,Number(d.processWatermarkOpacity||.15)));
  processWatermarkUseLogo=Boolean(d.processWatermarkUseLogo);
  processLogoData=d.processLogoData||'';
  processLogoHidden=Boolean(d.processLogoHidden);
  processLogoWidth=Number(d.processLogoWidth||180);
  processLogoX=Number.isFinite(Number(d.processLogoX))?Number(d.processLogoX):28;
  processLogoY=Number.isFinite(Number(d.processLogoY))?Number(d.processLogoY):28;
  applyConnectorPointSettings();
  applyProcessStyle(true);
  (d.nodes||[]).forEach(makeNode);
  links=MapliniConnectorCore.normalizeLinks(d.links||[]);
  seq=Math.max(0,...[...nodes.keys()].map(id=>parseInt(String(id).replace(/\D/g,''),10)||0));
  requestFullLinkRender(true);refreshEmptyState();clearRuntimeError();
  return true;
}
function openProcess(id){
  if(!processes[id])return;
  const previousId=currentId,previous=processes[previousId]?clone(processes[previousId]):null;
  currentId=id;resetHistory();
  processes[id]=MapliniStateCore.normalizeProcess(processes[id],id);
  if(!restore(processes[id])){
    if(previousId&&previous){currentId=previousId;processes[previousId]=previous;restore(previous)}
    msg('Processen kunde inte öppnas');return;
  }
  saveLocal(false);renderProcesses();refreshControls();refreshLinkControls();updateSelectionUi();msg('Process öppnad');scroll.scrollTop=0;scroll.scrollLeft=0;requestAnimationFrame(alignEditorTop)
}
function setNewProcessDialog(open){
  if(!newProcessDialog||!newProcessBackdrop)return false;
  const show=Boolean(open);
  newProcessDialog.hidden=!show;newProcessBackdrop.hidden=!show;
  if(show){
    persist();
    if(newProcessError){newProcessError.hidden=true;newProcessError.textContent=''}
    if(newProcessName){newProcessName.value='Ny process';requestAnimationFrame(()=>{newProcessName.focus();newProcessName.select()})}
  }else if(newProcessName){newProcessName.blur()}
  return true;
}
function createNewProcessFromDialog(){
  if(!requireEdit())return false;
  const n=String(newProcessName?.value||'').trim();
  if(!n){
    if(newProcessError){newProcessError.textContent='Skriv ett namn på processen.';newProcessError.hidden=false}
    if(newProcessName)newProcessName.focus();
    return false;
  }
  currentId=uid();processes[currentId]=MapliniWorkflowCore.emptyProcess(currentId,n);
  processes[currentId].localModifiedAt=Date.now();resetHistory();restore(processes[currentId]);
  saveLocal(true);renderProcesses();scroll.scrollLeft=0;scroll.scrollTop=0;refreshEmptyState();
  setNewProcessDialog(false);msg('Ny process skapad · lägg till första steget på canvasen');
  return true;
}
function newProcess(){if(!requireEdit())return;setNewProcessDialog(true)}
async function deleteProcess(id){
  if(!requireEdit())return;
  const proc=processes[id];if(!proc)return;
  const label=proc.name||'Namnlös process';
  if(!confirm('Radera processen "'+label+'"? Detta går inte att ångra.'))return;

  persist(false,false);
  const beforeOk=saveLocal(true);
  if(!beforeOk){msg('Radering avbruten · lokal säkerhetskopia kunde inte sparas');return}

  const snapshot=MapliniReliabilityCore.makeEmergencySnapshot({schemaVersion:1,currentId,processes});
  try{sessionStorage.setItem('maplini_pre_delete_snapshot',JSON.stringify(snapshot))}
  catch(e){reportRuntimeError(e,'pre-delete-snapshot');msg('Radering avbruten · säkerhetskopia kunde inte skapas');return}

  const next=MapliniFlowCore.afterProcessDelete(processes,currentId,id);
  processes=next.processes;currentId=next.currentId;
  cloudLoadedProcessIds.delete(id);cloudLoadedProcessScopes.delete(id);

  if(!processes[currentId]){
    currentId=uid();
    processes[currentId]=MapliniWorkflowCore.emptyProcess(currentId,'Ny process');
    processes[currentId].localModifiedAt=Date.now();
  }
  resetHistory();restore(processes[currentId]);

  const localOk=saveLocal(true);
  if(!localOk){
    const restored=MapliniStateCore.normalizeStore(snapshot);
    processes=restored.processes;currentId=restored.currentId;
    restore(processes[currentId]);saveLocal(true);renderProcesses(true);
    msg('Radering misslyckades · tidigare läge återställt');return;
  }

  renderProcesses(true);refreshControls();refreshLinkControls();updateSelectionUi();
  const cloudOk=await deleteCloud(id);
  if(cloudOk){
    try{sessionStorage.removeItem('maplini_pre_delete_snapshot')}catch(ignore){}
    msg('Process raderad');
  }else{
    msg('Process raderad lokalt – molnradering misslyckades');
  }
}
function nodeText(t){return{start:'Start',object:'Nytt objekt',process:'Ny aktivitet',decision:'Beslut?',end:'Slut',subprocess:'Ny delprocess',group:'Ny grupp / område',note:'Anteckning',document:'Dokument'}[t]||'Nytt steg'}
function place(el,x,y){const p=MapliniCanvasCore.place(x,y,el.offsetWidth,el.offsetHeight);el.style.left=p.x+'px';el.style.top=p.y+'px'}
function sync(el){const x=nodes.get(el.dataset.id);if(x){x.data.x=parseFloat(el.style.left)||0;x.data.y=parseFloat(el.style.top)||0}}
function center(el){return[(parseFloat(el.style.left)||0)+el.offsetWidth/2,(parseFloat(el.style.top)||0)+el.offsetHeight/2]}
function anchor(el,side){
  const x=el.offsetLeft,y=el.offsetTop,w=el.offsetWidth,h=el.offsetHeight;
  if(side==='left')return[x,y+h/2];
  if(side==='right')return[x+w,y+h/2];
  if(side==='top')return[x+w/2,y];
  return[x+w/2,y+h];
}
const SNAP_GRID=10,SNAP_TOLERANCE=8;
function hideSnapGuides(){if(snapGuideX)snapGuideX.hidden=true;if(snapGuideY)snapGuideY.hidden=true}
function showSnapGuides(result){
  if(snapGuideX){
    snapGuideX.hidden=result.snapY==null;
    if(result.snapY!=null)snapGuideX.style.top=result.snapY+'px';
  }
  if(snapGuideY){
    snapGuideY.hidden=result.snapX==null;
    if(result.snapX!=null)snapGuideY.style.left=result.snapX+'px';
  }
}
function magneticSnap(start,proposedX,proposedY,excludeIds){
  const w=start.width||180,h=start.height||70;
  const movingX=[proposedX,proposedX+w/2,proposedX+w];
  const movingY=[proposedY,proposedY+h/2,proposedY+h];
  let bestX=null,bestY=null;
  for(const item of nodes.values()){
    if(excludeIds.has(item.data.id))continue;
    const ox=parseFloat(item.el.style.left)||0,oy=parseFloat(item.el.style.top)||0,ow=item.el.offsetWidth,oh=item.el.offsetHeight;
    const targetsX=[ox,ox+ow/2,ox+ow],targetsY=[oy,oy+oh/2,oy+oh];
    /* Center-to-center alignment is the strongest snap because it produces a truly straight
       connector between differently sized nodes. Give it a slightly larger capture range. */
    const centerDx=targetsX[1]-movingX[1],centerDy=targetsY[1]-movingY[1];
    if(Math.abs(centerDx)<=14&&(!bestX||-1<bestX.score))bestX={diff:centerDx,abs:Math.abs(centerDx),score:-1,line:targetsX[1],centerPair:true};
    if(Math.abs(centerDy)<=14&&(!bestY||-1<bestY.score))bestY={diff:centerDy,abs:Math.abs(centerDy),score:-1,line:targetsY[1],centerPair:true};
    for(let mi=0;mi<movingX.length;mi++)for(let ti=0;ti<targetsX.length;ti++){
      const tx=targetsX[ti],diff=tx-movingX[mi],abs=Math.abs(diff);
      const centerPair=mi===1&&ti===1,score=abs-(centerPair?4:0);
      if(abs<=SNAP_TOLERANCE&&(!bestX||score<bestX.score))bestX={diff,abs,score,line:tx,centerPair};
    }
    for(let mi=0;mi<movingY.length;mi++)for(let ti=0;ti<targetsY.length;ti++){
      const ty=targetsY[ti],diff=ty-movingY[mi],abs=Math.abs(diff);
      const centerPair=mi===1&&ti===1,score=abs-(centerPair?4:0);
      if(abs<=SNAP_TOLERANCE&&(!bestY||score<bestY.score))bestY={diff,abs,score,line:ty,centerPair};
    }
  }
  let x=proposedX+(bestX?bestX.diff:0),y=proposedY+(bestY?bestY.diff:0);
  /* If no nearby node alignment exists, use the invisible 10px base grid. */
  if(!bestX)x=Math.round(x/SNAP_GRID)*SNAP_GRID;
  if(!bestY)y=Math.round(y/SNAP_GRID)*SNAP_GRID;
  return{x,y,snapX:bestX?bestX.line:null,snapY:bestY?bestY.line:null};
}
function polishAutomaticConnectedLinks(movedIds,{forceAuto=false}={}){
  const moved=new Set((movedIds||[]).map(String));
  let changed=0;
  for(let i=0;i<links.length;i++){
    const l=links[i];if(!Array.isArray(l)||(!moved.has(String(l[0]))&&!moved.has(String(l[1]))))continue;
    const A=nodes.get(String(l[0]))?.el,B=nodes.get(String(l[1]))?.el;if(!A||!B)continue;
    const st=linkStyle(l);
    /* Respect deliberate manual connector work. A free route or fixed anchor is user-owned
       unless Smart Layout explicitly asks us to normalize the whole selection. */
    if(!forceAuto&&(st.routing==='free'||st.anchorMode!=='auto'))continue;
    const [ax,ay]=center(A),[bx,by]=center(B);
    const alignedH=Math.abs(ay-by)<=1,alignedV=Math.abs(ax-bx)<=1;
    const routing=(alignedH||alignedV)?'straight':'orthogonal';
    setLinkStyle(i,{routing,anchorMode:'auto',viaX:null,viaY:null,freeDx:0,freeDy:0});
    dirtyLinks.add(i);changed++;
  }
  return changed;
}
function straightenAlignedConnectedLinks(movedIds){
  return polishAutomaticConnectedLinks(movedIds);
}
function targetSide(a,b){const[ax,ay]=center(a),[bx,by]=center(b),dx=bx-ax,dy=by-ay;if(Math.abs(dx)>=Math.abs(dy))return dx>=0?'left':'right';return dy>=0?'top':'bottom'}
function linkSides(link,A,B){const st=linkStyle(link),[ax,ay]=center(A),[bx,by]=center(B);if(st.anchorMode==='auto'){const sides=MapliniConnectorCore.autoSides(bx-ax,by-ay);return{source:sides[0],target:sides[1]}}return{source:link[2]||'right',target:targetSide(A,B)}}
function linkGeometry(link,A,B){const st=linkStyle(link),sides=linkSides(link,A,B),a=anchor(A,sides.source),b=anchor(B,sides.target),points=MapliniConnectorCore.routePoints(a[0],a[1],b[0],b[1],sides.source,sides.target,st);return{st,sides,points,d:MapliniConnectorCore.pathData(points)}}
function lastSegmentAngle(points){if(!points||points.length<2)return 0;const a=points[points.length-2],b=points[points.length-1];return Math.atan2(b[1]-a[1],b[0]-a[0])}


function refreshNodeQuickToolbar(){
  if(!nodeQuick)return;
  const ids=selectedIds.size?[...selectedIds]:(selectedId?[selectedId]:[]);
  const items=ids.map(id=>nodes.get(id)).filter(Boolean);
  const visible=canEdit()&&selectedLinkIndex==null&&items.length>0;
  nodeQuick.classList.toggle('on',visible);
  if(!visible){if(nodeQuickArrange)nodeQuickArrange.open=false;return}
  const multi=items.length>1;nodeQuick.dataset.mode=multi?'multi':'single';
  let left=Infinity,top=Infinity,right=-Infinity;
  for(const item of items){const x=parseFloat(item.el.style.left)||0,y=parseFloat(item.el.style.top)||0,w=item.el.offsetWidth||180;left=Math.min(left,x);top=Math.min(top,y);right=Math.max(right,x+w)}
  const maxToolbarX=Math.max(120,canvasLogicalWidth-80);
  const x=Math.max(80,Math.min(maxToolbarX,(left+right)/2));
  const y=Math.max(56,top);nodeQuick.style.left=x+'px';nodeQuick.style.top=y+'px';
  if(nodeQuickColor){const shared=sharedStyleValue(items,'bgColor');nodeQuickColor.value=shared||styleOf(items[0].data).bgColor||'#ffffff'}
  if(nodeQuickFlow){
    const source=!multi&&isNextStepSource(items[0]);
    nodeQuickFlow.hidden=!source;
    nodeQuickFlow.textContent=source?workflowCue(items[0]):'';
    nodeQuickFlow.title=source?'Rekommenderad ordning i processflödet':'';
  }
  if(nodeQuickNext){
    const source=!multi&&isNextStepSource(items[0]);
    nodeQuickNext.disabled=!source;nodeQuickNext.hidden=!source;
    if(source){nodeQuickNext.textContent=preferredNextLabel(items[0]);nodeQuickNext.title='Lägg till rekommenderat nästa steg direkt';}
  }
  if(nodeQuickNextMore){
    const source=!multi&&isNextStepSource(items[0]);
    nodeQuickNextMore.disabled=!source;nodeQuickNextMore.hidden=!source;
  }
}
function focusFormattingPanel(){
  if(isMobileLayout())setMobileTools(true);
  requestAnimationFrame(()=>{try{formatPanel&&formatPanel.scrollIntoView({block:'start',behavior:'smooth'})}catch(_){if(sidePanel&&formatPanel)sidePanel.scrollTop=Math.max(0,formatPanel.offsetTop-12)};if(formatPanel){formatPanel.classList.add('p48-focus-flash');setTimeout(()=>formatPanel.classList.remove('p48-focus-flash'),700)}});
}
function refreshMobileBar(){
  if(!mobileBar)return;
  const nodeCount=selectedIds.size||(selectedId?1:0);
  const selectedMode=isMobileLayout()&&canEdit()&&selectedLinkIndex==null&&nodeCount>0;
  mobileBar.dataset.mode=selectedMode?'selected':'normal';
  if(mobileNext){
    const item=selectedId&&nodeCount===1?nodes.get(selectedId):null;
    mobileNext.hidden=!(item&&isNextStepSource(item));
    if(item&&isNextStepSource(item))mobileNext.textContent=preferredNextLabel(item);
  }
  if(mobileUndo)mobileUndo.disabled=!canEdit()||undo.length===0;
  if(mobileRedo)mobileRedo.disabled=!canEdit()||redo.length===0;
}
function updateSelectionUi(){
  for(const item of nodes.values()){
    item.el.classList.toggle('multi-selected', selectedIds.has(item.data.id));
    if(selectedId===item.data.id)item.el.classList.add('selected');
    else item.el.classList.remove('selected');
    const nextVisible=selectedId===item.data.id&&selectedIds.size===1&&canEdit()&&isNextStepSource(item);
    item.el.classList.toggle('p48-next-visible',nextVisible);
    if(!nextVisible&&item.nextMenu&&!item.nextMenu.hidden){item.nextMenu.hidden=true;if(item.nextBtn)item.nextBtn.setAttribute('aria-expanded','false')}
  }
  deleteSelectionBtn.disabled=selectedIds.size===0&&selectedLinkIndices.size===0;
  if(duplicateSelectionBtn)duplicateSelectionBtn.disabled=!canEdit()||selectedIds.size===0;

  smartLayoutChoices.forEach(btn=>{btn.disabled=!canEdit()||(btn.dataset.layoutScope==='selected'&&selectedIds.size<2)});
  if(autoCleanBtn)autoCleanBtn.disabled=!canEdit()||nodes.size<2;
  if(smartLayoutHint)smartLayoutHint.textContent=selectedIds.size>=2?`${selectedIds.size} markerade · välj hela processen eller markeringen.`:'Markera minst två rutor för att snygga till bara en del.';
  selectToolBtn.classList.toggle('primary',selectionMode);
  selectToolBtn.setAttribute('aria-pressed',selectionMode?'true':'false');
  selectToolBtn.textContent=selectionMode?'Avsluta markering':'Markera område';
  if(formatHint&&!selectedId&&selectedLinkIndex==null&&selectedIds.size<2){
    formatHint.textContent=MapliniUiCore.selectionHint({
      selectedLinkIndex,
      selectedNodeCount:selectedIds.size,
      selectedLinkCount:selectedLinkIndices.size,
      nodeEnabled:false
    });
  }
  refreshNodeQuickToolbar();
  refreshMobileBar();
}
function clearSelection(){
  const hadLinks=(selectedLinkIndex!=null||selectedLinkIndices.size>0);
  const next=MapliniSelectionCore.clear();
  selectedId=next.selectedId;selectedIds=new Set(next.selectedIds);
  selectedLinkIndex=next.selectedLinkIndex;selectedLinkIndices=new Set(next.selectedLinkIndices);
  refreshControls();refreshLinkControls();updateSelectionUi();
  if(hadLinks)requestFullLinkRender(true);
}
function selectMany(ids){
  selectedIds=new Set(ids);
  selectedId=selectedIds.size===1?[...selectedIds][0]:null;
  refreshControls();updateSelectionUi();
}
function copySelectedNodes({announce=true}={}){
  const ids=selectedIds.size?new Set(selectedIds):(selectedId?new Set([selectedId]):new Set());
  if(!ids.size){if(announce)msg('Markera minst en ruta först');return false}
  editingClipboard=MapliniEditingCore.makeClipboard([...nodes.values()].map(x=>x.data),links,[...ids]);
  clipboardPasteOffset=28;
  if(!MapliniEditingCore.hasNodes(editingClipboard)){if(announce)msg('Inget att kopiera');return false}
  const text=MapliniEditingCore.serialize(editingClipboard);
  if(text&&navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(text).catch(()=>{});}
  if(announce)msg(ids.size===1?'Ruta kopierad':`${ids.size} rutor kopierade`);
  return true;
}
function pasteEditingClipboard({announce=true}={}){
  if(!requireEdit())return false;
  if(!MapliniEditingCore.hasNodes(editingClipboard)){if(announce)msg('Kopiera en ruta först');return false}
  pushUndo();
  const result=MapliniEditingCore.instantiate(editingClipboard,()=>{seq++;return 'n'+seq},clipboardPasteOffset);
  if(!result.nodes.length)return false;
  for(const d of result.nodes)makeNode(d);
  links=MapliniConnectorCore.normalizeLinks(links.concat(result.links));
  const newIds=result.nodes.map(n=>n.id);
  selectedIds=new Set(newIds);selectedId=newIds.length===1?newIds[0]:null;
  selectedLinkIndex=null;selectedLinkIndices.clear();
  clipboardPasteOffset=Math.min(196,clipboardPasteOffset+28);
  requestFullLinkRender(true);persist();refreshControls();refreshLinkControls();updateSelectionUi();
  if(announce)msg(newIds.length===1?'Ruta inklistrad':`${newIds.length} rutor inklistrade`);
  return true;
}
function duplicateSelectedNodes(){
  if(!requireEdit())return false;
  if(!copySelectedNodes({announce:false}))return false;
  const ok=pasteEditingClipboard({announce:false});
  if(ok)msg(selectedIds.size===1?'Ruta duplicerad':`${selectedIds.size} rutor duplicerade`);
  return ok;
}

function deleteSelectedMany(){
  if(!requireEdit())return;
  if(!selectedIds.size&&!selectedLinkIndices.size)return;
  pushUndo();
  const doomed=new Set(selectedIds);
  for(const id of doomed){
    const item=nodes.get(id);
    if(item){item.el.remove();nodes.delete(id);}
  }
  links=MapliniConnectorCore.removeSelected(links,doomed,selectedLinkIndices);
  const cleared=MapliniSelectionCore.clear();
  selectedId=cleared.selectedId;selectedIds=new Set(cleared.selectedIds);
  selectedLinkIndex=cleared.selectedLinkIndex;selectedLinkIndices=new Set(cleared.selectedLinkIndices);
  requestFullLinkRender(true);persist();refreshControls();refreshLinkControls();updateSelectionUi();msg('Markerat område borttaget');
}
function rectsIntersect(a,b){return MapliniCanvasCore.rectsIntersect(a,b);}
function linksInSelectionRect(selRect){
  const hits=[];
  for(const [index,entry] of linkDomByIndex.entries()){
    const path=entry&&entry.visible;
    if(!path||typeof path.getBBox!=='function')continue;
    try{
      const b=path.getBBox();
      const lr={left:b.x,top:b.y,right:b.x+b.width,bottom:b.y+b.height};
      if(rectsIntersect(selRect,lr))hits.push(index);
    }catch(_){}
  }
  return hits;
}
function finishTempArrow(){
  temp.hidden=true;
  temp.setAttribute('d','');
}

function select(el){
  const hadLinks=(selectedLinkIndex!=null||selectedLinkIndices.size>0);
  selectedLinkIndex=null;selectedLinkIndices.clear();refreshLinkControls();
  selectedIds.clear();selectedId=el.dataset.id;selectedIds.add(selectedId);
  refreshControls();updateSelectionUi();
  if(hadLinks)requestFullLinkRender(true);
}
function toggleNodeSelection(el){
  if(!el||!el.dataset.id)return;
  const hadLinks=(selectedLinkIndex!=null||selectedLinkIndices.size>0);
  selectedLinkIndex=null;selectedLinkIndices.clear();refreshLinkControls();
  const id=el.dataset.id;
  if(selectedIds.has(id)){
    selectedIds.delete(id);
  }else{
    selectedIds.add(id);
  }
  selectedId=selectedIds.size===1?[...selectedIds][0]:null;
  refreshControls();updateSelectionUi();
  if(hadLinks)requestFullLinkRender(true);
}

function ensureIO(item){
  if(!Array.isArray(item.data.inputs))item.data.inputs=[];
  if(!Array.isArray(item.data.outputs))item.data.outputs=[];
}
function renderNodeIO(item){
  if(!item.io){const io=document.createElement('div');io.className='p48-node-io';item.el.appendChild(io);item.io=io;}
  ensureIO(item);item.io.innerHTML='';
  if(item.data.inputs.length){const s=document.createElement('span');s.textContent='In: '+item.data.inputs.join(', ');item.io.appendChild(s);}
  if(item.data.outputs.length){const s=document.createElement('span');s.textContent='Out: '+item.data.outputs.join(', ');item.io.appendChild(s);}
  item.io.style.display=(item.data.inputs.length||item.data.outputs.length)?'grid':'none';
  const ts=styleOf(item.data);item.io.style.fontFamily=ts.fontFamily;item.io.style.fontSize=Math.max(9,Math.round(ts.fontSize*.72))+'px';
}
function renderIOEditor(item){
  inputsBox.innerHTML='';outputsBox.innerHTML='';ensureIO(item);
  const row=(value,index,kind)=>{
    const r=document.createElement('div');r.className='p48-io-row';
    const inp=document.createElement('input');inp.value=value;inp.placeholder=kind==='inputs'?'Input':'Output';
    inp.addEventListener('change',()=>{if(!requireEdit())return;pushUndo();item.data[kind][index]=inp.value.trim();item.data[kind]=item.data[kind].filter(Boolean);renderNodeIO(item);drawLinks();persist();refreshControls();});
    const del=document.createElement('button');del.type='button';del.textContent='×';
    del.addEventListener('click',()=>{if(!requireEdit())return;pushUndo();item.data[kind].splice(index,1);renderNodeIO(item);drawLinks();persist();refreshControls();});
    r.append(inp,del);return r;
  };
  item.data.inputs.forEach((v,i)=>inputsBox.appendChild(row(v,i,'inputs')));
  item.data.outputs.forEach((v,i)=>outputsBox.appendChild(row(v,i,'outputs')));
}

function ensureProcessInfo(item){
  if(!item)return MapliniProcessInfoCore.normalize({});
  item.data.processInfo=MapliniProcessInfoCore.normalize(item.data.processInfo);
  return item.data.processInfo;
}
function processInfoEligible(item){
  return Boolean(item&&['process','subprocess','decision'].includes(String(item.data?.type||'')));
}
function processInfoSuggestions(key){
  const values=[];
  for(const candidate of nodes.values()){
    if(!processInfoEligible(candidate))continue;
    const info=ensureProcessInfo(candidate),value=String(info[key]||'').trim();
    if(value&&!values.some(v=>v.toLocaleLowerCase('sv-SE')===value.toLocaleLowerCase('sv-SE')))values.push(value);
  }
  return values.sort((a,b)=>a.localeCompare(b,'sv-SE')).slice(0,40);
}
function renderSuggestionList(el,values){
  if(!el)return;el.innerHTML='';
  for(const value of values){const option=document.createElement('option');option.value=value;el.appendChild(option);}
}
function renderProcessInfoEditor(item){
  const eligible=processInfoEligible(item);
  if(processInfoPanel)processInfoPanel.hidden=!eligible;
  if(!eligible)return;
  const info=ensureProcessInfo(item);
  for(const [key,el] of Object.entries(processInfoFields))if(el&&document.activeElement!==el)el.value=info[key]||'';
  renderSuggestionList(roleSuggestions,processInfoSuggestions('responsibleRole'));
  renderSuggestionList(systemSuggestions,processInfoSuggestions('system'));
  const c=MapliniProcessInfoCore.completion(info);
  if(processInfoProgress){
    processInfoProgress.textContent=`${c.filled} av ${c.total}`;
    processInfoProgress.title=c.filled===c.total?'Steget är väl beskrivet':'Frivilligt – fyll bara i det som är relevant';
  }
  if(processInfoMoreCount){
    const advanced=['instruction','risk','control','kpi'].filter(k=>Boolean(info[k])).length;
    processInfoMoreCount.textContent=advanced?`· ${advanced}/4 ifyllda`:'';
  }
}
function saveProcessInfoField(key,value){
  if(!requireEdit())return false;
  const item=selectedId?nodes.get(selectedId):null;
  if(!processInfoEligible(item)||!Object.prototype.hasOwnProperty.call(processInfoFields,key))return false;
  const before=JSON.stringify(ensureProcessInfo(item));
  const next=MapliniProcessInfoCore.normalize(Object.assign({},item.data.processInfo,{[key]:String(value||'')}));
  if(before===JSON.stringify(next))return false;
  pushUndo(true);item.data.processInfo=next;persist();renderProcessInfoEditor(item);
  msg('Processinformation sparad');return true;
}
function selectedNodeItems(){
  const ids=selectedIds.size?[...selectedIds]:(selectedId?[selectedId]:[]);
  return ids.map(id=>nodes.get(id)).filter(Boolean);
}
function sharedStyleValue(items,key){
  if(!items.length)return null;
  const first=styleOf(items[0].data)[key];
  return items.every(item=>styleOf(item.data)[key]===first)?first:null;
}
function syncFontSelect(value){
  if(!font)return;
  const wanted=String(value||'Inter');
  for(const option of [...font.querySelectorAll('option[data-legacy-font="true"]')])option.remove();
  const exists=[...font.options].some(option=>option.value===wanted);
  if(!exists){
    const option=document.createElement('option');
    option.value=wanted;option.textContent=`Tidigare typsnitt: ${wanted}`;option.dataset.legacyFont='true';
    font.appendChild(option);
  }
  font.value=wanted;
}
const standardNodeStyles=new Set(['standard','raised','flat']);
const legacyNodeStyleLabels={ '3d':'3D', glass:'Glas' };
function syncNodeStyleSelect(value){
  if(!nodeStyleSelect)return;
  const wanted=String(value||'standard');
  for(const option of [...nodeStyleSelect.querySelectorAll('option[data-legacy-node-style="true"]')])option.remove();
  if(!standardNodeStyles.has(wanted)){
    const option=document.createElement('option');
    option.value=wanted;
    option.textContent=`Tidigare rutstil: ${legacyNodeStyleLabels[wanted]||wanted}`;
    option.dataset.legacyNodeStyle='true';
    nodeStyleSelect.appendChild(option);
  }
  nodeStyleSelect.value=wanted;
}
function setFormatEnabled(enabled){
  const linkMode=selectedLinkIndex!=null;
  const multiNodeMode=!linkMode&&selectedIds.size>1;
  const editable=canEdit();
  const context=linkMode?'link':(multiNodeMode?'multi':(enabled?'node':'none'));
  if(formatPanel)formatPanel.dataset.context=context;
  if(deleteNodeBtn)deleteNodeBtn.hidden=!(context==='node'&&selectedIds.size===1&&selectedId!=null);
  if(formatTitle){
    formatTitle.textContent=context==='link'?'Pil':(context==='multi'?'Flera rutor':(context==='node'?'Ruta':'Formatering'));
  }
  if(formatHint){
    if(context==='link')formatHint.textContent='Ändra text, utseende och beteende för den markerade pilen.';
    else if(context==='multi')formatHint.textContent=`${selectedIds.size} rutor markerade · ändringar gäller alla markerade.`;
    else if(context==='node'){
      const item=selectedId?nodes.get(selectedId):null;
      if(item?.data?.type==='object'){
        const role=item.data.objectRole==='input'?'Objekt in · det som triggar eller behövs före en aktivitet.':(item.data.objectRole==='output'?'Objekt ut · resultatet som aktiviteten producerar.':'Objekt · kan vara både resultat från ett steg och input till nästa.');
        formatHint.textContent=role+' Ändra text och utseende här.';
      }else if(processInfoEligible(item))formatHint.textContent='Beskriv vad som händer, vem som ansvarar och vilket system som används. Utseendet ligger separat.';
      else formatHint.textContent='Ändra text och utseende för den markerade rutan.';
    }
    else formatHint.textContent='Markera en ruta eller pil för att visa relevanta inställningar.';
  }
  controls.querySelectorAll('select,input,textarea,button').forEach(el=>{
    const commonForLink=(el===linkColor||el===linkWidth||el===linkEnd||el===linkDash||el===linkRouting||el===linkAnchorMode||el===linkLabel||el===insertLinkStepBtn||el===deleteLinkBtn);
    if(linkMode)el.disabled=!editable||!commonForLink;
    else el.disabled=!editable||!enabled;
  });
  root.querySelectorAll('.p48-step-io input,.p48-step-io button').forEach(el=>{el.disabled=!editable||!enabled||multiNodeMode;});
  controls.style.opacity='1';
  linkFormat.style.opacity=linkMode?'1':'';
  const stepIO=root.querySelector('.p48-step-io');
  if(stepIO){stepIO.classList.toggle('on',enabled&&!multiNodeMode);stepIO.style.opacity='1';}
}

function refreshControls(){
  const items=selectedNodeItems();
  const item=selectedId?nodes.get(selectedId):null;
  if(!items.length){
    setFormatEnabled(false);inputsBox.innerHTML='';outputsBox.innerHTML='';if(processInfoPanel)processInfoPanel.hidden=true;
    if(documentLinkEditor)documentLinkEditor.hidden=true;
    if(documentUrlInput)documentUrlInput.value='';
    if(documentOpenEditor){documentOpenEditor.hidden=true;documentOpenEditor.removeAttribute('href');}
    if(selectedLinkIndex!=null)refreshLinkControls();return
  }
  setFormatEnabled(true);
  const first=items[0],s=styleOf(first.data),multi=items.length>1;
  if(multi&&formatHint)formatHint.textContent=`${items.length} rutor markerade · ändringar gäller alla. Blandade värden visas från den första rutan tills du väljer ett nytt värde.`;
  syncFontSelect(sharedStyleValue(items,'fontFamily')||s.fontFamily);
  size.value=sharedStyleValue(items,'fontSize')??s.fontSize;
  textColor.value=sharedStyleValue(items,'textColor')||s.textColor;
  bgColor.value=sharedStyleValue(items,'bgColor')||s.bgColor;
  borderColor.value=sharedStyleValue(items,'borderColor')||s.borderColor;
  borderWidth.value=String(sharedStyleValue(items,'borderWidth')??s.borderWidth);
  syncNodeStyleSelect(sharedStyleValue(items,'nodeStyle')||s.nodeStyle);
  bold.classList.toggle('active',sharedStyleValue(items,'fontWeight')==='700');
  italic.classList.toggle('active',sharedStyleValue(items,'fontStyle')==='italic');
  under.classList.toggle('active',sharedStyleValue(items,'textDecoration')==='underline');
  root.querySelectorAll('[data-text-align]').forEach(b=>b.classList.toggle('active',b.dataset.textAlign===sharedStyleValue(items,'textAlign')));
  if(documentLinkEditor)documentLinkEditor.hidden=multi||!item||item.data.type!=='document';
  if(documentUrlInput)documentUrlInput.value=(!multi&&item&&item.data.type==='document')?(item.data.documentUrl||''):'';
  if(documentOpenEditor){const u=(!multi&&item&&item.data.type==='document')?safeDocumentUrl(item.data.documentUrl):'';documentOpenEditor.hidden=!u;if(u)documentOpenEditor.href=u;else documentOpenEditor.removeAttribute('href');}
  if(!multi&&item){renderIOEditor(item);renderProcessInfoEditor(item)}else{inputsBox.innerHTML='';outputsBox.innerHTML='';if(processInfoPanel)processInfoPanel.hidden=true;}
}
for(const [key,el] of Object.entries(processInfoFields)){
  if(!el)continue;
  el.addEventListener('change',()=>saveProcessInfoField(key,el.value));
  el.addEventListener('keydown',e=>{
    if(e.key==='Enter'&&(e.ctrlKey||e.metaKey)){
      e.preventDefault();saveProcessInfoField(key,el.value);el.blur();
      const item=selectedId?nodes.get(selectedId):null;if(item)item.el.focus();
    }
  });
}
function updateStyle(patch){
  if(!requireEdit())return;
  const items=selectedNodeItems();if(!items.length)return;
  const keepIds=[...selectedIds],keepSelectedId=selectedId;
  pushUndo();
  for(const item of items){
    Object.assign(item.data,patch);applyStyle(item);renderNodeIO(item);renderDocumentLink(item);invalidateNodeGeom(item.data.id);markNodeLinksDirty(item.data.id);
  }
  drawLinks();persist();
  selectedIds=new Set(keepIds.length?keepIds:items.map(x=>x.data.id));
  selectedId=keepSelectedId&&selectedIds.has(keepSelectedId)?keepSelectedId:(selectedIds.size===1?[...selectedIds][0]:null);
  refreshControls();updateSelectionUi();
}
function beginInlineEdit(el){
  if(!requireEdit())return;
  const item=nodes.get(el.dataset.id);
  if(!item)return;
  select(el);
  if(item.label.contentEditable==='true')return;
  pushUndo();
  item.label.contentEditable='true';
  item.label.focus();
  const range=document.createRange();
  range.selectNodeContents(item.label);
  range.collapse(false);
  const selection=window.getSelection();
  selection.removeAllRanges();
  selection.addRange(range);
}
function finishInlineEdit(el){
  const item=nodes.get(el.dataset.id);
  if(!item)return;
  if(item.label.contentEditable!=='true')return;
  if(!canEdit()){
    item.label.textContent=item.data.text||'Nytt steg';
    item.label.contentEditable='false';
    refreshControls();
    return;
  }
  const clean=(item.label.innerText||'').replace(/\n{3,}/g,'\n\n').trim();
  item.data.text=clean||item.data.text||'Nytt steg';
  item.label.textContent=item.data.text;
  item.label.contentEditable='false';
  applyStyle(item);
  invalidateNodeGeom(item.data.id);
  markNodeLinksDirty(item.data.id);
  drawLinks();
  persist();
  refreshControls();
}

function makeNode(data){
const d=clone(data),el=document.createElement('div');el.className='p48-node '+d.type;el.dataset.id=d.id;el.style.left=d.x+'px';el.style.top=d.y+'px';el.tabIndex=0;
if(d.width){
  el.style.boxSizing='border-box';el.style.minWidth='0px';el.style.maxWidth='none';el.style.width=d.width+'px';
}
if(d.height){el.style.boxSizing='border-box';el.style.minHeight='0px';el.style.height=d.height+'px';}
if(d.type==='object'){
  d.objectRole=['input','output','intermediate'].includes(d.objectRole)?d.objectRole:'intermediate';
  el.dataset.objectRole=d.objectRole;
}
const label=document.createElement('span');label.className='p48-label';label.textContent=d.text;label.contentEditable='false';label.spellcheck=true;el.appendChild(label);
const handles={};for(const side of ['right','left','top','bottom']){const h=document.createElement('span');h.className='p48-handle '+side;h.dataset.side=side;el.appendChild(h);handles[side]=h}
const resizeHandles={};for(const corner of ['se','sw','ne','nw']){const rh=document.createElement('span');rh.className='p48-resize '+corner;rh.dataset.corner=corner;el.appendChild(rh);resizeHandles[corner]=rh}
const nextWrap=document.createElement('div');nextWrap.className='p48-next-step-wrap';
const nextBtn=document.createElement('button');nextBtn.type='button';nextBtn.className='p48-next-step-btn';nextBtn.textContent='＋';nextBtn.title='Välj typ av nästa steg';nextBtn.setAttribute('aria-label','Lägg till nästa steg');nextBtn.setAttribute('aria-haspopup','true');nextBtn.setAttribute('aria-expanded','false');
const nextMenu=document.createElement('div');nextMenu.className='p48-next-step-menu';nextMenu.hidden=true;
const nextChoices=d.type==='process'
  ? [['object','▪ Objekt / resultat'],['decision','◇ Beslut'],['document','📄 Dokument'],['end','■ Slut']]
  : d.type==='object'
    ? [['process','▭ Aktivitet'],['decision','◇ Beslut'],['end','■ Slut']]
    : [['object','▪ Objekt'],['process','▭ Aktivitet'],['decision','◇ Beslut'],['document','📄 Dokument'],['end','■ Slut']];
for(const [type,caption] of nextChoices){
  const b=document.createElement('button');b.type='button';b.className='p48-next-step-choice';b.dataset.nextType=type;b.textContent=caption;
  if(type===preferredNextType({data:d}))b.classList.add('recommended');
  nextMenu.appendChild(b);
}
nextWrap.append(nextBtn,nextMenu);el.appendChild(nextWrap);
canvas.appendChild(el);nodes.set(d.id,{el,data:d,label,handles,resizeHandles,io:null,docOpen:null,docInlineEditor:null,docInlineInput:null,nextWrap,nextBtn,nextMenu});refreshEmptyState();applyStyle(nodes.get(d.id));renderNodeIO(nodes.get(d.id));renderDocumentLink(nodes.get(d.id));
nextBtn.addEventListener('pointerdown',e=>{e.stopPropagation();e.preventDefault()});
nextBtn.addEventListener('click',e=>{e.stopPropagation();e.preventDefault();if(!canEdit())return;closeNodeNextMenus(nextWrap);nextMenu.hidden=!nextMenu.hidden;nextBtn.setAttribute('aria-expanded',nextMenu.hidden?'false':'true')});
nextMenu.querySelectorAll('.p48-next-step-choice').forEach(b=>{b.addEventListener('pointerdown',e=>{e.stopPropagation()});b.addEventListener('click',e=>{e.stopPropagation();e.preventDefault();addNextStepFromNode(d.id,b.dataset.nextType)})});
for(const h of Object.values(handles)){
  h.style.width=connectorPointSize+'px';
  h.style.height=connectorPointSize+'px';
  h.style.background=connectorPointColor;
  h.style.border='1px solid #fff';
  h.style.boxShadow='0 0 0 1px '+connectorPointColor;
  h.style.display=connectorPointsHidden?'none':'';
}
el.addEventListener('dblclick',e=>{e.stopPropagation();beginInlineEdit(el)});
label.addEventListener('click',e=>{e.stopPropagation();if(e.ctrlKey||e.metaKey){e.preventDefault();toggleNodeSelection(el)}else select(el)});
label.addEventListener('dblclick',e=>{e.stopPropagation();beginInlineEdit(el)});
label.addEventListener('input',()=>{const item=nodes.get(el.dataset.id);if(item&&canEdit()){invalidateNodeGeom(item.data.id);markNodeLinksDirty(item.data.id);drawLinks()}});
label.addEventListener('blur',()=>finishInlineEdit(el));
label.addEventListener('keydown',e=>{
  if(e.key==='Escape'){e.preventDefault();finishInlineEdit(el);el.focus();}
  if(e.key==='Enter'&&(e.ctrlKey||e.metaKey)){
    e.preventDefault();finishInlineEdit(el);
    const item=nodes.get(el.dataset.id),type=preferredNextType(item);
    if(type)addNextStepFromNode(el.dataset.id,type);
    return;
  }
  if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();finishInlineEdit(el);el.focus();}
});
let suppressSelectClick=false;
el.addEventListener('click',e=>{
  e.stopPropagation();
  if(suppressSelectClick){suppressSelectClick=false;return}
  if(e.ctrlKey||e.metaKey){e.preventDefault();toggleNodeSelection(el);return}
  select(el);
});
el.addEventListener('pointerdown',e=>{
  if(!canEdit())return;
  if(e.button!==0||e.target.classList.contains('p48-handle')||e.target.classList.contains('p48-resize')||e.target.classList.contains('p48-doc-open')||(e.target.closest&&e.target.closest('.p48-doc-inline-editor'))||(e.target.closest&&e.target.closest('.p48-next-step-wrap'))||(e.target.classList.contains('p48-label')&&e.target.isContentEditable))return;
  if(e.ctrlKey||e.metaKey){
    e.preventDefault();e.stopPropagation();toggleNodeSelection(el);suppressSelectClick=true;return;
  }
  const groupIds=(selectedIds.size>1&&selectedIds.has(el.dataset.id))?[...selectedIds]:null;
  if(!groupIds)select(el);
  const activeIds=groupIds||[el.dataset.id];
  const startItems=activeIds.map(id=>{const item=nodes.get(id);return item?{id,x:parseFloat(item.el.style.left)||0,y:parseFloat(item.el.style.top)||0,width:item.el.offsetWidth,height:item.el.offsetHeight}:null}).filter(Boolean);
  const startVia=MapliniEditingCore.movedInternalVias(links,activeIds,0,0).map(v=>({index:v.index,viaX:v.viaX,viaY:v.viaY}));
  const sx=e.clientX,sy=e.clientY,pointerType=e.pointerType||'mouse';
  let mutated=false;
  fastGeometryInteraction=true;
  try{el.setPointerCapture(e.pointerId)}catch(ignore){}
  const mv=ev=>{
    const screenDx=ev.clientX-sx,screenDy=ev.clientY-sy;
    if(!mutated&&MapliniMobileCore.movedEnough(screenDx,screenDy,pointerType)){pushUndo(true);mutated=true}
    if(!mutated)return;
    const raw=screenDeltaToCanvas(screenDx,screenDy);
    let delta=MapliniEditingCore.groupMoveDelta(startItems,raw.dx,raw.dy,MapliniCanvasCore.DEFAULT_BOUNDS,20);
    const reference=startItems.find(x=>x.id===el.dataset.id)||startItems[0];
    if(reference){
      const snapped=magneticSnap(reference,reference.x+delta.dx,reference.y+delta.dy,new Set(activeIds));
      delta={dx:snapped.x-reference.x,dy:snapped.y-reference.y};
      showSnapGuides(snapped);
    }
    for(const start of startItems){
      const item=nodes.get(start.id);if(!item)continue;
      item.el.style.left=(start.x+delta.dx)+'px';item.el.style.top=(start.y+delta.dy)+'px';sync(item.el);invalidateNodeGeom(start.id);markNodeLinksDirty(start.id);
    }
    for(const base of startVia){
      const link=links[base.index];if(!link||!link[3]||typeof link[3]!=='object')continue;
      if(base.viaX!=null)link[3].viaX=base.viaX+delta.dx;
      if(base.viaY!=null)link[3].viaY=base.viaY+delta.dy;
    }
    drawLinks();
  };
  const done=()=>{
    el.removeEventListener('pointermove',mv);el.removeEventListener('pointerup',done);el.removeEventListener('pointercancel',done);
    try{if(el.hasPointerCapture&&el.hasPointerCapture(e.pointerId))el.releasePointerCapture(e.pointerId)}catch(ignore){}
    hideSnapGuides();
    fastGeometryInteraction=false;
    if(mutated){
      straightenAlignedConnectedLinks(activeIds);
      suppressSelectClick=Boolean(groupIds);requestFullLinkRender(true);persist();updateSelectionUi();
    }else{
      drawLinks(true);
    }
  };
  el.addEventListener('pointermove',mv);el.addEventListener('pointerup',done);el.addEventListener('pointercancel',done);
});

Object.values(resizeHandles).forEach(rh=>rh.addEventListener('pointerdown',e=>{
  if(!canEdit())return;
  e.stopPropagation();e.preventDefault();select(el);
  const corner=rh.dataset.corner,sx=e.clientX,sy=e.clientY;
  const ox=parseFloat(el.style.left)||0,oy=parseFloat(el.style.top)||0,ow=el.offsetWidth,oh=el.offsetHeight;
  let mutated=false;
  fastGeometryInteraction=true;
  const mv=ev=>{
    const screenDx=ev.clientX-sx,screenDy=ev.clientY-sy;
    if(!mutated&&MapliniMobileCore.movedEnough(screenDx,screenDy,e.pointerType||'mouse')){pushUndo(true);mutated=true}
    if(!mutated)return;
    const {dx,dy}=screenDeltaToCanvas(screenDx,screenDy);
    const box=MapliniCanvasCore.resize({x:ox,y:oy,width:ow,height:oh},corner,dx,dy,el.classList.contains('decision')?'decision':'process');
    el.style.left=box.x+'px';el.style.top=box.y+'px';el.style.width=box.width+'px';el.style.height=box.height+'px';el.style.minHeight=box.height+'px';
    sync(el);const item=nodes.get(el.dataset.id);item.data.width=box.width;item.data.height=box.height;invalidateNodeGeom(el.dataset.id);markNodeLinksDirty(el.dataset.id);drawLinks();
  };
  const done=()=>{
    document.removeEventListener('pointermove',mv);document.removeEventListener('pointerup',done);document.removeEventListener('pointercancel',done);
    fastGeometryInteraction=false;
    if(mutated){requestFullLinkRender(true);persist()}else drawLinks(true);
  };
  document.addEventListener('pointermove',mv);document.addEventListener('pointerup',done);document.addEventListener('pointercancel',done);
}));

Object.values(handles).forEach(h=>h.addEventListener('pointerdown',e=>{
  if(!canEdit())return;
  e.stopPropagation();e.preventDefault();
  const side=h.dataset.side,[x1,y1]=anchor(el,side);
  temp.hidden=false;temp.setAttribute('d',`M${x1},${y1} L${x1},${y1}`);
  const mv=ev=>{const p=clientToCanvas(ev.clientX,ev.clientY);temp.setAttribute('d',`M${x1},${y1} L${p.x},${p.y}`)};
  const finish=ev=>{
    document.removeEventListener('pointermove',mv);document.removeEventListener('pointerup',finish);document.removeEventListener('pointercancel',cancel);
    finishTempArrow();
    if(!ev)return;
    const target=document.elementFromPoint(ev.clientX,ev.clientY)?.closest('.p48-node');
    if(target&&target!==el){
      pushUndo();const autoLabel=decisionAutoLabel(el.dataset.id);
      links.push(MapliniConnectorCore.create(el.dataset.id,target.dataset.id,side,{label:autoLabel}));
      const newIndex=links.length-1;
      polishAutomaticConnectedLinks([el.dataset.id,target.dataset.id],{forceAuto:true});
      requestFullLinkRender();persist();
      coachDirectActivityLink(newIndex);
    }
  };
  const cancel=()=>{document.removeEventListener('pointermove',mv);document.removeEventListener('pointerup',finish);document.removeEventListener('pointercancel',cancel);finishTempArrow()};
  document.addEventListener('pointermove',mv);document.addEventListener('pointerup',finish);document.addEventListener('pointercancel',cancel);
}));
return el}

function addNode(type,x,y,options={}){
  if(!requireEdit())return;pushUndo();seq++;
  const objectRole=type==='object'&&['input','output','intermediate'].includes(options.objectRole)?options.objectRole:'intermediate';
  const el=makeNode({id:'n'+seq,type,text:nodeText(type),x:x-90,y:y-38,objectRole,processInfo:MapliniProcessInfoCore.normalize({})});
  place(el,x-90,y-38);sync(el);select(el);drawLinks();persist();
}
function isNextStepSource(item){return Boolean(item&&['start','object','process','decision','document','subprocess'].includes(String(item.data&&item.data.type||'')))}
function preferredNextType(item){
  const type=String(item?.data?.type||'');
  if(type==='process')return'object';
  if(['start','object','decision','document','subprocess'].includes(type))return'process';
  return null;
}
function preferredNextLabel(item){
  const type=preferredNextType(item);
  if(type==='object')return'＋ Objekt ut';
  if(type==='process')return'＋ Aktivitet';
  return'＋ Nästa';
}
function workflowCue(item){
  const current=String(item?.data?.type||'');
  const currentLabel=current==='process'?'Aktivitet':(current==='object'?(item.data.objectRole==='input'?'Objekt in':(item.data.objectRole==='output'?'Objekt ut':'Objekt')):(current==='start'?'Start':(current==='decision'?'Beslut':(current==='document'?'Dokument':(current==='subprocess'?'Delprocess':'')))));
  const next=preferredNextType(item),nextLabel=next==='object'?'Objekt ut':(next==='process'?'Aktivitet':'');
  return currentLabel&&nextLabel?`${currentLabel} → ${nextLabel}`:'';
}
function ensureNodeVisible(el){
  if(!el||!scroll)return;
  const left=parseFloat(el.style.left)||0,top=parseFloat(el.style.top)||0,w=el.offsetWidth||180,h=el.offsetHeight||76;
  const visualLeft=left*canvasScale,visualTop=top*canvasScale,visualRight=(left+w)*canvasScale,visualBottom=(top+h)*canvasScale;
  const margin=84;
  let nextLeft=scroll.scrollLeft,nextTop=scroll.scrollTop;
  if(visualLeft<scroll.scrollLeft+margin)nextLeft=Math.max(0,visualLeft-margin);
  else if(visualRight>scroll.scrollLeft+scroll.clientWidth-margin)nextLeft=Math.max(0,visualRight-scroll.clientWidth+margin);
  if(visualTop<scroll.scrollTop+margin)nextTop=Math.max(0,visualTop-margin);
  else if(visualBottom>scroll.scrollTop+scroll.clientHeight-margin)nextTop=Math.max(0,visualBottom-scroll.clientHeight+margin);
  if(nextLeft!==scroll.scrollLeft||nextTop!==scroll.scrollTop){
    scroll.scrollTo({left:nextLeft,top:nextTop,behavior:'smooth'});
  }
}

function closeNodeNextMenus(exceptWrap=null){for(const item of nodes.values()){if(!item.nextMenu||item.nextMenu.hidden||item.nextWrap===exceptWrap)continue;item.nextMenu.hidden=true;if(item.nextBtn)item.nextBtn.setAttribute('aria-expanded','false')}}
function addNextStepFromNode(sourceId,type='process'){
  if(!requireEdit())return false;
  const allowed=new Set(['object','process','decision','document','end']);type=allowed.has(String(type))?String(type):'process';
  const source=nodes.get(sourceId);if(!isNextStepSource(source)){msg('Det går inte att lägga ett nästa steg här');return false}
  pushUndo(true);seq++;const id='n'+seq;
  const nextObjectRole=type==='object'?(source.data.type==='process'?'output':'intermediate'):null;
  const el=makeNode({id,type,text:nodeText(type),x:0,y:0,objectRole:nextObjectRole,processInfo:MapliniProcessInfoCore.normalize({})});
  const sourceRect={x:source.el.offsetLeft,y:source.el.offsetTop,width:source.el.offsetWidth,height:source.el.offsetHeight};
  const existing=[...nodes.values()].filter(x=>x.data.id!==id).map(x=>({x:x.el.offsetLeft,y:x.el.offsetTop,width:x.el.offsetWidth,height:x.el.offsetHeight}));
  const pos=MapliniEditingCore.nextStepPosition(sourceRect,{width:el.offsetWidth,height:el.offsetHeight},existing,MapliniCanvasCore.DEFAULT_BOUNDS,120);
  el.style.left=pos.x+'px';el.style.top=pos.y+'px';sync(el);
  const autoLabel=decisionAutoLabel(sourceId);links.push(MapliniConnectorCore.create(sourceId,id,'right',{label:autoLabel}));
  polishAutomaticConnectedLinks([sourceId,id],{forceAuto:true});
  closeNodeNextMenus();select(el);requestFullLinkRender(true);persist();refreshControls();refreshLinkControls();updateSelectionUi();
  const names={object:(nextObjectRole==='output'?'Objekt ut':'Objekt'),process:'Aktivitet',decision:'Beslut',document:'Dokument',end:'Slut'};
  msg((names[type]||'Steg')+' tillagt · skriv namnet · Ctrl+Enter fortsätter');
  requestAnimationFrame(()=>{ensureNodeVisible(el);beginInlineEdit(el)});return true;
}


function distancePointToSegment(px,py,x1,y1,x2,y2){
  const vx=x2-x1,vy=y2-y1,wx=px-x1,wy=py-y1;
  const len2=vx*vx+vy*vy;
  if(len2===0)return Math.hypot(px-x1,py-y1);
  let t=(wx*vx+wy*vy)/len2;
  t=Math.max(0,Math.min(1,t));
  const qx=x1+t*vx,qy=y1+t*vy;
  return Math.hypot(px-qx,py-qy);
}
function linkDistanceAt(index,x,y){
  const link=links[index];if(!link)return Infinity;
  const A=nodes.get(link[0])?.el,B=nodes.get(link[1])?.el;if(!A||!B)return Infinity;
  const points=linkGeometry(link,A,B).points;
  let best=Infinity;for(let i=1;i<points.length;i++)best=Math.min(best,distancePointToSegment(x,y,points[i-1][0],points[i-1][1],points[i][0],points[i][1]));
  return best;
}
function hitTestLink(clientX,clientY){
  const rect=canvas.getBoundingClientRect();
  const x=clientX-rect.left;
  const y=clientY-rect.top;
  let best=null,bestDist=Infinity;
  links.forEach((_,i)=>{
    const d=linkDistanceAt(i,x,y);
    if(d<bestDist){bestDist=d;best=i}
  });
  return bestDist<=22?best:null;
}

function linkStyle(link){return MapliniConnectorCore.style(link)}
function setLinkStyle(i,patch){return MapliniConnectorCore.setStyle(links,i,patch)}
function dashArray(st){return st.dash==='dashed'?'10 7':st.dash==='dotted'?'2 6':''}
function refreshLinkControls(){
  const link=selectedLinkIndex!=null?links[selectedLinkIndex]:null;
  linkFormat.hidden=!link;
  linkFormat.classList.toggle('on',!!link);
  linkHandle.classList.toggle('on',!!link);
  if(linkQuick)linkQuick.classList.toggle('on',!!link&&canEdit());
  if(!link){linkQuickRouting.forEach(btn=>btn.classList.remove('active'));refreshFlowCoach();return;}
  const st=linkStyle(link);
  linkQuickRouting.forEach(btn=>{btn.disabled=!canEdit();btn.classList.toggle('active',btn.dataset.linkRouting===(st.routing||'straight'));});
  setFormatEnabled(false);
  const editable=canEdit();
  linkColor.disabled=!editable;
  if(linkWidth)linkWidth.disabled=!editable;
  linkEnd.disabled=!editable;
  linkDash.disabled=!editable;
  linkRouting.disabled=!editable;
  linkAnchorMode.disabled=!editable;
  linkLabel.disabled=!editable;
  if(insertLinkStepBtn)insertLinkStepBtn.disabled=!editable;
  insertLinkStepChoices.forEach(btn=>btn.disabled=!editable);
  if(!editable)setInsertStepMenu(false);
  deleteLinkBtn.disabled=!editable;
  linkColor.value=st.color||'#687584';
  if(linkWidth)linkWidth.value=String(Number(st.width)||2);
  linkEnd.value=st.end||'arrow';
  linkDash.value=st.dash||'solid';
  linkRouting.value=st.routing||'straight';
  linkAnchorMode.value=st.anchorMode||'manual';
  linkLabel.value=st.label||'';
  refreshFlowCoach();
}
function selectLink(i,deferRender=false){
  if(i==null||!links[i])return;
  selectedLinkIndices.clear();
  selectedLinkIndex=i;
  selectedId=null;
  selectedIds.clear();
  refreshControls();
  updateSelectionUi();
  refreshLinkControls();
  if(!deferRender)requestFullLinkRender(true);
}
function isDirectActivityLink(index){
  const link=index!=null?links[index]:null;if(!link)return false;
  const from=nodes.get(String(link[0]))?.data,to=nodes.get(String(link[1]))?.data;
  const st=linkStyle(link);
  return Boolean(from&&to&&from.type==='process'&&to.type==='process'&&st.methodOverride!=='direct_activity_ok');
}
function refreshFlowCoach(){
  if(!flowCoach)return;
  flowCoach.hidden=!(selectedLinkIndex!=null&&canEdit()&&isDirectActivityLink(selectedLinkIndex));
}
function coachDirectActivityLink(index){
  const link=index!=null?links[index]:null;
  if(!link)return false;
  const from=nodes.get(link[0])?.data,to=nodes.get(link[1])?.data;
  if(!from||!to||from.type!=='process'||to.type!=='process')return false;
  selectLink(index,true);
  setInsertStepMenu(false);
  refreshFlowCoach();
  msg('Två aktiviteter är kopplade direkt. Lägg gärna in resultatet som gör att nästa aktivitet kan börja.');
  requestFullLinkRender(true);
  return true;
}
function setInsertStepMenu(open){
  if(!insertLinkStepMenu||!insertLinkStepBtn)return;
  const show=!!open&&selectedLinkIndex!=null&&canEdit();
  insertLinkStepMenu.hidden=!show;
  insertLinkStepBtn.setAttribute('aria-expanded',show?'true':'false');
}
function insertStepOnSelectedLink(type='process'){
  if(!requireEdit())return false;
  const allowed=new Set(['object','process','decision','document','end']);
  type=allowed.has(String(type))?String(type):'process';
  const index=selectedLinkIndex;
  const link=index!=null?links[index]:null;
  if(!link){setInsertStepMenu(false);msg('Markera först en pil');return false}
  const A=nodes.get(link[0])?.el,B=nodes.get(link[1])?.el;
  if(!A||!B){setInsertStepMenu(false);msg('Kopplingen kunde inte läsas');return false}
  const points=linkGeometry(link,A,B).points,mp=MapliniConnectorCore.midpoint(points);
  if(!mp){setInsertStepMenu(false);msg('Kopplingen kunde inte läsas');return false}
  pushUndo(true);
  seq++;
  const id='n'+seq;
  const objectRole=type==='object'?'intermediate':null;
  const el=makeNode({id,type,text:nodeText(type),x:mp.x-90,y:mp.y-38,objectRole});
  place(el,mp.x-90,mp.y-38);sync(el);
  links=MapliniConnectorCore.splitLink(links,index,id);
  selectedLinkIndex=null;selectedLinkIndices.clear();
  setInsertStepMenu(false);
  select(el);
  requestFullLinkRender(true);persist();refreshControls();refreshLinkControls();updateSelectionUi();
  const names={object:'Objekt',process:'Aktivitet',decision:'Beslut',document:'Dokument',end:'Slut'};
  msg((names[type]||'Steg')+' infogat på pilen');
  requestAnimationFrame(()=>beginInlineEdit(el));
  return true;
}
function deleteLinkAt(index,withUndo=true){
  if(!requireEdit())return false;
  if(index==null||!links[index])return false;
  if(withUndo)pushUndo();
  links=MapliniConnectorCore.removeAt(links,index);
  const next=MapliniSelectionCore.afterLinkDelete({
    selectedId,selectedIds:[...selectedIds],selectedLinkIndex,selectedLinkIndices:[...selectedLinkIndices]
  },index);
  selectedId=next.selectedId;selectedIds=new Set(next.selectedIds);
  selectedLinkIndex=next.selectedLinkIndex;selectedLinkIndices=new Set(next.selectedLinkIndices);
  requestFullLinkRender(true);persist();
  refreshControls();refreshLinkControls();updateSelectionUi();
  return true;
}
function clearLinkSelection(){
  const had=(selectedLinkIndex!=null||selectedLinkIndices.size>0);
  selectedLinkIndex=null;selectedLinkIndices.clear();refreshLinkControls();
  if(had)requestFullLinkRender(true);
}
function markerFor(st,x,y,ang){
  const ns='http://www.w3.org/2000/svg',sw=Math.max(1,Number(st.width||2));
  if(st.end==='none')return null;
  if(st.end==='circle'){const c=document.createElementNS(ns,'circle');c.setAttribute('cx',x);c.setAttribute('cy',y);c.setAttribute('r',4.2+sw*.45);c.setAttribute('fill','#fff');c.setAttribute('stroke',st.color);c.setAttribute('stroke-width',Math.min(sw,2.5));return c}
  const p=document.createElementNS(ns,'polygon'),len=7.5+sw*1.15,w=3.2+sw*.72;
  let pts;
  if(st.end==='diamond')pts=[[0,0],[-len,w],[-2*len,0],[-len,-w]];
  else pts=[[0,0],[-len,w],[-len,-w]];
  p.setAttribute('points',pts.map(([px,py])=>{const rx=x+px*Math.cos(ang)-py*Math.sin(ang),ry=y+px*Math.sin(ang)+py*Math.cos(ang);return rx+','+ry}).join(' '));
  p.setAttribute('fill',st.color);
  p.setAttribute('stroke',st.color);
  p.setAttribute('stroke-linejoin','round');
  p.setAttribute('stroke-width',Math.min(.8,sw*.3));
  return p;
}
function linkLabelPlacement(points,offset=22){
  if(!Array.isArray(points)||points.length<2)return null;
  let total=0,segments=[];
  for(let i=1;i<points.length;i++){
    const a=points[i-1],b=points[i],len=Math.hypot(b[0]-a[0],b[1]-a[1]);
    if(len>0){segments.push({a,b,len});total+=len}
  }
  if(!segments.length)return null;
  let target=total/2,used=0,seg=segments[segments.length-1],t=.5;
  for(const candidate of segments){
    if(used+candidate.len>=target){seg=candidate;t=(target-used)/candidate.len;break}
    used+=candidate.len;
  }
  const x=seg.a[0]+(seg.b[0]-seg.a[0])*t,y=seg.a[1]+(seg.b[1]-seg.a[1])*t;
  const dx=seg.b[0]-seg.a[0],dy=seg.b[1]-seg.a[1],len=Math.max(1,Math.hypot(dx,dy));
  let nx=-dy/len,ny=dx/len;
  // Keep horizontal labels above the line and vertical labels to the right.
  if(Math.abs(dx)>=Math.abs(dy)){if(ny>0){nx=-nx;ny=-ny}}
  else if(nx<0){nx=-nx;ny=-ny}
  return {x:x+nx*offset,y:y+ny*offset};
}
function linkQuickPlacement(points,st){
  // Keep the routing toolbar on the opposite side of the connector from its text label.
  // This prevents the three selected-link affordances (text, handle, toolbar) from stacking.
  const hasLabel=Boolean(String(st&&st.label||'').trim());
  return linkLabelPlacement(points,hasLabel?-42:-32);
}
function updateSelectedLinkUi(points,st){
  const mp=MapliniConnectorCore.midpoint(points);if(!mp)return;
  linkHandle.style.left=mp.x+'px';linkHandle.style.top=mp.y+'px';linkHandle.classList.add('on');
  if(linkQuick){
    const qp=linkQuickPlacement(points,st)||mp;
    linkQuick.style.left=qp.x+'px';linkQuick.style.top=qp.y+'px';
    linkQuick.classList.toggle('on',canEdit());
  }
}
function linkLabelElement(st,points,selected=false){
  const value=String(st&&st.label||'').trim();
  if(!value)return null;
  const pos=linkLabelPlacement(points);if(!pos)return null;
  const ns='http://www.w3.org/2000/svg',g=document.createElementNS(ns,'g');
  g.setAttribute('class','p48-link-label');g.style.pointerEvents='none';
  const width=Math.min(300,Math.max(42,value.length*7.8+22)),height=26;
  const rect=document.createElementNS(ns,'rect');
  rect.setAttribute('x',pos.x-width/2);rect.setAttribute('y',pos.y-height/2);rect.setAttribute('width',width);rect.setAttribute('height',height);rect.setAttribute('rx','7');
  if(selected){rect.setAttribute('stroke','#5b92cb');rect.setAttribute('stroke-width','1.5')}
  const text=document.createElementNS(ns,'text');text.setAttribute('x',pos.x);text.setAttribute('y',pos.y+.5);text.textContent=value;
  g.append(rect,text);return g;
}
function decisionAutoLabel(sourceId){
  // Connector text is explicit per connector. Never inject a standard Ja/Nej label.
  // Existing saved labels are preserved; new links start blank until the user names them.
  return '';
}
function selectedLinkMidpoint(){
  const link=selectedLinkIndex!=null?links[selectedLinkIndex]:null;if(!link)return null;
  const A=nodes.get(link[0])?.el,B=nodes.get(link[1])?.el;if(!A||!B)return null;
  return MapliniConnectorCore.midpoint(linkGeometry(link,A,B).points);
}


function clearLinkHitLayer(){
  if(linkHitLayer)linkHitLayer.innerHTML='';
}

function startSelectedLinkDrag(index,e){
  if(!canEdit()||index==null||!links[index])return false;
  e.preventDefault();e.stopPropagation();
  const pointerTarget=e.currentTarget||null;
  try{if(pointerTarget&&pointerTarget.setPointerCapture&&e.pointerId!=null)pointerTarget.setPointerCapture(e.pointerId)}catch(_err){}
  if(selectedLinkIndex!==index)selectLink(index,true);
  const sx=e.clientX,sy=e.clientY,pointerType=e.pointerType||'mouse';
  const startLink=links[index],startA=nodes.get(startLink[0])?.el,startB=nodes.get(startLink[1])?.el;
  if(!startA||!startB)return false;
  const startStyle=Object.assign({},linkStyle(startLink));
  const startSides=linkSides(startLink,startA,startB),startAnchorA=anchor(startA,startSides.source),startAnchorB=anchor(startB,startSides.target);
  const directMidX=(startAnchorA[0]+startAnchorB[0])/2,directMidY=(startAnchorA[1]+startAnchorB[1])/2;
  const routeMid=MapliniConnectorCore.midpoint(linkGeometry(startLink,startA,startB).points)||{x:directMidX,y:directMidY};
  const baseFreeDx=startStyle.routing==='free'?(Number(startStyle.freeDx)||0):(routeMid.x-directMidX);
  const baseFreeDy=startStyle.routing==='free'?(Number(startStyle.freeDy)||0):(routeMid.y-directMidY);
  let mutated=false;
  const move=ev=>{
    const screenDx=ev.clientX-sx,screenDy=ev.clientY-sy;
    if(!mutated&&MapliniMobileCore.movedEnough(screenDx,screenDy,pointerType)){pushUndo(true);mutated=true}
    if(!mutated)return;
    // Use pointer delta from pointerdown, not absolute pointer position. This guarantees
    // that the connector never jumps when the user grabs it near either endpoint.
    const dx=screenDx/canvasScale,dy=screenDy/canvasScale;
    MapliniConnectorCore.setFreeOffset(links,index,baseFreeDx+dx,baseFreeDy+dy);
    dirtyLinks.add(index);
    drawLinks();
    refreshLinkControls();
  };
  const finish=()=>{
    document.removeEventListener('pointermove',move);
    document.removeEventListener('pointerup',finish);
    document.removeEventListener('pointercancel',finish);
    if(mutated)persist();
    else requestFullLinkRender(true);
  };
  document.addEventListener('pointermove',move);
  document.addEventListener('pointerup',finish);
  document.addEventListener('pointercancel',finish);
  return true;
}

function addHtmlLinkHitSegment(index,x1,y1,x2,y2){
  if(!linkHitLayer)return;
  const dx=x2-x1,dy=y2-y1,len=Math.hypot(dx,dy);
  if(len<1)return;
  const seg=document.createElement('div');
  seg.className='p48-link-hit-segment';
  seg.dataset.linkIndex=String(index);
  seg.style.left=x1+'px';
  seg.style.top=(y1-14)+'px';
  seg.style.width=len+'px';
  seg.style.height='28px';
  seg.style.transform=`rotate(${Math.atan2(dy,dx)}rad)`;
  seg.style.transformOrigin='0 50%';
  seg.style.pointerEvents='auto';
  const choose=e=>{
    e.preventDefault();
    e.stopPropagation();
    if(canEdit()){
      // One gesture must be enough: select the connector and immediately arm dragging.
      // startSelectedLinkDrag only mutates after the movement threshold, so a normal
      // click still behaves as a pure selection.
      startSelectedLinkDrag(index,e);
      return;
    }
    selectLink(index);
  };
  if(selectedLinkIndex===index)seg.classList.add('p48-selected-link-hit');
  seg.addEventListener('pointerdown',choose);
  seg.addEventListener('click',e=>{e.preventDefault();e.stopPropagation();if(selectedLinkIndex!==index)selectLink(index)});
  linkHitLayer.appendChild(seg);
}

function renderAllLinksNow(){
  rebuildLinkAdjacency();
  linkLayer.innerHTML='';clearLinkHitLayer();
  links.forEach((link,index)=>{
    const [a,b,side]=link;
    const A=nodes.get(a)?.el,B=nodes.get(b)?.el;
    if(!A||!B)return;

    const geom=linkGeometry(link,A,B),st=geom.st,points=geom.points,d=geom.d;
    for(let pi=1;pi<points.length;pi++)addHtmlLinkHitSegment(index,points[pi-1][0],points[pi-1][1],points[pi][0],points[pi][1]);

    const g=document.createElementNS('http://www.w3.org/2000/svg','g');
    if(selectedLinkIndex===index||selectedLinkIndices.has(index))g.setAttribute('class','p48-link-selected');

    if(selectedLinkIndex===index){
      const halo=document.createElementNS('http://www.w3.org/2000/svg','path');
      halo.setAttribute('class','p48-link-selection');
      halo.setAttribute('d',d);
      g.appendChild(halo);
    }

    const v=document.createElementNS('http://www.w3.org/2000/svg','path');
    v.setAttribute('class','p48-link-visible');
    v.setAttribute('d',d);
    v.setAttribute('stroke',st.color);
    v.setAttribute('stroke-width',st.width);
    v.setAttribute('fill','none');
    v.setAttribute('stroke-linecap','round');
    v.setAttribute('stroke-linejoin','round');
    const da=dashArray(st);
    if(da)v.setAttribute('stroke-dasharray',da);
    else v.removeAttribute('stroke-dasharray');
    v.setAttribute('stroke-linecap','round');

    const hit=document.createElementNS('http://www.w3.org/2000/svg','path');
    hit.setAttribute('class','p48-link-hit');
    hit.setAttribute('d',d);
    hit.setAttribute('fill','none');
    hit.setAttribute('stroke','rgba(0,0,0,0.001)');
    hit.setAttribute('stroke-width','20');
    hit.style.pointerEvents='stroke';
    hit.style.cursor='pointer';
    hit.addEventListener('pointerdown',e=>{
      e.preventDefault();
      e.stopPropagation();
      if(canEdit()){
        // Allow click-drag directly, even when the connector was not selected beforehand.
        startSelectedLinkDrag(index,e);
        return;
      }
      selectLink(index);
    });
    hit.addEventListener('click',e=>{
      e.preventDefault();
      e.stopPropagation();
      selectLink(index);
    });

    g.appendChild(v);

    const endPt=points[points.length-1],ang=lastSegmentAngle(points);
    const mk=markerFor(st,endPt[0],endPt[1],ang);
    if(mk){
      mk.style.pointerEvents='none';
      g.appendChild(mk);
    }
    const labelEl=linkLabelElement(st,points,selectedLinkIndex===index);
    if(labelEl)g.appendChild(labelEl);

    // hit path last = topmost click target
    g.appendChild(hit);
    linkDomByIndex.set(index,{group:g,visible:v,hit,halo:(selectedLinkIndex===index?g.querySelector('.p48-link-selection'):null),marker:mk||null,label:labelEl||null});linkLayer.appendChild(g);
  });

  if(selectedLinkIndex!=null){
    const selected=links[selectedLinkIndex],A=selected&&nodes.get(selected[0])?.el,B=selected&&nodes.get(selected[1])?.el;
    if(selected&&A&&B){
      const geom=linkGeometry(selected,A,B);
      updateSelectedLinkUi(geom.points,geom.st);
    }
  }else{
    linkHandle.classList.remove('on');
    if(linkQuick)linkQuick.classList.remove('on');
  }
}

const linkDomByIndex=new Map();
let dirtyLinks=new Set();
let fullLinkRenderNeeded=true;
const linkIndicesByNode=new Map();
let linkAdjacencyReady=false;
let fastGeometryInteraction=false;

function rebuildLinkAdjacency(){
  linkIndicesByNode.clear();
  for(let i=0;i<links.length;i++){
    const l=links[i];if(!Array.isArray(l)||l.length<2)continue;
    const a=String(l[0]),b=String(l[1]);
    if(!linkIndicesByNode.has(a))linkIndicesByNode.set(a,[]);
    if(!linkIndicesByNode.has(b))linkIndicesByNode.set(b,[]);
    linkIndicesByNode.get(a).push(i);
    if(b!==a)linkIndicesByNode.get(b).push(i);
  }
  linkAdjacencyReady=true;
}
function linksForNode(id){
  const key=String(id);
  if(linkAdjacencyReady)return linkIndicesByNode.get(key)||[];
  const out=[];
  for(let i=0;i<links.length;i++){
    const l=links[i];
    if(Array.isArray(l)&&(String(l[0])===key||String(l[1])===key))out.push(i);
  }
  return out;
}

function markNodeLinksDirty(id){
  for(const i of linksForNode(id))dirtyLinks.add(i);
}

function redrawSingleLink(index){
  // Small-path update; if DOM entry isn't available, fall back to full render.
  const entry=linkDomByIndex.get(index);
  const link=links[index];
  if(!entry||!link){fullLinkRenderNeeded=true;return}
  const [a,b,side]=link;
  const A=nodes.get(a)?.el,B=nodes.get(b)?.el;
  if(!A||!B){fullLinkRenderNeeded=true;return}
  const geom=linkGeometry(link,A,B),st=geom.st,points=geom.points,d=geom.d;
  entry.visible.setAttribute('d',d);
  entry.hit.setAttribute('d',d);
  if(entry.halo)entry.halo.setAttribute('d',d);

  /* During node drag/resize, keep the hot frame path-only. Rebuilding HTML hit
     segments, markers and labels for every pointermove is expensive on large maps.
     A complete render runs when the gesture ends. */
  if(fastGeometryInteraction){
    if(selectedLinkIndex===index)updateSelectedLinkUi(points,st);
    return;
  }

  // update HTML hit segments only for this link
  for(const el of linkHitLayer.querySelectorAll(`[data-link-index="${index}"]`))el.remove();
  for(let pi=1;pi<points.length;pi++)addHtmlLinkHitSegment(index,points[pi-1][0],points[pi-1][1],points[pi][0],points[pi][1]);

  const oldMarker=entry.marker;
  if(oldMarker&&oldMarker.parentNode)oldMarker.parentNode.removeChild(oldMarker);
  const endPt=points[points.length-1],ang=lastSegmentAngle(points);
  const mk=markerFor(st,endPt[0],endPt[1],ang);
  if(mk){
    mk.style.pointerEvents='none';
    entry.group.insertBefore(mk,entry.hit);
    entry.marker=mk;
  }else entry.marker=null;
  if(entry.label&&entry.label.parentNode)entry.label.parentNode.removeChild(entry.label);
  const labelEl=linkLabelElement(st,points,selectedLinkIndex===index);
  if(labelEl)entry.group.insertBefore(labelEl,entry.hit);
  entry.label=labelEl||null;

  if(selectedLinkIndex===index)updateSelectedLinkUi(points,st);
}

function renderDirtyLinksNow(){
  if(fullLinkRenderNeeded){
    fullLinkRenderNeeded=false;
    renderAllLinksNow();
    return;
  }
  if(!dirtyLinks.size)return;
  const items=[...dirtyLinks];
  dirtyLinks.clear();
  for(const i of items)redrawSingleLink(i);
}




function requestFullLinkRender(immediate=false){
  fullLinkRenderNeeded=true;
  linkAdjacencyReady=false;
  drawLinks(immediate);
}

let linkRenderRaf=0;
function drawLinks(immediate=false){
  if(immediate){
    if(linkRenderRaf){cancelAnimationFrame(linkRenderRaf);linkRenderRaf=0;}
    renderDirtyLinksNow();
    if(selectedId||selectedIds.size)refreshNodeQuickToolbar();
    return;
  }
  if(linkRenderRaf)return;
  linkRenderRaf=requestAnimationFrame(()=>{
    linkRenderRaf=0;
    renderDirtyLinksNow();
    if(selectedId||selectedIds.size)refreshNodeQuickToolbar();
  });
}





document.addEventListener('pointerdown',e=>{
  if(e.button!==0)return;
  if(!canvas.contains(e.target))return;
  if(e.target.closest&&e.target.closest('.p48-node'))return;
  if(e.target===linkHandle)return;
  if(e.target.closest&&e.target.closest('.p48-node-quick,.p48-link-quick'))return;
  const segment=e.target.closest&&e.target.closest('.p48-link-hit-segment');
  const hit=segment?Number(segment.dataset.linkIndex):hitTestLink(e.clientX,e.clientY);
  if(hit!=null&&Number.isInteger(hit)&&links[hit]){
    // This capture listener runs before the connector segment's own pointerdown handler.
    // Arm dragging here as well, otherwise the first gesture only selects the connector.
    if(canEdit()){
      startSelectedLinkDrag(hit,e);
      return;
    }
    e.preventDefault();
    e.stopPropagation();
    selectLink(hit);
  }
},true);


function isMobileLayout(){
  return window.matchMedia('(max-width:900px), (pointer:coarse) and (max-width:1100px)').matches;
}
function clientToCanvas(clientX,clientY){
  const p=MapliniMobileCore.clientToLocal(clientX,clientY,canvas.getBoundingClientRect());
  return {x:p.x/canvasScale,y:p.y/canvasScale};
}
function setMobileTools(open){
  if(!sidePanel||!mobileToolsBtn||!mobileBackdrop)return;
  const on=Boolean(open)&&isMobileLayout();
  sidePanel.classList.toggle('p48-mobile-open',on);
  mobileBackdrop.classList.toggle('on',on);
  mobileToolsBtn.setAttribute('aria-expanded',on?'true':'false');
  mobileToolsBtn.textContent=on?'✕ Stäng':'☰ Verktyg';
  const full=root.classList.contains('p48-mobile-canvas-fullscreen');
  document.documentElement.style.overflowY=full?'hidden':'visible';
  document.body.style.overflowY=full?'hidden':'visible';
}
function setMobileSheet(mode=null){
  if(!mobileSheet||!mobileSheetBackdrop)return;
  const on=Boolean(mode)&&isMobileLayout();
  mobileSheet.classList.toggle('on',on);mobileSheetBackdrop.classList.toggle('on',on);mobileSheet.setAttribute('aria-hidden',on?'false':'true');
  if(!on)return;
  const context=mode==='context';mobileAddSheet.hidden=context;mobileContextSheet.hidden=!context;if(mobileSheetTitle)mobileSheetTitle.textContent=context?'Markerade rutor':'Lägg till steg';
}
function setMobileFullscreen(on,{fromBrowser=false}={}){
  const enabled=Boolean(on)&&isMobileLayout();root.classList.toggle('p48-mobile-canvas-fullscreen',enabled);document.documentElement.style.overflow=enabled?'hidden':'';document.body.style.overflow=enabled?'hidden':'';
  if(mobileFullscreen){mobileFullscreen.textContent=enabled?'⤢ Avsluta':'⛶ Helskärm';mobileFullscreen.setAttribute('aria-pressed',enabled?'true':'false')}
  if(mobileSheetFullscreen){mobileSheetFullscreen.textContent=enabled?'⤢ Avsluta helskärm':'⛶ Helskärm';mobileSheetFullscreen.setAttribute('aria-pressed',enabled?'true':'false')}
  if(enabled){
    setMobileTools(false);setMobileSheet(null);document.documentElement.style.overflow='hidden';document.body.style.overflow='hidden';
    if(!fromBrowser&&!document.fullscreenElement&&root.requestFullscreen){try{const req=root.requestFullscreen();if(req&&req.catch)req.catch(()=>{})}catch(_){}}
  }else if(!fromBrowser&&document.fullscreenElement&&document.exitFullscreen){try{const ex=document.exitFullscreen();if(ex&&ex.catch)ex.catch(()=>{})}catch(_){}}
  requestAnimationFrame(()=>{fitProcessToScreen();refreshMobileBar()});
}
document.addEventListener('fullscreenchange',()=>{if(!document.fullscreenElement&&root.classList.contains('p48-mobile-canvas-fullscreen'))setMobileFullscreen(false,{fromBrowser:true})});
if(mobileToolsBtn)mobileToolsBtn.addEventListener('click',()=>setMobileTools(!sidePanel.classList.contains('p48-mobile-open')));
if(mobileBackdrop)mobileBackdrop.addEventListener('click',()=>setMobileTools(false));
if(mobileAdd)mobileAdd.addEventListener('click',()=>setMobileSheet('add'));
if(mobileUndo)mobileUndo.addEventListener('click',()=>root.querySelector('#p48-undo').click());
if(mobileRedo)mobileRedo.addEventListener('click',()=>root.querySelector('#p48-redo').click());
if(mobileFit)mobileFit.addEventListener('click',()=>fitProcessToScreen());
if(mobileMore)mobileMore.addEventListener('click',()=>setMobileTools(true));
if(mobileFullscreen)mobileFullscreen.addEventListener('click',()=>setMobileFullscreen(!root.classList.contains('p48-mobile-canvas-fullscreen')));
if(mobileNext)mobileNext.addEventListener('click',()=>{if(nodeQuickNext&&!nodeQuickNext.hidden)nodeQuickNext.click()});
if(mobileFormat)mobileFormat.addEventListener('click',()=>setMobileSheet('context'));
if(mobileDuplicate)mobileDuplicate.addEventListener('click',()=>duplicateSelectedNodes());
if(mobileContext)mobileContext.addEventListener('click',()=>setMobileSheet('context'));
if(mobileDelete)mobileDelete.addEventListener('click',()=>deleteSelectedMany());
if(mobileSheetBackdrop)mobileSheetBackdrop.addEventListener('click',()=>setMobileSheet(null));if(mobileSheetClose)mobileSheetClose.addEventListener('click',()=>setMobileSheet(null));
if(mobileSheetRedo)mobileSheetRedo.addEventListener('click',()=>{setMobileSheet(null);root.querySelector('#p48-redo').click()});
if(mobileSheetFullscreen)mobileSheetFullscreen.addEventListener('click',()=>{setMobileSheet(null);setMobileFullscreen(!root.classList.contains('p48-mobile-canvas-fullscreen'))});
if(mobileOpenTools)mobileOpenTools.addEventListener('click',()=>{setMobileSheet(null);setMobileTools(true)});if(mobileSheetTools)mobileSheetTools.addEventListener('click',()=>{setMobileSheet(null);focusFormattingPanel()});
if(mobileSheetFormat)mobileSheetFormat.addEventListener('click',()=>{setMobileSheet(null);focusFormattingPanel()});
if(mobileSheetCopy)mobileSheetCopy.addEventListener('click',()=>{copySelectedNodes({announce:false});setMobileSheet(null);msg('Markerade kopierade')});
if(mobileSheetLayoutH)mobileSheetLayoutH.addEventListener('click',()=>{smartLayout('selected','horizontal');setMobileSheet(null)});if(mobileSheetLayoutV)mobileSheetLayoutV.addEventListener('click',()=>{smartLayout('selected','vertical');setMobileSheet(null)});
if(mobileSheetDelete)mobileSheetDelete.addEventListener('click',()=>{setMobileSheet(null);deleteSelectedMany()});
root.querySelectorAll('[data-mobile-add]').forEach(btn=>btn.addEventListener('click',()=>{const [x,y]=paletteInsertPoint();addNode(btn.dataset.mobileAdd,x,y);setMobileSheet(null);msg('Form tillagd')}));
window.addEventListener('keydown',e=>{if(e.key==='Escape'){if(root.classList.contains('p48-mobile-canvas-fullscreen'))setMobileFullscreen(false);else{setMobileSheet(null);setMobileTools(false)}}});
root.addEventListener('click',e=>{
  if(!isMobileLayout())return;
  const addBtn=e.target.closest&&e.target.closest('[data-add]');
  if(addBtn)setTimeout(()=>setMobileTools(false),0);
});

// v0.16.3 desktop canvas navigation: drag blank canvas with the primary mouse button.
let desktopPan=null,desktopPanMoved=false;
function desktopPanBlankTarget(target){
  if(!target)return false;
  return target===scroll||target===canvas||target===canvas.parentElement||
    target.id==='p48-svg'||target.id==='p48-links'||target.classList?.contains('p48-print-page');
}
if(scroll){
  scroll.classList.add('p48-desktop-pan-ready');
  scroll.addEventListener('pointerdown',e=>{
    if(isMobileLayout()||selectionMode||e.pointerType==='touch'||e.button!==0||!desktopPanBlankTarget(e.target))return;
    desktopPan={id:e.pointerId,x:e.clientX,y:e.clientY,left:scroll.scrollLeft,top:scroll.scrollTop};
    desktopPanMoved=false;scroll.classList.add('p48-desktop-panning');
    try{scroll.setPointerCapture(e.pointerId)}catch(_){}
    e.preventDefault();
  },{passive:false});
  scroll.addEventListener('pointermove',e=>{
    if(!desktopPan||desktopPan.id!==e.pointerId)return;
    const dx=e.clientX-desktopPan.x,dy=e.clientY-desktopPan.y;
    if(Math.abs(dx)>3||Math.abs(dy)>3)desktopPanMoved=true;
    scroll.scrollLeft=Math.max(0,desktopPan.left-dx);
    scroll.scrollTop=Math.max(0,desktopPan.top-dy);
    scheduleHorizontalNavSync();
    e.preventDefault();
  },{passive:false});
  const endDesktopPan=e=>{
    if(!desktopPan||desktopPan.id!==e.pointerId)return;
    const wasClick=!desktopPanMoved;
    desktopPan=null;scroll.classList.remove('p48-desktop-panning');
    try{scroll.releasePointerCapture(e.pointerId)}catch(_){}
    /* A press/release on blank canvas is a normal outside click, not a pan.
       Clear node/link selection here because pointer capture can retarget the later click event to scroll. */
    if(wasClick&&!selectionMode){
      clearSelection();clearLinkSelection();finishTempArrow();
    }
  };
  scroll.addEventListener('pointerup',endDesktopPan);
  scroll.addEventListener('pointercancel',endDesktopPan);
}

// v0.13 mobile canvas gestures: one finger pans blank canvas, two fingers pinch-zoom.
const mobilePointers=new Map();let mobileGesture=null;
function mobileGestureBlocked(target){return Boolean(target&&target.closest&&target.closest('.p48-node,.p48-node-quick,.p48-link-quick,.p48-link-hit-segment,.p48-link-visible,.p48-link-selection,.p48-link-handle,.p48-handle,.p48-resize,button,input,select,summary,a'));}
function resetMobileGesture(){mobileGesture=null;if(!mobilePointers.size&&scroll)scroll.classList.remove('p48-touching')}
if(scroll){
  scroll.addEventListener('pointerdown',e=>{
    if(!isMobileLayout()||selectionMode||e.pointerType!=='touch'||mobileGestureBlocked(e.target))return;
    mobilePointers.set(e.pointerId,{x:e.clientX,y:e.clientY});scroll.classList.add('p48-touching');
    try{scroll.setPointerCapture(e.pointerId)}catch(_){}
    const pts=[...mobilePointers.values()];
    if(pts.length===1)mobileGesture={kind:'pan',x:pts[0].x,y:pts[0].y,left:scroll.scrollLeft,top:scroll.scrollTop};
    else if(pts.length>=2){const a=pts[0],b=pts[1],mid=MapliniMobileCore.gestureMidpoint(a,b),rect=scroll.getBoundingClientRect();mobileGesture={kind:'pinch',distance:MapliniMobileCore.gestureDistance(a,b),scale:canvasScale,logicalX:(scroll.scrollLeft+mid.x-rect.left)/canvasScale,logicalY:(scroll.scrollTop+mid.y-rect.top)/canvasScale};}
    e.preventDefault();
  },{passive:false});
  scroll.addEventListener('pointermove',e=>{
    if(!mobilePointers.has(e.pointerId)||!mobileGesture)return;
    mobilePointers.set(e.pointerId,{x:e.clientX,y:e.clientY});const pts=[...mobilePointers.values()];
    if(pts.length>=2){
      const a=pts[0],b=pts[1],mid=MapliniMobileCore.gestureMidpoint(a,b),rect=scroll.getBoundingClientRect();
      if(mobileGesture.kind!=='pinch')mobileGesture={kind:'pinch',distance:MapliniMobileCore.gestureDistance(a,b),scale:canvasScale,logicalX:(scroll.scrollLeft+mid.x-rect.left)/canvasScale,logicalY:(scroll.scrollTop+mid.y-rect.top)/canvasScale};
      const next=MapliniMobileCore.pinchScale(mobileGesture.scale,mobileGesture.distance,MapliniMobileCore.gestureDistance(a,b));applyCanvasScale(next,false);
      scroll.scrollLeft=Math.max(0,mobileGesture.logicalX*canvasScale-(mid.x-rect.left));scroll.scrollTop=Math.max(0,mobileGesture.logicalY*canvasScale-(mid.y-rect.top));scheduleHorizontalNavSync();
    }else if(pts.length===1){
      const p=pts[0];if(mobileGesture.kind!=='pan')mobileGesture={kind:'pan',x:p.x,y:p.y,left:scroll.scrollLeft,top:scroll.scrollTop};
      scroll.scrollLeft=Math.max(0,mobileGesture.left-(p.x-mobileGesture.x));scroll.scrollTop=Math.max(0,mobileGesture.top-(p.y-mobileGesture.y));scheduleHorizontalNavSync();
    }
    e.preventDefault();
  },{passive:false});
  const endMobilePointer=e=>{if(!mobilePointers.has(e.pointerId))return;mobilePointers.delete(e.pointerId);const pts=[...mobilePointers.values()];if(pts.length===1){const p=pts[0];mobileGesture={kind:'pan',x:p.x,y:p.y,left:scroll.scrollLeft,top:scroll.scrollTop}}else if(!pts.length)resetMobileGesture();};
  scroll.addEventListener('pointerup',endMobilePointer);scroll.addEventListener('pointercancel',endMobilePointer);
}


function deleteSelected(){
  if(selectedIds.size>1){deleteSelectedMany();return;}
  if(!selectedId||!nodes.has(selectedId))return;
  selectedIds=new Set([selectedId]);deleteSelectedMany();
}

function crc32(bytes){let crc=0^(-1);for(let i=0;i<bytes.length;i++){crc^=bytes[i];for(let j=0;j<8;j++)crc=(crc>>>1)^(0xEDB88320&-(crc&1))}return(crc^(-1))>>>0}
const u16=n=>new Uint8Array([n&255,(n>>>8)&255]);const u32=n=>new Uint8Array([n&255,(n>>>8)&255,(n>>>16)&255,(n>>>24)&255]);
function cat(parts){const n=parts.reduce((s,p)=>s+p.length,0),o=new Uint8Array(n);let k=0;for(const p of parts){o.set(p,k);k+=p.length}return o}
function mkzip(files){
  const enc=new TextEncoder(),locals=[],centrals=[];let off=0;
  for(const f of files){
    const nb=enc.encode(f.name);
    const db=(f.data instanceof Uint8Array)?f.data:enc.encode(String(f.data));
    const crc=crc32(db);
    const local=cat([u32(0x04034b50),u16(20),u16(0),u16(0),u16(0),u16(0),u32(crc),u32(db.length),u32(db.length),u16(nb.length),u16(0),nb,db]);
    locals.push(local);
    centrals.push(cat([u32(0x02014b50),u16(20),u16(20),u16(0),u16(0),u16(0),u16(0),u32(crc),u32(db.length),u32(db.length),u16(nb.length),u16(0),u16(0),u16(0),u16(0),u32(0),u32(off),nb]));
    off+=local.length;
  }
  const cb=cat(centrals),end=cat([u32(0x06054b50),u16(0),u16(0),u16(files.length),u16(files.length),u32(cb.length),u32(off),u16(0)]);
  return cat([...locals,cb,end]);
}


function xmlEscape(v){
  return String(v??'')
    .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
    .replace(/"/g,'&quot;').replace(/'/g,'&apos;');
}
function colName(n){
  let s='';while(n>0){n--;s=String.fromCharCode(65+(n%26))+s;n=Math.floor(n/26)}return s;
}
function xlsxInlineCell(ref,value,style=0){
  const v=String(value??'');
  const preserve=/^\s|\s$|\n/.test(v)?' xml:space="preserve"':'';
  return `<c r="${ref}" t="inlineStr"${style?` s="${style}"`:''}><is><t${preserve}>${xmlEscape(v)}</t></is></c>`;
}
function xlsxNumberCell(ref,value,style=0){
  const n=Number(value);
  return `<c r="${ref}"${style?` s="${style}"`:''}><v>${Number.isFinite(n)?n:0}</v></c>`;
}
function typeLabel(type){
  return ({
    start:'Start',
    activity:'Aktivitet',
    decision:'Beslut',
    end:'Slut',
    subprocess:'Delprocess',
    note:'Anteckning',
    document:'Dokument'
  })[type]||String(type||'');
}
function processRowsForSheet(){
  const ordered=[...nodes.values()]
    .map(item=>item.data)
    .sort((a,b)=>((a.y||0)-(b.y||0))||((a.x||0)-(b.x||0)));
  const nodeById=new Map(ordered.map(n=>[n.id,n]));
  return ordered.map((d,index)=>{
    const outgoing=links.filter(l=>l[0]===d.id).map(l=>nodeById.get(l[1])?.text||l[1]);
    const incoming=links.filter(l=>l[1]===d.id).map(l=>nodeById.get(l[0])?.text||l[0]);
    return [
      index+1,
      d.id||'',
      typeLabel(d.type),
      d.text||'',
      d.type==='document'?(d.documentUrl||''):'',
      Array.isArray(d.inputs)?d.inputs.filter(Boolean).join(' | '):'',
      Array.isArray(d.outputs)?d.outputs.filter(Boolean).join(' | '):'',
      outgoing.join(' | '),
      incoming.join(' | '),
      d.x||0,
      d.y||0,
      d.width||'',
      d.height||''
    ];
  });
}
function buildSheetXml(headers,rows,widths){
  const rowXml=[];
  rowXml.push(`<row r="1" ht="24" customHeight="1">${headers.map((h,i)=>xlsxInlineCell(colName(i+1)+'1',h,1)).join('')}</row>`);
  rows.forEach((row,ri)=>{
    const r=ri+2;
    const cells=row.map((v,ci)=>{
      const ref=colName(ci+1)+r;
      return (typeof v==='number')?xlsxNumberCell(ref,v,0):xlsxInlineCell(ref,v,0);
    }).join('');
    rowXml.push(`<row r="${r}">${cells}</row>`);
  });
  const cols=(widths||headers.map(()=>18)).map((w,i)=>`<col min="${i+1}" max="${i+1}" width="${w}" customWidth="1"/>`).join('');
  const last=colName(headers.length)+(rows.length+1);
  return `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
<dimension ref="A1:${last}"/>
<sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>
<cols>${cols}</cols>
<sheetData>${rowXml.join('')}</sheetData>
<autoFilter ref="A1:${last}"/>
</worksheet>`;
}
function buildGoogleSheetsXlsx(){
  persist();
  const s=state();
  const stepHeaders=['Ordning','ID','Typ','Text','Dokumentlänk','Inputs','Outputs','Nästa steg','Föregående steg','X','Y','Bredd','Höjd'];
  const stepRows=processRowsForSheet();
  const nodeMap=new Map((s.nodes||[]).map(n=>[n.id,n]));
  const linkHeaders=['Från ID','Från steg','Till ID','Till steg','Anslutning','Piltext'];
  const linkRows=(s.links||[]).map(l=>[
    l[0],
    nodeMap.get(l[0])?.text||'',
    l[1],
    nodeMap.get(l[1])?.text||'',
    l[2]||'right',
    MapliniConnectorCore.style(l).label||''
  ]);

  const sheet1=buildSheetXml(stepHeaders,stepRows,[9,12,14,36,42,28,28,30,30,10,10,10,10]);
  const sheet2=buildSheetXml(linkHeaders,linkRows,[14,34,14,34,14,24]);

  const contentTypes=`<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
<Override PartName="/xl/worksheets/sheet2.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
</Types>`;
  const rootRels=`<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>`;
  const workbook=`<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
<sheets>
<sheet name="Processsteg" sheetId="1" r:id="rId1"/>
<sheet name="Kopplingar" sheetId="2" r:id="rId2"/>
</sheets>
</workbook>`;
  const workbookRels=`<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet2.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>`;
  const styles=`<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
<fonts count="2">
<font><sz val="11"/><name val="Arial"/></font>
<font><b/><color rgb="FFFFFFFF"/><sz val="11"/><name val="Arial"/></font>
</fonts>
<fills count="3">
<fill><patternFill patternType="none"/></fill>
<fill><patternFill patternType="gray125"/></fill>
<fill><patternFill patternType="solid"><fgColor rgb="FF1F6F55"/><bgColor indexed="64"/></patternFill></fill>
</fills>
<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>
<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
<cellXfs count="2">
<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>
<xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0" applyFont="1" applyFill="1"/>
</cellXfs>
<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>
</styleSheet>`;

  return mkzip([
    {name:'[Content_Types].xml',data:contentTypes},
    {name:'_rels/.rels',data:rootRels},
    {name:'xl/workbook.xml',data:workbook},
    {name:'xl/_rels/workbook.xml.rels',data:workbookRels},
    {name:'xl/styles.xml',data:styles},
    {name:'xl/worksheets/sheet1.xml',data:sheet1},
    {name:'xl/worksheets/sheet2.xml',data:sheet2}
  ]);
}
function prepareExport(){
  persist(false,false);
  const localOk=saveLocal(true);
  if(!localOk)reportRuntimeError(new Error('Local pre-export save failed'),'export-preflight');
  return localOk;
}
function exportGoogleSheets(){
  try{
    prepareExport();
    const bytes=buildGoogleSheetsXlsx();
    downloadBytes(
      bytes,
      cleanFileName(state().name)+'_Google_Sheets.xlsx',
      'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
      'zip'
    );
    msg('Google Sheets-fil skapad');
  }catch(err){
    reportRuntimeError(err,'export-xlsx');msg('Google Sheets-export misslyckades');
  }
}


function cleanFileName(name){
  return (String(name||'Maplini_process').replace(/[^a-z0-9åäö_-]+/gi,'_').replace(/^_+|_+$/g,'')||'Maplini_process');
}
function hexRgb(hex){
  const h=String(hex||'#ffffff').replace('#','');
  if(h.length!==6)return [255,255,255];
  return [parseInt(h.slice(0,2),16),parseInt(h.slice(2,4),16),parseInt(h.slice(4,6),16)];
}
function rgba(hex,a=1){
  const [r,g,b]=hexRgb(hex);return `rgba(${r},${g},${b},${a})`;
}
function wrapCanvasText(ctx,text,maxWidth){
  const lines=[];
  for(const paragraph of String(text??'').split(/\n/)){
    const words=paragraph.split(/\s+/).filter(Boolean);
    if(!words.length){lines.push('');continue}
    let line='';
    for(const word of words){
      const candidate=line?line+' '+word:word;
      if(ctx.measureText(candidate).width<=maxWidth){line=candidate}
      else{
        if(line)lines.push(line);
        let part='';
        for(const ch of word){
          if(ctx.measureText(part+ch).width>maxWidth&&part){lines.push(part);part=ch}
          else part+=ch;
        }
        line=part;
      }
    }
    if(line)lines.push(line);
  }
  return lines;
}
function exportBounds(){
  const items=[...nodes.values()];
  if(!items.length)return null;
  let minX=Infinity,minY=Infinity,maxX=-Infinity,maxY=-Infinity;
  for(const item of items){
    const x=item.data.x||0,y=item.data.y||0,w=item.el.offsetWidth,h=item.el.offsetHeight;
    minX=Math.min(minX,x);minY=Math.min(minY,y);maxX=Math.max(maxX,x+w);maxY=Math.max(maxY,y+h);
  }
  return {minX,minY,maxX,maxY,width:maxX-minX,height:maxY-minY};
}
function drawArrow(ctx,x1,y1,x2,y2){
  ctx.save();ctx.strokeStyle='#687584';ctx.fillStyle='#687584';ctx.lineWidth=2;
  ctx.beginPath();ctx.moveTo(x1,y1);ctx.lineTo(x2,y2);ctx.stroke();
  const ang=Math.atan2(y2-y1,x2-x1),len=10,w=5;
  ctx.beginPath();ctx.moveTo(x2,y2);
  ctx.lineTo(x2-len*Math.cos(ang)+w*Math.sin(ang),y2-len*Math.sin(ang)-w*Math.cos(ang));
  ctx.lineTo(x2-len*Math.cos(ang)-w*Math.sin(ang),y2-len*Math.sin(ang)+w*Math.cos(ang));
  ctx.closePath();ctx.fill();ctx.restore();
}
function drawRoundedRect(ctx,x,y,w,h,r){
  const rr=Math.min(r,w/2,h/2);ctx.beginPath();ctx.moveTo(x+rr,y);ctx.arcTo(x+w,y,x+w,y+h,rr);ctx.arcTo(x+w,y+h,x,y+h,rr);ctx.arcTo(x,y+h,x,y,rr);ctx.arcTo(x,y,x+w,y,rr);ctx.closePath();
}

function drawProcessBackgroundPattern(ctx,x,y,w,h){
  const type=processBackgroundType||'solid';
  const d=Math.max(8,Number(processPatternDensity)||20);
  const c=processPatternColor||'#d7e1e8';
  const bg=processBackground||'#ffffff';

  ctx.save();
  if(type==='gradient'){
    const angle=(Number(processGradientAngle)||0)*Math.PI/180,dx=Math.cos(angle),dy=Math.sin(angle);
    const cx=x+w/2,cy=y+h/2,len=Math.abs(w*dx)+Math.abs(h*dy);
    const g=ctx.createLinearGradient(cx-dx*len/2,cy-dy*len/2,cx+dx*len/2,cy+dy*len/2);
    g.addColorStop(0,processGradientStart||'#ffffff');g.addColorStop(1,processGradientEnd||'#e7f1ff');
    ctx.fillStyle=g;ctx.fillRect(x,y,w,h);
  }else{
    const base=type==='texture-paper'?'#f4efe4':type==='texture-parchment'?'#f3dfb2':type==='texture-canvas'?'#ece8dc':type==='texture-concrete'?'#dedfdf':(type==='none'?'#ffffff':bg);
    ctx.fillStyle=base;ctx.fillRect(x,y,w,h);
  }

  ctx.beginPath();ctx.rect(x,y,w,h);ctx.clip();
  ctx.strokeStyle=c;ctx.fillStyle=c;ctx.lineWidth=1;

  if(type==='dots'){
    for(let px=x;px<x+w;px+=d)for(let py=y;py<y+h;py+=d){ctx.beginPath();ctx.arc(px,py,1.2,0,Math.PI*2);ctx.fill();}
  }else if(type==='grid'||type==='technical'||type==='crosshatch'){
    const xStep=(type==='crosshatch')?d*2:d;
    for(let px=x;px<x+w;px+=xStep){ctx.beginPath();ctx.moveTo(px,y);ctx.lineTo(px,y+h);ctx.stroke();}
    for(let py=y;py<y+h;py+=d){ctx.beginPath();ctx.moveTo(x,py);ctx.lineTo(x+w,py);ctx.stroke();}
    if(type==='technical'){const major=d*5;ctx.lineWidth=1.5;for(let px=x;px<x+w;px+=major){ctx.beginPath();ctx.moveTo(px,y);ctx.lineTo(px,y+h);ctx.stroke();}for(let py=y;py<y+h;py+=major){ctx.beginPath();ctx.moveTo(x,py);ctx.lineTo(x+w,py);ctx.stroke();}}
  }else if(type==='lines'){
    for(let py=y;py<y+h;py+=d){ctx.beginPath();ctx.moveTo(x,py);ctx.lineTo(x+w,py);ctx.stroke();}
  }else if(type==='diagonal'){
    for(let k=-h;k<w;k+=d){ctx.beginPath();ctx.moveTo(x+k,y);ctx.lineTo(x+k+h,y+h);ctx.stroke();}
    for(let k=0;k<w+h;k+=d){ctx.beginPath();ctx.moveTo(x+k,y);ctx.lineTo(x+k-h,y+h);ctx.stroke();}
  }else if(type.startsWith('texture-')){
    ctx.globalAlpha=.14;ctx.strokeStyle='#765f43';ctx.lineWidth=.7;
    if(type==='texture-canvas'){for(let py=y;py<y+h;py+=5){ctx.beginPath();ctx.moveTo(x,py);ctx.lineTo(x+w,py);ctx.stroke()}for(let px=x;px<x+w;px+=5){ctx.beginPath();ctx.moveTo(px,y);ctx.lineTo(px,y+h);ctx.stroke()}}
    else {for(let i=0;i<Math.min(1300,Math.floor(w*h/2400));i++){const px=x+((i*73)%Math.max(1,w)),py=y+((i*151)%Math.max(1,h));ctx.beginPath();ctx.arc(px,py,type==='texture-concrete'?1.7:1,0,Math.PI*2);ctx.stroke()}}
    ctx.globalAlpha=1;
  }else if(type==='watermark'&&!processWatermarkUseLogo){
    ctx.save();ctx.globalAlpha=Math.max(.05,Math.min(.4,Number(processWatermarkOpacity)||.15));ctx.fillStyle=processPatternColor||'#64748b';ctx.font='800 74px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.translate(x+w/2,y+h/2);ctx.rotate(-28*Math.PI/180);ctx.fillText((processWatermarkText||'UTKAST').slice(0,80),0,0,Math.max(300,w*.78));ctx.restore();
  }
  ctx.restore();
}

async function renderMapSnapshot(){
  persist();
  if(document.fonts&&document.fonts.ready){try{await document.fonts.ready}catch(e){}}
  const b=exportBounds();if(!b)throw new Error('Processen är tom');
  const logoImg=new Image();
  const logoReady=new Promise(resolve=>{logoImg.onload=()=>resolve(true);logoImg.onerror=()=>resolve(false);});
  logoImg.src="__MAPLINI_LOGO__";
  await logoReady;
  const pad=60,header=90,scale=Math.min(2,Math.max(1,1800/Math.max(900,b.width)));
  const width=Math.ceil((b.width+pad*2)*scale),height=Math.ceil((b.height+pad*2+header)*scale);
  const out=document.createElement('canvas');out.width=width;out.height=height;
  const ctx=out.getContext('2d');ctx.scale(scale,scale);
  ctx.fillStyle='#ffffff';ctx.fillRect(0,0,width/scale,height/scale);

  // branded export header
  ctx.textBaseline='top';
  if(logoImg.complete&&logoImg.naturalWidth){
    const maxLogoW=260,maxLogoH=58;
    const lr=Math.min(maxLogoW/logoImg.naturalWidth,maxLogoH/logoImg.naturalHeight);
    const lw=logoImg.naturalWidth*lr,lh=logoImg.naturalHeight*lr;
    ctx.drawImage(logoImg,pad,12,lw,lh);
  }else{
    ctx.fillStyle='#12243b';ctx.font='700 30px Arial';ctx.fillText('Maplini',pad,15);
  }
  ctx.fillStyle='#20364f';ctx.font='700 13px Arial';ctx.fillText('MAP · UNDERSTAND · IMPROVE',pad,66);
  ctx.fillStyle='#12243b';ctx.font='700 22px Arial';ctx.fillText(state().name,pad+330,28);

  const ox=pad-b.minX,oy=header+pad-b.minY;
  drawProcessBackgroundPattern(ctx,0,header,width/scale,(height/scale)-header);
  if(processBackgroundType==='image'&&processBackgroundImageData){
    try{
      const bgImg=await loadImage(processBackgroundImageData);
      const areaW=width/scale,areaH=(height/scale)-header;
      const r=Math.max(areaW/bgImg.width,areaH/bgImg.height),dw=bgImg.width*r,dh=bgImg.height*r;
      ctx.save();ctx.globalAlpha=Math.max(.05,Math.min(1,Number(processBackgroundImageOpacity)||.25));
      ctx.drawImage(bgImg,(areaW-dw)/2,header+(areaH-dh)/2,dw,dh);ctx.restore();
    }catch(e){}
  }
  if(processBackgroundType==='watermark'&&processWatermarkUseLogo&&processLogoData){
    try{
      const wm=await loadImage(processLogoData),areaW=width/scale,areaH=(height/scale)-header,maxW=areaW*.42,maxH=areaH*.36,r=Math.min(maxW/wm.width,maxH/wm.height);
      ctx.save();ctx.globalAlpha=Math.max(.05,Math.min(.4,Number(processWatermarkOpacity)||.15));
      ctx.translate(areaW/2,header+areaH/2);ctx.rotate(-18*Math.PI/180);ctx.drawImage(wm,-wm.width*r/2,-wm.height*r/2,wm.width*r,wm.height*r);ctx.restore();
    }catch(e){}
  }

  if(processLogoData&&!processLogoHidden){
    try{
      const logoImg=await loadImage(processLogoData);
      const maxW=Math.min(processLogoWidth,260),scale=Math.min(maxW/logoImg.width,90/logoImg.height,1);
      ctx.drawImage(logoImg,pad,pad,logoImg.width*scale,logoImg.height*scale);
    }catch(e){}
  }

  // connectors
  for(const link of links){
    const [a,bid,side]=link,A=nodes.get(a)?.el,B=nodes.get(bid)?.el;if(!A||!B)continue;
    const geom=linkGeometry(link,A,B),st=geom.st,points=geom.points;
    ctx.save();ctx.strokeStyle=st.color;ctx.fillStyle=st.color;ctx.lineWidth=Number(st.width)||2;
    if(st.dash==='dashed')ctx.setLineDash([10,7]);else if(st.dash==='dotted')ctx.setLineDash([2,6]);
    ctx.beginPath();ctx.moveTo(ox+points[0][0],oy+points[0][1]);for(let pi=1;pi<points.length;pi++)ctx.lineTo(ox+points[pi][0],oy+points[pi][1]);ctx.stroke();
    const endPt=points[points.length-1],px=ox+endPt[0],py=oy+endPt[1],ang=lastSegmentAngle(points),len=10+(Number(st.width)||2)*1.5,w=5+(Number(st.width)||2);
    if(st.end==='arrow'){ctx.beginPath();ctx.moveTo(px,py);ctx.lineTo(px-len*Math.cos(ang)+w*Math.sin(ang),py-len*Math.sin(ang)-w*Math.cos(ang));ctx.lineTo(px-len*Math.cos(ang)-w*Math.sin(ang),py-len*Math.sin(ang)+w*Math.cos(ang));ctx.closePath();ctx.fill()}
    else if(st.end==='circle'){ctx.beginPath();ctx.arc(px,py,6+(Number(st.width)||2),0,Math.PI*2);ctx.fillStyle='#fff';ctx.fill();ctx.stroke()}
    else if(st.end==='diamond'){const pts=[[0,0],[-len,w],[-2*len,0],[-len,-w]];ctx.beginPath();pts.forEach(([qx,qy],i)=>{const rx=px+qx*Math.cos(ang)-qy*Math.sin(ang),ry=py+qx*Math.sin(ang)+qy*Math.cos(ang);i?ctx.lineTo(rx,ry):ctx.moveTo(rx,ry)});ctx.closePath();ctx.fillStyle=st.color;ctx.fill()}
    const linkText=String(st.label||'').trim();
    if(linkText){
      const mp=MapliniConnectorCore.midpoint(points),lx=ox+mp.x,ly=oy+mp.y;
      ctx.font='600 11px Arial';ctx.textAlign='center';ctx.textBaseline='middle';
      const tw=Math.min(240,Math.max(30,ctx.measureText(linkText).width+16)),th=21;
      ctx.fillStyle='rgba(255,255,255,.97)';ctx.strokeStyle='#d4dce5';ctx.lineWidth=1;
      drawRoundedRect(ctx,lx-tw/2,ly-th/2,tw,th,9);ctx.fill();ctx.stroke();
      ctx.fillStyle='#415064';ctx.fillText(linkText,lx,ly,tw-10);
    }
    ctx.restore();
  }

  // nodes
  for(const item of nodes.values()){
    const d=item.data,s=styleOf(d),x=ox+(d.x||0),y=oy+(d.y||0),w=item.el.offsetWidth,h=item.el.offsetHeight;
    ctx.save();
    if(s.nodeStyle==='3d'){ctx.shadowColor='rgba(31,42,55,.25)';ctx.shadowBlur=10;ctx.shadowOffsetX=5;ctx.shadowOffsetY=8;}
    else if(s.nodeStyle==='raised'){ctx.shadowColor='rgba(31,42,55,.22)';ctx.shadowBlur=18;ctx.shadowOffsetY=8;}
    else if(s.nodeStyle==='glass'){ctx.globalAlpha=.88;ctx.shadowColor='rgba(31,42,55,.16)';ctx.shadowBlur=12;ctx.shadowOffsetY=5;}
    else if(s.nodeStyle==='flat'){ctx.shadowColor='transparent';ctx.shadowBlur=0;}
    ctx.fillStyle=s.bgColor||'#ffffff';
    ctx.strokeStyle=s.borderColor||'#637387';ctx.lineWidth=Number(s.borderWidth)||2;

    if(d.type==='decision'){
      ctx.beginPath();ctx.moveTo(x+w/2,y);ctx.lineTo(x+w,y+h/2);ctx.lineTo(x+w/2,y+h);ctx.lineTo(x,y+h/2);ctx.closePath();ctx.fill();ctx.stroke();
    }else if(d.type==='start'||d.type==='end'){
      ctx.beginPath();ctx.ellipse(x+w/2,y+h/2,w/2,h/2,0,0,Math.PI*2);ctx.fill();ctx.stroke();
    }else{
      drawRoundedRect(ctx,x,y,w,h,10);ctx.fill();ctx.stroke();
    }
    ctx.shadowColor='transparent';ctx.shadowBlur=0;ctx.shadowOffsetX=0;ctx.shadowOffsetY=0;ctx.globalAlpha=1;

    const fontSize=Math.max(10,Math.min(36,Number(s.fontSize||13)));
    const weight=s.fontWeight==='700'?'700':'400',italicStyle=s.fontStyle==='italic'?'italic ':'';
    ctx.font=`${italicStyle}${weight} ${fontSize}px ${s.fontFamily==='system-ui'?'Arial':s.fontFamily}`;
    ctx.fillStyle=s.textColor||'#17202a';ctx.textBaseline='top';
    const inputs=Array.isArray(d.inputs)?d.inputs.filter(Boolean):[],outputs=Array.isArray(d.outputs)?d.outputs.filter(Boolean):[];
    const ioLines=[];
    if(inputs.length)ioLines.push('In: '+inputs.join(', '));
    if(outputs.length)ioLines.push('Out: '+outputs.join(', '));
    const maxText=Math.max(40,w-28);
    const labelLines=wrapCanvasText(ctx,d.text,maxText);
    const ioSize=Math.max(9,fontSize*.72),lineH=fontSize*1.28,ioH=ioSize*1.25;
    const totalH=labelLines.length*lineH+ioLines.length*ioH+(ioLines.length?7:0);
    let cy=y+Math.max(10,(h-totalH)/2);
    const align=s.textAlign||'center';
    ctx.textAlign=align;
    const tx=align==='left'?x+14:align==='right'?x+w-14:x+w/2;
    for(const line of labelLines){ctx.fillText(line,tx,cy,maxText);cy+=lineH}
    if(ioLines.length){cy+=4;ctx.font=`400 ${ioSize}px Arial`;ctx.fillStyle=rgba(s.textColor||'#17202a',.78);}
    for(const line of ioLines){const ls=wrapCanvasText(ctx,line,maxText);for(const sub of ls){ctx.fillText(sub,tx,cy,maxText);cy+=ioH}}
    ctx.restore();
  }
  return out;
}
function canvasJpegBytes(canvas,quality=.92){
  const dataUrl=canvas.toDataURL('image/jpeg',quality);
  const bin=atob(dataUrl.split(',')[1]),bytes=new Uint8Array(bin.length);
  for(let i=0;i<bin.length;i++)bytes[i]=bin.charCodeAt(i);
  return bytes;
}
function asciiBytes(s){return new TextEncoder().encode(s)}
function buildPdfFromJpeg(jpeg,imgW,imgH){
  // Kept for compatibility; current export uses buildMultiPagePdfFromCanvas.
  const spec=pageSpec();
  return buildMultiPagePdfFromCanvas(null,jpeg,imgW,imgH,spec,1);
}
function buildMultiPagePdfFromCanvas(canvasEl,jpeg,imgW,imgH,spec,count){
  const pageW=spec.pdfW,pageH=spec.pdfH,margin=28;
  const parts=[asciiBytes('%PDF-1.4\n%Maplini\n')],offsets={};
  const addObj=(num,chunks)=>{
    offsets[num]=parts.reduce((n,p)=>n+p.length,0);
    parts.push(asciiBytes(`${num} 0 obj\n`),...chunks,asciiBytes('\nendobj\n'));
  };

  const pageObjs=[],contentObjs=[],imageObjs=[];
  let nextObj=3;

  // If we have a canvas, slice it into equal-width image pages.
  const slices=[];
  if(canvasEl){
    const sliceW=Math.ceil(canvasEl.width/count);
    for(let i=0;i<count;i++){
      const x=i*sliceW;
      const w=Math.min(sliceW,canvasEl.width-x);
      const c=document.createElement('canvas');
      c.width=w;c.height=canvasEl.height;
      const cx=c.getContext('2d');
      cx.fillStyle='#fff';cx.fillRect(0,0,w,c.height);
      cx.drawImage(canvasEl,x,0,w,canvasEl.height,0,0,w,canvasEl.height);
      slices.push({jpeg:canvasJpegBytes(c,.94),w,h:c.height});
    }
  }else{
    slices.push({jpeg,w:imgW,h:imgH});
  }

  slices.forEach((sl,idx)=>{
    const pageObj=nextObj++,contentObj=nextObj++,imageObj=nextObj++;
    pageObjs.push(pageObj);contentObjs.push(contentObj);imageObjs.push(imageObj);
  });

  addObj(1,[asciiBytes('<< /Type /Catalog /Pages 2 0 R >>')]);
  addObj(2,[asciiBytes(`<< /Type /Pages /Kids [${pageObjs.map(x=>x+' 0 R').join(' ')}] /Count ${pageObjs.length} >>`)]);

  slices.forEach((sl,idx)=>{
    const pageObj=pageObjs[idx],contentObj=contentObjs[idx],imageObj=imageObjs[idx];
    const sc=Math.min((pageW-2*margin)/sl.w,(pageH-2*margin)/sl.h);
    const w=sl.w*sc,h=sl.h*sc,x=(pageW-w)/2,y=(pageH-h)/2;
    const content=asciiBytes(`q\n${w.toFixed(3)} 0 0 ${h.toFixed(3)} ${x.toFixed(3)} ${y.toFixed(3)} cm\n/Im${idx+1} Do\nQ\n`);
    addObj(pageObj,[asciiBytes(`<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${pageW} ${pageH}] /Resources << /XObject << /Im${idx+1} ${imageObj} 0 R >> >> /Contents ${contentObj} 0 R >>`)]);
    addObj(contentObj,[asciiBytes(`<< /Length ${content.length} >>\nstream\n`),content,asciiBytes('endstream')]);
    addObj(imageObj,[asciiBytes(`<< /Type /XObject /Subtype /Image /Width ${sl.w} /Height ${sl.h} /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length ${sl.jpeg.length} >>\nstream\n`),sl.jpeg,asciiBytes('\nendstream')]);
  });

  const totalObjs=nextObj-1;
  const xref=parts.reduce((n,p)=>n+p.length,0);
  let tail=`xref\n0 ${totalObjs+1}\n0000000000 65535 f \n`;
  for(let i=1;i<=totalObjs;i++)tail+=String(offsets[i]).padStart(10,'0')+' 00000 n \n';
  tail+=`trailer\n<< /Size ${totalObjs+1} /Root 1 0 R >>\nstartxref\n${xref}\n%%EOF`;
  parts.push(asciiBytes(tail));
  return cat(parts);
}
function buildDocxWithJpeg(jpeg,imgW,imgH,title){
  const maxCx=9144000,maxCy=6400800; // roughly 10 x 7 in
  let cx=maxCx,cy=Math.round(cx*imgH/imgW);
  if(cy>maxCy){cy=maxCy;cx=Math.round(cy*imgW/imgH)}
  const safeTitle=String(title||'Maplini process').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const doc=`<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
 xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
 xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
 xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">
<w:body>
<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:b/><w:sz w:val="32"/></w:rPr><w:t>${safeTitle}</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:drawing>
<wp:inline distT="0" distB="0" distL="0" distR="0">
<wp:extent cx="${cx}" cy="${cy}"/><wp:docPr id="1" name="Maplini process map"/>
<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">
<pic:pic><pic:nvPicPr><pic:cNvPr id="0" name="process-map.jpg"/><pic:cNvPicPr/></pic:nvPicPr>
<pic:blipFill><a:blip r:embed="rId1"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>
<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="${cx}" cy="${cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>
</pic:pic></a:graphicData></a:graphic>
</wp:inline></w:drawing></w:r></w:p>
<w:sectPr><w:pgSz w:w="16838" w:h="11906" w:orient="landscape"/><w:pgMar w:top="720" w:right="720" w:bottom="720" w:left="720"/></w:sectPr>
</w:body></w:document>`;
  const contentTypes=`<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Default Extension="jpg" ContentType="image/jpeg"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>`;
  const packageRels=`<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>`;
  const docRels=`<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/process-map.jpg"/>
</Relationships>`;
  return mkzip([
    {name:'[Content_Types].xml',data:contentTypes},
    {name:'_rels/.rels',data:packageRels},
    {name:'word/document.xml',data:doc},
    {name:'word/_rels/document.xml.rels',data:docRels},
    {name:'word/media/process-map.jpg',data:jpeg}
  ]);
}
function downloadBytes(bytes,name,type,kind='binary'){
  const check=MapliniExportCore.validateBytes(bytes,kind);
  if(!check.ok)throw new Error('Export validation failed: '+check.reason);
  const blob=new Blob([bytes],{type}),a=document.createElement('a');
  a.href=URL.createObjectURL(blob);a.download=MapliniExportCore.safeFileName(name);a.click();
  setTimeout(()=>URL.revokeObjectURL(a.href),1500);
}
async function exportPdf(){
  try{
    prepareExport();
    const shot=await renderMapSnapshot();
    const spec=pageSpec();
    const count=desiredPageCount();
    const jpeg=canvasJpegBytes(shot,.94);
    const pdf=buildMultiPagePdfFromCanvas(shot,jpeg,shot.width,shot.height,spec,count);
    downloadBytes(pdf,cleanFileName(state().name)+`_${spec.code}_${count}sidor.pdf`,'application/pdf','pdf');
    msg(`PDF skapad · ${spec.name} · ${count} sida${count>1?'or':''}`);
  }catch(err){reportRuntimeError(err,'export-pdf');msg('PDF-export misslyckades')}
}
async function exportDoc(){
  try{
    prepareExport();
    const shot=await renderMapSnapshot(),jpeg=canvasJpegBytes(shot,.94);
    const docx=buildDocxWithJpeg(jpeg,shot.width,shot.height,state().name);
    downloadBytes(docx,cleanFileName(state().name)+'.docx','application/vnd.openxmlformats-officedocument.wordprocessingml.document','zip');
    msg('DOCX skapad');
  }catch(err){reportRuntimeError(err,'export-docx');msg('DOCX-export misslyckades')}
}


selectToolBtn.addEventListener('click',()=>{
  selectionMode=!selectionMode;
  canvas.classList.toggle('p48-selection-mode',selectionMode);
  clearSelection();
  updateSelectionUi();
});
deleteSelectionBtn.addEventListener('click',deleteSelectedMany);
if(clearCanvasBtn)clearCanvasBtn.addEventListener('click',()=>{if(clearEntireCanvas()&&moreMenu)moreMenu.open=false});

canvas.addEventListener('pointerdown',e=>{
  if(!selectionMode||e.button!==0||e.target.closest('.p48-node'))return;
  e.preventDefault();finishTempArrow();
  const startPoint=clientToCanvas(e.clientX,e.clientY);
  const sx=startPoint.x,sy=startPoint.y;
  marquee.style.left=sx+'px';marquee.style.top=sy+'px';marquee.style.width='0px';marquee.style.height='0px';marquee.style.display='block';

  const move=ev=>{
    const p=clientToCanvas(ev.clientX,ev.clientY),x=p.x,y=p.y;
    const left=Math.min(sx,x),top=Math.min(sy,y),w=Math.abs(x-sx),h=Math.abs(y-sy);
    marquee.style.left=left+'px';marquee.style.top=top+'px';marquee.style.width=w+'px';marquee.style.height=h+'px';
  };
  const up=ev=>{
    document.removeEventListener('pointermove',move);document.removeEventListener('pointerup',up);document.removeEventListener('pointercancel',cancel);
    const p=clientToCanvas(ev.clientX,ev.clientY),x=p.x,y=p.y;
    const selRect=MapliniCanvasCore.normalizeRect({x:sx,y:sy},{x,y});
    const ids=[];
    for(const item of nodes.values()){
      const nr={left:item.data.x||0,top:item.data.y||0,right:(item.data.x||0)+item.el.offsetWidth,bottom:(item.data.y||0)+item.el.offsetHeight};
      if(rectsIntersect(selRect,nr))ids.push(item.data.id);
    }
    selectedLinkIndex=null;
    selectedLinkIndices=new Set(linksInSelectionRect(selRect));
    marquee.style.display='none';
    selectMany(ids);
    refreshLinkControls();
    requestFullLinkRender(true);
    updateSelectionUi();
  };
  const cancel=()=>{
    document.removeEventListener('pointermove',move);document.removeEventListener('pointerup',up);document.removeEventListener('pointercancel',cancel);
    marquee.style.display='none';
  };
  document.addEventListener('pointermove',move);document.addEventListener('pointerup',up);document.addEventListener('pointercancel',cancel);
});

document.addEventListener('pointerup',e=>{
  if(!e.target.closest || !e.target.closest('.p48-handle')) finishTempArrow();
});
document.addEventListener('keydown',e=>{
  if(e.key==='Escape'){
    if(newProcessDialog&&!newProcessDialog.hidden){e.preventDefault();setNewProcessDialog(false);return}
    if(['INPUT','TEXTAREA','SELECT'].includes(e.target.tagName)||e.target.isContentEditable)return;
    selectionMode=false;canvas.classList.remove('p48-selection-mode');marquee.style.display='none';finishTempArrow();
    if(selectedId||selectedIds.size||selectedLinkIndex!=null||selectedLinkIndices.size)clearSelection();
    else updateSelectionUi();
  }
});

function paletteInsertPoint(){
  const x=Math.max(140,scroll.scrollLeft+Math.min(Math.max(scroll.clientWidth*.5,180),720));
  const row=nodes.size%6;
  const y=150+(row*105);
  return [x,y];
}
function addFromPalette(item,{closeMobile=false}={}){
  if(!item||sharedView)return;
  const [x,y]=paletteInsertPoint();
  addNode(item.dataset.type,x,y,{objectRole:item.dataset.objectRole||null});
  if(closeMobile)setMobileTools(false);
  const paletteName=item.dataset.type==='object'?(item.dataset.objectRole==='input'?'Objekt in':'Objekt ut'):(item.dataset.type==='process'?'Aktivitet':'Steg');
  msg(`${paletteName} tillagt · markera rutan och använd Nästa för att fortsätta`);
}
if(emptyObject)emptyObject.addEventListener('click',()=>addFirstStep('object','input'));
if(emptyActivity)emptyActivity.addEventListener('click',()=>addFirstStep('process'));
root.querySelectorAll('.p48-item').forEach(i=>{
  i.addEventListener('dragstart',e=>{e.dataTransfer.setData('text/plain',JSON.stringify({type:i.dataset.type,objectRole:i.dataset.objectRole||null}));e.dataTransfer.effectAllowed='copy'});
  i.addEventListener('click',e=>{if(isMobileLayout()){e.preventDefault();addFromPalette(i,{closeMobile:true})}});
  i.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();addFromPalette(i,{closeMobile:isMobileLayout()})}});
});
canvas.addEventListener('dragover',e=>{e.preventDefault();e.dataTransfer.dropEffect='copy'});
canvas.addEventListener('drop',e=>{
  e.preventDefault();const raw=e.dataTransfer.getData('text/plain');if(!raw)return;
  let payload={type:raw,objectRole:null};try{const parsed=JSON.parse(raw);if(parsed&&parsed.type)payload=parsed}catch(_){}
  const p=clientToCanvas(e.clientX,e.clientY);addNode(payload.type,p.x,p.y,{objectRole:payload.objectRole});
});
canvas.addEventListener('click',e=>{
  if(desktopPanMoved){desktopPanMoved=false;e.preventDefault();e.stopPropagation();return}
  if(desktopPanBlankTarget(e.target)||e.target===linkLayer){
    if(!selectionMode){clearSelection();clearLinkSelection();finishTempArrow();}
  }
});
nameInput.addEventListener('change',()=>{if(!requireEdit())return;persist(false,true);msg('Namn sparat')});
root.querySelector('#p48-new').addEventListener('click',newProcess);
if(newProcessCreate)newProcessCreate.addEventListener('click',createNewProcessFromDialog);
if(newProcessCancel)newProcessCancel.addEventListener('click',()=>setNewProcessDialog(false));
if(newProcessBackdrop)newProcessBackdrop.addEventListener('click',()=>setNewProcessDialog(false));
if(newProcessName)newProcessName.addEventListener('keydown',e=>{
  if(e.key==='Enter'){e.preventDefault();createNewProcessFromDialog()}
  else if(e.key==='Escape'){e.preventDefault();setNewProcessDialog(false)}
});

root.querySelector('#p48-save').addEventListener('click',async()=>{
  if(ownerId()){
    try{
      const result=await saveCurrentToCloud();
      msg(result.localOk!==false?'Sparad lokalt och i molnet':'Sparad i molnet · lokal lagring misslyckades');
    }catch(e){
      console.error(e);reportRuntimeError(e,'cloud-save');
      const localOk=saveLocal(true);
      msg(localOk?'Sparad lokalt · molnsynk misslyckades':'Sparning misslyckades lokalt och i molnet');
    }
    return;
  }
  persist(false);
  const localOk=saveLocal(true);
  msg(localOk?'Sparad lokalt':'Lokal sparning misslyckades');
});
function closeOpenMenus(exceptTarget=null){
  root.querySelectorAll('details.p48-canvas-menu[open],details.p48-sheets-menu[open]').forEach(menu=>{
    if(!exceptTarget||!menu.contains(exceptTarget))menu.open=false;
  });
  if(shareBox&&shareBox.style.display==='block'&&(!exceptTarget||(!shareBox.contains(exceptTarget)&&exceptTarget!==shareBtn)))shareBox.style.display='none';
  if(insertLinkStepMenu&&!insertLinkStepMenu.hidden&&(!exceptTarget||!insertLinkStepWrap?.contains(exceptTarget)))setInsertStepMenu(false);
  if(nodeQuickArrange&&nodeQuickArrange.open&&(!exceptTarget||!nodeQuickArrange.contains(exceptTarget)))nodeQuickArrange.open=false;
  if(!exceptTarget)closeNodeNextMenus();else{const keep=exceptTarget.closest?exceptTarget.closest('.p48-next-step-wrap'):null;closeNodeNextMenus(keep)}
}
document.addEventListener('pointerdown',e=>closeOpenMenus(e.target),true);
window.addEventListener('blur',()=>closeOpenMenus());
root.querySelectorAll('details.p48-canvas-menu,details.p48-sheets-menu').forEach(menu=>menu.addEventListener('toggle',()=>{
  if(!menu.open)return;
  root.querySelectorAll('details.p48-canvas-menu[open],details.p48-sheets-menu[open]').forEach(other=>{if(other!==menu)other.open=false;});
}));

shareBtn.addEventListener('click',shareCurrent);copyShareBtn.addEventListener('click',async()=>{try{await navigator.clipboard.writeText(shareUrlInput.value);msg('Länk kopierad')}catch(e){try{shareUrlInput.select();const ok=document.execCommand('copy');if(!ok)throw new Error('copy command failed');msg('Länk kopierad')}catch(copyErr){reportRuntimeError(copyErr,'share-copy');msg('Kunde inte kopiera länken')}}});
loginBtn.addEventListener('click',signIn);signupBtn.addEventListener('click',signUp);logoutBtn.addEventListener('click',signOut);
setTimeout(refreshAccountSummary,0);



function refreshAccountSummary(){
  if(!accountSummaryState)return;
  const signedInNow=signedIn && !signedIn.hidden;
  accountSummaryState.textContent=signedInNow?(userEmail?.textContent||'Inloggad'):'Ej inloggad';
}
if(accountPanel)accountPanel.addEventListener('toggle',refreshAccountSummary);
if(signedOut&&signedIn&&typeof MutationObserver!=='undefined'){const accountObserver=new MutationObserver(refreshAccountSummary);accountObserver.observe(signedOut,{attributes:true,attributeFilter:['hidden']});accountObserver.observe(signedIn,{attributes:true,attributeFilter:['hidden']});}
function pageSpec(){
  const specs={
    A4P:{name:'A4 stående',code:'A4P',w:636,h:900,pdfW:595.28,pdfH:841.89},
    A4L:{name:'A4 liggande',code:'A4L',w:900,h:636,pdfW:841.89,pdfH:595.28},
    A3P:{name:'A3 stående',code:'A3P',w:794,h:1123,pdfW:841.89,pdfH:1190.55},
    A3L:{name:'A3 liggande',code:'A3L',w:1123,h:794,pdfW:1190.55,pdfH:841.89}
  };
  return specs[pdfView]||specs.A4P;
}
function contentExtent(){
  const b=exportBounds();
  if(!b)return {width:0,height:0,minX:0,minY:0,maxX:0,maxY:0};
  return b;
}
function desiredPageCount(){
  const spec=pageSpec(),b=contentExtent();
  if(pageCountMode!=='auto')return Math.max(1,parseInt(pageCountMode)||1);
  const usableW=spec.w-80;
  const pages=Math.max(1,Math.ceil((b.width||1)/usableW));
  return Math.min(8,pages);
}
function clearPrintPages(){
  canvas.querySelectorAll('.p48-print-page').forEach(x=>x.remove());
}
function updateCanvasExtentForPages(){
  const baseW=2400,baseH=1400,gap=24,left=40,top=40,margin=48;
  let requiredW=baseW,requiredH=baseH;
  if(pdfView!=='off'){
    const spec=pageSpec(),count=desiredPageCount();
    requiredW=Math.max(requiredW,left+count*spec.w+Math.max(0,count-1)*gap+margin);
    requiredH=Math.max(requiredH,top+spec.h+margin);
  }
  // Never clip manually positioned nodes when they extend beyond the default workspace.
  for(const item of nodes.values()){
    const d=item.data||{},w=item.el?.offsetWidth||Number(d.width)||180,h=item.el?.offsetHeight||Number(d.height)||80;
    requiredW=Math.max(requiredW,(Number(d.x)||0)+w+margin);
    requiredH=Math.max(requiredH,(Number(d.y)||0)+h+margin);
  }
  canvasLogicalWidth=Math.ceil(requiredW);canvasLogicalHeight=Math.ceil(requiredH);
  canvas.style.width=canvasLogicalWidth+'px';canvas.style.minWidth=canvasLogicalWidth+'px';
  canvas.style.height=canvasLogicalHeight+'px';canvas.style.minHeight=canvasLogicalHeight+'px';
  const svg=root.querySelector('#p48-svg');if(svg)svg.setAttribute('viewBox',`0 0 ${canvasLogicalWidth} ${canvasLogicalHeight}`);
  const wrap=canvas.parentElement;if(wrap){
    wrap.style.setProperty('--p48-canvas-visual-width',(canvasLogicalWidth*canvasScale)+'px');
    wrap.style.setProperty('--p48-canvas-visual-height',(canvasLogicalHeight*canvasScale)+'px');
  }
  scheduleHorizontalNavSync();
}
function renderPrintPages(){
  clearPrintPages();
  updateCanvasExtentForPages();
  if(pdfView==='off')return;
  const spec=pageSpec(),count=desiredPageCount(),gap=24,left=40,top=40;
  for(let i=0;i<count;i++){
    const pg=document.createElement('div');pg.className='p48-print-page';
    pg.dataset.label=`${spec.name} · sida ${i+1}/${count}`;
    pg.style.left=(left+i*(spec.w+gap))+'px';pg.style.top=top+'px';
    pg.style.width=spec.w+'px';pg.style.height=spec.h+'px';
    canvas.appendChild(pg);
  }
  if(typeof refreshPageQuickUi==='function')refreshPageQuickUi();
}
function refreshPageQuickUi(){
  if(pdfViewSelect&&pdfViewSelect.value!==pdfView)pdfViewSelect.value=pdfView;
  if(pageFormatQuick&&pageFormatQuick.value!==pdfView)pageFormatQuick.value=pdfView;
  if(pageCountSelect&&pageCountSelect.value!==String(pageCountMode))pageCountSelect.value=String(pageCountMode);
  if(pageCountQuick&&pageCountQuick.value!==String(pageCountMode))pageCountQuick.value=String(pageCountMode);
  if(pageQuickSummary){
    const format=pdfView==='off'?'Ingen sidyta':pageSpec().name;
    const count=pageCountMode==='auto'?'Auto':`${desiredPageCount()} ${desiredPageCount()===1?'sida':'sidor'}`;
    pageQuickSummary.textContent=pdfView==='off'?`${format} ▾`:`${format} · ${count} ▾`;
  }
}
function applyPageSettings(nextView,nextCount){
  pdfView=String(nextView||pdfView);
  pageCountMode=String(nextCount||pageCountMode);
  renderPrintPages();refreshPageQuickUi();
}
pdfViewSelect.addEventListener('change',()=>applyPageSettings(pdfViewSelect.value,pageCountMode));
pageCountSelect.addEventListener('change',()=>applyPageSettings(pdfView,pageCountSelect.value));
if(pageFormatQuick)pageFormatQuick.addEventListener('change',()=>applyPageSettings(pageFormatQuick.value,pageCountMode));
if(pageCountQuick)pageCountQuick.addEventListener('change',()=>applyPageSettings(pdfView,pageCountQuick.value));
if(pageQuick)pageQuick.addEventListener('toggle',()=>{if(pageQuick.open)refreshPageQuickUi()});
refreshPageQuickUi();
function directGoogleSheetPayload(){
  persist();
  const st=state();
  const ordered=[...nodes.values()].map(x=>x.data).sort((a,b)=>((a.y||0)-(b.y||0))||((a.x||0)-(b.x||0)));
  const byId=new Map(ordered.map(n=>[n.id,n]));
  const step_rows=ordered.map((d,i)=>[
    i+1,d.id||'',typeLabel(d.type),d.text||'',d.type==='document'?(d.documentUrl||''):'',
    Array.isArray(d.inputs)?d.inputs.filter(Boolean).join(' | '):'',
    Array.isArray(d.outputs)?d.outputs.filter(Boolean).join(' | '):'',
    links.filter(l=>l[0]===d.id).map(l=>byId.get(l[1])?.text||l[1]).join(' | '),
    links.filter(l=>l[1]===d.id).map(l=>byId.get(l[0])?.text||l[0]).join(' | '),
    d.x||0,d.y||0,d.width||'',d.height||''
  ]);
  const link_rows=(st.links||[]).map(l=>[l[0],byId.get(l[0])?.text||'',l[1],byId.get(l[1])?.text||'',l[2]||'right']);
  return {title:st.name,step_rows,link_rows};
}
function createGoogleSheetDirect(){
  try{
    const url=new URL(window.parent.location.href);
    url.searchParams.set('gs_payload',JSON.stringify(directGoogleSheetPayload()));
    window.parent.location.href=url.toString();
  }catch(e){console.error(e);reportRuntimeError(e,'google-sheets-direct');msg('Kunde inte starta Google Sheets-export')}
}

root.querySelector('#p48-pdf').addEventListener('click',exportPdf);root.querySelector('#p48-doc').addEventListener('click',exportDoc);root.querySelector('#p48-sheets').addEventListener('click',exportGoogleSheets);root.querySelector('#p48-sheets-direct').addEventListener('click',createGoogleSheetDirect);
const sheetsMenu=root.querySelector('.p48-sheets-menu');
root.querySelector('#p48-sheets').addEventListener('click',()=>{if(sheetsMenu)sheetsMenu.open=false;});
root.querySelector('#p48-sheets-direct').addEventListener('click',()=>{if(sheetsMenu)sheetsMenu.open=false;});
root.querySelector('#p48-undo').addEventListener('click',()=>{if(!requireEdit())return;if(!undo.length)return;redo.push(JSON.stringify(state()));restore(undo.pop());refreshControls();refreshLinkControls();updateSelectionUi();persist()});
root.querySelector('#p48-redo').addEventListener('click',()=>{if(!requireEdit())return;if(!redo.length)return;undo.push(JSON.stringify(state()));restore(redo.pop());refreshControls();refreshLinkControls();updateSelectionUi();persist()});
if(duplicateSelectionBtn)duplicateSelectionBtn.addEventListener('click',duplicateSelectedNodes);
root.addEventListener('keydown',e=>{
  if(['INPUT','TEXTAREA','SELECT'].includes(e.target.tagName)||e.target.isContentEditable)return;
  const mod=e.ctrlKey||e.metaKey,key=e.key.toLowerCase();
  if(e.key==='Escape'){
    const had=MapliniSelectionCore.hasAny({selectedId,selectedIds:[...selectedIds],selectedLinkIndex,selectedLinkIndices:[...selectedLinkIndices]});
    selectionMode=false;canvas.classList.remove('p48-selection-mode');marquee.style.display='none';finishTempArrow();
    if(had){e.preventDefault();clearSelection()}
    return;
  }
  if(mod&&key==='z'){if(!canEdit())return;e.preventDefault();if(e.shiftKey){if(redo.length){undo.push(JSON.stringify(state()));restore(redo.pop());refreshControls();refreshLinkControls();updateSelectionUi();persist()}}else if(undo.length){redo.push(JSON.stringify(state()));restore(undo.pop());refreshControls();refreshLinkControls();updateSelectionUi();persist()}return}
  if(mod&&key==='y'){if(!canEdit())return;e.preventDefault();if(redo.length){undo.push(JSON.stringify(state()));restore(redo.pop());refreshControls();refreshLinkControls();updateSelectionUi();persist()}return}
  if(mod&&key==='c'){e.preventDefault();copySelectedNodes();return}
  if(mod&&key==='v'){if(!canEdit())return;e.preventDefault();pasteEditingClipboard();return}
  if(mod&&key==='d'){if(!canEdit())return;e.preventDefault();duplicateSelectedNodes();return}
  if(e.key==='Delete'||e.key==='Backspace'){if(!canEdit())return;
    const action=MapliniSelectionCore.deleteAction({selectedId,selectedIds:[...selectedIds],selectedLinkIndex,selectedLinkIndices:[...selectedLinkIndices]});
    if(action==='many'||action==='node'){e.preventDefault();deleteSelectedMany()}
    else if(action==='link'){e.preventDefault();deleteLinkAt(selectedLinkIndex!=null?selectedLinkIndex:[...selectedLinkIndices][0],true)}
  }
});
font.addEventListener('change',()=>updateStyle({fontFamily:font.value}));
fontAllBtn.addEventListener('click',()=>{
  if(!requireEdit())return;
  if(!nodes.size)return;
  const globalFont=font.value;
  const globalSize=Math.max(10,Math.min(36,Number(size.value)||13));
  pushUndo();
  for(const item of nodes.values()){
    item.data.fontFamily=globalFont;
    item.data.fontSize=globalSize;
    applyStyle(item);
    renderNodeIO(item);
    renderDocumentLink(item);
  }
  persist();
  refreshControls();
  msg('Typsnitt och storlek uppdaterat på all text');
});
nodeStyleSelect.addEventListener('change',()=>updateStyle({nodeStyle:nodeStyleSelect.value}));
nodeStyleAllBtn.addEventListener('click',()=>{
  if(!requireEdit())return;
  if(!nodes.size)return;
  const chosen=nodeStyleSelect.value;
  pushUndo();
  for(const item of nodes.values()){
    item.data.nodeStyle=chosen;
    applyStyle(item);
  }
  drawLinks();persist();refreshControls();
  msg('Rutstil uppdaterad på alla rutor');
});

pointSize.addEventListener('change',()=>{
  if(!requireEdit())return;
  connectorPointSize=Number(pointSize.value)||8;
  applyConnectorPointSettings();
  persist();
});
pointColor.addEventListener('input',()=>{
  if(!requireEdit())return;
  connectorPointColor=pointColor.value;
  applyConnectorPointSettings();
  persist();
});
hidePoints.addEventListener('change',()=>{
  if(!requireEdit())return;
  connectorPointsHidden=hidePoints.checked;
  applyConnectorPointSettings();
  persist();
});

canvasBg.addEventListener('input',()=>{
  if(!requireEdit())return;
  processBackground=canvasBg.value;applyProcessStyle();persistAfterIdle();
});
bgType.addEventListener('change',()=>{
  if(!requireEdit())return;
  processBackgroundType=bgType.value;applyProcessStyle();persistAfterIdle();
});
bgPatternColor.addEventListener('input',()=>{
  if(!requireEdit())return;
  processPatternColor=bgPatternColor.value;applyProcessStyle();persistAfterIdle();
});
bgDensity.addEventListener('change',()=>{
  if(!requireEdit())return;
  processPatternDensity=Number(bgDensity.value)||20;applyProcessStyle();persistAfterIdle();
});

gradientStart.addEventListener('input',()=>{if(!requireEdit())return;processGradientStart=gradientStart.value;applyProcessStyle();persistAfterIdle();});
gradientEnd.addEventListener('input',()=>{if(!requireEdit())return;processGradientEnd=gradientEnd.value;applyProcessStyle();persistAfterIdle();});
gradientAngle.addEventListener('change',()=>{if(!requireEdit())return;processGradientAngle=Number(gradientAngle.value)||0;applyProcessStyle();persistAfterIdle();});
bgImageOpacity.addEventListener('input',()=>{if(!requireEdit())return;processBackgroundImageOpacity=Math.max(.05,Math.min(1,Number(bgImageOpacity.value)/100));applyProcessStyle();persistAfterIdle();});
bgImageRemove.addEventListener('click',()=>{if(!requireEdit())return;processBackgroundImageData='';bgImageFile.value='';applyProcessStyle();persistAfterIdle();msg('Bakgrundsbild borttagen');});
bgImageFile.addEventListener('change',()=>{
  if(!requireEdit())return;
  const file=bgImageFile.files&&bgImageFile.files[0];if(!file)return;
  if(!/^image\/(png|jpeg|webp)$/.test(file.type)){msg('Välj PNG, JPG eller WebP');return}
  if(file.size>1500000){msg('Bakgrundsbilden får vara max 1,5 MB');bgImageFile.value='';return}
  const reader=new FileReader();
  reader.onload=()=>{if(!canEdit())return;processBackgroundImageData=String(reader.result||'');processBackgroundType='image';applyProcessStyle(true);persistAfterIdle();msg('Bakgrundsbild tillagd')};
  reader.readAsDataURL(file);
});
watermarkText.addEventListener('input',()=>{if(!requireEdit())return;processWatermarkText=watermarkText.value.slice(0,80);applyProcessStyle();persistAfterIdle();});
watermarkUseLogo.addEventListener('change',()=>{if(!requireEdit())return;processWatermarkUseLogo=watermarkUseLogo.checked;applyProcessStyle();persistAfterIdle();});
watermarkOpacity.addEventListener('input',()=>{if(!requireEdit())return;processWatermarkOpacity=Math.max(.05,Math.min(.4,Number(watermarkOpacity.value)/100));applyProcessStyle();persistAfterIdle();});


processLogo.addEventListener('pointerdown',e=>{
  if(!canEdit()||!processLogoData||processLogoHidden||e.button!==0)return;
  e.preventDefault();e.stopPropagation();
  clearSelection();
  processLogo.classList.add('selected');
  const pointerId=e.pointerId;
  try{processLogo.setPointerCapture(pointerId)}catch(ignore){}
  const start=clientToCanvas(e.clientX,e.clientY);
  const startX=processLogoX,startY=processLogoY;
  let mutated=false;
  const move=ev=>{
    if(ev.pointerId!==pointerId)return;
    if(!canEdit()){finish(ev,true);return}
    const p=clientToCanvas(ev.clientX,ev.clientY);
    const dx=p.x-start.x,dy=p.y-start.y;
    if(!mutated&&MapliniCanvasCore.hasMeaningfulDelta(dx,dy)){pushUndo(true);mutated=true}
    if(!mutated)return;
    processLogoX=Math.max(0,Math.min(canvas.scrollWidth-processLogo.offsetWidth,startX+dx));
    processLogoY=Math.max(0,Math.min(canvas.scrollHeight-processLogo.offsetHeight,startY+dy));
    processLogo.style.left=processLogoX+'px';
    processLogo.style.top=processLogoY+'px';
  };
  const finish=(ev,cancelled=false)=>{
    document.removeEventListener('pointermove',move);
    document.removeEventListener('pointerup',up);
    document.removeEventListener('pointercancel',cancel);
    try{processLogo.releasePointerCapture(pointerId)}catch(ignore){}
    if(cancelled&&!canEdit()){
      processLogoX=startX;processLogoY=startY;
      processLogo.style.left=processLogoX+'px';processLogo.style.top=processLogoY+'px';
    }else if(mutated){
      lastProcessStyleSignature='';
      persist();
      msg('Logotyp flyttad');
    }
  };
  const up=ev=>{if(ev.pointerId===pointerId)finish(ev,false)};
  const cancel=ev=>{if(ev.pointerId===pointerId)finish(ev,true)};
  document.addEventListener('pointermove',move);
  document.addEventListener('pointerup',up);
  document.addEventListener('pointercancel',cancel);
});
canvas.addEventListener('pointerdown',e=>{
  if(e.target!==processLogo)processLogo.classList.remove('selected');
});

logoSize.addEventListener('change',()=>{
  if(!requireEdit())return;
  processLogoWidth=Number(logoSize.value)||180;
  applyProcessStyle();persistAfterIdle();
});
logoHide.addEventListener('change',()=>{
  if(!requireEdit())return;
  processLogoHidden=logoHide.checked;
  applyProcessStyle();persistAfterIdle();
});
logoRemove.addEventListener('click',()=>{
  if(!requireEdit())return;
  processLogoData='';
  processLogoHidden=false;
  processLogoX=28;processLogoY=28;
  processLogo.classList.remove('selected');
  logoFile.value='';
  applyProcessStyle();persistAfterIdle();
  msg('Logotype borttagen');
});
logoFile.addEventListener('change',()=>{
  if(!requireEdit())return;
  const file=logoFile.files&&logoFile.files[0];
  if(!file)return;
  if(!/^image\/(png|jpeg|webp)$/.test(file.type)){msg('Välj PNG, JPG eller WebP');return}
  const reader=new FileReader();
  reader.onload=()=>{
    if(!canEdit()){logoFile.value='';msg('Endast visning');return}
    processLogoData=String(reader.result||'');
    processLogoHidden=false;
    applyProcessStyle();persistAfterIdle();
    msg('Logotype tillagd');
  };
  reader.readAsDataURL(file);
});

size.addEventListener('change',()=>updateStyle({fontSize:Math.max(10,Math.min(36,Number(size.value)||13))}));textColor.addEventListener('change',()=>updateStyle({textColor:textColor.value}));bgColor.addEventListener('change',()=>updateStyle({bgColor:bgColor.value}));borderColor.addEventListener('change',()=>{
  if(!requireEdit())return;
  if(selectedLinkIndex!=null){
    pushUndo();
    setLinkStyle(selectedLinkIndex,{color:borderColor.value});
    drawLinks();persist();refreshLinkControls();
    return;
  }
  updateStyle({borderColor:borderColor.value});
});
borderWidth.addEventListener('change',()=>{
  if(!requireEdit())return;
  if(selectedLinkIndex!=null){
    pushUndo();
    setLinkStyle(selectedLinkIndex,{width:Number(borderWidth.value)});
    drawLinks();persist();refreshLinkControls();
    return;
  }
  updateStyle({borderWidth:Number(borderWidth.value)});
});
bold.addEventListener('click',()=>{const items=selectedNodeItems();if(items.length)updateStyle({fontWeight:items.every(x=>styleOf(x.data).fontWeight==='700')?'400':'700'})});italic.addEventListener('click',()=>{const items=selectedNodeItems();if(items.length)updateStyle({fontStyle:items.every(x=>styleOf(x.data).fontStyle==='italic')?'normal':'italic'})});under.addEventListener('click',()=>{const items=selectedNodeItems();if(items.length)updateStyle({textDecoration:items.every(x=>styleOf(x.data).textDecoration==='underline')?'none':'underline'})});root.querySelectorAll('[data-text-align]').forEach(b=>b.addEventListener('click',()=>updateStyle({textAlign:b.dataset.textAlign})));



documentUrlInput.addEventListener('change',()=>{
  if(!requireEdit())return;
  const item=selectedId?nodes.get(selectedId):null;
  if(!item||item.data.type!=='document')return;
  const raw=documentUrlInput.value.trim();
  if(raw&&!safeDocumentUrl(raw)){msg('Dokumentlänken måste börja med http:// eller https://');documentUrlInput.value=item.data.documentUrl||'';return}
  pushUndo();
  item.data.documentUrl=raw;
  renderDocumentLink(item);
  const valid=safeDocumentUrl(raw);if(documentOpenEditor){documentOpenEditor.hidden=!valid;if(valid)documentOpenEditor.href=valid;else documentOpenEditor.removeAttribute('href');}
  persist();
  msg(raw?'Dokumentlänk sparad':'Dokumentlänk borttagen');
});
addInputBtn.addEventListener('click',()=>{if(!requireEdit())return;const item=selectedId?nodes.get(selectedId):null;if(!item)return;pushUndo();ensureIO(item);item.data.inputs.push('Ny input');renderNodeIO(item);persist();refreshControls();});
addOutputBtn.addEventListener('click',()=>{if(!requireEdit())return;const item=selectedId?nodes.get(selectedId):null;if(!item)return;pushUndo();ensureIO(item);item.data.outputs.push('Ny output');renderNodeIO(item);persist();refreshControls();});

deleteNodeBtn.addEventListener('click',()=>deleteSelected());
linkColor.addEventListener('input',()=>{
  if(!requireEdit())return;
  if(selectedLinkIndex==null){msg('Markera först en pil');return}
  pushUndo();
  setLinkStyle(selectedLinkIndex,{color:linkColor.value});
  drawLinks(true);
  persist();
  msg('Pilfärg ändrad');
});
if(linkWidth)linkWidth.addEventListener('change',()=>{
  if(!requireEdit())return;
  if(selectedLinkIndex==null){msg('Markera först en koppling');return}
  const width=Math.max(1,Math.min(6,Number(linkWidth.value)||2));
  pushUndo();setLinkStyle(selectedLinkIndex,{width});
  dirtyLinks.add(selectedLinkIndex);drawLinks();persist();refreshLinkControls();
  msg('Piltjocklek ändrad');
});
linkEnd.addEventListener('change',()=>{
  if(!requireEdit())return;
  if(selectedLinkIndex==null){msg('Markera först en koppling');return}
  pushUndo();
  setLinkStyle(selectedLinkIndex,{end:String(linkEnd.value)});
  dirtyLinks.add(selectedLinkIndex);drawLinks();persist();refreshLinkControls();
  msg('Slutmarkör ändrad');
});
linkDash.addEventListener('change',()=>{
  if(!requireEdit())return;
  if(selectedLinkIndex==null){msg('Markera först en koppling');return}
  pushUndo();
  setLinkStyle(selectedLinkIndex,{dash:String(linkDash.value)});
  dirtyLinks.add(selectedLinkIndex);drawLinks();persist();refreshLinkControls();
  msg('Linjetyp ändrad');
});
function applySelectedLinkRouting(routing){
  if(!requireEdit())return false;if(selectedLinkIndex==null){msg('Markera först en koppling');return false}
  routing=['orthogonal','straight','free'].includes(String(routing))?String(routing):'straight';
  const current=linkStyle(links[selectedLinkIndex]).routing||'straight';
  if(current===routing){refreshLinkControls();return true}
  pushUndo();
  const patch=routing==='straight'
    ?{routing,viaX:null,viaY:null,freeDx:0,freeDy:0}
    :(routing==='orthogonal'?{routing,freeDx:0,freeDy:0}:{routing,viaX:null,viaY:null});
  setLinkStyle(selectedLinkIndex,patch);dirtyLinks.add(selectedLinkIndex);drawLinks();persist();refreshLinkControls();
  msg(routing==='straight'?'Pilen är nu rak':(routing==='orthogonal'?'Pilen är nu vinkelrät':'Pilen kan nu flyttas fritt'));
  return true;
}
linkRouting.addEventListener('change',()=>applySelectedLinkRouting(linkRouting.value));
linkQuickRouting.forEach(btn=>{
  btn.addEventListener('pointerdown',e=>{e.preventDefault();e.stopPropagation()});
  btn.addEventListener('click',e=>{e.preventDefault();e.stopPropagation();applySelectedLinkRouting(btn.dataset.linkRouting)});
});
linkAnchorMode.addEventListener('change',()=>{
  if(!requireEdit())return;if(selectedLinkIndex==null){msg('Markera först en koppling');return}
  pushUndo();setLinkStyle(selectedLinkIndex,{anchorMode:String(linkAnchorMode.value)});dirtyLinks.add(selectedLinkIndex);drawLinks();persist();refreshLinkControls();msg('Fästpunkter ändrade');
});
let linkLabelEditIndex=null,linkLabelUndoTaken=false;
linkLabel.addEventListener('focus',()=>{
  linkLabelEditIndex=selectedLinkIndex;linkLabelUndoTaken=false;
});
linkLabel.addEventListener('input',()=>{
  if(!requireEdit())return;
  if(selectedLinkIndex==null||linkLabelEditIndex!==selectedLinkIndex)return;
  const value=String(linkLabel.value||'').slice(0,60);
  const current=String(linkStyle(links[selectedLinkIndex]).label||'');
  if(value===current)return;
  if(!linkLabelUndoTaken){pushUndo(true);linkLabelUndoTaken=true}
  setLinkStyle(selectedLinkIndex,{label:value});
  dirtyLinks.add(selectedLinkIndex);drawLinks();persistAfterIdle();
});
linkLabel.addEventListener('blur',()=>{
  if(selectedLinkIndex==null||linkLabelEditIndex!==selectedLinkIndex){linkLabelEditIndex=null;linkLabelUndoTaken=false;return}
  const value=String(linkLabel.value||'').trim().slice(0,60);
  setLinkStyle(selectedLinkIndex,{label:value});linkLabel.value=value;
  dirtyLinks.add(selectedLinkIndex);drawLinks();persist();refreshLinkControls();
  if(linkLabelUndoTaken)msg(value?'Piltext sparad':'Piltext borttagen');
  linkLabelEditIndex=null;linkLabelUndoTaken=false;
});
if(insertLinkStepBtn)insertLinkStepBtn.addEventListener('click',e=>{e.preventDefault();e.stopPropagation();setInsertStepMenu(insertLinkStepMenu?.hidden!==false)});
insertLinkStepChoices.forEach(btn=>btn.addEventListener('click',e=>{e.preventDefault();e.stopPropagation();insertStepOnSelectedLink(btn.dataset.insertType)}));
if(flowCoachInsert)flowCoachInsert.addEventListener('click',e=>{
  e.preventDefault();e.stopPropagation();
  if(selectedLinkIndex!=null&&isDirectActivityLink(selectedLinkIndex))insertStepOnSelectedLink('object');
});
if(flowCoachKeep)flowCoachKeep.addEventListener('click',e=>{
  e.preventDefault();e.stopPropagation();
  if(selectedLinkIndex==null||!links[selectedLinkIndex])return;
  pushUndo(true);setLinkStyle(selectedLinkIndex,{methodOverride:'direct_activity_ok'});persist();refreshFlowCoach();
  msg('Direktkopplingen behålls och markeras som avsiktlig');
});
linkLabel.addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();linkLabel.blur()}});
deleteLinkBtn.addEventListener('click',()=>{if(deleteLinkAt(selectedLinkIndex,true))msg('Koppling borttagen')});
linkHandle.addEventListener('pointerdown',e=>{if(selectedLinkIndex==null)return;startSelectedLinkDrag(selectedLinkIndex,e)});


function focusAnalysisNodes(ids){
  const valid=(Array.isArray(ids)?ids:[]).filter(id=>nodes.has(String(id))).map(String);if(!valid.length)return false;
  selectMany(valid);
  let left=Infinity,top=Infinity,right=-Infinity,bottom=-Infinity;for(const id of valid){const item=nodes.get(id);if(!item)continue;const x=Number(item.data.x)||0,y=Number(item.data.y)||0,w=item.el.offsetWidth||180,h=item.el.offsetHeight||76;left=Math.min(left,x);top=Math.min(top,y);right=Math.max(right,x+w);bottom=Math.max(bottom,y+h)}
  if(Number.isFinite(left)){const cx=(left+right)/2,cy=(top+bottom)/2;scroll.scrollLeft=Math.max(0,cx*canvasScale-scroll.clientWidth/2);scroll.scrollTop=Math.max(0,cy*canvasScale-scroll.clientHeight/2);if(hnav)hnav.scrollLeft=scroll.scrollLeft}
  return true;
}
function renderProcessAnalysis(result){
  if(!analysisPanel||!analysisList)return;analysisPanel.hidden=false;
  if(analysisScore)analysisScore.textContent=(Number(result.score)||0).toFixed(1)+'/10';
  if(analysisErrors)analysisErrors.textContent=String(result.counts.error||0);
  if(analysisWarnings)analysisWarnings.textContent=String(result.counts.warning||0);
  if(analysisInfo)analysisInfo.textContent=String(result.counts.info||0);
  analysisList.innerHTML='';

  const first=result.findings&&result.findings.length?result.findings[0]:null;
  if(analysisNext){
    analysisNext.hidden=!first;
    if(first){
      if(analysisNextTitle)analysisNextTitle.textContent=first.title;
      if(analysisNextAction)analysisNextAction.textContent=first.action||first.detail||'Kontrollera flödet.';
      if(analysisNextShow){
        const canShow=Array.isArray(first.nodeIds)&&first.nodeIds.length>0;
        analysisNextShow.hidden=!canShow;
        analysisNextShow.onclick=canShow?()=>focusAnalysisNodes(first.nodeIds):null;
      }
    }
  }

  if(!result.findings.length){
    const empty=document.createElement('div');empty.className='p48-analysis-empty';
    empty.innerHTML='<strong>Processen ser strukturellt tydlig ut.</strong><span>Maplini hittade inga brutna flöden, saknade start-/slutpunkter eller andra strukturella problem.</span>';
    analysisList.appendChild(empty);return;
  }

  for(const f of result.findings){
    const item=document.createElement('div');item.className='p48-analysis-item '+f.severity;
    const head=document.createElement('div');head.className='p48-analysis-item-head';
    const badge=document.createElement('span');badge.className='p48-analysis-priority '+f.severity;badge.textContent=f.priority||'Kontrollera';
    const title=document.createElement('div');title.className='p48-analysis-item-title';title.textContent=f.title;
    head.append(badge,title);
    const detail=document.createElement('div');detail.className='p48-analysis-item-detail';detail.textContent=f.detail;
    const fix=document.createElement('div');fix.className='p48-analysis-item-fix';
    const fixLabel=document.createElement('strong');fixLabel.textContent='Gör så här:';
    const fixText=document.createElement('span');fixText.textContent=f.action||'Kontrollera flödet.';
    fix.append(fixLabel,fixText);
    item.append(head,detail,fix);
    if(f.nodeIds.length){
      const action=document.createElement('button');action.type='button';action.className='p48-analysis-item-action';
      action.textContent=f.nodeIds.length===1?'Visa berörd ruta →':`Visa ${f.nodeIds.length} berörda rutor →`;
      action.addEventListener('click',()=>focusAnalysisNodes(f.nodeIds));item.appendChild(action);
    }
    if(f.code==='direct_activity'&&Number.isInteger(f.meta?.linkIndex)&&links[f.meta.linkIndex]){
      const fixNow=document.createElement('button');fixNow.type='button';fixNow.className='p48-btn primary';fixNow.style.marginTop='7px';
      fixNow.textContent='＋ Infoga Objekt / resultat';
      fixNow.addEventListener('click',()=>{
        analysisPanel.hidden=true;selectLink(f.meta.linkIndex,true);insertStepOnSelectedLink('object');
      });
      item.appendChild(fixNow);
    }
    analysisList.appendChild(item);
  }
}
function runProcessAnalysis(){
  const data=[...nodes.values()].map(x=>x.data);const result=MapliniProcessIntelligenceCore.analyze(data,links,{longChainThreshold:5});renderProcessAnalysis(result);msg(result.findings.length?`Processkontroll klar · ${result.findings.length} saker att gå igenom`:'Processkontroll klar · inga strukturella problem hittades');return result;
}
if(analyzeBtn)analyzeBtn.addEventListener('click',runProcessAnalysis);if(analysisClose)analysisClose.addEventListener('click',()=>{analysisPanel.hidden=true});

function selectedNodeRects(ids){
  const wanted=ids?new Set(ids):null,out=[];
  for(const item of nodes.values()){
    if(wanted&&!wanted.has(item.data.id))continue;
    out.push({id:item.data.id,x:Number(item.data.x)||0,y:Number(item.data.y)||0,width:item.el.offsetWidth||Number(item.data.width)||180,height:item.el.offsetHeight||Number(item.data.height)||76});
  }
  return out;
}

function scaleWholeProcess(factor,fitToPage=false,recordHistory=true){
  if(!requireEdit())return false;
  const items=[...nodes.values()];
  if(!items.length){msg('Processen har inga rutor att skala');return false}
  const rects=selectedNodeRects([...nodes.keys()]);
  let minX=Math.min(...rects.map(r=>r.x)),minY=Math.min(...rects.map(r=>r.y));
  let maxX=Math.max(...rects.map(r=>r.x+r.width)),maxY=Math.max(...rects.map(r=>r.y+r.height));
  let actualFactor=Number(factor)||1;
  if(fitToPage){
    if(pdfView==='off'){msg('Välj A4 eller A3 först');return false}
    const spec=pageSpec(),margin=54;
    const availW=Math.max(100,spec.w-margin*2),availH=Math.max(100,spec.h-margin*2);
    const contentW=Math.max(1,maxX-minX),contentH=Math.max(1,maxY-minY);
    actualFactor=Math.min(availW/contentW,availH/contentH);
    actualFactor=Math.max(.35,Math.min(1.75,actualFactor));
  }
  if(Math.abs(actualFactor-1)<.005){msg('Processen har redan rätt storlek');return false}
  if(recordHistory)pushUndo(true);
  const anchorX=fitToPage?54:minX,anchorY=fitToPage?54:minY;
  for(const item of items){
    const d=item.data||{},el=item.el;
    const x=Number(d.x)||parseFloat(el.style.left)||0,y=Number(d.y)||parseFloat(el.style.top)||0;
    const w=Math.max(56,Number(d.width)||el.offsetWidth||180),h=Math.max(34,Number(d.height)||el.offsetHeight||70);
    const sx=anchorX+(x-minX)*actualFactor,sy=anchorY+(y-minY)*actualFactor;
    const sw=Math.max(56,w*actualFactor),sh=Math.max(34,h*actualFactor);
    d.x=sx;d.y=sy;d.width=sw;d.height=sh;
    el.style.left=sx+'px';el.style.top=sy+'px';
    /* CSS min/max sizes used to stop the visible node from shrinking/growing with process scale.
       Inline geometry owns the dimensions after scaling. */
    el.style.boxSizing='border-box';el.style.minWidth='0px';el.style.maxWidth='none';el.style.minHeight='0px';
    el.style.width=sw+'px';el.style.height=sh+'px';
    if(d.type==='decision')el.style.padding=Math.max(12,38*actualFactor)+'px';
    else if(d.type==='object')el.style.padding=`${Math.max(5,10*actualFactor)}px ${Math.max(8,14*actualFactor)}px`;
    else el.style.padding=`${Math.max(7,14*actualFactor)}px ${Math.max(10,26*actualFactor)}px`;
    d.fontSize=Math.max(8,Math.min(40,(Number(styleOf(d).fontSize)||13)*actualFactor));
    sync(el);applyStyle(item);invalidateNodeGeom(item.data.id);markNodeLinksDirty(item.data.id);
  }
  // Scale manual connector breakpoints around the same origin.
  for(let i=0;i<links.length;i++){
    const s=linkStyle(i);
    const patch={};
    if(Number.isFinite(Number(s.viaX)))patch.viaX=anchorX+(Number(s.viaX)-minX)*actualFactor;
    if(Number.isFinite(Number(s.viaY)))patch.viaY=anchorY+(Number(s.viaY)-minY)*actualFactor;
    if(s.routing==='free'){
      patch.freeDx=(Number(s.freeDx)||0)*actualFactor;
      patch.freeDy=(Number(s.freeDy)||0)*actualFactor;
    }
    if(Object.keys(patch).length)setLinkStyle(i,patch);
  }
  updateCanvasExtentForPages();requestFullLinkRender(true);drawLinks();persist();refreshControls();updateSelectionUi();
  if(fitToPage){
    processScalePercent=100;
    if(processScaleSlider)processScaleSlider.value='100';
    if(processScaleValue)processScaleValue.textContent='100 %';
  }
  msg(fitToPage?`Processen anpassades till ${pageSpec().name}`:`Processens storlek ändrad`);
  return true;
}
function fitProcessToScreen(){
  const rects=selectedNodeRects();if(!rects.length){msg('Processen har inga rutor att anpassa');return false}
  const result=MapliniEditingCore.fitToScreen(rects,{width:scroll.clientWidth,height:scroll.clientHeight},{margin:64,minScale:.25,maxScale:1.5});if(!result)return false;
  applyCanvasScale(result.scale,false);
  requestAnimationFrame(()=>{scroll.scrollLeft=result.scrollLeft;scroll.scrollTop=result.scrollTop;if(hnav)hnav.scrollLeft=scroll.scrollLeft;scheduleHorizontalNavSync()});
  msg(`Anpassad till ${Math.round(result.scale*100)}%`);return true;
}
function applyNodePositions(positionMap,label,recordHistory=true){
  if(!requireEdit())return false;if(!positionMap||!Object.keys(positionMap).length)return false;
  if(recordHistory)pushUndo(true);
  for(const [id,pos] of Object.entries(positionMap)){
    const item=nodes.get(id);if(!item)continue;
    item.el.style.left=Number(pos.x)+'px';item.el.style.top=Number(pos.y)+'px';sync(item.el);invalidateNodeGeom(id);markNodeLinksDirty(id);
  }
  drawLinks();persist();refreshControls();updateSelectionUi();msg(label);return true;
}
function alignSelected(mode){
  if(selectedIds.size<2){msg('Markera minst två rutor');return false}
  return applyNodePositions(MapliniEditingCore.alignNodes(selectedNodeRects([...selectedIds]),mode),'Markerade rutor justerade');
}
function distributeSelected(axis){
  if(selectedIds.size<3){msg('Markera minst tre rutor för att fördela');return false}
  return applyNodePositions(MapliniEditingCore.distributeNodes(selectedNodeRects([...selectedIds]),axis),'Markerade rutor fördelade jämnt');
}
function preferredLayoutOrientation(ids=[...nodes.keys()]){
  const wanted=new Set((ids||[]).map(String));
  let horizontalWeight=0,verticalWeight=0,usable=0;
  for(const l of links){
    if(!Array.isArray(l)||!wanted.has(String(l[0]))||!wanted.has(String(l[1])))continue;
    const A=nodes.get(String(l[0]))?.el,B=nodes.get(String(l[1]))?.el;if(!A||!B)continue;
    const [ax,ay]=center(A),[bx,by]=center(B),dx=Math.abs(bx-ax),dy=Math.abs(by-ay);
    if(dx<2&&dy<2)continue;
    horizontalWeight+=dx;verticalWeight+=dy;usable++;
  }
  if(usable)return verticalWeight>horizontalWeight*1.15?'vertical':'horizontal';
  const rects=selectedNodeRects(ids);if(!rects.length)return'horizontal';
  const left=Math.min(...rects.map(r=>r.x)),right=Math.max(...rects.map(r=>r.x+r.width));
  const top=Math.min(...rects.map(r=>r.y)),bottom=Math.max(...rects.map(r=>r.y+r.height));
  return (bottom-top)>(right-left)*1.2?'vertical':'horizontal';
}
function autoCleanProcess(){
  if(!requireEdit())return false;
  const ids=[...nodes.keys()];
  if(ids.length<2){msg('Processen behöver minst två rutor');return false}
  const orientation=preferredLayoutOrientation(ids);
  const ok=smartLayout('all',orientation);
  if(ok)msg(`Processen ordnades automatiskt · ${orientation==='horizontal'?'vänster → höger':'uppifrån ↓'}`);
  return ok;
}
function smartLayout(scope,orientation){
  if(!requireEdit())return false;
  const ids=scope==='selected'?[...selectedIds]:[...nodes.keys()];
  if(ids.length<2){msg(scope==='selected'?'Markera minst två rutor':'Processen behöver minst två rutor');return false}
  return runAtomicUndoOperation(()=>{
    const wanted=new Set(ids),internalLinks=links.filter(l=>Array.isArray(l)&&wanted.has(String(l[0]))&&wanted.has(String(l[1])));
    const positions=MapliniLayoutCore.smartLayout(selectedNodeRects(ids),internalLinks,{orientation,mainGap:150,crossGap:68,bounds:{width:canvasLogicalWidth,height:canvasLogicalHeight,padding:28}});
    const ok=applyNodePositions(positions,scope==='selected'?'Markerade rutor snyggades till':'Processen snyggades till',false);
    if(ok){
      // Layout + connector cleanup is one atomic Undo operation.
      polishAutomaticConnectedLinks(ids,{forceAuto:true});
      persist();requestFullLinkRender(true);drawLinks();fitProcessToScreen();
    }
    return ok;
  });
}

function closeTransientMenus(except=null){
  const menus=[smartLayoutMenu,root.querySelector('#p48-export-menu'),root.querySelector('#p48-more-menu'),scaleMenu,root.querySelector('#p48-logo-menu'),root.querySelector('.p48-canvas-menu'),root.querySelector('.p48-sheets-menu')];
  for(const menu of menus){
    // Nested menus (e.g. Sheets inside Export or Processyta inside More) must keep
    // their parent details open. Close only unrelated transient menus.
    const isAncestor=Boolean(except&&menu!==except&&menu.contains&&menu.contains(except));
    if(menu&&menu!==except&&!isAncestor&&menu.open)menu.open=false;
  }
  const nextMenus=root.querySelectorAll('.p48-next-menu:not([hidden])');
  nextMenus.forEach(menu=>{menu.hidden=true;const owner=menu.closest('.p48-node');const btn=owner&&owner.querySelector('.p48-next-btn');if(btn)btn.setAttribute('aria-expanded','false')});
}
for(const menu of [smartLayoutMenu,root.querySelector('#p48-export-menu'),root.querySelector('#p48-more-menu'),scaleMenu,root.querySelector('#p48-logo-menu'),root.querySelector('.p48-canvas-menu'),root.querySelector('.p48-sheets-menu')]){
  if(menu)menu.addEventListener('toggle',()=>{if(menu.open)closeTransientMenus(menu)});
}
const exportMenu=root.querySelector('#p48-export-menu');
const moreMenu=root.querySelector('#p48-more-menu');
for(const id of ['#p48-pdf','#p48-doc','#p48-sheets','#p48-sheets-direct']){
  const btn=root.querySelector(id);if(btn)btn.addEventListener('click',()=>{setTimeout(()=>{if(exportMenu)exportMenu.open=false},0)});
}
if(scroll)scroll.addEventListener('pointerdown',e=>{
  if(e.target===scroll||e.target===canvas||e.target.classList?.contains('p48-print-page'))closeTransientMenus();
},{capture:true});
if(fitScreenBtn)fitScreenBtn.addEventListener('click',fitProcessToScreen);
function applyProcessScaleSlider(next){
  const target=Math.max(50,Math.min(150,Number(next)||100));
  if(processScaleValue)processScaleValue.textContent=Math.round(target)+' %';
  if(Math.abs(target-processScalePercent)<.01)return false;
  const ratio=target/processScalePercent;
  const ok=scaleWholeProcess(ratio,false,false);
  if(ok)processScalePercent=target;
  return ok;
}
if(processScaleSlider){
  processScaleSlider.addEventListener('pointerdown',e=>{e.stopPropagation();if(!processScaleGesture){beginUndoGesture();processScaleGesture=true}});
  processScaleSlider.addEventListener('input',e=>{e.stopPropagation();applyProcessScaleSlider(processScaleSlider.value);if(scaleMenu)scaleMenu.open=true});
  const finishScaleGesture=()=>{if(processScaleGesture)endUndoGesture();processScaleGesture=false;if(scaleMenu)scaleMenu.open=true};
  processScaleSlider.addEventListener('pointerup',finishScaleGesture);
  processScaleSlider.addEventListener('pointercancel',finishScaleGesture);
  processScaleSlider.addEventListener('keydown',e=>{
    if(!['ArrowLeft','ArrowRight','ArrowUp','ArrowDown','Home','End','PageUp','PageDown'].includes(e.key))return;
    if(!processScaleGesture){beginUndoGesture();processScaleGesture=true}
  });
  processScaleSlider.addEventListener('change',()=>{if(processScaleGesture)endUndoGesture();processScaleGesture=false;if(scaleMenu)scaleMenu.open=true});
}
if(scaleFitPageBtn)scaleFitPageBtn.addEventListener('click',()=>{if(scaleWholeProcess(1,true)&&scaleMenu)scaleMenu.open=false});
if(autoCleanBtn)autoCleanBtn.addEventListener('click',()=>{if(autoCleanProcess()&&smartLayoutMenu)smartLayoutMenu.open=false});
smartLayoutChoices.forEach(btn=>btn.addEventListener('click',()=>{if(smartLayout(btn.dataset.layoutScope,btn.dataset.layoutOrientation)&&smartLayoutMenu)smartLayoutMenu.open=false}));

if(nodeQuick){nodeQuick.addEventListener('pointerdown',e=>e.stopPropagation());nodeQuick.addEventListener('click',e=>e.stopPropagation())}
if(nodeQuickNext)nodeQuickNext.addEventListener('click',e=>{
  e.preventDefault();e.stopPropagation();
  const item=selectedId&&selectedIds.size===1?nodes.get(selectedId):null;
  const type=preferredNextType(item);
  if(item&&type)addNextStepFromNode(item.data.id,type);
});
if(nodeQuickNextMore)nodeQuickNextMore.addEventListener('click',e=>{
  e.preventDefault();e.stopPropagation();
  const item=selectedId&&selectedIds.size===1?nodes.get(selectedId):null;
  if(item&&isNextStepSource(item)&&item.nextBtn)item.nextBtn.click();
});
if(nodeQuickFormat)nodeQuickFormat.addEventListener('click',e=>{e.preventDefault();e.stopPropagation();focusFormattingPanel()});
if(nodeQuickColor)nodeQuickColor.addEventListener('change',e=>{e.stopPropagation();updateStyle({bgColor:String(nodeQuickColor.value||'#ffffff')})});
if(nodeQuickDuplicate)nodeQuickDuplicate.addEventListener('click',e=>{e.preventDefault();e.stopPropagation();duplicateSelectedNodes();refreshNodeQuickToolbar()});
if(nodeQuickDelete)nodeQuickDelete.addEventListener('click',e=>{e.preventDefault();e.stopPropagation();deleteSelectedMany()});

zoomOutBtn.addEventListener('click',()=>applyCanvasScale(MapliniCanvasCore.zoomStep(canvasScale,'out')));
zoomInBtn.addEventListener('click',()=>applyCanvasScale(MapliniCanvasCore.zoomStep(canvasScale,'in')));
zoomResetBtn.addEventListener('click',()=>applyCanvasScale(1));
applyCanvasScale(1,false);


function showPendingRecovery(){if(!pendingRecoveryStore||!recoveryBanner)return;recoveryBanner.hidden=false}
function hidePendingRecovery(){if(recoveryBanner)recoveryBanner.hidden=true}
function restorePendingRecovery(){
  if(!pendingRecoveryStore)return false;
  try{
    const restored=MapliniStateCore.normalizeStore(pendingRecoveryStore);processes=restored.processes;currentId=restored.currentId;resetHistory();lastLocalPayload='';
    openProcess(currentId);renderProcesses(true);refreshControls();refreshLinkControls();updateSelectionUi();saveLocal(true);pendingRecoveryStore=null;hidePendingRecovery();setSaveState('recovered');msg('Avbrutna ändringar återställdes');return true;
  }catch(e){reportRuntimeError(e,'recovery-restore');msg('Återställningen misslyckades');return false}
}
function ignorePendingRecovery(){pendingRecoveryStore=null;try{localStorage.removeItem(LOCAL_RECOVERY_KEY)}catch(ignore){}hidePendingRecovery();msg('Återställning ignorerad')}
if(recoveryRestore)recoveryRestore.addEventListener('click',restorePendingRecovery);
if(recoveryIgnore)recoveryIgnore.addEventListener('click',ignorePendingRecovery);


window.addEventListener('keydown',e=>{
  if(e.key!=='Escape')return;
  closeTransientMenus();
  if(nodeQuickArrange)nodeQuickArrange.open=false;
  if(linkQuick)linkQuick.classList.remove('on');
},{capture:true});
loadCloudSession();
const SHARE_TOKEN="__SHARE_TOKEN__";
(async()=>{
 if(SHARE_TOKEN&&await loadShared(SHARE_TOKEN))return;
 if(!loadLocal()){processes[starter.id]=clone(starter);currentId=starter.id}
 try{
  openProcess(currentId);
}catch(err){
  console.error('Maplini restore failed',err);
  clearCanvas();
  const fallback=MapliniWorkflowCore.emptyProcess(currentId,'Ny process');
  processes[currentId]=fallback;
  nameInput.value=fallback.name;
}
renderProcesses();refreshControls();updateSelectionUi();updateAccountUi();setSaveState('saved');showPendingRecovery();msg('Klar');
 applyProcessStyle();
 renderPrintPages();
 if(ownerId()){
   const valid=await validateSession();
   if(valid){
     await loadWorkspaces();
     const cloudOk=await loadCloudProcesses();
     applyRoleUi();
     if(!cloudOk)msg('Klar · lokal data återställd, molnet kunde inte läsas');
   }else{
     resetWorkspaceState();
     msg('Klar · lokal lagring');
   }
 }
})();
})();


function syncResponsiveLayout(){
  const mobile=isMobileLayout();
  if(!mobile){
    setMobileTools(false);
    canvas.classList.toggle('p48-selection-mode',selectionMode);
  }
  if(scroll){scroll.style.visibility='visible';scroll.style.pointerEvents='auto';}
  invalidateNodeGeom();
  requestFullLinkRender();
  scheduleHorizontalNavSync();
}
function scheduleResponsiveLayout(){
  MapliniPerformanceCore.rafOnce('responsive-layout',syncResponsiveLayout);
}
window.addEventListener('orientationchange',()=>setTimeout(scheduleResponsiveLayout,120));
window.addEventListener('resize',scheduleResponsiveLayout,{passive:true});
scheduleResponsiveLayout();

function flushLifecycleSave(context){
  if(!MapliniPrivacyCore.shouldPersistLocally({sharedView}))return true;
  try{
    persist(false,false);
    const ok=saveLocal(true);
    if(!ok)reportRuntimeError(new Error('Local lifecycle save failed'),context);
    return ok;
  }catch(e){
    reportRuntimeError(e,context);
    return false;
  }
}
document.addEventListener('visibilitychange',()=>{if(document.visibilityState==='hidden')flushLifecycleSave('visibility-save')});
window.addEventListener('pagehide',()=>{flushLifecycleSave('pagehide-save')});
document.addEventListener('freeze',()=>{flushLifecycleSave('freeze-save')});
window.addEventListener('beforeunload',()=>{flushLifecycleSave('beforeunload-save')});

function alignEditorTop(){
  invalidateNodeGeom();
  requestFullLinkRender();
  scheduleHorizontalNavSync();
}
MapliniPerformanceCore.rafOnce('align-editor-top',alignEditorTop);
setTimeout(()=>MapliniPerformanceCore.rafOnce('align-editor-top',alignEditorTop),100);

</script>
</div>
"""

# Google export integration (OAuth callback + optional Drive connection UI)
maplini_google_ui.render_google_export_ui(st, google_docs)

html = html.replace("__MAPLINI_LOGO__", f"data:image/png;base64,{_LOGO_B64}")
html = html.replace("__MAPLINI_VERSION__", APP_VERSION)
html = html.replace("__MAPLINI_CONNECTOR_CORE__", _CONNECTOR_CORE_JS)
html = html.replace("__MAPLINI_CANVAS_CORE__", _CANVAS_CORE_JS)
html = html.replace("__MAPLINI_UI_CORE__", _UI_CORE_JS)
html = html.replace("__MAPLINI_STATE_CORE__", _STATE_CORE_JS)
html = html.replace("__MAPLINI_PROCESS_INFO_CORE__", _PROCESS_INFO_CORE_JS)
html = html.replace("__MAPLINI_RELIABILITY_CORE__", _RELIABILITY_CORE_JS)
html = html.replace("__MAPLINI_EXPORT_CORE__", _EXPORT_CORE_JS)
html = html.replace("__MAPLINI_WORKFLOW_CORE__", _WORKFLOW_CORE_JS)
html = html.replace("__MAPLINI_PERFORMANCE_CORE__", _PERFORMANCE_CORE_JS)
html = html.replace("__MAPLINI_MOBILE_CORE__", _MOBILE_CORE_JS)
html = html.replace("__MAPLINI_SELECTION_CORE__", _SELECTION_CORE_JS)
html = html.replace("__MAPLINI_SYNC_CORE__", _SYNC_CORE_JS)
html = html.replace("__MAPLINI_SESSION_CORE__", _SESSION_CORE_JS)
html = html.replace("__MAPLINI_RC_CORE__", _RC_CORE_JS)
html = html.replace("__MAPLINI_FLOW_CORE__", _FLOW_CORE_JS)
html = html.replace("__MAPLINI_ACCESS_CORE__", _ACCESS_CORE_JS)
html = html.replace("__MAPLINI_PRIVACY_CORE__", _PRIVACY_CORE_JS)
html = html.replace("__MAPLINI_EDITING_CORE__", _EDITING_CORE_JS)
html = html.replace("__MAPLINI_LAYOUT_CORE__", _LAYOUT_CORE_JS)
html = html.replace("__MAPLINI_AUTOSAVE_CORE__", _AUTOSAVE_CORE_JS)
html = html.replace("__MAPLINI_PROCESS_INTELLIGENCE_CORE__", _PROCESS_INTELLIGENCE_CORE_JS)
html = html.replace("__SUPABASE_URL__", _SUPABASE_URL)
html = html.replace("__SUPABASE_ANON_KEY__", _SUPABASE_ANON_KEY)
html = html.replace("__PUBLIC_APP_URL__", _PUBLIC_APP_URL)
html = html.replace("__SHARE_TOKEN__", st.query_params.get("share", ""))
if not _CLOUD_ENABLED:
    st.caption("Molnlagring är inte aktiverad ännu. Lägg Supabase-inställningarna i Streamlit Secrets enligt README.")
components.html(html, height=920, scrolling=False)
