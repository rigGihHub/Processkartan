(function(global){
'use strict';
function clear(){return {selectedId:null,selectedIds:[],selectedLinkIndex:null,selectedLinkIndices:[]}}
function normalize(state){
  state=state||{};
  let selectedIds=[...new Set((Array.isArray(state.selectedIds)?state.selectedIds:[]).filter(Boolean))];
  let selectedLinkIndices=[...new Set((Array.isArray(state.selectedLinkIndices)?state.selectedLinkIndices:[]).filter(i=>Number.isInteger(i)&&i>=0))].sort((a,b)=>a-b);
  let selectedId=state.selectedId||null;
  let selectedLinkIndex=Number.isInteger(state.selectedLinkIndex)&&state.selectedLinkIndex>=0?state.selectedLinkIndex:null;
  if(selectedId&&!selectedIds.includes(selectedId))selectedIds.push(selectedId);
  if(selectedLinkIndex!==null&&!selectedLinkIndices.includes(selectedLinkIndex))selectedLinkIndices.push(selectedLinkIndex);
  selectedId=selectedIds.length===1?selectedIds[0]:null;
  selectedLinkIndex=selectedLinkIndices.length===1?selectedLinkIndices[0]:null;
  return {selectedId,selectedIds,selectedLinkIndex,selectedLinkIndices};
}
function hasAny(state){const s=normalize(state);return s.selectedIds.length>0||s.selectedLinkIndices.length>0}
function deleteAction(state){
  const s=normalize(state),count=s.selectedIds.length+s.selectedLinkIndices.length;
  if(count>1)return 'many';
  if(s.selectedIds.length===1)return 'node';
  if(s.selectedLinkIndices.length===1)return 'link';
  return 'none';
}
function afterLinkDelete(state,deletedIndex){
  const s=normalize(state);
  const selectedLinkIndices=s.selectedLinkIndices.filter(i=>i!==deletedIndex).map(i=>i>deletedIndex?i-1:i);
  return normalize({selectedId:s.selectedId,selectedIds:s.selectedIds,selectedLinkIndices});
}
global.MapliniSelectionCore={clear,normalize,hasAny,deleteAction,afterLinkDelete};
})(typeof window!=='undefined'?window:globalThis);
