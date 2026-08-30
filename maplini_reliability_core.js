(function(global){
'use strict';
function nowIso(){try{return new Date().toISOString()}catch(e){return ''}}
function errorInfo(error,context){let message='Unknown error',name='Error',stack='';if(error&&typeof error==='object'){message=String(error.message||error.reason||error.toString?.()||message).slice(0,800);name=String(error.name||name).slice(0,120);stack=String(error.stack||'').slice(0,4000)}else if(error!==undefined&&error!==null){message=String(error).slice(0,800)}return {context:String(context||'runtime').slice(0,120),name,message,stack,at:nowIso()}}
function parseJsonSafe(raw){if(typeof raw!=='string'||!raw.trim())return null;try{return JSON.parse(raw)}catch(e){return null}}
function isUsableProcess(p){return !!(p&&typeof p==='object'&&typeof p.id==='string'&&p.id&&Array.isArray(p.nodes)&&Array.isArray(p.links))}
function makeEmergencySnapshot(store){store=(store&&typeof store==='object')?store:{};const processes=(store.processes&&typeof store.processes==='object'&&!Array.isArray(store.processes))?store.processes:{};return {schemaVersion:1,emergency:true,capturedAt:nowIso(),currentId:typeof store.currentId==='string'?store.currentId:'',processes}}
function validateStoreShape(store){if(!store||typeof store!=='object')return {ok:false,reason:'not-object'};if(!store.processes||typeof store.processes!=='object'||Array.isArray(store.processes))return {ok:false,reason:'processes'};return {ok:true,reason:''}}
global.MapliniReliabilityCore={errorInfo,parseJsonSafe,isUsableProcess,makeEmergencySnapshot,validateStoreShape};
})(typeof window!=='undefined'?window:globalThis);
