# After Effects through the Higgsfield bridge: building a cartoon stage directly in AE

Read this when the user has an After Effects project open and the Higgsfield bridge (the `ae_*` MCP)
is connected, and asks for the explainer to be built **directly in AE**. Reference numbers from one
cartoon-stage explainer build (103 s of VO, 10 stages, 20 jointed characters, 96 PNG assets):
about 67 minutes from the master comp to the last contact sheet, about 100 AE tool calls,
0 Higgsfield credits. The style laws still come from `cartoon-stage.md`; this document is
only about HOW to build it through the bridge.

## What the bridge can and cannot do

| Can | Cannot (and the way out) |
|---|---|
| `ae_build_scene_from_lottie` creates a comp + precomps + simple shape layers at once | A large Lottie (>~60 KB): split it. Use Lottie only for the **skeleton**, fill in through atomic ops |
| `ae_batch` runs dozens of ops (`add_shape_layer`, `add_null_layer`, `import_image`, `modify_layer`, `set_keyframes`, `set_expression`) in one call | `apply_gradient`, `get_layer_info`, `export_frame` inside a batch → the whole batch errors; call them standalone |
| `add_shape_layer` rectangle (with `roundness`) and ellipse, colors `{r,g,b}` 0–1 | Paths/polygons/stars, strokes, gradients on shapes → draw them as SVG outside, render to PNG, import |
| `ae_import_image` PNG/JPG/WAV (WAV gives a harmless "hidden property" warning) | SVG ("invalid file type"); files in a temporary/virtual folder owned by the agent app are often invisible to AE → copy assets to an ordinary folder first (e.g. `C:/ae-assets/`) |
| `ae_apply_gradient` Gradient Ramp 2 stops / 4-Color on a static shape (sky) | A gradient on a keyframed layer; a gradient inside a batch |
| `set_expression` on Position/Scale/Rotation/Opacity/Anchor | Expressions on effect properties or paths; `ae_reorder_layers` is always "layer not found" → **stacking order = creation order**, create from back to front |
| `ae_export_contact_sheet` (5–8 times) and `ae_export_frame` → an r2.dev URL | Viewing the r2.dev URL from Indonesia (blocked) → relay: `media_import_url(url)` in the Higgsfield MCP → `curl https://d2ol7oe51mr4n9.cloudfront.net/<user>/<media_id>.png` → Read. The relay sometimes fails ("Something went wrong"); export again, a new URL usually gets through |
| `ae_get_layer_info`, `ae_list_layers`, `ae_list_compositions` for verifying numbers | Saving the project, rendering, deleting comps. The user must press **Ctrl+S**; MP4 through the Render Queue or `aerender.exe` |

The bridge traps that happen most often:

1. **A new null is born at (960,540).** `add_null_layer` and then parenting right away →
   every child that is not yet keyframed jumps −960,−540. Immediately `modify_layer`
   anchorPoint `[0,0]` + position `[0,0]` on that null BEFORE any parenting.
2. **Parenting to a CAM that is already keyframed** bakes the CAM's transform into the child:
   the position shifts too, the scale shrinks too. After parenting, set the child's
   position/scale again explicitly (or parent first, animate the CAM later).
3. **Keyframes on a parented layer use the parent's space.** An eye inside a head is not
   `[932,472]` (comp) but `[-28,-2]` (relative to the head center). The wrong space = a part
   of the face thrown out of frame.
4. **Partial batches.** If one op fails with `stopOnError:false`, the other ops are still
   applied; read `results[i].ok` one by one, do not repeat the whole batch.
5. **Lottie: child positions are written in comp space**, not relative to the parent; the converter also
   makes a duplicate comp when the name is the same and drops gradients/images/masks/expressions.
   `ip/op/st` on a precomp layer are translated correctly. Use them for the master timing.
6. **A contact sheet inside a precomp that the master zooms looks blurry** → the camera is not on
   the master precomp layer but on the `CAM` null inside each stage.

## A proven architecture

```
# <title>                     master comp 1920×1080 30fps, duration = VO
├─ VO (wav)                   second 0
└─ > P01 … > P10              precomp layers, ip/op from the VO pauses, st = ip (local starts at 0)
     ### P01 <stage name>     precomp, duration = segment + 0.6 s (P04 +8 s when reused as the closing)
     ├─ sky                   a comp-sized rect from the Lottie → ae_apply_gradient
     ├─ CAM                   null, anchor [0,0] pos [0,0]; ALL world layers are parented to it
     ├─ hills, ground, …      2× PNG from SVG, scale 50, anchor from the manifest, pos = comp pivot
     ├─ <character> ROOT + 29 parts   native AE shapes (see the rig)
     └─ dark/morning/fire layers    PNG/rect overlays, made LAST (topmost), opacity keyframed
```

**Camera = the CAM null.** To look at point (x,y) at zoom z:
`CAM.Position = [960 − x·z, 540 − y·z]`, `CAM.Scale = [100z, 100z]`. Keyframe with
`influence` 50–75 for easing. Zoom is never < 1.08 (cartoon stage Law 1).

**A comp reused as another stage** (the closing uses the campfire stage):
a second precomp layer in the master with `st` = ip − local_start_time; the closing
part's animation is placed at that local time (example: 13 s), separated from the first scene by
a double hold keyframe (12.93 → 12.967) so there is no interpolation between scenes.

**A 96 px slide accent** (once, the change of era): Position keyframes on the precomp layers in the
master: P08 960→864 (0.3 s, influence 70→10), P09 1056→960 (0.4 s, influence 10→80);
add Scale 100→111 and 111→100 at the same times so the comp edge is not exposed.

## Workflow

0. The rundown per stage is locked to the VO pauses (`vo-pauses.html` or `ffmpeg silencedetect`),
   plus a camera list per stage `(t, x, y, z)`. The cartoon stage style brief is still required.
1. **The skeleton through one small Lottie**: the master comp + each precomp holding only the
   `sky` layer, precomp layers in the master with `ip/op/st`. Import the VO WAV into the master.
2. **Illustration assets from code** (`scripts/ae/bridge/svg-assets.py`): each asset = one
   drawing function (rect/ellipse/smooth path) in local coordinates with a defined
   pivot; the script writes SVG + a `manifest.json` holding `png, pos, anchor (2× px),
   scale 50`. Render everything with `node scripts/ae/bridge/svg2png.cjs <folder>`
   (puppeteer, a transparent PNG the size of the 2× SVG). Draw to fit the camera zones: what is
   outside a zoom ≥1.08 does not need drawing.
3. **Per stage, one `ae_batch`** in back → front order:
   `add_null_layer CAM` → `modify_layer` CAM anchor/pos 0 → `import_image` + `modify_layer`
   (anchor, position, scale 50, initial opacity) per asset → `modify_layer parentLayerName:"CAM"`
   for all → `set_keyframes` camera & assets → `set_expression` idle motion.
   `ae_apply_gradient` for the sky is called separately BEFORE the batch.
4. **Characters**: `python scripts/ae/bridge/character-rig.py "<comp>" <prefix> <x> <gy> <scale> [variant]`
   prints about 90 ops; add `modify_layer <prefix> ROOT parentLayerName CAM` and set
   ROOT position/scale again (trap 2). Send it as one `ae_batch` per character
   (about 15 KB). Once the rig is built, a second batch holds the pose/action + idle expressions.
5. **Verify each stage** with `ae_export_contact_sheet` at 5–8 key times → relay
   → look. Check: the rig is intact (joints not detached), the background has not shifted (traps 1–2),
   overlays are on top, ≥10 objects moving. Finally a **master** contact sheet at one time
   per stage + the transition times.
6. **Handover**: ask the user to Ctrl+S (the bridge cannot save), delete the test comps,
   render through the Render Queue or
   `"C:/Program Files/Adobe/Adobe After Effects 2026/Support Files/aerender.exe" -project … -comp "# …" -output ….mp4`.
   State the remaining compromises (example: the layer order that cannot be rearranged).

## The native character rig (`character-rig.py`)

A proven pattern: **create the shape at its comp position → `modify_layer` anchor = joint point
(layer coordinates, relative to the shape's center) + position = joint point (comp) → parent**.
"Jump" parenting keeps the appearance, and Rotation turns exactly at the joint.

```
<p> ROOT (null, pelvis = gy − 214s, anchor [50,50])
├─ thigh-L/R (anchor [0,−52s], hip joint ±24s) → calf (knee gy−112s) → foot (ankle gy−16s)
└─ torso (anchor [0,76s], pelvis joint)
   ├─ arm-L/R (shoulder ±52s, gy−340s) → forearm (elbow gy−262s) → hand (wrist gy−190s)
   ├─ tunic-fringe, neck
   └─ head (anchor [0,72s], neck gy−398s)
      └─ ear, hair-1..5, beard (main/member3 variants), eye-L/R, brow-L/R, nose, mouth
```

Creation order = stacking order: back leg (R) → back arm (R) → torso →
head + face → front arm (L). Scale 0.75 (far), 0.85–0.9 (normal stage), 1.15–1.4
(close-up). Skin/tunic/hair variants are in `VAR`; do not add variants named after
real brands/figures.

The expression/action numbers used (all deterministic from `time`):

| Motion | Expression / keyframe |
|---|---|
| Breathing | torso Scale `[value[0], value[1]*(1+Math.sin(time*2.4)*0.015)]` (a different phase per character) |
| Blink | eye Scale `var c=(time+0.4)%3.3; c<0.12?[value[0],value[1]*0.1]:value` |
| Walking (gated) | thigh `value ± sin((time−t0)*11)*24`, calf `max(0, ±sin(…−1))*20`, opposite arm `*18`, ROOT y `−abs(sin)*6`, only inside `t0<time<t1` |
| Jump | ROOT Position 3× (0.25 s down-up 55 px), thigh `−abs(sin(π·2t))*25`, calf `+35` |
| Arc throw | arm Rotation 0 → −20 (wind-up) → 110 (release, influence 30) → 0; the object: 3 Position keyframes (hand → peak → receiving hand) + Rotation 540–720 |
| Waving | arm Rotation −150 ↔ −120 every 0.3 s |
| Hugging/worried | arm-R −35, forearm-R −60, arm-L −70, forearm-L −40; brows ±15; mouth Scale `[70,60]` |
| Startled/happy | mouth Scale `[130,260]` within 0.03 s; eye Position shifted ±10 in head space |
| Sleeping | ROOT Rotation −90 (cut, double hold), eye Scale `[110,12]`, breathing at 1.6 Hz amplitude 0.03 |
| Fire | flame Scale `1+sin(time*13..21)*0.07..0.18`, Rotation `sin(time*8..10)*4..5`; the fire-glow PNG opacity 30, Scale breathing 3 % |
| Fly/star/bush | Position `sin/cos` amplitude 30–80 px; star Opacity `value*(0.85+sin(time*2.3)*0.15)`; bush Rotation `sin(time*1.7)*2` |

## What was compromised in this build (tell the user up front)

- The layer order follows the creation order; an object that must cross IN FRONT of a character
  must be created after the character, or recreated.
- Illustration assets are raster PNGs; changing a color/shape = editing the SVG script, rendering
  again, replacing the footage. Characters stay vector and are fully editable in AE.
- No motion blur, no effects except Gradient Ramp; blur/glow is added by the user in AE.
- Each character = about 15 KB of command text that must be written out in full (the bridge does not read
  op files); 20 characters ≈ 300 KB. That is the biggest time contributor, not the bridge latency
  (average `ae_batch` 6.5 s, contact sheet 12 s, relay 7 s).

## Bridge checklist

- [ ] CAM: anchor `[0,0]`, position `[0,0]` before any child; the camera only on CAM,
      master precomp layers still (except the 96 px slide accent)
- [ ] All world layers parented to CAM; after parenting, asset position/scale are checked
      through `ae_get_layer_info` (ground must be `[0,0]`, scale `[50,50]`)
- [ ] Creation order: sky → far background → ground → props → characters → thrown
      objects → light/night overlays
- [ ] Body-part keyframes in parent space; a double hold (Δ1 frame) for cuts inside a
      reused stage
- [ ] The contact sheet of each stage looked at with the eyes (through the relay if r2 is blocked), then
      the master contact sheet at one time per stage
- [ ] `apply_gradient` / `get_layer_info` / `export_*` are never inside an `ae_batch`
- [ ] Closing message: Ctrl+S, delete the test comp, the `aerender` command, the list of compromises
