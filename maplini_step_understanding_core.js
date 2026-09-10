/* v0.20.60: compact, deterministic step understanding */
(function(global){
'use strict';
function clean(v,max=500){return String(v==null?'':v).replace(/\s+/g,' ').trim().slice(0,max)}
function unique(values){const out=[];for(const raw of (Array.isArray(values)?values:[])){const v=clean(raw,240);if(v&&!out.some(x=>x.toLocaleLowerCase('sv-SE')===v.toLocaleLowerCase('sv-SE')))out.push(v)}return out}
function nextText(type,next){
  const rows=(Array.isArray(next)?next:[]).map(x=>({title:clean(x?.title||x,180),label:clean(x?.label,80)})).filter(x=>x.title);
  if(!rows.length)return String(type||'')==='end'?'Processen slutar här':'Inget nästa steg är kopplat';
  if(rows.length===1)return rows[0].label?`${rows[0].label}: ${rows[0].title}`:rows[0].title;
  const labelled=rows.map(x=>x.label?`${x.label}: ${x.title}`:x.title);
  return `${rows.length} möjliga vägar · ${labelled.join(' · ')}`.slice(0,600);
}
function summarize(data){
  data=(data&&typeof data==='object')?data:{};
  const title=clean(data.title,300),description=clean(data.description,1200),role=clean(data.responsibleRole,300),inputs=unique(data.inputs),outputs=unique(data.outputs);
  const values={
    what:description||title||'Inte beskrivet ännu',
    who:role||'Inte angivet ännu',
    input:inputs.length?inputs.join(' · '):'Ingen input angiven',
    output:outputs.length?outputs.join(' · '):'Ingen output angiven',
    next:nextText(data.type,data.next)
  };
  const rows=[
    {key:'what',label:'Vad?',value:values.what,missing:!description&&!title},
    {key:'who',label:'Vem?',value:values.who,missing:!role},
    {key:'input',label:'Input',value:values.input,missing:!inputs.length},
    {key:'output',label:'Output',value:values.output,missing:!outputs.length},
    {key:'next',label:'Sedan',value:values.next,missing:!Array.isArray(data.next)||!data.next.length}
  ];
  return {rows,values,complete:rows.filter(r=>!r.missing).length,total:rows.length};
}
global.MapliniStepUnderstandingCore={clean,unique,nextText,summarize};
})(typeof window!=='undefined'?window:globalThis);
