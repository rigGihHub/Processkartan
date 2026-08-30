(function(global){
'use strict';
function clone(v){return JSON.parse(JSON.stringify(v))}
function toMillis(v){if(typeof v==='number'&&Number.isFinite(v))return v;if(!v)return 0;const n=Date.parse(v);return Number.isFinite(n)?n:0}
function stripSyncMeta(process){const p=clone(process||{});delete p.localModifiedAt;delete p.cloudUpdatedAt;return p}
function contentSignature(process){try{return JSON.stringify(stripSyncMeta(process))}catch(e){return ''}}
function contentChanged(previous,next){if(!previous)return true;return contentSignature(previous)!==contentSignature(next)}
function chooseSource(localProcess,row){
  if(!localProcess)return 'cloud';
  const localAt=toMillis(localProcess.localModifiedAt),cloudAt=toMillis(row&&row.updated_at);
  if(localAt&&cloudAt&&localAt>cloudAt)return 'local';
  return 'cloud';
}
function cloudProcess(row){
  const data=(row&&row.data&&typeof row.data==='object')?clone(row.data):{};
  return Object.assign({},data,{id:row.id,name:row.name||data.name||'Namnlös process',cloudUpdatedAt:row.updated_at||null});
}
function mergeCloudRows(localProcesses,rows){
  const processes=clone(localProcesses||{}),cloudLoadedIds=[],preservedLocalIds=[];
  for(const row of(rows||[])){
    if(!row||!row.id||!row.data)continue;
    if(chooseSource(processes[row.id],row)==='local'){preservedLocalIds.push(row.id);continue}
    processes[row.id]=cloudProcess(row);cloudLoadedIds.push(row.id);
  }
  return {processes,cloudLoadedIds,preservedLocalIds};
}
function signOutPlan(processes,cloudLoadedIds,currentId){
  const out=clone(processes||{}),removedIds=[],preservedModifiedIds=[];
  for(const id of new Set(cloudLoadedIds||[])){
    const p=out[id];if(!p)continue;
    const localAt=toMillis(p.localModifiedAt),cloudAt=toMillis(p.cloudUpdatedAt);
    if(localAt&&cloudAt&&localAt>cloudAt){preservedModifiedIds.push(id);delete p.cloudUpdatedAt;continue}
    delete out[id];removedIds.push(id);
  }
  const ids=Object.keys(out);
  return {processes:out,currentId:out[currentId]?currentId:(ids[0]||null),removedIds,preservedModifiedIds};
}
global.MapliniSyncCore={toMillis,stripSyncMeta,contentSignature,contentChanged,chooseSource,cloudProcess,mergeCloudRows,signOutPlan};
})(typeof window!=='undefined'?window:globalThis);
