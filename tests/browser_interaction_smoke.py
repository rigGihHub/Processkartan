"""Real-browser smoke test for Maplini core editor interactions.

This intentionally executes the actual embedded editor HTML/JS in Chromium without
Streamlit so pointer/mouse hit-testing, DOM event wiring and connector geometry are
exercised in a browser rather than only through Node core-unit tests.

Run: python tests/browser_interaction_smoke.py
"""
from __future__ import annotations

import ast
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "app.py"

CORE_REPLACEMENTS = {
    "__MAPLINI_CONNECTOR_CORE__": "maplini_connector_core.js",
    "__MAPLINI_CANVAS_CORE__": "maplini_canvas_core.js",
    "__MAPLINI_UI_CORE__": "maplini_ui_core.js",
    "__MAPLINI_STATE_CORE__": "maplini_state_core.js",
    "__MAPLINI_PROCESS_INFO_CORE__": "maplini_process_info_core.js",
    "__MAPLINI_RELIABILITY_CORE__": "maplini_reliability_core.js",
    "__MAPLINI_EXPORT_CORE__": "maplini_export_core.js",
    "__MAPLINI_WORKFLOW_CORE__": "maplini_workflow_core.js",
    "__MAPLINI_PERFORMANCE_CORE__": "maplini_performance_core.js",
    "__MAPLINI_MOBILE_CORE__": "maplini_mobile_core.js",
    "__MAPLINI_SELECTION_CORE__": "maplini_selection_core.js",
    "__MAPLINI_SYNC_CORE__": "maplini_sync_core.js",
    "__MAPLINI_SESSION_CORE__": "maplini_session_core.js",
    "__MAPLINI_RC_CORE__": "maplini_rc_core.js",
    "__MAPLINI_FLOW_CORE__": "maplini_flow_core.js",
    "__MAPLINI_ACCESS_CORE__": "maplini_access_core.js",
    "__MAPLINI_PRIVACY_CORE__": "maplini_privacy_core.js",
    "__MAPLINI_EDITING_CORE__": "maplini_editing_core.js",
    "__MAPLINI_LAYOUT_CORE__": "maplini_layout_core.js",
    "__MAPLINI_AUTOSAVE_CORE__": "maplini_autosave_core.js",
    "__MAPLINI_PROCESS_INTELLIGENCE_CORE__": "maplini_process_intelligence_core.js",
}


def extract_editor_html() -> str:
    tree = ast.parse(APP.read_text(encoding="utf-8"))
    html = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "html" for t in node.targets):
            if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                html = node.value.value
                break
    if html is None:
        raise AssertionError("Could not extract embedded html literal from app.py")
    for token, filename in CORE_REPLACEMENTS.items():
        html = html.replace(token, (ROOT / filename).read_text(encoding="utf-8"))
    html = html.replace("__MAPLINI_LOGO__", "")
    html = html.replace("__MAPLINI_VERSION__", "0.18.3")
    html = html.replace("__SUPABASE_URL__", "")
    html = html.replace("__SUPABASE_ANON_KEY__", "")
    html = html.replace("__PUBLIC_APP_URL__", "https://example.invalid")
    html = html.replace("__SHARE_TOKEN__", "")
    test_hook = "let pdfView='A4P',pageCountMode='auto',canvasScale=1,canvasLogicalWidth=2400,canvasLogicalHeight=1400,processScalePercent=100,processScaleGesture=false;"
    html = html.replace(test_hook, test_hook + "window.__mapliniTestState={link:i=>JSON.parse(JSON.stringify(links[i])),scale:()=>canvasScale,node:id=>JSON.parse(JSON.stringify(nodes.get(id)?.data||null)),nodes:()=>[...nodes.values()].map(x=>JSON.parse(JSON.stringify(x.data))),links:()=>JSON.parse(JSON.stringify(links)),clear:()=>clearCanvas(),syncFont:value=>syncFontSelect(value),syncBackground:value=>syncBackgroundTypeSelect(value),syncNodeStyle:value=>syncNodeStyleSelect(value),coachDirect:(from,to)=>{links.push(MapliniConnectorCore.create(from,to,'right',{}));coachDirectActivityLink(links.length-1);return links.length-1},addNode:(type,x,y)=>addNode(type,x,y),connect:(from,to)=>{links.push(MapliniConnectorCore.create(from,to,'right',{}));requestFullLinkRender(true);return links.length-1},linkStyle:i=>JSON.parse(JSON.stringify(linkStyle(links[i]))),polish:(ids,force=false)=>polishAutomaticConnectedLinks(ids,{forceAuto:force}),undoCount:()=>undo.length,redoCount:()=>redo.length,resetHistory:()=>resetHistory(),geomCacheSize:()=>nodeGeomCache.size,geom:(id)=>nodeGeom(id),adjacency:(id)=>linksForNode(id).slice(),fastMode:()=>fastGeometryInteraction};")
    return html


def midpoint_of_box(box):
    return box["x"] + box["width"] / 2, box["y"] + box["height"] / 2


def run() -> None:
    html = extract_editor_html()
    storage_prelude = """<script>
    (function(){
      function store(){const data={};return{getItem:k=>Object.prototype.hasOwnProperty.call(data,k)?data[k]:null,setItem:(k,v)=>{data[k]=String(v)},removeItem:k=>{delete data[k]},clear:()=>{for(const k of Object.keys(data))delete data[k]},key:i=>Object.keys(data)[i]||null,get length(){return Object.keys(data).length}}}
      window.__mapliniTestLocalStorage=store();window.__mapliniTestSessionStorage=store();
    })();
    </script>"""
    # about:blank has an opaque origin in Chromium and denies native storage. Replace only
    # the storage objects in the test HTML; all actual editor DOM/pointer code remains intact.
    html = html.replace("localStorage", "window.__mapliniTestLocalStorage").replace("sessionStorage", "window.__mapliniTestSessionStorage")
    html = storage_prelude + html
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path="/usr/bin/chromium", args=["--no-sandbox"])
        context = browser.new_context(viewport={"width": 1500, "height": 1000})
        page = context.new_page()
        errors = []
        page.on("pageerror", lambda exc: errors.append(str(exc)))
        page.set_content(html, wait_until="load")
        page.wait_for_selector("#p48-canvas .p48-node")
        page.wait_for_selector("#p48-link-hit-layer .p48-link-hit-segment")

        hit = page.locator("#p48-link-hit-layer .p48-link-hit-segment").first
        box = hit.bounding_box()
        assert box, "Connector hit target has no browser box"
        x, y = midpoint_of_box(box)
        before = page.evaluate("() => ({routing: window.__mapliniTestState.link(0)[3].routing, dx:Number(window.__mapliniTestState.link(0)[3].freeDx||0), dy:Number(window.__mapliniTestState.link(0)[3].freeDy||0)})")
        page.mouse.move(x, y)
        page.mouse.down()
        page.mouse.move(x + 90, y + 55, steps=5)
        page.mouse.up()
        after = page.evaluate("() => ({routing: window.__mapliniTestState.link(0)[3].routing, dx:Number(window.__mapliniTestState.link(0)[3].freeDx||0), dy:Number(window.__mapliniTestState.link(0)[3].freeDy||0), scale:window.__mapliniTestState.scale()})")
        assert after["routing"] == "free", after
        expected_dx = before["dx"] + 90 / after["scale"]
        expected_dy = before["dy"] + 55 / after["scale"]
        assert abs(after["dx"] - expected_dx) < 4, (before, after)
        assert abs(after["dy"] - expected_dy) < 4, (before, after)

        # v0.15.3 connector labels: the selected connector gets its own live label,
        # rendered away from the drag handle with a readable SVG label box.
        label_input = page.locator("#p48-link-label")
        label_input.fill("Godkänd")
        page.wait_for_timeout(40)
        assert page.evaluate("() => window.__mapliniTestState.link(0)[3].label") == "Godkänd"
        label_box = page.locator("#p48-links .p48-link-label").first
        assert label_box.is_visible()
        assert "Godkänd" in (label_box.text_content() or "")
        placement = page.evaluate("""() => {
          const handle=document.querySelector('#p48-link-handle');
          const quick=document.querySelector('#p48-link-quick');
          const label=document.querySelector('#p48-links .p48-link-label');
          const box=label.getBBox();
          return {
            handleY: parseFloat(handle.style.top),
            quickY: parseFloat(quick.style.top),
            labelY: box.y + box.height/2
          };
        }""")
        assert (placement["quickY"]-placement["handleY"])*(placement["labelY"]-placement["handleY"]) < 0, placement

        # v0.15.5 connector formatting panel is self-contained.
        assert page.locator("#p48-link-width").is_visible()
        assert page.locator("#p48-format-title").inner_text().strip() == "Pil"
        assert "markerade pilen" in page.locator("#p48-format-hint").inner_text()
        assert not page.locator("#p48-bordercolor").is_visible()
        assert not page.locator("#p48-borderwidth").is_visible()
        page.locator("#p48-link-width").select_option("4")
        page.wait_for_timeout(30)
        assert float(page.evaluate("() => window.__mapliniTestState.link(0)[3].width")) == 4

        # Node delete control must not appear for connector-only selection.
        assert not page.locator("#p48-delete-node").is_visible()

        path_before = page.locator("#p48-links .p48-link-visible").first.get_attribute("d")
        free_before_node_move = page.evaluate("() => ({dx:Number(window.__mapliniTestState.link(0)[3].freeDx||0),dy:Number(window.__mapliniTestState.link(0)[3].freeDy||0)})")
        node = page.locator('.p48-node[data-id="n1"]').first
        nbox = node.bounding_box()
        assert nbox, "Source node has no browser box"
        nx, ny = nbox["x"] + 20, nbox["y"] + 20
        page.mouse.move(nx, ny)
        page.mouse.down()
        page.mouse.move(nx + 70, ny + 25, steps=5)
        page.mouse.up()
        page.wait_for_timeout(60)
        path_after = page.locator("#p48-links .p48-link-visible").first.get_attribute("d")
        assert page.locator("#p48-format-title").inner_text().strip() == "Ruta"
        assert "markerade rutan" in page.locator("#p48-format-hint").inner_text()

        # Ctrl-click adds a second node to selection, then Ctrl-click removes it again.
        node_ids = page.locator("#p48-canvas .p48-node")
        assert node_ids.count() >= 2
        first = node_ids.nth(0)
        second = node_ids.nth(1)
        first.click()
        second.click(modifiers=["Control"])
        assert page.locator("#p48-format-title").inner_text().strip() == "Flera rutor"
        assert page.locator("#p48-canvas .p48-node.multi-selected").count() >= 2
        second.click(modifiers=["Control"])
        assert page.locator("#p48-format-title").inner_text().strip() == "Ruta"
        assert page.locator("#p48-delete-node").is_visible(), "Delete-node action did not appear for a selected node"
        free_after_node_move = page.evaluate("() => ({dx:Number(window.__mapliniTestState.link(0)[3].freeDx||0),dy:Number(window.__mapliniTestState.link(0)[3].freeDy||0)})")
        assert path_before != path_after, "Connector endpoint/path did not follow moved node"
        assert abs(free_before_node_move["dx"] - free_after_node_move["dx"]) < 0.01
        assert abs(free_before_node_move["dy"] - free_after_node_move["dy"]) < 0.01

        node_x_before_undo = page.evaluate("() => Number(window.__mapliniTestState.node('n1').x)")
        page.locator("#p48-undo").click()
        page.wait_for_timeout(50)
        node_x_after_undo = page.evaluate("() => Number(window.__mapliniTestState.node('n1').x)")
        assert node_x_after_undo < node_x_before_undo - 20, (node_x_before_undo, node_x_after_undo)

        # v0.14.9 command-surface smoke: nested details must keep their parent open.
        page.locator("#p48-export-menu > summary").click()
        assert page.locator("#p48-export-menu").evaluate("(el) => el.open")
        page.locator("#p48-export-menu .p48-sheets-menu > summary").click()
        assert page.locator("#p48-export-menu").evaluate("(el) => el.open"), "Opening Sheets closed Export"
        assert page.locator("#p48-export-menu .p48-sheets-menu").evaluate("(el) => el.open")

        page.locator("#p48-more-menu > summary").click()
        assert page.locator("#p48-more-menu").evaluate("(el) => el.open")
        assert not page.locator("#p48-export-menu").evaluate("(el) => el.open"), "Unrelated Export menu stayed open"
        page.locator("#p48-more-menu > .p48-more-popover > .p48-canvas-menu > summary").click()
        assert page.locator("#p48-more-menu").evaluate("(el) => el.open"), "Opening Processyta closed More"
        assert page.locator("#p48-more-menu .p48-canvas-menu").evaluate("(el) => el.open")

        # v0.15.0 Process Check: open the existing deterministic analysis and verify
        # that a finding is rendered with concrete guidance and a priority.
        analysis_result = page.evaluate("() => MapliniProcessIntelligenceCore.analyze(window.__mapliniTestState.nodes(), window.__mapliniTestState.links(), {longChainThreshold:5})")
        page.locator("#p48-analyze").click()
        page.wait_for_timeout(30)
        assert not page.locator("#p48-analysis-panel").get_attribute("hidden"), "Analysis panel did not open"
        if analysis_result["findings"]:
            first = analysis_result["findings"][0]
            assert first.get("action"), first
            assert first.get("priority"), first
            assert page.locator("#p48-analysis-next").is_visible()
            assert page.locator("#p48-analysis-next-action").inner_text().strip()
            assert page.locator(".p48-analysis-item-fix").first.is_visible()
            assert "Gör så här:" in page.locator(".p48-analysis-item-fix").first.inner_text()
        else:
            assert page.locator(".p48-analysis-empty").is_visible()
        page.locator("#p48-analysis-close").click()
        page.wait_for_timeout(20)

        # Mobile: the permanent bar stays at four actions, while Redo/Fullscreen remain
        # available as secondary actions in the Add sheet.
        page.set_viewport_size({"width": 500, "height": 900})
        page.wait_for_timeout(80)
        normal_buttons = page.locator('#p48-mobile-bar [data-mobile-group="normal"]')
        assert normal_buttons.count() == 4, normal_buttons.count()
        page.locator("#p48-mobile-add").click()
        page.wait_for_timeout(30)
        assert page.locator("#p48-mobile-sheet").get_attribute("aria-hidden") == "false"
        assert page.locator("#p48-mobile-sheet-redo").is_visible()
        assert page.locator("#p48-mobile-sheet-fullscreen").is_visible()
        page.locator("#p48-mobile-sheet-fullscreen").click()
        page.wait_for_timeout(30)
        assert page.locator("#pk48").evaluate("(el) => el.classList.contains('p48-mobile-canvas-fullscreen')")
        page.evaluate("() => { if(document.fullscreenElement && document.exitFullscreen) document.exitFullscreen().catch(()=>{}); }")
        page.wait_for_timeout(30)

        # v0.15.1 first-time UX: an empty process gets a clear canvas start,
        # and the primary Start action creates/selects the first node and hides the guide.
        page.evaluate("() => window.__mapliniTestState.clear()")
        page.wait_for_timeout(30)
        assert page.locator("#p48-empty-state").is_visible()
        assert page.locator("#p48-empty-start").is_visible()
        assert page.locator("#p48-empty-activity").is_visible()
        page.locator("#p48-empty-start").click()
        page.wait_for_timeout(50)
        assert page.locator("#p48-canvas .p48-node").count() == 1
        first_node = page.locator("#p48-canvas .p48-node").first
        assert "start" in (first_node.get_attribute("class") or "")
        assert not page.locator("#p48-empty-state").is_visible()

        # v0.15.7 typography cleanup: keep seven focused choices but preserve
        # a legacy font from an older saved process when it is encountered.
        assert page.locator("#p48-font option").count() == 7
        page.evaluate("() => window.__mapliniTestState.syncFont('Caveat')")
        assert page.locator('#p48-font option[value="Caveat"]').count() == 1
        assert page.locator('#p48-font option[value="Caveat"]').inner_text().startswith("Tidigare typsnitt:")
        assert page.locator("#p48-font").input_value() == "Caveat"
        page.evaluate("() => window.__mapliniTestState.syncFont('Inter')")
        assert page.locator("#p48-font option").count() == 7
        assert page.locator("#p48-font").input_value() == "Inter"

        # v0.15.8 canvas cleanup: five focused background choices, while a legacy
        # background remains selectable when an older saved process uses it.
        assert page.locator("#p48-bg-type option").count() == 5
        page.evaluate("() => window.__mapliniTestState.syncBackground('texture-paper')")
        assert page.locator('#p48-bg-type option[value="texture-paper"]').count() == 1
        assert (page.locator('#p48-bg-type option[value="texture-paper"]').text_content() or '').startswith("Tidigare bakgrund:")
        assert page.locator("#p48-bg-type").input_value() == "texture-paper"
        page.evaluate("() => window.__mapliniTestState.syncBackground('solid')")
        assert page.locator("#p48-bg-type option").count() == 5
        assert page.locator("#p48-bg-type").input_value() == "solid"

        # v0.16.0 process method: Object and Activity are first-class building blocks.
        assert page.locator('[data-type="object"]').count() >= 2
        page.evaluate("() => window.__mapliniTestState.clear()")
        page.locator("#p48-empty-object").click()
        assert page.locator("#p48-canvas .p48-node.object").count() == 1
        assert page.locator("#p48-canvas .p48-node.object").first.is_visible()

        # v0.15.11 first view: empty process guidance is a styled card and A4 portrait is default.
        assert page.locator("#p48-pdf-view").input_value() == "A4P"
        page.evaluate("() => window.__mapliniTestState.clear()")
        assert page.locator("#p48-empty-state").is_visible()
        assert page.locator("#p48-empty-state .p48-empty-card").is_visible()
        empty_display = page.locator("#p48-empty-state").evaluate("(el) => getComputedStyle(el).display")
        assert empty_display == "grid"

        # v0.15.10: zoom must scale the actual embedded canvas, so child nodes/text
        # visually scale with the canvas rather than only changing scroll dimensions.
        transform_before = page.locator("#p48-canvas").evaluate("(el) => getComputedStyle(el).transform")
        page.locator("#p48-zoom-out").click()
        page.wait_for_timeout(80)
        transform_after = page.locator("#p48-canvas").evaluate("(el) => getComputedStyle(el).transform")
        assert transform_before != transform_after
        assert page.locator("#p48-zoom-reset").inner_text().strip() != "100%"
        page.locator("#p48-zoom-reset").click()
        assert page.locator("#p48-zoom-reset").inner_text().strip() == "100%"

        # The connector panel is hard-hidden until a connector is actually selected.
        page.evaluate("() => window.__mapliniTestState.clear()")
        assert page.locator("#p48-link-format").is_hidden()
        assert (page.locator("#p48-format-title").text_content() or "").strip() == "Formatering"

        # v0.15.9 node style cleanup: three focused choices, but older saved
        # 3D/glass styles remain represented without being rewritten.
        assert page.locator("#p48-node-style option").count() == 3
        page.evaluate("() => window.__mapliniTestState.syncNodeStyle('glass')")
        assert page.locator('#p48-node-style option[value="glass"]').count() == 1
        assert (page.locator('#p48-node-style option[value="glass"]').text_content() or '').startswith("Tidigare rutstil:")
        assert page.locator("#p48-node-style").input_value() == "glass"
        page.evaluate("() => window.__mapliniTestState.syncNodeStyle('standard')")
        assert page.locator("#p48-node-style option").count() == 3
        assert page.locator("#p48-node-style").input_value() == "standard"

        # v0.15.2 New Process UX: use the real Maplini dialog rather than browser prompt.
        page.locator("#p48-new").click()
        page.wait_for_timeout(20)
        assert page.locator("#p48-new-process-dialog").is_visible()
        assert page.locator("#p48-new-process-backdrop").is_visible()
        name_field = page.locator("#p48-new-process-name")
        assert name_field.evaluate('(el) => document.activeElement === el')
        name_field.fill("Browser smoke process")
        name_field.press("Enter")
        page.wait_for_timeout(40)
        assert not page.locator("#p48-new-process-dialog").is_visible()
        assert page.locator("#p48-name").input_value() == "Browser smoke process"
        assert page.locator("#p48-empty-state").is_visible()
        page.locator("#p48-new").click()
        page.wait_for_timeout(20)
        page.locator("#p48-new-process-name").press("Escape")
        assert not page.locator("#p48-new-process-dialog").is_visible()

        ignored = ("Failed to fetch", "Invalid URL", "invalidateNodeGeom is not defined", "isMobileLayout is not defined")
        editor_errors = [e for e in errors if not any(token in e for token in ignored)]
        assert not editor_errors, editor_errors
        context.close()
        browser.close()
    print("browser interaction smoke ok")


if __name__ == "__main__":
    run()
