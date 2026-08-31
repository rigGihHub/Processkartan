(function(global){
  'use strict';
  const DEFAULT_BOUNDS={width:2400,height:1400,padding:10};
  function num(v,fallback=0){const n=Number(v);return Number.isFinite(n)?n:fallback}
  function snap(value,grid=20){grid=Math.max(1,num(grid,20));return Math.round(num(value)/grid)*grid}
  function clamp(v,min,max){return Math.max(min,Math.min(max,v))}
  function normalizeRect(a,b){
    const x1=num(a?.x),y1=num(a?.y),x2=num(b?.x),y2=num(b?.y);
    return{left:Math.min(x1,x2),top:Math.min(y1,y2),right:Math.max(x1,x2),bottom:Math.max(y1,y2)};
  }
  function rectsIntersect(a,b){return !(a.right<b.left||a.left>b.right||a.bottom<b.top||a.top>b.bottom)}
  function place(x,y,width,height,bounds=DEFAULT_BOUNDS,grid=20){
    const pad=num(bounds.padding,10),bw=num(bounds.width,2400),bh=num(bounds.height,1400);
    const w=Math.max(0,num(width)),h=Math.max(0,num(height));
    return{
      x:clamp(snap(x,grid),pad,Math.max(pad,bw-w-pad)),
      y:clamp(snap(y,grid),pad,Math.max(pad,bh-h-pad))
    };
  }
  function resize(box,corner,dx,dy,type='process',bounds=DEFAULT_BOUNDS){
    const start={x:num(box.x),y:num(box.y),width:num(box.width),height:num(box.height)};
    dx=num(dx);dy=num(dy);corner=String(corner||'se');
    let w=start.width+(corner.includes('e')?dx:-dx);
    let h=start.height+(corner.includes('s')?dy:-dy);
    if(type==='decision'){
      const size=clamp(Math.max(w,h),130,420);w=size;h=size;
    }else{
      w=clamp(w,120,700);h=clamp(h,54,500);
    }
    let x=corner.includes('w')?start.x+start.width-w:start.x;
    let y=corner.includes('n')?start.y+start.height-h:start.y;
    const pad=num(bounds.padding,10),bw=num(bounds.width,2400),bh=num(bounds.height,1400);
    x=clamp(x,pad,Math.max(pad,bw-w-pad));
    y=clamp(y,pad,Math.max(pad,bh-h-pad));
    // If clamping the top/left edge, keep dimensions inside the canvas too.
    w=Math.min(w,Math.max(0,bw-x-pad));
    h=Math.min(h,Math.max(0,bh-y-pad));
    if(type==='decision'){
      const size=Math.max(130,Math.min(420,Math.min(w,h)));w=size;h=size;
    }
    return{x,y,width:w,height:h};
  }
  function hasMeaningfulDelta(dx,dy,threshold=2){return Math.abs(num(dx))+Math.abs(num(dy))>=Math.max(0,num(threshold,2))}
  function zoomStep(scale,direction,step=.1,min=.25,max=1.5){
    const current=num(scale,1),delta=Math.abs(num(step,.1));
    const next=String(direction)==='out'?current-delta:current+delta;
    return Math.round(clamp(next,min,max)*100)/100;
  }
  global.MapliniCanvasCore={DEFAULT_BOUNDS,snap,clamp,normalizeRect,rectsIntersect,place,resize,hasMeaningfulDelta,zoomStep};
})(typeof window!=='undefined'?window:globalThis);
