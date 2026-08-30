(function(global){
'use strict';
function num(v,fallback=0){const n=Number(v);return Number.isFinite(n)?n:fallback}
function clientToLocal(clientX,clientY,rect){rect=rect||{left:0,top:0};return {x:num(clientX)-num(rect.left),y:num(clientY)-num(rect.top)}}
function dragThreshold(pointerType){pointerType=String(pointerType||'mouse').toLowerCase();if(pointerType==='touch')return 9;if(pointerType==='pen')return 5;return 2}
function movedEnough(dx,dy,pointerType){const t=dragThreshold(pointerType);return Math.hypot(num(dx),num(dy))>=t}
function isCoarse(pointerType){pointerType=String(pointerType||'').toLowerCase();return pointerType==='touch'||pointerType==='pen'}
global.MapliniMobileCore={clientToLocal,dragThreshold,movedEnough,isCoarse};
})(typeof window!=='undefined'?window:globalThis);
