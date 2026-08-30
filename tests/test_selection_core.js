const fs=require('fs'),vm=require('vm');vm.runInThisContext(fs.readFileSync('maplini_selection_core.js','utf8'));const S=globalThis.MapliniSelectionCore;
function ok(v,m){if(!v)throw new Error(m)}
ok(!S.hasAny(S.clear()),'clear');ok(S.deleteAction({selectedId:'a'})==='node','node');ok(S.deleteAction({selectedLinkIndex:2})==='link','link');ok(S.deleteAction({selectedIds:['a'],selectedLinkIndices:[2]})==='many','mixed');
let x=S.afterLinkDelete({selectedLinkIndices:[1,3,5]},3);ok(x.selectedLinkIndices.join(',')==='1,4','reindex multi');
let y=S.afterLinkDelete({selectedLinkIndex:3},1);ok(y.selectedLinkIndex===2,'reindex single');
console.log('selection core OK');
