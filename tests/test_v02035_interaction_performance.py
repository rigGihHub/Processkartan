from pathlib import Path
APP=(Path(__file__).resolve().parents[1]/'app.py').read_text(encoding='utf-8')

def test_version():
    assert 'APP_VERSION = "0.20.71"' in APP

def test_drag_snap_targets_are_cached_for_the_gesture():
    assert 'function buildMagneticSnapTargets(excludeIds)' in APP
    assert 'snapTargets=buildMagneticSnapTargets(snapExclude)' in APP
    assert 'magneticSnap(reference,reference.x+delta.dx,reference.y+delta.dy,snapExclude,snapTargets)' in APP

def test_snap_lookup_is_binary_search_not_layout_read_per_pointermove():
    assert 'function nearestSortedValue(values,target,tolerance)' in APP
    body=APP.split('function magneticSnap(start,proposedX,proposedY,excludeIds,targetCache=null){',1)[1].split('\n}',1)[0]
    assert 'offsetWidth' not in body and 'offsetHeight' not in body

def test_drag_pointermoves_are_coalesced_to_animation_frames():
    assert 'pendingMove=null,moveRaf=0' in APP
    assert 'if(!moveRaf)moveRaf=requestAnimationFrame(flushMove)' in APP
    assert 'if(pendingMove){const ev=pendingMove;pendingMove=null;applyMove(ev)}' in APP

def test_overview_uses_geometry_cache():
    assert 'const d=item.data||{},g=nodeGeom(d.id),w=g?.width' in APP
