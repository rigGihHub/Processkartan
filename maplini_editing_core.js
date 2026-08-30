(function(global){
'use strict';

function clone(value){return JSON.parse(JSON.stringify(value));}

function makeClipboard(nodeValues,links,selectedIds){
  const selected=new Set((selectedIds||[]).map(String));
  const sourceNodes=Array.isArray(nodeValues)?nodeValues:[];
  const nodes=sourceNodes.filter(n=>n&&selected.has(String(n.id))).map(clone);
  const internalLinks=(Array.isArray(links)?links:[])
    .filter(l=>Array.isArray(l)&&selected.has(String(l[0]))&&selected.has(String(l[1])))
    .map(clone);
  return {schema:'maplini-clipboard-v1',nodes,links:internalLinks};
}

function hasNodes(payload){return Boolean(payload&&Array.isArray(payload.nodes)&&payload.nodes.length);}

function instantiate(payload,idFactory,offset){
  if(!hasNodes(payload)||typeof idFactory!=='function')return {nodes:[],links:[],idMap:{}};
  const delta=Number.isFinite(Number(offset))?Number(offset):28;
  const idMap={};
  const nodes=payload.nodes.map(source=>{
    const d=clone(source);
    const oldId=String(d.id);
    const newId=String(idFactory(oldId));
    idMap[oldId]=newId;
    d.id=newId;
    d.x=(Number(d.x)||0)+delta;
    d.y=(Number(d.y)||0)+delta;
    return d;
  });
  const links=(Array.isArray(payload.links)?payload.links:[]).map(source=>{
    const l=clone(source);
    const from=idMap[String(l[0])],to=idMap[String(l[1])];
    if(!from||!to)return null;
    l[0]=from;l[1]=to;
    if(l[3]&&typeof l[3]==='object'){
      if(l[3].viaX!=null&&Number.isFinite(Number(l[3].viaX)))l[3].viaX=Number(l[3].viaX)+delta;
      if(l[3].viaY!=null&&Number.isFinite(Number(l[3].viaY)))l[3].viaY=Number(l[3].viaY)+delta;
    }
    return l;
  }).filter(Boolean);
  return {nodes,links,idMap};
}


function groupMoveDelta(items,dx,dy,bounds,grid){
  const source=Array.isArray(items)?items:[];
  if(!source.length)return {dx:0,dy:0};
  const b=Object.assign({width:2400,height:1400,padding:10},bounds||{});
  const pad=Number(b.padding)||0,bw=Number(b.width)||2400,bh=Number(b.height)||1400;
  const snapStep=Math.max(1,Number(grid)||20);
  const snap=v=>Math.round((Number(v)||0)/snapStep)*snapStep;
  let minX=Infinity,minY=Infinity,maxR=-Infinity,maxB=-Infinity;
  for(const item of source){
    const x=Number(item.x)||0,y=Number(item.y)||0,w=Math.max(0,Number(item.width)||0),h=Math.max(0,Number(item.height)||0);
    minX=Math.min(minX,x);minY=Math.min(minY,y);maxR=Math.max(maxR,x+w);maxB=Math.max(maxB,y+h);
  }
  let mx=snap(dx),my=snap(dy);
  mx=Math.max(pad-minX,Math.min(bw-pad-maxR,mx));
  my=Math.max(pad-minY,Math.min(bh-pad-maxB,my));
  return {dx:mx,dy:my};
}
function movedInternalVias(links,selectedIds,dx,dy){
  const selected=new Set((selectedIds||[]).map(String));
  const out=[];
  (Array.isArray(links)?links:[]).forEach((link,index)=>{
    if(!Array.isArray(link)||!selected.has(String(link[0]))||!selected.has(String(link[1])))return;
    const style=link[3]&&typeof link[3]==='object'?link[3]:null;
    if(!style)return;
    const next={index};
    let used=false;
    if(style.viaX!=null&&Number.isFinite(Number(style.viaX))){next.viaX=Number(style.viaX)+(Number(dx)||0);used=true;}
    if(style.viaY!=null&&Number.isFinite(Number(style.viaY))){next.viaY=Number(style.viaY)+(Number(dy)||0);used=true;}
    if(used)out.push(next);
  });
  return out;
}


function nextStepPosition(source,targetSize,existingRects,bounds,gap){
  const src=source||{},target=targetSize||{},list=Array.isArray(existingRects)?existingRects:[];
  const b=Object.assign({width:2400,height:1400,padding:10},bounds||{}),pad=Number(b.padding)||0;
  const sw=Math.max(1,Number(src.width)||180),sh=Math.max(1,Number(src.height)||76),tw=Math.max(1,Number(target.width)||180),th=Math.max(1,Number(target.height)||76);
  const sx=Number(src.x)||0,sy=Number(src.y)||0,g=Math.max(40,Number(gap)||120);
  const candidates=[
    {x:sx+sw+g,y:sy+(sh-th)/2,rank:0},
    {x:sx+(sw-tw)/2,y:sy+sh+g,rank:1},
    {x:sx-tw-g,y:sy+(sh-th)/2,rank:2},
    {x:sx+(sw-tw)/2,y:sy-th-g,rank:3}
  ];
  const areaOverlap=(a,r)=>{const left=Math.max(a.x,Number(r.x)||0),top=Math.max(a.y,Number(r.y)||0),right=Math.min(a.x+tw,(Number(r.x)||0)+(Number(r.width)||0)),bottom=Math.min(a.y+th,(Number(r.y)||0)+(Number(r.height)||0));return Math.max(0,right-left)*Math.max(0,bottom-top)};
  let best=null;
  for(const c of candidates){
    const x=Math.max(pad,Math.min((Number(b.width)||2400)-pad-tw,c.x));
    const y=Math.max(pad,Math.min((Number(b.height)||1400)-pad-th,c.y));
    const overlap=list.reduce((sum,r)=>sum+areaOverlap({x,y},r),0);
    const clampPenalty=Math.abs(x-c.x)+Math.abs(y-c.y);
    const score=overlap*1000+clampPenalty*10+c.rank;
    if(!best||score<best.score)best={x,y,score};
  }
  return {x:Math.round(best?best.x:pad),y:Math.round(best?best.y:pad)};
}


function boundingBox(items){
  const list=(Array.isArray(items)?items:[]).filter(Boolean);
  if(!list.length)return null;
  let left=Infinity,top=Infinity,right=-Infinity,bottom=-Infinity;
  for(const item of list){
    const x=Number(item.x)||0,y=Number(item.y)||0,w=Math.max(0,Number(item.width)||0),h=Math.max(0,Number(item.height)||0);
    left=Math.min(left,x);top=Math.min(top,y);right=Math.max(right,x+w);bottom=Math.max(bottom,y+h);
  }
  return {left,top,right,bottom,width:right-left,height:bottom-top,centerX:(left+right)/2,centerY:(top+bottom)/2};
}
function fitToScreen(items,viewport,options){
  const box=boundingBox(items);if(!box)return null;
  const v=viewport||{},o=options||{},margin=Math.max(0,Number(o.margin)||56);
  const vw=Math.max(1,Number(v.width)||1),vh=Math.max(1,Number(v.height)||1);
  const minScale=Number.isFinite(Number(o.minScale))?Number(o.minScale):.25,maxScale=Number.isFinite(Number(o.maxScale))?Number(o.maxScale):1.5;
  const sx=(vw-margin*2)/Math.max(1,box.width),sy=(vh-margin*2)/Math.max(1,box.height);
  const scale=Math.max(minScale,Math.min(maxScale,Math.min(sx,sy)));
  return {scale,box,scrollLeft:Math.max(0,box.centerX*scale-vw/2),scrollTop:Math.max(0,box.centerY*scale-vh/2)};
}
function alignNodes(items,mode){
  const list=(Array.isArray(items)?items:[]).filter(x=>x&&x.id!=null);if(list.length<2)return {};
  const box=boundingBox(list),out={};
  for(const item of list){
    const w=Math.max(0,Number(item.width)||0),h=Math.max(0,Number(item.height)||0);let x=Number(item.x)||0,y=Number(item.y)||0;
    if(mode==='left')x=box.left;
    else if(mode==='hcenter')x=box.centerX-w/2;
    else if(mode==='right')x=box.right-w;
    else if(mode==='top')y=box.top;
    else if(mode==='vcenter')y=box.centerY-h/2;
    else if(mode==='bottom')y=box.bottom-h;
    out[String(item.id)]={x:Math.round(x),y:Math.round(y)};
  }
  return out;
}
function distributeNodes(items,axis){
  const list=(Array.isArray(items)?items:[]).filter(x=>x&&x.id!=null);if(list.length<3)return {};
  const horizontal=axis==='horizontal';
  const sorted=list.slice().sort((a,b)=>(Number(horizontal?a.x:a.y)||0)-(Number(horizontal?b.x:b.y)||0));
  const first=sorted[0],last=sorted[sorted.length-1];
  const start=Number(horizontal?first.x:first.y)||0;
  const lastEnd=(Number(horizontal?last.x:last.y)||0)+Math.max(0,Number(horizontal?last.width:last.height)||0);
  const totalSize=sorted.reduce((sum,item)=>sum+Math.max(0,Number(horizontal?item.width:item.height)||0),0);
  const gap=(lastEnd-start-totalSize)/(sorted.length-1);let cursor=start;const out={};
  sorted.forEach((item,index)=>{
    const x=Number(item.x)||0,y=Number(item.y)||0;
    out[String(item.id)]={x:horizontal?Math.round(cursor):Math.round(x),y:horizontal?Math.round(y):Math.round(cursor)};
    cursor+=Math.max(0,Number(horizontal?item.width:item.height)||0)+(index<sorted.length-1?gap:0);
  });
  return out;
}

function serialize(payload){return hasNodes(payload)?'MAPLINI_CLIPBOARD_V1\n'+JSON.stringify(payload):'';}
function parse(text){
  if(typeof text!=='string'||!text.startsWith('MAPLINI_CLIPBOARD_V1\n'))return null;
  try{const payload=JSON.parse(text.slice('MAPLINI_CLIPBOARD_V1\n'.length));return hasNodes(payload)?payload:null}catch(_){return null}
}

global.MapliniEditingCore={makeClipboard,hasNodes,instantiate,groupMoveDelta,movedInternalVias,nextStepPosition,boundingBox,fitToScreen,alignNodes,distributeNodes,serialize,parse};
})(typeof window!=='undefined'?window:globalThis);
