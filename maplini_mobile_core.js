(function(global){
'use strict';
function num(v,fallback=0){const n=Number(v);return Number.isFinite(n)?n:fallback}
function clientToLocal(clientX,clientY,rect){rect=rect||{left:0,top:0};return {x:num(clientX)-num(rect.left),y:num(clientY)-num(rect.top)}}
function dragThreshold(pointerType){pointerType=String(pointerType||'mouse').toLowerCase();if(pointerType==='touch')return 9;if(pointerType==='pen')return 5;return 2}
function movedEnough(dx,dy,pointerType){const t=dragThreshold(pointerType);return Math.hypot(num(dx),num(dy))>=t}
function isCoarse(pointerType){pointerType=String(pointerType||'').toLowerCase();return pointerType==='touch'||pointerType==='pen'}
function gestureDistance(a,b){if(!a||!b)return 0;return Math.hypot(num(b.x)-num(a.x),num(b.y)-num(a.y))}
function gestureMidpoint(a,b){if(!a||!b)return{x:0,y:0};return{x:(num(a.x)+num(b.x))/2,y:(num(a.y)+num(b.y))/2}}
function pinchScale(startScale,startDistance,currentDistance,min=.25,max=1.5){const base=Math.max(1,num(startDistance,1));const raw=num(startScale,1)*(Math.max(1,num(currentDistance,1))/base);return Math.max(num(min,.25),Math.min(num(max,1.5),Math.round(raw*100)/100))}
global.MapliniMobileCore={clientToLocal,dragThreshold,movedEnough,isCoarse,gestureDistance,gestureMidpoint,pinchScale};
})(typeof window!=='undefined'?window:globalThis);
