# Techniques: tested effect recipes

All recipes are stated generically; the numbers are starting points that have proven
pleasant, not laws. Fonts, colors, and content always belong to the user's brand.

## Table of contents

1. Alive typography (per-letter split, optional emphasis & highlight, alternating direction) + 1b. Background contrast
2. Directional motion blur (the main difference from "web animation")
3. Camera: push-through (optional, motivated)
3b. Shot size: the camera moves to an element (wide ↔ medium close-up ↔ close-up)
4. Camera: a 3D pan along a sentence, word by word
4b. Transitions between scenes: the right hierarchy
5. Light leak transition
6. The right glow (and when not to)
7. Three.js backgrounds: nebula, dust, grid, 3D ornaments, bloom
7b–7d. Light backgrounds & changes, background motion, background surfaces (including grainy gradient)
7e. Object render style menu (flat, clay, glossy, glass, isometric, gold, neon line)
8. Icon tiles & UI mockups
9. Deterministic typing / living numbers
9b. Video as footage layers (clip, timeline sync, export)
10. Traps (bugs that have happened)

---

## 1. Alive typography: recipes that worked vs failed

Two patterns that show up often. Opener A feels stiff: every
title is ALL CAPS, one wide font weight 800, always centered, entering
with the same letter stagger, with no emphasis of any kind, with no size variation.
Opener B feels alive: sentence-case sentences at weight 500, ONE keyword
per sentence in a pill that expands from the left + a sparkle, punctuation
appearing separately afterwards, size and entry direction alternating every scene,
some sentences placed near their object (not always centered), and
dark scenes alternating with light scenes. Recipe B:

> **A warning about the shape.** In opener B, the highlight was a blue pill that
> expands from the left with a small star (sparkle) at its corner. That is that project's
> SIGNATURE, not a rule. The only rule is: a sentence
> has emphasis. A word highlight is ONE way and OPTIONAL; many good openers have
> no highlight at all (word by word dim → full, size,
> pauses, an icon/UI beside the word). When used, the SHAPE is chosen in the style brief
> and consistent within one video, not required on every sentence; the ORNAMENT
> (a star, a dot, a lightning line) is optional and derived from a brand shape.
> Two different projects with the same pill + star = copying the skin.

**Emphasis menu** (pick one per video; `none` is a legitimate choice):

| Variant | Feel | Good for |
|---|---|---|
| `none`: no field/line; word by word dim → full, size, pauses, or an icon/UI beside the word | calm, a product that speaks | SaaS, AI, minimal brands, feature announcements |
| `pill`: a color block expanding from the left | firm, digital product | app, SaaS, tech |
| `under`: a thick underline drawing from the left | editorial, calm | finance, productivity, journalistic |
| `marker`: a tilted highlighter scribble, slightly transparent | warm, human | education, community, food |
| `box`: a thin-line box drawing around | technical, precise | developer tools, hardware |
| `color`: only the word's color changes, no field | luxury, minimal | fashion, property, automotive |
| `strike`: a strikethrough line then the replacement word appears | ironic, before/after | "not X, but Y" promos |

**CSS**
```css
.line{font-size:112px;font-weight:500;letter-spacing:-.015em;color:#fff;white-space:nowrap;
  text-shadow:0 4px 28px rgba(0,0,0,.5);line-height:1.1;opacity:0}
.line.sm{font-size:74px}.line.md{font-size:92px}.line.lg{font-size:128px}
.line.xl{font-size:150px;font-weight:600;letter-spacing:-.02em}
.line.ink{color:var(--ink-dark);text-shadow:none}          /* the version for light scenes */
.wd{display:inline-block;white-space:nowrap}
.ch{display:inline-block;will-change:transform,opacity,filter;opacity:0}
.txt2{display:inline-block;opacity:0}                        /* OPTIONAL punctuation: only when the sentence really has punctuation */
/* highlight word: .hl + one shape variant; <i> is the field/line being drawn */
.hl{position:relative;display:inline-block}
.hl i{position:absolute;transform:scaleX(0);transform-origin:0 50%}
.hl-t{position:relative;opacity:0}
.hl.pill{padding:.02em .24em .04em;border-radius:.26em}
.hl.pill i{inset:0;border-radius:inherit;background:linear-gradient(95deg,color-mix(in srgb,var(--accent) 70%,#000),var(--accent) 60%,var(--accent-lit))}
.hl.pill .hl-t{color:#fff}
.hl.under i{left:0;right:0;bottom:-.04em;height:.14em;border-radius:.07em;background:var(--accent)}
.hl.marker i{left:-.1em;right:-.1em;top:.5em;bottom:-.02em;background:var(--accent);opacity:.55;transform:scaleX(0) rotate(-1.5deg)}
.hl.box i{inset:-.06em -.14em;border:.04em solid var(--accent);border-radius:.12em;background:none}
.hl.color .hl-t{color:var(--accent)}      /* no <i> */
/* OPTIONAL ornament: only when the brand shape asks for it; replace the path with the brand shape */
.hl-orn{position:absolute;width:.46em;height:.46em;right:-.22em;top:-.24em;fill:var(--accent-lit);opacity:0}
```

**Markup**: only `.txt` is split per letter; the highlight and punctuation
have their own tweens (an example of the `under` variant, with no ornament):
```html
<h1 class="line md"><span class="txt">Tired of typing</span>&nbsp;<span class="hl under" id="hl-a"><i></i><span class="hl-t">captions</span></span>&nbsp;<span class="txt">one by one</span><span class="txt2">?</span></h1>
```

**JS**: four entry/exit doors + pill + punctuation:
```js
const inUp  =(ch,el,at,{dur=.8,st=.024}={})=>{tl.fromTo(ch,{opacity:0,yPercent:60,scaleY:1.45},{opacity:1,yPercent:0,scaleY:1,duration:dur,ease:'power4.out',stagger:st,immediateRender:false},at);blurTween(tl,el,at,30,0,dur,VERT);};
const inLeft=(ch,el,at,{dur=.75,st=.02}={})=>{tl.fromTo(ch,{opacity:0,xPercent:-45},{opacity:1,xPercent:0,duration:dur,ease:'power4.out',stagger:st,immediateRender:false},at);blurTween(tl,el,at,50,0,dur,{ease:'power4.out'});};
const outUp =(ch,el,at,{dur=.4,st=.01}={})=>{tl.to(ch,{opacity:0,yPercent:-70,duration:dur,ease:'power2.in',stagger:st},at);blurTween(tl,el,at,0,45,dur+.1,{ease:'power2.in',...VERT});};
const outLeft=(ch,el,at,{dur=.4,st=.01}={})=>{tl.to(ch,{opacity:0,xPercent:-60,duration:dur,ease:'power2.in',stagger:st},at);blurTween(tl,el,at,0,55,dur+.1,{ease:'power2.in'});};
/* mark(): draws any highlight field/line whatever the shape variant, then reveals the word; the ornament only if present */
const mark=(hl,at)=>{const i=$('i',hl);if(i)tl.fromTo(i,{scaleX:0},{scaleX:1,duration:.5,ease:'power3.out',immediateRender:false},at);
  tl.fromTo($('.hl-t',hl),{opacity:0,yPercent:60},{opacity:1,yPercent:0,duration:.7,ease:'power4.out',immediateRender:false},at);
  const orn=$('.hl-orn',hl);if(orn)tl.fromTo(orn,{opacity:0,scale:.2,rotate:-40},{opacity:1,scale:1,rotate:0,duration:.5,ease:'back.out(2)',immediateRender:false},at+.22);};
const popDot=(el,at)=>tl.fromTo(el,{opacity:0,yPercent:60},{opacity:1,yPercent:0,duration:.5,ease:'power4.out',immediateRender:false},at);
```
The order of one sentence with a highlight: `inUp(ch)` → 0.4–0.6 s later `mark(hl)` →
`popDot(txt2)` 0.25 s after that, ONLY when the sentence really has punctuation. Without
a highlight: the text door only (e.g. per word or dim → full); remove the `.hl` span, and remove
`.txt2` when the sentence has no punctuation (the default for titles and claims).

**Hard typography rules (from failure A):**
1. Sentence case, weight 500–600. ALL CAPS + weight 800 + a wide font
   only for ONE emphasis scene, not all of them.
2. A word highlight is OPTIONAL, decided in the style brief, not a default. If
   used: a shape from the menu above, one shape per video, not required on
   every sentence, different from the previous project; the ornament is not a default.
   If not: emphasis from word order, size/weight, dim → full, pauses,
   or an object beside the word. What stays rejected is a flat sentence with no
   emphasis of any kind.
3. Two scenes in a row must not be the same in: size (sm/md/lg/xl),
   entry direction (inUp/inLeft), position (center / near the object / top-left).
4. A long sentence is split into two lines with different weights (500 then 600),
   or the second line becomes a `.txt2` that pops in afterwards.
5. Titles, claims, and short phrases are DEFAULT NO PERIOD (especially ≤ 4 words or one
   line). Punctuation only when it changes meaning or rhythm: `?` for a real
   question, a period for a deliberate style of two short sentences in a row, `!`
   very rarely. The style is decided once in the style brief and kept consistent. When used,
   punctuation is a separate element that appears last (`.txt2` + `popDot`), but
   do not add a period just because the recipe has `popDot`.
6. Text attached to an object (a mockup, a card) is positioned beside it
   (`.pos` + left/top), not forced to the center over the object.

## 1b. Contrast: the background yields to the text

An example failure: 96 white light bars with additive bloom brighter
than the title → the white letters lose their edges and the background feels
busy with no contrast. Rules that can be measured:
- **The text pocket**: in the text area, background luminance ≤ 25 % (dark) for
  white text, or ≥ 80 % (light) for ink text. If the background is busy,
  put a `.pocket` (a dark radial-gradient 55 % → transparent) under the
  text and turn it on together with the text.
- **Any background element (particles, shapes, textures, lines)**: colors taken from the DARK side of the
  palette (not white), opacity ≤ .35 inside the text pocket, the number of visible bright
  elements ≤ 40, small in size. A high bloom threshold (≥ .55) and only
  for objects, not the background layer.
- **A quick test**: capture a frame when the title is full, convert to grayscale; if
  any part of the background is as bright as the letters, the background is too busy. If all text
  is hidden the background should feel CALM, not "interesting".
- **A dark–light rhythm**: alternate dark and light scenes (e.g. a light "paper"
  card with ink text); contrast between scenes is stronger than
  any effect inside a scene.

## 2. Directional motion blur: SVG `feGaussianBlur`

CSS `filter: blur()` blurs in all directions → it looks "out of focus".
AE's motion blur blurs ALONG the direction of movement. `feGaussianBlur` accepts a separate
`stdDeviation="x y"`:

```js
// make the <filter> once per tween, widen its box (the default clips the tail)
f.setAttribute('x','-70%'); f.setAttribute('y','-70%');
f.setAttribute('width','240%'); f.setAttribute('height','240%');
// tween the value 30→0 on entry, 0→50 on exit; the axis follows the direction of movement
blur.setAttribute('stdDeviation', `${v} ${v*0.08}`);   // horizontal movement
```

Attach the filter when the tween starts, REMOVE it when done (`filter:'none'`):
an element that keeps an SVG filter is re-rasterized every frame, which is expensive.

## 3. Camera: push-through (optional, motivated)

One of the transitions from the §4c menu: a quota of ±1 per video, only when there is a reason
(§4b), not a transition between all segments. Three steps on the `#world` rig (the whole world):

```js
const camThrough = (atCut, {push=2.0, from=1.5, inDur=.5, outDur=.95,
                            oOut='50% 50%', oIn='50% 50%'} = {}) => {
  tl.set(rig, {transformOrigin:oOut}, atCut-inDur);
  tl.to (rig, {scale:push, duration:inDur, ease:'power2.in'}, atCut-inDur);
  tl.set(rig, {transformOrigin:oIn, scale:from}, atCut);
  tl.to (rig, {scale:1, duration:outDur, ease:'power3.out'}, atCut);
};
```

- Push IN to the text that is leaving (`power2.in` = getting faster), cut,
  pull BACK from the new text born oversized (`power3.out`).
- The scale jump at the cut point is NOT visible because it happens while the frame is
  empty / covered by a light leak: deliberate, this is a film technique.
- `transformOrigin` points at the TEXT POSITION (the center for a hero; ~'50% 22%'
  for scenes whose text is at the top): the zoom must head toward the subject.
- Syncing with the WebGL camera (`camZ`) adds depth, but it is the DOM rig
  that carries the "camera" feeling.

## 3b. Shot size: the camera moves to an element (so it is not static)

"Zoom in-out" in motion graphics means a **change of shot size**: the camera moves in to
one element that is telling the story, then pulls back. A camera breath of a few percent (§4b)
is nearly invisible; it is a base layer, not the answer when a video feels static.

**Shot vocabulary** (the scale is computed from the element's size, not a fixed number)
- **Wide**: the whole composition is visible; used when many elements or wide text need
  reading together.
- **Medium close-up**: the main element with a little of its context; the target fills roughly
  a third to a half of the frame.
- **Close-up**: one element or its detail fills most of the frame; used for
  emphasis, an action moment, or a small detail that must be readable.

**Choosing the target and timing**
- The focus point = the center of the element that is *currently* telling the story: text that has just
  appeared, an object arriving, a button being clicked, a detail named by the sentence. The camera welcomes, it does not chase.
- Shots change following the beat of the content. A common pattern: close to element A → pull back to wide
  when the composition needs the whole frame → close to element B. Vary the size; two shots
  of the same size in a row feel flat.
- Two motion tempos: **a shot change** (brief, ease in-out) and **a slow push while
  holding** (slow, sine ease) so the hold is not dead.
- At a cut point, the camera may be directly in a close-up with no tween: the scene is born close,
  then pulls back. The video may even open already in a close-up.
- A held closing (logo, CTA) still gets a slow push; do not freeze.
- Avoid flipping between near and far faster than the reader has time to read or
  look; it is dizzying. Text appears after the camera arrives, not in the middle of a move.

**The rig**
```js
const CAM = {s:1, fx:W/2, fy:H/2};                       // scale + focus point (world coordinates)
const shot  = (at, dur, s, fx, fy, ease='power2.inOut') => tl.to(CAM, {s, fx, fy, duration:dur, ease}, at);
const cutTo = (at, s, fx, fy) => tl.set(CAM, {s, fx, fy}, at);   // jump at a cut point
// size from the element: fill ≈ the part of the frame the target fills (close-up large, medium close-up medium)
const rectIn = (el, root) => { let x = 0, y = 0, n = el;
  while (n && n !== root) { x += n.offsetLeft; y += n.offsetTop; n = n.offsetParent; }
  return {x, y, w: el.offsetWidth, h: el.offsetHeight}; };          // SVG elements: use getBBox()
const frameOn = (el, fill) => { const r = rectIn(el, world);
  return [Math.max(1, Math.min(W * fill / r.w, H * fill / r.h)), r.x + r.w / 2, r.y + r.h / 2]; };
// in render(t):
function applyCam(t){
  const s = CAM.s * (1 + .01 * Math.sin(t * .7));                  // a gentle breath over the shot (optional)
  let tx = W/2 - CAM.fx * s, ty = H/2 - CAM.fy * s;
  tx = Math.min(0, Math.max(W - W * s, tx)); ty = Math.min(0, Math.max(H - H * s, ty));   // the world edge is not exposed
  world.style.transform = `translate(${tx}px,${ty}px) scale(${s})`; }
// example: shot(T, .8, ...frameOn($('#title'), .6)); shot(T + 2, .7, 1, W/2, H/2);
```
- One scale system per wrapper: if a scene uses `shot()`, do not also tween
  `scale` on `#world` from `breathe()`/push-through; stack the breath inside `applyCam`.
  The explainer starter already has its equivalents: `look()` = a shot to a point, `home()` = wide.
- The world/background must be larger than the frame (overscan) so edge clamping does not lock the shot.

**Layers**
- Elements that are part of the world zoom along. Labels, captions, and on-screen interfaces
  sit on a screen layer (HUD) outside the rig so they do not grow or get clipped by the edge.
- A local camera may be set per act (e.g. moving in to a click area, or a reveal
  pulled back from a large scale) without disturbing the world camera. Impact shake on
  a separate wrapper.

**Check**
- Capture at the peak of each shot: text is not clipped by the edge, the world edge is not exposed.
- Raster assets are sharp enough for the close-up scale (resolution ≥ scale × display size).

## 4. A 3D pan along a sentence

For 1 (max 2) special segments: a sentence WIDER than the frame,
the camera travels along it, each word waking as it is passed.

```js
// x puts the pivot at the center of the frame; xPercent (relative to the sentence width)
// carries the camera, independent of the actual font width
tl.set(line, {x:W/2, xPercent:-6, rotateY:10});          // parent: perspective
tl.to (line, {xPercent:-94, duration:2.9, ease:'power1.inOut'});
tl.to (line, {rotateY:-10,  duration:2.9, ease:'power1.inOut'});
// words: dim → bright as the camera passes
tl.fromTo(words, {opacity:.2, yPercent:16, scale:.96},
  {opacity:1, yPercent:0, scale:1, duration:.55, ease:'power2.out',
   stagger: panDur/(nWords-1) * 0.95});
```

The key to the feel: words AHEAD of the camera are dim (~20%) and waiting, words already
passed stay bright; `rotateY` swings (not static) so it feels like a curved
dolly; the WebGL camera shifts `camX` in the same direction for background parallax.

## 4b. Transitions between scenes: the right hierarchy

Two kinds of transition that feel cheap: a translational whip (exposes a black
gap, reads as "turning the page"), and a sudden spin/yaw/roll (a sudden zoom +
blur is the language of video editor presets, not motion design). The right order:

1. **A breathing camera** (the foundation, always on): the world rig drifts a slow zoom
   `sine.inOut` ±4–5% per scene, alternating direction, chained with no jumps.
   The camera is never still and never jolts. This breath is only a base
   layer; it does not read as a "zoom in-out"; for that use shot size (§3b).
2. **Overlapping element choreography**: the old scene's elements exit (fast,
   `power2.in`, directional blur) WHILE the new scene's elements enter; the time
   overlap is what makes the change feel alive, not a camera effect.
3. **Object wipe**: an ornament (a star/brand shape) sweeps NEAR the lens and
   covers the frame exactly at the cut point; the scene changes behind it. Recipe:
   position z ≈ (camZ - 3), world scale ~2× the frame height at that distance,
   a diagonal `power1.inOut` path ~1 second, the scale peak exactly at the cut,
   direction alternating between uses. Beware an old tween still writing the
   same ornament properties; it kills the wipe (check the time overlap).
4. **A motivated zoom**: push-through as a TRANSITION (a quota of ±1 per video) ONLY
   when there is a reason: diving into a mockup screen, entering a logo hole. An
   unmotivated zoom feels like a jolt effect. This quota is specifically for transition zooms: a camera
   that moves in to the UI area being clicked and then pulls back is demo language, not a
   jolt effect, and does not count against the quota (§8 "The camera follows UI interaction").

An element-driven exit is still a good recipe: the old elements fly PAST the lens
(scale ~2.2 + blur + stagger), the camera just follows gently (no jumps).

### 4c. The transition menu: not a square block sweeping

A common failure: an "object wipe" in the form of a giant flat-color block
crossing diagonally feels odd and cheap, and is easily repeated if an example mentions
the object wipe first. An opener that worked uses depth: a 3D push-through, a glass card spinning in, a tile
that `rotateY`s from depth, an element passing the lens with thickness.
Pick from this menu; within one video at least TWO kinds, at least ONE
with depth (3D/perspective), and wipes at most twice:

| # | Transition | How | Feel |
|---|---|---|---|
| 1 | 3D push-through | `camThrough` + layers with different `translateZ` (perspective 1400px) so the front layers pass faster | diving into a world |
| 2 | A card/object spinning in (`rotateY` −35° → 0, `perspective`) | the next object arrives from depth while spinning, the old one leaves the opposite way | premium, tactile |
| 3 | An object passing the lens with THICKNESS | an extruded logo/glass card/3D tile (not a flat square) grows 1 → 2.5×, directional blur, the frame covered briefly | cinematic |
| 4 | A light sweep (light leak / bloom through) | light covers 40–60 % of the frame at the cut point, not 100 % | soft |
| 5 | A mask reveal through a brand shape | the new scene is seen through a hole shaped like the logo/letters that grows (`clip-path`/`mask`) | strong brand |
| 6 | A whip with directional blur | the world shifts 120–200 px + 18 px blur, 0.3 s, in a changing direction | energetic |
| 7 | Rack focus / depth | the old scene is blurred & shrunk to the back, the new scene is sharp from the front | narrative |
| 8 | Overlapping choreography with no cut | the old elements exit fast while the new elements have already entered; the camera keeps breathing | flowing |
| 9 | Swapping the background behind #1–#5 | a dark↔light/color-block change happens while the frame is covered | a new segment |

Rejected as defaults: a flat-color square/block sweeping the full
frame, a thin line sweeping, and one kind of transition repeated on all
cuts. A wipe is allowed only when its object has meaning and depth (a glass
card, an extruded logo, a tile), not a flat field.

Transitions with no cut that are carried by an object (the new scene's object becomes the wipe, exits the
screen, a shape match cut + a render-style change, a pull back revealing the destination, a hand
that picks up, passing through a symbol, a pushing parade, a thin spin → a color card opening,
pages rising stacked, a dot growing, a container blooming/shrinking, a result moving away into a
sentence, a zoom into a UI piece, dimming then switching, delete-typing) are in `opener-concepts.md` → "The menu of transitions
carried by objects". A palette color field that BECOMES the next act's background (the logo stays in
place and flips color at the field line) is not a decorative block passing by: allowed,
at most twice per video.

## 5. The light leak transition

Not a line of light sweeping (it looks cheap), but a soft ball of light
seeping in from the edge, alternating left/right:

- a round div ±2400px, a radial-gradient bright core → transparent, `blur(64px)`,
  `mix-blend-mode:screen`, **on the TOPMOST layer** (above the vignette;
  it is light in front of the lens, not a world property)
- enters `sine.in` 40% of the duration → exits `sine.out` 60%; a slow diagonal drift
- tint it to match the brand accent

## 6. The right glow

An expensive lesson: **glow on all titles = dull and tacky text**.

- Titles: full white + `text-shadow: 0 4px 28px rgba(0,0,0,.5)` only
  (a readability drop shadow, not a glow).
- Glow is kept for product OBJECTS: tiles/cards (a bright rim border + an inner glow
  rising from the bottom), mockups, ornaments, spectrum bars: objects that really are in the concept.
- Realistic elements (app store rows, buttons) get NO glow at all:
  the more realistic the element, the more wrong the glow.
- WebGL bloom: `threshold ≥ 0.5`. A low threshold makes the background bloom too
  and the whole frame white (this has happened).

## 7. Three.js backgrounds

Layers from back to front, all tied to `state`:

- **Nebula**: a plane with an fbm-noise shader, `NormalBlending` (DO NOT use additive:
  it stacks through the bloom → white), a vertical gradation: `exp(-((y-0.02)*3.4)^2)`
  lights up the horizon, the top dimmed ~70%. This is the antidote to a "flat background".
- **Dust**: 1000–1500 `Points`, size ∝ 1/z, twinkle via a per-seed sine.
- **Floor grid**: an `fwidth`-antialiased shader, fading FAR before the horizon
  (lines meeting at the horizon pile into a bright band cutting through the text);
  opacity per scene 0.2–0.6, no more.
- **3D ornaments** (a star ✦, a brand shape): a `Shape` + a concave curve →
  `ExtrudeGeometry` + bevel, `MeshStandardMaterial` + DirectionalLight;
  Basic material looks flat, and flat = PPT. Sway the Y axis
  with a sine ±0.55 rad, DO NOT rotate fully (a flat object seen from the side =
  a single line). One "hero" ornament crosses quickly during a transition.
- **Tunnel/rush**: SHORT particles (len 0.8–2.5), medium-dark color,
  ≤300 of them, opacity ≤0.6; the long white line version is too busy
  and leaves the text without contrast.
- **Bloom**: `UnrealBloomPass(strength .75–.95, radius .7, threshold .52)`,
  + a small pulse following the beat.
- **The WebGL camera**: a `camZ` dolly per scene + a slow sine handheld sway +
  beat shake via a high-frequency sine.

A cheap extra gradient: a `mix-blend-mode:screen` div holding an accent
radial-gradient at bottom-center, INSIDE the `#world` rig.

## 7b. Light backgrounds & background changes between scenes

The dark WebGL background in §7 is only one language. One of the accepted openers
changed its background following its segments: a dark base for the problem → light
for the solution → dark again for emphasis → a color block for the CTA. That is an
EXAMPLE, not a template: light can be a soft two-palette-color gradient, a flat
pastel with blobs, a solid color block, textured paper, or a photo
with a gradation. The recipe for the light version (paper and gradients use the same CSS,
just change `background`):

```css
.paper{position:absolute;inset:0;opacity:0;visibility:hidden;
  background:linear-gradient(180deg,#F7FAFF 0%,#EEF4FF 55%,#E6EEFF 100%)}
.paper .b{position:absolute;border-radius:50%;pointer-events:none}          /* soft color blobs, following the palette */
.paper .b1{left:-260px;top:-380px;width:1100px;height:1100px;background:radial-gradient(circle,color-mix(in srgb,var(--accent-lit) 38%,#fff) 0%,transparent 68%)}
.paper .b2{left:1180px;top:520px;width:1000px;height:1000px;background:radial-gradient(circle,color-mix(in srgb,var(--accent) 22%,#fff) 0%,transparent 66%)}
.line.ink{color:#0B1B33;text-shadow:none}                                    /* text for a light background */
```
```js
/* swap the background BEHIND a cut/wipe: the frame is covered, the jump is invisible */
tl.set('#paper',{autoAlpha:1},atCut); tl.to('#gl',{opacity:0,duration:.25},atCut);
tl.to('.vignette',{opacity:.35,duration:.4},atCut); tl.to('.bgfx',{opacity:0,duration:.25},atCut);
tl.to('.paper .b',{x:60,y:-40,duration:3,ease:'sine.inOut',yoyo:true,repeat:1,stagger:.4},atCut); // living blobs
/* at t=0 (loop): restore everything */
tl.set('#paper',{autoAlpha:0},0); tl.set(['#gl','.vignette','.bgfx'],{opacity:1},0);
```
When to change: whenever needed, planned in the style brief: the mood
or topic of a segment changes (problem → solution, claim → product, content → CTA), a
colorful brand demands a color rhythm (palette color fields alternating), or an
on-screen action changes it (a toggle is switched on, an object covers the lens, an icon
grows to fill the frame). A short bumper or a single-mood opener may have one
background color, but that background still MOVES (§7c); a still background is rejected.
What is not legitimate: a background that was never considered (dark automatically
because the starter was dark) and a change with no trigger. When it changes: at
a cut point/beat, behind a wipe/object (camThrough/wipe/leak), or as the
result of an on-screen action; never an unexplained cross-fade; the text switches
to its variant (`.ink`) and the dark pocket (`.pocket`) is turned off in light scenes;
the vignette is lightened (0.3–0.4), WebGL bloom is turned off. An example light gradient:
`background:linear-gradient(160deg,color-mix(in srgb,var(--accent-lit) 30%,#fff),#fff 55%,color-mix(in srgb,var(--accent) 14%,#fff))`.

## 7c. The background motion menu: "motion every second" does not mean objects crossing

A common failure: openers for different products all use
bars/pieces of light shooting sideways, because the rule "motion must
exist in the world (an object crossing) every second" was read narrowly: the model picks the cheapest
way and then looks for a justification from the product. Background motion is chosen in the style brief from
this menu, and must be different from the previous project:

| # | Background motion language | Feel | Notes |
|---|---|---|---|
| 1 | A textured background + a breathing camera + one gentle motion (a tint/light/grain shifting slowly) | calm, expensive | the calmest choice that is still legitimate; a truly still background is rejected |
| 2 | A large gradient slowly drifting/rotating (2–3 palette colors) | soft, modern | `background-position`/the angle tweened over 8–15 s |
| 3 | Floating color blobs (2–4 blurred circles) | friendly, light | follows the palette; drift ±60 px, 4–6 s |
| 4 | Live grain/paper texture (a mask offset per frame from t) | organic, print | not random noise: an offset from `t` |
| 5 | A light sweep ONCE per segment | premium | not a continuous sweep |
| 6 | A big geometric shape (a circle/lines/a negative logo) rotating 20–40 s per revolution, 2 parallax layers | brand, strong | the shape from the logo/theme |
| 7 | Particles slowly RISING (dust, bubbles, sparks) | warm, alive | not horizontal; opacity ≤ .35 in the text pocket |
| 8 | A grid/pattern that breathes (scale/opacity 1.0↔1.04, 6–10 s) | technical, precise | no scrolling |
| 9 | Giant ghost text drifting slowly behind | editorial | low contrast ≥ .12, one style |
| 10 | A theme photo/illustration with Ken Burns + 2-layer parallax | narrative | needs a dark gradation on the text side |
| 11 | Horizontal flow (streaks/lanes/ranges/particle rain) | speed, data | ONLY when the theme = speed/flow; already used in two projects in a row → avoid unless in a clearly new way |
| 12 | Palette color fields alternating (a sweep/snap of 0.15–0.3 s, triggered by an object, a UI action, or a beat) | pop, energetic | for colorful brands; each field filled with moving flat shapes/objects |

The rule: one language per opener (two allowed if the background changes between
segments), written in the style brief on the "background motion" line, separate from
the "signature move" (which moves OBJECTS/text, not the background). This menu
also applies to the WebGL background in §7: a slowly drifting nebula + a breathing camera
is #1, rising dust is #7; "tunnel/rush" is #11. The background is never
still in any scene; a background color change (§7b) may be added on top of
any motion language.

## 7d. The background surface menu: gradients, light, texture (not flat)

"Dark ≤ 25 % / light ≥ 80 % under the text" is a TEXT POCKET rule,
not an order to make the whole background a flat single color. An accepted opener
used a rich background: dark with a radial glow on the horizon, light with a soft
gradient and palette-color blobs. The menu (all from palette tokens; the values
may be freely changed):

```css
/* a. horizon glow (dark) */ background:radial-gradient(70% 42% at 50% 108%,color-mix(in srgb,var(--accent) 34%,transparent),color-mix(in srgb,var(--accent) 12%,transparent) 48%,transparent 70%),linear-gradient(180deg,#05060a,var(--base) 60%,#0b1020);
/* b. diagonal duotone   */ background:linear-gradient(160deg,color-mix(in srgb,var(--accent) 55%,#000) 0%,var(--base) 45%,color-mix(in srgb,var(--accent-lit) 30%,#000) 100%);
/* c. light mesh (blobs) */ background:#F7FAFF; + 3–4 <i> radial-gradient(circle,color-mix(in srgb,var(--accent-lit) 38%,#fff),transparent 66%) sized 800–1200 px, drift ±60 px
/* d. spotlight + tint   */ background:radial-gradient(55% 60% at 50% 40%,color-mix(in srgb,var(--accent) 18%,var(--base)),var(--base) 75%);
/* e. a layered sky      */ background:linear-gradient(180deg,#cfe0f5 0%,#f5efe3 100%); + 2–3 layers of thin color bands with opacity .2–.4
/* f. texture + tint     */ paper/grain (feTurbulence) over a/b/c with mix-blend-mode:multiply/overlay, opacity .1–.3
/* g. grainy gradient    */ a saturated 2–3 color gradient in SHAPES and the background + a fine grain layer over everything (recipe below)
```
The rule: a flat single color only for the "poster color-block" direction (given
a fine grain/texture) and "flat pop with photos" (flat fields are legitimate because they change
quickly and are always filled with moving flat shapes/objects). Every background has ≥ 2 layers (a base + light/
texture/blobs). Background colors come from the theme palette, not pure black/white.

### Grainy gradient

The popular term is *grainy gradient* or *noisy gradient*: a soft saturated color gradient
plus an even fine grain. The grain makes the gradient feel print/analog, and
also acts as a dither that prevents banding (staircase lines) when the video is compressed.

**Style traits**
- The gradient is placed IN SHAPES, not just in the background: circles, arcs, holes,
  petals, concentric layers. Each shape glows from within then fades to a
  deep/dark color; its edge stays sharp, its inside soft.
- A palette of 2–3 colors far apart (e.g. blue ↔ orange, teal ↔ cream, purple ↔ pink) over
  a dark or deep-color base.
- A fine monochrome grain across the whole frame (background AND objects), the same intensity on light
  and dark; not big specks, not dust.
- Calm motion: layers slowly opening/rotating, the camera passing through a shape's hole, one small light
  orb guiding the eye.

**Recipe**
```html
<svg width="0" height="0" style="position:absolute"><filter id="grain" x="0" y="0" width="100%" height="100%">
  <feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="3" stitchTiles="stitch"/>
  <feColorMatrix type="saturate" values="0"/></filter></svg>
<div class="grain" id="grain"></div>   <!-- the topmost layer, above the background and objects -->
```
```css
.shape{background:radial-gradient(60% 60% at 50% 30%,var(--c-lit),var(--c-mid) 45%,var(--c-deep) 100%)}
.grain{position:absolute;inset:-60px;pointer-events:none;filter:url(#grain);opacity:.22;mix-blend-mode:overlay}
```
```js
/* deterministic live grain: the position jumps 12× per second from t, not Math.random */
const grainAt=t=>{const k=Math.floor(t*12);grainEl.style.transform=`translate(${k*37%60-30}px,${k*61%60-30}px)`;};
```
- A dark background: overlay/soft-light, opacity .15–.3. A light background: multiply, opacity .08–.15.
- `baseFrequency` .65–.9 at 1920×1080 gives a grain of 1–2 px; finer than that
  vanishes on encode.
- WebGL: add at the end of the fragment shader
  `col += (hash(gl_FragCoord.xy + floor(uTime*12.)) - .5) * .06;`, which is lighter than a
  full-screen SVG filter.
- A real-time preview is heavy with a full-screen SVG filter: make a 256 px noise tile once on a
  canvas and use it as a repeating `background-image`. For per-frame rendering both are safe.

**Precautions**
- Grain and fine gradients are damaged by compression: encode with `-crf 10–12 -tune grain`
  (libx264) or a high bitrate, then check the MP4, not just the browser. A video
  re-uploaded at low resolution loses its grain and shows banding; a slightly
  bigger grain survives better.
- The text pocket is still contrast-tested; small text may be placed above the grain layer so
  the letters do not look dirty.
- A grainy gradient is a skin, not a skeleton: the concept and transitions still come from
  `opener-concepts.md`.

## 7e. The object render style menu: one family per video

Objects (icons, things, mascots, devices) can be rendered in many material languages.
Pick one family per video, or two when the change is made a moment (a flat shape
spins and turns out to be a 3D object). Mixing without a reason feels like a collection of stock assets.

| Render style | Traits | How on the web | Good for |
|---|---|---|---|
| Flat solid | even color fills, no shadows, geometric shapes | SVG/CSS | consumer apps, education, infographics |
| Flat + color dots | palette circles of various sizes scattered, moving elastically around the object | SVG + GSAP | cheerful brands, logo reveals |
| Soft 3D / clay | matte pastel, thick rounded corners, soft shadows | Three.js `MeshStandardMaterial` roughness .7–.9, or an image from a generator | friendly fintech, education, productivity |
| Glossy 3D | shiny plastic, rim light, environment reflections | `MeshPhysicalMaterial` clearcoat 1 + envMap | tech, security, gaming |
| Glass / glowing orb | transparent, refraction, a glowing core | `MeshPhysicalMaterial` transmission 1 + a small bloom | AI, portals, eye guides |
| Isometric | a 30° angle, no perspective, tidy blocks | CSS isometric transforms or an orthographic camera | property, SaaS, process maps |
| Realistic metal/marble | PBR, plane depth, cinematic dark | Three.js PBR + HDRI + DOF, or a render/generator imported as a layer | awards, luxury, events |
| Neon line on dark | a thin glowing outline, layered curves/frames | SVG stroke + a thin glow, or Three.js lines | tech, music, portals |
| Flat character illustration | vector figures, warm colors, a thin texture | layered SVG/PNG | community, services, explainers |

- Realistic objects (metal, marble, devices) are most efficiently made as images/video from a
  generator or a 3D render, then animated as layers (parallax, in/out, fake
  DOF); do not force Three.js if the result is far worse.
- The render style is written in the style brief and differs from the previous project.

## 8. Icon tiles & UI mockups

**Icon tiles** (ONE option for presenting features, not a default; the full menu is in
`opener-concepts.md`; the number follows the features, not always three): a rounded-square ±210px, a bright accent
rim border 2px, an inner glow rising from the bottom (a radial at 50% 115%), a white
stroke icon 3.5–4.5 + `drop-shadow`, a 1–2 word label below. Entry
`back.out(1.9)` stagger 0.15.

**UI mockups**: a large `border-radius` bezel + an `overflow:hidden` screen;
the mockup contents use the REAL PRODUCT FONT & COLORS (not the display font); the mockup
is judged as "the app", not decoration. Living elements inside it
(spectrum, numbers, sparklines) are driven from the same data source as the
3D background so they stay consistent. It enters as an OBJECT (rising from the bottom of the frame,
rotateY ±10–24° with a `perspective` parent), not as a layout column.

**App/SaaS UI animation**: the UI is assembled from components, used (a cursor/finger/UI action), the data
is alive, and transitions are carried by the UI (a panel blooming, a badge shrinking, a window carousel):
the layout-color-rhythm guidance and the motion menu are in `opener-concepts.md` under "UI animation
for apps & SaaS".

**The camera follows UI interaction**, so the demo is not static and it is clear what is clicked.
A whole UI in frame with only the cursor moving feels like a still screen recording, and
a small click is not readable. When a click matters to the story, the camera follows:

1. **Approach before the click**: 0.3–0.5 s before the cursor arrives, the camera zooms to the target area
   (scale 1.4–2.2, `power2.inOut` 0.6–0.9 s); the target slightly above the center of the frame.
2. **The click reads**: the cursor stops for ±0.2 s, the button is pressed (scale .92 → 1), a thin
   highlight on the button; the camera is nearly still during the click.
3. **Follow the result**: the camera pulls back to wide or shifts to the panel that changed
   (0.7–1 s), not jumping.
4. **Choose, not all**: 1–3 important clicks per act get a zoom; other clicks are fine on the
   wide camera or a slow pan. A UI scene that is calm by nature (a dashboard being shown off, data
   filling in) may have no zoom. Avoid zooming in and out back and forth faster than
   ±1.5 s; it is dizzying.
5. Smooth, with no radial blur, unlike a slam zoom.

```js
/* ui = the wrapper of the whole UI + cursor (position:relative; transform-origin:0 0), inside an
   overflow:hidden frame. target = an element inside ui (ui as its offsetParent). */
const camTo=(ui,target,at,{s=1.8,dur=.8,fy=.45}={})=>{
  const W=ui.offsetWidth,H=ui.offsetHeight;
  const cx=target.offsetLeft+target.offsetWidth/2, cy=target.offsetTop+target.offsetHeight/2;
  tl.to(ui,{x:W/2-cx*s,y:H*fy-cy*s,scale:s,duration:dur,ease:'power2.inOut'},at);};
const camWide=(ui,at,dur=.9)=>tl.to(ui,{x:0,y:0,scale:1,duration:dur,ease:'power2.inOut'},at);
/* pattern: camTo(ui,btn,T-.5) → click at T → camWide(ui,T+.6) or camTo(ui,newPanel,T+.6,{s:1.3}) */
```
The cursor sits INSIDE `ui` so it grows together with its button. A target nested
inside other positioned elements: compute its position by summing `offsetLeft/Top` up to `ui`.

## 9. Typing & living numbers (deterministic)

Typing for text that really is typed in the concept's world (a message, a command, a search
that is the core of the product), not an input box placed in every opener.

- Typing: `tl.fromTo(o,{i:0},{i:n, ease:'none', onUpdate: el.textContent =
  str.slice(0, Math.round(o.i))})`, NOT setInterval.
- Uptime/counter: `f(t) = base + (t - tStart)`, formatted in the render loop.
- Sparkline/spectrum: a sum of sines at different frequencies over `t`: cheap,
  looks organic, and is reproducible.

## 9b. Video as footage layers

Motion graphics are not only pictures and shapes: a video clip can be a layer like footage
in After Effects: trimmed, positioned, masked, graded, and animated together with other
elements. All the starters already carry a `clip()` helper.

**When video is stronger than a picture**
- Real motion that serves as evidence: a product screen recording, a person using the product, a process
  running, the atmosphere of a place.
- One emphasis moment of 3–8 s, not a replacement for all the motion design. Text, numbers,
  annotations, and transitions are still animated above/around the clip.
- If a still picture explains enough, use a picture (lighter, faster export).

**Clip sources** (asked of the user, the same as photos; `opener-concepts.md` "Photos in openers")
- Files from the user (priority): a product screen recording, brand B-roll, event footage.
- Generated through the Higgsfield MCP if approved; check the cost first (video clips are far more expensive
  than images). Most consistent: generate an image in the project's style, then image-to-video.
- Licensed stock. Factual contexts (news, history, data): a generated clip is labeled
  "illustration/reconstruction"; do not present it as real footage; faces of real people are not
  generated.

**Format**
- MP4 H.264 (`yuv420p`, `+faststart`) or WebM VP9; no sound (music/VO stay separate
  tracks); 720p–1080p; trim to the part used so it stays light.
```bash
ffmpeg -i source.mov -ss 2 -t 6 -vf "scale=1920:-2" -c:v libx264 -pix_fmt yuv420p -crf 20 -movflags +faststart -an assets/clip.mp4
```
- The deliverable becomes `index.html` + an `assets/` folder holding the clips; tell the user so.

**Usage patterns** (animate the WRAPPER, not the `<video>` itself)
- Inside a device: a laptop/phone screen in a SaaS opener; the camera passes through into the screen.
- Inside a container: a photo card, a rounded frame, a circle, giant letters (`clip-path`/mask).
- A split screen: video on one side, a claim/number on the other.
- Full screen with layers above it: a palette grade/tint (`filter` or a
  `mix-blend-mode` layer), a vignette, text in a contrast pocket (§1b).
- Time: trim `in/out`, `rate` for slow/fast motion, `hold` for a last freeze frame.
- Entry/exit transitions the same as other elements (an object wipe, a growing card, a match cut).

**The helper API** (in all starters, after the `window.OPENER=` line)
```html
<div class="clipbox" id="box1"><video id="v1" src="assets/clip.mp4" muted playsinline preload="auto"></video></div>
```
```js
clip($('#v1'), {at:4, in:1.5, out:6, rate:1, hold:false});  // at = timeline seconds; in/out = the source trim
tl.set('#box1', {autoAlpha:1}, 4);                             // show the wrapper when the clip starts
tl.fromTo('#box1', {scale:.8}, {scale:1, duration:1, ease:'power3.out', immediateRender:false}, 4);
```
- The video's contents follow the timeline clock: synced during playback (corrected if the gap > 0.2 s),
  and seeked exactly during scrub/pause. Do not use the `autoplay`/`loop` attributes and do not
  call `play()` yourself.
- `OPENER.seekFrame(t)` seeks the timeline AND waits for the clip frame to be ready; `snap.mjs` and
  `export-frames.mjs` use it automatically, and wait for `OPENER.clipsReady()` before starting.
- Hide the wrapper outside the clip's range (`autoAlpha`); outside the range the video is paused.

**Precautions**
- At most 2–3 clips shown at once; a big clip that is not visible is still decoded.
- MP4 export is slower because every frame waits for the video decoder.
- A ±1 frame difference during real-time playback is normal; the exported result stays frame-exact.
- Check the result with `snap.mjs` at seconds that contain clips, not just in the browser.

## 10. Traps

| Symptom | Cause | Remedy |
|---|---|---|
| The whole frame glows white | a low bloom threshold + additive layers | threshold ≥.5; NormalBlending backgrounds |
| An element appears ahead of its animation | a CSS selector more specific than the initial-state `opacity:0` | do not write opacity in a specific selector; GSAP gives the final value |
| JS edits "have no effect" | the browser caches modules (heuristic) | a `Cache-Control: no-store` server |
| A 3D ornament becomes a white line | a flat object fully rotated on the Y axis | a sine sway, not a full rotation |
| The blur tail is clipped by a box | the default filter region 110% | x/y -70%, width/height 240% |
| Text looks "dark/dull" | stacked glow sucks the contrast | remove the title glow, full white |
| A bright band cuts through text at the horizon | grid lines pile up at the meeting point | fade the grid before the horizon |
| Scrub produces different images each time | there is random/accumulation in the render | see the determinism prohibition list |
| Text breaks/the width is wrong on split | splitting before the font has loaded | wait for `document.fonts.ready` |
| A letter/pill "flashes" briefly before its entry animation | `tl.set(el,{autoAlpha:1})` and then `fromTo(...immediateRender:false)` starts a few frames later; in between the element shows fully | the initial state of `.ch`, `.hl-t`, punctuation = `opacity:0` IN CSS, not just on their wrapper |
| A control card/text jitters in width while a number runs | proportional digits (1 is narrower than 8) | `font-variant-numeric:tabular-nums` + `min-width` on the number element |
| A scrub screenshot lags one step behind / is out of sync | GSAP writes styles lazily on the next tick and the canvas waits for rAF (throttled in a hidden tab) | provide `OPENER.seek(t)` = `tl.pause(); tl.time(t); gsap.ticker.tick(); render(t)` and use it from puppeteer/the console |
