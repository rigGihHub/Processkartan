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



function flowSegmentCollisionPenalty(candidate,targetSize,source,segments,clearance=24){
  const list=Array.isArray(segments)?segments:[];
  if(!list.length)return 0;
  const tw=Math.max(1,Number(targetSize&&targetSize.width)||180),th=Math.max(1,Number(targetSize&&targetSize.height)||76);
  const pad=Math.max(4,Number(clearance)||24);
  const rect={left:Number(candidate.x)||0,top:Number(candidate.y)||0,right:(Number(candidate.x)||0)+tw,bottom:(Number(candidate.y)||0)+th};
  const expanded={left:rect.left-pad,top:rect.top-pad,right:rect.right+pad,bottom:rect.bottom+pad};
  const pointInRect=(x,y,r)=>x>=r.left&&x<=r.right&&y>=r.top&&y<=r.bottom;
  const orient=(ax,ay,bx,by,cx,cy)=>(bx-ax)*(cy-ay)-(by-ay)*(cx-ax);
  const onSegment=(ax,ay,bx,by,cx,cy)=>Math.min(ax,bx)-.001<=cx&&cx<=Math.max(ax,bx)+.001&&Math.min(ay,by)-.001<=cy&&cy<=Math.max(ay,by)+.001;
  const intersects=(a,b,c,d)=>{
    const o1=orient(a.x,a.y,b.x,b.y,c.x,c.y),o2=orient(a.x,a.y,b.x,b.y,d.x,d.y),o3=orient(c.x,c.y,d.x,d.y,a.x,a.y),o4=orient(c.x,c.y,d.x,d.y,b.x,b.y);
    if(((o1>0&&o2<0)||(o1<0&&o2>0))&&((o3>0&&o4<0)||(o3<0&&o4>0)))return true;
    if(Math.abs(o1)<.001&&onSegment(a.x,a.y,b.x,b.y,c.x,c.y))return true;
    if(Math.abs(o2)<.001&&onSegment(a.x,a.y,b.x,b.y,d.x,d.y))return true;
    if(Math.abs(o3)<.001&&onSegment(c.x,c.y,d.x,d.y,a.x,a.y))return true;
    return Math.abs(o4)<.001&&onSegment(c.x,c.y,d.x,d.y,b.x,b.y);
  };
  const segmentHitsRect=(a,b,r)=>{
    if(pointInRect(a.x,a.y,r)||pointInRect(b.x,b.y,r))return true;
    const tl={x:r.left,y:r.top},tr={x:r.right,y:r.top},br={x:r.right,y:r.bottom},bl={x:r.left,y:r.bottom};
    return intersects(a,b,tl,tr)||intersects(a,b,tr,br)||intersects(a,b,br,bl)||intersects(a,b,bl,tl);
  };
  const cx=rect.left+tw/2,cy=rect.top+th/2;
  const sx=(Number(source&&source.x)||0)+(Math.max(1,Number(source&&source.width)||180))/2;
  const sy=(Number(source&&source.y)||0)+(Math.max(1,Number(source&&source.height)||76))/2;
  let penalty=0;
  for(const raw of list){
    if(!raw)continue;
    const a=Array.isArray(raw)?{x:Number(raw[0])||0,y:Number(raw[1])||0}:{x:Number(raw.x1??raw.a?.[0]??raw.a?.x)||0,y:Number(raw.y1??raw.a?.[1]??raw.a?.y)||0};
    const b=Array.isArray(raw)?{x:Number(raw[2])||0,y:Number(raw[3])||0}:{x:Number(raw.x2??raw.b?.[0]??raw.b?.x)||0,y:Number(raw.y2??raw.b?.[1]??raw.b?.y)||0};
    if(segmentHitsRect(a,b,expanded))penalty+=500000;
    // Use the center-to-center line as a cheap proxy for the new automatic connector.
    // It does not replace routing, but strongly discourages placements that would cross an existing flow.
    if(intersects({x:sx,y:sy},{x:cx,y:cy},a,b))penalty+=180000;
  }
  return penalty;
}

function smartNextStepPosition(source,targetSize,existingRects,bounds,options){
  const src=source||{},target=targetSize||{},list=Array.isArray(existingRects)?existingRects:[];
  const b=Object.assign({width:2400,height:1400,padding:10},bounds||{}),o=options||{},pad=Number(b.padding)||0;
  const sw=Math.max(1,Number(src.width)||180),sh=Math.max(1,Number(src.height)||76),tw=Math.max(1,Number(target.width)||180),th=Math.max(1,Number(target.height)||76);
  const sx=Number(src.x)||0,sy=Number(src.y)||0,g=Math.max(50,Number(o.gap)||110),grid=Math.max(1,Number(o.grid)||20);
  const direction=['right','left','down','up'].includes(String(o.direction))?String(o.direction):'right';
  const branchIndex=Number.isInteger(o.branchIndex)?o.branchIndex:null;
  const branchSlots=branchIndex===0?[-1,1,0,-2,2,3,-3]:(branchIndex===1?[1,-1,0,2,-2,3,-3]:[0,-1,1,-2,2,-3,3]);
  const crossGap=Math.max(36,Number(o.crossGap)||54);
  const step=Math.max(100,Math.round((Math.max(sh,th)+crossGap)/grid)*grid);
  const snap=v=>Math.round(v/grid)*grid;
  const areaOverlap=(a,r)=>{const left=Math.max(a.x,Number(r.x)||0),top=Math.max(a.y,Number(r.y)||0),right=Math.min(a.x+tw,(Number(r.x)||0)+(Number(r.width)||0)),bottom=Math.min(a.y+th,(Number(r.y)||0)+(Number(r.height)||0));return Math.max(0,right-left)*Math.max(0,bottom-top)};
  const raw=[];
  for(const slot of branchSlots){
    let x=sx,y=sy;
    if(direction==='right'){x=sx+sw+g;y=sy+(sh-th)/2+slot*step;}
    else if(direction==='left'){x=sx-tw-g;y=sy+(sh-th)/2+slot*step;}
    else if(direction==='down'){x=sx+(sw-tw)/2+slot*step;y=sy+sh+g;}
    else{x=sx+(sw-tw)/2+slot*step;y=sy-th-g;}
    raw.push({x:snap(x),y:snap(y),slot});
  }
  // Keep the process moving in the same direction. Only use a reverse-axis fallback when every forward slot is blocked.
  let best=null;
  for(const c of raw){
    const x=Math.max(pad,Math.min((Number(b.width)||2400)-pad-tw,c.x));
    const y=Math.max(pad,Math.min((Number(b.height)||1400)-pad-th,c.y));
    const overlap=list.reduce((sum,r)=>sum+areaOverlap({x,y},r),0);
    const clampPenalty=Math.abs(x-c.x)+Math.abs(y-c.y);
    const slotPenalty=Math.abs(c.slot)*6;
    const flowPenalty=flowSegmentCollisionPenalty({x,y},target,src,o.linkSegments,o.linkClearance);
    const score=overlap*1000+flowPenalty+clampPenalty*20+slotPenalty;
    if(!best||score<best.score)best={x,y,score,overlap};
    if(overlap===0&&flowPenalty===0&&clampPenalty===0)break;
  }
  if(!best||best.overlap>0){
    const fallback=nextStepPosition(src,target,list,b,g);
    return {x:snap(fallback.x),y:snap(fallback.y),direction};
  }
  return {x:Math.round(best.x),y:Math.round(best.y),direction};
}

function smartDecisionBranchPositions(source,targetSize,existingRects,bounds,options){
  const src=source||{},target=targetSize||{},list=Array.isArray(existingRects)?existingRects:[];
  const b=Object.assign({width:2400,height:1400,padding:10},bounds||{}),o=options||{},pad=Number(b.padding)||0;
  const sw=Math.max(1,Number(src.width)||180),sh=Math.max(1,Number(src.height)||76),tw=Math.max(1,Number(target.width)||180),th=Math.max(1,Number(target.height)||76);
  const sx=Number(src.x)||0,sy=Number(src.y)||0,g=Math.max(80,Number(o.gap)||148),grid=Math.max(1,Number(o.grid)||20);
  const direction=['right','left','down','up'].includes(String(o.direction))?String(o.direction):'right';
  const crossGap=Math.max(48,Number(o.crossGap)||82),forwardStep=Math.max(60,Number(o.forwardStep)||80);
  const snap=v=>Math.round(v/grid)*grid;
  const areaOverlap=(a,r)=>{const left=Math.max(a.x,Number(r.x)||0),top=Math.max(a.y,Number(r.y)||0),right=Math.min(a.x+tw,(Number(r.x)||0)+(Number(r.width)||0)),bottom=Math.min(a.y+th,(Number(r.y)||0)+(Number(r.height)||0));return Math.max(0,right-left)*Math.max(0,bottom-top)};
  const clamp=(x,y)=>({x:Math.max(pad,Math.min((Number(b.width)||2400)-pad-tw,x)),y:Math.max(pad,Math.min((Number(b.height)||1400)-pad-th,y))});
  const horizontal=direction==='right'||direction==='left';
  const crossSize=horizontal?th:tw;
  const baseSeparation=Math.max(crossSize+crossGap,Math.round((crossSize*1.35+crossGap)/grid)*grid);
  let best=null;
  for(const spreadFactor of [1,1.35,1.7,2.1]){
    const half=(baseSeparation*spreadFactor)/2;
    for(const forwardExtra of [0,forwardStep,forwardStep*2]){
      let mainX=sx+(sw-tw)/2,mainY=sy+(sh-th)/2;
      if(direction==='right')mainX=sx+sw+g+forwardExtra;
      else if(direction==='left')mainX=sx-tw-g-forwardExtra;
      else if(direction==='down')mainY=sy+sh+g+forwardExtra;
      else mainY=sy-th-g-forwardExtra;
      const rawYes=horizontal?{x:mainX,y:sy+(sh-th)/2-half}:{x:sx+(sw-tw)/2-half,y:mainY};
      const rawNo=horizontal?{x:mainX,y:sy+(sh-th)/2+half}:{x:sx+(sw-tw)/2+half,y:mainY};
      const y0=clamp(snap(rawYes.x),snap(rawYes.y)),n0=clamp(snap(rawNo.x),snap(rawNo.y));
      const yes={x:snap(y0.x),y:snap(y0.y)},no={x:snap(n0.x),y:snap(n0.y)};
      const overlapYes=list.reduce((sum,r)=>sum+areaOverlap(yes,r),0),overlapNo=list.reduce((sum,r)=>sum+areaOverlap(no,r),0);
      const pairOverlap=areaOverlap(yes,no);
      const clampPenalty=Math.abs(yes.x-snap(rawYes.x))+Math.abs(yes.y-snap(rawYes.y))+Math.abs(no.x-snap(rawNo.x))+Math.abs(no.y-snap(rawNo.y));
      const symmetryPenalty=horizontal?Math.abs((yes.y+th/2)+(no.y+th/2)-2*(sy+sh/2)):Math.abs((yes.x+tw/2)+(no.x+tw/2)-2*(sx+sw/2));
      const flowPenalty=flowSegmentCollisionPenalty(yes,target,src,o.linkSegments,o.linkClearance)+flowSegmentCollisionPenalty(no,target,src,o.linkSegments,o.linkClearance);
      const score=(overlapYes+overlapNo+pairOverlap)*1000+flowPenalty+clampPenalty*20+symmetryPenalty*3+forwardExtra*.15+(spreadFactor-1)*20;
      if(!best||score<best.score)best={yes:{...yes,direction},no:{...no,direction},score,blocked:overlapYes+overlapNo+pairOverlap};
      if(best&&best.blocked===0&&flowPenalty===0&&clampPenalty===0&&spreadFactor===1&&forwardExtra===0)return {yes:best.yes,no:best.no,direction};
    }
  }
  return best?{yes:best.yes,no:best.no,direction}:{yes:smartNextStepPosition(src,target,list,b,{...o,direction,branchIndex:0}),no:smartNextStepPosition(src,target,list,b,{...o,direction,branchIndex:1}),direction};
}

function smartFlowContinuationPosition(source,targetSize,existingRects,bounds,options){
  const src=source||{},target=targetSize||{},list=Array.isArray(existingRects)?existingRects:[];
  const b=Object.assign({width:2400,height:1400,padding:10},bounds||{}),o=options||{},pad=Number(b.padding)||0;
  const sw=Math.max(1,Number(src.width)||180),sh=Math.max(1,Number(src.height)||76),tw=Math.max(1,Number(target.width)||180),th=Math.max(1,Number(target.height)||76);
  const sx=Number(src.x)||0,sy=Number(src.y)||0,g=Math.max(50,Number(o.gap)||110),grid=Math.max(1,Number(o.grid)||20);
  const direction=['right','left','down','up'].includes(String(o.direction))?String(o.direction):'right';
  const horizontal=direction==='right'||direction==='left';
  const laneCenter=Number.isFinite(Number(o.laneCenter))?Number(o.laneCenter):(horizontal?sy+sh/2:sx+sw/2);
  const forwardStep=Math.max(60,Number(o.forwardStep)||80),crossStep=Math.max(60,Number(o.crossStep)||Math.max(horizontal?th:tw,Number(o.crossGap)||64));
  const snap=v=>Math.round(v/grid)*grid;
  const areaOverlap=(a,r)=>{const left=Math.max(a.x,Number(r.x)||0),top=Math.max(a.y,Number(r.y)||0),right=Math.min(a.x+tw,(Number(r.x)||0)+(Number(r.width)||0)),bottom=Math.min(a.y+th,(Number(r.y)||0)+(Number(r.height)||0));return Math.max(0,right-left)*Math.max(0,bottom-top)};
  const clamp=(x,y)=>({x:Math.max(pad,Math.min((Number(b.width)||2400)-pad-tw,x)),y:Math.max(pad,Math.min((Number(b.height)||1400)-pad-th,y))});
  let best=null;
  const crossOffsets=[0,-crossStep,crossStep,-crossStep*2,crossStep*2];
  for(const crossOffset of crossOffsets){
    for(const forwardExtra of [0,forwardStep,forwardStep*2,forwardStep*3,forwardStep*4]){
      let x=sx,y=sy;
      if(direction==='right'){x=sx+sw+g+forwardExtra;y=laneCenter-th/2+crossOffset;}
      else if(direction==='left'){x=sx-tw-g-forwardExtra;y=laneCenter-th/2+crossOffset;}
      else if(direction==='down'){x=laneCenter-tw/2+crossOffset;y=sy+sh+g+forwardExtra;}
      else{x=laneCenter-tw/2+crossOffset;y=sy-th-g-forwardExtra;}
      const raw={x:snap(x),y:snap(y)},c0=clamp(raw.x,raw.y),c={x:snap(c0.x),y:snap(c0.y)};
      const overlap=list.reduce((sum,r)=>sum+areaOverlap(c,r),0);
      const clampPenalty=Math.abs(c.x-raw.x)+Math.abs(c.y-raw.y);
      const lanePenalty=Math.abs(crossOffset)*4;
      const flowPenalty=flowSegmentCollisionPenalty(c,target,src,o.linkSegments,o.linkClearance);
      const score=overlap*1000+flowPenalty+clampPenalty*20+lanePenalty+forwardExtra*.08;
      if(!best||score<best.score)best={...c,direction,score,overlap,crossOffset};
      if(overlap===0&&flowPenalty===0&&clampPenalty===0&&crossOffset===0)return {x:c.x,y:c.y,direction};
    }
  }
  if(best&&best.overlap===0)return {x:best.x,y:best.y,direction};
  return smartNextStepPosition(src,target,list,b,o);
}

function smartBranchRejoinPosition(sourceA,sourceB,targetSize,existingRects,bounds,options){
  const a=sourceA||{},bSrc=sourceB||{},target=targetSize||{},list=Array.isArray(existingRects)?existingRects:[];
  const boundsCfg=Object.assign({width:2400,height:1400,padding:10},bounds||{}),o=options||{},pad=Number(boundsCfg.padding)||0;
  const tw=Math.max(1,Number(target.width)||180),th=Math.max(1,Number(target.height)||76),grid=Math.max(1,Number(o.grid)||20),gap=Math.max(70,Number(o.gap)||132);
  const direction=['right','left','down','up'].includes(String(o.direction))?String(o.direction):'right';
  const forwardStep=Math.max(60,Number(o.forwardStep)||80),crossStep=Math.max(40,Number(o.crossStep)||60);
  const rect=r=>({x:Number(r.x)||0,y:Number(r.y)||0,width:Math.max(1,Number(r.width)||180),height:Math.max(1,Number(r.height)||76)}),ra=rect(a),rb=rect(bSrc);
  const snap=v=>Math.round(v/grid)*grid;
  const clamp=(x,y)=>({x:Math.max(pad,Math.min((Number(boundsCfg.width)||2400)-pad-tw,x)),y:Math.max(pad,Math.min((Number(boundsCfg.height)||1400)-pad-th,y))});
  const areaOverlap=(p,r)=>{const rr=rect(r),left=Math.max(p.x,rr.x),top=Math.max(p.y,rr.y),right=Math.min(p.x+tw,rr.x+rr.width),bottom=Math.min(p.y+th,rr.y+rr.height);return Math.max(0,right-left)*Math.max(0,bottom-top)};
  const horizontal=direction==='right'||direction==='left';
  const centerA=horizontal?ra.y+ra.height/2:ra.x+ra.width/2,centerB=horizontal?rb.y+rb.height/2:rb.x+rb.width/2,crossCenter=(centerA+centerB)/2;
  let baseMain;
  if(direction==='right')baseMain=Math.max(ra.x+ra.width,rb.x+rb.width)+gap;
  else if(direction==='left')baseMain=Math.min(ra.x,rb.x)-gap-tw;
  else if(direction==='down')baseMain=Math.max(ra.y+ra.height,rb.y+rb.height)+gap;
  else baseMain=Math.min(ra.y,rb.y)-gap-th;
  let best=null;
  for(const crossOffset of [0,-crossStep,crossStep,-crossStep*2,crossStep*2]){
    for(const forwardExtra of [0,forwardStep,forwardStep*2,forwardStep*3,forwardStep*4]){
      let x,y;
      if(direction==='right'){x=baseMain+forwardExtra;y=crossCenter-th/2+crossOffset;}
      else if(direction==='left'){x=baseMain-forwardExtra;y=crossCenter-th/2+crossOffset;}
      else if(direction==='down'){x=crossCenter-tw/2+crossOffset;y=baseMain+forwardExtra;}
      else{x=crossCenter-tw/2+crossOffset;y=baseMain-forwardExtra;}
      const raw={x:snap(x),y:snap(y)},c0=clamp(raw.x,raw.y),p={x:snap(c0.x),y:snap(c0.y)};
      const overlap=list.reduce((sum,r)=>sum+areaOverlap(p,r),0),clampPenalty=Math.abs(p.x-raw.x)+Math.abs(p.y-raw.y);
      const flowPenalty=flowSegmentCollisionPenalty(p,target,ra,o.linkSegments,o.linkClearance)+flowSegmentCollisionPenalty(p,target,rb,o.linkSegments,o.linkClearance);
      const score=overlap*1000+flowPenalty+clampPenalty*20+Math.abs(crossOffset)*5+forwardExtra*.08;
      if(!best||score<best.score)best={...p,direction,score,overlap,crossOffset};
      if(overlap===0&&flowPenalty===0&&clampPenalty===0&&crossOffset===0)return{x:p.x,y:p.y,direction};
    }
  }
  if(best&&best.overlap===0)return{x:best.x,y:best.y,direction};
  const mid={x:(ra.x+rb.x)/2,y:(ra.y+rb.y)/2,width:(ra.width+rb.width)/2,height:(ra.height+rb.height)/2};
  return smartNextStepPosition(mid,target,list,boundsCfg,{...o,direction});
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

global.MapliniEditingCore={makeClipboard,hasNodes,instantiate,groupMoveDelta,movedInternalVias,nextStepPosition,flowSegmentCollisionPenalty,smartNextStepPosition,smartDecisionBranchPositions,smartFlowContinuationPosition,smartBranchRejoinPosition,boundingBox,fitToScreen,alignNodes,distributeNodes,serialize,parse};
})(typeof window!=='undefined'?window:globalThis);
