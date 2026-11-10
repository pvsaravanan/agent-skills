# Cartoon stage: a flat educational cartoon explainer, one stage per scene

The sixth explainer style. Its reference numbers come from two kinds of video: a cartoon story of about 40 s
with one character in five environments, and an explainer of about 80 s (7 stages, 2 characters,
no captions). Common failures are recorded below because a model easily becomes certain
the result is right.

**Definition.** Every scene is its own *stage* the size of the frame (1920×1080 +
overscan), drawn as vectors, fully alive (≥10 moving objects), with its own camera.
The camera only moves **inside** a stage (zoom 1.08–1.95, never wide).
Between stages: a **cut**, or a 96 px / 72 px slide with blur ≤10 px. The VO carries
the sentences; the pictures carry the meaning; **there are no captions**.

How it differs from the other modes in this skill:

| | Collage cartoon (`starter-explainer-cartoon`) | Cartoon stage (`starter-explainer-stage`) |
|---|---|---|
| World | one big sheet of paper holding still cutouts | many stages, each stage one frame |
| Main motion | the camera travels over still assets | the stage's contents act; the camera accompanies |
| Scene change | camera push-through | cut / 96 px slide |
| Background | cream paper + grain + stains | bright flat, no texture |
| Text | sentence + highlighter pill | zero captions; diegetic labels only |
| Assets | generated illustration → cutout | drawn vectors + a jointed raster head |

## Law 1: One stage per scene, the camera is never wide

The reference project's camera plan: 1.95 → 1.08 · 1.65 → 1.14 → 1.18 · 1.90 → 1.12 → 1.36 ·
1.45 → 1.57 → 1.17. **Not one is below 1.08.** A character in close-up
fills ~55–65 % of the frame height, in wide still ~35 %.

A real failure: the world was built as one giant map (20,000 px) that
the camera explored at zoom 0.2–0.7. Everything moved, but half the video became
a miniature: a house the size of a thumb, 60 % of the screen empty ground. It still felt like
"a slide with a small picture in the middle". The fix is not patching: the world
must be split into stages the size of the frame.

The camera pattern per stage: **hold 0.45–0.7 s → one move per VO beat → hold.**
Legitimate moves: a push-in to an object (1.12 → 1.45), a tilt up to a roof / down to the underground
in a stage deliberately made taller than the frame, following the subject
(a jump: the camera height follows the arc, loose framing in the air). Zoom
is interpolated logarithmically so it feels even.

## Law 2: Continuous inside a stage, cuts between them

A VO sentence changing ≠ the stage changing. As long as the spatial/causal relationship
still helps the viewer, stay on the same stage and change the **action**:
a wall lifts to reveal a shelf, a meter needle rises, a green light turns on,
plants grow in sequence. Change stages only when the location, scale, or way of
explaining really changes. Reference project: 39.6 s = 5 stages; 81 s = 7.

An accented transition only for a genuine change of place (2 of 6
changes in the reference project), the rest direct cuts. Proven numbers:

```
exit    0.28 s  offset = -d · q²        (q = 0→1)
cut
enter   0.42 s  offset = +d · (1-q)³
d = 96 px horizontal or 72 px vertical, blur ≤ 10 px on the container,
WITHOUT a scale bump, WITHOUT extra sweeping lines.
```

The offset is applied to the stage's camera rig, not by sliding a frame that
has already been cropped. Do not fly across the world for 3 seconds (up to the sky, diving
underground, zooming out); that is the tiring pattern "hold → pan far while zooming → cut → repeat".

A cut between stages is **not** a violation of "Structural prohibition #1" in SKILL.md
as long as every stage is alive (its contents act). What is forbidden is a still
picture being faded.

## Law 3: Each stage has ≥10 moving objects

Not decoration: each object explains a place, an activity, or a relationship. Proven
examples: a spinning fan (`t·100°`), a swaying meter needle, a pulsing status light, water drops
crawling **along the pipe path** (parametric
`getPointAtLength`, not dash-offset), river ripples shifting, smoke/steam rising
with keyframed opacity, dust blowing, a bird crossing, laundry swaying,
tree leaves breathing, a chicken walking with moving feet, shelf lights turning on
in sequence then blinking randomly-deterministically, a plant growing then wilting, cracks
spreading (stroke-dashoffset), soil layers piling up, the water level dropping.

Particles: **one motion tween + one keyframed opacity tween**
(`keyframes:{opacity:[0,.9,.9,0]}`), both `repeat:-1`. Two infinite opacity tweens on the same
element overwrite each other, so the steam never appears.

## Law 4: A jointed rig, not a whole picture

A whole picture has no joints. A proven hierarchy (local coordinates, feet at y=0):

```
root (pelvis at 0,-214)
├─ thigh_L/R  translate(±26,-214)   thigh 118 → knee at +102
│  └─ shin     translate(0,102)     calf 108 → ankle at +96
│     └─ foot  translate(0,96)
└─ torso       translate(0,-214)    body -152..+8, neck -178..-138
   ├─ arm_R    translate(50,-126)   upper arm 98 → elbow +78    (drawn BEFORE the body)
   │  └─ fore  translate(0,78)      forearm 90 → wrist +74
   │     └─ hand translate(0,74)
   ├─ arm_L    (the same, -50; drawn AFTER the body)
   └─ head     translate(0,-160)    chin at the neck joint, 14 px overlap onto the neck
```

An idle that makes a character alive without "doing" anything:
body `±1.1° / 1.7 s`, head `±1.7° / 2.3 s`, arms `±1–1.5° / 1.9 s`,
**a blink every ≈3.5 s for 0.13 s** (offset per character so they are not in unison).
Walking: `step = sin(t·8)`; thigh `step·15°`, calf `max(0,step)·18°`, the body
bobbing `|step|·3–4 px`, **the ellipse shadow at the feet shifts too**. Jump: thigh,
calf, arms, shadow (shrinking in the air) are all functions of one `jump(t)` curve.
A small action in each sentence: pointing (upper arm 6° → -72° in 0.7 s),
waving, drawing water (arm -62°/-10° yoyo 0.42 s + a crank `+=180°`), fanning the
face (forearm -40° ↔ -70°, 0.35 s).

Expression = swapping the head picture (happy / worried / startled), not a morph. A blink =
a second head picture with closed eyes, opacity 0 → 1 → 0.

Foot shadow: an ellipse `rx ≈ 72·scale, ry 16, opacity .13`, drawn **before** the
character, moving along when walking.

## Law 5: Transforms are written manually; GSAP must not touch joints

The two traps that happen most often:

1. **GSAP `transformOrigin` on SVG is relative to the bounding box**, and a group's
   bbox changes when its children move. As a result shoulders, neck, fan shaft, chicken feet
   all rotate around a shifting point: the head looks detached, the propeller
   floats out of its shaft, the feet are left behind the body.
2. **A GSAP `x`/`y` tween on a group that already has a `translate(...)` overwrites that
   translate** (an absolute value, not an addition). The power pole vanishes, the cloud
   never moves.

The solution (a null-per-joint pattern): every joint has a proxy `{tx,ty,x,y,r,sx,sy}` and the
`transform` attribute is written by yourself:

```js
function J(el,tx=0,ty=0){const j={el,tx,ty,x:0,y:0,r:0,sx:1,sy:1,
  apply(){el.setAttribute('transform',
    `translate(${j.tx+j.x},${j.ty+j.y}) rotate(${j.r}) scale(${j.sx},${j.sy})`);}};
  j.apply();return j;}
tl.to(j,{r:-62,duration:.42,onUpdate:j.apply},at);     // the pivot = the local origin point
```

The derived rule: the **placement** group (`translate`) and the **animated**
group are always two different elements. GSAP may touch `opacity`, `attr`, and
`x/y` directly on elements **without** a transform (rect/circle
with `x/cx`), or `scaleX/scaleY` on a single element (whose bbox stays fixed).

## Law 6: Zero captions, text only diegetic

The reference project has not a single sentence on screen. The text that exists is part of
the world: an "AIRLOCK" sign, an "O2" tank, a "DATA CENTER" plate, a "FOR SALE" board. VO
sentences are not rewritten on screen; if the viewer needs to read, the picture
has not explained yet. The highlighted sentence + highlighter pill belong to collage mode, not
this mode.

## Law 7: A bright flat palette; not paper, not grain

Cream paper + grain + water stains are the skin of the *collage cartoon*; in this mode
they look vintage and wrong. What has been proven: a pale gradient sky
(`#BFDDE3 → #F6EFDD` or `#EDB095 → #F8D8AD`), ground `#D88560`/`#E6D5AC`, cream
`#FFF3DC`, navy `#345867`, teal `#237C80`, mint `#8DD3C3`, gold `#F4BC52`, coral
`#E0714F`. Flat fills, no outlines, no texture, no vignette. Shadows are only the
contact ellipse on the ground and the dark side of buildings at 0.86–0.9× the base color. Choosing a palette
from the theme still applies (Law #3 of SKILL.md); only **no texture** is locked here.

## Characters: a raster head + a vector body

A proven pipeline (the identity may come from the user's photo, or be anonymous):

1. **Generate only the HEAD** (one image, transparent background). A prompt that
   worked (without naming any brand):
   > ONE isolated front-facing cartoon HEAD, centered, generous margin. No body,
   > no neck below the jaw, no shoulders, no text. VERY MINIMAL flat 2D
   > educational-cartoon style: broad softly rounded head, simple small ears,
   > hair as ONE solid silhouette (no strands, no highlights), eyes ONLY TWO
   > SMALL SOLID BLACK DOTS (no sclera, iris, highlights, eyelids), two tiny
   > eyebrow strokes, nose omitted, mouth a tiny curved smile line. Flat fills,
   > ~3 colors, no gradients, no outlines, no shading. A clean silhouette for a
   > cutout animation puppet.
   Add identity traits (skin tone, hairstyle, glasses, a plain single-color
   headscarf) as a separate sentence.
2. **Expressions & blinks are made locally**: `scripts/head-expressions.py` detects the two
   pupils (nearly square dark components in the middle of the face) and the mouth (a
   wide-thin component below them), then redraws: blink = a skin-colored ellipse + a
   curved line; worried = a concave mouth; startled = a circle. It produces
   `<name>-{happy,worried,startled}[-blink].png` + `head-meta.json` (bbox, pupils,
   skin color). There is no regenerating for expressions.
3. **The body is drawn as vectors** with the Law 4 hierarchy; the head is attached at the neck
   joint with an `<image>` whose chin (the bottom of the bbox) sits exactly at (0,0) and overlaps
   14 px onto the neck. Head width ≈ 150 px on a body 130 px wide.
4. All costume variations (shirt, trousers, dress) go through the colors & body path; the same
   head is reused. The approved master is frozen.

Without generation access: `character()` in the starter has a simple vector head
(a skin circle, a hair silhouette, two eye dots, a mouth line), enough for
this style.

## Stages that have proven themselves for "process & impact" stories

A house page (a character + a phone, a response bubble, a flying signal) · the exterior of a
big machine (push-in → wall lifts → the inside lights up → tilt up to the roof) · a riverside factory
(two flow directions + a circular arrow) · a tower & the sky (a tall stage:
a tilt following steam to the clouds, rain, wind) · a well & a soil cross-section (the surface
at y≈520, layers piling up, an aquifer, a labeled suction pipe) · dry land &
drought (the sun rising, cracks, wilting plants, a character fanning) · a map of rice paddy plots
(a grid filling with water in sequence, a rain band shifting) · back to the earlier
stage with the camera closer as the closing.

A character's height scale ≈ 520 px at scale 1 (head 186 + body). A stage
with an underground: character height 0.85 and layers ≤ 440 px so the head and the
aquifer fit one frame at zoom 1.08.

## Verification

Capture 20–24 key seconds (`scripts/snap.mjs`) → a 4-column contact sheet, then
judge with the eyes: **is there a wide frame?** head/tower clipped? a character
"detached" at a joint? an object that should appear missing (a sign of a tween overwriting
a translate)? For continuous sequences, render an 8 fps GIF of one full stage,
not a montage, to prove there is no break. Besides that, check mechanically:
`grep` finds no `transformOrigin:'0px 0px'` / `rotation:` on joints, and no
`tl.to(<translated group>,{x|y})`.
