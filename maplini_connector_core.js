(function(global){
'use strict';
const DEFAULT_STYLE={color:'#687584',width:2,end:'arrow',dash:'solid',viaX:null,viaY:null};

function cloneStyle(value){return Object.assign({},DEFAULT_STYLE,value&&typeof value==='object'?value:{});}
function normalizeLink(link){
  if(!Array.isArray(link)||link.length<2)return null;
  return [String(link[0]),String(link[1]),link[2]||'right',cloneStyle(link[3])];
}
function normalizeLinks(links){return (Array.isArray(links)?links:[]).map(normalizeLink).filter(Boolean);}
function style(link){
  if(!Array.isArray(link))return cloneStyle();
  link[3]=cloneStyle(link[3]);
  return link[3];
}
function setStyle(links,index,patch){
  if(!Array.isArray(links)||index==null||!links[index])return null;
  links[index][3]=Object.assign(style(links[index]),patch||{});
  return links[index][3];
}
function create(sourceId,targetId,side,stylePatch){
  return [String(sourceId),String(targetId),side||'right',Object.assign(cloneStyle(),stylePatch||{})];
}
function setVia(links,index,x,y){return setStyle(links,index,{viaX:Number(x),viaY:Number(y)});}
function rectsIntersect(a,b){return !(a.right<b.left||a.left>b.right||a.bottom<b.top||a.top>b.bottom);}
function removeSelected(links,doomedIds,selectedIndices){
  const doomed=doomedIds instanceof Set?doomedIds:new Set(doomedIds||[]);
  const selected=selectedIndices instanceof Set?selectedIndices:new Set(selectedIndices||[]);
  return normalizeLinks(links).filter((l,i)=>!doomed.has(l[0])&&!doomed.has(l[1])&&!selected.has(i));
}
function removeAt(links,index){
  const out=normalizeLinks(links);
  if(index==null||index<0||index>=out.length)return out;
  out.splice(index,1);
  return out;
}
function selectionAfterDelete(selectedIndex,deletedIndex){
  if(selectedIndex==null)return null;
  if(selectedIndex===deletedIndex)return null;
  return selectedIndex>deletedIndex?selectedIndex-1:selectedIndex;
}

global.MapliniConnectorCore={DEFAULT_STYLE,cloneStyle,normalizeLink,normalizeLinks,style,setStyle,create,setVia,rectsIntersect,removeSelected,removeAt,selectionAfterDelete};
})(typeof window!=='undefined'?window:globalThis);
