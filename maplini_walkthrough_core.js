(function(global){
'use strict';

function safeString(v,maxLen){return String(v==null?'':v).trim().slice(0,maxLen);}
function normalizeQuestion(q,index){
  q=(q&&typeof q==='object')?q:{text:q};
  const text=safeString(q.text,1200);
  if(!text)return null;
  const rawId=safeString(q.id,120)||('q-'+(index+1));
  const kind=q.kind==='route'||Boolean(q.route)?'route':'control';
  return {id:rawId,text,required:q.required!==false,kind,route:kind==='route'};
}
function normalizeQuestions(value){
  const list=Array.isArray(value)?value:[];
  const out=[],used=new Set();
  for(let i=0;i<list.length&&out.length<30;i++){
    const q=normalizeQuestion(list[i],i);if(!q)continue;
    let id=q.id,n=2;while(used.has(id))id=q.id+'-'+(n++);
    used.add(id);out.push(Object.assign({},q,{id}));
  }
  return out;
}
function graph(nodes,links){
  const ns=Array.isArray(nodes)?nodes:[],ids=new Set(ns.map(n=>String(n.id)));
  const incoming=new Map(),outgoing=new Map();
  ns.forEach(n=>{incoming.set(String(n.id),[]);outgoing.set(String(n.id),[])});
  for(let i=0;i<(Array.isArray(links)?links:[]).length;i++){
    const l=links[i];if(!Array.isArray(l)||!ids.has(String(l[0]))||!ids.has(String(l[1])))continue;
    const style=l[3]&&typeof l[3]==='object'?l[3]:{};
    const e={index:i,from:String(l[0]),to:String(l[1]),label:safeString(style.label,500)};
    outgoing.get(e.from).push(e);incoming.get(e.to).push(e);
  }
  return {incoming,outgoing};
}
function startNodeIds(nodes,links){
  const ns=Array.isArray(nodes)?nodes:[],g=graph(ns,links);
  const explicit=ns.filter(n=>String(n.type)==='start').map(n=>String(n.id));
  if(explicit.length)return explicit;
  const roots=ns.filter(n=>(g.incoming.get(String(n.id))||[]).length===0).map(n=>String(n.id));
  return roots.length?roots:(ns[0]?[String(ns[0].id)]:[]);
}
function nextEdges(nodeId,nodes,links){
  return graph(nodes,links).outgoing.get(String(nodeId))||[];
}

function normalizedBranchLabel(value){
  const text=safeString(value,500).toLocaleLowerCase('sv-SE').replace(/[.!?:;]+$/g,'').trim();
  if(['ja','yes','y','true','godkänd','godkand','ok'].includes(text))return 'yes';
  if(['nej','no','n','false','avslag','avslagen','inte godkänd','inte godkand'].includes(text))return 'no';
  return '';
}
function routeQuestion(questions){
  const qs=normalizeQuestions(questions);
  return qs.find(q=>q.route)||null;
}
function routeEdges(edges){
  const list=Array.isArray(edges)?edges:[];
  const yes=list.filter(e=>normalizedBranchLabel(e&&e.label)==='yes');
  const no=list.filter(e=>normalizedBranchLabel(e&&e.label)==='no');
  return {yes:yes.length===1?yes[0]:null,no:no.length===1?no[0]:null,ambiguous:yes.length>1||no.length>1};
}
function automaticRoute(questions,answers,edges){
  const q=routeQuestion(questions);
  if(!q)return {mode:'manual',reason:'no-route-question',question:null,edge:null};
  const answer=answers&&typeof answers==='object'?answers[q.id]:null;
  if(answer!=='yes'&&answer!=='no')return {mode:'pending',reason:'route-question-unanswered',question:q,edge:null};
  const mapped=routeEdges(edges);
  if(mapped.ambiguous)return {mode:'manual',reason:'ambiguous-labels',question:q,edge:null};
  const edge=answer==='yes'?mapped.yes:mapped.no;
  if(!edge)return {mode:'manual',reason:answer==='yes'?'missing-yes-edge':'missing-no-edge',question:q,edge:null};
  return {mode:'auto',reason:'matched',question:q,answer,edge};
}

function answerIsDeviation(question,answer){
  const q=question&&typeof question==='object'?question:{};
  const kind=q.kind==='route'||q.route===true?'route':'control';
  return kind==='control'&&answer==='no';
}
function currentDeviationCount(questions,answers){
  const qs=normalizeQuestions(questions),map=answers&&typeof answers==='object'?answers:{};
  return qs.reduce((sum,q)=>sum+(answerIsDeviation(q,map[q.id])?1:0),0);
}
function summarize(history){
  const rows=Array.isArray(history)?history:[];
  let yes=0,no=0,answered=0,routeYes=0,routeNo=0,controlYes=0,controlNo=0;
  const deviations=[];
  for(const row of rows){
    const answers=Array.isArray(row.answers)?row.answers:[];
    for(const a of answers){
      const kind=a.kind==='route'||a.route===true?'route':'control';
      if(a.answer==='yes'){yes++;answered++;if(kind==='route')routeYes++;else controlYes++}
      if(a.answer==='no'){
        no++;answered++;if(kind==='route')routeNo++;else controlNo++;
        if(answerIsDeviation({kind,route:a.route},a.answer))deviations.push({
          questionId:safeString(a.id,120),nodeId:row.nodeId,nodeText:row.nodeText||'',question:a.question||'',answer:'no',
          explanation:safeString(a.explanation,4000),owner:safeString(a.owner,300),dueDate:safeString(a.dueDate,40),
          status:a.status==='resolved'?'resolved':'open',statusUpdatedAt:Number(a.statusUpdatedAt)||null
        });
      }
    }
  }
  return {steps:rows.length,answered,yes,no,routeYes,routeNo,controlYes,controlNo,deviations,passed:deviations.length===0};
}
global.MapliniWalkthroughCore={normalizeQuestion,normalizeQuestions,graph,startNodeIds,nextEdges,normalizedBranchLabel,routeQuestion,routeEdges,automaticRoute,answerIsDeviation,currentDeviationCount,summarize};
})(typeof window!=='undefined'?window:globalThis);
