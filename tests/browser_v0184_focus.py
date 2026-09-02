
import sys
sys.path.insert(0,"tests")
from browser_interaction_smoke import extract_editor_html
from playwright.sync_api import sync_playwright

html=extract_editor_html()
pre="""<script>(function(){function S(){const d={};return{getItem:k=>d[k]??null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k],clear:()=>{},key:i=>Object.keys(d)[i]||null,get length(){return Object.keys(d).length}}}window.__mapliniTestLocalStorage=S();window.__mapliniTestSessionStorage=S()})();</script>"""
html=html.replace("localStorage","window.__mapliniTestLocalStorage").replace("sessionStorage","window.__mapliniTestSessionStorage")

with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,executable_path="/usr/bin/chromium",args=["--no-sandbox"])
    page=browser.new_page(viewport={"width":1600,"height":920})
    page.set_content(pre+html,wait_until="load")
    page.wait_for_selector("#p48-canvas")

    # 1) Chrome sidebar: real bottom must be reachable with breathing room.
    side=page.locator("#p48-side")
    dims=side.evaluate("(el)=>({client:el.clientHeight,scroll:el.scrollHeight})")
    assert dims["scroll"] > dims["client"], dims
    side.evaluate("(el)=>el.scrollTop=el.scrollHeight")
    page.wait_for_timeout(60)
    endpos=side.evaluate("(el)=>({top:el.scrollTop,max:el.scrollHeight-el.clientHeight})")
    assert endpos["max"]-endpos["top"] <= 2, endpos
    last=page.locator("#p48-format-panel")
    sb=side.bounding_box(); lb=last.bounding_box()
    assert lb is not None and sb is not None
    assert lb["y"]+lb["height"] < sb["y"]+sb["height"]+1, (sb,lb)

    # 2) Snygga till: only linked flow is rearranged; isolated draft remains, zoom unchanged.
    page.evaluate("()=>window.__mapliniTestState.clear()")
    page.evaluate("()=>window.__mapliniTestState.addNode('process',300,260)")
    page.evaluate("()=>window.__mapliniTestState.addNode('process',760,430)")
    page.evaluate("()=>window.__mapliniTestState.addNode('note',1160,700)")
    ns=page.evaluate("()=>window.__mapliniTestState.nodes()")
    a,b,isolated=[x["id"] for x in ns]
    page.evaluate("([a,b])=>window.__mapliniTestState.connect(a,b)",[a,b])
    before_iso=page.evaluate("(id)=>window.__mapliniTestState.node(id)",isolated)
    before_scale=page.evaluate("()=>window.__mapliniTestState.scale()")
    page.locator("#p48-smart-layout-menu > summary").click()
    page.locator("#p48-auto-clean").click()
    page.wait_for_timeout(120)
    after_iso=page.evaluate("(id)=>window.__mapliniTestState.node(id)",isolated)
    after_a=page.evaluate("(id)=>window.__mapliniTestState.node(id)",a)
    after_b=page.evaluate("(id)=>window.__mapliniTestState.node(id)",b)
    assert (after_iso["x"],after_iso["y"]) == (before_iso["x"],before_iso["y"]), (before_iso,after_iso)
    assert after_a["x"] < after_b["x"], (after_a,after_b)
    assert page.evaluate("()=>window.__mapliniTestState.scale()") == before_scale

    # 3) Configure a yes/no verification question and run the process interactively.
    page.evaluate("()=>window.__mapliniTestState.clear()")
    page.evaluate("()=>window.__mapliniTestState.addNode('start',260,300)")
    page.evaluate("()=>window.__mapliniTestState.addNode('process',600,300)")
    page.evaluate("()=>window.__mapliniTestState.addNode('end',940,300)")
    ns=page.evaluate("()=>window.__mapliniTestState.nodes()")
    sid,aid,eid=[x["id"] for x in ns]
    page.evaluate("([a,b])=>window.__mapliniTestState.connect(a,b)",[sid,aid])
    page.evaluate("([a,b])=>window.__mapliniTestState.connect(a,b)",[aid,eid])

    activity=page.locator(f'#p48-canvas .p48-node[data-id="{aid}"]')
    activity.click()
    page.locator("#p48-check-questions > summary").click()
    page.locator("#p48-add-check-question").click()
    q=page.locator("#p48-check-question-list textarea").last
    q.fill("Är kontrollen utförd?")
    q.blur()
    stored=page.evaluate("(id)=>window.__mapliniTestState.node(id)",aid)
    assert stored["walkthroughQuestions"][0]["text"]=="Är kontrollen utförd?", stored

    page.locator("#p48-walkthrough-launch").click()
    assert page.locator("#p48-walkthrough-panel").is_visible()
    page.locator("#p48-walkthrough-start-btn").click()
    assert page.locator("#p48-walkthrough-step-type").text_content()=="Start"
    page.locator("#p48-walkthrough-next").click()
    assert page.locator("#p48-walkthrough-step-type").text_content()=="Aktivitet"
    assert activity.evaluate("(el)=>el.classList.contains('p48-walk-active')")
    page.locator('.p48-walkthrough-answer[data-answer="no"]').click()
    assert "1 avvikelse" in page.locator("#p48-walkthrough-deviation-count").text_content()
    page.locator("#p48-walkthrough-next").click()
    assert page.locator("#p48-walkthrough-step-type").text_content()=="Slut"
    page.locator("#p48-walkthrough-finish").click()
    assert page.locator("#p48-walkthrough-summary").is_visible()
    assert "avvikelser behöver följas upp" in page.locator("#p48-walkthrough-summary-status").text_content()
    assert "Är kontrollen utförd?" in page.locator("#p48-walkthrough-summary-list").text_content()

    browser.close()
print("v0.19.1 focused Chrome/layout/walkthrough smoke ok")
