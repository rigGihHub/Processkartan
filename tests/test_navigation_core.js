const assert=require('assert');
global.window=global;
require('../maplini_navigation_core.js');
const nodes=[
 {id:'s',type:'start',text:'Start',x:0,y:0},
 {id:'a',type:'process',text:'A',x:100,y:0},
 {id:'d',type:'decision',text:'Beslut',x:200,y:0},
 {id:'y',type:'process',text:'Ja-väg',x:300,y:-60},
 {id:'n',type:'process',text:'Nej-väg',x:300,y:60},
 {id:'e',type:'end',text:'Slut',x:400,y:0}
];
const links=[['s','a','right'],['a','d','right'],['d','y','right',{label:'Ja'}],['d','n','right',{label:'Nej'}],['y','e','right'],['n','e','right']];
let st=MapliniNavigationCore.analyze(nodes,links,'d');
assert.deepStrictEqual(st.starts.map(x=>x.id),['s']);
assert.deepStrictEqual(st.ends.map(x=>x.id),['e']);
assert.deepStrictEqual(st.previous.map(x=>x.id),['a']);
assert.deepStrictEqual(st.next.map(x=>x.id),['y','n']);
assert.deepStrictEqual(st.next.map(x=>x.branchLabel),['Ja','Nej']);
st=MapliniNavigationCore.analyze([{id:'b',text:'B',x:0,y:100},{id:'a',text:'A',x:0,y:0}],[],'a');
assert.deepStrictEqual(st.starts.map(x=>x.id),['a','b']);
assert.deepStrictEqual(st.ends.map(x=>x.id),['a','b']);
console.log('navigation core ok');
