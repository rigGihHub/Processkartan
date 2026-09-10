"""Chromium interaction benchmark for large Maplini processes.

Measures hot interaction paths at 100/250/500/1000 nodes. The JSON is evidence,
not a brittle CI timing gate; container/browser scheduling varies.
"""
from __future__ import annotations
import ast, json, statistics
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
APP=ROOT/'app.py'
CORE_REPLACEMENTS={
    '__MAPLINI_CONNECTOR_CORE__':'maplini_connector_core.js','__MAPLINI_CANVAS_CORE__':'maplini_canvas_core.js',
    '__MAPLINI_UI_CORE__':'maplini_ui_core.js','__MAPLINI_STATE_CORE__':'maplini_state_core.js',
    '__MAPLINI_PROCESS_INFO_CORE__':'maplini_process_info_core.js','__MAPLINI_STEP_UNDERSTANDING_CORE__':'maplini_step_understanding_core.js','__MAPLINI_EMPTY_STEP_SUGGESTIONS_CORE__':'maplini_empty_step_suggestions_core.js','__MAPLINI_WALKTHROUGH_CORE__':'maplini_walkthrough_core.js',
    '__MAPLINI_RELIABILITY_CORE__':'maplini_reliability_core.js','__MAPLINI_EXPORT_CORE__':'maplini_export_core.js',
    '__MAPLINI_WORKFLOW_CORE__':'maplini_workflow_core.js','__MAPLINI_PERFORMANCE_CORE__':'maplini_performance_core.js',
    '__MAPLINI_MOBILE_CORE__':'maplini_mobile_core.js','__MAPLINI_SELECTION_CORE__':'maplini_selection_core.js',
    '__MAPLINI_SYNC_CORE__':'maplini_sync_core.js','__MAPLINI_SESSION_CORE__':'maplini_session_core.js',
    '__MAPLINI_RC_CORE__':'maplini_rc_core.js','__MAPLINI_FLOW_CORE__':'maplini_flow_core.js',
    '__MAPLINI_ACCESS_CORE__':'maplini_access_core.js','__MAPLINI_PRIVACY_CORE__':'maplini_privacy_core.js',
    '__MAPLINI_EDITING_CORE__':'maplini_editing_core.js','__MAPLINI_LAYOUT_CORE__':'maplini_layout_core.js',
    '__MAPLINI_AUTOSAVE_CORE__':'maplini_autosave_core.js','__MAPLINI_PROCESS_INTELLIGENCE_CORE__':'maplini_process_intelligence_core.js',
}

def extract_html():
    tree=ast.parse(APP.read_text(encoding='utf-8')); html=None
    for node in ast.walk(tree):
        if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='html' for t in node.targets):
            if isinstance(node.value,ast.Constant) and isinstance(node.value.value,str): html=node.value.value; break
    assert html
    for token,fn in CORE_REPLACEMENTS.items(): html=html.replace(token,(ROOT/fn).read_text(encoding='utf-8'))
    for token,val in [('__MAPLINI_LOGO__',''),('__MAPLINI_VERSION__','0.20.35'),('__SUPABASE_URL__',''),('__SUPABASE_ANON_KEY__',''),('__PUBLIC_APP_URL__','https://example.invalid'),('__SHARE_TOKEN__','')]: html=html.replace(token,val)
    needle="let pdfView='A4P',pageCountMode='auto',canvasScale=1,canvasLogicalWidth=2400,canvasLogicalHeight=1400,processScalePercent=100,processScaleGesture=false;"
    hook=r"""window.__interactionPerf={
restore:p=>{restore(p);return nodes.size},
snap:iter=>{const item=nodes.values().next().value,g=nodeGeom(item.data.id),ref={id:item.data.id,x:g.left,y:g.top,width:g.width,height:g.height},ex=new Set([item.data.id]),cache=buildMagneticSnapTargets(ex),t=performance.now();for(let i=0;i<iter;i++)magneticSnap(ref,ref.x+((i%17)-8),ref.y+((i%13)-6),ex,cache);return performance.now()-t},
dragFrames:iter=>{const item=nodes.values().next().value,g=nodeGeom(item.data.id),ox=g.left,oy=g.top;fastGeometryInteraction=true;const t=performance.now();for(let i=0;i<iter;i++){item.el.style.left=(ox+(i%7))+'px';item.el.style.top=(oy+(i%5))+'px';sync(item.el);invalidateNodeGeom(item.data.id);markNodeLinksDirty(item.data.id);renderDirtyLinksNow()}const dt=performance.now()-t;item.el.style.left=ox+'px';item.el.style.top=oy+'px';sync(item.el);invalidateNodeGeom(item.data.id);markNodeLinksDirty(item.data.id);fastGeometryInteraction=false;requestFullLinkRender(true);return dt},
select:iter=>{const item=nodes.values().next().value,t=performance.now();for(let i=0;i<iter;i++)select(item.el);return performance.now()-t},
zoom:iter=>{const t=performance.now();for(let i=0;i<iter;i++)applyCanvasScale(i%2?.9:1,false);return performance.now()-t},
overviewViewport:iter=>{setProcessOverview(true);renderProcessOverview();const t=performance.now();for(let i=0;i<iter;i++){scroll.scrollLeft=(i*13)%700;scroll.scrollTop=(i*7)%500;updateOverviewViewport()}const dt=performance.now()-t;setProcessOverview(false);return dt},
persist:iter=>{const t=performance.now();for(let i=0;i<iter;i++)persist(false,false);return performance.now()-t}
};"""
    html=html.replace(needle,needle+hook)
    storage="""<script>(function(){function store(){const d={};return{getItem:k=>Object.prototype.hasOwnProperty.call(d,k)?d[k]:null,setItem:(k,v)=>{d[k]=String(v)},removeItem:k=>{delete d[k]},clear:()=>{for(const k of Object.keys(d))delete d[k]},key:i=>Object.keys(d)[i]||null,get length(){return Object.keys(d).length}}}Object.defineProperty(window,'localStorage',{value:store()});Object.defineProperty(window,'sessionStorage',{value:store()});})();</script>"""
    return html.replace('<head>','<head>'+storage,1)

def proc(n):
    cols=25; nodes=[]; links=[]
    for i in range(n):
        row=i//cols; col=i%cols; nid=f'n{i+1}'
        nodes.append({'id':nid,'type':'process','text':f'Steg {i+1}','x':80+col*210,'y':80+row*115,'processInfo':{}})
        if i and col: links.append([f'n{i}',nid,'right',{'autoManaged':True,'routing':'orthogonal'}])
    return {'id':'bench','name':f'Benchmark {n}','nodes':nodes,'links':links,'processBackground':'#ffffff'}

def median3(page, expr):
    return round(statistics.median(page.evaluate(expr) for _ in range(3)),2)

def main():
    rows=[]
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        page=browser.new_page(viewport={'width':1440,'height':1000});page.set_content(extract_html(),wait_until='load')
        for n in (100,250,500,1000):
            payload=proc(n);page.evaluate('(p)=>window.__interactionPerf.restore(p)',payload)
            rows.append({
                'nodes':n,'links':len(payload['links']),
                'snap_200_ms':median3(page,'()=>window.__interactionPerf.snap(200)'),
                'drag_60_frames_ms':median3(page,'()=>window.__interactionPerf.dragFrames(60)'),
                'select_100_ms':median3(page,'()=>window.__interactionPerf.select(100)'),
                'zoom_100_ms':median3(page,'()=>window.__interactionPerf.zoom(100)'),
                'overview_viewport_100_ms':median3(page,'()=>window.__interactionPerf.overviewViewport(100)'),
                'persist_10_ms':median3(page,'()=>window.__interactionPerf.persist(10)'),
            })
        browser.close()
    print(json.dumps(rows,indent=2))
    (ROOT/'PERFORMANCE_INTERACTION_v0.20.35.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
if __name__=='__main__': main()
