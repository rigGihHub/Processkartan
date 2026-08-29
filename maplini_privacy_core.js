(function(global){
'use strict';
function shouldPersistLocally(state){
  state=state||{};
  return !Boolean(state.sharedView);
}
function persistenceMode(state){
  return shouldPersistLocally(state)?'local':'ephemeral';
}
global.MapliniPrivacyCore={shouldPersistLocally,persistenceMode};
})(typeof window!=='undefined'?window:globalThis);
