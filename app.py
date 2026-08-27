import streamlit as st
import streamlit.components.v1 as components
from datetime import date

st.set_page_config(page_title='Processkartan', page_icon='🧭', layout='wide', initial_sidebar_state='expanded')
APP_VERSION = '0.1.0'

st.markdown('''
<style>
.block-container {padding-top:1.15rem; padding-bottom:2rem; max-width:1600px;}
[data-testid="stSidebar"] {min-width:265px; max-width:265px;}
.app-badge {display:inline-block;padding:.18rem .55rem;border-radius:999px;background:#eef6f1;color:#1f6f55;font-size:.78rem;font-weight:700;border:1px solid #cfe7dc;}
.small-muted {color:#6b7280;font-size:.88rem;}
div[data-testid="stMetric"] {border:1px solid #e5e7eb;border-radius:12px;padding:12px;background:#fff;}
</style>
''', unsafe_allow_html=True)

for key, value in {
    'process_name': 'Anbudsprocess – offentlig upphandling',
    'process_owner': 'Bid Manager',
    'revision': '0.1',
    'status': 'Utkast',
}.items():
    if key not in st.session_state:
        st.session_state[key] = value

with st.sidebar:
    st.markdown('## Processkartan')
    st.caption(f'Streamlit prototyp · v{APP_VERSION}')
    st.text_input('Processnamn', key='process_name')
    st.text_input('Processägare', key='process_owner')
    st.selectbox('Status', ['Utkast','Under granskning','Godkänd','Publicerad'], key='status')
    st.text_input('Revision', key='revision')
    st.date_input('Nästa översyn', value=date.today().replace(year=date.today().year + 1))
    st.divider()
    st.markdown('**ISO-stöd i prototypen**')
    st.caption('Processägare · roller · input/output · risker · kontroller · KPI · dokument · revisioner · godkännande')
    st.divider()
    st.caption('Själva kartan sparas som projektfil i webbläsaren. Nästa tekniska steg är databas + riktig Google Workspace-integration.')

st.title(st.session_state.process_name)
st.markdown(
    f'<span class="app-badge">{st.session_state.status}</span> '
    f'<span class="small-muted">&nbsp; Revision {st.session_state.revision} · Processägare: {st.session_state.process_owner}</span>',
    unsafe_allow_html=True,
)

tab_map, tab_risk, tab_docs, tab_rev, tab_report, tab_admin = st.tabs(
    ['Processkarta','Risker & kontroller','Dokument','Revisioner','Rapport / Export','Administration']
)

with tab_map:
    st.caption('Dra steg, skapa pilar, använd swimlanes och fyll i ISO-relevant metadata på varje processsteg.')
    html = '''
<div id="flowapp">
<style>
#flowapp{font-family:Inter,system-ui,sans-serif;color:#17202a;background:#f7f8fa;border:1px solid #dfe3e8;border-radius:14px;overflow:hidden}
#flowapp *{box-sizing:border-box}
.fa-top{display:flex;gap:7px;flex-wrap:wrap;padding:10px;background:white;border-bottom:1px solid #e2e5e9;align-items:center}
.fa-btn{border:1px solid #cbd2d9;background:white;border-radius:8px;padding:7px 10px;font:600 13px system-ui;cursor:pointer;min-height:36px}
.fa-btn:hover{background:#f2f4f6}.fa-btn.primary{background:#1f6f55;border-color:#1f6f55;color:white}.fa-btn.warn{color:#a33}
.fa-msg{margin-left:auto;color:#647080;font-size:12px}
.fa-main{display:grid;grid-template-columns:190px minmax(0,1fr) 285px;min-height:760px}
.fa-side{background:white;padding:12px;border-right:1px solid #e2e5e9}.fa-side.right{border-right:0;border-left:1px solid #e2e5e9}
.fa-side h3{font-size:13px;margin:0 0 9px}.fa-palette{display:grid;gap:7px}.fa-palette .fa-btn{text-align:left}
.fa-help{font-size:11.5px;line-height:1.45;color:#687484}
.fa-scroll{overflow:auto;background:#eef1f4}
#fa-canvas{position:relative;width:1420px;height:760px;background:#fff;touch-action:pan-x pan-y}
.fa-lane{position:absolute;left:0;width:1420px;height:152px;border-bottom:1px solid #d5dbe1}
.fa-lane:nth-child(odd){background:#fbfcfd}.fa-lane-label{position:absolute;left:10px;top:8px;font-size:12px;font-weight:800;color:#66717e;background:#fff;padding:3px 6px;border-radius:5px;border:1px solid #dde2e7}
#fa-svg{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.fa-node{position:absolute;width:185px;min-height:70px;padding:9px 10px;border:2px solid #607083;border-radius:10px;background:#fff;display:flex;align-items:center;justify-content:center;text-align:center;font-weight:700;font-size:13px;box-shadow:0 2px 6px rgba(0,0,0,.07);user-select:none;touch-action:none}
.fa-node.start,.fa-node.end{border-radius:35px}.fa-node.start{border-color:#287a5d;background:#eef9f4}.fa-node.end{border-color:#9b4f46;background:#fff3f1}
.fa-node.decision{width:140px;height:105px;min-height:105px;background:#fff8df;border-color:#ad7a15;clip-path:polygon(50% 0,100% 50%,50% 100%,0 50%);border-radius:0;padding:24px}
.fa-node.selected{outline:3px solid #2684ff;outline-offset:2px}.fa-node.source{outline:3px solid #e59618;outline-offset:2px}
.fa-field{margin-bottom:8px}.fa-field label{display:block;font-size:11px;font-weight:800;color:#616d79;margin-bottom:3px}.fa-field input,.fa-field select,.fa-field textarea{width:100%;border:1px solid #ccd3da;border-radius:7px;padding:7px;font:13px system-ui;background:#fff}.fa-field textarea{min-height:54px;resize:vertical}
.fa-row{display:grid;grid-template-columns:1fr 1fr;gap:6px}
.fa-chip{display:inline-block;background:#edf2f7;border-radius:999px;padding:2px 6px;font-size:10px;color:#536171;margin:2px}
.fa-section{margin-top:14px;padding-top:10px;border-top:1px solid #e6e9ed}.fa-empty{color:#718090;font-size:12px}
@media(max-width:900px){.fa-main{grid-template-columns:1fr}.fa-side.right{border-left:0;border-top:1px solid #e2e5e9}.fa-side{border-right:0;border-bottom:1px solid #e2e5e9}.fa-msg{width:100%;margin-left:0}}
</style>
<div class="fa-top">
  <button class="fa-btn primary" id="fa-add">+ Aktivitet</button>
  <button class="fa-btn" id="fa-link">↗ Skapa pil</button>
  <button class="fa-btn" id="fa-undo">↶ Ångra</button>
  <button class="fa-btn" id="fa-redo">↷ Gör om</button>
  <button class="fa-btn warn" id="fa-del">Ta bort</button>
  <button class="fa-btn" id="fa-save">Spara projekt</button>
  <label class="fa-btn">Öppna projekt<input id="fa-open" type="file" accept=".json,application/json" hidden></label>
  <button class="fa-btn" id="fa-doc">Google Docs (.doc)</button>
  <span class="fa-msg" id="fa-msg">Klicka på ett steg för att redigera metadata.</span>
</div>
<div class="fa-main">
  <aside class="fa-side">
    <h3>Lägg till</h3>
    <div class="fa-palette">
      <button class="fa-btn" data-add="start">Start / trigger</button>
      <button class="fa-btn" data-add="process">Aktivitet</button>
      <button class="fa-btn" data-add="decision">Beslut</button>
      <button class="fa-btn" data-add="end">Slut / överlämning</button>
    </div>
    <div class="fa-section"><h3>Swimlanes</h3><div class="fa-help">Dra varje aktivitet till den roll som ansvarar för steget.</div><div style="margin-top:8px"><span class="fa-chip">Bid / Sälj</span><span class="fa-chip">Region</span><span class="fa-chip">Kalkyl</span><span class="fa-chip">Juridik</span><span class="fa-chip">Ledning</span></div></div>
    <div class="fa-section"><h3>Snabbhjälp</h3><div class="fa-help">Dubbelklicka på en ruta för att ändra rubriken. För pil: klicka “Skapa pil”, välj från-steg och sedan till-steg.</div></div>
  </aside>
  <div class="fa-scroll">
    <div id="fa-canvas">
      <div class="fa-lane" style="top:0"><span class="fa-lane-label">Bid / Sälj</span></div>
      <div class="fa-lane" style="top:152px"><span class="fa-lane-label">Region</span></div>
      <div class="fa-lane" style="top:304px"><span class="fa-lane-label">Kalkyl</span></div>
      <div class="fa-lane" style="top:456px"><span class="fa-lane-label">Juridik</span></div>
      <div class="fa-lane" style="top:608px"><span class="fa-lane-label">Ledning</span></div>
      <svg id="fa-svg" viewBox="0 0 1420 760"><defs><marker id="arr" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><polygon points="0,0 10,4 0,8" fill="#687585"></polygon></marker></defs><g id="fa-lines"></g></svg>
    </div>
  </div>
  <aside class="fa-side right"><h3>Egenskaper / ISO-data</h3><div id="fa-props" class="fa-empty">Ingen aktivitet markerad.</div></aside>
</div>
</div>
<script>
(()=>{
const R=document.getElementById('flowapp'); if(R.dataset.ready)return; R.dataset.ready='1';
const C=R.querySelector('#fa-canvas'), L=R.querySelector('#fa-lines'), P=R.querySelector('#fa-props'), M=R.querySelector('#fa-msg');
const roles=['Bid / Sälj','Region','Kalkyl','Juridik','Ledning'];
let nodes=new Map(), links=[], selected=null, linkMode=false, source=null, seq=20, undo=[], redo=[];
const seed=[
{id:'n1',type:'start',text:'Upphandling identifieras',x:40,y:48,owner:'Bid / Sälj',input:'Annons / bevakning',output:'Identifierad möjlighet',risk:'Relevant annons missas',control:'Daglig bevakning',kpi:'Tid till första bedömning',doc:'Bevakningskälla'},
{id:'n2',type:'process',text:'Första bedömning',x:280,y:48,owner:'Bid / Sälj',input:'Annons + grunddata',output:'Preliminär relevans',risk:'Felaktig första bedömning',control:'Kvalificeringskriterier',kpi:'Andel rätt kvalificerade',doc:'Checklista'},
{id:'n3',type:'decision',text:'Relevant?',x:535,y:32,owner:'Bid / Sälj',input:'Bedömning',output:'Ja / Nej',risk:'Fel Go/No-go',control:'Fastställda kriterier',kpi:'Andel avstådda sent',doc:'Go/No-go kriterier'},
{id:'n4',type:'process',text:'Kvalificera upphandling',x:770,y:48,owner:'Bid / Sälj',input:'Upphandlingsdokument',output:'Kvalificerad möjlighet',risk:'Skallkrav missas',control:'Tvåstegsgranskning',kpi:'Ledtid kvalificering',doc:'Kvalificeringsmall'},
{id:'n5',type:'process',text:'Fördela region / ansvarig',x:1040,y:200,owner:'Region',input:'Kvalificerad möjlighet',output:'Utsedd ansvarig',risk:'Otydligt ägarskap',control:'Ansvar bekräftas',kpi:'Tid till ägarskap',doc:'Ansvarsmatris'},
{id:'n6',type:'process',text:'Kalkyl & lösning',x:790,y:350,owner:'Kalkyl',input:'Krav + volymer',output:'Kalkyl och lösning',risk:'Felaktiga antaganden',control:'Kalkylgranskning',kpi:'Kalkylavvikelse',doc:'Kalkylmall'},
{id:'n7',type:'process',text:'Juridisk / kommersiell kontroll',x:510,y:500,owner:'Juridik',input:'Avtal + anbud',output:'Granskat underlag',risk:'Avtalsrisk förbises',control:'Juridisk checklista',kpi:'Antal sena avtalsfrågor',doc:'Avtalschecklista'},
{id:'n8',type:'decision',text:'Go / No-go',x:290,y:630,owner:'Ledning',input:'Affärscase',output:'Beslut',risk:'Beslut på bristande underlag',control:'Beslutsunderlag',kpi:'Hit-rate',doc:'Beslutsmall'},
{id:'n9',type:'process',text:'Slutför & kvalitetssäkra anbud',x:50,y:350,owner:'Kalkyl',input:'Samtliga bidrag',output:'Färdigt anbud',risk:'Ofullständigt svar',control:'Fyra-ögon-princip',kpi:'Avvikelser före inlämning',doc:'QA-checklista'}
];
let seedLinks=[['n1','n2',''],['n2','n3',''],['n3','n4','Ja'],['n4','n5',''],['n5','n6',''],['n6','n7',''],['n7','n8',''],['n8','n9','Go']];
function snapshot(){return JSON.stringify({nodes:[...nodes.values()].map(n=>n.data),links});}
function pushUndo(){undo.push(snapshot());if(undo.length>40)undo.shift();redo=[];}
function loadState(s){const d=typeof s==='string'?JSON.parse(s):s;[...nodes.values()].forEach(o=>o.el.remove());nodes.clear();links=d.links||[];(d.nodes||[]).forEach(makeNode);selected=null;renderProps();draw();}
function makeNode(d){
 const data={owner:'Bid / Sälj',input:'',output:'',risk:'',control:'',kpi:'',doc:'',...d};
 const el=document.createElement('div');el.className='fa-node '+data.type;el.dataset.id=data.id;el.tabIndex=0;el.textContent=data.text;el.style.left=data.x+'px';el.style.top=data.y+'px';C.appendChild(el);nodes.set(data.id,{el,data});
 el.addEventListener('click',e=>{e.stopPropagation();if(linkMode)return connect(el);choose(el)});
 el.addEventListener('dblclick',e=>{e.stopPropagation();el.contentEditable='true';el.focus();const end=()=>{el.contentEditable='false';nodes.get(data.id).data.text=el.textContent;renderProps();draw()};el.addEventListener('blur',end,{once:true})});
 el.addEventListener('pointerdown',e=>{if(linkMode||e.button!==0||el.isContentEditable)return;choose(el);pushUndo();const sx=e.clientX,sy=e.clientY,ox=parseFloat(el.style.left),oy=parseFloat(el.style.top);el.setPointerCapture(e.pointerId);const mv=ev=>{place(el,ox+ev.clientX-sx,oy+ev.clientY-sy);syncPos(el);draw()};const up=()=>{el.removeEventListener('pointermove',mv);el.removeEventListener('pointerup',up)};el.addEventListener('pointermove',mv);el.addEventListener('pointerup',up)});
 return el;
}
function place(el,x,y){el.style.left=Math.max(0,Math.min(1420-el.offsetWidth,x))+'px';el.style.top=Math.max(0,Math.min(760-el.offsetHeight,y))+'px';}
function syncPos(el){const d=nodes.get(el.dataset.id).data;d.x=parseFloat(el.style.left);d.y=parseFloat(el.style.top);d.owner=roles[Math.max(0,Math.min(4,Math.floor((d.y+el.offsetHeight/2)/152)))];if(selected===el)renderProps();}
function choose(el){[...nodes.values()].forEach(o=>o.el.classList.remove('selected'));selected=el;el.classList.add('selected');renderProps();M.textContent='Markerat: '+nodes.get(el.dataset.id).data.text;}
function renderProps(){
 if(!selected){P.className='fa-empty';P.textContent='Ingen aktivitet markerad.';return;}P.className='';const d=nodes.get(selected.dataset.id).data;
 P.innerHTML='<div class="fa-field"><label>Rubrik</label><input id="p-text"></div><div class="fa-row"><div class="fa-field"><label>Typ</label><select id="p-type"><option value="process">Aktivitet</option><option value="start">Start</option><option value="decision">Beslut</option><option value="end">Slut</option></select></div><div class="fa-field"><label>Ansvarig roll</label><select id="p-owner">'+roles.map(r=>'<option>'+r+'</option>').join('')+'</select></div></div><div class="fa-field"><label>Input</label><textarea id="p-input"></textarea></div><div class="fa-field"><label>Output</label><textarea id="p-output"></textarea></div><div class="fa-field"><label>Risk</label><textarea id="p-risk"></textarea></div><div class="fa-field"><label>Kontroll / styrning</label><textarea id="p-control"></textarea></div><div class="fa-field"><label>KPI / mätetal</label><input id="p-kpi"></div><div class="fa-field"><label>Dokument / bevis</label><input id="p-doc"></div>';
 const map={text:'p-text',type:'p-type',owner:'p-owner',input:'p-input',output:'p-output',risk:'p-risk',control:'p-control',kpi:'p-kpi',doc:'p-doc'};
 Object.entries(map).forEach(([k,id])=>{const q=P.querySelector('#'+id);q.value=d[k]||'';q.addEventListener('change',()=>{pushUndo();d[k]=q.value;if(k==='text')selected.textContent=q.value;if(k==='type')selected.className='fa-node '+q.value+' selected';draw()});});
}
function connect(el){if(!source){source=el;el.classList.add('source');M.textContent='Välj vart pilen ska gå.';return;}if(source===el){source.classList.remove('source');source=null;return;}pushUndo();links.push([source.dataset.id,el.dataset.id,'']);source.classList.remove('source');source=null;linkMode=false;R.querySelector('#fa-link').classList.remove('primary');M.textContent='Pil skapad.';draw();}
function center(el){return[parseFloat(el.style.left)+el.offsetWidth/2,parseFloat(el.style.top)+el.offsetHeight/2]}
function draw(){L.innerHTML='';links.forEach(([a,b,label])=>{const A=nodes.get(a)?.el,B=nodes.get(b)?.el;if(!A||!B)return;let[x1,y1]=center(A),[x2,y2]=center(B),dx=x2-x1,dy=y2-y1;if(Math.abs(dx)>Math.abs(dy)){x1+=Math.sign(dx)*A.offsetWidth/2;x2-=Math.sign(dx)*B.offsetWidth/2}else{y1+=Math.sign(dy)*A.offsetHeight/2;y2-=Math.sign(dy)*B.offsetHeight/2}const mx=(x1+x2)/2,p=document.createElementNS('http://www.w3.org/2000/svg','path');p.setAttribute('d','M'+x1+','+y1+' C'+mx+','+y1+' '+mx+','+y2+' '+x2+','+y2);p.setAttribute('fill','none');p.setAttribute('stroke','#687585');p.setAttribute('stroke-width','2.2');p.setAttribute('marker-end','url(#arr)');L.appendChild(p);if(label){const t=document.createElementNS('http://www.w3.org/2000/svg','text');t.setAttribute('x',mx+5);t.setAttribute('y',(y1+y2)/2-5);t.setAttribute('font-size','12');t.setAttribute('fill','#4f5966');t.textContent=label;L.appendChild(t)}})}
function add(type){pushUndo();seq++;choose(makeNode({id:'n'+seq,type,text:type==='decision'?'Beslut?':type==='start'?'Start':type==='end'?'Slut':'Ny aktivitet',x:420+Math.random()*80,y:60+Math.random()*60,owner:'Bid / Sälj'}));draw();}
function dl(data,name,type){const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([data],{type}));a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000)}
function esc(s){return String(s??'').replace(/[&<>\"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;'}[c]))}
function reportDoc(){const rows=[...nodes.values()].map(o=>o.data).map(d=>'<tr><td>'+esc(d.text)+'</td><td>'+esc(d.owner)+'</td><td>'+esc(d.input)+'</td><td>'+esc(d.output)+'</td><td>'+esc(d.risk)+'</td><td>'+esc(d.control)+'</td><td>'+esc(d.kpi)+'</td><td>'+esc(d.doc)+'</td></tr>').join('');return '<!DOCTYPE html><html><head><meta charset="utf-8"><style>body{font-family:Arial,sans-serif}table{border-collapse:collapse;width:100%}td,th{border:1px solid #999;padding:6px;font-size:10pt}th{background:#eee}h1{font-size:18pt}</style></head><body><h1>Processbeskrivning</h1><p>Exporterad från Processkartan.</p><table><tr><th>Steg</th><th>Ansvar</th><th>Input</th><th>Output</th><th>Risk</th><th>Kontroll</th><th>KPI</th><th>Dokument</th></tr>'+rows+'</table></body></html>';}
R.querySelectorAll('[data-add]').forEach(b=>b.addEventListener('click',()=>add(b.dataset.add)));R.querySelector('#fa-add').addEventListener('click',()=>add('process'));
R.querySelector('#fa-link').addEventListener('click',e=>{linkMode=!linkMode;e.currentTarget.classList.toggle('primary',linkMode);if(source){source.classList.remove('source');source=null}M.textContent=linkMode?'Välj från-steg och sedan till-steg.':'Pil-läge av.'});
R.querySelector('#fa-del').addEventListener('click',()=>{if(!selected)return;pushUndo();const id=selected.dataset.id;selected.remove();nodes.delete(id);links=links.filter(x=>x[0]!==id&&x[1]!==id);selected=null;renderProps();draw();});
R.querySelector('#fa-undo').addEventListener('click',()=>{if(!undo.length)return;redo.push(snapshot());loadState(undo.pop())});R.querySelector('#fa-redo').addEventListener('click',()=>{if(!redo.length)return;undo.push(snapshot());loadState(redo.pop())});
R.querySelector('#fa-save').addEventListener('click',()=>dl(snapshot(),'processkarta.json','application/json'));R.querySelector('#fa-doc').addEventListener('click',()=>dl(reportDoc(),'processbeskrivning_google_docs.doc','application/msword'));
R.querySelector('#fa-open').addEventListener('change',async e=>{const f=e.target.files[0];if(!f)return;try{loadState(await f.text());M.textContent='Projekt öppnat.'}catch{M.textContent='Projektfilen kunde inte läsas.'}e.target.value=''});
C.addEventListener('click',()=>{if(!linkMode){[...nodes.values()].forEach(o=>o.el.classList.remove('selected'));selected=null;renderProps()}});
seed.forEach(makeNode);links=seedLinks;draw();
})();
</script>
'''
    components.html(html, height=850, scrolling=True)

with tab_risk:
    st.subheader('Risker & kontroller')
    st.info('I kartan kan varje steg redan ha risk och kontroll. Den här fliken visar den centrala riskvyn som ska kopplas till databasen i nästa version.')
    st.dataframe({
        'Risk':['Relevant upphandling missas','Skallkrav missas','Felaktiga kalkylantaganden','Avtalsrisk förbises'],
        'Processsteg':['Upphandling identifieras','Kvalificera upphandling','Kalkyl & lösning','Juridisk kontroll'],
        'Kontroll':['Daglig bevakning','Tvåstegsgranskning','Kalkylgranskning','Juridisk checklista'],
        'Ansvar':['Bid / Sälj','Bid / Sälj','Kalkyl','Juridik']
    }, use_container_width=True, hide_index=True)
    st.caption('Nästa version: sannolikhet × konsekvens, riskägare, åtgärd, deadline, status och residualrisk.')

with tab_docs:
    st.subheader('Dokument och bevis')
    st.write('Här ska processsteg kunna länkas till styrande dokument, mallar, checklistor och verifierbara bevis.')
    st.text_input('Google Drive / dokumentlänk', placeholder='Klistra in länk till styrande dokument')
    st.selectbox('Dokumenttyp', ['Mall','Checklista','Instruktion','Policy','Avtal','Bevis / record'])
    st.button('Koppla dokument', disabled=True, help='Aktiveras när databasen och stegkopplingen är på plats.')

with tab_rev:
    st.subheader('Revisioner och godkännande')
    c1,c2,c3,c4=st.columns(4)
    c1.metric('Revision',st.session_state.revision); c2.metric('Status',st.session_state.status); c3.metric('Processägare',st.session_state.process_owner); c4.metric('Översyn','Årlig')
    st.dataframe({'Version':['0.1'],'Datum':[str(date.today())],'Ändring':['Första Streamlit-prototyp'],'Status':['Utkast'],'Godkänd av':['–']},use_container_width=True,hide_index=True)

with tab_report:
    st.subheader('Rapport / Export')
    st.markdown('''
**Google Docs:** Processkartan har en knapp för att exportera metadata till ett Word-kompatibelt `.doc`-dokument som kan laddas upp och öppnas i Google Docs.

**Google Slides / Drawings:** Nästa version bör exportera själva kartan som SVG/PNG. Riktig redigerbar Google-export kräver Google Workspace API + OAuth.

**ISO-rapport:** Nästa version kan generera en sammanhängande processbeskrivning med ansvar, input/output, risker, kontroller, KPI, dokument och revisionshistorik.
''')
    st.warning('Direkt Google-API-export är medvetet inte påslagen ännu eftersom den kräver Google-autentisering och behörighetsstyrning.')

with tab_admin:
    st.subheader('Administration')
    st.toggle('Kräv godkännande före publicering',value=True)
    st.toggle('Behåll historiska revisioner',value=True)
    st.toggle('Kräv processägare',value=True)
    st.toggle('Kräv risk/kontroll på kritiska steg',value=True)
    st.selectbox('Standard för processstyrning',['ISO 9001-inspirerad','Egen modell'])
    st.caption('I produktionsversionen flyttas detta till databas, behörighetsmodell och audit log.')
