(function(global){
'use strict';
function clean(s){return String(s||'').replace(/\s+/g,' ').trim();}
function unique(arr){const out=[];for(const v of arr){const x=clean(v);if(x&&!out.some(y=>y.toLocaleLowerCase('sv-SE')===x.toLocaleLowerCase('sv-SE')))out.push(x)}return out;}
const ROLE_WORDS=['kundservice','ekonomi','inköp','sälj','försäljning','lager','produktion','transport','chaufför','arbetsledare','teamledare','chef','projektledare','handläggare','administratör','beställare','leverantör','kund','medarbetare','controller','hr','it','support','kvalitet','miljö','drift','planerare'];
function sentencePool(text){
  const raw=String(text||'').replace(/\r/g,'\n').replace(/[\t ]+/g,' ').replace(/\n{3,}/g,'\n\n');
  const lines=raw.split(/\n+/).map(x=>clean(x.replace(/^\s*(?:[-*•]+|\d+[.)]|[a-zA-Z][.)])\s*/,''))).filter(Boolean);
  const pool=[];for(const line of lines){const parts=line.split(/(?<=[.!?])\s+(?=[A-ZÅÄÖ])/);pool.push(...parts);}
  return pool.map(clean).filter(Boolean);
}
function roleFrom(s){
  let m=s.match(/^([A-ZÅÄÖ][A-Za-zÅÄÖåäö0-9 &\/-]{1,45}?)\s+(?:ska|skall|bör|kan|måste|ansvarar|kontrollerar|registrerar|skickar|tar emot|godkänner|bedömer|kontaktar|hanterar|utför|skapar|väljer|granskar|signerar|arkiverar|rapporterar|informerar|planerar|bokar|levererar|behandlar|sorterar|transporterar)\b/i);
  if(m)return clean(m[1]);
  const low=s.toLocaleLowerCase('sv-SE');for(const r of ROLE_WORDS){if(new RegExp('(?:^|\\b)'+r+'(?:n|en|et|arna|erna)?\\b','i').test(low))return r.charAt(0).toUpperCase()+r.slice(1)}
  m=s.match(/(?:ansvarig(?: roll)?|utförs av|hanteras av)\s*[:\-]?\s*([A-ZÅÄÖ][A-Za-zÅÄÖåäö0-9 &\/-]{1,45})/i);return m?clean(m[1]):'';
}
function systemFrom(s){
  const pats=[/(?:i|via|genom)\s+(?:systemet|system|verktyget|verktyg|portalen|plattformen)\s+([A-ZÅÄÖ][A-Za-zÅÄÖåäö0-9 ._\/-]{1,45})/i,/(?:registreras|läggs in|sparas|hanteras)\s+i\s+([A-ZÅÄÖ][A-Za-zÅÄÖåäö0-9._\/-]{2,30})\b/];
  for(const p of pats){const m=s.match(p);if(m)return clean(m[1].replace(/[.,;:].*$/,''));}return '';
}
function ioFrom(s){const input=[],output=[];let m;
  m=s.match(/(?:tar emot|mottar|får in|inkommer med)\s+(?:en|ett|de|den|det)?\s*([^,.;]{3,70})/i);if(m)input.push(clean(m[1]));
  m=s.match(/(?:skickar|skapar|upprättar|genererar|lämnar|levererar|registrerar)\s+(?:en|ett|de|den|det)?\s*([^,.;]{3,70})/i);if(m)output.push(clean(m[1]));
  return {inputs:unique(input).slice(0,3),outputs:unique(output).slice(0,3)};
}
function typeFrom(s){const t=clean(s);if(/\?$/.test(t)||/^(?:om|ifall|huruvida)\b/i.test(t)||/\b(?:är|finns|har|kan|ska)\b.{0,80}\?/i.test(t))return'decision';if(/^(?:start|börjar|processen startar)\b/i.test(t))return'start';if(/^(?:slut|avslut|processen avslutas)\b/i.test(t))return'end';return'process';}
function actionCandidate(s){return /\b(?:ska|skall|måste|bör|kontroller|registr|skick|ta emot|tar emot|mottag|godkänn|bedöm|kontakt|hanter|utför|lägg|skapa|väljer|beslut|gransk|signer|arkiver|rapport|inform|planer|bok|leverer|behandl|sorter|transport|beställ|betala|verifier|stäm av|stämmer av|följer upp|kompletter)\w*/i.test(s)||/\?$/.test(s);}
function confidenceFor(rec,s){let score=0.52;if(rec.type==='decision')score+=.14;if(rec.responsibleRole)score+=.12;if(rec.system)score+=.09;if(rec.inputs.length||rec.outputs.length)score+=.07;if(actionCandidate(s))score+=.08;return Math.max(.45,Math.min(.95,score));}
function interpretationLabel(c){return c>=.82?'Tydligt i texten':c>=.68?'Trolig tolkning':'Behöver kontroll';}
function recordFrom(text,type,evidence,extra={}){const s=clean(text).replace(/[.]$/,'');const io=ioFrom(s);const rec={text:s,type:type||typeFrom(s),responsibleRole:roleFrom(s),system:systemFrom(s),inputs:io.inputs,outputs:io.outputs,evidence:clean(evidence||s),confidence:0,review:false,...extra};rec.confidence=confidenceFor(rec,s);rec.review=Boolean(extra.review)||rec.confidence<.68||rec.type==='decision';rec.confidenceLabel=interpretationLabel(rec.confidence);return rec;}
function interpret(text,limit=80){const out=[],skip=/^(?:sida \d+|page \d+|innehåll|contents|www\.|https?:|©)/i;
  for(const s0 of sentencePool(text)){let s=clean(s0).replace(/[;:]$/,'');if(s.length<4||s.length>190||skip.test(s))continue;if(!actionCandidate(s))continue;
    const rec=recordFrom(s,typeFrom(s),s);if(!out.some(v=>v.text.toLocaleLowerCase('sv-SE')===rec.text.toLocaleLowerCase('sv-SE')))out.push(rec);if(out.length>=limit)break;
  }
  if(out.length<2){for(const s0 of sentencePool(text)){const s=clean(s0);if(s.length>=4&&s.length<=150&&!skip.test(s)&&!out.some(v=>v.text===s)){out.push(recordFrom(s,typeFrom(s),s,{review:true}));}if(out.length>=Math.min(limit,40))break;}}
  return out;
}
function summary(items){items=Array.isArray(items)?items:[];return {steps:items.length,decisions:items.filter(x=>x.type==='decision').length,roles:unique(items.map(x=>x.responsibleRole)).length,systems:unique(items.map(x=>x.system)).length,needsReview:items.filter(x=>x.review).length};}
function capFirst(s){s=clean(s);return s?s.charAt(0).toLocaleUpperCase('sv-SE')+s.slice(1):s;}
function conditionText(s){const t=capFirst(clean(s).replace(/^(?:att|så att)\s+/i,'').replace(/[?.!,;:]+$/,''));return t+(t?'?':'');}
function branchAction(s){return capFirst(clean(s).replace(/^(?:så|då|ska|skall)\s+/i,'').replace(/[.;]+$/,''));}
function conditionalFromSentence(s){
  const t=clean(s).replace(/[.]$/,'');let m=t.match(/^(?:om|ifall)\s+(.+?)(?:,\s*|\s+så\s+)(.+?)(?:,\s*|;\s*|\s+)(?:annars|i annat fall)\s+(.+)$/i);
  if(m)return{condition:conditionText(m[1]),yes:branchAction(m[2]),no:branchAction(m[3]),evidence:t};
  m=t.match(/^(.+?\?)\s*(?:ja\s*[:\-]\s*)(.+?)(?:[,;]\s*|\s+)(?:nej\s*[:\-]\s*)(.+)$/i);
  if(m)return{condition:conditionText(m[1]),yes:branchAction(m[2]),no:branchAction(m[3]),evidence:t};
  return null;
}
function conditionalWithNext(pool,i){const t=clean(pool[i]||'').replace(/[.]$/,'');const next=clean(pool[i+1]||'').replace(/[.]$/,'');if(!/^(?:annars|i annat fall)\b/i.test(next))return null;const m=t.match(/^(?:om|ifall)\s+(.+?)(?:,\s*|\s+så\s+)(.+)$/i);if(!m)return null;return{condition:conditionText(m[1]),yes:branchAction(m[2]),no:branchAction(next.replace(/^(?:annars|i annat fall)\s*[:,\-]?\s*/i,'')),evidence:t+' '+next,consumeNext:true};}
function normalizeMatch(s){return clean(s).toLocaleLowerCase('sv-SE').replace(/[^a-zåäö0-9 ]/g,' ').replace(/\b(?:den|det|en|ett|till|steg|process|aktivitet|rollen|roll)\b/g,' ').replace(/\s+/g,' ').trim();}
function feedbackTarget(text){const m=clean(text).match(/(?:gå|går|återgå|återgår|skicka|skickas|returnera|returneras|lämna|lämnas|föras|förs)\b.{0,45}?\btillbaka\s+till\s+([^,.;]{2,70})/i);return m?clean(m[1]):'';}
function subprocessHint(text){return /\b(?:delprocess|se\s+rutin|enligt\s+rutin|se\s+process|enligt\s+process)\b/i.test(clean(text));}
function findLoopTarget(nodes,target,beforeIndex){const norm=normalizeMatch(target);if(!norm)return null;const tokens=norm.split(' ').filter(x=>x.length>3),textHits=[],roleHits=[];for(let i=0;i<beforeIndex;i++){const n=nodes[i],role=normalizeMatch(n.responsibleRole),txt=normalizeMatch(n.text);if(tokens.length&&tokens.every(t=>txt.includes(t)))textHits.push(n.id);if(role&&(role===norm||norm.includes(role)||role.includes(norm)))roleHits.push(n.id);}if(textHits.length===1)return textHits[0];if(!textHits.length&&roleHits.length===1)return roleHits[0];return null;}
function interpretFlow(text,limit=80){
  const pool=sentencePool(text),nodes=[],groups=[],skip=/^(?:sida \d+|page \d+|innehåll|contents|www\.|https?:|©)/i;let idSeq=0,col=0;
  function addNode(rec,column,lane,flowKind){const n={...rec,id:'d'+(++idSeq),flowColumn:column,flowLane:lane||0,flowKind:flowKind||'sequence',subprocessHint:subprocessHint(rec.text)};nodes.push(n);return n;}
  for(let i=0;i<pool.length&&nodes.length<limit;i++){
    const raw=clean(pool[i]);if(raw.length<4||raw.length>240||skip.test(raw))continue;
    let cond=conditionalFromSentence(raw);if(!cond)cond=conditionalWithNext(pool,i);
    if(cond&&cond.yes&&cond.no){const d=addNode(recordFrom(cond.condition,'decision',cond.evidence,{review:true}),col,0,'decision'),yes=addNode(recordFrom(cond.yes,'process',cond.evidence),col+1,-1,'branch-yes'),no=addNode(recordFrom(cond.no,'process',cond.evidence),col+1,1,'branch-no');groups.push({entry:d.id,exits:[yes.id,no.id],decision:d.id,yes:yes.id,no:no.id});col+=2;if(cond.consumeNext)i++;continue;}
    if(!actionCandidate(raw)&&!subprocessHint(raw))continue;
    const rec=recordFrom(raw,typeFrom(raw),raw,{review:subprocessHint(raw)});const n=addNode(rec,col,0,subprocessHint(raw)?'subprocess-hint':'sequence');groups.push({entry:n.id,exits:[n.id]});col++;
  }
  if(nodes.length===0){const fallback=interpret(text,Math.min(limit,40));for(const rec of fallback){const n=addNode(rec,col++,0,'sequence');groups.push({entry:n.id,exits:[n.id]});}}
  const edges=[];for(let g=0;g<groups.length;g++){const group=groups[g];if(group.decision){edges.push({from:group.decision,to:group.yes,label:'Ja',kind:'branch',confidence:.95},{from:group.decision,to:group.no,label:'Nej',kind:'branch',confidence:.95});}
    const next=groups[g+1];if(next){for(const exit of group.exits)edges.push({from:exit,to:next.entry,label:'',kind:'sequence',confidence:.9});}}
  let loops=0;for(let i=0;i<nodes.length;i++){const targetText=feedbackTarget(nodes[i].text);if(!targetText)continue;const target=findLoopTarget(nodes,targetText,i);nodes[i].feedbackTarget=targetText;nodes[i].review=true;nodes[i].confidenceLabel='Behöver kontroll';if(target){for(let e=edges.length-1;e>=0;e--){if(edges[e].from===nodes[i].id&&edges[e].kind==='sequence')edges.splice(e,1);}edges.push({from:nodes[i].id,to:target,label:'Tillbaka',kind:'loop',confidence:.86});nodes[i].feedbackTargetId=target;loops++;}}
  const branches=edges.filter(e=>e.kind==='branch').length;const subProcesses=nodes.filter(n=>n.subprocessHint).length;
  return{items:nodes,edges,summary:{...summary(nodes),branches,loops,subProcesses},hasRealFlow:branches>0||loops>0};
}

function mergeKey(text){return normalizeMatch(text).replace(/\b(?:kundservice|ekonomi|inköp|sälj|försäljning|lager|produktion|transport|chaufför|arbetsledare|teamledare|chef|projektledare|handläggare|administratör|beställare|leverantör|kund|medarbetare|controller|hr|it|support|kvalitet|miljö|drift|planerare)\b/g,' ').replace(/\b(?:i|via|genom|systemet|system|verktyget|verktyg)\b/g,' ').replace(/\s+/g,' ').trim();}
function sameValue(a,b){return normalizeMatch(a)===normalizeMatch(b)}
function interpretDocuments(documents,limit=100){
  const docs=(Array.isArray(documents)?documents:[]).map((d,i)=>({name:clean(d?.name)||`Dokument ${i+1}`,text:String(d?.text||'')})).filter(d=>d.text.trim());
  if(!docs.length)return{items:[],edges:[],conflicts:[],summary:{...summary([]),branches:0,loops:0,subProcesses:0,documents:0,conflicts:0},hasRealFlow:false};
  const merged=[],byKey=new Map(),maps=[],conflicts=[],conflictByKey=new Map();let idSeq=0,conflictSeq=0;
  function addConflict(item,type,message,sources,options=[],extra={}){
    if(item){if(!item.conflictMessages)item.conflictMessages=[];if(!item.conflictMessages.includes(message))item.conflictMessages.push(message);item.review=true;item.confidenceLabel='Behöver kontroll';}
    const itemId=item?.id||String(extra.itemId||''),key=`${type}|${itemId}|${String(extra.pairKey||'')}`;let c=conflictByKey.get(key);
    if(!c){c={id:'c'+(++conflictSeq),type,itemId,itemIds:extra.itemIds||[itemId].filter(Boolean),message,sources:unique(sources||[]),options:[]};conflicts.push(c);conflictByKey.set(key,c)}
    c.sources=unique([...(c.sources||[]),...(sources||[])]);c.options=unique([...(c.options||[]),...options].map(x=>typeof x==='string'?x:String(x||''))).filter(Boolean);if(extra.pairKey)c.pairKey=extra.pairKey;if(extra.directions)c.directions=extra.directions;return c;
  }
  for(const doc of docs){const plan=interpretFlow(doc.text,Math.min(80,limit)),idMap=new Map();
    for(const rec0 of plan.items){const rec={...rec0},key=mergeKey(rec.text)||normalizeMatch(rec.text);let target=byKey.get(key);
      if(!target){target={...rec,id:'m'+(++idSeq),sourceNames:[doc.name],sourceEvidence:{[doc.name]:rec.evidence},flowColumn:merged.length,flowLane:rec.flowLane||0,conflictMessages:[]};merged.push(target);byKey.set(key,target)}
      else{
        target.sourceNames=unique([...(target.sourceNames||[]),doc.name]);target.sourceEvidence={...(target.sourceEvidence||{}),[doc.name]:rec.evidence};target.inputs=unique([...(target.inputs||[]),...(rec.inputs||[])]).slice(0,5);target.outputs=unique([...(target.outputs||[]),...(rec.outputs||[])]).slice(0,5);
        if(!target.responsibleRole&&rec.responsibleRole)target.responsibleRole=rec.responsibleRole;else if(target.responsibleRole&&rec.responsibleRole&&!sameValue(target.responsibleRole,rec.responsibleRole))addConflict(target,'responsibility',`Olika ansvar: ${target.responsibleRole} / ${rec.responsibleRole}`,target.sourceNames,[target.responsibleRole,rec.responsibleRole]);
        if(!target.system&&rec.system)target.system=rec.system;else if(target.system&&rec.system&&!sameValue(target.system,rec.system))addConflict(target,'system',`Olika system: ${target.system} / ${rec.system}`,target.sourceNames,[target.system,rec.system]);
        if(target.type!==rec.type)addConflict(target,'type',`Olika tolkning av stegtyp: ${target.type==='decision'?'beslut':'aktivitet'} / ${rec.type==='decision'?'beslut':'aktivitet'}`,target.sourceNames,[target.type,rec.type]);
      }
      idMap.set(rec.id,target.id);if(merged.length>=limit)break;
    }
    maps.push({doc,plan,idMap});if(merged.length>=limit)break;
  }
  const rawEdges=[];
  for(const entry of maps){for(const e of entry.plan.edges||[]){const from=entry.idMap.get(e.from),to=entry.idMap.get(e.to);if(!from||!to||from===to)continue;rawEdges.push({...e,from,to,sources:[entry.doc.name]})}}
  const edgeMap=new Map();for(const e of rawEdges){const k=`${e.from}>${e.to}|${e.label||''}|${e.kind||''}`;const old=edgeMap.get(k);if(old)old.sources=unique([...(old.sources||[]),...(e.sources||[])]);else edgeMap.set(k,{...e})}
  const edges=[...edgeMap.values()];
  const seqPairs=new Map();for(const e of edges.filter(x=>x.kind==='sequence'))seqPairs.set(`${e.from}>${e.to}`,e);
  const marked=new Set();for(const e of edges.filter(x=>x.kind==='sequence')){const rev=seqPairs.get(`${e.to}>${e.from}`);if(!rev)continue;const pair=[e.from,e.to].sort().join('|');if(marked.has(pair))continue;marked.add(pair);e.conflict=true;rev.conflict=true;const a=merged.find(x=>x.id===e.from),b=merged.find(x=>x.id===e.to);const msg=`Olika ordning mellan “${a?.text||'steg'}” och “${b?.text||'steg'}”`;if(a){if(!a.conflictMessages.includes(msg))a.conflictMessages.push(msg);a.review=true;a.confidenceLabel='Behöver kontroll'}if(b){if(!b.conflictMessages.includes(msg))b.conflictMessages.push(msg);b.review=true;b.confidenceLabel='Behöver kontroll'}addConflict(null,'order',msg,[...(e.sources||[]),...(rev.sources||[])],[],{itemId:a?.id||'',itemIds:[a?.id,b?.id].filter(Boolean),pairKey:pair,directions:[{from:e.from,to:e.to,label:`${a?.text||'Steg'} → ${b?.text||'Steg'}`},{from:rev.from,to:rev.to,label:`${b?.text||'Steg'} → ${a?.text||'Steg'}`}]});}
  const branches=edges.filter(e=>e.kind==='branch'&&!e.conflict).length,loops=edges.filter(e=>e.kind==='loop'&&!e.conflict).length,subProcesses=merged.filter(n=>n.subprocessHint).length;
  return{items:merged,edges,conflicts,summary:{...summary(merged),branches,loops,subProcesses,documents:docs.length,conflicts:conflicts.length},hasRealFlow:edges.some(e=>!e.conflict&&(e.kind==='branch'||e.kind==='loop')),documents:docs.map(d=>d.name)};
}

global.MapliniDocumentInterpretationCore={interpret,interpretFlow,interpretDocuments,summary,roleFrom,systemFrom,ioFrom,typeFrom,interpretationLabel,conditionalFromSentence,feedbackTarget,subprocessHint};
})(typeof window!=='undefined'?window:globalThis);
