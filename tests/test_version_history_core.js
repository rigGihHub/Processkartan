require('../maplini_version_history_core.js');
const V=global.MapliniVersionHistoryCore;
function ok(v,m){if(!v)throw new Error(m)}
const p={id:'p',name:'Test',nodes:[{id:'a',type:'process',text:'A'}],links:[]};
let r=V.addVersion(p,[],{now:100,label:'Första'});
ok(r.added&&r.history.length===1,'first version');
let duplicate=V.addVersion(p,r.history,{now:200});
ok(!duplicate.added&&duplicate.history.length===1,'no duplicate snapshot');
const changed=JSON.parse(JSON.stringify(p));changed.nodes[0].text='B';changed.nodes.push({id:'b',type:'end',text:'Slut'});changed.links.push(['a','b','right',{}]);
let r2=V.addVersion(changed,r.history,{now:300,label:'Andra'});
ok(r2.added&&r2.history.length===2&&r2.history[0].createdAt===300,'newest first');
const d=V.diff(p,changed);
ok(d.addedNodes===1&&d.changedNodes===1&&d.addedLinks===1&&d.changed,'diff counts');
ok(V.diffLabel(d).includes('+1 steg')&&V.diffLabel(d).includes('1 ändrade steg'),'diff label');
const many=[];for(let i=0;i<25;i++)many.push(V.addVersion({...p,name:'P'+i},many,{now:1000+i}).record);
ok(V.normalizeHistory(many,20).length===20,'history capped');
console.log('version history core ok');
