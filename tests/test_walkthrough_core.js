const assert=require('assert');
require('../maplini_walkthrough_core.js');
const W=global.MapliniWalkthroughCore;

const qs=W.normalizeQuestions([
  {id:'q1',text:' Är underlaget komplett? '},
  {id:'q1',text:'Är kontrollen utförd?',required:false},
  {text:'   '},
]);
assert.strictEqual(qs.length,2);
assert.strictEqual(qs[0].text,'Är underlaget komplett?');
assert.notStrictEqual(qs[0].id,qs[1].id,'duplicate question ids are made unique');
assert.strictEqual(qs[1].required,false);

const nodes=[
  {id:'s',type:'start',text:'Start'},
  {id:'a',type:'process',text:'Kontrollera'},
  {id:'d',type:'decision',text:'Godkänd?'},
  {id:'e',type:'end',text:'Slut'},
];
const links=[['s','a','right',{}],['a','d','right',{}],['d','e','right',{label:'Ja'}]];
assert.deepStrictEqual(W.startNodeIds(nodes,links),['s']);
assert.strictEqual(W.nextEdges('d',nodes,links)[0].label,'Ja');

const roots=W.startNodeIds([{id:'a',type:'process'},{id:'b',type:'process'}],[]);
assert.deepStrictEqual(roots,['a','b']);

const sum=W.summarize([
  {nodeId:'a',nodeText:'Kontrollera',answers:[{question:'Q1',answer:'yes'},{question:'Q2',answer:'no'}]},
  {nodeId:'d',nodeText:'Godkänd?',answers:[{question:'Q3',answer:'yes'}]},
]);
assert.strictEqual(sum.steps,2);
assert.strictEqual(sum.yes,2);
assert.strictEqual(sum.no,1);
assert.strictEqual(sum.passed,false);
assert.strictEqual(sum.deviations[0].question,'Q2');

const routed=W.normalizeQuestions([{id:'route',text:'Är beställningen komplett?',route:true}]);
assert.strictEqual(routed[0].route,true);
const branchEdges=[
  {from:'d',to:'yes-node',label:'Ja'},
  {from:'d',to:'no-node',label:'Nej'}
];
let auto=W.automaticRoute(routed,{route:'yes'},branchEdges);
assert.strictEqual(auto.mode,'auto');
assert.strictEqual(auto.edge.to,'yes-node');
auto=W.automaticRoute(routed,{route:'no'},branchEdges);
assert.strictEqual(auto.mode,'auto');
assert.strictEqual(auto.edge.to,'no-node');
assert.strictEqual(W.automaticRoute(routed,{},branchEdges).mode,'pending');
assert.strictEqual(W.automaticRoute(routed,{route:'yes'},[{from:'d',to:'x',label:'Klar'}]).mode,'manual');
assert.strictEqual(W.normalizedBranchLabel(' YES! '),'yes');
assert.strictEqual(W.normalizedBranchLabel('nej'),'no');


const semantic=W.normalizeQuestions([
  {id:'c',text:'Är kontrollen utförd?',kind:'control'},
  {id:'r',text:'Behövs komplettering?',kind:'route'}
]);
assert.strictEqual(semantic[0].kind,'control');
assert.strictEqual(semantic[1].kind,'route');
assert.strictEqual(W.answerIsDeviation(semantic[0],'no'),true);
assert.strictEqual(W.answerIsDeviation(semantic[1],'no'),false);
assert.strictEqual(W.currentDeviationCount(semantic,{c:'yes',r:'no'}),0);
assert.strictEqual(W.currentDeviationCount(semantic,{c:'no',r:'yes'}),1);
const semanticSummary=W.summarize([
  {nodeId:'a',nodeText:'Steg',answers:[
    {question:'Kontroll',kind:'control',answer:'yes'},
    {question:'Vägval',kind:'route',answer:'no'}
  ]}
]);
assert.strictEqual(semanticSummary.no,1,'raw No is still counted');
assert.strictEqual(semanticSummary.routeNo,1,'route No is tracked');
assert.strictEqual(semanticSummary.deviations.length,0,'route No is not a deviation');
assert.strictEqual(semanticSummary.passed,true);


const detailed=W.summarize([
  {nodeId:'a',nodeText:'Kontrollera',answers:[
    {question:'Är kontrollen utförd?',kind:'control',answer:'no',explanation:'Kontroll saknas',owner:'Anna',dueDate:'2026-09-15'},
    {question:'Behövs komplettering?',kind:'route',answer:'no',explanation:'',owner:'',dueDate:''}
  ]}
]);
assert.strictEqual(detailed.deviations.length,1);
assert.strictEqual(detailed.deviations[0].explanation,'Kontroll saknas');
assert.strictEqual(detailed.deviations[0].owner,'Anna');
assert.strictEqual(detailed.deviations[0].dueDate,'2026-09-15');
assert.strictEqual(detailed.deviations[0].status,'open');
assert.strictEqual(detailed.deviations[0].questionId,'');

require('../maplini_state_core.js');
const S=global.MapliniStateCore;
const proc=S.normalizeProcess({id:'p',nodes:[{id:'a',type:'process',walkthroughQuestions:[{id:'x',text:' Test? '},{id:'x',text:'Test 2?'}]}],links:[]},'p');
assert.strictEqual(proc.nodes[0].walkthroughQuestions.length,2);
assert.strictEqual(proc.nodes[0].walkthroughQuestions[0].text,'Test?');
assert.notStrictEqual(proc.nodes[0].walkthroughQuestions[0].id,proc.nodes[0].walkthroughQuestions[1].id);
console.log('walkthrough core ok');
