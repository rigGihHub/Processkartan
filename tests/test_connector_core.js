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

// v0.15.11 independent connector labels
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
