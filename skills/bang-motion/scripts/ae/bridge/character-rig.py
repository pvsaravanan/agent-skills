"""Native character rig for the AE bridge (see references/ae-bridge-higgsfield.md).
After these ops: modify_layer "<p> ROOT" parentLayerName "CAM", then reset ROOT's position/scale (parenting to a keyframed CAM bakes in its transform).

Native caveman rig (shape layers + joint nulls) → a list of ae_batch ops.
The pattern proven on the bridge: create the shape at its comp position → set the anchor at the joint point + position = the joint point →
parent (the jump keeps the position). A joint's rotation then turns exactly at that joint.

usage: python character-rig.py "<comp>" <prefix> <x> <gy> <scale> [variant]   → prints the JSON ops
variants: main (bearded, fur tunic), member1..3 (different colors/hair)
Hierarchy: <p> ROOT(null, pelvis) → thigh → shin → foot ; ROOT → torso → arm → forearm → hand ; torso → head → hair/eyes/brows/mouth/beard
"""
import json, sys

def col(h): h = h.lstrip('#'); return {"r": round(int(h[0:2], 16) / 255, 3), "g": round(int(h[2:4], 16) / 255, 3), "b": round(int(h[4:6], 16) / 255, 3)}
VAR = {
    'main':      dict(skin='#C98B5E', skin2='#B07650', tunic='#A9724A', tunic2='#8C5A36', hair='#3B2A20', beard=True),
    'member1': dict(skin='#D39A6A', skin2='#B9835A', tunic='#7F8F5A', tunic2='#66744A', hair='#2F2620', beard=False),
    'member2': dict(skin='#B8784E', skin2='#9E6644', tunic='#C8553D', tunic2='#A84634', hair='#4A3325', beard=False),
    'member3': dict(skin='#C48A5C', skin2='#AA744E', tunic='#9C9186', tunic2='#7D736A', hair='#2B2B2B', beard=True),
}

def rig(comp, p, x, gy, s, var='main'):
    V = VAR[var]; ops = []
    def add(name, shape, cx, cy, w, h, c, r=0):
        ops.append({"tool": "add_shape_layer", "input": {"compositionName": comp, "name": f"{p} {name}", "shapeType": shape,
                    "size": [round(w * s, 1), round(h * s, 1)], "position": [round(cx, 1), round(cy, 1)], "fillColor": col(c),
                    **({"roundness": round(r * s, 1)} if shape == 'rectangle' and r else {})}})
    def joint(name, ax, ay, jx, jy):
        """anchor (layer coordinates, relative to the shape center) + the joint point position in the comp."""
        ops.append({"tool": "modify_layer", "input": {"compositionName": comp, "layerName": f"{p} {name}",
                    "anchorPoint": [round(ax * s, 1), round(ay * s, 1)], "position": [round(jx, 1), round(jy, 1)]}})
    def parent(child, par):
        ops.append({"tool": "modify_layer", "input": {"compositionName": comp, "layerName": f"{p} {child}", "parentLayerName": f"{p} {par}"}})
    X = lambda dx: x + dx * s
    Y = lambda dy: gy + dy * s        # negative dy = upward from the sole
    pel = (X(0), Y(-214))
    # ---- ROOT ----
    ops.append({"tool": "add_null_layer", "input": {"compositionName": comp, "name": f"{p} ROOT"}})
    ops.append({"tool": "modify_layer", "input": {"compositionName": comp, "layerName": f"{p} ROOT", "anchorPoint": [50, 50], "position": [round(pel[0], 1), round(pel[1], 1)]}})
    # ---- back leg (R) then front (L) — creation order = stacking order (the last created is on top) ----
    order = []
    for side, dx, shade in (('R', 24, 'skin2'), ('L', -24, 'skin')):
        hip = (X(dx), Y(-214)); knee = (X(dx), Y(-112)); ank = (X(dx), Y(-16))
        add(f'foot-{side}', 'rectangle', ank[0] + 12 * s, ank[1] + 6 * s, 64, 26, '#5A3E2B', 12); joint(f'foot-{side}', -12, -6, ank[0], ank[1])
        add(f'shin-{side}', 'rectangle', knee[0], knee[1] + 50 * s, 38, 110, V[shade], 18); joint(f'shin-{side}', 0, -50, knee[0], knee[1])
        add(f'thigh-{side}', 'rectangle', hip[0], hip[1] + 52 * s, 46, 118, V[shade], 22); joint(f'thigh-{side}', 0, -52, hip[0], hip[1])
        order += [(f'foot-{side}', f'shin-{side}'), (f'shin-{side}', f'thigh-{side}'), (f'thigh-{side}', 'ROOT')]
    # ---- back arm (R) ----
    sh_r = (X(52), Y(-340)); el_r = (X(52), Y(-262)); wr_r = (X(52), Y(-190))
    add('hand-R', 'ellipse', wr_r[0], wr_r[1] + 8 * s, 34, 40, V['skin2']); joint('hand-R', 0, -8, wr_r[0], wr_r[1])
    add('forearm-R', 'rectangle', el_r[0], el_r[1] + 36 * s, 30, 86, V['skin2'], 15); joint('forearm-R', 0, -36, el_r[0], el_r[1])
    add('arm-R', 'rectangle', sh_r[0], sh_r[1] + 38 * s, 34, 96, V['skin2'], 17); joint('arm-R', 0, -38, sh_r[0], sh_r[1])
    # ---- torso: fur tunic + shoulder strap ----
    add('torso', 'rectangle', X(0), Y(-290), 136, 190, V['tunic'], 48); joint('torso', 0, 76, X(0), Y(-214))
    add('tunic-fringe', 'rectangle', X(0), Y(-205), 150, 40, V['tunic2'], 18); joint('tunic-fringe', 0, 0, X(0), Y(-205))
    add('neck', 'rectangle', X(0), Y(-388), 34, 40, V['skin'], 12); joint('neck', 0, 0, X(0), Y(-388))
    # ---- head ----
    nk = (X(0), Y(-398))
    add('head', 'ellipse', X(0), Y(-470), 150, 162, V['skin']); joint('head', 0, 72, nk[0], nk[1])
    add('ear', 'ellipse', X(-70), Y(-468), 30, 40, V['skin2']); joint('ear', 0, 0, X(-70), Y(-468))
    for k, (dx, dy, w, h) in enumerate([(-48, -540, 80, 70), (0, -556, 96, 74), (48, -540, 80, 70), (-66, -505, 40, 60), (66, -505, 40, 60)]):
        add(f'hair-{k+1}', 'ellipse', X(dx), Y(dy), w, h, V['hair']); joint(f'hair-{k+1}', 0, 0, X(dx), Y(dy))
    if V['beard']:
        add('beard', 'ellipse', X(0), Y(-408), 118, 70, V['hair']); joint('beard', 0, 0, X(0), Y(-408))
    for side, dx in (('L', -28), ('R', 28)):
        add(f'eye-{side}', 'ellipse', X(dx), Y(-472), 16, 20, '#23201C'); joint(f'eye-{side}', 0, 0, X(dx), Y(-472))
        add(f'brow-{side}', 'rectangle', X(dx), Y(-500), 30, 8, V['hair'], 4); joint(f'brow-{side}', 0, 0, X(dx), Y(-500))
    add('nose', 'ellipse', X(4), Y(-450), 26, 22, V['skin2']); joint('nose', 0, 0, X(4), Y(-450))
    add('mouth', 'rectangle', X(2), Y(-422), 34, 9, '#5A2E24', 5); joint('mouth', 0, 0, X(2), Y(-422))
    # ---- front arm (L) ----
    sh_l = (X(-52), Y(-340)); el_l = (X(-52), Y(-262)); wr_l = (X(-52), Y(-190))
    add('hand-L', 'ellipse', wr_l[0], wr_l[1] + 8 * s, 34, 40, V['skin']); joint('hand-L', 0, -8, wr_l[0], wr_l[1])
    add('forearm-L', 'rectangle', el_l[0], el_l[1] + 36 * s, 30, 86, V['skin'], 15); joint('forearm-L', 0, -36, el_l[0], el_l[1])
    add('arm-L', 'rectangle', sh_l[0], sh_l[1] + 38 * s, 34, 96, V['tunic'], 17); joint('arm-L', 0, -38, sh_l[0], sh_l[1])
    # ---- parenting (children first, then parent to parent) ----
    order += [('hand-R', 'forearm-R'), ('forearm-R', 'arm-R'), ('arm-R', 'torso'),
              ('hand-L', 'forearm-L'), ('forearm-L', 'arm-L'), ('arm-L', 'torso'),
              ('tunic-fringe', 'torso'), ('neck', 'torso'), ('head', 'torso'), ('ear', 'head'), ('nose', 'head'), ('mouth', 'head')]
    order += [(f'hair-{k+1}', 'head') for k in range(5)] + [(f'eye-{sd}', 'head') for sd in 'LR'] + [(f'brow-{sd}', 'head') for sd in 'LR']
    if V['beard']: order.append(('beard', 'head'))
    order.append(('torso', 'ROOT'))
    for c_, p_ in order: parent(c_, p_)
    return ops

if __name__ == '__main__':
    comp, p, x, gy, s = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
    var = sys.argv[6] if len(sys.argv) > 6 else 'main'
    ops = rig(comp, p, x, gy, s, var)
    print(json.dumps(ops, separators=(',', ':')))
    print(len(ops), 'ops', file=sys.stderr)
