const fs=require('fs'),vm=require('vm');
vm.runInThisContext(fs.readFileSync('maplini_ui_core.js','utf8'));
const u=globalThis.MapliniUiCore;
function ok(v,m){if(!v)throw new Error(m);}
ok(u.selectionHint({})==='Markera en ruta eller koppling för att visa relevanta inställningar.','empty');
ok(u.selectionHint({selectedNodeCount:1}).startsWith('Ruta markerad'),'one');
ok(u.selectionHint({selectedNodeCount:3}).startsWith('3 objekt markerade'),'many nodes');
ok(u.selectionHint({selectedLinkCount:2}).startsWith('2 kopplingar markerade'),'many links');
ok(u.selectionHint({selectedLinkIndex:0}).startsWith('Koppling markerad'),'single link');
console.log('ui core OK');
