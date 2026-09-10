(function(global){'use strict';
function clean(v){return String(v==null?'':v).trim()}
function unique(values){const out=[];for(const v of values||[]){const s=clean(v);if(s&&!out.includes(s))out.push(s)}return out}
function typeLabel(type){return({responsibility:'Olika ansvar',system:'Olika system',type:'Olika stegtyp',order:'Olika ordning'})[clean(type)]||'Källorna skiljer sig'}
function summarize(trace){const sources=Array.isArray(trace?.sources)?trace.sources:[],disagreements=Array.isArray(trace?.disagreements)?trace.disagreements.filter(d=>clean(d?.message)):[];const count=sources.length,has=disagreements.length>0;let headline='';if(count<=1)headline='1 källa bakom steget';else if(!has)headline=`${count} källor stödjer samma steg`;else headline=`${count} källor beskriver steget · ${disagreements.length} uppgift behöver uppmärksamhet`;
const detail=has?'Maplini har inte dolt skillnaden mellan underlagen. Se vad som skiljer sig nedan.':count>1?'Källorna har slagits ihop eftersom de beskriver samma processsteg.':'';
return{sourceCount:count,hasDisagreement:has,headline,detail,disagreements:disagreements.map(d=>({label:typeLabel(d.type),message:clean(d.message),sources:unique(d.sources),resolution:clean(d.resolution)}))}}
global.MapliniSourceSupportCore={summarize,typeLabel};
})(typeof window!=='undefined'?window:globalThis);
