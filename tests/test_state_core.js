const fs=require('fs'),vm=require('vm');vm.runInThisContext(fs.readFileSync('maplini_state_core.js','utf8'));const s=globalThis.MapliniStateCore;
function ok(v,m){if(!v)throw new Error(m)}
let p=s.normalizeProcess({id:'p1',nodes:[{id:'a',type:'process',x:'12'},{id:'b',type:'end'}],links:[['a','b','right',{color:'#123456'}],['a','missing','right',{}]]},'x');
ok(p.nodes[0].x===12,'number');ok(p.links.length===1,'drop orphan');ok(Array.isArray(p.links[0])&&p.links[0][0]==='a'&&p.links[0][1]==='b','array preserved');ok(p.links[0][3].color==='#123456','style preserved');
let legacy=s.normalizeProcess({id:'p2',nodes:[{id:'a'},{id:'b'}],links:[{sourceId:'a',targetId:'b',side:'bottom',style:{width:3}}]},'p2');ok(legacy.links[0][2]==='bottom'&&legacy.links[0][3].width===3,'legacy link');
let st=s.normalizeStore({currentId:'missing',processes:{p1:p}});ok(st.currentId==='p1'&&st.schemaVersion===1,'store');console.log('state core OK');

{
  const n = MapliniStateCore.normalizeNode({id:'shape-1',type:'process',text:'A',shapePreset:'rounded'},0);
  if(n.shapePreset!=='rounded') throw new Error('shapePreset should persist');
  const bad = MapliniStateCore.normalizeNode({id:'shape-2',type:'process',shapePreset:'triangle'},1);
  if(bad.shapePreset!=='standard') throw new Error('invalid shapePreset should normalize to standard');
}
