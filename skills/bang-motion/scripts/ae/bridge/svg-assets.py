"""Cartoon stage illustration assets → SVG (vectors from code) → a placement manifest for the AE bridge.
Flow: write a drawing function per asset → run this script → `node svg2png.cjs assets` (transparent 2× PNG)
→ in AE via the bridge: import_image the PNG, modify_layer anchor=manifest.anchor, position=manifest.pos,
scale=50, parentLayerName="CAM". Characters are NOT here — they are built natively via character-rig.py.

usage: python svg-assets.py          → writes assets/*.svg + manifest.json (the sample stage below)
Replace/fill the "# ---- assets ----" section with your project's stage; the palette comes from the style brief.
"""
import json, os, math

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'assets'); os.makedirs(OUT, exist_ok=True)
PX = 2  # render density: 2× PNG, placed in AE at 50 % scale

# Sample palette (cartoon stage: bright flat, no texture). Replace from the project's style brief.
PAL = dict(sky1='#CFE6E4', sky2='#FBF1DC', ochre='#D9A066', ochre2='#B97F4A', stone='#9C9186', stone2='#7D736A',
           grass='#9DB874', grass2='#7FA65E', fire='#C8553D', fire2='#F2C46D', ink='#2F4858', wood='#8A6A4A',
           cream='#FBF1DC', water='#5AABB8', water2='#9ED6DD', night='#34505E')
C = PAL

class Shapes:
    """A collection of shapes in local coordinates; (0,0) = the asset pivot. All chainable (return self)."""
    def __init__(s): s.items = []; s.minx = s.miny = 1e9; s.maxx = s.maxy = -1e9
    def _box(s, pts):
        for x, y in pts:
            s.minx = min(s.minx, x); s.miny = min(s.miny, y); s.maxx = max(s.maxx, x); s.maxy = max(s.maxy, y)
    def rc(s, x, y, w, h, c, r=0, rot=0):
        a = math.radians(rot); ca, sa = math.cos(a), math.sin(a)
        s._box([(x + dx * ca - dy * sa, y + dx * sa + dy * ca) for dx in (-w / 2, w / 2) for dy in (-h / 2, h / 2)])
        s.items.append(f'<rect x="{-w/2:.1f}" y="{-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r:.1f}" '
                       f'fill="{C.get(c, c)}" transform="translate({x:.1f} {y:.1f}) rotate({rot})"/>')
        return s
    def el(s, x, y, w, h, c):
        s._box([(x - w / 2, y - h / 2), (x + w / 2, y + h / 2)])
        s.items.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{w/2:.1f}" ry="{h/2:.1f}" fill="{C.get(c, c)}"/>'); return s
    def pth(s, pts, c, smooth=0.0):
        """Closed polygon; smooth 0 = sharp corners, 0.3–0.5 = rounded hills/rocks (Catmull-Rom → bezier)."""
        n = len(pts); T = []
        for k in range(n):
            a, b = pts[(k - 1) % n], pts[(k + 1) % n]
            T.append(((b[0] - a[0]) * smooth / 2, (b[1] - a[1]) * smooth / 2))
        d = f'M{pts[0][0]:.1f} {pts[0][1]:.1f}'
        for k in range(n):
            p0, p1 = pts[k], pts[(k + 1) % n]
            c1 = (p0[0] + T[k][0], p0[1] + T[k][1]); c2 = (p1[0] - T[(k + 1) % n][0], p1[1] - T[(k + 1) % n][1])
            d += f' C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p1[0]:.1f} {p1[1]:.1f}'
            s._box([c1, c2, p1])
        s.items.append(f'<path d="{d} Z" fill="{C.get(c, c)}"/>'); return s

MAN = {}
def asset(stage, name, build, pivot=(0, 0)):
    """build(sh) draws in local coordinates with (0,0) = the pivot; pivot = the position in the stage comp (1920×1080).
    Manifest: png, pos (= pivot, comp), anchor (2× source px), scale 50 — used directly by modify_layer."""
    sh = Shapes(); build(sh); m = 6
    x0, y0 = math.floor(sh.minx - m), math.floor(sh.miny - m); w, h = math.ceil(sh.maxx + m) - x0, math.ceil(sh.maxy + m) - y0
    fn = f"{stage.split()[0]}_{name.replace(' ', '-')}.svg"
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{w*PX}" height="{h*PX}" viewBox="{x0} {y0} {w} {h}">' + ''.join(sh.items) + '</svg>'
    open(os.path.join(OUT, fn), 'w', encoding='utf-8').write(svg)
    MAN.setdefault(stage, []).append(dict(name=name, svg=fn, png=fn.replace('.svg', '.png'), w=w * PX, h=h * PX,
                                            pos=[round(pivot[0], 1), round(pivot[1], 1)], anchor=[-x0 * PX, -y0 * PX], scale=100 / PX))

# ---- frequently used pieces (comp coordinates; background asset pivot = (0,0)) ----
def hill(sh, base, c='grass'):
    sh.pth([(-400, base + 460), (-400, base), (100, base - 120), (520, base - 40), (900, base - 190), (1350, base - 70),
            (1760, base - 160), (2320, base - 30), (2320, base + 460)], c, 0.4)
def ground(sh, gy, c='ochre', rim='grass2'):
    sh.rc(960, gy + 300, 2700, 600, c).rc(960, gy + 8, 2700, 22, rim)
def rock(sh, x, y, s=1.0, c='stone'):
    sh.pth([(x - 90 * s, y), (x - 70 * s, y - 55 * s), (x - 10 * s, y - 80 * s), (x + 60 * s, y - 60 * s), (x + 95 * s, y)], c, 0.5)
def tree(sh, x, gy, s=1.0):
    sh.rc(x, gy - 90 * s, 34 * s, 190 * s, 'wood', 10 * s).el(x - 60 * s, gy - 230 * s, 150 * s, 130 * s, 'grass2') \
      .el(x + 55 * s, gy - 240 * s, 140 * s, 125 * s, 'grass2').el(x, gy - 300 * s, 170 * s, 150 * s, 'grass')
def fire_layers(P, x, gy):
    """Campfire = logs + 3 separate flames (so each flame can be scaled/rotated on its own via expressions)."""
    asset(P, 'fire logs', lambda sh: sh.rc(-60, 0, 150, 18, 'wood', 8, -12).rc(60, 0, 150, 18, 'wood', 8, 12), (x, gy))
    for k, (dx, w, h) in enumerate([(-28, 70, 170), (26, 60, 140), (0, 46, 100)]):
        asset(P, f'fire flame {k+1}', lambda sh, w=w, h=h: sh.el(0, -h / 2, w, h, 'fire' if h > 120 else 'fire2'), (x + dx, gy - 22))

# ---- assets (a SAMPLE single stage; replace with your project's stage) ----
P = 'P01 sample'; gy = 860
asset(P, 'far hill', lambda sh: hill(sh, 700))
asset(P, 'ground', lambda sh: ground(sh, gy))
asset(P, 'tree', lambda sh: tree(sh, 0, 0, 1.1), (1500, gy))
asset(P, 'sitting rock', lambda sh: rock(sh, 0, 0, .9, 'stone2'), (560, gy + 20))
fire_layers(P, 960, gy + 20)
asset(P, 'fire glow', lambda sh: sh.el(0, 0, 900, 520, 'fire2'), (960, gy - 60))   # in AE: opacity 30, created before the characters

json.dump(MAN, open(os.path.join(HERE, 'manifest.json'), 'w', encoding='utf-8'), indent=1)
print(sum(len(v) for v in MAN.values()), 'assets in', len(MAN), 'stages ->', OUT)
