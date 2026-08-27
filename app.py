import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Processkartan", page_icon="🧭", layout="wide", initial_sidebar_state="collapsed")
APP_VERSION = "0.3.0"

st.markdown("""
<style>
.block-container{padding:0.6rem 0.8rem 1rem;max-width:none}
header[data-testid="stHeader"]{height:2.2rem}
#MainMenu,footer{visibility:hidden}
</style>
""", unsafe_allow_html=True)

st.markdown(f"**Processkartan** · v{APP_VERSION} · drag-and-drop workspace")

html = r'''
<div id="pk-app">
<style>
#pk-app{font-family:Inter,system-ui,sans-serif;color:#17202a;background:#f6f8fb;border:1px solid #dde3ea;border-radius:14px;overflow:hidden}
#pk-app *{box-sizing:border-box}
.pk-top{display:flex;align-items:center;gap:8px;flex-wrap:wrap;padding:10px 12px;background:#fff;border-bottom:1px solid #dde3ea}
.pk-btn{border:1px solid #cdd5de;background:#fff;color:#24303d;border-radius:8px;padding:7px 10px;min-height:36px;font:600 13px system-ui;cursor:pointer}
.pk-btn:hover{background:#f1f4f7}.pk-btn.primary{background:#1f6f55;color:#fff;border-color:#1f6f55}.pk-btn.danger{color:#a23c34}.pk-spacer{flex:1}.pk-msg{font-size:12px;color:#697584}
.pk-shell{display:grid;grid-template-columns:210px minmax(0,1fr) 285px;min-height:790px}
.pk-left,.pk-right{background:#fff;padding:12px;min-width:0}.pk-left{border-right:1px solid #dde3ea}.pk-right{border-left:1px solid #dde3ea}
.pk-title{font-size:13px;font-weight:800;margin:0 0 8px}.pk-sub{font-size:11.5px;color:#6d7886;line-height:1.45;margin-bottom:10px}
.pk-palette{display:grid;gap:8px}.pk-drag{display:flex;align-items:center;gap:9px;border:1px solid #d1d8e0;border-radius:9px;padding:9px;background:#fff;cursor:grab;user-select:none;font-size:12.5px;font-weight:700}.pk-drag:active{cursor:grabbing}.pk-icon{width:24px;height:24px;border-radius:6px;display:grid;place-items:center;background:#eef2f6;font-size:12px}.pk-drag.meta{border-style:dashed}
.pk-section{margin-top:16px;padding-top:12px;border-top:1px solid #e8ebef}.pk-export{display:grid;gap:7px}
.pk-scroll{overflow:auto;background:#e9eef3;position:relative}
#pk-canvas{position:relative;width:1600px;height:900px;background:#fff;touch-action:none;background-image:radial-gradient(#dce2e8 1px,transparent 1px);background-size:20px 20px}
.pk-lane{position:absolute;left:0;width:1600px;height:180px;border-bottom:1px solid #dce2e8;background:rgba(248,250,252,.72)}.pk-lane:nth-of-type(even){background:rgba(241,245,249,.72)}
.pk-lane-label{position:absolute;left:12px;top:10px;background:#fff;border:1px solid #d7dde4;border-radius:999px;padding:4px 9px;font-size:11px;font-weight:800;color:#596675;z-index:2;cursor:grab}
#pk-svg{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:3}.pk-temp{stroke:#e29521;stroke-width:2.5;fill:none;stroke-dasharray:6 5}.pk-link{stroke:#687584;stroke-width:2.2;fill:none}
.pk-node{position:absolute;width:190px;min-height:76px;padding:12px 24px 12px 12px;border:2px solid #657487;border-radius:10px;background:#fff;box-shadow:0 3px 9px rgba(31,42,55,.10);z-index:5;user-select:none;touch-action:none;font-size:13px;font-weight:750;text-align:center;display:flex;align-items:center;justify-content:center}.pk-node.start,.pk-node.end{border-radius:38px}.pk-node.subprocess{border-style:double;border-width:4px;background:#f7f3ff;border-color:#7556a6}.pk-node.group{width:240px;min-height:105px;border-style:dashed;background:#f8fafc;color:#536171}.pk-node.start{border-color:#2b7b61;background:#edf8f3}.pk-node.end{border-color:#9a5149;background:#fff3f1}.pk-node.decision{width:145px;height:110px;min-height:110px;padding:28px 22px;border-color:#a97a20;background:#fff8df;clip-path:polygon(50% 0,100% 50%,50% 100%,0 50%);border-radius:0}.pk-node.selected{outline:3px solid #2c7be5;outline-offset:3px}.pk-node.drop-target{outline:4px solid #1f8a63;outline-offset:4px}.pk-handle{position:absolute;right:-9px;top:50%;transform:translateY(-50%);width:18px;height:18px;border-radius:50%;background:#1f6f55;border:3px solid #fff;box-shadow:0 0 0 1px #1f6f55;cursor:crosshair;z-index:8}.pk-node.decision .pk-handle{right:4px}
.pk-badges{position:absolute;left:6px;bottom:-14px;display:flex;gap:3px;flex-wrap:wrap;max-width:185px}.pk-badge{font-size:9px;padding:2px 5px;border-radius:999px;background:#edf2f7;color:#536171;border:1px solid #dae1e8;font-weight:700}.pk-badge.risk{background:#fff1ef;color:#93453e}.pk-badge.control{background:#edf8f3;color:#276a54}.pk-badge.kpi{background:#eef4ff;color:#3b5d93}.pk-badge.doc{background:#f5f0ff;color:#6e4b93}
.pk-properties{font-size:12px}.pk-empty{color:#74808e;font-size:12px}.pk-field{margin:0 0 9px}.pk-field label{display:block;font-size:10.5px;color:#65717e;font-weight:800;margin-bottom:3px}.pk-field input,.pk-field textarea,.pk-field select{width:100%;border:1px solid #cfd6de;border-radius:7px;padding:7px;font:12px system-ui}.pk-field textarea{min-height:50px;resize:vertical}.pk-meta-list{display:grid;gap:6px;margin-top:6px}.pk-meta-row{border:1px solid #e0e5ea;border-radius:7px;padding:7px;background:#fafbfc}.pk-meta-row b{font-size:10px;text-transform:uppercase;color:#697584}.pk-mini{font-size:10.5px;color:#74808e;line-height:1.4}.pk-tip{padding:8px;border-radius:8px;background:#f1f6f4;color:#46655a;font-size:11px;line-height:1.45}
@media(max-width:950px){.pk-shell{grid-template-columns:1fr}.pk-left{border-right:0;border-bottom:1px solid #dde3ea}.pk-right{border-left:0;border-top:1px solid #dde3ea}.pk-palette{grid-template-columns:repeat(2,minmax(0,1fr))}}
</style>
<div class="pk-top">
  <button type="button" class="pk-btn" id="pk-undo">↶ Ångra</button>
  <button type="button" class="pk-btn" id="pk-redo">↷ Gör om</button>
  <button type="button" class="pk-btn" id="pk-auto">Ordna automatiskt</button>
  <button type="button" class="pk-btn" id="pk-copy">Kopiera</button>
  <button type="button" class="pk-btn" id="pk-paste">Klistra in</button>
  <label class="pk-btn" style="display:flex;align-items:center;gap:6px"><input type="checkbox" id="pk-snap" checked> Snap 20 px</label>
  <button type="button" class="pk-btn danger" id="pk-delete">Ta bort markerat</button>
  <span class="pk-spacer"></span><span class="pk-msg" id="pk-msg" aria-live="polite">Dra ett objekt från vänster till arbetsytan.</span>
</div>
<div class="pk-shell">
  <aside class="pk-left">
    <div class="pk-title">Dra till arbetsytan</div>
    <div class="pk-sub">Skapa processen genom att dra objekt. Inga separata “lägg till”-formulär behövs.</div>
    <div class="pk-palette">
      <div class="pk-drag" draggable="true" data-kind="node" data-type="start"><span class="pk-icon">▶</span>Start / trigger</div>
      <div class="pk-drag" draggable="true" data-kind="node" data-type="process"><span class="pk-icon">□</span>Aktivitet</div>
      <div class="pk-drag" draggable="true" data-kind="node" data-type="decision"><span class="pk-icon">◇</span>Beslut</div>
      <div class="pk-drag" draggable="true" data-kind="node" data-type="end"><span class="pk-icon">■</span>Slut / överlämning</div>
      <div class="pk-drag" draggable="true" data-kind="node" data-type="subprocess"><span class="pk-icon">▣</span>Delprocess</div>
      <div class="pk-drag" draggable="true" data-kind="node" data-type="group"><span class="pk-icon">G</span>Grupp / område</div>
    </div>
    <div class="pk-section">
      <div class="pk-title">Dra på ett processsteg</div>
      <div class="pk-sub">Släpp dessa direkt på en ruta för att koppla ISO-information till steget.</div>
      <div class="pk-palette">
        <div class="pk-drag meta" draggable="true" data-kind="meta" data-type="risk"><span class="pk-icon">!</span>Risk</div>
        <div class="pk-drag meta" draggable="true" data-kind="meta" data-type="control"><span class="pk-icon">✓</span>Kontroll</div>
        <div class="pk-drag meta" draggable="true" data-kind="meta" data-type="kpi"><span class="pk-icon">K</span>KPI / mätetal</div>
        <div class="pk-drag meta" draggable="true" data-kind="meta" data-type="doc"><span class="pk-icon">D</span>Dokument / bevis</div>
      </div>
    </div>
    <div class="pk-section"><div class="pk-tip"><b>Pilar:</b> dra från den gröna punkten på en ruta och släpp på en annan ruta.<br><br><b>Ansvar:</b> dra hela rutan mellan swimlanes.</div></div>
  </aside>
  <main class="pk-scroll" id="pk-scroll">
    <div id="pk-canvas">
      <div class="pk-lane" style="top:0px"><span class="pk-lane-label">Bid / Sälj</span></div>
      <div class="pk-lane" style="top:180px"><span class="pk-lane-label">Region</span></div>
      <div class="pk-lane" style="top:360px"><span class="pk-lane-label">Kalkyl</span></div>
      <div class="pk-lane" style="top:540px"><span class="pk-lane-label">Juridik</span></div>
      <div class="pk-lane" style="top:720px"><span class="pk-lane-label">Ledning</span></div>
      <svg id="pk-svg" viewBox="0 0 1600 900"><defs><marker id="pk-arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><polygon points="0,0 10,4 0,8" fill="#687584"></polygon></marker></defs><g id="pk-links"></g><path id="pk-temp" class="pk-temp" d="" hidden></path></svg>
    </div>
  </main>
  <aside class="pk-right">
    <div class="pk-title">Markerat steg</div>
    <div id="pk-props" class="pk-empty">Klicka på ett processsteg.</div>
    <div class="pk-section">
      <div class="pk-title">Projekt & export</div>
      <div class="pk-export">
        <button type="button" class="pk-btn" id="pk-save">Spara projekt (.json)</button>
        <label class="pk-btn" style="text-align:center">Öppna projekt<input id="pk-open" type="file" accept="application/json,.json" hidden></label>
        <button type="button" class="pk-btn primary" id="pk-doc">Exportera till Google Docs (.doc)</button>
        <button type="button" class="pk-btn" id="pk-svgexport">Exportera karta (.svg)</button>
      </div>
      <p class="pk-mini">Google Docs-exporten skapar en dokumentfil som kan laddas upp direkt till Google Drive och öppnas i Google Docs. Den innehåller processöversikt, ansvar, risker, kontroller, KPI och dokument/bevis. SVG-filen kan infogas som processkarta.</p>
    </div>
  </aside>
</div>
</div>
<script>
(()=>{
 const R=document.getElementById('pk-app'); if(R.dataset.ready)return; R.dataset.ready='1';
 const C=R.querySelector('#pk-canvas'), G=R.querySelector('#pk-links'), TEMP=R.querySelector('#pk-temp'), P=R.querySelector('#pk-props'), M=R.querySelector('#pk-msg');
 let roles=['Bid / Sälj','Region','Kalkyl','Juridik','Ledning'];
 let nodes=new Map(), links=[], selected=null, selectedIds=new Set(), seq=30, undo=[], redo=[], dragMeta=null, connection=null, clipboard=[];
 const defaults={risk:'Ny risk – dubbelklicka/ändra i panelen',control:'Ny kontroll',kpi:'Nytt mätetal',doc:'Nytt dokument/bevis'};
 const seed=[
 {id:'n1',type:'start',text:'Upphandling identifieras',x:60,y:55,meta:{risk:['Relevant annons missas'],control:['Daglig bevakning'],kpi:[],doc:[]}},
 {id:'n2',type:'process',text:'Första bedömning',x:330,y:55,meta:{risk:['Felaktig första bedömning'],control:['Kvalificeringskriterier'],kpi:['Tid till bedömning'],doc:['Checklista']}},
 {id:'n3',type:'decision',text:'Relevant?',x:610,y:35,meta:{risk:['Felaktigt beslut'],control:['Fastställda kriterier'],kpi:[],doc:[]}},
 {id:'n4',type:'process',text:'Kvalificera upphandling',x:850,y:55,meta:{risk:['Skallkrav missas'],control:['Tvåstegsgranskning'],kpi:['Ledtid kvalificering'],doc:['Kvalificeringsmall']}},
 {id:'n5',type:'process',text:'Fördela region / ansvarig',x:1120,y:235,meta:{risk:['Otydligt ägarskap'],control:['Ansvar bekräftas'],kpi:[],doc:['Ansvarsmatris']}},
 {id:'n6',type:'process',text:'Kalkyl & lösning',x:860,y:415,meta:{risk:['Felaktiga antaganden'],control:['Kalkylgranskning'],kpi:['Kalkylavvikelse'],doc:['Kalkylmall']}},
 {id:'n7',type:'process',text:'Juridisk / kommersiell kontroll',x:560,y:595,meta:{risk:['Avtalsrisk förbises'],control:['Juridisk checklista'],kpi:[],doc:['Avtalschecklista']}},
 {id:'n8',type:'decision',text:'Go / No-go',x:300,y:755,meta:{risk:['Beslut på bristande underlag'],control:['Beslutsunderlag'],kpi:['Hit-rate'],doc:['Beslutsmall']}}
 ];
 const seedLinks=[['n1','n2'],['n2','n3'],['n3','n4'],['n4','n5'],['n5','n6'],['n6','n7'],['n7','n8']];
 function copy(v){return JSON.parse(JSON.stringify(v))}
 function state(){return {nodes:[...nodes.values()].map(o=>copy(o.data)),links:copy(links),roles:copy(roles)}}
 function snapshot(){undo.push(JSON.stringify(state()));if(undo.length>50)undo.shift();redo=[]}
 function restore(raw){const s=typeof raw==='string'?JSON.parse(raw):raw;[...nodes.values()].forEach(o=>o.el.remove());nodes.clear();links=s.links||[];roles=s.roles||roles;updateLaneLabels();(s.nodes||[]).forEach(makeNode);selected=null;selectedIds.clear();renderProps();drawLinks()}
 function laneFor(y,h=76){return Math.max(0,Math.min(4,Math.floor((y+h/2)/180)))}
 function makeNode(data){
   data={meta:{risk:[],control:[],kpi:[],doc:[]},...data};data.meta={risk:[],control:[],kpi:[],doc:[],...data.meta};
   const el=document.createElement('div');el.className='pk-node '+data.type;el.dataset.id=data.id;el.style.left=data.x+'px';el.style.top=data.y+'px';el.tabIndex=0;
   const label=document.createElement('span');label.className='pk-label';label.textContent=data.text;el.appendChild(label);
   const handle=document.createElement('span');handle.className='pk-handle';handle.title='Dra för att skapa pil';el.appendChild(handle);
   const badges=document.createElement('span');badges.className='pk-badges';el.appendChild(badges);C.appendChild(el);nodes.set(data.id,{el,data,label,badges});renderBadges(data.id);
   el.addEventListener('click',e=>{if(e.target===handle)return;e.stopPropagation();select(el,e.ctrlKey||e.metaKey)});
   label.addEventListener('dblclick',e=>{e.stopPropagation();label.contentEditable='true';label.focus();const end=()=>{label.contentEditable='false';snapshot();data.text=label.textContent||'Namnlöst steg';renderProps();label.removeEventListener('blur',end)};label.addEventListener('blur',end)});
   el.addEventListener('pointerdown',e=>{if(e.target===handle||label.isContentEditable||e.button!==0)return;e.stopPropagation();select(el);snapshot();const sx=e.clientX,sy=e.clientY,ox=parseFloat(el.style.left),oy=parseFloat(el.style.top);el.setPointerCapture(e.pointerId);const mv=ev=>{place(el,ox+ev.clientX-sx,oy+ev.clientY-sy);sync(el);drawLinks()};const up=()=>{el.removeEventListener('pointermove',mv);el.removeEventListener('pointerup',up);M.textContent='Flyttat till '+roles[laneFor(parseFloat(el.style.top),el.offsetHeight)]};el.addEventListener('pointermove',mv);el.addEventListener('pointerup',up)});
   handle.addEventListener('pointerdown',e=>{e.stopPropagation();e.preventDefault();const a=center(el);connection={from:data.id,x:a[0],y:a[1]};TEMP.hidden=false;TEMP.setAttribute('d','M'+a[0]+','+a[1]+' L'+a[0]+','+a[1]);handle.setPointerCapture(e.pointerId);const mv=ev=>{const r=C.getBoundingClientRect();const x=ev.clientX-r.left+C.parentElement.scrollLeft,y=ev.clientY-r.top+C.parentElement.scrollTop;TEMP.setAttribute('d','M'+connection.x+','+connection.y+' L'+x+','+y)};const up=ev=>{handle.removeEventListener('pointermove',mv);handle.removeEventListener('pointerup',up);TEMP.hidden=true;const target=document.elementFromPoint(ev.clientX,ev.clientY)?.closest('.pk-node');if(target&&target.dataset.id!==data.id){snapshot();links.push([data.id,target.dataset.id]);drawLinks();M.textContent='Pil skapad genom drag-and-drop.'}connection=null};handle.addEventListener('pointermove',mv);handle.addEventListener('pointerup',up)});
   el.addEventListener('dragover',e=>{if(dragMeta){e.preventDefault();el.classList.add('drop-target')}});el.addEventListener('dragleave',()=>el.classList.remove('drop-target'));
   el.addEventListener('drop',e=>{if(!dragMeta)return;e.preventDefault();el.classList.remove('drop-target');snapshot();data.meta[dragMeta].push(defaults[dragMeta]);renderBadges(data.id);select(el);M.textContent='Kopplade '+dragMeta+' till '+data.text;dragMeta=null});
   return el;
 }
 function place(el,x,y){const snap=R.querySelector('#pk-snap')?.checked!==false;if(snap){x=Math.round(x/20)*20;y=Math.round(y/20)*20}el.style.left=Math.max(20,Math.min(1600-el.offsetWidth-20,x))+'px';el.style.top=Math.max(20,Math.min(900-el.offsetHeight-20,y))+'px'}
 function sync(el){const d=nodes.get(el.dataset.id).data;d.x=parseFloat(el.style.left);d.y=parseFloat(el.style.top)}
 function center(el){return[parseFloat(el.style.left)+el.offsetWidth/2,parseFloat(el.style.top)+el.offsetHeight/2]}
 function select(el,add=false){if(!add){[...nodes.values()].forEach(o=>o.el.classList.remove('selected'));selectedIds.clear()}selected=el;selectedIds.add(el.dataset.id);el.classList.add('selected');renderProps();M.textContent=selectedIds.size>1?selectedIds.size+' steg markerade.':'Markerat: '+nodes.get(el.dataset.id).data.text}
 function renderBadges(id){const o=nodes.get(id);if(!o)return;o.badges.innerHTML='';Object.entries(o.data.meta).forEach(([k,arr])=>{if(arr.length){const s=document.createElement('span');s.className='pk-badge '+k;s.textContent=({risk:'Risk',control:'Kontroll',kpi:'KPI',doc:'Dok'}[k])+' '+arr.length;o.badges.appendChild(s)}})}
 function renderProps(){
   if(!selected){P.className='pk-empty';P.textContent='Klicka på ett processsteg.';return}P.className='pk-properties';const d=nodes.get(selected.dataset.id).data;const owner=roles[laneFor(d.y,selected.offsetHeight)];
   P.innerHTML='<div class="pk-field"><label>Steg</label><input id="pp-text"></div><div class="pk-field"><label>Ansvar via swimlane</label><input id="pp-owner" disabled></div><div class="pk-meta-list" id="pp-meta"></div>';
   const ti=P.querySelector('#pp-text');ti.value=d.text;ti.addEventListener('change',()=>{snapshot();d.text=ti.value||'Namnlöst steg';nodes.get(d.id).label.textContent=d.text});P.querySelector('#pp-owner').value=owner;
   const m=P.querySelector('#pp-meta');Object.entries(d.meta).forEach(([kind,arr])=>{const title={risk:'Risker',control:'Kontroller',kpi:'KPI / mätetal',doc:'Dokument / bevis'}[kind];const wrap=document.createElement('div');wrap.className='pk-meta-row';wrap.innerHTML='<b>'+title+'</b>';if(!arr.length){const x=document.createElement('div');x.className='pk-mini';x.textContent='Dra hit från vänster.';wrap.appendChild(x)}arr.forEach((v,i)=>{const inp=document.createElement('textarea');inp.value=v;inp.style.marginTop='5px';inp.addEventListener('change',()=>{snapshot();arr[i]=inp.value;renderBadges(d.id)});wrap.appendChild(inp)});m.appendChild(wrap)});
 }
 function drawLinks(){G.innerHTML='';links.forEach(([a,b])=>{const A=nodes.get(a)?.el,B=nodes.get(b)?.el;if(!A||!B)return;let[x1,y1]=center(A),[x2,y2]=center(B),dx=x2-x1,dy=y2-y1;if(Math.abs(dx)>Math.abs(dy)){x1+=Math.sign(dx)*A.offsetWidth/2;x2-=Math.sign(dx)*B.offsetWidth/2}else{y1+=Math.sign(dy)*A.offsetHeight/2;y2-=Math.sign(dy)*B.offsetHeight/2}const mx=(x1+x2)/2,p=document.createElementNS('http://www.w3.org/2000/svg','path');p.setAttribute('class','pk-link');p.setAttribute('marker-end','url(#pk-arrow)');p.setAttribute('d','M'+x1+','+y1+' C'+mx+','+y1+' '+mx+','+y2+' '+x2+','+y2);G.appendChild(p)})}
 function addNode(type,x,y){snapshot();seq++;const text={start:'Start',process:'Ny aktivitet',decision:'Beslut?',end:'Slut',subprocess:'Ny delprocess',group:'Ny grupp / område'}[type];const el=makeNode({id:'n'+seq,type,text,x:x-90,y:y-38,meta:{risk:[],control:[],kpi:[],doc:[]}});place(el,x-90,y-38);sync(el);select(el);drawLinks()}
 R.querySelectorAll('.pk-drag').forEach(el=>{el.addEventListener('dragstart',e=>{e.dataTransfer.setData('text/plain',el.dataset.kind+':'+el.dataset.type);if(el.dataset.kind==='meta')dragMeta=el.dataset.type});el.addEventListener('dragend',()=>{dragMeta=null;[...nodes.values()].forEach(o=>o.el.classList.remove('drop-target'))})});
 C.addEventListener('dragover',e=>e.preventDefault());C.addEventListener('drop',e=>{if(e.target.closest('.pk-node'))return;const raw=e.dataTransfer.getData('text/plain');if(!raw.startsWith('node:'))return;e.preventDefault();const type=raw.split(':')[1],r=C.getBoundingClientRect();addNode(type,e.clientX-r.left+C.parentElement.scrollLeft,e.clientY-r.top+C.parentElement.scrollTop)});
 C.addEventListener('click',e=>{if(e.target===C||e.target.classList.contains('pk-lane')){[...nodes.values()].forEach(o=>o.el.classList.remove('selected'));selected=null;selectedIds.clear();renderProps()}});
 R.querySelector('#pk-delete').addEventListener('click',()=>{if(!selectedIds.size)return;snapshot();const ids=[...selectedIds];ids.forEach(id=>{nodes.get(id)?.el.remove();nodes.delete(id)});links=links.filter(l=>!selectedIds.has(l[0])&&!selectedIds.has(l[1]));selected=null;selectedIds.clear();renderProps();drawLinks()});
 R.querySelector('#pk-undo').addEventListener('click',()=>{if(!undo.length)return;redo.push(JSON.stringify(state()));restore(undo.pop())});R.querySelector('#pk-redo').addEventListener('click',()=>{if(!redo.length)return;undo.push(JSON.stringify(state()));restore(redo.pop())});
 function copySelected(){clipboard=[...selectedIds].map(id=>copy(nodes.get(id).data));M.textContent=clipboard.length?clipboard.length+' steg kopierade.':'Markera ett eller flera steg först.'}
 function pasteSelected(){if(!clipboard.length)return;snapshot();[...nodes.values()].forEach(o=>o.el.classList.remove('selected'));selectedIds.clear();clipboard.forEach(src=>{seq++;const d=copy(src);d.id='n'+seq;d.x+=40;d.y+=40;const el=makeNode(d);selectedIds.add(d.id);el.classList.add('selected');selected=el});drawLinks();renderProps();M.textContent=clipboard.length+' steg inklistrade.'}
 R.querySelector('#pk-copy').addEventListener('click',copySelected);R.querySelector('#pk-paste').addEventListener('click',pasteSelected);
 R.addEventListener('keydown',e=>{if(['INPUT','TEXTAREA','SELECT'].includes(e.target.tagName)||e.target.isContentEditable)return;if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='c'){e.preventDefault();copySelected()}if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='v'){e.preventDefault();pasteSelected()}if(e.key==='Delete'){R.querySelector('#pk-delete').click()}});
 function updateLaneLabels(){R.querySelectorAll('.pk-lane-label').forEach((el,i)=>{el.textContent=roles[i];el.dataset.index=i;el.draggable=true})}
 let laneDrag=null;R.querySelectorAll('.pk-lane-label').forEach((el,i)=>{el.draggable=true;el.dataset.index=i;el.addEventListener('dragstart',()=>laneDrag=Number(el.dataset.index));el.addEventListener('dragover',e=>e.preventDefault());el.addEventListener('drop',e=>{e.preventDefault();const to=Number(el.dataset.index);if(laneDrag===null||laneDrag===to)return;snapshot();const moved=roles.splice(laneDrag,1)[0];roles.splice(to,0,moved);updateLaneLabels();renderProps();laneDrag=null;M.textContent='Swimlanes omordnade med drag-and-drop.'})});updateLaneLabels();
 R.querySelector('#pk-auto').addEventListener('click',()=>{snapshot();let x=70;[...nodes.values()].forEach((o,i)=>{o.data.y=55+(i%5)*180;o.data.x=x+Math.floor(i/5)*270;o.el.style.left=o.data.x+'px';o.el.style.top=o.data.y+'px'});drawLinks();renderProps()});
 function dl(data,name,type){const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([data],{type}));a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1200)}
 function esc(s){return String(s??'').replace(/[&<>\"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;'}[c]||c))}
 R.querySelector('#pk-save').addEventListener('click',()=>dl(JSON.stringify(state(),null,2),'processkartan.json','application/json'));
 R.querySelector('#pk-open').addEventListener('change',async e=>{const f=e.target.files[0];if(!f)return;try{restore(await f.text());M.textContent='Projekt öppnat.'}catch{M.textContent='Kunde inte läsa projektfilen.'}e.target.value=''});
 R.querySelector('#pk-doc').addEventListener('click',()=>{const ordered=[...nodes.values()].sort((a,b)=>a.data.y-b.data.y||a.data.x-b.data.x);const rows=ordered.map((o,i)=>{const d=o.data;return '<tr><td>'+(i+1)+'</td><td>'+esc(d.text)+'</td><td>'+esc(roles[laneFor(d.y,o.el.offsetHeight)])+'</td><td>'+esc(d.meta.risk.join('; '))+'</td><td>'+esc(d.meta.control.join('; '))+'</td><td>'+esc(d.meta.kpi.join('; '))+'</td><td>'+esc(d.meta.doc.join('; '))+'</td></tr>'}).join('');const now=new Date().toLocaleDateString('sv-SE');const doc='<!doctype html><html><head><meta charset="utf-8"><style>body{font-family:Arial,sans-serif;color:#222}h1{font-size:22px}h2{font-size:16px;margin-top:24px}table{border-collapse:collapse;width:100%}th,td{border:1px solid #aaa;padding:6px;vertical-align:top;font-size:10pt}th{background:#eee}.small{color:#666;font-size:9pt}</style></head><body><h1>Processbeskrivning – Processkartan</h1><p class="small">Exporterad '+now+' · Processkartan v0.3.0</p><h2>Processöversikt</h2><p>Swimlanes / ansvar: '+roles.map(esc).join(' → ')+'</p><h2>Processsteg och ISO-information</h2><table><tr><th>#</th><th>Steg</th><th>Ansvar</th><th>Risker</th><th>Kontroller</th><th>KPI / mätetal</th><th>Dokument / bevis</th></tr>'+rows+'</table><p class="small">Ladda upp denna .doc-fil till Google Drive och välj Öppna med → Google Dokument. Processkartan kan exporteras separat som SVG och infogas i dokumentet.</p></body></html>';dl(doc,'Processkartan_Google_Docs.doc','application/msword');M.textContent='Google Docs-export skapad. Ladda upp filen till Google Drive och öppna med Google Dokument.'});
 R.querySelector('#pk-svgexport').addEventListener('click',()=>{let parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900"><rect width="100%" height="100%" fill="white"/>'];parts.push(G.innerHTML.replaceAll('url(#pk-arrow)',''));[...nodes.values()].forEach(o=>{const d=o.data,w=o.el.offsetWidth,h=o.el.offsetHeight;parts.push('<rect x="'+d.x+'" y="'+d.y+'" width="'+w+'" height="'+h+'" rx="12" fill="white" stroke="#657487" stroke-width="2"/><text x="'+(d.x+w/2)+'" y="'+(d.y+h/2)+'" text-anchor="middle" dominant-baseline="middle" font-family="Arial" font-size="13">'+esc(d.text)+'</text>')});parts.push('</svg>');dl(parts.join(''),'processkarta.svg','image/svg+xml')});
 seed.forEach(makeNode);links=seedLinks;drawLinks();
})();
</script>
'''

components.html(html, height=920, scrolling=True)
