(function(global){
'use strict';
function clone(v){try{return JSON.parse(JSON.stringify(v));}catch(e){return null;}}
function finiteNumber(v,fallback,min,max){const n=Number(v);return Number.isFinite(n)?Math.min(max,Math.max(min,n)):fallback;}
function safeString(v,fallback,maxLen){const s=typeof v==='string'?v:fallback;return s.slice(0,maxLen);}
function normalizeNode(n,index){
  n=(n&&typeof n==='object')?clone(n):{};
  const allowed=new Set(['start','process','decision','end','subprocess','group','note','document']);
  const type=allowed.has(n.type)?n.type:'process';
  const id=safeString(n.id||('node-'+(index+1)),'node-'+(index+1),120);
  return Object.assign({},n,{id,type,text:safeString(n.text||n.label||'','',5000),
    x:finiteNumber(n.x,80,0,20000),y:finiteNumber(n.y,80,0,20000),
    w:finiteNumber(n.w||n.width,180,60,4000),h:finiteNumber(n.h||n.height,80,36,4000),
    documentUrl:safeString(n.documentUrl||'','',4000),
    nodeStyle:['standard','3d','raised','glass','flat'].includes(n.nodeStyle)?n.nodeStyle:'standard'});
}
function normalizeLink(l){
  if(Array.isArray(l)){
    const sourceId=safeString(l[0]||'','',120),targetId=safeString(l[1]||'','',120);
    const side=safeString(l[2]||'right','right',20);
    const style=(l[3]&&typeof l[3]==='object')?clone(l[3]):{};
    return [sourceId,targetId,side,style];
  }
  l=(l&&typeof l==='object')?clone(l):{};
  return [safeString(l.sourceId||l.source||'','',120),
    safeString(l.targetId||l.target||'','',120),
    safeString(l.side||'right','right',20),
    (l.style&&typeof l.style==='object')?clone(l.style):{}];
}
function normalizeProcess(p,fallbackId){
  p=(p&&typeof p==='object')?clone(p):{};
  const id=safeString(p.id||fallbackId||'proc-1','proc-1',160);
  const nodes=Array.isArray(p.nodes)?p.nodes.map(normalizeNode):[];
  const nodeIds=new Set(nodes.map(n=>n.id));
  const links=(Array.isArray(p.links)?p.links:[]).map(normalizeLink)
    .filter(l=>l&&l[0]&&l[1]&&nodeIds.has(l[0])&&nodeIds.has(l[1]));
  return Object.assign({},p,{id,name:safeString(p.name||'Namnlös process','Namnlös process',300),nodes,links,
    connectorPointSize:finiteNumber(p.connectorPointSize,8,2,40),
    connectorPointColor:safeString(p.connectorPointColor||'#1f6f55','#1f6f55',32),
    connectorPointsHidden:Boolean(p.connectorPointsHidden),
    processBackground:safeString(p.processBackground||'#ffffff','#ffffff',32),
    processBackgroundType:safeString(p.processBackgroundType||'solid','solid',40),
    processPatternColor:safeString(p.processPatternColor||'#d7e1e8','#d7e1e8',32),
    processPatternDensity:finiteNumber(p.processPatternDensity,20,4,100),
    processGradientStart:safeString(p.processGradientStart||'#ffffff','#ffffff',32),
    processGradientEnd:safeString(p.processGradientEnd||'#e7f1ff','#e7f1ff',32),
    processGradientAngle:finiteNumber(p.processGradientAngle,45,0,360),
    processBackgroundImageData:typeof p.processBackgroundImageData==='string'?p.processBackgroundImageData:'',
    processBackgroundImageOpacity:finiteNumber(p.processBackgroundImageOpacity,.25,.05,1),
    processWatermarkText:safeString(p.processWatermarkText||'UTKAST','UTKAST',80),
    processWatermarkOpacity:finiteNumber(p.processWatermarkOpacity,.15,.05,.4),
    processWatermarkUseLogo:Boolean(p.processWatermarkUseLogo),
    processLogoData:typeof p.processLogoData==='string'?p.processLogoData:'',
    processLogoHidden:Boolean(p.processLogoHidden),
    processLogoWidth:finiteNumber(p.processLogoWidth,180,40,1200),
    processLogoX:finiteNumber(p.processLogoX,28,0,20000),
    processLogoY:finiteNumber(p.processLogoY,28,0,20000)});
}
function normalizeStore(store){
  store=(store&&typeof store==='object')?store:{};
  const raw=(store.processes&&typeof store.processes==='object'&&!Array.isArray(store.processes))?store.processes:{};
  const processes={};
  for(const [key,value] of Object.entries(raw)){const p=normalizeProcess(value,key);processes[p.id]=p;}
  const ids=Object.keys(processes);
  const requested=typeof store.currentId==='string'?store.currentId:'';
  return {schemaVersion:1,currentId:(requested&&processes[requested])?requested:(ids[0]||''),processes};
}
global.MapliniStateCore={clone,normalizeNode,normalizeLink,normalizeProcess,normalizeStore};
})(typeof window!=='undefined'?window:globalThis);
