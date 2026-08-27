import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Processkartan",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

APP_VERSION = "0.4.2"

st.markdown("""
<style>
.block-container{padding:0.35rem 0.45rem 0.8rem;max-width:none}
header[data-testid="stHeader"]{height:2rem}
#MainMenu,footer{visibility:hidden}
</style>
""", unsafe_allow_html=True)

st.markdown(f"**Processkartan** · v{APP_VERSION}")

html = r'''
<div id="pk4">
<style>
#pk4{font-family:Inter,system-ui,sans-serif;color:#17202a;background:#eef2f6;border:1px solid #dce2e8;border-radius:12px;overflow:hidden}
#pk4 *{box-sizing:border-box}
.pk4-top{display:flex;gap:7px;align-items:center;flex-wrap:wrap;padding:9px 10px;background:#fff;border-bottom:1px solid #dce2e8}
.pk4-btn,.pk4-select{border:1px solid #ccd4dc;background:#fff;color:#24303d;border-radius:8px;min-height:36px;padding:7px 10px;font:600 13px system-ui}
.pk4-btn{cursor:pointer}.pk4-btn:hover{background:#f2f5f7}.pk4-btn.primary{background:#1f6f55;color:#fff;border-color:#1f6f55}.pk4-btn.danger{color:#a13d35}
.pk4-name{font:800 14px system-ui;border:2px solid #8aa2b8;border-radius:8px;padding:7px 10px;min-width:260px;background:#fbfdff}
.pk4-spacer{flex:1}
.pk4-body{display:grid;grid-template-columns:185px minmax(0,1fr);min-height:900px}
.pk4-palette{background:#fff;border-right:1px solid #dce2e8;padding:10px}
.pk4-title{font-size:12px;font-weight:800;margin:0 0 8px}.pk4-sub{font-size:11px;color:#6c7784;line-height:1.45;margin-bottom:10px}
.pk4-drag{display:flex;align-items:center;gap:8px;border:1px solid #d0d7df;background:#fff;border-radius:9px;padding:9px;margin-bottom:7px;cursor:grab;font-size:12.5px;font-weight:700;user-select:none}
.pk4-drag:active{cursor:grabbing}.pk4-icon{width:23px;height:23px;border-radius:6px;background:#edf2f6;display:grid;place-items:center;font-size:11px}
.pk4-tip{margin-top:12px;padding:8px;border-radius:8px;background:#f2f6f4;color:#4c655c;font-size:10.8px;line-height:1.45}
.pk4-scroll{overflow:auto;background:#e9eef3}
#pk4-canvas{position:relative;width:2400px;height:1400px;background:#fff;touch-action:none;background-image:radial-gradient(#dce2e8 1px,transparent 1px);background-size:20px 20px}
#pk4-svg{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:2}
.pk4-link{stroke:#687584;stroke-width:2.2;fill:none}.pk4-temp{stroke:#df941e;stroke-width:2.5;fill:none;stroke-dasharray:6 5}
.pk4-node{position:absolute;width:190px;min-height:76px;padding:12px 25px 12px 12px;border:2px solid #637387;border-radius:10px;background:#fff;box-shadow:0 3px 9px rgba(31,42,55,.10);z-index:5;user-select:none;touch-action:none;font-size:13px;font-weight:750;text-align:center;display:flex;align-items:center;justify-content:center}
.pk4-node.start,.pk4-node.end{border-radius:38px}.pk4-node.start{border-color:#2b7b61;background:#edf8f3}.pk4-node.end{border-color:#985148;background:#fff3f1}
.pk4-node.decision{width:145px;height:110px;min-height:110px;padding:28px 22px;border-color:#a97a20;background:#fff8df;clip-path:polygon(50% 0,100% 50%,50% 100%,0 50%);border-radius:0}
.pk4-node.subprocess{border-style:double;border-width:4px;background:#f7f3ff;border-color:#7556a6}
.pk4-node.note{background:#fffbe8;border-color:#b8973e;font-weight:600}
.pk4-node.group{width:260px;min-height:120px;border-style:dashed;background:#f8fafc;color:#536171}
.pk4-node.selected{outline:3px solid #2c7be5;outline-offset:3px}
.pk4-handle{position:absolute;width:16px;height:16px;border-radius:50%;background:#1f6f55;border:3px solid #fff;box-shadow:0 0 0 1px #1f6f55;cursor:crosshair;z-index:8}
.pk4-handle.right{right:-8px;top:50%;transform:translateY(-50%)}
.pk4-handle.left{left:-8px;top:50%;transform:translateY(-50%)}
.pk4-handle.top{top:-8px;left:50%;transform:translateX(-50%)}
.pk4-handle.bottom{bottom:-8px;left:50%;transform:translateX(-50%)}
.pk4-node.decision .pk4-handle.right{right:4px}
.pk4-node.decision .pk4-handle.left{left:4px}
.pk4-node.decision .pk4-handle.top{top:4px}
.pk4-node.decision .pk4-handle.bottom{bottom:4px}
.pk4-edit{position:absolute;left:6px;top:6px;width:19px;height:19px;border-radius:6px;border:1px solid #d3dae2;background:#fff;font-size:11px;display:none;place-items:center;cursor:pointer}
.pk4-node.selected .pk4-edit{display:grid}
@media(max-width:850px){.pk4-body{grid-template-columns:1fr}.pk4-palette{border-right:0;border-bottom:1px solid #dce2e8;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}.pk4-title,.pk4-sub,.pk4-tip{grid-column:1/-1}.pk4-drag{margin-bottom:0}}
</style>

<div class="pk4-top">
  <strong style="font-size:15px;margin-right:4px">Process</strong>
  <input class="pk4-name" id="pk4-name" aria-label="Processnamn" placeholder="Döp processen...">
  <button type="button" class="pk4-btn" id="pk4-rename">Byt namn</button>
  <button type="button" class="pk4-btn primary" id="pk4-new">+ Ny process</button>
  <button type="button" class="pk4-btn" id="pk4-save">Spara</button>
  <button type="button" class="pk4-btn" id="pk4-undo">↶ Ångra</button>
  <button type="button" class="pk4-btn" id="pk4-redo">↷ Gör om</button>
  <span class="pk4-spacer"></span>
  <button type="button" class="pk4-btn primary" id="pk4-doc">Exportera till Google Docs</button>
</div>

<div class="pk4-body">
  <aside class="pk4-palette">
    <div class="pk4-title">Dra till arbetsytan</div>
    <div class="pk4-sub">Bygg processen direkt på canvasen.</div>
    <div class="pk4-drag" draggable="true" data-type="start"><span class="pk4-icon">▶</span>Start</div>
    <div class="pk4-drag" draggable="true" data-type="process"><span class="pk4-icon">□</span>Aktivitet</div>
    <div class="pk4-drag" draggable="true" data-type="decision"><span class="pk4-icon">◇</span>Beslut</div>
    <div class="pk4-drag" draggable="true" data-type="end"><span class="pk4-icon">■</span>Slut</div>
    <div class="pk4-drag" draggable="true" data-type="subprocess"><span class="pk4-icon">▣</span>Delprocess</div>
    <div class="pk4-drag" draggable="true" data-type="group"><span class="pk4-icon">G</span>Grupp / område</div>
    <div class="pk4-drag" draggable="true" data-type="note"><span class="pk4-icon">N</span>Anteckning</div>
    <div class="pk4-tip"><b>Pilar:</b> dra från någon av de fyra gröna punkterna.<br><br><b>Redigera:</b> dubbelklicka på rutan eller markera den och klicka pennan.</div>
  </aside>

  <main class="pk4-scroll" id="pk4-scroll">
    <div id="pk4-canvas">
      <svg id="pk4-svg" viewBox="0 0 2400 1400">
        <defs>
          <marker id="pk4-arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
            <polygon points="0,0 10,4 0,8" fill="#687584"></polygon>
          </marker>
        </defs>
        <g id="pk4-links"></g>
        <path id="pk4-temp" class="pk4-temp" d="" hidden></path>
      </svg>
    </div>
  </main>
</div>

<script>
(()=>{
const R=document.getElementById('pk4'); if(R.dataset.ready)return; R.dataset.ready='1';
const C=R.querySelector('#pk4-canvas'), G=R.querySelector('#pk4-links'), TEMP=R.querySelector('#pk4-temp');
const NAME=R.querySelector('#pk4-name'), SCROLL=R.querySelector('#pk4-scroll');

let nodes=new Map(), links=[], selectedIds=new Set(), selected=null, seq=0, clipboard=[], undo=[], redo=[];
let currentId=null, dragPaletteType=null, processes={};

const starter={
 id:'proc-1',
 name:'Exempel – upphandlingsprocess',
 nodes:[
  {id:'n1',type:'start',text:'Upphandling identifieras',x:100,y:130},
  {id:'n2',type:'process',text:'Första bedömning',x:390,y:130},
  {id:'n3',type:'decision',text:'Relevant?',x:680,y:110},
  {id:'n4',type:'process',text:'Kvalificera upphandling',x:950,y:130},
  {id:'n5',type:'process',text:'Fördela ansvar',x:1240,y:130},
  {id:'n6',type:'process',text:'Kalkyl & lösning',x:1240,y:360},
  {id:'n7',type:'process',text:'Kvalitetssäkra',x:950,y:360},
  {id:'n8',type:'end',text:'Lämna anbud',x:660,y:360}
 ],
 links:[['n1','n2'],['n2','n3'],['n3','n4'],['n4','n5'],['n5','n6'],['n6','n7'],['n7','n8']]
};

function clone(o){return JSON.parse(JSON.stringify(o))}
function uid(prefix){return prefix+'-'+Date.now().toString(36)+'-'+Math.random().toString(36).slice(2,7)}
function currentState(){return {id:currentId,name:NAME.value.trim()||'Namnlös process',nodes:[...nodes.values()].map(o=>clone(o.data)),links:clone(links)}}
function saveLocal(){try{localStorage.setItem('processkartan_v040',JSON.stringify({currentId,processes}))}catch(e){}}
function loadLocal(){
 try{
  const raw=localStorage.getItem('processkartan_v040');
  if(raw){
   const d=JSON.parse(raw);
   if(d && d.processes && Object.keys(d.processes).length){processes=d.processes;currentId=d.currentId||Object.keys(processes)[0];return true}
  }
 }catch(e){}
 return false;
}
function snapshot(){undo.push(JSON.stringify(currentState())); if(undo.length>50)undo.shift(); redo=[]}
function clearCanvas(){[...nodes.values()].forEach(o=>o.el.remove());nodes.clear();links=[];selectedIds.clear();selected=null;G.innerHTML=''}
function restoreState(s){
 const d=typeof s==='string'?JSON.parse(s):clone(s);
 clearCanvas(); currentId=d.id||currentId; NAME.value=d.name||'Namnlös process';
 (d.nodes||[]).forEach(makeNode); links=d.links||[]; seq=Math.max(0,...[...nodes.keys()].map(id=>parseInt(String(id).replace(/\D/g,''))||0)); drawLinks(); renderSelect();
}
function persistCurrent(show=true){
 if(!currentId)currentId=uid('proc');
 const s=currentState();processes[currentId]=clone(s);saveLocal();renderSelect();
 if(show)
}
function renderSelect(){}
function openProcess(id){
 if(!processes[id])return;currentId=id;undo=[];redo=[];restoreState(processes[id]);saveLocal();
}
function newProcess(){
 persistCurrent(false);
 const name=prompt('Namn på den nya processen:','Ny process');
 if(name===null)return;
 currentId=uid('proc');processes[currentId]={id:currentId,name:(name.trim()||'Ny process'),nodes:[],links:[]};
 undo=[];redo=[];restoreState(processes[currentId]);saveLocal();SCROLL.scrollLeft=0;SCROLL.scrollTop=0;
}
function nodeText(type){return ({start:'Start',process:'Ny aktivitet',decision:'Beslut?',end:'Slut',subprocess:'Ny delprocess',group:'Ny grupp / område',note:'Anteckning'})[type]||'Nytt steg'}
function place(el,x,y){
 const snap=20;x=Math.round(x/snap)*snap;y=Math.round(y/snap)*snap;
 el.style.left=Math.max(10,Math.min(2400-el.offsetWidth-10,x))+'px';el.style.top=Math.max(10,Math.min(1400-el.offsetHeight-10,y))+'px';
}
function sync(el){const d=nodes.get(el.dataset.id).data;d.x=parseFloat(el.style.left);d.y=parseFloat(el.style.top)}
function center(el){return[parseFloat(el.style.left)+el.offsetWidth/2,parseFloat(el.style.top)+el.offsetHeight/2]}
function anchorPoint(el,side){
 const x=parseFloat(el.style.left),y=parseFloat(el.style.top),w=el.offsetWidth,h=el.offsetHeight;
 if(side==='left')return[x,y+h/2];
 if(side==='top')return[x+w/2,y];
 if(side==='bottom')return[x+w/2,y+h];
 return[x+w,y+h/2];
}
function bestTargetSide(A,B){
 const [ax,ay]=center(A),[bx,by]=center(B),dx=bx-ax,dy=by-ay;
 if(Math.abs(dx)>=Math.abs(dy))return dx>=0?'left':'right';
 return dy>=0?'top':'bottom';
}
function selectNode(el,add=false){
 if(!add){[...nodes.values()].forEach(o=>o.el.classList.remove('selected'));selectedIds.clear()}
 selected=el;selectedIds.add(el.dataset.id);el.classList.add('selected');
 
}
function editNode(el){
 const d=nodes.get(el.dataset.id).data;const val=prompt('Text i steget:',d.text);
 if(val===null)return;snapshot();d.text=val.trim()||d.text;nodes.get(d.id).label.textContent=d.text;persistCurrent(false);
}
function makeNode(data){
 const d={...data};const el=document.createElement('div');el.className='pk4-node '+d.type;el.dataset.id=d.id;el.style.left=d.x+'px';el.style.top=d.y+'px';el.tabIndex=0;
 const label=document.createElement('span');label.textContent=d.text;el.appendChild(label);
 const edit=document.createElement('button');edit.type='button';edit.className='pk4-edit';edit.textContent='✎';edit.title='Redigera text';el.appendChild(edit);
 const handles={};
 ['right','left','top','bottom'].forEach(side=>{
   const h=document.createElement('span');h.className='pk4-handle '+side;h.dataset.side=side;h.title='Dra pil '+side;el.appendChild(h);handles[side]=h;
 });
 C.appendChild(el);nodes.set(d.id,{el,data:d,label,handles});
 edit.addEventListener('click',e=>{e.stopPropagation();editNode(el)});
 el.addEventListener('dblclick',e=>{e.stopPropagation();editNode(el)});
 el.addEventListener('click',e=>{e.stopPropagation();selectNode(el,e.ctrlKey||e.metaKey)});
 el.addEventListener('pointerdown',e=>{
  if(e.target.classList.contains('pk4-handle')||e.target===edit||e.button!==0)return;
  selectNode(el,e.ctrlKey||e.metaKey);snapshot();
  const sx=e.clientX,sy=e.clientY;
  const starts=[...selectedIds].map(id=>({id,x:nodes.get(id).data.x,y:nodes.get(id).data.y}));
  el.setPointerCapture(e.pointerId);
  const mv=ev=>{
   const dx=ev.clientX-sx,dy=ev.clientY-sy;
   starts.forEach(s=>{const o=nodes.get(s.id);place(o.el,s.x+dx,s.y+dy);sync(o.el)});drawLinks()
  };
  const up=()=>{el.removeEventListener('pointermove',mv);el.removeEventListener('pointerup',up);persistCurrent(false)};
  el.addEventListener('pointermove',mv);el.addEventListener('pointerup',up)
 });
 Object.values(handles).forEach(handle=>handle.addEventListener('pointerdown',e=>{
  e.stopPropagation();e.preventDefault();
  const side=handle.dataset.side;
  const p=anchorPoint(el,side),x=p[0],y=p[1];
  TEMP.hidden=false;TEMP.setAttribute('d','M'+x+','+y+' L'+x+','+y);
  const mv=ev=>{const r=C.getBoundingClientRect(),tx=ev.clientX-r.left+SCROLL.scrollLeft,ty=ev.clientY-r.top+SCROLL.scrollTop;TEMP.setAttribute('d','M'+x+','+y+' L'+tx+','+ty)};
  const up=ev=>{
   document.removeEventListener('pointermove',mv);document.removeEventListener('pointerup',up);TEMP.hidden=true;
   const target=document.elementFromPoint(ev.clientX,ev.clientY)?.closest('.pk4-node');
   if(target&&target!==el){snapshot();links.push([el.dataset.id,target.dataset.id,side]);drawLinks();persistCurrent(false);
  document.addEventListener('pointermove',mv);document.addEventListener('pointerup',up)
 }));
 return el;
}
function addNode(type,x,y){snapshot();seq++;const el=makeNode({id:'n'+seq,type,text:nodeText(type),x:x-90,y:y-38});place(el,x-90,y-38);sync(el);selectNode(el);drawLinks();persistCurrent(false)}
function drawLinks(){
 G.innerHTML='';
 links.forEach(link=>{
  const [a,b,sourceSide]=link;
  const A=nodes.get(a)?.el,B=nodes.get(b)?.el;if(!A||!B)return;
  let side=sourceSide;
  if(!side){
   const [ax,ay]=center(A),[bx,by]=center(B),dx=bx-ax,dy=by-ay;
   side=Math.abs(dx)>=Math.abs(dy)?(dx>=0?'right':'left'):(dy>=0?'bottom':'top');
  }
  const targetSide=bestTargetSide(A,B);
  const [x1,y1]=anchorPoint(A,side),[x2,y2]=anchorPoint(B,targetSide);
  const p=document.createElementNS('http://www.w3.org/2000/svg','path');
  p.setAttribute('class','pk4-link');p.setAttribute('marker-end','url(#pk4-arrow)');
  p.setAttribute('d','M'+x1+','+y1+' L'+x2+','+y2);G.appendChild(p)
 })
}
R.querySelectorAll('.pk4-drag').forEach(el=>{
 el.addEventListener('dragstart',e=>{dragPaletteType=el.dataset.type;e.dataTransfer.setData('text/plain',el.dataset.type)});
 el.addEventListener('dragend',()=>dragPaletteType=null)
});
C.addEventListener('dragover',e=>e.preventDefault());
C.addEventListener('drop',e=>{
 if(e.target.closest('.pk4-node'))return;e.preventDefault();
 const type=e.dataTransfer.getData('text/plain')||dragPaletteType;if(!type)return;
 const r=C.getBoundingClientRect();addNode(type,e.clientX-r.left+SCROLL.scrollLeft,e.clientY-r.top+SCROLL.scrollTop)
});
C.addEventListener('click',e=>{
 if(e.target===C){[...nodes.values()].forEach(o=>o.el.classList.remove('selected'));selectedIds.clear();selected=null;
NAME.addEventListener('change',()=>{persistCurrent(false);renderSelect()});
R.querySelector('#pk4-new').addEventListener('click',newProcess);
R.querySelector('#pk4-rename').addEventListener('click',()=>{
 const old=NAME.value.trim()||'Namnlös process';
 const val=prompt('Nytt namn på processen:',old);
 if(val===null)return;
 NAME.value=val.trim()||old;
 persistCurrent(false);renderSelect();
});
R.querySelector('#pk4-save').addEventListener('click',()=>persistCurrent(true));
function deleteSelected(){
 if(!selectedIds.size)return;snapshot();
 const ids=[...selectedIds];ids.forEach(id=>{nodes.get(id)?.el.remove();nodes.delete(id)});
 links=links.filter(l=>!selectedIds.has(l[0])&&!selectedIds.has(l[1]));selectedIds.clear();selected=null;drawLinks();persistCurrent(false)
}
R.querySelector('#pk4-undo').addEventListener('click',()=>{if(!undo.length)return;redo.push(JSON.stringify(currentState()));const s=undo.pop();restoreState(s);persistCurrent(false)});
R.querySelector('#pk4-redo').addEventListener('click',()=>{if(!redo.length)return;undo.push(JSON.stringify(currentState()));const s=redo.pop();restoreState(s);persistCurrent(false)});
function copySelected(){clipboard=[...selectedIds].map(id=>clone(nodes.get(id).data));snapshot();[...nodes.values()].forEach(o=>o.el.classList.remove('selected'));selectedIds.clear();
 clipboard.forEach(src=>{seq++;const d=clone(src);d.id='n'+seq;d.x+=40;d.y+=40;const el=makeNode(d);selectedIds.add(d.id);el.classList.add('selected');selected=el});
 drawLinks();persistCurrent(false);
R.addEventListener('keydown',e=>{
 if(['INPUT','TEXTAREA','SELECT'].includes(e.target.tagName)||e.target.isContentEditable)return;
 if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='c'){e.preventDefault();copySelected()}
 if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='v'){e.preventDefault();pasteSelected()}
 if(e.key==='Delete')deleteSelected()
});
function dl(data,name,type){const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([data],{type}));a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1200)}
function esc(s){return String(s??'').replace(/[&<>\"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;'}[c]||c))}


if(!loadLocal()){processes[starter.id]=clone(starter);currentId=starter.id}
renderSelect();openProcess(currentId);
})();
</script>
</div>
'''

components.html(html, height=990, scrolling=True)
