(function(global){
'use strict';
function clean(s){return String(s||'').replace(/\s+/g,' ').trim()}
function sentencePool(text){
  const raw=String(text||'').replace(/\r/g,'\n').replace(/[\t ]+/g,' ').replace(/\n{3,}/g,'\n\n');
  const lines=raw.split(/\n+/).map(x=>clean(x.replace(/^\s*(?:[-*•]+|\d+[.)]|[a-zA-Z][.)])\s*/,''))).filter(Boolean);
  const out=[];for(const line of lines){out.push(...line.split(/(?<=[.!?])\s+(?=[A-ZÅÄÖ0-9])/).map(clean).filter(Boolean))}return out;
}
const WORK=/\b(?:ska|skall|måste|bör|ansvarar|utför|hanter|kontroller|registr|godkänn|gransk|signer|arkiver|rapporter|beställ|leverer|behandl|planer|bokar|skickar|tar emot|mottar)\w*/i;
const CASE=/\b(?:beslut|beslutade|ansökan|ansöker|remiss|yttrande|överklag|överpröv|tilldelning|upphandling|anbud|godkänn|avslag|ärende|handlägg|diarieför|nämnd|styrelse|myndighet|kommunfullmäktige)\w*/i;
const EVENT=/\b(?:meddelade|uppgav|sade|lanserade|öppnade|stängde|köpte|sålde|förvärvade|tecknade|startade|påbörjade|avslutade|införde|ändrade|ökade|minskade|steg|föll|beslutade|godkände|avvisade|presenterade|publicerade|drabbades|intr[äa]ffade|hände|skedde|följde|ledde|resulterade|orsakade|därefter|sedan|senare|först|slutligen)\b/i;
function score(text,re){return sentencePool(text).filter(s=>re.test(s)).length}
function classifySource(text){
  const s=sentencePool(text),n=Math.max(1,s.length),work=score(text,WORK),caseScore=score(text,CASE),events=score(text,EVENT);
  let type='general_flow';
  if(caseScore>=Math.max(2,work*.75)&&caseScore/n>=.10)type='case_flow';
  else if(work>=Math.max(2,events*.8)&&work/n>=.12)type='work_process';
  else if(events>=2||events/n>=.12)type='event_timeline';
  const confidence=Math.min(.95,.5+Math.max(work,caseScore,events)/n*.8);
  return{type,label:{work_process:'Arbetsprocess',case_flow:'Besluts-/ärendeflöde',event_timeline:'Händelseförlopp',general_flow:'Allmänt flöde'}[type],confidence,scores:{work,case:caseScore,events},sentences:n};
}
const RELATIONS=[
  {kind:'cause_effect',label:'Orsak → konsekvens',re:/\b(?:därför|på grund av|till följd av|vilket (?:ledde|leder) till|ledde till|leder till|orsakade|orsakar|resulterade i|resulterar i|som följd|because|therefore|resulted in|led to|caused)\b/i},
  {kind:'decision_effect',label:'Beslut → effekt',re:/\b(?:beslut(?:et|ade)? (?:innebär|innebar|medför|medförde|gör att)|beslutade att .{0,80}(?:vilket|så att)|decision .{0,60}(?:means|resulted|caused))\b/i},
  {kind:'problem_action',label:'Problem → åtgärd',re:/\b(?:för att (?:lösa|åtgärda|hantera|motverka)|som åtgärd|åtgärden blev|svarade med|bemötte .{0,40} med|to address|to solve|in response to)\b/i},
  {kind:'condition_result',label:'Villkor → resultat',re:/\b(?:om .{2,100}(?:så|kommer|blir|ska)|under förutsättning att|förutsatt att|if .{2,100}(?:then|will)|provided that)\b/i},
  {kind:'event_reaction',label:'Händelse → reaktion',re:/\b(?:som reaktion på|efter beskedet|efter händelsen|därefter svarade|reagerade genom|in reaction to|following (?:the )?(?:announcement|event)|responded by)\b/i},
  {kind:'actor_action',label:'Aktör → handling',re:/^(?:[A-ZÅÄÖ][\p{L}0-9&.'’\-]+(?:\s+[A-ZÅÄÖ][\p{L}0-9&.'’\-]+){0,4}|Kommunen|Bolaget|Företaget|Regeringen|Myndigheten|Nämnden|Styrelsen)\s+(?:beslutade|meddelade|införde|startade|lanserade|godkände|avvisade|presenterade|publicerade|köpte|sålde|förvärvade|tecknade|stängde|öppnade)\b/iu}
];
function explicitRelation(previous,current){
  const a=clean(previous),b=clean(current),pair=`${a} ${b}`;
  for(const r of RELATIONS){const target=r.kind==='actor_action'?b:pair;if(r.re.test(target))return{kind:r.kind,label:r.label,confidence:r.kind==='actor_action'?.78:.86,evidence:b};}
  return null;
}
function enrichRelations(flow){
  const items=flow?.items||[],byId=new Map(items.map(x=>[x.id,x]));let count=0;
  for(const e of flow?.edges||[]){if(e.conflict||e.kind==='loop'||e.label==='Ja'||e.label==='Nej')continue;const a=byId.get(e.from),b=byId.get(e.to);if(!a||!b)continue;const rel=explicitRelation(a.evidence||a.text,b.evidence||b.text);if(!rel)continue;e.relationKind=rel.kind;e.relationLabel=rel.label;e.relationEvidence=rel.evidence;e.relationConfidence=rel.confidence;if(!e.label)e.label=rel.label;count++;}
  flow.summary=flow.summary||{};flow.summary.relations=count;return flow;
}
function eventItems(text,limit=80){
  const out=[];let id=0;for(const s0 of sentencePool(text)){
    const s=clean(s0);if(s.length<10||s.length>260)continue;if(!EVENT.test(s)&&!CASE.test(s))continue;
    const review=!EVENT.test(s);out.push({id:'a'+(++id),text:s.replace(/[.]$/,''),type:/\?$/.test(s)?'decision':'process',responsibleRole:'',system:'',inputs:[],outputs:[],evidence:s,confidence:review?.58:.72,confidenceLabel:review?'Behöver kontroll':'Trolig tolkning',review,flowColumn:out.length,flowLane:0,flowKind:'sequence'});if(out.length>=limit)break;
  }
  if(out.length<2){for(const s0 of sentencePool(text)){const s=clean(s0);if(s.length>=10&&s.length<=220&&!out.some(x=>x.text===s)){out.push({id:'a'+(++id),text:s.replace(/[.]$/,''),type:'process',responsibleRole:'',system:'',inputs:[],outputs:[],evidence:s,confidence:.52,confidenceLabel:'Behöver kontroll',review:true,flowColumn:out.length,flowLane:0,flowKind:'sequence'});if(out.length>=Math.min(limit,12))break}}
  }
  const edges=[];for(let i=1;i<out.length;i++)edges.push({from:out[i-1].id,to:out[i].id,label:'',kind:'sequence',confidence:.62});
  return enrichRelations({items:out,edges,conflicts:[],summary:{steps:out.length,decisions:out.filter(x=>x.type==='decision').length,roles:0,systems:0,needsReview:out.filter(x=>x.review).length,branches:0,loops:0,subProcesses:0,documents:1,conflicts:0,relations:0},hasRealFlow:false});
}
function plan(text,documentCore,limit=80){
  const classification=classifySource(text);let flow;
  if(classification.type==='work_process'||classification.type==='case_flow')flow=documentCore&&documentCore.interpretFlow?documentCore.interpretFlow(text,limit):eventItems(text,limit);
  else flow=eventItems(text,limit);
  if((flow.items||[]).length<2&&documentCore&&documentCore.interpretFlow)flow=documentCore.interpretFlow(text,limit);
  enrichRelations(flow);flow.sourceClassification=classification;return flow;
}
function normalizeUrl(raw){let s=clean(raw);if(!s)return'';if(!/^https?:\/\//i.test(s))s='https://'+s;try{const u=new URL(s);if(!/^https?:$/.test(u.protocol))return'';return u.toString()}catch(_){return''}}
function readerUrl(raw){const u=normalizeUrl(raw);return u?'https://r.jina.ai/'+u:''}
function markdownToText(md){return String(md||'').replace(/^Title:\s*.*$/gmi,'').replace(/^URL Source:\s*.*$/gmi,'').replace(/^Published Time:\s*.*$/gmi,'').replace(/^Markdown Content:\s*$/gmi,'').replace(/!\[[^\]]*\]\([^)]*\)/g,' ').replace(/\[([^\]]+)\]\([^)]*\)/g,'$1').replace(/^#{1,6}\s+/gm,'').replace(/[*_`~]/g,'').replace(/\n{3,}/g,'\n\n').trim()}
global.MapliniAnySourceCore={sentencePool,classifySource,explicitRelation,enrichRelations,eventItems,plan,normalizeUrl,readerUrl,markdownToText};
})(typeof window!=='undefined'?window:globalThis);
