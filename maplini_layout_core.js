(function(global){
'use strict';

function asNodes(items){
  return (Array.isArray(items)?items:[]).filter(x=>x&&x.id!=null).map(x=>({
    id:String(x.id),x:Number(x.x)||0,y:Number(x.y)||0,
    width:Math.max(1,Number(x.width)||180),height:Math.max(1,Number(x.height)||76)
  }));
}
function labelOf(link){
  if(!Array.isArray(link)||!link[3]||typeof link[3]!=='object')return '';
  return String(link[3].label||'').trim();
}
function internalEdges(links,allowed){
  const out=[];
  for(let i=0;i<(Array.isArray(links)?links:[]).length;i++){
    const link=links[i];
    if(!Array.isArray(link)||link.length<2)continue;
    const from=String(link[0]),to=String(link[1]);
    if(from===to||!allowed.has(from)||!allowed.has(to))continue;
    out.push({from,to,label:labelOf(link),index:i,feedback:false});
  }
  return out;
}
function boundingBox(nodes){
  if(!nodes.length)return null;
  let left=Infinity,top=Infinity,right=-Infinity,bottom=-Infinity;
  for(const n of nodes){left=Math.min(left,n.x);top=Math.min(top,n.y);right=Math.max(right,n.x+n.width);bottom=Math.max(bottom,n.y+n.height)}
  return {left,top,right,bottom,width:right-left,height:bottom-top,centerX:(left+right)/2,centerY:(top+bottom)/2};
}
function branchBias(label){
  const text=String(label||'').trim().toLocaleLowerCase('sv-SE');
  if(['ja','yes','true','godkänd','godkand','ok'].includes(text))return -0.35;
  if(['nej','no','false','avslag','avslagen'].includes(text))return 0.35;
  return 0;
}
function markFeedbackEdges(nodes,edges,orientation){
  const nodeById=new Map(nodes.map(n=>[n.id,n]));
  const cross=n=>orientation==='horizontal'?n.y:n.x;
  const main=n=>orientation==='horizontal'?n.x:n.y;
  const visualIds=nodes.slice().sort((a,b)=>main(a)-main(b)||cross(a)-cross(b)||a.id.localeCompare(b.id)).map(n=>n.id);
  const outgoing=new Map(nodes.map(n=>[n.id,[]])),incomingCount=new Map(nodes.map(n=>[n.id,0]));
  edges.forEach(e=>{outgoing.get(e.from).push(e);incomingCount.set(e.to,(incomingCount.get(e.to)||0)+1)});
  for(const list of outgoing.values())list.sort((a,b)=>{
    const na=nodeById.get(a.to),nb=nodeById.get(b.to);
    return branchBias(a.label)-branchBias(b.label)||cross(na)-cross(nb)||main(na)-main(nb);
  });
  const state=new Map();
  function visit(id){
    state.set(id,1);
    for(const e of outgoing.get(id)||[]){
      const s=state.get(e.to)||0;
      if(s===1){e.feedback=true;continue;}
      if(s===0)visit(e.to);
    }
    state.set(id,2);
  }
  const roots=visualIds.filter(id=>(incomingCount.get(id)||0)===0);
  for(const id of roots)if(!state.get(id))visit(id);
  for(const id of visualIds)if(!state.get(id))visit(id);
  return edges;
}
function ranksFor(nodes,edges){
  const forward=edges.filter(e=>!e.feedback),ids=nodes.map(n=>n.id);
  const incoming=new Map(ids.map(id=>[id,0])),outgoing=new Map(ids.map(id=>[id,[]]));
  forward.forEach(e=>{incoming.set(e.to,(incoming.get(e.to)||0)+1);outgoing.get(e.from).push(e.to)});
  const queue=[],rank=new Map();
  ids.forEach(id=>{if((incoming.get(id)||0)===0){rank.set(id,0);queue.push(id)}});
  while(queue.length){
    const id=queue.shift(),base=rank.get(id)||0;
    for(const to of outgoing.get(id)||[]){
      rank.set(to,Math.max(rank.get(to)||0,base+1));
      incoming.set(to,(incoming.get(to)||0)-1);
      if(incoming.get(to)===0)queue.push(to);
    }
  }
  // Defensive fallback: after feedback-edge removal this should be rare, but never let malformed graphs explode.
  let fallback=Math.max(0,...rank.values());
  for(const n of nodes)if(!rank.has(n.id))rank.set(n.id,++fallback);
  return rank;
}
function orderLevels(nodes,edges,rank,orientation){
  const cross=n=>orientation==='horizontal'?n.y:n.x,nodeById=new Map(nodes.map(n=>[n.id,n]));
  const groups=new Map();
  nodes.forEach(n=>{const r=rank.get(n.id)||0;if(!groups.has(r))groups.set(r,[]);groups.get(r).push(n.id)});
  const levels=[...groups.keys()].sort((a,b)=>a-b);
  const forward=edges.filter(e=>!e.feedback);
  const incoming=new Map(nodes.map(n=>[n.id,[]])),outgoing=new Map(nodes.map(n=>[n.id,[]]));
  forward.forEach(e=>{incoming.get(e.to).push(e);outgoing.get(e.from).push(e)});
  const incomingBias=new Map(nodes.map(n=>[n.id,0]));
  for(const n of nodes){const es=incoming.get(n.id)||[];if(es.length)incomingBias.set(n.id,es.reduce((sum,e)=>sum+branchBias(e.label),0)/es.length)}
  for(const r of levels)groups.get(r).sort((a,b)=>cross(nodeById.get(a))-cross(nodeById.get(b))||a.localeCompare(b));
  function indexMap(){
    const m=new Map();
    for(const r of levels)groups.get(r).forEach((id,i)=>m.set(id,i));
    return m;
  }
  function sweep(direction){
    const ordered=direction==='down'?levels:levels.slice().reverse(),idx=indexMap();
    for(const r of ordered){
      const list=groups.get(r),neighbors=direction==='down'?incoming:outgoing;
      list.sort((a,b)=>{
        const score=id=>{
          const es=neighbors.get(id)||[];
          if(!es.length)return idx.get(id)||0;
          let total=0;
          for(const e of es){
            const other=direction==='down'?e.from:e.to;
            total+=(idx.get(other)||0)+(direction==='down'?branchBias(e.label):0);
          }
          return total/es.length;
        };
        return score(a)-score(b)||(incomingBias.get(a)||0)-(incomingBias.get(b)||0)||cross(nodeById.get(a))-cross(nodeById.get(b))||a.localeCompare(b);
      });
    }
  }
  // A few barycentric sweeps reduce crossings while keeping layout deterministic.
  for(let i=0;i<3;i++){sweep('down');sweep('up')}
  return {groups,levels};
}
function smartLayout(items,links,options){
  const nodes=asNodes(items);if(nodes.length<2)return {};
  const opts=options||{},orientation=opts.orientation==='vertical'?'vertical':'horizontal';
  const allowed=new Set(nodes.map(n=>n.id)),edges=markFeedbackEdges(nodes,internalEdges(links,allowed),orientation),rank=ranksFor(nodes,edges);
  const ordered=orderLevels(nodes,edges,rank,orientation),groups=ordered.groups,levels=ordered.levels,box=boundingBox(nodes);
  let mainGap=Math.max(32,Number(opts.mainGap)||160),baseCrossGap=Math.max(24,Number(opts.crossGap)||72);
  const bounds=opts.bounds||{},padding=Math.max(0,Number(bounds.padding)||24),boundWidth=Math.max(1,Number(bounds.width)||2400),boundHeight=Math.max(1,Number(bounds.height)||1400);
  const nodeById=new Map(nodes.map(n=>[n.id,n])),levelMainSize=new Map();
  levels.forEach(r=>{const list=groups.get(r).map(id=>nodeById.get(id));levelMainSize.set(r,Math.max(...list.map(n=>orientation==='horizontal'?n.width:n.height)))});
  const totalMain=levels.reduce((sum,r)=>sum+levelMainSize.get(r),0),availableMain=(orientation==='horizontal'?boundWidth:boundHeight)-padding*2;
  if(levels.length>1&&totalMain+mainGap*(levels.length-1)>availableMain)mainGap=Math.max(32,(availableMain-totalMain)/(levels.length-1));
  let mainCursor=Math.max(padding,orientation==='horizontal'?box.left:box.top);
  const out={};
  for(const r of levels){
    const list=groups.get(r).map(id=>nodeById.get(id));
    const crossSizes=list.map(n=>orientation==='horizontal'?n.height:n.width),rawCross=crossSizes.reduce((a,b)=>a+b,0),availableCross=(orientation==='horizontal'?boundHeight:boundWidth)-padding*2;
    const crossGap=list.length>1?Math.max(24,Math.min(baseCrossGap,(availableCross-rawCross)/(list.length-1))):0,totalCross=rawCross+crossGap*Math.max(0,list.length-1);
    const crossCenter=orientation==='horizontal'?box.centerY:box.centerX,crossStart=Math.max(padding,Math.min((orientation==='horizontal'?boundHeight:boundWidth)-padding-totalCross,crossCenter-totalCross/2));
    let crossCursor=crossStart;
    for(const n of list){
      if(orientation==='horizontal')out[n.id]={x:Math.round(mainCursor),y:Math.round(crossCursor)};
      else out[n.id]={x:Math.round(crossCursor),y:Math.round(mainCursor)};
      crossCursor+=(orientation==='horizontal'?n.height:n.width)+crossGap;
    }
    mainCursor+=levelMainSize.get(r)+mainGap;
  }
  const laid=nodes.map(n=>({id:n.id,x:out[n.id].x,y:out[n.id].y,width:n.width,height:n.height})),newBox=boundingBox(laid);
  let dx=box.left-newBox.left,dy=box.top-newBox.top;
  if(newBox.right+dx>boundWidth-padding)dx-=newBox.right+dx-(boundWidth-padding);
  if(newBox.left+dx<padding)dx+=padding-(newBox.left+dx);
  if(newBox.bottom+dy>boundHeight-padding)dy-=newBox.bottom+dy-(boundHeight-padding);
  if(newBox.top+dy<padding)dy+=padding-(newBox.top+dy);
  Object.keys(out).forEach(id=>{out[id]={x:Math.round(out[id].x+dx),y:Math.round(out[id].y+dy)}});
  return out;
}

function analyzeLayout(items,links,options){
  const nodes=asNodes(items),orientation=options&&options.orientation==='vertical'?'vertical':'horizontal',allowed=new Set(nodes.map(n=>n.id));
  const edges=markFeedbackEdges(nodes,internalEdges(links,allowed),orientation),rank=ranksFor(nodes,edges);
  return {feedbackEdges:edges.filter(e=>e.feedback).map(e=>({from:e.from,to:e.to,label:e.label})),ranks:Object.fromEntries(nodes.map(n=>[n.id,rank.get(n.id)||0]))};
}

global.MapliniLayoutCore={smartLayout,boundingBox,analyzeLayout};
})(typeof window!=='undefined'?window:globalThis);
