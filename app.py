import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64
import google_docs

st.set_page_config(page_title="Maplini", page_icon="🧭", layout="wide", initial_sidebar_state="collapsed")
APP_VERSION = "0.6.0"
_LOGO_PATH = Path(__file__).resolve().parent / "assets" / "maplini_logo.png"
_LOGO_B64 = base64.b64encode(_LOGO_PATH.read_bytes()).decode("ascii") if _LOGO_PATH.exists() else ""

st.markdown("""
<style>
.block-container{padding:0.35rem 0.45rem 0.8rem;max-width:none}
header[data-testid="stHeader"]{height:2rem}
#MainMenu,footer{visibility:hidden}
</style>
""", unsafe_allow_html=True)


html = r"""
<div id="pk48">
<style>
#pk48{font-family:Inter,system-ui,sans-serif;color:#17202a;background:#eef2f6;border:1px solid #dce2e8;border-radius:12px;overflow:hidden}
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
.p48-body{display:grid;grid-template-columns:220px minmax(0,1fr);min-height:900px}
.p48-side{background:#fff;border-right:1px solid #dce2e8;padding:10px}
.p48-section{margin-bottom:16px}.p48-title{font-size:12px;font-weight:800;margin-bottom:8px}.p48-sub{font-size:11px;color:#6c7784;line-height:1.45;margin-bottom:9px}
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
.p48-format-grid{display:grid;grid-template-columns:1fr 1fr;gap:7px}
.p48-format label{display:block;font-size:10px;font-weight:800;color:#65717e;margin-bottom:3px}
.p48-format select,.p48-format input[type="number"]{width:100%;min-height:34px;border:1px solid #cfd7df;border-radius:7px;padding:5px 7px;font:12px system-ui;background:#fff}
.p48-format input[type="color"]{width:100%;height:34px;border:1px solid #cfd7df;border-radius:7px;padding:2px;background:#fff}
.p48-actions{display:grid;grid-template-columns:repeat(3,1fr);gap:5px;margin-top:7px}
.p48-mini{min-height:33px;border:1px solid #cfd7df;border-radius:7px;background:#fff;font:700 12px system-ui;cursor:pointer}.p48-mini.active{background:#eaf1f8;border-color:#7c9ab5}
.p48-empty{font-size:11px;color:#75818d;line-height:1.4}
.p48-scroll{overflow:auto;background:#e9eef3}
#p48-canvas{position:relative;width:2400px;height:1400px;background:#fff;touch-action:none;background-image:radial-gradient(#dce2e8 1px,transparent 1px);background-size:20px 20px}
#p48-svg{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:2}
.p48-link{stroke:#687584;stroke-width:2.2;fill:none}.p48-temp{stroke:#df941e;stroke-width:2.4;fill:none;stroke-dasharray:6 5}
.p48-node{position:absolute;min-width:160px;max-width:360px;width:max-content;min-height:64px;height:auto;padding:14px 26px;border:2px solid #637387;border-radius:10px;background:#fff;box-shadow:0 3px 9px rgba(31,42,55,.10);z-index:5;user-select:none;touch-action:none;display:flex;align-items:center;justify-content:center}
.p48-label{display:block;width:100%;white-space:pre-wrap;overflow-wrap:anywhere;word-break:break-word;line-height:1.28;cursor:text;outline:none}
.p48-label[contenteditable="true"]{user-select:text;-webkit-user-select:text;cursor:text;min-width:40px}
.p48-node.start,.p48-node.end{border-radius:38px}.p48-node.start{border-color:#2b7b61}.p48-node.end{border-color:#985148}
.p48-node.decision{min-width:160px;max-width:240px;min-height:120px;padding:34px 32px;border:0;background:transparent!important;border-radius:0;overflow:visible}
.p48-node.decision::before{content:"";position:absolute;left:50%;top:50%;width:70%;height:70%;transform:translate(-50%,-50%) rotate(45deg);background:var(--decision-bg,#fff8df);border:2px solid #a97a20;z-index:-1}
.p48-node.decision .p48-label,.p48-node.decision .p48-node-io{position:relative;z-index:2}
.p48-node.subprocess{border-style:double;border-width:4px;border-color:#7556a6}.p48-node.note{border-color:#b8973e}.p48-node.group{min-width:240px;max-width:440px;min-height:120px;border-style:dashed;color:#536171}
.p48-node.selected{outline:3px solid #2c7be5;outline-offset:3px}
.p48-node.decision.selected{outline:none}
.p48-node.decision.selected::before{border-color:#2c7be5;box-shadow:none}
.p48-handle{position:absolute;width:16px;height:16px;border-radius:50%;background:#1f6f55;border:3px solid #fff;box-shadow:0 0 0 1px #1f6f55;cursor:crosshair;z-index:8}
.p48-handle.right{right:-8px;top:50%;transform:translateY(-50%)}.p48-handle.left{left:-8px;top:50%;transform:translateY(-50%)}.p48-handle.top{top:-8px;left:50%;transform:translateX(-50%)}.p48-handle.bottom{bottom:-8px;left:50%;transform:translateX(-50%)}
.p48-node.decision .p48-handle.right{right:2px;top:50%}.p48-node.decision .p48-handle.left{left:2px;top:50%}.p48-node.decision .p48-handle.top{top:2px;left:50%}.p48-node.decision .p48-handle.bottom{bottom:2px;left:50%}
.p48-node.decision .p48-resize{display:none!important}
@media(max-width:850px){.p48-body{grid-template-columns:1fr}.p48-side{border-right:0;border-bottom:1px solid #dce2e8}}
</style>

<div class="p48-brand">
  <div class="p48-brand-inner">
    <div class="p48-logo-crop"><img src="__MAPLINI_LOGO__" alt="Maplini"></div>
    <div class="p48-tagline">MAP · UNDERSTAND · IMPROVE</div>
  </div>
</div>
<div class="p48-top">
  <strong>Process</strong>
  <input id="p48-name" class="p48-name" value="Exempel – upphandlingsprocess" aria-label="Processnamn">
  <button type="button" class="p48-btn primary" id="p48-new">+ Ny process</button>
  <button type="button" class="p48-btn" id="p48-save">Spara</button>
  <button type="button" class="p48-btn" id="p48-undo">↶ Ångra</button>
  <button type="button" class="p48-btn" id="p48-redo">↷ Gör om</button>
  <span class="p48-spacer"></span>
  <button type="button" class="p48-btn primary" id="p48-pdf">Exportera PDF</button>
  <button type="button" class="p48-btn" id="p48-doc">Exportera DOCX</button>
  <span id="p48-status" class="p48-status"></span>
</div>

<div class="p48-body">
  <aside class="p48-side">
    <div class="p48-section">
      <div class="p48-title">Sparade processer</div>
      <div id="p48-processes" class="p48-list"></div>
    </div>

    <div class="p48-section">
      <div class="p48-title">Dra till arbetsytan</div>
      <div class="p48-item" draggable="true" data-type="start"><span class="p48-icon">▶</span>Start</div>
      <div class="p48-item" draggable="true" data-type="process"><span class="p48-icon">□</span>Aktivitet</div>
      <div class="p48-item" draggable="true" data-type="decision"><span class="p48-icon">◇</span>Beslut</div>
      <div class="p48-item" draggable="true" data-type="end"><span class="p48-icon">■</span>Slut</div>
      <div class="p48-item" draggable="true" data-type="subprocess"><span class="p48-icon">▣</span>Delprocess</div>
      <div class="p48-item" draggable="true" data-type="note"><span class="p48-icon">N</span>Anteckning</div>
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

    <div class="p48-format">
      <div class="p48-title">Formatering</div>
      <div class="p48-sub">Markera en ruta för att ändra dess text, färger och formatering.</div>
      <div id="p48-controls">
        <div class="p48-format-grid">
          <div><label>Typsnitt</label><select id="p48-font"><option value="Arial">Arial</option><option value="Verdana">Verdana</option><option value="Georgia">Georgia</option><option value="Trebuchet MS">Trebuchet MS</option><option value="Courier New">Courier New</option><option value="system-ui">System</option></select></div>
          <div><label>Storlek</label><input id="p48-size" type="number" min="10" max="36" value="13"></div>
          <div><label>Textfärg</label><input id="p48-textcolor" type="color" value="#17202a"></div>
          <div><label>Bakgrund</label><input id="p48-bgcolor" type="color" value="#ffffff"></div>
        </div>
        <div class="p48-actions">
          <button type="button" class="p48-mini" id="p48-bold"><b>B</b></button>
          <button type="button" class="p48-mini" id="p48-italic"><i>I</i></button>
          <button type="button" class="p48-mini" id="p48-under"><u>U</u></button>
        </div>
        <div class="p48-actions">
          <button type="button" class="p48-mini" data-align="left">Vänster</button>
          <button type="button" class="p48-mini" data-align="center">Centrera</button>
          <button type="button" class="p48-mini" data-align="right">Höger</button>
        </div>
        <button type="button" class="p48-btn" id="p48-delete-node" style="width:100%;margin-top:10px;color:#a43d34;border-color:#e0c4c1">Ta bort markerad ruta</button>

      </div>
    </div>
  </aside>

  <main class="p48-scroll" id="p48-scroll">
    <div id="p48-canvas">
      <svg id="p48-svg" viewBox="0 0 2400 1400">
        <defs><marker id="p48-arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><polygon points="0,0 10,4 0,8" fill="#687584"></polygon></marker></defs>
        <g id="p48-links"></g>
        <path id="p48-temp" class="p48-temp" hidden></path>
      </svg>
    </div>
  </main>
</div>

<script>
(()=>{
const root=document.getElementById('pk48'); if(!root||root.dataset.ready==='1')return; root.dataset.ready='1';
const canvas=root.querySelector('#p48-canvas'),scroll=root.querySelector('#p48-scroll'),linkLayer=root.querySelector('#p48-links'),temp=root.querySelector('#p48-temp');
const nameInput=root.querySelector('#p48-name'),status=root.querySelector('#p48-status'),processBox=root.querySelector('#p48-processes');
const controls=root.querySelector('#p48-controls'),font=root.querySelector('#p48-font'),size=root.querySelector('#p48-size'),textColor=root.querySelector('#p48-textcolor'),bgColor=root.querySelector('#p48-bgcolor');
const bold=root.querySelector('#p48-bold'),italic=root.querySelector('#p48-italic'),under=root.querySelector('#p48-under');
const inputsBox=root.querySelector('#p48-inputs'),outputsBox=root.querySelector('#p48-outputs');
const addInputBtn=root.querySelector('#p48-add-input'),addOutputBtn=root.querySelector('#p48-add-output'),deleteNodeBtn=root.querySelector('#p48-delete-node');

let nodes=new Map(),links=[],selectedId=null,seq=8,undo=[],redo=[],currentId='proc-1',processes={};

const starter={id:'proc-1',name:'Exempel – upphandlingsprocess',nodes:[
{id:'n1',type:'start',text:'Upphandling identifieras',x:100,y:130},{id:'n2',type:'process',text:'Första bedömning',x:390,y:130},{id:'n3',type:'decision',text:'Relevant?',x:680,y:110},{id:'n4',type:'process',text:'Kvalificera upphandling',x:950,y:130}
],links:[['n1','n2','right'],['n2','n3','right'],['n3','n4','right']]};

function clone(v){return JSON.parse(JSON.stringify(v))}
function uid(){return 'proc-'+Date.now().toString(36)+'-'+Math.random().toString(36).slice(2,7)}
function msg(t){status.textContent=t;setTimeout(()=>{if(status.textContent===t)status.textContent=''},1800)}
function defBg(type){return {start:'#edf8f3',end:'#fff3f1',decision:'#fff8df',subprocess:'#f7f3ff',note:'#fffbe8',group:'#f8fafc'}[type]||'#ffffff'}
function styleOf(d){return{fontFamily:d.fontFamily||'Arial',fontSize:Number(d.fontSize||13),textColor:d.textColor||'#17202a',bgColor:d.bgColor||defBg(d.type),fontWeight:d.fontWeight||'700',fontStyle:d.fontStyle||'normal',textDecoration:d.textDecoration||'none',textAlign:d.textAlign||'center'}}
function applyStyle(item){const s=styleOf(item.data);Object.assign(item.data,s);item.label.style.fontFamily=s.fontFamily;item.label.style.fontSize=s.fontSize+'px';item.label.style.color=s.textColor;item.label.style.fontWeight=s.fontWeight;item.label.style.fontStyle=s.fontStyle;item.label.style.textDecoration=s.textDecoration;item.label.style.textAlign=s.textAlign;item.el.style.background=s.bgColor;item.el.style.setProperty('--decision-bg',s.bgColor)}
function state(){return{id:currentId,name:nameInput.value.trim()||'Namnlös process',nodes:[...nodes.values()].map(x=>clone(x.data)),links:clone(links)}}
function saveLocal(){try{localStorage.setItem('maplini_v050',JSON.stringify({currentId,processes}))}catch(e){}}
function loadLocal(){
  try{
    const raw=localStorage.getItem('maplini_v050')||localStorage.getItem('processkartan_v048');
    if(!raw)return false;
    const d=JSON.parse(raw);
    if(!d.processes||!Object.keys(d.processes).length)return false;
    processes=d.processes;
    currentId=d.currentId&&processes[d.currentId]?d.currentId:Object.keys(processes)[0];
    saveLocal();
    return true;
  }catch(e){return false}
}
function renderProcesses(){
  processBox.innerHTML='';
  Object.values(processes).sort((a,b)=>(a.name||'').localeCompare(b.name||'','sv')).forEach(p=>{
    const row=document.createElement('div');row.className='p48-proc-row';
    const b=document.createElement('button');b.type='button';b.className='p48-proc'+(p.id===currentId?' active':'');
    b.textContent=p.name||'Namnlös process';b.title=p.name||'Namnlös process';
    b.addEventListener('click',()=>{if(p.id!==currentId){persist();openProcess(p.id)}});
    const del=document.createElement('button');del.type='button';del.className='p48-proc-delete';del.textContent='×';del.title='Radera process';
    del.addEventListener('click',e=>{e.stopPropagation();deleteProcess(p.id)});
    row.append(b,del);processBox.appendChild(row);
  });
}
function persist(show=false){const s=state();processes[currentId]=clone(s);saveLocal();renderProcesses();if(show)msg('Sparad')}
function pushUndo(){undo.push(JSON.stringify(state()));if(undo.length>50)undo.shift();redo=[]}
function clearCanvas(){for(const x of nodes.values())x.el.remove();nodes.clear();links=[];selectedId=null;linkLayer.innerHTML='';refreshControls()}
function restore(s){const d=typeof s==='string'?JSON.parse(s):clone(s);clearCanvas();currentId=d.id||currentId;nameInput.value=d.name||'Namnlös process';(d.nodes||[]).forEach(makeNode);links=d.links||[];seq=Math.max(0,...[...nodes.keys()].map(id=>parseInt(String(id).replace(/\D/g,''),10)||0));drawLinks()}
function openProcess(id){if(!processes[id])return;currentId=id;undo=[];redo=[];restore(processes[id]);saveLocal();renderProcesses();msg('Process öppnad')}
function newProcess(){persist();const n=prompt('Namn på den nya processen:','Ny process');if(n===null)return;currentId=uid();processes[currentId]={id:currentId,name:n.trim()||'Ny process',nodes:[],links:[]};undo=[];redo=[];restore(processes[currentId]);saveLocal();renderProcesses();scroll.scrollLeft=0;scroll.scrollTop=0;msg('Ny process skapad')}
function deleteProcess(id){
  const proc=processes[id]; if(!proc)return;
  const label=proc.name||'Namnlös process';
  if(!confirm('Radera processen "'+label+'"? Detta går inte att ångra.'))return;
  delete processes[id];
  if(id===currentId){
    const remaining=Object.keys(processes);
    if(remaining.length){
      currentId=remaining[0];
      restore(processes[currentId]);
    }else{
      currentId=uid();
      processes[currentId]={id:currentId,name:'Ny process',nodes:[],links:[]};
      restore(processes[currentId]);
    }
  }
  saveLocal();renderProcesses();refreshControls();msg('Process raderad');
}
function nodeText(t){return{start:'Start',process:'Ny aktivitet',decision:'Beslut?',end:'Slut',subprocess:'Ny delprocess',group:'Ny grupp / område',note:'Anteckning'}[t]||'Nytt steg'}
function place(el,x,y){const snap=20,nx=Math.round(x/snap)*snap,ny=Math.round(y/snap)*snap;el.style.left=Math.max(10,Math.min(2400-el.offsetWidth-10,nx))+'px';el.style.top=Math.max(10,Math.min(1400-el.offsetHeight-10,ny))+'px'}
function sync(el){const x=nodes.get(el.dataset.id);if(x){x.data.x=parseFloat(el.style.left)||0;x.data.y=parseFloat(el.style.top)||0}}
function center(el){return[(parseFloat(el.style.left)||0)+el.offsetWidth/2,(parseFloat(el.style.top)||0)+el.offsetHeight/2]}
function anchor(el,side){const x=parseFloat(el.style.left)||0,y=parseFloat(el.style.top)||0,w=el.offsetWidth,h=el.offsetHeight;if(side==='left')return[x,y+h/2];if(side==='top')return[x+w/2,y];if(side==='bottom')return[x+w/2,y+h];return[x+w,y+h/2]}
function targetSide(a,b){const[ax,ay]=center(a),[bx,by]=center(b),dx=bx-ax,dy=by-ay;if(Math.abs(dx)>=Math.abs(dy))return dx>=0?'left':'right';return dy>=0?'top':'bottom'}
function select(el){for(const x of nodes.values())x.el.classList.remove('selected');selectedId=el.dataset.id;el.classList.add('selected');refreshControls()}

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
}
function renderIOEditor(item){
  inputsBox.innerHTML='';outputsBox.innerHTML='';ensureIO(item);
  const row=(value,index,kind)=>{
    const r=document.createElement('div');r.className='p48-io-row';
    const inp=document.createElement('input');inp.value=value;inp.placeholder=kind==='inputs'?'Input':'Output';
    inp.addEventListener('change',()=>{pushUndo();item.data[kind][index]=inp.value.trim();item.data[kind]=item.data[kind].filter(Boolean);renderNodeIO(item);drawLinks();persist();refreshControls();});
    const del=document.createElement('button');del.type='button';del.textContent='×';
    del.addEventListener('click',()=>{pushUndo();item.data[kind].splice(index,1);renderNodeIO(item);drawLinks();persist();refreshControls();});
    r.append(inp,del);return r;
  };
  item.data.inputs.forEach((v,i)=>inputsBox.appendChild(row(v,i,'inputs')));
  item.data.outputs.forEach((v,i)=>outputsBox.appendChild(row(v,i,'outputs')));
}

function setFormatEnabled(enabled){
  controls.querySelectorAll('select,input,button').forEach(el=>{el.disabled=!enabled;});
  root.querySelectorAll('.p48-step-io input,.p48-step-io button').forEach(el=>{el.disabled=!enabled;});
  controls.style.opacity=enabled?'1':'0.45';
  const stepIO=root.querySelector('.p48-step-io');
  if(stepIO)stepIO.style.opacity=enabled?'1':'0.45';
}

function refreshControls(){const item=selectedId?nodes.get(selectedId):null;if(!item){setFormatEnabled(false);inputsBox.innerHTML='';outputsBox.innerHTML='';return}setFormatEnabled(true);const s=styleOf(item.data);font.value=s.fontFamily;size.value=s.fontSize;textColor.value=s.textColor;bgColor.value=s.bgColor;bold.classList.toggle('active',s.fontWeight==='700');italic.classList.toggle('active',s.fontStyle==='italic');under.classList.toggle('active',s.textDecoration==='underline');root.querySelectorAll('[data-align]').forEach(b=>b.classList.toggle('active',b.dataset.align===s.textAlign));renderIOEditor(item)}
function updateStyle(patch){const item=selectedId?nodes.get(selectedId):null;if(!item)return;pushUndo();Object.assign(item.data,patch);applyStyle(item);drawLinks();persist();refreshControls()}
function beginInlineEdit(el){
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
  const clean=(item.label.innerText||'').replace(/\n{3,}/g,'\n\n').trim();
  item.data.text=clean||item.data.text||'Nytt steg';
  item.label.textContent=item.data.text;
  item.label.contentEditable='false';
  applyStyle(item);
  drawLinks();
  persist();
  refreshControls();
}

function makeNode(data){
const d=clone(data),el=document.createElement('div');el.className='p48-node '+d.type;el.dataset.id=d.id;el.style.left=d.x+'px';el.style.top=d.y+'px';el.tabIndex=0;if(d.width)el.style.width=d.width+'px';if(d.height)el.style.minHeight=d.height+'px';
const label=document.createElement('span');label.className='p48-label';label.textContent=d.text;label.contentEditable='false';label.spellcheck=true;el.appendChild(label);
const handles={};for(const side of ['right','left','top','bottom']){const h=document.createElement('span');h.className='p48-handle '+side;h.dataset.side=side;el.appendChild(h);handles[side]=h}
const resizeHandles={};for(const corner of ['se','sw','ne','nw']){const rh=document.createElement('span');rh.className='p48-resize '+corner;rh.dataset.corner=corner;el.appendChild(rh);resizeHandles[corner]=rh}
canvas.appendChild(el);nodes.set(d.id,{el,data:d,label,handles,resizeHandles,io:null});applyStyle(nodes.get(d.id));renderNodeIO(nodes.get(d.id));
el.addEventListener('dblclick',e=>{e.stopPropagation();beginInlineEdit(el)});
label.addEventListener('click',e=>{e.stopPropagation();select(el)});
label.addEventListener('dblclick',e=>{e.stopPropagation();beginInlineEdit(el)});
label.addEventListener('input',()=>{const item=nodes.get(el.dataset.id);if(item){item.data.text=label.innerText;drawLinks();}});
label.addEventListener('blur',()=>finishInlineEdit(el));
label.addEventListener('keydown',e=>{
  if(e.key==='Escape'){e.preventDefault();finishInlineEdit(el);el.focus();}
  if((e.ctrlKey||e.metaKey)&&e.key==='Enter'){e.preventDefault();finishInlineEdit(el);el.focus();}
});
el.addEventListener('click',e=>{e.stopPropagation();select(el)});
el.addEventListener('pointerdown',e=>{if(e.button!==0||e.target.classList.contains('p48-handle')||e.target.classList.contains('p48-label')||e.target.classList.contains('p48-resize'))return;select(el);pushUndo();const sx=e.clientX,sy=e.clientY,ox=parseFloat(el.style.left)||0,oy=parseFloat(el.style.top)||0;el.setPointerCapture(e.pointerId);const mv=ev=>{place(el,ox+ev.clientX-sx,oy+ev.clientY-sy);sync(el);drawLinks()};const up=()=>{el.removeEventListener('pointermove',mv);el.removeEventListener('pointerup',up);persist()};el.addEventListener('pointermove',mv);el.addEventListener('pointerup',up)});

Object.values(resizeHandles).forEach(rh=>rh.addEventListener('pointerdown',e=>{
  e.stopPropagation();e.preventDefault();select(el);pushUndo();
  const corner=rh.dataset.corner,sx=e.clientX,sy=e.clientY;
  const ox=parseFloat(el.style.left)||0,oy=parseFloat(el.style.top)||0,ow=el.offsetWidth,oh=el.offsetHeight;
  const mv=ev=>{
    const dx=ev.clientX-sx,dy=ev.clientY-sy;
    let w=ow+(corner.includes('e')?dx:-dx),h=oh+(corner.includes('s')?dy:-dy);
    w=Math.max(120,Math.min(700,w));h=Math.max(54,Math.min(500,h));
    if(corner.includes('w'))el.style.left=(ox+ow-w)+'px';
    if(corner.includes('n'))el.style.top=(oy+oh-h)+'px';
    el.style.width=w+'px';el.style.minHeight=h+'px';
    sync(el);const item=nodes.get(el.dataset.id);item.data.width=w;item.data.height=h;drawLinks();
  };
  const up=()=>{document.removeEventListener('pointermove',mv);document.removeEventListener('pointerup',up);persist()};
  document.addEventListener('pointermove',mv);document.addEventListener('pointerup',up);
}));

Object.values(handles).forEach(h=>h.addEventListener('pointerdown',e=>{e.stopPropagation();e.preventDefault();const side=h.dataset.side,[x1,y1]=anchor(el,side);temp.hidden=false;temp.setAttribute('d',`M${x1},${y1} L${x1},${y1}`);const mv=ev=>{const r=canvas.getBoundingClientRect(),x2=ev.clientX-r.left+scroll.scrollLeft,y2=ev.clientY-r.top+scroll.scrollTop;temp.setAttribute('d',`M${x1},${y1} L${x2},${y2}`)};const up=ev=>{document.removeEventListener('pointermove',mv);document.removeEventListener('pointerup',up);temp.hidden=true;const target=document.elementFromPoint(ev.clientX,ev.clientY)?.closest('.p48-node');if(target&&target!==el){pushUndo();links.push([el.dataset.id,target.dataset.id,side]);drawLinks();persist()}};document.addEventListener('pointermove',mv);document.addEventListener('pointerup',up)}));
return el}

function addNode(type,x,y){pushUndo();seq++;const el=makeNode({id:'n'+seq,type,text:nodeText(type),x:x-90,y:y-38});place(el,x-90,y-38);sync(el);select(el);drawLinks();persist()}
function drawLinks(){linkLayer.innerHTML='';for(const [a,b,side] of links){const A=nodes.get(a)?.el,B=nodes.get(b)?.el;if(!A||!B)continue;const s=side||'right',t=targetSide(A,B),[x1,y1]=anchor(A,s),[x2,y2]=anchor(B,t),p=document.createElementNS('http://www.w3.org/2000/svg','path');p.setAttribute('class','p48-link');p.setAttribute('marker-end','url(#p48-arrow)');p.setAttribute('d',`M${x1},${y1} L${x2},${y2}`);linkLayer.appendChild(p)}}
function deleteSelected(){if(!selectedId||!nodes.has(selectedId))return;pushUndo();nodes.get(selectedId).el.remove();nodes.delete(selectedId);links=links.filter(l=>l[0]!==selectedId&&l[1]!==selectedId);selectedId=null;drawLinks();persist();refreshControls()}

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
async function renderMapSnapshot(){
  persist();
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

  // connectors
  for(const [a,bid,side] of links){
    const A=nodes.get(a)?.el,B=nodes.get(bid)?.el;if(!A||!B)continue;
    const t=targetSide(A,B),[ax,ay]=anchor(A,side||'right'),[bx,by]=anchor(B,t);
    drawArrow(ctx,ox+ax,oy+ay,ox+bx,oy+by);
  }

  // nodes
  for(const item of nodes.values()){
    const d=item.data,s=styleOf(d),x=ox+(d.x||0),y=oy+(d.y||0),w=item.el.offsetWidth,h=item.el.offsetHeight;
    ctx.save();
    ctx.fillStyle=s.bgColor||'#ffffff';
    let stroke='#637387';
    if(d.type==='start')stroke='#2b7b61';
    else if(d.type==='end')stroke='#985148';
    else if(d.type==='decision')stroke='#a97a20';
    else if(d.type==='subprocess')stroke='#7556a6';
    else if(d.type==='note')stroke='#b8973e';
    ctx.strokeStyle=stroke;ctx.lineWidth=(d.type==='subprocess'?4:2);

    if(d.type==='decision'){
      ctx.beginPath();ctx.moveTo(x+w/2,y);ctx.lineTo(x+w,y+h/2);ctx.lineTo(x+w/2,y+h);ctx.lineTo(x,y+h/2);ctx.closePath();ctx.fill();ctx.stroke();
    }else if(d.type==='start'||d.type==='end'){
      ctx.beginPath();ctx.ellipse(x+w/2,y+h/2,w/2,h/2,0,0,Math.PI*2);ctx.fill();ctx.stroke();
    }else{
      drawRoundedRect(ctx,x,y,w,h,10);ctx.fill();ctx.stroke();
    }

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
  // A3 landscape
  const pageW=1190.55,pageH=841.89,margin=30;
  const scale=Math.min((pageW-2*margin)/imgW,(pageH-2*margin)/imgH);
  const w=imgW*scale,h=imgH*scale,x=(pageW-w)/2,y=(pageH-h)/2;
  const content=asciiBytes(`q\n${w.toFixed(3)} 0 0 ${h.toFixed(3)} ${x.toFixed(3)} ${y.toFixed(3)} cm\n/Im1 Do\nQ\n`);
  const parts=[asciiBytes('%PDF-1.4\n%Maplini\n')],offsets=[0];
  const addObj=(num,chunks)=>{
    offsets[num]=parts.reduce((n,p)=>n+p.length,0);
    parts.push(asciiBytes(`${num} 0 obj\n`),...chunks,asciiBytes('\nendobj\n'));
  };
  addObj(1,[asciiBytes('<< /Type /Catalog /Pages 2 0 R >>')]);
  addObj(2,[asciiBytes('<< /Type /Pages /Kids [3 0 R] /Count 1 >>')]);
  addObj(3,[asciiBytes(`<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${pageW} ${pageH}] /Resources << /XObject << /Im1 5 0 R >> >> /Contents 4 0 R >>`)]);
  addObj(4,[asciiBytes(`<< /Length ${content.length} >>\nstream\n`),content,asciiBytes('endstream')]);
  addObj(5,[asciiBytes(`<< /Type /XObject /Subtype /Image /Width ${imgW} /Height ${imgH} /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length ${jpeg.length} >>\nstream\n`),jpeg,asciiBytes('\nendstream')]);
  const xref=parts.reduce((n,p)=>n+p.length,0);
  let tail='xref\n0 6\n0000000000 65535 f \n';
  for(let i=1;i<=5;i++)tail+=String(offsets[i]).padStart(10,'0')+' 00000 n \n';
  tail+=`trailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n${xref}\n%%EOF`;
  parts.push(asciiBytes(tail));return cat(parts);
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
function downloadBytes(bytes,name,type){
  const blob=new Blob([bytes],{type}),a=document.createElement('a');
  a.href=URL.createObjectURL(blob);a.download=name;a.click();
  setTimeout(()=>URL.revokeObjectURL(a.href),1500);
}
async function exportPdf(){
  try{
    const shot=await renderMapSnapshot(),jpeg=canvasJpegBytes(shot,.94);
    const pdf=buildPdfFromJpeg(jpeg,shot.width,shot.height);
    downloadBytes(pdf,cleanFileName(state().name)+'.pdf','application/pdf');msg('PDF skapad');
  }catch(err){console.error(err);msg('PDF-export misslyckades')}
}
async function exportDoc(){
  try{
    const shot=await renderMapSnapshot(),jpeg=canvasJpegBytes(shot,.94);
    const docx=buildDocxWithJpeg(jpeg,shot.width,shot.height,state().name);
    downloadBytes(docx,cleanFileName(state().name)+'.docx','application/vnd.openxmlformats-officedocument.wordprocessingml.document');msg('DOCX skapad');
  }catch(err){console.error(err);msg('DOCX-export misslyckades')}
}

root.querySelectorAll('.p48-item').forEach(i=>i.addEventListener('dragstart',e=>{e.dataTransfer.setData('text/plain',i.dataset.type);e.dataTransfer.effectAllowed='copy'}));
canvas.addEventListener('dragover',e=>{e.preventDefault();e.dataTransfer.dropEffect='copy'});
canvas.addEventListener('drop',e=>{e.preventDefault();const type=e.dataTransfer.getData('text/plain');if(!type)return;const r=canvas.getBoundingClientRect();addNode(type,e.clientX-r.left+scroll.scrollLeft,e.clientY-r.top+scroll.scrollTop)});
canvas.addEventListener('click',e=>{if(e.target===canvas){for(const x of nodes.values())x.el.classList.remove('selected');selectedId=null;refreshControls()}});
nameInput.addEventListener('change',()=>{persist();msg('Namn sparat')});
root.querySelector('#p48-new').addEventListener('click',newProcess);root.querySelector('#p48-save').addEventListener('click',()=>persist(true));root.querySelector('#p48-pdf').addEventListener('click',exportPdf);root.querySelector('#p48-doc').addEventListener('click',exportDoc);
root.querySelector('#p48-undo').addEventListener('click',()=>{if(!undo.length)return;redo.push(JSON.stringify(state()));restore(undo.pop());persist()});
root.querySelector('#p48-redo').addEventListener('click',()=>{if(!redo.length)return;undo.push(JSON.stringify(state()));restore(redo.pop());persist()});
root.addEventListener('keydown',e=>{if(['INPUT','TEXTAREA','SELECT'].includes(e.target.tagName))return;if(e.key==='Delete')deleteSelected()});
font.addEventListener('change',()=>updateStyle({fontFamily:font.value}));size.addEventListener('change',()=>updateStyle({fontSize:Math.max(10,Math.min(36,Number(size.value)||13))}));textColor.addEventListener('input',()=>updateStyle({textColor:textColor.value}));bgColor.addEventListener('input',()=>updateStyle({bgColor:bgColor.value}));
bold.addEventListener('click',()=>{const x=selectedId?nodes.get(selectedId):null;if(x)updateStyle({fontWeight:styleOf(x.data).fontWeight==='700'?'400':'700'})});italic.addEventListener('click',()=>{const x=selectedId?nodes.get(selectedId):null;if(x)updateStyle({fontStyle:styleOf(x.data).fontStyle==='italic'?'normal':'italic'})});under.addEventListener('click',()=>{const x=selectedId?nodes.get(selectedId):null;if(x)updateStyle({textDecoration:styleOf(x.data).textDecoration==='underline'?'none':'underline'})});root.querySelectorAll('[data-align]').forEach(b=>b.addEventListener('click',()=>updateStyle({textAlign:b.dataset.align})));


addInputBtn.addEventListener('click',()=>{const item=selectedId?nodes.get(selectedId):null;if(!item)return;pushUndo();ensureIO(item);item.data.inputs.push('Ny input');renderNodeIO(item);persist();refreshControls();});
addOutputBtn.addEventListener('click',()=>{const item=selectedId?nodes.get(selectedId):null;if(!item)return;pushUndo();ensureIO(item);item.data.outputs.push('Ny output');renderNodeIO(item);persist();refreshControls();});
deleteNodeBtn.addEventListener('click',()=>deleteSelected());

if(!loadLocal()){processes[starter.id]=clone(starter);currentId=starter.id}
openProcess(currentId);renderProcesses();refreshControls();msg('Klar');
})();
</script>
</div>
"""

# Google OAuth callback
if google_docs.configured(st) and st.query_params.get("code") and not st.session_state.get("google_token"):
    try:
        st.session_state["google_token"] = google_docs.exchange(st, st.query_params["code"])
        st.query_params.clear()
        st.toast("Google-kontot är anslutet.")
    except Exception as exc:
        st.error(f"Google-inloggningen misslyckades: {exc}")

with st.expander("Google Docs", expanded=False):
    if not google_docs.configured(st):
        st.info("Lägg in Google OAuth-uppgifter i Streamlit Secrets för att aktivera direkt skapande av Google Docs.")
        st.code('[google_oauth]\nclient_id = "..."\\nclient_secret = "..."\\nredirect_uri = "https://DIN-APP.streamlit.app"', language="toml")
    elif not google_docs.creds(st):
        st.link_button("Anslut Google-konto", google_docs.auth_url(st))
    else:
        st.success("Google-kontot är anslutet.")
        title = st.text_input("Dokumentnamn", value="Maplini process")
        body = st.text_area("Text till Google Doc", value="Dokument skapat från Maplini.", height=80)
        if st.button("Skapa Google Doc"):
            try:
                doc_id = google_docs.create_doc(st, title, body)
                st.success("Google Doc skapat.")
                st.link_button("Öppna dokumentet", f"https://docs.google.com/document/d/{doc_id}/edit")
            except Exception as exc:
                st.error(f"Kunde inte skapa Google Doc: {exc}")

html = html.replace("__MAPLINI_LOGO__", f"data:image/png;base64,{_LOGO_B64}")
components.html(html, height=1000, scrolling=True)
