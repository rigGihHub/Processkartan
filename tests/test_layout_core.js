const assert=require('assert');
require('../maplini_layout_core.js');
const L=global.MapliniLayoutCore;
const nodes=[
 {id:'a',x:20,y:100,width:120,height:60},
 {id:'b',x:350,y:220,width:140,height:60},
 {id:'c',x:360,y:20,width:140,height:60},
 {id:'d',x:700,y:120,width:120,height:60}
];
const links=[['a','b','right',{label:'Ja'}],['a','c','right',{label:'Nej'}],['b','d'],['c','d']];
const h=L.smartLayout(nodes,links,{orientation:'horizontal',mainGap:120,crossGap:50});
assert(h.a.x<h.b.x && h.a.x<h.c.x,'branches move to later rank');
assert.strictEqual(h.b.x,h.c.x,'siblings share rank');
assert(h.d.x>h.b.x,'merge is later rank');
assert(h.b.y<h.c.y,'Ja branch is placed before/above Nej even if original visual order was reversed');
const v=L.smartLayout(nodes,links,{orientation:'vertical',mainGap:100,crossGap:40});
assert(v.a.y<v.b.y && v.d.y>v.b.y,'vertical ranks progress downward');
assert.strictEqual(v.b.y,v.c.y,'vertical siblings share rank');
assert(v.b.x<v.c.x,'Ja branch is placed left of Nej in vertical layout');

// A feedback loop must not make ranks grow indefinitely or push the loop target after its source.
const loopNodes=[
 {id:'start',x:20,y:80,width:100,height:50},
 {id:'x',x:220,y:80,width:100,height:50},
 {id:'y',x:420,y:80,width:100,height:50},
 {id:'z',x:620,y:80,width:100,height:50}
];
const loopLinks=[['start','x'],['x','y'],['y','z'],['z','x']];
const analysis=L.analyzeLayout(loopNodes,loopLinks,{orientation:'horizontal'});
assert(analysis.feedbackEdges.some(e=>e.from==='z'&&e.to==='x'),'cycle edge is classified as feedback');
assert(analysis.ranks.start<analysis.ranks.x && analysis.ranks.x<analysis.ranks.y && analysis.ranks.y<analysis.ranks.z,'forward loop path keeps compact forward ranks');
const loopLayout=L.smartLayout(loopNodes,loopLinks,{orientation:'horizontal',mainGap:100,crossGap:40,bounds:{width:1600,height:800,padding:20}});
assert(loopLayout.start.x<loopLayout.x.x && loopLayout.x.x<loopLayout.y.x && loopLayout.y.x<loopLayout.z.x,'loop layout keeps main flow forward');
assert(loopLayout.z.x-loopLayout.start.x<1200,'loop remains compact');

// Crossing reduction: parents with matching children should preserve paired ordering.
const crossNodes=[
 {id:'p1',x:20,y:20,width:100,height:50},{id:'p2',x:20,y:220,width:100,height:50},
 {id:'q1',x:400,y:220,width:100,height:50},{id:'q2',x:400,y:20,width:100,height:50}
];
const crossLinks=[['p1','q2'],['p2','q1']];
const cross=L.smartLayout(crossNodes,crossLinks,{orientation:'horizontal',mainGap:120,crossGap:60});
assert(cross.q2.y<cross.q1.y,'barycentric ordering follows parent order and avoids a crossing');
console.log('layout core ok');
