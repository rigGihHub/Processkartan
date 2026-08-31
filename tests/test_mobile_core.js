const fs=require('fs'),vm=require('vm');vm.runInThisContext(fs.readFileSync('maplini_mobile_core.js','utf8'));const M=globalThis.MapliniMobileCore;
function ok(v,m){if(!v)throw new Error(m)}
let p=M.clientToLocal(125,80,{left:-375,top:20});ok(p.x===500&&p.y===60,'scrolled coordinate');ok(M.dragThreshold('touch')>M.dragThreshold('mouse'),'threshold');
ok(!M.movedEnough(3,3,'touch'),'jitter');ok(M.movedEnough(8,5,'touch'),'touch drag');ok(M.movedEnough(2,0,'mouse'),'mouse precision');ok(M.isCoarse('touch')&&M.isCoarse('pen')&&!M.isCoarse('mouse'),'coarse');
ok(M.gestureDistance({x:0,y:0},{x:3,y:4})===5,'gesture distance');let mid=M.gestureMidpoint({x:10,y:20},{x:30,y:60});ok(mid.x===20&&mid.y===40,'gesture midpoint');
ok(M.pinchScale(1,100,125)===1.25,'pinch zoom in');ok(M.pinchScale(1,100,10)===.25,'pinch clamp min');ok(M.pinchScale(1.4,100,200)===1.5,'pinch clamp max');console.log('mobile core OK');
