"""Google export UI integration for Maplini.

Kept separate from the canvas editor so OAuth/query-param handling cannot be
duplicated accidentally inside app.py.
"""

import json


def _handle_oauth_callback(st, google_docs):
    if not google_docs.configured(st):
        return
    code = st.query_params.get("code")
    if not code or st.session_state.get("google_token"):
        return
    try:
        st.session_state["google_token"] = google_docs.exchange(st, code)
        st.query_params.clear()
        st.toast("Google är anslutet för export.")
    except Exception as exc:
        st.error(f"Google-anslutningen misslyckades: {exc}")


def _render_drive_connection(st, google_docs):
    if not google_docs.configured(st):
        st.caption("Google-export är inte konfigurerad ännu. Övriga exporter fungerar utan Google.")
        return

    if not google_docs.creds(st):
        c1, c2 = st.columns([1, 5])
        with c1:
            st.link_button("Anslut Google-export", google_docs.auth_url(st), use_container_width=True)
        with c2:
            st.caption("Valfritt. Behövs bara för att skapa Google Docs/Sheets direkt i Drive.")
        return

    st.caption("Google-export ansluten ✓")
    payload_raw = st.query_params.get("gs_payload")
    if not payload_raw:
        return
    try:
        payload = json.loads(payload_raw)
        _, sheet_url = google_docs.create_sheet(
            st,
            payload.get("title") or "Maplini process",
            payload.get("step_rows") or [],
            payload.get("link_rows") or [],
        )
        st.success("Google Sheet skapat.")
        st.link_button("Öppna Google Sheet", sheet_url)
        st.query_params.pop("gs_payload", None)
    except Exception as exc:
        st.error(f"Kunde inte skapa Google Sheet: {exc}")


def render_google_export_ui(st, google_docs):
    """Handle Google OAuth once and render the optional Drive integration UI."""
    _handle_oauth_callback(st, google_docs)
    _render_drive_connection(st, google_docs)
