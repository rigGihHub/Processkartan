(function(global){
'use strict';

function selectionHint(state){
  state=state||{};
  const singleLink=state.selectedLinkIndex!==null && state.selectedLinkIndex!==undefined;
  const nodeCount=Number(state.selectedNodeCount||0);
  const linkCount=Number(state.selectedLinkCount||0);
  if(singleLink)return 'Koppling markerad – endast kopplingsinställningar visas.';
  if(nodeCount>1)return nodeCount+' objekt markerade – använd Ta bort markerat eller klicka utanför för att avmarkera.';
  if(nodeCount===1 || state.nodeEnabled)return 'Ruta markerad – redigera text, färg, formatering och inputs/outputs.';
  if(linkCount>0)return linkCount+' kopplingar markerade – använd Ta bort markerat eller klicka utanför för att avmarkera.';
  return 'Markera en ruta eller koppling för att visa relevanta inställningar.';
}

global.MapliniUiCore={selectionHint};
})(typeof window!=='undefined'?window:globalThis);
