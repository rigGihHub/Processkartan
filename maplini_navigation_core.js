(function(global){
  'use strict';

  function text(v){return String(v==null?'':v).trim()}
  function nodeMap(nodes){
    const map=new Map();
    for(const raw of Array.isArray(nodes)?nodes:[]){
      if(!raw)continue;
      const id=text(raw.id);if(!id)continue;
      map.set(id,{id,type:text(raw.type),text:text(raw.text)||'Namnlöst steg',x:Number(raw.x)||0,y:Number(raw.y)||0});
    }
    return map;
  }
  function linkParts(link){
    if(!Array.isArray(link)||link.length<2)return null;
    const a=text(link[0]),b=text(link[1]);if(!a||!b)return null;
    let label='';
    if(link.length>3&&link[3]&&typeof link[3]==='object')label=text(link[3].label);
    return{a,b,label};
  }
  function sortVisual(items){return items.slice().sort((a,b)=>a.y-b.y||a.x-b.x||a.text.localeCompare(b.text,'sv'))}
  function analyze(nodes,links,selectedId){
    const map=nodeMap(nodes),incoming=new Map(),outgoing=new Map();
    for(const id of map.keys()){incoming.set(id,[]);outgoing.set(id,[])}
    for(const raw of Array.isArray(links)?links:[]){
      const p=linkParts(raw);if(!p||!map.has(p.a)||!map.has(p.b))continue;
      outgoing.get(p.a).push({id:p.b,label:p.label});
      incoming.get(p.b).push({id:p.a,label:p.label});
    }
    const all=[...map.values()];
    const startTyped=all.filter(n=>n.type==='start');
    const endTyped=all.filter(n=>n.type==='end');
    const starts=sortVisual(startTyped.length?startTyped:all.filter(n=>(incoming.get(n.id)||[]).length===0));
    const ends=sortVisual(endTyped.length?endTyped:all.filter(n=>(outgoing.get(n.id)||[]).length===0));
    const selected=map.get(text(selectedId))||null;
    const enrich=list=>(list||[]).map(ref=>{const n=map.get(ref.id);return n?{...n,branchLabel:text(ref.label)}:null}).filter(Boolean);
    return{
      starts,ends,selected,
      previous:selected?enrich(incoming.get(selected.id)):[],
      next:selected?enrich(outgoing.get(selected.id)):[]
    };
  }
  function orderedOutline(nodes,links){
    const map=nodeMap(nodes),incoming=new Map(),outgoing=new Map(),neighbors=new Map();
    for(const id of map.keys()){incoming.set(id,[]);outgoing.set(id,[]);neighbors.set(id,new Set())}
    for(const raw of Array.isArray(links)?links:[]){
      const p=linkParts(raw);if(!p||!map.has(p.a)||!map.has(p.b))continue;
      outgoing.get(p.a).push({id:p.b,label:p.label});incoming.get(p.b).push({id:p.a,label:p.label});neighbors.get(p.a).add(p.b);neighbors.get(p.b).add(p.a);
    }
    const all=[...map.values()];if(!all.length)return[];
    const components=[];const assigned=new Set();
    for(const seed of sortVisual(all)){
      if(assigned.has(seed.id))continue;
      const ids=[],queue=[seed.id];assigned.add(seed.id);
      while(queue.length){const id=queue.shift();ids.push(id);for(const next of neighbors.get(id)||[]){if(!assigned.has(next)){assigned.add(next);queue.push(next)}}}
      components.push(ids);
    }
    const explicitStarts=new Set(all.filter(n=>n.type==='start').map(n=>n.id));
    components.sort((a,b)=>{
      const aStart=a.some(id=>explicitStarts.has(id)),bStart=b.some(id=>explicitStarts.has(id));
      if(aStart!==bStart)return aStart?-1:1;if(a.length!==b.length)return b.length-a.length;
      const av=sortVisual(a.map(id=>map.get(id)))[0],bv=sortVisual(b.map(id=>map.get(id)))[0];return av.y-bv.y||av.x-bv.x;
    });
    const result=[];
    function branchRank(ref){const label=text(ref.label).toLocaleLowerCase('sv-SE');if(label==='ja')return 0;if(label==='nej')return 1;return 2}
    components.forEach((ids,componentIndex)=>{
      const allowed=new Set(ids),seen=new Set();
      let roots=ids.map(id=>map.get(id)).filter(n=>explicitStarts.has(n.id));
      if(!roots.length)roots=ids.map(id=>map.get(id)).filter(n=>(incoming.get(n.id)||[]).filter(x=>allowed.has(x.id)).length===0);
      if(!roots.length)roots=[sortVisual(ids.map(id=>map.get(id)))[0]];else roots=sortVisual(roots);
      const visit=(id,depth,branchLabel='')=>{
        if(seen.has(id)||!allowed.has(id))return;seen.add(id);const n=map.get(id);result.push({...n,depth,branchLabel:text(branchLabel),disconnected:componentIndex>0});
        const next=(outgoing.get(id)||[]).filter(x=>allowed.has(x.id)&&!seen.has(x.id)).sort((a,b)=>branchRank(a)-branchRank(b)||((map.get(a.id)?.y||0)-(map.get(b.id)?.y||0))||((map.get(a.id)?.x||0)-(map.get(b.id)?.x||0)));
        for(const ref of next){const waiting=(incoming.get(ref.id)||[]).some(prev=>allowed.has(prev.id)&&!seen.has(prev.id));if(!waiting)visit(ref.id,depth+1,ref.label)}
      };
      roots.forEach(root=>visit(root.id,0,''));
      sortVisual(ids.filter(id=>!seen.has(id)).map(id=>map.get(id))).forEach(n=>visit(n.id,0,''));
    });
    return result;
  }
  global.MapliniNavigationCore={analyze,orderedOutline};
})(typeof window!=='undefined'?window:globalThis);
