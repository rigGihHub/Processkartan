(function(global){
'use strict';
const DEFAULT_STYLE={color:'#5b6775',width:2,end:'arrow',dash:'solid',viaX:null,viaY:null,routing:'straight',anchorMode:'manual',label:''};

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
  return [String(sourceId),String(targetId),side||'right',Object.assign(cloneStyle(),{routing:'orthogonal',anchorMode:'auto'},stylePatch||{})];
}
function autoSides(dx,dy){
  if(Math.abs(dx)>=Math.abs(dy))return dx>=0?['right','left']:['left','right'];
  return dy>=0?['bottom','top']:['top','bottom'];
}
function routePoints(x1,y1,x2,y2,sourceSide,targetSide,styleValue){
  const st=cloneStyle(styleValue);
  if(st.routing!=='orthogonal'){
    // "straight" is a strict direct segment. Legacy/manual via coordinates must not bend it.
    return [[x1,y1],[x2,y2]];
  }
  const srcHorizontal=sourceSide==='left'||sourceSide==='right';
  const dstHorizontal=targetSide==='left'||targetSide==='right';
  if(srcHorizontal&&dstHorizontal){
    const mx=st.viaX==null?(x1+x2)/2:Number(st.viaX);
    return [[x1,y1],[mx,y1],[mx,y2],[x2,y2]];
  }
  if(!srcHorizontal&&!dstHorizontal){
    const my=st.viaY==null?(y1+y2)/2:Number(st.viaY);
    return [[x1,y1],[x1,my],[x2,my],[x2,y2]];
  }
  if(srcHorizontal){
    if(st.viaX!=null||st.viaY!=null){
      const vx=st.viaX==null?(x1+x2)/2:Number(st.viaX),vy=st.viaY==null?(y1+y2)/2:Number(st.viaY);
      return [[x1,y1],[vx,y1],[vx,vy],[x2,vy],[x2,y2]];
    }
    return [[x1,y1],[x2,y1],[x2,y2]];
  }
  if(st.viaX!=null||st.viaY!=null){
    const vx=st.viaX==null?(x1+x2)/2:Number(st.viaX),vy=st.viaY==null?(y1+y2)/2:Number(st.viaY);
    return [[x1,y1],[x1,vy],[vx,vy],[vx,y2],[x2,y2]];
  }
  return [[x1,y1],[x1,y2],[x2,y2]];
}
function pathData(points){return points.map((p,i)=>(i?'L':'M')+p[0]+','+p[1]).join(' ');}
function midpoint(points){
  if(!Array.isArray(points)||points.length<2)return null;
  let total=0,lens=[];
  for(let i=1;i<points.length;i++){const l=Math.hypot(points[i][0]-points[i-1][0],points[i][1]-points[i-1][1]);lens.push(l);total+=l;}
  let target=total/2;
  for(let i=0;i<lens.length;i++){if(target<=lens[i]||i===lens.length-1){const a=points[i],b=points[i+1],t=lens[i]?target/lens[i]:0;return{x:a[0]+(b[0]-a[0])*t,y:a[1]+(b[1]-a[1])*t};}target-=lens[i];}
  return{x:points[0][0],y:points[0][1]};
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
function decisionLabel(outgoingCount){const n=Math.max(0,Number(outgoingCount)||0);return n===0?'Ja':n===1?'Nej':'';}
function splitLink(links,index,newNodeId){
  const source=normalizeLinks(links);
  if(index==null||index<0||index>=source.length||!newNodeId)return source;
  const original=source[index],st=cloneStyle(original[3]);
  const common=Object.assign({},st,{viaX:null,viaY:null,anchorMode:'auto'});
  const first=create(original[0],String(newNodeId),original[2]||'right',Object.assign({},common,{label:st.label||''}));
  const second=create(String(newNodeId),original[1],'right',Object.assign({},common,{label:''}));
  source.splice(index,1,first,second);
  return source;
}

global.MapliniConnectorCore={DEFAULT_STYLE,cloneStyle,normalizeLink,normalizeLinks,style,setStyle,create,setVia,autoSides,routePoints,pathData,midpoint,rectsIntersect,removeSelected,removeAt,selectionAfterDelete,decisionLabel,splitLink};
})(typeof window!=='undefined'?window:globalThis);
