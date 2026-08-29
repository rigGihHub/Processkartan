(function(global){
'use strict';
const rafJobs=new Map();
function signature(values){
  if(!Array.isArray(values))values=[values];
  return values.map(v=>{
    if(v===null)return 'null';
    if(v===undefined)return 'undefined';
    if(typeof v==='string')return 's:'+v;
    if(typeof v==='number')return 'n:'+String(v);
    if(typeof v==='boolean')return 'b:'+(v?'1':'0');
    try{return 'j:'+JSON.stringify(v)}catch(e){return 'x:'+String(v)}
  }).join('\u001f');
}
function rafOnce(key,fn){
  key=String(key||'default');
  if(rafJobs.has(key))return rafJobs.get(key);
  const raf=(typeof requestAnimationFrame==='function')?requestAnimationFrame:(cb=>setTimeout(cb,16));
  const id=raf(()=>{rafJobs.delete(key);fn()});
  rafJobs.set(key,id);
  return id;
}
function debounce(fn,wait=120){
  let timer=null;
  return function(...args){
    if(timer)clearTimeout(timer);
    timer=setTimeout(()=>{timer=null;fn.apply(this,args)},Math.max(0,Number(wait)||0));
  };
}
function shouldRun(previous,next){return previous!==next}
global.MapliniPerformanceCore={signature,rafOnce,debounce,shouldRun};
})(typeof window!=='undefined'?window:globalThis);
