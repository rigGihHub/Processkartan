(function(global){
'use strict';

function toBytes(value){
  if(value instanceof Uint8Array)return value;
  if(Array.isArray(value))return Uint8Array.from(value);
  if(value&&value.buffer instanceof ArrayBuffer)return new Uint8Array(value.buffer,value.byteOffset||0,value.byteLength||value.length||0);
  return new Uint8Array(0);
}
function validateBytes(value,kind){
  const b=toBytes(value);
  if(b.length<4)return {ok:false,reason:'too-small',size:b.length};
  if(kind==='pdf'){
    const ok=b[0]===0x25&&b[1]===0x50&&b[2]===0x44&&b[3]===0x46;
    return {ok,reason:ok?'':'bad-pdf-signature',size:b.length};
  }
  if(kind==='zip'){
    const ok=b[0]===0x50&&b[1]===0x4b&&(
      (b[2]===0x03&&b[3]===0x04)||
      (b[2]===0x05&&b[3]===0x06)||
      (b[2]===0x07&&b[3]===0x08)
    );
    return {ok,reason:ok?'':'bad-zip-signature',size:b.length};
  }
  return {ok:true,reason:'',size:b.length};
}
function safeFileName(name){
  let s=String(name||'Maplini_export').replace(/[\\/:*?"<>|\u0000-\u001f]+/g,'_').replace(/\s+/g,' ').trim();
  if(!s)s='Maplini_export';
  if(s.length>180){
    const dot=s.lastIndexOf('.');
    const ext=(dot>0&&s.length-dot<=12)?s.slice(dot):'';
    s=s.slice(0,180-ext.length)+ext;
  }
  return s;
}
function deletionPlan(store,deleteId){
  const ids=Object.keys((store&&store.processes)||{}).filter(id=>id!==deleteId);
  return {remainingIds:ids,nextId:ids[0]||null,deletingCurrent:!!(store&&store.currentId===deleteId)};
}
global.MapliniExportCore={validateBytes,safeFileName,deletionPlan};
})(typeof window!=='undefined'?window:globalThis);
