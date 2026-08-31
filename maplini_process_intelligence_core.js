(function(global){
'use strict';

function normNodes(nodes){
  return (Array.isArray(nodes)?nodes:[]).filter(n=>n&&n.id!=null).map(n=>({
    id:String(n.id),type:String(n.type||'process'),text:String(n.text||'').trim()
  }));
}
function normLinks(links,ids){
  const out=[];
  for(let i=0;i<(Array.isArray(links)?links:[]).length;i++){
    const l=links[i];if(!Array.isArray(l)||l.length<2)continue;
    const from=String(l[0]),to=String(l[1]);if(!ids.has(from)||!ids.has(to))continue;
    const style=l[3]&&typeof l[3]==='object'?l[3]:{};
    out.push({from,to,index:i,label:String(style.label||'').trim()});
  }
  return out;
}
function severityRank(s){return s==='error'?0:s==='warning'?1:2}
const ACTIONS={
  missing_start:'Lägg till en Start-ruta och koppla den till processens första verkliga steg.',
  multiple_starts:'Kontrollera om processen verkligen har flera startvägar. Slå annars ihop dem till en tydlig Start.',
  missing_end:'Lägg till en Slut-ruta och koppla processens sista väg till den.',
  isolated:'Koppla rutan till rätt steg före och efter. Ta bort den om den inte hör till processen.',
  no_incoming:'Koppla ett föregående steg till rutan, eller gör den till en Start om den faktiskt börjar processen.',
  dead_end:'Koppla steget vidare till nästa steg eller ändra det till Slut om processen ska avslutas här.',
  decision_branches:'Lägg till minst två tydliga utgående vägar från beslutet, till exempel Ja och Nej.',
  merge_bottleneck:'Kontrollera om alla inkommande vägar behöver mötas här och om ansvar eller väntetid behöver tydliggöras.',
  fanout:'Kontrollera att varje utgående gren behövs och märk gärna alternativen så att vägvalet blir tydligt.',
  loop:'Kontrollera att återkopplingen är avsiktlig och ange vad som gör att processen lämnar loopen.',
  long_chain:'Se om flera steg kan slås ihop, grupperas eller beskrivas enklare utan att tappa viktig information.',
  direct_activity:'Kontrollera vad den första aktiviteten producerar. Lägg in resultatet som ett Objekt mellan aktiviteterna om det är det som triggar nästa steg.'
};
function priorityLabel(severity){return severity==='error'?'Åtgärda först':severity==='warning'?'Kontrollera':'Förbättring';}
function finding(code,severity,title,detail,nodeIds=[],meta={}){
  return {code,severity,title,detail,action:ACTIONS[code]||'Kontrollera om flödet kan göras tydligare.',priority:priorityLabel(severity),nodeIds:[...new Set(nodeIds.map(String))],meta};
}
function stronglyConnected(ids,outEdges){
  let index=0;const stack=[],onStack=new Set(),idx=new Map(),low=new Map(),components=[];
  function visit(v){
    idx.set(v,index);low.set(v,index);index++;stack.push(v);onStack.add(v);
    for(const w of outEdges.get(v)||[]){
      if(!idx.has(w)){visit(w);low.set(v,Math.min(low.get(v),low.get(w)))}
      else if(onStack.has(w))low.set(v,Math.min(low.get(v),idx.get(w)));
    }
    if(low.get(v)===idx.get(v)){
      const c=[];let w;do{w=stack.pop();onStack.delete(w);c.push(w)}while(w!==v);components.push(c);
    }
  }
  for(const id of ids)if(!idx.has(id))visit(id);
  return components;
}
function longChains(activeIds,inMap,outMap,byId,minLength){
  const seen=new Set(),chains=[];
  for(const id of activeIds){
    if(seen.has(id))continue;
    const incoming=inMap.get(id)||[],outgoing=outMap.get(id)||[];
    const predecessor=incoming.length===1?incoming[0]:null;
    const startsChain=incoming.length!==1 || (predecessor && (outMap.get(predecessor)||[]).length!==1);
    if(!startsChain||outgoing.length!==1)continue;
    const chain=[id];let cur=id;
    while((outMap.get(cur)||[]).length===1){
      const next=(outMap.get(cur)||[])[0];
      if(chain.includes(next)||(inMap.get(next)||[]).length!==1)break;
      chain.push(next);cur=next;
      if((outMap.get(cur)||[]).length!==1)break;
    }
    chain.forEach(x=>seen.add(x));
    const meaningful=chain.filter(x=>!['start','end'].includes((byId.get(x)||{}).type));
    if(meaningful.length>=minLength)chains.push(chain);
  }
  return chains;
}
function analyze(nodes,links,options={}){
  const N=normNodes(nodes),byId=new Map(N.map(n=>[n.id,n])),ids=new Set(byId.keys()),L=normLinks(links,ids);
  const ignoredTypes=new Set(['note','group']),active=N.filter(n=>!ignoredTypes.has(n.type)),activeIds=new Set(active.map(n=>n.id));
  const inMap=new Map(active.map(n=>[n.id,[]])),outMap=new Map(active.map(n=>[n.id,[]]));
  for(const l of L){if(!activeIds.has(l.from)||!activeIds.has(l.to))continue;outMap.get(l.from).push(l.to);inMap.get(l.to).push(l.from)}
  const findings=[];
  const starts=active.filter(n=>n.type==='start'),ends=active.filter(n=>n.type==='end');
  if(!starts.length)findings.push(finding('missing_start','error','Processen saknar Start','Lägg till minst en tydlig startpunkt.'));
  else if(starts.length>1)findings.push(finding('multiple_starts','warning',`${starts.length} startpunkter`,'Kontrollera att flera startpunkter är avsiktliga.',starts.map(n=>n.id)));
  if(!ends.length)findings.push(finding('missing_end','error','Processen saknar Slut','Lägg till minst en tydlig slutpunkt.'));

  for(const l of L){
    const from=byId.get(l.from),to=byId.get(l.to);
    if(from&&to&&from.type==='process'&&to.type==='process'){
      findings.push(finding(
        'direct_activity','warning',
        `Aktiviteter kopplade direkt: ${from.text||'Aktivitet'} → ${to.text||'Aktivitet'}`,
        'Direktkopplade aktiviteter kan dölja vilket resultat eller behov som faktiskt gör att nästa aktivitet kan börja.',
        [from.id,to.id],{linkIndex:l.index}
      ));
    }
  }

  for(const n of active){
    const inc=inMap.get(n.id)||[],out=outMap.get(n.id)||[];
    if(n.type!=='start'&&n.type!=='end'&&inc.length===0&&out.length===0){
      findings.push(finding('isolated','error',`Isolerad ruta: ${n.text||'Namnlös ruta'}`,'Rutan är inte ansluten till resten av processen.',[n.id]));continue;
    }
    if(n.type!=='start'&&inc.length===0)findings.push(finding('no_incoming','warning',`Saknar inkommande flöde: ${n.text||'Namnlös ruta'}`,'Kontrollera var detta steg ska börja från.',[n.id]));
    if(n.type!=='end'&&out.length===0)findings.push(finding('dead_end','error',`Död ände: ${n.text||'Namnlös ruta'}`,'Steget saknar utgående flöde och är inte markerat som Slut.',[n.id]));
    if(n.type==='decision'&&out.length<2)findings.push(finding('decision_branches','error',`Beslut saknar gren: ${n.text||'Beslut'}`,'Ett beslut bör normalt ha minst två utgående alternativ.',[n.id]));
    if(inc.length>=3)findings.push(finding('merge_bottleneck','info',`Många flöden möts: ${n.text||'Namnlös ruta'}`,`${inc.length} inkommande flöden. Kontrollera om steget riskerar att bli en flaskhals.`,[n.id],{count:inc.length}));
    if(out.length>=3)findings.push(finding('fanout','info',`Många grenar: ${n.text||'Namnlös ruta'}`,`${out.length} utgående flöden. Kontrollera att grenarna är tydliga och nödvändiga.`,[n.id],{count:out.length}));
  }

  const outEdges=new Map([...activeIds].map(id=>[id,(outMap.get(id)||[]).filter(x=>activeIds.has(x))]));
  const comps=stronglyConnected([...activeIds],outEdges);
  for(const comp of comps){
    const selfLoop=comp.length===1&&L.some(l=>l.from===comp[0]&&l.to===comp[0]);
    if(comp.length>1||selfLoop){
      findings.push(finding('loop','info',`Återkoppling/loop med ${comp.length} steg`,'Kontrollera att loopen är avsiktlig och att det finns ett tydligt villkor för att lämna den.',comp));
    }
  }

  const minChain=Math.max(4,Number(options.longChainThreshold)||5);
  for(const chain of longChains(activeIds,inMap,outMap,byId,minChain)){
    const names=chain.map(id=>(byId.get(id)||{}).text).filter(Boolean);
    findings.push(finding('long_chain','info',`Lång sekvens: ${chain.length} steg`,names.length?`Sekvensen går genom ${names.slice(0,3).join(' → ')}${names.length>3?' …':''}. Kontrollera om något kan förenklas eller grupperas.`:'Kontrollera om sekvensen kan förenklas eller grupperas.',chain));
  }

  findings.sort((a,b)=>severityRank(a.severity)-severityRank(b.severity)||a.title.localeCompare(b.title,'sv'));
  const weights={error:1.8,warning:.8,info:.25};
  const penalty=findings.reduce((s,f)=>s+(weights[f.severity]||0),0);
  const divisor=Math.max(3,active.length);
  const score=Math.max(1.5,Math.min(10,10-(penalty/divisor)*2.5));
  const counts={error:0,warning:0,info:0};findings.forEach(f=>counts[f.severity]++);
  return {score:Math.round(score*10)/10,counts,findings,nodeCount:active.length,linkCount:L.filter(l=>activeIds.has(l.from)&&activeIds.has(l.to)).length};
}

global.MapliniProcessIntelligenceCore={analyze};
})(typeof window!=='undefined'?window:globalThis);
