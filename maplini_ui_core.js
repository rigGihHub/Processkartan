(function(global){
'use strict';

function selectionHint(state){
  state=state||{};
  const singleLink=state.selectedLinkIndex!==null && state.selectedLinkIndex!==undefined;
  const nodeCount=Number(state.selectedNodeCount||0);
  const linkCount=Number(state.selectedLinkCount||0);
  if(singleLink)return 'Koppling markerad – endast kopplingsinställningar visas.';
  if(nodeCount>1)return nodeCount+' objekt markerade – använd Ta bort markerat eller klicka utanför för att avmarkera.';
  if(nodeCount===1 || state.nodeEnabled)return 'Ruta markerad – redigera text, färg, formatering och inputs/outputs.';
  if(linkCount>0)return linkCount+' kopplingar markerade – använd Ta bort markerat eller klicka utanför för att avmarkera.';
  return 'Markera en ruta eller koppling för att visa relevanta inställningar.';
}

function applyCanvasCalmHotfix(){
  if(typeof document==='undefined')return;
  const styleId='maplini-v02094-workspace-focus';
  if(!document.getElementById(styleId)){
    const style=document.createElement('style');
    style.id=styleId;
    style.textContent=`
      #pk48 .p48-next-step-wrap{left:calc(100% + 7px)!important}
      #pk48 .p48-next-step-btn{width:24px!important;height:24px!important;border:1px solid #9fc4b3!important;border-radius:999px!important;background:rgba(255,255,255,.96)!important;color:#2f8065!important;box-shadow:0 1px 4px rgba(31,52,70,.08)!important;opacity:.78!important;transition:opacity .12s ease,background-color .12s ease,color .12s ease,border-color .12s ease,transform .12s ease!important}
      #pk48 .p48-next-step-btn::before{content:'+'!important;font:750 15px/1 Inter,system-ui!important;transform:translateY(-.5px)}
      #pk48 .p48-next-step-btn:hover,#pk48 .p48-next-step-btn:focus-visible{opacity:1!important;transform:scale(1.04)!important;background:#edf6f1!important;color:#24664f!important;border-color:#6fa58e!important;box-shadow:0 2px 7px rgba(31,92,70,.12)!important}
      #pk48 .p48-node.selected .p48-next-step-btn{opacity:1!important}
      #pk48 .p48-next-step-menu{left:31px!important}
      #pk48 .p48-node.process{box-shadow:0 1px 4px rgba(31,52,70,.07)!important}
      #pk48 .p48-node.process:hover{box-shadow:0 2px 7px rgba(31,52,70,.09)!important}

      /* v0.20.94 – keep editing chrome subordinate to the process */
      #pk48:not(.p48-read-mode) .p48-side{width:268px!important;padding:10px 9px!important}
      #pk48:not(.p48-read-mode) .p48-body{grid-template-columns:268px minmax(0,1fr)!important}
      #pk48 .p48-side details{margin-block:4px!important}
      #pk48 .p48-side summary{min-height:32px!important}
      #pk48 .p48-quick-format{gap:5px!important;padding:7px!important;margin-bottom:7px!important}
      #pk48 .p48-quick-format button{min-height:30px!important}
      #pk48 .p48-canvas-wrap,#pk48 .p48-stage{min-width:0!important}
      @media (min-width:1100px){#pk48:not(.p48-read-mode) .p48-side{width:252px!important}#pk48:not(.p48-read-mode) .p48-body{grid-template-columns:252px minmax(0,1fr)!important}}
      @media (max-width:700px){#pk48:not(.p48-read-mode) .p48-body{grid-template-columns:minmax(0,1fr)!important}#pk48:not(.p48-read-mode) .p48-side{width:auto!important}}
    `;
    document.head.appendChild(style);
  }

  const disablePdfGuide=()=>{
    const select=document.getElementById('p48-pdf-view');
    if(!select)return false;
    if(select.value!=='off'){
      select.value='off';
      select.dispatchEvent(new Event('change',{bubbles:true}));
    }
    return true;
  };
  if(!disablePdfGuide()){
    let tries=0;
    const timer=setInterval(()=>{
      tries+=1;
      if(disablePdfGuide() || tries>30)clearInterval(timer);
    },100);
  }
}

if(typeof document!=='undefined'){
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>setTimeout(applyCanvasCalmHotfix,0),{once:true});
  else setTimeout(applyCanvasCalmHotfix,0);
}

global.MapliniUiCore={selectionHint,applyCanvasCalmHotfix};
})(typeof window!=='undefined'?window:globalThis);
