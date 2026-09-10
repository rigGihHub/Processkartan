/* v0.20.61: conservative suggestions for placeholder/empty process steps */
(function(global){
'use strict';
const DEFAULTS=new Set(['ny aktivitet','nytt steg','beslut?','ny delprocess','nytt objekt','dokument']);
function clean(v,max=240){return String(v==null?'':v).replace(/\s+/g,' ').trim().slice(0,max)}
function norm(v){return clean(v).toLocaleLowerCase('sv-SE')}
function isPlaceholder(title,type){const t=norm(title);if(!t)return true;if(DEFAULTS.has(t))return true;if(type==='process'&&/^ny aktivitet\b/.test(t))return true;return false}
function shortSubject(v){let s=clean(v,120).replace(/[.!?]+$/,'');return s.length>68?s.slice(0,65).trim()+'…':s}
function add(out,text,reason){text=clean(text,110);if(!text||out.some(x=>norm(x.text)===norm(text)))return;out.push({text,reason:clean(reason,180)})}
function suggest(ctx){ctx=(ctx&&typeof ctx==='object')?ctx:{};const type=String(ctx.type||'process');if(!isPlaceholder(ctx.title,type))return {eligible:false,suggestions:[]};
 const incoming=(Array.isArray(ctx.incoming)?ctx.incoming:[]).map(x=>({title:shortSubject(x?.title||x),type:String(x?.type||'')})).filter(x=>x.title);
 const outgoing=(Array.isArray(ctx.outgoing)?ctx.outgoing:[]).map(x=>({title:shortSubject(x?.title||x),type:String(x?.type||'')})).filter(x=>x.title);
 const inputs=(Array.isArray(ctx.inputs)?ctx.inputs:[]).map(shortSubject).filter(Boolean);const outputs=(Array.isArray(ctx.outputs)?ctx.outputs:[]).map(shortSubject).filter(Boolean);const out=[];
 if(type==='process'){
   if(inputs[0])add(out,`Hantera ${inputs[0]}`,`Bygger på angiven input: ${inputs[0]}`);
   if(outputs[0])add(out,`Ta fram ${outputs[0]}`,`Bygger på angiven output: ${outputs[0]}`);
   const prevObj=incoming.find(x=>x.type==='object');if(prevObj)add(out,`Hantera ${prevObj.title}`,`Bygger på föregående objekt: ${prevObj.title}`);
   const nextObj=outgoing.find(x=>x.type==='object');if(nextObj)add(out,`Ta fram ${nextObj.title}`,`Bygger på nästa objekt: ${nextObj.title}`);
   if(incoming[0]&&outgoing[0])add(out,`Fortsätt från ${incoming[0].title}`,`Steget ligger mellan ${incoming[0].title} och ${outgoing[0].title}`);
 }
 if(type==='decision'){
   const next=outgoing[0];if(next)add(out,`Kan vi gå vidare till ${next.title}?`,`Bygger på nästa kopplade steg: ${next.title}`);
 }
 if(type==='subprocess'&&outgoing[0])add(out,`Hantera delen före ${outgoing[0].title}`,`Bygger på nästa kopplade steg: ${outgoing[0].title}`);
 return {eligible:true,suggestions:out.slice(0,3),contextCount:incoming.length+outgoing.length+inputs.length+outputs.length};
}
global.MapliniEmptyStepSuggestionsCore={clean,norm,isPlaceholder,suggest};
})(typeof window!=='undefined'?window:globalThis);
