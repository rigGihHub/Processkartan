"""Repeatable large-process browser benchmark for Maplini.

Measures the real embedded editor in Chromium for synthetic processes at 100/250/500/1000 nodes.
This is a benchmark, not a hard timing gate: CI/container timing varies.
Run: python tests/browser_large_process_performance.py
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
    '__MAPLINI_PROCESS_INFO_CORE__':'maplini_process_info_core.js','__MAPLINI_WALKTHROUGH_CORE__':'maplini_walkthrough_core.js',
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
    for token,val in [('__MAPLINI_LOGO__',''),('__MAPLINI_VERSION__','0.20.34'),('__SUPABASE_URL__',''),('__SUPABASE_ANON_KEY__',''),('__PUBLIC_APP_URL__','https://example.invalid'),('__SHARE_TOKEN__','')]: html=html.replace(token,val)
    needle="let pdfView='A4P',pageCountMode='auto',canvasScale=1,canvasLogicalWidth=2400,canvasLogicalHeight=1400,processScalePercent=100,processScaleGesture=false;"
    hook="""window.__perf={restore:p=>{const t=performance.now();restore(p);return performance.now()-t},serialize:()=>{const t=performance.now();JSON.stringify(state());return performance.now()-t},save:()=>{persist(false,false);const t=performance.now();saveLocal(true);return performance.now()-t},overview:()=>{setProcessOverview(true);const t=performance.now();renderProcessOverview();return performance.now()-t},closeOverview:()=>setProcessOverview(false),count:()=>nodes.size};"""
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
    vals=[page.evaluate(expr) for _ in range(3)]
    return round(statistics.median(vals),2)

def main():
    html=extract_html(); rows=[]
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox']); page=browser.new_page(viewport={'width':1440,'height':1000}); page.set_content(html,wait_until='load')
        for n in (100,250,500,1000):
            payload=proc(n)
            # evaluate with arg for restore, then repeat fresh 3 times
            vals=[page.evaluate('(p)=>window.__perf.restore(p)',payload) for _ in range(3)]
            serialize=median3(page,'()=>window.__perf.serialize()')
            save=median3(page,'()=>window.__perf.save()')
            overview=median3(page,'()=>window.__perf.overview()')
            page.evaluate('()=>window.__perf.closeOverview()')
            rows.append({'nodes':n,'links':len(payload['links']),'restore_ms':round(statistics.median(vals),2),'serialize_ms':serialize,'save_flush_ms':save,'overview_ms':overview})
        browser.close()
    print(json.dumps(rows,indent=2))
    (ROOT/'PERFORMANCE_BASELINE_v0.20.34.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
if __name__=='__main__': main()
