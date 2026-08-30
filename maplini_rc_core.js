(function(global){
'use strict';
function clone(v){return JSON.parse(JSON.stringify(v))}
function captureScopeState(processes,currentId,cloudLoadedIds,cloudLoadedScopes){
  return {
    processes:clone(processes||{}),
    currentId:currentId||null,
    cloudLoadedIds:[...(cloudLoadedIds||[])],
    cloudLoadedScopes:[...(cloudLoadedScopes instanceof Map?cloudLoadedScopes.entries():Object.entries(cloudLoadedScopes||{}))]
  };
}
function restoreScopeState(snapshot){
  snapshot=snapshot||{};
  return {
    processes:clone(snapshot.processes||{}),
    currentId:snapshot.currentId||null,
    cloudLoadedIds:Array.isArray(snapshot.cloudLoadedIds)?[...snapshot.cloudLoadedIds]:[],
    cloudLoadedScopes:Array.isArray(snapshot.cloudLoadedScopes)?snapshot.cloudLoadedScopes.map(x=>[x[0],x[1]]):[]
  };
}
function ensureCurrentId(processes,currentId,preferredIds){
  processes=processes||{};
  if(currentId&&processes[currentId])return currentId;
  for(const id of(preferredIds||[]))if(id&&processes[id])return id;
  const ids=Object.keys(processes);
  return ids[0]||null;
}
function validateStoreInvariant(processes,currentId){
  if(!processes||typeof processes!=='object'||Array.isArray(processes))return false;
  const ids=Object.keys(processes);
  if(!ids.length)return currentId==null;
  return !!(currentId&&processes[currentId]);
}
global.MapliniRcCore={captureScopeState,restoreScopeState,ensureCurrentId,validateStoreInvariant};
})(typeof window!=='undefined'?window:globalThis);
