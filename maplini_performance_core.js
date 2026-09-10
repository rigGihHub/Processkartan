(function(global){
  'use strict';
  function signature(values){
    if(!Array.isArray(values))values=[values];
    return values.map(v=>{if(v===null)return 'null';if(v===undefined)return 'undefined';if(typeof v==='string')return 's:'+v;if(typeof v==='number')return 'n:'+String(v);if(typeof v==='boolean')return 'b:'+(v?'1':'0');try{return 'j:'+JSON.stringify(v)}catch(e){return 'x:'+String(v)}}).join('\u001f');
  }
  const rafJobs=new Map();
  function rafOnce(key,fn){key=String(key||'default');if(rafJobs.has(key))return rafJobs.get(key);const raf=(typeof requestAnimationFrame==='function')?requestAnimationFrame:(cb=>setTimeout(cb,16));const id=raf(()=>{rafJobs.delete(key);fn()});rafJobs.set(key,id);return id;}
  function debounce(fn,wait=120){let timer=null;return function(...args){if(timer)clearTimeout(timer);timer=setTimeout(()=>{timer=null;fn.apply(this,args)},Math.max(0,Number(wait)||0));};}
  function shouldRun(previous,next){return previous!==next}
  function policy(nodeCount,linkCount){
    const n=Math.max(0,Number(nodeCount)||0),l=Math.max(0,Number(linkCount)||0);
    const score=n+(l*0.55);
    const large=n>=80||l>=120||score>=130;
    return {large,mode:large?'large':'normal',nodeCount:n,linkCount:l,score:Math.round(score*10)/10};
  }
  global.MapliniPerformanceCore={signature,rafOnce,debounce,shouldRun,policy};
})(typeof window!=='undefined'?window:globalThis);
