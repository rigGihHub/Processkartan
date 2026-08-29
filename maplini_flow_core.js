(function(global){
'use strict';
function clone(v){return JSON.parse(JSON.stringify(v))}
function sharedProcess(row){
  if(!row||!row.id||!row.data||typeof row.data!=='object')return null;
  return Object.assign({},clone(row.data),{id:row.id,name:row.name||row.data.name||'Namnlös process'});
}
function afterProcessDelete(processes,currentId,deletedId){
  const out=clone(processes||{});
  delete out[deletedId];
  const ids=Object.keys(out);
  const nextCurrent=(currentId!==deletedId&&out[currentId])?currentId:(ids[0]||null);
  return {processes:out,currentId:nextCurrent};
}
global.MapliniFlowCore={sharedProcess,afterProcessDelete};
})(typeof window!=='undefined'?window:globalThis);
