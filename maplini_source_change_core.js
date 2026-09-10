(function(global){
'use strict';
function clean(s){return String(s||'').replace(/\s+/g,' ').trim()}
function norm(s){return clean(s).toLocaleLowerCase('sv-SE').replace(/[^a-z0-9åäöéüæø ]/gi,' ')}
function tokens(s){return new Set(norm(s).split(/\s+/).filter(x=>x.length>2))}
function sentences(text){return String(text||'').replace(/\r/g,'\n').split(/(?<=[.!?])\s+|\n+/).map(clean).filter(x=>x.length>=8)}
function similarity(a,b){const A=tokens(a),B=tokens(b);if(!A.size||!B.size)return 0;let inter=0;for(const x of A)if(B.has(x))inter++;const union=new Set([...A,...B]).size;return union?inter/union:0}
function compareEvidence(oldEvidence,newText){const old=clean(oldEvidence),pool=sentences(newText);if(!old)return{status:'unknown',score:0,newEvidence:''};const oldN=norm(old);for(const s of pool){const n=norm(s);if(n===oldN||n.includes(oldN)||oldN.includes(n))return{status:'unchanged',score:1,newEvidence:s}}
  let best='',score=0;for(const s of pool){const v=similarity(old,s);if(v>score){score=v;best=s}}
  if(score>=.55)return{status:'changed',score,newEvidence:best};
  return{status:'missing',score,newEvidence:best};
}
function compareSteps(steps,newText,sourceName){const results=[];for(const step of steps||[]){const trace=step?.sourceTrace||{};for(const src of trace.sources||[]){if(sourceName&&String(src.name)!==String(sourceName))continue;const r=compareEvidence(src.evidence,newText);results.push({id:step.id,text:step.text||'',sourceName:src.name||'',oldEvidence:src.evidence||'',...r});}}
  const summary={total:results.length,unchanged:0,changed:0,missing:0,unknown:0};for(const r of results)summary[r.status]=(summary[r.status]||0)+1;return{results,summary};
}
global.MapliniSourceChangeCore={clean,norm,sentences,similarity,compareEvidence,compareSteps};
})(typeof window!=='undefined'?window:globalThis);
