(function(global){
'use strict';
const DEFAULT_STYLE={color:'#5b6775',width:2,end:'arrow',dash:'solid',viaX:null,viaY:null,freeDx:0,freeDy:0,routing:'straight',anchorMode:'manual',label:'',autoManaged:false};

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
  return [String(sourceId),String(targetId),side||'right',Object.assign(cloneStyle(),{routing:'orthogonal',anchorMode:'auto',autoManaged:true},stylePatch||{})];
}
function autoSides(dx,dy){
  if(Math.abs(dx)>=Math.abs(dy))return dx>=0?['right','left']:['left','right'];
  return dy>=0?['bottom','top']:['top','bottom'];
}
function routePoints(x1,y1,x2,y2,sourceSide,targetSide,styleValue){
  const st=cloneStyle(styleValue);
  if(st.routing==='free'){
    // Free routing keeps both endpoints attached to their nodes while translating the
    // connector's middle body independently. Offsets are relative to the direct line,
    // so moving either node makes the free route follow automatically.
    const ox=Number(st.freeDx)||0,oy=Number(st.freeDy)||0;
    const p1=[x1+(x2-x1)*0.25+ox,y1+(y2-y1)*0.25+oy];
    const p2=[x1+(x2-x1)*0.75+ox,y1+(y2-y1)*0.75+oy];
    return [[x1,y1],p1,p2,[x2,y2]];
  }
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

function cleanPoints(points){
  const out=[];
  for(const p of Array.isArray(points)?points:[]){
    if(!Array.isArray(p)||p.length<2)continue;
    const q=[Number(p[0])||0,Number(p[1])||0],prev=out[out.length-1];
    if(!prev||prev[0]!==q[0]||prev[1]!==q[1])out.push(q);
  }
  return out;
}
function segmentHitsRect(a,b,r,padding=0){
  const left=Number(r.left)-padding,right=Number(r.right)+padding,top=Number(r.top)-padding,bottom=Number(r.bottom)+padding;
  if(a[0]===b[0]){const x=a[0],lo=Math.min(a[1],b[1]),hi=Math.max(a[1],b[1]);return x>=left&&x<=right&&hi>=top&&lo<=bottom;}
  if(a[1]===b[1]){const y=a[1],lo=Math.min(a[0],b[0]),hi=Math.max(a[0],b[0]);return y>=top&&y<=bottom&&hi>=left&&lo<=right;}
  return false;
}
function properSegmentsCross(a,b,c,d){
  const ax=Number(a[0])||0,ay=Number(a[1])||0,bx=Number(b[0])||0,by=Number(b[1])||0;
  const cx=Number(c[0])||0,cy=Number(c[1])||0,dx=Number(d[0])||0,dy=Number(d[1])||0;
  const cross=(px,py,qx,qy,rx,ry)=>(qx-px)*(ry-py)-(qy-py)*(rx-px);
  const o1=cross(ax,ay,bx,by,cx,cy),o2=cross(ax,ay,bx,by,dx,dy),o3=cross(cx,cy,dx,dy,ax,ay),o4=cross(cx,cy,dx,dy,bx,by);
  const eps=1e-7;
  /* Only count a real interior crossing. Endpoint touches, shared corners and collinear
     overlap are normal in process diagrams and should not trigger a detour. */
  if(Math.abs(o1)<=eps||Math.abs(o2)<=eps||Math.abs(o3)<=eps||Math.abs(o4)<=eps)return false;
  return (o1>0)!==(o2>0)&&(o3>0)!==(o4>0);
}
function parallelSegmentOverlap(a,b,c,d,tolerance=10){
  const ax=Number(a[0])||0,ay=Number(a[1])||0,bx=Number(b[0])||0,by=Number(b[1])||0;
  const cx=Number(c[0])||0,cy=Number(c[1])||0,dx=Number(d[0])||0,dy=Number(d[1])||0;
  const ah=Math.abs(ay-by)<1e-7,bh=Math.abs(cy-dy)<1e-7,av=Math.abs(ax-bx)<1e-7,bv=Math.abs(cx-dx)<1e-7;
  if(ah&&bh&&Math.abs(ay-cy)<=tolerance){
    const overlap=Math.min(Math.max(ax,bx),Math.max(cx,dx))-Math.max(Math.min(ax,bx),Math.min(cx,dx));
    return Math.max(0,overlap);
  }
  if(av&&bv&&Math.abs(ax-cx)<=tolerance){
    const overlap=Math.min(Math.max(ay,by),Math.max(cy,dy))-Math.max(Math.min(ay,by),Math.min(cy,dy));
    return Math.max(0,overlap);
  }
  return 0;
}
function routeParallelOverlap(points,segments,context,{tolerance=10,sharedAllowance=30}={}){
  const pts=cleanPoints(points);let overlap=0;
  const sourceId=String(context&&context.sourceId||''),targetId=String(context&&context.targetId||'');
  for(let i=1;i<pts.length;i++){
    const a=pts[i-1],b=pts[i];
    for(const s of segments||[]){
      if(!s)continue;
      const ss=String(s.sourceId||''),tt=String(s.targetId||'');
      const shared=Boolean((sourceId&&(ss===sourceId||tt===sourceId))||(targetId&&(ss===targetId||tt===targetId)));
      let amount=parallelSegmentOverlap(a,b,[Number(s.x1)||0,Number(s.y1)||0],[Number(s.x2)||0,Number(s.y2)||0],tolerance);
      /* A short shared trunk directly beside a decision/rejoin is visually normal. Longer
         overlap is what makes two connectors become indistinguishable, so only that excess
         is penalized for links sharing an endpoint. */
      if(shared)amount=Math.max(0,amount-sharedAllowance);
      overlap+=amount;
    }
  }
  return overlap;
}
function routeCrossingCount(points,segments,context){
  const pts=cleanPoints(points);let crossings=0;
  const sourceId=String(context&&context.sourceId||''),targetId=String(context&&context.targetId||'');
  for(let i=1;i<pts.length;i++){
    const a=pts[i-1],b=pts[i];
    for(const s of segments||[]){
      if(!s)continue;
      /* Links sharing an endpoint with the candidate are allowed to fan in/out naturally;
         only unrelated flow lines count as avoidable crossings. */
      const ss=String(s.sourceId||''),tt=String(s.targetId||'');
      if(sourceId&&(ss===sourceId||tt===sourceId))continue;
      if(targetId&&(ss===targetId||tt===targetId))continue;
      if(properSegmentsCross(a,b,[Number(s.x1)||0,Number(s.y1)||0],[Number(s.x2)||0,Number(s.y2)||0]))crossings++;
    }
  }
  return crossings;
}
function routeScore(points,obstacles,padding=18,segments=[],context=null){
  const pts=cleanPoints(points);let length=0,hits=0;
  for(let i=1;i<pts.length;i++){
    length+=Math.abs(pts[i][0]-pts[i-1][0])+Math.abs(pts[i][1]-pts[i-1][1]);
    for(const r of obstacles||[])if(segmentHitsRect(pts[i-1],pts[i],r,padding))hits++;
  }
  const crossings=routeCrossingCount(pts,segments,context);
  const parallelOverlap=routeParallelOverlap(pts,segments,context);
  return hits*100000+crossings*420+parallelOverlap*7+length+Math.max(0,pts.length-2)*8;
}
function smartOrthogonalRoute(x1,y1,x2,y2,sourceSide,targetSide,styleValue,obstacles,padding=18,segments=[],context=null){
  const st=cloneStyle(styleValue),base=routePoints(x1,y1,x2,y2,sourceSide,targetSide,st);
  if(st.routing!=='orthogonal')return base;
  const obs=Array.isArray(obstacles)?obstacles.filter(Boolean):[];
  const segs=Array.isArray(segments)?segments.filter(Boolean):[];
  if(!obs.length&&!segs.length)return base;
  const candidates=[base];
  const srcHorizontal=sourceSide==='left'||sourceSide==='right';
  const dstHorizontal=targetSide==='left'||targetSide==='right';
  const xs=[(x1+x2)/2],ys=[(y1+y2)/2];
  for(const r of obs){
    xs.push(Number(r.left)-padding-12,Number(r.right)+padding+12);
    ys.push(Number(r.top)-padding-12,Number(r.bottom)+padding+12);
  }
  /* Existing flow lines also provide possible corridors. A small offset keeps the new
     route visibly separate instead of merely moving the crossing onto the old line. */
  for(const s of segs){
    const x1=Number(s.x1)||0,x2=Number(s.x2)||0,y1=Number(s.y1)||0,y2=Number(s.y2)||0;
    xs.push(x1-28,x1+28,x2-28,x2+28);
    ys.push(y1-28,y1+28,y2-28,y2+28);
  }
  const compactCorridors=(values,center,limit=18)=>{
    const unique=[...new Set(values.map(v=>Math.round(Number(v)||0)))];
    unique.sort((a,b)=>Math.abs(a-center)-Math.abs(b-center));
    return unique.slice(0,limit);
  };
  const routeXs=compactCorridors(xs,(x1+x2)/2),routeYs=compactCorridors(ys,(y1+y2)/2);
  if(srcHorizontal&&dstHorizontal){
    for(const x of routeXs)candidates.push([[x1,y1],[x,y1],[x,y2],[x2,y2]]);
    const sx=x1+(sourceSide==='right'?24:-24),tx=x2+(targetSide==='right'?24:-24);
    for(const y of routeYs)candidates.push([[x1,y1],[sx,y1],[sx,y],[tx,y],[tx,y2],[x2,y2]]);
  }else if(!srcHorizontal&&!dstHorizontal){
    for(const y of routeYs)candidates.push([[x1,y1],[x1,y],[x2,y],[x2,y2]]);
    const sy=y1+(sourceSide==='bottom'?24:-24),ty=y2+(targetSide==='bottom'?24:-24);
    for(const x of routeXs)candidates.push([[x1,y1],[x1,sy],[x,sy],[x,ty],[x2,ty],[x2,y2]]);
  }else{
    // Mixed anchors need a two-turn dogleg when the natural elbow is blocked.
    for(const x of routeXs)for(const y of routeYs){
      if(srcHorizontal)candidates.push([[x1,y1],[x,y1],[x,y],[x2,y],[x2,y2]]);
      else candidates.push([[x1,y1],[x1,y],[x,y],[x,y2],[x2,y2]]);
    }
  }
  let best=cleanPoints(candidates[0]),bestScore=routeScore(best,obs,padding,segs,context);
  for(let i=1;i<candidates.length;i++){
    const candidate=cleanPoints(candidates[i]),score=routeScore(candidate,obs,padding,segs,context);
    if(score<bestScore){best=candidate;bestScore=score;}
  }
  return best;
}


function rectOverlap(a,b,padding=0){
  return !(Number(a.right)+padding<Number(b.left)||Number(a.left)-padding>Number(b.right)||Number(a.bottom)+padding<Number(b.top)||Number(a.top)-padding>Number(b.bottom));
}
function smartLabelPlacement(points,width=60,height=26,obstacles=[],occupied=[],options={}){
  const pts=cleanPoints(points);if(pts.length<2)return null;
  const offset=Math.max(12,Number(options.offset)||22),clearance=Math.max(6,Number(options.clearance)||8);
  const candidates=[];let total=0;const segs=[];
  for(let i=1;i<pts.length;i++){
    const a=pts[i-1],b=pts[i],dx=b[0]-a[0],dy=b[1]-a[1],len=Math.hypot(dx,dy);
    if(len<1)continue;segs.push({a,b,dx,dy,len,start:total});total+=len;
  }
  if(!segs.length)return null;
  const pathMid=total/2;
  for(const seg of segs){
    const horizontal=Math.abs(seg.dx)>=Math.abs(seg.dy);
    for(const t of [0.5,0.38,0.62]){
      const along=seg.start+seg.len*t;
      const baseX=seg.a[0]+seg.dx*t,baseY=seg.a[1]+seg.dy*t;
      let nx=-seg.dy/seg.len,ny=seg.dx/seg.len;
      if(horizontal&&ny>0){nx=-nx;ny=-ny}else if(!horizontal&&nx<0){nx=-nx;ny=-ny}
      for(const sign of [1,-1]){
        const x=baseX+nx*offset*sign,y=baseY+ny*offset*sign;
        const box={left:x-width/2,right:x+width/2,top:y-height/2,bottom:y+height/2};
        let obstacleHits=0,labelHits=0;
        for(const r of obstacles||[])if(r&&rectOverlap(box,r,clearance))obstacleHits++;
        for(const r of occupied||[])if(r&&rectOverlap(box,r,6))labelHits++;
        const endClear=Math.min(seg.len*t,seg.len*(1-t));
        const bendPenalty=endClear<Math.min(34,width*.35)?(Math.min(34,width*.35)-endClear)*40:0;
        const midpointPenalty=Math.abs(along-pathMid)*0.12;
        const shortPenalty=Math.max(0,width+18-seg.len)*18;
        const sidePenalty=sign<0?10:0;
        const score=obstacleHits*100000+labelHits*60000+bendPenalty+shortPenalty+midpointPenalty+sidePenalty;
        candidates.push({x,y,box,score,segmentLength:seg.len});
      }
    }
  }
  candidates.sort((a,b)=>a.score-b.score||b.segmentLength-a.segmentLength);
  return candidates[0]||null;
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
function setFreeOffset(links,index,dx,dy){return setStyle(links,index,{routing:'free',freeDx:Number(dx)||0,freeDy:Number(dy)||0,viaX:null,viaY:null});}
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

global.MapliniConnectorCore={DEFAULT_STYLE,cloneStyle,normalizeLink,normalizeLinks,style,setStyle,create,setVia,setFreeOffset,autoSides,routePoints,smartOrthogonalRoute,segmentHitsRect,properSegmentsCross,parallelSegmentOverlap,routeParallelOverlap,routeCrossingCount,routeScore,smartLabelPlacement,pathData,midpoint,rectsIntersect,removeSelected,removeAt,selectionAfterDelete,decisionLabel,splitLink};
})(typeof window!=='undefined'?window:globalThis);
