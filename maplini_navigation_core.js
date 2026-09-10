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
  global.MapliniNavigationCore={analyze};
})(typeof window!=='undefined'?window:globalThis);
