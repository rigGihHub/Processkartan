const assert=require('assert');
require('../maplini_editing_core.js');
const E=global.MapliniEditingCore;

const nodes=[
 {id:'n1',type:'process',text:'A',x:10,y:20,width:180,documentUrl:'',nodeStyle:'3d'},
 {id:'n2',type:'document',text:'B',x:250,y:20,documentUrl:'https://example.com'},
 {id:'n3',type:'process',text:'C',x:500,y:20}
];
const links=[
 ['n1','n2','right',{color:'#111111',width:3,routing:'orthogonal',anchorMode:'auto',label:'Ja',viaX:150,viaY:80}],
 ['n2','n3','right',{label:'Nej'}]
];
const clip=E.makeClipboard(nodes,links,['n1','n2']);
assert.strictEqual(clip.nodes.length,2);
assert.strictEqual(clip.links.length,1,'only internal links should be copied');
assert.strictEqual(clip.nodes[1].documentUrl,'https://example.com');
let seq=10;
const out=E.instantiate(clip,()=>`n${++seq}`,28);
assert.deepStrictEqual(out.nodes.map(n=>n.id),['n11','n12']);
assert.strictEqual(out.nodes[0].x,38);
assert.strictEqual(out.nodes[0].y,48);
assert.strictEqual(out.nodes[0].nodeStyle,'3d');
assert.strictEqual(out.nodes[1].documentUrl,'https://example.com');
assert.strictEqual(out.links.length,1);
assert.strictEqual(out.links[0][0],'n11');
assert.strictEqual(out.links[0][1],'n12');
assert.strictEqual(out.links[0][3].label,'Ja');
assert.strictEqual(out.links[0][3].viaX,178);
assert.strictEqual(out.links[0][3].viaY,108);
const text=E.serialize(clip);
assert.ok(text.startsWith('MAPLINI_CLIPBOARD_V1\n'));
assert.strictEqual(E.parse(text).nodes.length,2);
assert.strictEqual(E.parse('hello'),null);
console.log('editing core ok');
const delta=E.groupMoveDelta([
  {x:100,y:100,width:180,height:80},
  {x:400,y:200,width:200,height:100}
],37,43,{width:1000,height:700,padding:10},20);
assert.deepStrictEqual(delta,{dx:40,dy:40},'group movement should use one snapped delta');
const bounded=E.groupMoveDelta([{x:800,y:500,width:180,height:180}],100,100,{width:1000,height:700,padding:10},20);
assert.deepStrictEqual(bounded,{dx:10,dy:10},'group delta should clamp the entire selection inside canvas');
const vias=E.movedInternalVias(links,['n1','n2'],40,20);
assert.deepStrictEqual(vias,[{index:0,viaX:190,viaY:100}], 'only internal connector via points should move with group');

const nextRight=E.nextStepPosition({x:100,y:100,width:180,height:80},{width:180,height:80},[{x:100,y:100,width:180,height:80}],{width:1200,height:800,padding:10},120);
assert.deepStrictEqual(nextRight,{x:400,y:100},'quick next should prefer right when space is clear');
const nextAvoid=E.nextStepPosition({x:100,y:100,width:180,height:80},{width:180,height:80},[{x:100,y:100,width:180,height:80},{x:400,y:100,width:180,height:80}],{width:1200,height:800,padding:10},120);
assert.strictEqual(nextAvoid.y,300,'quick next should choose below when right side is occupied');


const smartStraight=E.smartNextStepPosition({x:100,y:100,width:180,height:80},{width:180,height:80},[{x:100,y:100,width:180,height:80}],{width:1400,height:900,padding:10},{gap:110,direction:'right',grid:20});
assert.deepStrictEqual(smartStraight,{x:400,y:100,direction:'right'},'smart next should stay aligned with the current flow');
const smartOccupied=E.smartNextStepPosition({x:100,y:100,width:180,height:80},{width:180,height:80},[{x:100,y:100,width:180,height:80},{x:400,y:100,width:180,height:80}],{width:1400,height:900,padding:10},{gap:110,direction:'right',grid:20});
assert.strictEqual(smartOccupied.x,400,'occupied main lane should keep forward progress instead of dropping below the source');
assert.notStrictEqual(smartOccupied.y,100,'occupied main lane should use a parallel lane');
const branchA=E.smartNextStepPosition({x:300,y:300,width:180,height:80},{width:180,height:80},[{x:300,y:300,width:180,height:80}],{width:1600,height:1000,padding:10},{gap:110,direction:'right',branchIndex:0,grid:20});
const branchB=E.smartNextStepPosition({x:300,y:300,width:180,height:80},{width:180,height:80},[{x:300,y:300,width:180,height:80},{x:600,y:180,width:180,height:80}],{width:1600,height:1000,padding:10},{gap:110,direction:'right',branchIndex:1,grid:20});
assert.ok(branchA.y<300 && branchB.y>300,'decision branches should fan out around the decision');

const fit=E.fitToScreen([
  {id:'a',x:100,y:100,width:200,height:100},
  {id:'b',x:700,y:500,width:200,height:100}
],{width:800,height:600},{margin:50,minScale:.25,maxScale:1.5});
assert.ok(fit.scale>0 && fit.scale<=1.5,'fit scale should be bounded');
assert.strictEqual(fit.box.left,100);
assert.strictEqual(fit.box.right,900);

const aligned=E.alignNodes([
  {id:'a',x:100,y:100,width:100,height:60},
  {id:'b',x:300,y:180,width:200,height:80}
],'hcenter');
assert.strictEqual(aligned.a.x,250);
assert.strictEqual(aligned.b.x,200);

const distributed=E.distributeNodes([
  {id:'a',x:100,y:50,width:100,height:50},
  {id:'b',x:300,y:80,width:200,height:50},
  {id:'c',x:800,y:100,width:100,height:50}
],'horizontal');
assert.deepStrictEqual(distributed.a.x,100);
assert.deepStrictEqual(distributed.c.x,800);
assert.deepStrictEqual(distributed.b.x,400,'distribution should create equal edge-to-edge gaps');
console.log('layout editing helpers ok');
