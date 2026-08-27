import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Processkartan",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

APP_VERSION = "0.4.4"

st.markdown("""
<style>
.block-container{padding:0.35rem 0.45rem 0.8rem;max-width:none}
header[data-testid="stHeader"]{height:2rem}
#MainMenu,footer{visibility:hidden}
</style>
""", unsafe_allow_html=True)

st.markdown(f"**Processkartan** · v{APP_VERSION}")

html = r"""
<div id="pk">
<style>
#pk{font-family:Inter,system-ui,sans-serif;color:#17202a;background:#eef2f6;border:1px solid #dce2e8;border-radius:12px;overflow:hidden}
#pk *{box-sizing:border-box}
.pk-top{display:flex;gap:8px;align-items:center;flex-wrap:wrap;padding:10px;background:#fff;border-bottom:1px solid #dce2e8}
.pk-btn{border:1px solid #ccd4dc;background:#fff;color:#24303d;border-radius:8px;min-height:38px;padding:8px 11px;font:600 13px system-ui;cursor:pointer}
.pk-btn:hover{background:#f2f5f7}.pk-btn.primary{background:#1f6f55;color:#fff;border-color:#1f6f55}
.pk-name{font:800 14px system-ui;border:2px solid #8aa2b8;border-radius:8px;padding:8px 10px;min-width:300px;background:#fbfdff}
.pk-spacer{flex:1}
.pk-body{display:grid;grid-template-columns:180px minmax(0,1fr);min-height:900px}
.pk-palette{background:#fff;border-right:1px solid #dce2e8;padding:10px}
.pk-title{font-size:12px;font-weight:800;margin-bottom:8px}
.pk-sub{font-size:11px;color:#6c7784;line-height:1.45;margin-bottom:10px}
.pk-item{display:flex;align-items:center;gap:8px;border:1px solid #d0d7df;background:#fff;border-radius:9px;padding:10px;margin-bottom:7px;cursor:grab;font-size:12.5px;font-weight:700;user-select:none}
.pk-item:active{cursor:grabbing}
.pk-icon{width:23px;height:23px;border-radius:6px;background:#edf2f6;display:grid;place-items:center;font-size:11px}
.pk-tip{margin-top:12px;padding:8px;border-radius:8px;background:#f2f6f4;color:#4c655c;font-size:10.8px;line-height:1.45}
.pk-scroll{overflow:auto;background:#e9eef3}
#pk-canvas{position:relative;width:2400px;height:1400px;background:#fff;touch-action:none;background-image:radial-gradient(#dce2e8 1px,transparent 1px);background-size:20px 20px}
#pk-svg{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:2}
.pk-link{stroke:#687584;stroke-width:2.2;fill:none}
.pk-temp{stroke:#df941e;stroke-width:2.4;fill:none;stroke-dasharray:6 5}
.pk-node{position:absolute;width:190px;min-height:76px;padding:12px 24px;border:2px solid #637387;border-radius:10px;background:#fff;box-shadow:0 3px 9px rgba(31,42,55,.10);z-index:5;user-select:none;touch-action:none;font-size:13px;font-weight:750;text-align:center;display:flex;align-items:center;justify-content:center}
.pk-node.start,.pk-node.end{border-radius:38px}
.pk-node.start{border-color:#2b7b61;background:#edf8f3}
.pk-node.end{border-color:#985148;background:#fff3f1}
.pk-node.decision{width:145px;height:110px;min-height:110px;padding:28px 20px;border-color:#a97a20;background:#fff8df;clip-path:polygon(50% 0,100% 50%,50% 100%,0 50%);border-radius:0}
.pk-node.subprocess{border-style:double;border-width:4px;background:#f7f3ff;border-color:#7556a6}
.pk-node.note{background:#fffbe8;border-color:#b8973e;font-weight:600}
.pk-node.group{width:260px;min-height:120px;border-style:dashed;background:#f8fafc;color:#536171}
.pk-node.selected{outline:3px solid #2c7be5;outline-offset:3px}
.pk-handle{position:absolute;width:16px;height:16px;border-radius:50%;background:#1f6f55;border:3px solid #fff;box-shadow:0 0 0 1px #1f6f55;cursor:crosshair;z-index:8}
.pk-handle.right{right:-8px;top:50%;transform:translateY(-50%)}
.pk-handle.left{left:-8px;top:50%;transform:translateY(-50%)}
.pk-handle.top{top:-8px;left:50%;transform:translateX(-50%)}
.pk-handle.bottom{bottom:-8px;left:50%;transform:translateX(-50%)}
.pk-node.decision .pk-handle.right{right:4px}.pk-node.decision .pk-handle.left{left:4px}.pk-node.decision .pk-handle.top{top:4px}.pk-node.decision .pk-handle.bottom{bottom:4px}
.pk-edit{position:absolute;left:6px;top:6px;width:20px;height:20px;border-radius:6px;border:1px solid #d3dae2;background:#fff;font-size:11px;display:none;place-items:center;cursor:pointer}
.pk-node.selected .pk-edit{display:grid}
.pk-status{font-size:12px;color:#667382;padding:0 4px}
@media(max-width:850px){.pk-body{grid-template-columns:1fr}.pk-palette{border-right:0;border-bottom:1px solid #dce2e8;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}.pk-title,.pk-sub,.pk-tip{grid-column:1/-1}.pk-item{margin-bottom:0}}
</style>

<div class="pk-top">
  <strong>Process</strong>
  <input id="pk-name" class="pk-name" value="Exempel – upphandlingsprocess" aria-label="Processnamn">
  <button type="button" class="pk-btn primary" id="pk-new">+ Ny process</button>
  <button type="button" class="pk-btn" id="pk-save">Spara</button>
  <button type="button" class="pk-btn" id="pk-undo">↶ Ångra</button>
  <button type="button" class="pk-btn" id="pk-redo">↷ Gör om</button>
  <span class="pk-spacer"></span>
  <button type="button" class="pk-btn primary" id="pk-doc">Exportera till Google Docs</button>
  <span id="pk-status" class="pk-status" aria-live="polite"></span>
</div>

<div class="pk-body">
  <aside class="pk-palette">
    <div class="pk-title">Dra till arbetsytan</div>
    <div class="pk-sub">Dra ett objekt och släpp det var du vill på canvasen.</div>
    <div class="pk-item" draggable="true" data-type="start"><span class="pk-icon">▶</span>Start</div>
    <div class="pk-item" draggable="true" data-type="process"><span class="pk-icon">□</span>Aktivitet</div>
    <div class="pk-item" draggable="true" data-type="decision"><span class="pk-icon">◇</span>Beslut</div>
    <div class="pk-item" draggable="true" data-type="end"><span class="pk-icon">■</span>Slut</div>
    <div class="pk-item" draggable="true" data-type="subprocess"><span class="pk-icon">▣</span>Delprocess</div>
    <div class="pk-item" draggable="true" data-type="group"><span class="pk-icon">G</span>Grupp / område</div>
    <div class="pk-item" draggable="true" data-type="note"><span class="pk-icon">N</span>Anteckning</div>
    <div class="pk-tip"><b>Pilar:</b> dra från någon av de fyra gröna punkterna på en ruta till en annan ruta.<br><br><b>Text:</b> dubbelklicka på en ruta för att ändra texten.<br><br><b>Ta bort:</b> markera ruta och tryck Delete.</div>
  </aside>

  <main class="pk-scroll" id="pk-scroll">
    <div id="pk-canvas">
      <svg id="pk-svg" viewBox="0 0 2400 1400">
        <defs>
          <marker id="pk-arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
            <polygon points="0,0 10,4 0,8" fill="#687584"></polygon>
          </marker>
        </defs>
        <g id="pk-links"></g>
        <path id="pk-temp" class="pk-temp" d="" hidden></path>
      </svg>
    </div>
  </main>
</div>

<script>
(()=>{
  const root = document.getElementById('pk');
  if (!root || root.dataset.ready === '1') return;
  root.dataset.ready = '1';

  const canvas = root.querySelector('#pk-canvas');
  const scroll = root.querySelector('#pk-scroll');
  const linksLayer = root.querySelector('#pk-links');
  const tempLine = root.querySelector('#pk-temp');
  const nameInput = root.querySelector('#pk-name');
  const status = root.querySelector('#pk-status');

  let nodes = new Map();
  let links = [];
  let selectedId = null;
  let seq = 8;
  let undoStack = [];
  let redoStack = [];
  let currentProcessId = 'proc-1';
  let processes = {};

  const starter = {
    id: 'proc-1',
    name: 'Exempel – upphandlingsprocess',
    nodes: [
      {id:'n1',type:'start',text:'Upphandling identifieras',x:100,y:130},
      {id:'n2',type:'process',text:'Första bedömning',x:390,y:130},
      {id:'n3',type:'decision',text:'Relevant?',x:680,y:110},
      {id:'n4',type:'process',text:'Kvalificera upphandling',x:950,y:130},
      {id:'n5',type:'process',text:'Fördela ansvar',x:1240,y:130},
      {id:'n6',type:'process',text:'Kalkyl & lösning',x:1240,y:360},
      {id:'n7',type:'process',text:'Kvalitetssäkra',x:950,y:360},
      {id:'n8',type:'end',text:'Lämna anbud',x:660,y:360}
    ],
    links: [
      ['n1','n2','right'],['n2','n3','right'],['n3','n4','right'],
      ['n4','n5','right'],['n5','n6','bottom'],['n6','n7','left'],['n7','n8','left']
    ]
  };

  function clone(value) {
    return JSON.parse(JSON.stringify(value));
  }

  function setStatus(text) {
    status.textContent = text || '';
    if (text) {
      window.setTimeout(() => {
        if (status.textContent === text) status.textContent = '';
      }, 2200);
    }
  }

  function uid(prefix) {
    return prefix + '-' + Date.now().toString(36) + '-' + Math.random().toString(36).slice(2,7);
  }

  function currentState() {
    return {
      id: currentProcessId,
      name: nameInput.value.trim() || 'Namnlös process',
      nodes: Array.from(nodes.values()).map(item => clone(item.data)),
      links: clone(links)
    };
  }

  function saveBrowser() {
    try {
      localStorage.setItem('processkartan_v044', JSON.stringify({currentProcessId, processes}));
    } catch (e) {}
  }

  function loadBrowser() {
    try {
      const raw = localStorage.getItem('processkartan_v044');
      if (!raw) return false;
      const parsed = JSON.parse(raw);
      if (!parsed.processes || !Object.keys(parsed.processes).length) return false;
      processes = parsed.processes;
      currentProcessId = parsed.currentProcessId && processes[parsed.currentProcessId]
        ? parsed.currentProcessId
        : Object.keys(processes)[0];
      return true;
    } catch (e) {
      return false;
    }
  }

  function persistCurrent(showMessage=false) {
    const state = currentState();
    processes[currentProcessId] = clone(state);
    saveBrowser();
    if (showMessage) setStatus('Sparad');
  }

  function pushUndo() {
    undoStack.push(JSON.stringify(currentState()));
    if (undoStack.length > 50) undoStack.shift();
    redoStack = [];
  }

  function clearCanvas() {
    for (const item of nodes.values()) item.el.remove();
    nodes.clear();
    links = [];
    selectedId = null;
    linksLayer.innerHTML = '';
  }

  function restoreState(state) {
    const data = typeof state === 'string' ? JSON.parse(state) : clone(state);
    clearCanvas();
    currentProcessId = data.id || currentProcessId;
    nameInput.value = data.name || 'Namnlös process';
    for (const node of (data.nodes || [])) makeNode(node);
    links = data.links || [];
    seq = Math.max(0, ...Array.from(nodes.keys()).map(id => parseInt(String(id).replace(/\D/g,''), 10) || 0));
    drawLinks();
  }

  function openCurrentProcess() {
    if (!processes[currentProcessId]) return;
    restoreState(processes[currentProcessId]);
  }

  function nodeDefaultText(type) {
    return {
      start:'Start',
      process:'Ny aktivitet',
      decision:'Beslut?',
      end:'Slut',
      subprocess:'Ny delprocess',
      group:'Ny grupp / område',
      note:'Anteckning'
    }[type] || 'Nytt steg';
  }

  function place(el, x, y) {
    const snap = 20;
    const nx = Math.round(x / snap) * snap;
    const ny = Math.round(y / snap) * snap;
    el.style.left = Math.max(10, Math.min(2400 - el.offsetWidth - 10, nx)) + 'px';
    el.style.top = Math.max(10, Math.min(1400 - el.offsetHeight - 10, ny)) + 'px';
  }

  function syncPosition(el) {
    const item = nodes.get(el.dataset.id);
    if (!item) return;
    item.data.x = parseFloat(el.style.left) || 0;
    item.data.y = parseFloat(el.style.top) || 0;
  }

  function center(el) {
    return [
      (parseFloat(el.style.left) || 0) + el.offsetWidth / 2,
      (parseFloat(el.style.top) || 0) + el.offsetHeight / 2
    ];
  }

  function anchor(el, side) {
    const x = parseFloat(el.style.left) || 0;
    const y = parseFloat(el.style.top) || 0;
    const w = el.offsetWidth;
    const h = el.offsetHeight;
    if (side === 'left') return [x, y + h/2];
    if (side === 'top') return [x + w/2, y];
    if (side === 'bottom') return [x + w/2, y + h];
    return [x + w, y + h/2];
  }

  function bestSourceSide(a, b) {
    const [ax, ay] = center(a);
    const [bx, by] = center(b);
    const dx = bx - ax;
    const dy = by - ay;
    if (Math.abs(dx) >= Math.abs(dy)) return dx >= 0 ? 'right' : 'left';
    return dy >= 0 ? 'bottom' : 'top';
  }

  function bestTargetSide(a, b) {
    const source = bestSourceSide(a, b);
    if (source === 'right') return 'left';
    if (source === 'left') return 'right';
    if (source === 'bottom') return 'top';
    return 'bottom';
  }

  function selectNode(el) {
    for (const item of nodes.values()) item.el.classList.remove('selected');
    selectedId = el.dataset.id;
    el.classList.add('selected');
  }

  function editNode(el) {
    const item = nodes.get(el.dataset.id);
    if (!item) return;
    const next = prompt('Text i steget:', item.data.text);
    if (next === null) return;
    pushUndo();
    item.data.text = next.trim() || item.data.text;
    item.label.textContent = item.data.text;
    persistCurrent();
  }

  function makeNode(data) {
    const d = clone(data);
    const el = document.createElement('div');
    el.className = 'pk-node ' + d.type;
    el.dataset.id = d.id;
    el.style.left = d.x + 'px';
    el.style.top = d.y + 'px';
    el.tabIndex = 0;

    const label = document.createElement('span');
    label.textContent = d.text;
    el.appendChild(label);

    const edit = document.createElement('button');
    edit.type = 'button';
    edit.className = 'pk-edit';
    edit.textContent = '✎';
    edit.title = 'Redigera text';
    el.appendChild(edit);

    const handles = {};
    for (const side of ['right','left','top','bottom']) {
      const h = document.createElement('span');
      h.className = 'pk-handle ' + side;
      h.dataset.side = side;
      h.title = 'Dra pil';
      el.appendChild(h);
      handles[side] = h;
    }

    canvas.appendChild(el);
    nodes.set(d.id, {el, data:d, label, handles});

    edit.addEventListener('click', event => {
      event.stopPropagation();
      editNode(el);
    });

    el.addEventListener('dblclick', event => {
      event.stopPropagation();
      editNode(el);
    });

    el.addEventListener('click', event => {
      event.stopPropagation();
      selectNode(el);
    });

    el.addEventListener('pointerdown', event => {
      if (event.button !== 0) return;
      if (event.target === edit || event.target.classList.contains('pk-handle')) return;

      selectNode(el);
      pushUndo();

      const sx = event.clientX;
      const sy = event.clientY;
      const ox = parseFloat(el.style.left) || 0;
      const oy = parseFloat(el.style.top) || 0;

      el.setPointerCapture(event.pointerId);

      const move = ev => {
        place(el, ox + ev.clientX - sx, oy + ev.clientY - sy);
        syncPosition(el);
        drawLinks();
      };

      const up = ev => {
        el.removeEventListener('pointermove', move);
        el.removeEventListener('pointerup', up);
        persistCurrent();
      };

      el.addEventListener('pointermove', move);
      el.addEventListener('pointerup', up);
    });

    for (const handle of Object.values(handles)) {
      handle.addEventListener('pointerdown', event => {
        event.stopPropagation();
        event.preventDefault();

        const side = handle.dataset.side;
        const [x1, y1] = anchor(el, side);
        tempLine.hidden = false;
        tempLine.setAttribute('d', `M${x1},${y1} L${x1},${y1}`);

        const move = ev => {
          const rect = canvas.getBoundingClientRect();
          const x2 = ev.clientX - rect.left + scroll.scrollLeft;
          const y2 = ev.clientY - rect.top + scroll.scrollTop;
          tempLine.setAttribute('d', `M${x1},${y1} L${x2},${y2}`);
        };

        const up = ev => {
          document.removeEventListener('pointermove', move);
          document.removeEventListener('pointerup', up);
          tempLine.hidden = true;

          const target = document.elementFromPoint(ev.clientX, ev.clientY)?.closest('.pk-node');
          if (target && target !== el) {
            pushUndo();
            links.push([el.dataset.id, target.dataset.id, side]);
            drawLinks();
            persistCurrent();
          }
        };

        document.addEventListener('pointermove', move);
        document.addEventListener('pointerup', up);
      });
    }

    return el;
  }

  function addNode(type, x, y) {
    pushUndo();
    seq += 1;
    const el = makeNode({
      id: 'n' + seq,
      type,
      text: nodeDefaultText(type),
      x: x - 90,
      y: y - 38
    });
    place(el, x - 90, y - 38);
    syncPosition(el);
    selectNode(el);
    drawLinks();
    persistCurrent();
  }

  function drawLinks() {
    linksLayer.innerHTML = '';
    for (const link of links) {
      const [fromId, toId, savedSide] = link;
      const from = nodes.get(fromId)?.el;
      const to = nodes.get(toId)?.el;
      if (!from || !to) continue;

      const sourceSide = savedSide || bestSourceSide(from, to);
      const targetSide = bestTargetSide(from, to);
      const [x1, y1] = anchor(from, sourceSide);
      const [x2, y2] = anchor(to, targetSide);

      const path = document.createElementNS('http://www.w3.org/2000/svg','path');
      path.setAttribute('class','pk-link');
      path.setAttribute('marker-end','url(#pk-arrow)');
      path.setAttribute('d', `M${x1},${y1} L${x2},${y2}`);
      linksLayer.appendChild(path);
    }
  }

  function deleteSelected() {
    if (!selectedId || !nodes.has(selectedId)) return;
    pushUndo();
    nodes.get(selectedId).el.remove();
    nodes.delete(selectedId);
    links = links.filter(link => link[0] !== selectedId && link[1] !== selectedId);
    selectedId = null;
    drawLinks();
    persistCurrent();
  }

  function newProcess() {
    persistCurrent();
    const name = prompt('Namn på den nya processen:', 'Ny process');
    if (name === null) return;
    currentProcessId = uid('proc');
    processes[currentProcessId] = {
      id: currentProcessId,
      name: name.trim() || 'Ny process',
      nodes: [],
      links: []
    };
    undoStack = [];
    redoStack = [];
    restoreState(processes[currentProcessId]);
    scroll.scrollLeft = 0;
    scroll.scrollTop = 0;
    saveBrowser();
    setStatus('Ny process skapad');
  }

  function exportGoogleDoc() {
    persistCurrent();
    const state = currentState();
    const ordered = Array.from(nodes.values()).sort((a,b) => a.data.y - b.data.y || a.data.x - b.data.x);
    const esc = value => String(value ?? '').replace(/[&<>"]/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[ch]));
    const typeName = {
      start:'Start',process:'Aktivitet',decision:'Beslut',end:'Slut',
      subprocess:'Delprocess',group:'Grupp / område',note:'Anteckning'
    };
    const rows = ordered.map((item, index) =>
      `<tr><td>${index+1}</td><td>${esc(item.data.text)}</td><td>${esc(typeName[item.data.type] || item.data.type)}</td></tr>`
    ).join('');
    const connections = links.map(link => {
      const a = nodes.get(link[0])?.data.text || link[0];
      const b = nodes.get(link[1])?.data.text || link[1];
      return `<li>${esc(a)} → ${esc(b)}</li>`;
    }).join('');

    const doc = `<!doctype html><html><head><meta charset="utf-8"><style>
      body{font-family:Arial,sans-serif;color:#222}h1{font-size:22px}h2{font-size:16px;margin-top:24px}
      table{border-collapse:collapse;width:100%}th,td{border:1px solid #aaa;padding:7px;font-size:10pt}th{background:#eee}
    </style></head><body>
      <h1>${esc(state.name)}</h1>
      <h2>Processsteg</h2>
      <table><tr><th>#</th><th>Steg</th><th>Typ</th></tr>${rows}</table>
      <h2>Kopplingar</h2><ul>${connections}</ul>
    </body></html>`;

    const blob = new Blob([doc], {type:'application/msword'});
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = (state.name.replace(/[^a-z0-9åäö_-]+/gi,'_') || 'Processkartan') + '_Google_Docs.doc';
    a.click();
    setTimeout(() => URL.revokeObjectURL(a.href), 1200);
    setStatus('Google Docs-export skapad');
  }

  root.querySelectorAll('.pk-item').forEach(item => {
    item.addEventListener('dragstart', event => {
      event.dataTransfer.setData('text/plain', item.dataset.type);
      event.dataTransfer.effectAllowed = 'copy';
    });
  });

  canvas.addEventListener('dragover', event => {
    event.preventDefault();
    event.dataTransfer.dropEffect = 'copy';
  });

  canvas.addEventListener('drop', event => {
    event.preventDefault();
    const type = event.dataTransfer.getData('text/plain');
    if (!type) return;
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left + scroll.scrollLeft;
    const y = event.clientY - rect.top + scroll.scrollTop;
    addNode(type, x, y);
  });

  canvas.addEventListener('click', event => {
    if (event.target === canvas) {
      for (const item of nodes.values()) item.el.classList.remove('selected');
      selectedId = null;
    }
  });

  nameInput.addEventListener('change', () => {
    persistCurrent();
    setStatus('Namn sparat');
  });

  root.querySelector('#pk-new').addEventListener('click', newProcess);
  root.querySelector('#pk-save').addEventListener('click', () => persistCurrent(true));

  root.querySelector('#pk-undo').addEventListener('click', () => {
    if (!undoStack.length) return;
    redoStack.push(JSON.stringify(currentState()));
    restoreState(undoStack.pop());
    persistCurrent();
  });

  root.querySelector('#pk-redo').addEventListener('click', () => {
    if (!redoStack.length) return;
    undoStack.push(JSON.stringify(currentState()));
    restoreState(redoStack.pop());
    persistCurrent();
  });

  root.querySelector('#pk-doc').addEventListener('click', exportGoogleDoc);

  root.addEventListener('keydown', event => {
    if (['INPUT','TEXTAREA','SELECT'].includes(event.target.tagName)) return;
    if (event.key === 'Delete') deleteSelected();
  });

  if (!loadBrowser()) {
    processes[starter.id] = clone(starter);
    currentProcessId = starter.id;
  }
  openCurrentProcess();
  setStatus('Klar');
})();
</script>
</div>
"""
components.html(html, height=990, scrolling=True)
