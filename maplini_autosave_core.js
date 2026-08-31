(function(global){
'use strict';
function normalizeCapturedAt(value){const n=Number(value||0);return Number.isFinite(n)&&n>0?n:0}
function makeRecoverySnapshot(store,capturedAt){return {version:1,kind:'maplini-recovery',capturedAt:normalizeCapturedAt(capturedAt)||Date.now(),store:store&&typeof store==='object'?store:null}}
function parseRecovery(raw){if(typeof raw!=='string'||!raw.trim())return null;try{const value=JSON.parse(raw);if(!value||value.kind!=='maplini-recovery'||!value.store||typeof value.store!=='object')return null;return {version:Number(value.version||1),kind:'maplini-recovery',capturedAt:normalizeCapturedAt(value.capturedAt),store:value.store}}catch(e){return null}}
function comparable(store){if(!store||typeof store!=='object')return '';try{return JSON.stringify({schemaVersion:Number(store.schemaVersion||1),currentId:String(store.currentId||''),processes:store.processes&&typeof store.processes==='object'?store.processes:{}})}catch(e){return ''}}
function differs(recoveryStore,primaryStore){const a=comparable(recoveryStore),b=comparable(primaryStore);return !!a&&a!==b}
function shouldOfferRecovery(snapshot,primaryStore){return !!(snapshot&&snapshot.store&&differs(snapshot.store,primaryStore))}
function saveLabel(state,timeText){if(state==='saving')return 'Sparar…';if(state==='error')return 'Sparfel';if(state==='recovered')return 'Återställd';return timeText?('Autosparad · '+timeText):'Autosparad'}
global.MapliniAutosaveCore={makeRecoverySnapshot,parseRecovery,differs,shouldOfferRecovery,saveLabel};
})(typeof window!=='undefined'?window:globalThis);
