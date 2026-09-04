const fs=require('fs'),vm=require('vm'),assert=require('assert');
const code=fs.readFileSync(require('path').join(__dirname,'..','maplini_connector_core.js'),'utf8');
vm.runInThisContext(code);
const C=globalThis.MapliniConnectorCore;
assert(C,'connector core missing');
let links=[];
links.push(C.create('n1','n2','right'));
assert.deepStrictEqual(links[0].slice(0,3),['n1','n2','right']);
assert.strictEqual(C.style(links[0]).color,'#5b6775');
C.setStyle(links,0,{color:'#ff0000',width:4,dash:'dashed'});
assert.strictEqual(C.style(links[0]).color,'#ff0000');
assert.strictEqual(C.style(links[0]).width,4);
assert.strictEqual(C.style(links[0]).dash,'dashed');
C.setVia(links,0,120,220);
assert.strictEqual(C.style(links[0]).viaX,120);
assert.strictEqual(C.style(links[0]).viaY,220);
let serialized=JSON.stringify(links);
let restored=C.normalizeLinks(JSON.parse(serialized));
assert.deepStrictEqual(restored,links);
restored.push(C.create('n2','n3','bottom',{end:'diamond'}));
assert.strictEqual(C.style(restored[1]).end,'diamond');
let remaining=C.removeAt(restored,0);
assert.strictEqual(remaining.length,1);
assert.strictEqual(remaining[0][0],'n2');
assert.strictEqual(C.selectionAfterDelete(1,0),0);
assert.strictEqual(C.selectionAfterDelete(0,0),null);
let bulk=C.removeSelected([C.create('a','b'),C.create('b','c'),C.create('c','d')],new Set(['b']),new Set());
assert.strictEqual(bulk.length,1);
assert.deepStrictEqual(bulk[0].slice(0,2),['c','d']);
let area=C.rectsIntersect({left:0,right:10,top:0,bottom:10},{left:5,right:15,top:5,bottom:15});
assert.strictEqual(area,true);

// v0.11.4: straight routing must ignore stale/manual via points and remain a single segment.
{
  const pts = C.routePoints(10,20,210,80,'right','left',{routing:'straight',viaX:90,viaY:140});
  assert.deepStrictEqual(pts, [[10,20],[210,80]]);
}
console.log('connector lifecycle OK');
let modern=C.create('x','y','right');
assert.strictEqual(C.style(modern).routing,'orthogonal');
assert.strictEqual(C.style(modern).anchorMode,'auto');
assert.deepStrictEqual(C.autoSides(100,20),['right','left']);
assert.deepStrictEqual(C.autoSides(-100,20),['left','right']);
assert.deepStrictEqual(C.autoSides(10,100),['bottom','top']);
let pts=C.routePoints(0,10,100,50,'right','left',{routing:'orthogonal'});
assert.deepStrictEqual(pts,[[0,10],[50,10],[50,50],[100,50]]);
assert.strictEqual(C.pathData(pts),'M0,10 L50,10 L50,50 L100,50');
let mp=C.midpoint([[0,0],[100,0],[100,100]]);
assert.deepStrictEqual(mp,{x:100,y:0});

assert.strictEqual(C.style(C.create('d','a','right')).label,'');
assert.strictEqual(C.decisionLabel(0),'Ja');
assert.strictEqual(C.decisionLabel(1),'Nej');
assert.strictEqual(C.decisionLabel(2),'');
let labeled=C.create('d','x','right',{label:'Godkänd'});
assert.strictEqual(C.style(labeled).label,'Godkänd');
assert.strictEqual(C.style(C.normalizeLink(JSON.parse(JSON.stringify(labeled)))).label,'Godkänd');

// v0.10.45: splitting a link inserts a node without losing visual flow style.
{
  const links=[C.create('a','b','right',{color:'#123456',width:3,dash:'dashed',routing:'straight',anchorMode:'manual',label:'Ja',viaX:88,viaY:44})];
  const out=C.splitLink(links,0,'n9');
  assert.strictEqual(out.length,2);
  assert.deepStrictEqual(out[0].slice(0,2),['a','n9']);
  assert.deepStrictEqual(out[1].slice(0,2),['n9','b']);
  assert.strictEqual(C.style(out[0]).label,'Ja');
  assert.strictEqual(C.style(out[1]).label,'');
  assert.strictEqual(C.style(out[0]).color,'#123456');
  assert.strictEqual(C.style(out[1]).dash,'dashed');
  assert.strictEqual(C.style(out[0]).routing,'straight');
  assert.strictEqual(C.style(out[0]).anchorMode,'auto');
  assert.strictEqual(C.style(out[0]).viaX,null);
  assert.strictEqual(C.style(out[1]).viaY,null);
}

const mixedDragged=C.routePoints(0,0,100,100,'right','top',{routing:'orthogonal',viaX:40,viaY:60});
assert(mixedDragged.some(p=>p[0]===40&&p[1]===60));

// v0.19.1 independent connector labels
let labelLinks=[
  C.create('a','b','right',{label:'Godkänd'}),
  C.create('b','c','right',{label:'Avslag'})
];
assert.strictEqual(labelLinks[0][3].label,'Godkänd');
assert.strictEqual(labelLinks[1][3].label,'Avslag');
C.setStyle(labelLinks,0,{label:'Ja'});
assert.strictEqual(labelLinks[0][3].label,'Ja');
assert.strictEqual(labelLinks[1][3].label,'Avslag');
console.log('independent connector labels ok');

// v0.20.16: auto-managed orthogonal routes can detour around blocking nodes.
{
  const obstacles=[{left:40,right:60,top:0,bottom:80}];
  const smart=C.smartOrthogonalRoute(0,10,100,70,'right','left',{routing:'orthogonal'},obstacles,10);
  assert.strictEqual(C.routeScore(smart,obstacles,10)<100000,true);
  assert.notDeepStrictEqual(smart,[[0,10],[50,10],[50,70],[100,70]]);
}
console.log('smart orthogonal obstacle routing ok');

// v0.20.17: smart auto-routes prefer a clean corridor over crossing an unrelated connector.
{
  const existing=[{x1:20,y1:40,x2:80,y2:40,sourceId:'c',targetId:'d'}];
  const base=C.routePoints(0,10,100,70,'right','left',{routing:'orthogonal'});
  assert.strictEqual(C.routeCrossingCount(base,existing,{sourceId:'a',targetId:'b'})>0,true);
  const smart=C.smartOrthogonalRoute(0,10,100,70,'right','left',{routing:'orthogonal'},[],10,existing,{sourceId:'a',targetId:'b'});
  assert.strictEqual(C.routeCrossingCount(smart,existing,{sourceId:'a',targetId:'b'}),0);
  assert.notDeepStrictEqual(smart,base);
}
console.log('smart connector crossing reduction ok');

// Shared source/target fan-out is intentionally not treated as an avoidable crossing.
{
  const shared=[{x1:0,y1:10,x2:60,y2:50,sourceId:'a',targetId:'c'}];
  const candidate=[[0,10],[50,10],[50,70],[100,70]];
  assert.strictEqual(C.routeCrossingCount(candidate,shared,{sourceId:'a',targetId:'b'}),0);
}
console.log('shared endpoint crossing exemption ok');

// v0.20.19: long parallel overlap should be separated, while a short shared trunk is allowed.
{
  const existing=[{x1:20,y1:10,x2:80,y2:10,sourceId:'shared',targetId:'old'}];
  const sameLane=[[0,10],[100,10]];
  const separated=[[0,10],[20,10],[20,38],[80,38],[80,70],[100,70]];
  const overlap=C.routeParallelOverlap(sameLane,existing,{sourceId:'new',targetId:'target'});
  assert.ok(overlap>=50,'unrelated parallel overlap should be measured');
  assert.ok(C.routeScore(separated,[],10,existing,{sourceId:'new',targetId:'target'})<C.routeScore(sameLane,[],10,existing,{sourceId:'new',targetId:'target'}),'clean parallel lane should score better than long overlap');
  const shortShared=C.routeParallelOverlap([[0,10],[24,10],[24,50]], [{x1:0,y1:10,x2:24,y2:10,sourceId:'shared',targetId:'old'}], {sourceId:'shared',targetId:'new'});
  assert.strictEqual(shortShared,0,'short shared trunk at a common endpoint should remain allowed');
}
console.log('connector lane separation ok');

// v0.20.19 integration: smart routing chooses a nearby lane instead of sitting on an existing one.
{
  const existing=[{x1:50,y1:10,x2:50,y2:50,sourceId:'old-a',targetId:'old-b'}];
  const smart=C.smartOrthogonalRoute(0,0,100,60,'right','left',{routing:'orthogonal'},[],10,existing,{sourceId:'new-a',targetId:'new-b'});
  const overlap=C.routeParallelOverlap(smart,existing,{sourceId:'new-a',targetId:'new-b'});
  assert.strictEqual(overlap,0,'smart route should choose a separated corridor when the natural lane is already occupied');
}
console.log('smart connector lane selection ok');

// v0.20.19: connector labels prefer clean straight segments away from nodes and other labels.
{
  const points=[[0,50],[80,50],[80,150],[200,150]];
  const blockedAbove={left:36,right:86,top:12,bottom:42};
  const placed=C.smartLabelPlacement(points,54,26,[blockedAbove],[],{offset:22,clearance:8});
  assert.ok(placed,'label placement should exist');
  assert.strictEqual(C.rectsIntersect(placed.box,blockedAbove),false,'label should avoid blocking node');
}
{
  const points=[[0,50],[200,50]];
  const occupied=[{left:73,right:127,top:12,bottom:38}];
  const placed=C.smartLabelPlacement(points,54,26,[],occupied,{offset:22,clearance:8});
  assert.ok(placed,'label placement should exist with occupied label');
  assert.strictEqual(C.rectsIntersect(placed.box,occupied[0]),false,'label should avoid another connector label when a clean alternative exists');
}
console.log('smart connector label clarity ok');
