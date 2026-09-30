(function(global){
'use strict';
function clone(v){return JSON.parse(JSON.stringify(v))}
function emptyProcess(id,name){const raw={id:String(id||'proc-1'),name:String(name||'Ny process'),nodes:[],links:[]};return global.MapliniStateCore?global.MapliniStateCore.normalizeProcess(raw,raw.id):raw}
function addNode(process,node){const p=clone(process||emptyProcess('proc-1','Ny process'));p.nodes=Array.isArray(p.nodes)?p.nodes:[];p.nodes.push(clone(node));return global.MapliniStateCore?global.MapliniStateCore.normalizeProcess(p,p.id):p}
function updateNode(process,id,patch){const p=clone(process);p.nodes=(p.nodes||[]).map(n=>n.id===id?Object.assign({},n,clone(patch||{})):n);return global.MapliniStateCore?global.MapliniStateCore.normalizeProcess(p,p.id):p}
function connect(process,sourceId,targetId,side,stylePatch){const p=clone(process),link=global.MapliniConnectorCore?global.MapliniConnectorCore.create(sourceId,targetId,side,stylePatch):[sourceId,targetId,side||'right',stylePatch||{}];p.links=(p.links||[]).concat([link]);return global.MapliniStateCore?global.MapliniStateCore.normalizeProcess(p,p.id):p}
function deleteNodes(process,ids){const p=clone(process),doomed=new Set(ids||[]);p.nodes=(p.nodes||[]).filter(n=>!doomed.has(n.id));p.links=global.MapliniConnectorCore?global.MapliniConnectorCore.removeSelected(p.links,doomed,new Set()):(p.links||[]).filter(l=>!doomed.has(l[0])&&!doomed.has(l[1]));return global.MapliniStateCore?global.MapliniStateCore.normalizeProcess(p,p.id):p}
function snapshot(process){return JSON.stringify(global.MapliniStateCore?global.MapliniStateCore.normalizeProcess(process,process?.id):process)}
function restore(value){const raw=typeof value==='string'?JSON.parse(value):clone(value);return global.MapliniStateCore?global.MapliniStateCore.normalizeProcess(raw,raw?.id):raw}
function pushHistory(history,process,max=100){const out=Array.isArray(history)?history.slice():[],snap=snapshot(process);if(out[out.length-1]!==snap)out.push(snap);while(out.length>max)out.shift();return out}
function undoState(history,current){const h=Array.isArray(history)?history.slice():[];if(!h.length)return {history:h,process:clone(current),redo:null};const previous=h.pop();return {history:h,process:restore(previous),redo:snapshot(current)}}
function validateCriticalFlow(process){
  const p=global.MapliniStateCore?global.MapliniStateCore.normalizeProcess(process,process?.id):process;
  if(!p||!p.id||!Array.isArray(p.nodes)||!Array.isArray(p.links))return {ok:false,nodeCount:0,linkCount:0,orphanLinks:0,disconnectedNodes:0,duplicateNodeIds:0};
  const ids=new Set(),duplicates=new Set();
  for(const n of p.nodes){const id=String(n?.id||'');if(ids.has(id))duplicates.add(id);if(id)ids.add(id)}
  const validLinks=[],orphanLinks=[];
  for(const l of p.links){if(!Array.isArray(l)||!ids.has(l[0])||!ids.has(l[1]))orphanLinks.push(l);else validLinks.push(l)}
  const connected=new Set();
  for(const l of validLinks){connected.add(l[0]);connected.add(l[1])}
  const disconnectedNodes=p.nodes.filter(n=>p.nodes.length>1&&!connected.has(n.id)).length;
  return {
    ok:orphanLinks.length===0&&duplicates.size===0,
    nodeCount:p.nodes.length,
    linkCount:p.links.length,
    orphanLinks:orphanLinks.length,
    disconnectedNodes,
    duplicateNodeIds:duplicates.size
  };
}
function readiness(process){
  const check=validateCriticalFlow(process);
  if(!check.ok)return {level:'error',label:'Behöver rättas',detail:check.orphanLinks?'Processen innehåller trasiga kopplingar.':'Processen innehåller dubbla steg-id:n.',...check};
  if(check.nodeCount===0)return {level:'empty',label:'Tom process',detail:'Lägg till första steget för att börja.',...check};
  if(check.nodeCount===1)return {level:'draft',label:'Påbörjad',detail:'Lägg till nästa steg för att skapa ett flöde.',...check};
  if(check.disconnectedNodes>0)return {level:'warning',label:'Kontrollera flödet',detail:check.disconnectedNodes+' steg saknar koppling till resten av processen.',...check};
  return {level:'ready',label:'Sammanhängande',detail:'Processen har ett sammanhängande grundflöde.',...check};
}
global.MapliniWorkflowCore={emptyProcess,addNode,updateNode,connect,deleteNodes,snapshot,restore,pushHistory,undoState,validateCriticalFlow,readiness};
})(typeof window!=='undefined'?window:globalThis);
