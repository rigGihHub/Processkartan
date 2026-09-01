(function(global){
'use strict';
const MAX={description:12000,responsibleRole:300,system:500,instruction:4000,risk:4000,control:4000,kpi:1000,duration:300};
function text(v,max){return (typeof v==='string'?v:'').trim().slice(0,max);}
function normalize(info){
  info=(info&&typeof info==='object'&&!Array.isArray(info))?info:{};
  return {
    description:text(info.description,MAX.description),
    responsibleRole:text(info.responsibleRole,MAX.responsibleRole),
    system:text(info.system,MAX.system),
    instruction:text(info.instruction,MAX.instruction),
    risk:text(info.risk,MAX.risk),
    control:text(info.control,MAX.control),
    kpi:text(info.kpi,MAX.kpi),
    duration:text(info.duration,MAX.duration)
  };
}
function isEmpty(info){const n=normalize(info);return Object.values(n).every(v=>!v);}
function completion(info){const n=normalize(info);const keys=Object.keys(n);return {filled:keys.filter(k=>Boolean(n[k])).length,total:keys.length};}
global.MapliniProcessInfoCore={normalize,isEmpty,completion,MAX};
})(typeof window!=='undefined'?window:globalThis);
