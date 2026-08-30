(function(global){
'use strict';

function workspacePrefKey(userId){
  return 'maplini_workspace_'+String(userId||'anonymous');
}
function scopeKey(workspaceId){
  return workspaceId?('workspace:'+workspaceId):'personal';
}
function chooseWorkspace(preferredId,entries){
  entries=Array.isArray(entries)?entries:[];
  if(preferredId){
    const found=entries.find(x=>x&&x.workspace_id===preferredId);
    if(found)return {id:found.workspace_id,role:found.role||'viewer'};
  }
  return {id:null,role:'owner'};
}
function sessionState(session){
  const valid=!!(session&&session.access_token&&session.user&&session.user.id);
  return {valid,userId:valid?session.user.id:null};
}
function scopedIds(scopeMap,scope){
  const out=[];
  if(scopeMap instanceof Map){
    for(const [id,value] of scopeMap.entries())if(value===scope)out.push(id);
  }else{
    for(const [id,value] of Object.entries(scopeMap||{}))if(value===scope)out.push(id);
  }
  return out;
}
global.MapliniSessionCore={workspacePrefKey,scopeKey,chooseWorkspace,sessionState,scopedIds};
})(typeof window!=='undefined'?window:globalThis);
