(function(global){
'use strict';
function clone(v){try{return JSON.parse(JSON.stringify(v));}catch(e){return null;}}
function safeArray(v){return Array.isArray(v)?v:[]}
function stripHistory(process){
  const p=clone(process||{})||{};
  delete p.versionHistory;
  delete p.cloudUpdatedAt;
  delete p.localModifiedAt;
  return p;
}
function fingerprint(process){return JSON.stringify(stripHistory(process))}
function normalizeRecord(record){
  if(!record||typeof record!=='object')return null;
  const data=stripHistory(record.data||{});
  if(!data||!data.id||!Array.isArray(data.nodes)||!Array.isArray(data.links))return null;
  const createdAt=Number(record.createdAt||0);
  return {
    id:String(record.id||('version-'+createdAt)),
    createdAt:Number.isFinite(createdAt)&&createdAt>0?createdAt:Date.now(),
    label:String(record.label||'Sparad version').slice(0,120),
    nodeCount:data.nodes.length,
    linkCount:data.links.length,
    data
  };
}
function normalizeHistory(history,limit=20){
  const out=[];
  for(const raw of safeArray(history)){
    const rec=normalizeRecord(raw);if(!rec)continue;
    if(out.some(x=>x.id===rec.id))continue;
    out.push(rec);
  }
  out.sort((a,b)=>b.createdAt-a.createdAt);
  return out.slice(0,Math.max(1,Number(limit)||20));
}
function addVersion(process,history,options={}){
  const normalized=normalizeHistory(history,options.limit||20);
  const data=stripHistory(process);
  const currentFingerprint=fingerprint(data);
  if(normalized.length&&fingerprint(normalized[0].data)===currentFingerprint)return {history:normalized,added:false,record:normalized[0]};
  const now=Number(options.now||Date.now());
  const rec=normalizeRecord({id:'version-'+now,createdAt:now,label:options.label||'Sparad version',data});
  const next=normalizeHistory([rec,...normalized],options.limit||20);
  return {history:next,added:true,record:rec};
}
function stableNode(n){const x=clone(n||{})||{};return JSON.stringify(x)}
function stableLink(l){return JSON.stringify(clone(l||[]))}
function diff(fromProcess,toProcess){
  const from=stripHistory(fromProcess||{}),to=stripHistory(toProcess||{});
  const a=new Map(safeArray(from.nodes).map(n=>[String(n.id||''),n]));
  const b=new Map(safeArray(to.nodes).map(n=>[String(n.id||''),n]));
  let addedNodes=0,removedNodes=0,changedNodes=0;
  for(const [id,node] of b){if(!a.has(id))addedNodes++;else if(stableNode(a.get(id))!==stableNode(node))changedNodes++}
  for(const id of a.keys())if(!b.has(id))removedNodes++;
  const ac=new Map(),bc=new Map();
  for(const l of safeArray(from.links)){const k=stableLink(l);ac.set(k,(ac.get(k)||0)+1)}
  for(const l of safeArray(to.links)){const k=stableLink(l);bc.set(k,(bc.get(k)||0)+1)}
  let addedLinks=0,removedLinks=0;
  for(const [k,n] of bc)addedLinks+=Math.max(0,n-(ac.get(k)||0));
  for(const [k,n] of ac)removedLinks+=Math.max(0,n-(bc.get(k)||0));
  return {addedNodes,removedNodes,changedNodes,addedLinks,removedLinks,changed:addedNodes+removedNodes+changedNodes+addedLinks+removedLinks>0};
}
function diffLabel(d){
  d=d||{};const parts=[];
  if(d.addedNodes)parts.push('+'+d.addedNodes+' steg');
  if(d.removedNodes)parts.push('−'+d.removedNodes+' steg');
  if(d.changedNodes)parts.push(d.changedNodes+' ändrade steg');
  if(d.addedLinks)parts.push('+'+d.addedLinks+' koppling'+(d.addedLinks===1?'':'ar'));
  if(d.removedLinks)parts.push('−'+d.removedLinks+' koppling'+(d.removedLinks===1?'':'ar'));
  return parts.length?parts.join(' · '):'Samma innehåll som nu';
}
global.MapliniVersionHistoryCore={clone,stripHistory,fingerprint,normalizeRecord,normalizeHistory,addVersion,diff,diffLabel};
})(typeof window!=='undefined'?window:globalThis);
