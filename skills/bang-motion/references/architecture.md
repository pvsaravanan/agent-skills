# Architecture: project structure and its reasons

Every decision here was wrong once before it was right. The "why" parts
matter more than the code.

## File structure

```
project/
├── index.html          markup of all scenes + the SVG motion blur filter
├── css/app.css         color tokens, scene layout, hidden initial state
├── js/three-scene.js   a stateful WebGL world (background, particles, ornaments, bloom)
├── js/timeline.js      the ONLY place time is written (the GSAP master timeline)
├── js/util.js          splitChars + blurTween (directional motion blur)
├── js/main.js          glue: fit stage, render loop, control panel
└── tools/
    ├── serve.py        dev server Cache-Control: no-store
    └── export-frames.mjs  frame-by-frame render (puppeteer)
```

It may be condensed into one file (see `assets/starter-opener.html`) for
prototypes; split into the structure above once there are > 3 scenes.

## The stage: fixed at 1920×1080, then scaled

```css
#stage{position:fixed;left:50%;top:50%;width:1920px;height:1080px;
  transform:translate(-50%,-50%) scale(var(--fit));overflow:hidden}
```
```js
const s = Math.min(innerWidth/1920, innerHeight/1080);
```

**Why:** the composition must not change because of the window size. A position
approved on a 27" monitor must be identical when recorded. The window size only
changes the zoom, not the layout.

## The `#world` camera rig

```
#stage
└── #world            ← camera rig: SCALED/TRANSLATED by the timeline
    ├── <canvas>      ← WebGL (3D background)
    ├── .bgfx         ← gradient overlay (blend screen)
    └── #dom          ← all text/UI scenes
├── .leak             ← light leak: OUTSIDE world, the topmost layer
├── .vignette, .grain
```

**Why world wraps the canvas too:** when the camera zooms, both the TEXT and the
background must grow. Zooming only the text layer feels fake; zooming the whole world
feels like a camera. The light leak MUST be outside world: it is light in front of
the lens, not part of the world.

## State-driven WebGL

The Three.js scene knows nothing about time. It exposes one object:

```js
const state = {
  grid: 0, dust: .5, nebula: .6, stars: 0, tunnel: 0, flow: 0,
  camX: 0, camY: 0, camZ: 16, camRoll: 0, bloom: .85, shake: 0,
  heroO: 0, heroS: 1, heroX: 0, heroY: 0, heroZ: 6,   // main ornament
};
```

and the GSAP timeline tweens those numbers. The `render(t)` function receives
`t = tl.time()`.

**Why:** one source of truth for time. Scrub, pause, and export are automatically
right because WebGL has no clock of its own.

**The `flow` rule:** things that "flow" (tunnel, particle rain) are stored
as a DISTANCE that is tweened (`flow: '+=300'`), and each particle's position =
`(seed + flow*speed) % span`. DO NOT `pos += speed*dt`; that is accumulation, and
it makes scrub and export non-reproducible.

## Timeline: absolute seconds

```js
tl.fromTo(chars, {...}, {...}, 8.10);   // ← an absolute number, not "+=0.3"
```

**Why:** the scene rundown holds second numbers; writing the same numbers in the
code makes the order readable at a glance, and shifting one scene does not ripple
into the others. Provide a `DURATION` constant in one place.

## Initial state in CSS, not in GSAP

```css
.hero, .line, .obj, .ornament { opacity: 0 }
```
```js
tl.fromTo(el, {opacity:0,y:60}, {opacity:1,y:0, immediateRender:false}, 8.1);
```

**Why:** with `immediateRender:false`, CSS is what holds the state
before the tween starts. Without it every element flickers on the first frame.

**A TRAP that has happened:** the initial-state selector loses on specificity.
`.card.ghost{opacity:.85}` beats `.card{opacity:0}`, so the element
appears ahead of its animation. Never write `opacity` in a selector
more specific than the initial-state selector; let GSAP give the final value.

## Determinism: the list of prohibitions

| Prohibited | Replacement |
|---|---|
| `Math.random()` in the render loop | a high-frequency sine: `Math.sin(t*137.2)` |
| `Date.now()` / `performance.now()` | pass `tl.time()` in as a parameter |
| `setInterval` for running/typing text | tween `{i:0→n}` + an `onUpdate` slice |
| accumulation `pos += v*dt` | position = function(seed, state.flow) |
| `Math.random()` at SETUP is allowed | seeds are made once at load, not per frame |

## The dev server must be no-cache

`python -m http.server` lets the browser hold old JS modules through
heuristic caching: edits "have no effect", and you end up chasing ghosts.
Always use a server that sends `Cache-Control: no-store`
(`scripts/serve.py`). ES modules do not run through `file://`, so a server
is required during development.

## Verification vs export: two different things

- **Verification** (every batch of changes): `scripts/snap.mjs` captures
  6–20 key seconds through `OPENER.seek(t)`; the results are looked at, not
  saved. Without Node: `?debug=1` + manual screenshots.
- **Export** (only when the user asks for MP4): render all frames. Do not
  mix them up: rendering everything to "test" wastes thousands of images and gives
  no judgment of any kind.

## Exporting to video

Do not screen-record for the final result (frame drops). Because everything is
deterministic: set `tl.time(frame/fps)` → wait 2× rAF (one for GSAP
to write styles, one for the render loop to draw) → screenshot → repeat.
`scripts/export-frames.mjs` does this through puppeteer; merge with:

```
ffmpeg -framerate 60 -i frames/f%05d.png -c:v libx264 -pix_fmt yuv420p -crf 16 out.mp4
```

Expose `window.OPENER = { tl, DURATION }` so the export script (and console
debugging) can control the timeline.

## The developer control panel: hidden

Do not show a player in the deliverable. Default: autoplay when opened, loop
when finished, R restarts, Space pauses. The panel (play/pause, scrub slider, clock
`t.toFixed(2)`) appears only with `?debug=1`; `?clean=1` = no panel and
no autoplay for the export script. Scrub remains the user's main review tool
(they think in "second X"), but through the debug URL, not in the result.

## Visual verification (not optional)

After every batch of changes: open it in the browser, `tl.pause(); tl.time(X)` in the
console for each key second, take a screenshot, judge it with the heuristics in
`anti-ppt.md`. Code that runs ≠ a scene that is right; almost every user
revision comes from SEEING, not from errors.


## Deliverable form: one file, no server

During development it may be multi-file (css/, js/) + a no-cache server. But what is
DELIVERED is one `index.html` that can be double-clicked:

- `<style>` and `<script type="module">` are written inline. The reason is technical:
  Chrome rejects `<script type="module" src="js/app.js">` from `file://`
  (origin `null` → CORS), while an inline module may `import` from
  an https CDN without trouble.
- The import map + GSAP/Three from a CDN are still used (they need internet, not a
  server). Google Fonts too.
- Local assets (icons, images) just use relative paths: `<img src="icon.png">`
  is safe on `file://`.
- Avoid `fetch()`/XHR to local files; they are blocked on `file://`.
- Node/puppeteer is only for rendering MP4; do not let the user think the opener
  needs `node_modules`. Explain that in the README. Without Node: screen record
  (noting it can drop frames). Without Python: nothing is lost,
  a server is only needed when using local modules, and a single-file deliverable
  does not use them.
- The render/snap scripts default to `pathToFileURL(process.cwd())` so they
  work without a server; an http URL can still be passed through the `URL` env.

A safe inlining process: read the css & js, replace the `<link>`/`<script src>` tags
with their contents, make sure the JS does not contain `</script>`, then delete the
source folder so there are not two truths.
