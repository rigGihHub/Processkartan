(function(global){
'use strict';
function normalizeRole(role){return String(role||'viewer').toLowerCase()}
function canEdit(state){
  state=state||{};
  if(Boolean(state.sharedView))return false;
  const role=normalizeRole(state.currentRole);
  return role==='owner'||role==='editor';
}
function mode(state){return canEdit(state)?'edit':'view'}
global.MapliniAccessCore={normalizeRole,canEdit,mode};
})(typeof window!=='undefined'?window:globalThis);
