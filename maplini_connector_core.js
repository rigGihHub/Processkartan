(function(global){
'use strict';
const DEFAULT_STYLE={color:'#687584',width:2,end:'arrow',dash:'solid',viaX:null,viaY:null};
function style(link){if(!link[3]||typeof link[3]!=='object')link[3]={};return Object.assign({},DEFAULT_STYLE,link[3]);}
function setStyle(links,index,patch){if(index==null||!links[index])return null;links[index][3]=Object.assign(style(links[index]),patch||{});return links[index][3];}
function rectsIntersect(a,b){return !(a.right<b.left||a.left>b.right||a.bottom<b.top||a.top>b.bottom);}
function removeSelected(links,doomedIds,selectedIndices){const doomed=doomedIds instanceof Set?doomedIds:new Set(doomedIds||[]);const selected=selectedIndices instanceof Set?selectedIndices:new Set(selectedIndices||[]);return links.filter((l,i)=>!doomed.has(l[0])&&!doomed.has(l[1])&&!selected.has(i));}
global.MapliniConnectorCore={DEFAULT_STYLE,style,setStyle,rectsIntersect,removeSelected};
})(typeof window!=='undefined'?window:globalThis);
