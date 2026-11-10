---
name: bang-motion
description: Builds cinematic motion graphics in the browser (promo videos, openers, intros, bumpers, kinetic typography, illustrated explainer videos in 16:9 or 9:16) with HTML + CSS + GSAP (+ Three.js when needed), so the result moves like real video, not like presentation slides. Use this skill whenever the user asks for a "promo video", "opener", "animated intro", "motion graphic", "bumper", "kinetic typography", "cinematic text animation", "explainer", "explainer video" (visual journalism, educational cartoon, collage), or shows a reference promo/explainer video and wants a web version of it, even if they never say "motion graphic". Also use it when the user complains that a web animation looks "like a PPT/presentation" and wants it more cinematic, wants to render a web animation to an MP4 file, or wants a cartoon/animated explainer built DIRECTLY in After Effects through the Higgsfield bridge/MCP.
license: MIT
metadata:
  author: Bang Tutorial
  author_url: https://youtube.com/bangtutorial
  version: "1.19.0"
  updated: "2026-09-14"
  homepage: https://github.com/bangtutorial/bang-motion
---

# Bang Motion: web motion graphics that are not PPT

**v1.19.0 · by [Bang Tutorial](https://youtube.com/bangtutorial) · MIT.** Change history is in the upstream `CHANGELOG.md`;
install instructions are in the upstream `README.md`. This copy is an English translation of the upstream skill.

This skill is for any AI coding agent (open Agent Skills format).
It holds the laws and recipes for motion graphics that move like video, not like
a presentation. Follow them before writing code.

## Prerequisites: just a browser

The deliverable (`index.html`) needs only a modern browser plus internet for the CDNs
(GSAP, fonts). Python and Node are **optional** and used only for working tools:
`scripts/serve.py` (no-cache server, needed only when using local modules),
puppeteer (automatic snapshots/verification, `scripts/export-frames.mjs` → MP4).
If the user has neither: (1) still build a single file and open it with a double-click;
(2) verify visually with `?debug=1` (scrub panel) and manual screenshots at key
seconds; (3) get MP4 through screen recording (OBS / browser tab recording), and
explain that a screen recording can drop frames and that frame-by-frame rendering needs
Node. Never make a deliverable that needs `npm install` just to be WATCHED.

**ffmpeg is optional too.** Check first (`ffmpeg -version`); if it is missing:

| Need | With ffmpeg | Without ffmpeg |
|---|---|---|
| VO sync (sentence/paragraph boundaries) | `silencedetect` | `scripts/vo-pauses.html`: open it in the browser, pick the audio, copy `SEG`/`PARA`; same result (Web Audio, no install) |
| Audio duration/format | `ffprobe` | the `DUR` number from vo-pauses.html; the browser plays wav/mp3/m4a/ogg directly |
| MP4 export | merge the PNGs from export-frames.mjs | no MP4: offer a one-command install (`winget install Gyan.FFmpeg` / `brew install ffmpeg`) or screen recording |
| Studying a reference video (extract frames) | `fps=` + `tile=` | ask the user to send screenshots at key seconds, or open the video in the browser and capture at specific seconds |

Without ffmpeg the explainer flow is still complete up to VO sync; only the MP4
needs an install.

## Player: none, autoplay, loop

Default deliverable: **no panel/player on screen**, it plays immediately when opened
and restarts from the beginning when it ends (`onComplete → play(0)`; if there is
sound, the audio loops too). Hidden controls: R restarts, Space pauses. The scrub/clock
panel appears only with `?debug=1` (a review tool), and `?clean=1` holds autoplay for
export. Sound? Try `play()` right away; if the browser blocks it, hold on frame 0 and
start on the first click, with no "tap to start" text. This is already built into both
starters.

## Structural prohibitions: PPT checks you can run mechanically

Other models (and you, when tired) will fall into these patterns even after reading the
laws below. Before delivering, check the CODE, not your feelings:

1. `grep -c "class=\"scene\"\|<section" index.html`: if there are ≥ 3 scenes
   made of `<section>` elements switched on and off with `autoAlpha`/opacity,
   that is a slide deck. Scenes must change because the WORLD/CAMERA moves
   (the camera moves, whips to another corner, pushes through, the background changes),
   not because a section is faded. Legitimate exception: **cartoon stage**
   (`references/cartoon-stage.md`) uses a cut/96 px slide between stages.
   That is allowed because each stage is fully alive (≥10 objects in action), not a
   still picture being faded.
2. There is a visual through-line that persists: one subject (continuous action) OR
   one collage/paper/white world that the camera travels over (cartoon, photo,
   catalog, sketch). Full-bleed photos swapping with no shared world → PPT.
   One picture + one sentence per scene, swapping every scene → still a slideshow
   even if the camera moves: each scene has 3–5 elements that enter gradually per
   phrase (explainer.md "One scene = 3–5 elements").
3. Count text nodes per scene: eyebrow/kicker + title + body/credit = 3 levels
   → PPT. Maximum two: one big number/sentence + one world label.
   A document/stamp/date block with ≤ 3 short lines counts as an object, not a
   text level.
4. Ken Burns (scale 1.0→1.05 on a photo) as the only motion → PPT.
   Motion every second must come from the BACKGROUND MOTION LANGUAGE chosen in the
   style brief from the `techniques.md` §7c menu (camera breathing on a textured
   background, drifting gradient, floating blobs, live grain, a light sweep per
   segment, a large slowly rotating shape, rising particles, breathing grid, ghost
   text drifting, Ken Burns + parallax…). Bars/lines/pieces crossing sideways
   ("lane", "range", "streak", horizontal particle rain) have ALREADY been used by two
   projects in a row under different names. They are not a default; use them only
   when the theme really is speed/flow, and never in two projects in a row.
5. Transitions that are only fade + scale bump + light leak on every cut → PPT
   template. Whip to another corner, cut to an instrument (map/speedometer/profile),
   push-through.
6. Explainers start from the starter for their STYLE: `starter-explainer-cartoon`,
   `-journalism`, `-catalog`, `-sketch` (collage mode: the camera travels over
   still assets), `starter-explainer` (continuous action: the world flows), or
   `starter-explainer-stage` (cartoon stage: one stage per scene, jointed rig,
   camera only inside the stage). The collage ones share one rig; the stage one
   has a different rig. NOT from `assets/starter-opener.html` (text opener),
   and not from scratch.

7. **A miniature is a slide.** The camera zooms < 1.08, so a house is thumb-sized and
   empty ground fills half the screen → PPT even though everything moves.
   Split the world into frame-sized stages rather than one big map to explore
   (`cartoon-stage.md` Law 1).

8. **Template skeleton (opener/promo).** Check the rundown and code: the first
   scene is text that grows and then exits left; three feature tiles/cards
   side by side; an input box/searchbar being typed into; the order hook → feature →
   feature → promise → logo → CTA. Two or more with no demand from the concept →
   template, even with a new skin. Choose the skeleton again from
   `references/opener-concepts.md`.

Fail even one point → rework before showing the user.

## Kinds of work covered

This skill is for web motion graphics in GENERAL. The explainer is only one kind;
it has its own document because its structure differs, not because it is the main one.

Starters are named by category: `starter-opener.html` for openers, promos,
bumpers, intros, and kinetic typography; `starter-explainer-*.html` for explainers,
with a mode/style suffix (`-cartoon`, `-journalism`, `-catalog`, `-sketch` = collage;
no suffix = continuous action; `-stage` = cartoon stage). Cartoon stage is an
explainer mode (style 6), not a category of its own: its goal is still to explain
with VO, only the way it is produced differs.

| Kind | Usual length | Traits | Recipe |
|---|---|---|---|
| Opener / product promo | 25–40 s | one concept from the menu (the skeleton comes from the product, not a fixed order), one special moment, brand closing | `references/opener-concepts.md` + the workflow below + `references/techniques.md` |
| Bumper / ident / logo sting | 3–8 s | logo build-on, one signature move, done before the viewer notices | `techniques.md` (logo build-on, light leak) |
| Channel intro / outro | 5–12 s | channel name + the same signature move every episode | workflow below |
| Kinetic typography / lyrics | 15–60 s | text is the subject; split per word/letter; rhythm follows the audio | `techniques.md` (split + directional blur, per-word 3D pan) |
| Title / lower third / segment bumper | 2–6 s | a small element over footage, clean in and out, transparent background | `techniques.md` |
| Explainer / explainer video | 30–90 s | sourced facts, entities shown, changing viewpoints, five styles | `references/explainer.md` + the starter for each style |

## Explainers and characters: read before deciding shots

For a flat educational cartoon explainer with characters (the sixth style, **cartoon
stage**), or a revision that feels like a slideshow/miniature, read
`references/cartoon-stage.md`: one stage per scene, zoom 1.08–1.95,
continuous inside a stage and a cut/96 px slide between them, a jointed rig with
manual transforms, zero captions, a bright flat palette. Distinguish sentence, visual
beat, framing, and stage change. To build it directly in After Effects, read
`references/ae-bridge-higgsfield.md`. This explainer-specific guidance sharpens the
opener rules below; the example fonts, scene counts, and effects are not universal
recipes.

## Law #1: This is video, not slides

The most common disease: the model lays out scenes like slides, with title + subtitle
+ body copy + a row of badges. That reads instantly as "PPT" and will be rejected.

The hard rules:

- **For openers: one short sentence + at most one main object per scene.** No
  kicker ("01 — FEATURES"), subtitle, explanatory paragraph, feature chip/badge,
  or technical metadata (package name, long URL). Chips, buttons, and labels that
  are part of the product UI being used do not count.
- **New information = a new visual response.** In an explainer, change the state/action
  in the same world when it is still related; a new sentence does not have to change
  the shot.
- **Replace bullet lists with visuals, not automatically three tiles.** Pick the way
  from the feature menu in `references/opener-concepts.md` (one feature demoed, words
  that swap, an object that transforms, shuffled cards, a tile grid…); two openers in
  a row do not use the same way.
- **Scenes must be alive.** The camera may rest while objects carry the action.
  Move the camera to follow or reveal something; do not rely on text fading/sliding
  over a still background, or on repeated pan/zoom in every segment.
- **"Zoom in-out" = shot size, not camera breathing.** When the video feels static or
  the user asks for zoom, the camera moves in to the element that is telling the story
  (medium close-up / close-up) and then pulls back to wide following the beat of the
  content; a breath of a few percent is nearly invisible (`techniques.md` §3b).

Read `references/anti-ppt.md` BEFORE designing scenes. It lists real violations
together with their fixes.

## Law #2: Deterministic or dead

Not a single line reads the system clock. Every visual is a pure function of
`tl.time()` (the GSAP timeline time): spectrum, running numbers, particles, camera
shake (high-frequency sine, not `Math.random()`), the position of objects that
"flow" (tween DISTANCE, do not accumulate speed per frame). The consequence: scrubbing
is exact like an After Effects timeline, and frame-by-frame rendering to MP4 produces
identical images every time.

## Law #3: Style is born from the theme, not from the starter, not from a reference

A common failure: an opener for a different product comes out with EXACTLY the skin of
the previous product's opener: dark, blue accent, glow, nebula, the same font,
because the model took its style from the starter. The animation can be good and it
still fails: an opener is the face of a product, and two products must not share a face.

1. **Style brief first, code later.** Before touching a starter, write these lines
   and show them to the user together with the scene rundown:
   - theme/product + three adjectives for the feeling to leave behind;
   - **concept & structure fingerprint** (opener/promo): three candidate concepts from
     `references/opener-concepts.md`, one chosen with a reason from the product, then
     `concept · scene count · main object per scene · opening · closing`;
   - palette: one main color taken FROM the brand/theme (logo, app icon, site,
     packaging), one background color, one accent. State the hex AND the source of
     each color; a color that is not from the brand is written as "derived: reason";
   - a display font with character that fits that feeling (not
     Poppins/Inter/Roboto/Montserrat/Arial) + a companion font; exception: the
     claim → how → result concept uses the product's own UI font
     (`references/opener-concepts.md`);
   - text emphasis: no word highlight, or one form of highlight (name it). Word
     highlight is OPTIONAL, not a default of every opener;
   - background language per segment: one direction from the "Style directions" table
     for all of it, or a change plan (which segment changes, to what, why, triggered
     by what);
   - signature move: one kind of motion repeated as an identity (object wipe, 3D roll
     per word, flying paper, a line that draws, color blocks hitting the edge…);
   - background motion: one language from the `techniques.md` §7c menu. It is not the
     same thing as the signature move, and not automatically "objects crossing";
   - background surface: from the §7d menu (gradient/light/texture/grainy gradient,
     ≥ 2 layers), not flat;
   - object render style: one family from the `techniques.md` §7e menu (flat, clay,
     glossy, glass, isometric, realistic, neon line…);
   - photo assets (when the concept uses photos of people/places/products): the source
     (user photos, generated through the Higgsfield MCP, or licensed stock) is ASKED
     of the user, plus a shot list per act (`references/opener-concepts.md`, "Photos
     in openers");
   - transitions: decide which boundaries need an effect and which can be a plain cut;
     pick from the §4c menu to fit the context; two kinds or 3D are not mandatory;
   - one special moment (where the most expensive effect is used, once).
2. **A starter is architecture, not style.** The gray colors, system font, and WebGL
   background in `assets/starter-opener.html` are PLACEHOLDERS. If any of them is still
   visible in the result, the style was not derived. The WebGL background (nebula,
   dust, grid, bloom) is only one background language out of eight; turn it off when
   the style direction is different.
3. **A reference = rhythm, not skin.** From a reference video take: duration per shot,
   transition type, attention hierarchy, energy, motion language. DO NOT take: palette,
   font, texture, layout, ornament shapes, sentences, scene order, and unique moments
   (a distinctive opening/closing, one-time gimmicks). "Make it like this" means "as
   energetic as this", not "colored like this"; "use style X" means the skin and motion
   language of X, not the scenes of X. The example sequences in
   `references/opener-concepts.md` are treated the same way: principles, not scripts
   (skeleton Law #7).
   Copying a reference's skin is a violation even when the user supplies it. Say so
   in one sentence and then offer a version born from the theme.
4. **Different from the previous project: skin AND skeleton.** Two different products
   must differ in at least three of four: palette, font, background language,
   signature move, including the word-highlight shape if used (a pill + star belonging
   to one project must not appear again in another). The skeleton too: a different
   concept, or ≥ 3 of the 5 structure-fingerprint elements different
   (`references/opener-concepts.md`). A new color over the old scene order is still a
   template.
   Do not open old project folders for "examples". Only the rules in this skill may be
   inherited.
5. **The background is not dark by default.** Without this rule every opener tends to
   come out dark with a nebula because the starter and its examples are dark. The
   background follows the theme: a light gradient, soft colors, color blocks, paper,
   photo, or dark. The "Style directions" table has ten choices and most of them are not
   dark. The examples in this skill (light paper, nebula) are only examples, not locked
   templates.
   **The background is never static.** There is always background motion (§7c), and
   the background color MAY change whenever needed: the mood/topic of a segment
   changes (entering the product, problem → solution, claim → CTA), a colorful brand
   demands a color rhythm, or an on-screen action really changes it (a toggle is
   switched on, an object covers the lens, an icon grows to fill the frame). Only two
   things are guarded: the change has a visible trigger (wipe, object, UI action, push
   into a color field, cut on the beat), not an unexplained cross-fade that feels like
   "changing slides", and the background is not left a single still color just because
   it was never considered. The plan is written in the style brief.
6. **Free to express.** The laws here lock STRUCTURE (not slides), CONTRAST (text is
   readable), and NOVELTY (not repeating another project), not expression. Rich
   gradients, light, 3D, depth, texture, bold colors are encouraged when they suit the
   theme. Only taking the cheapest default and repeating it is forbidden: flat bars
   sweeping, lines crossing, flat backgrounds, another project's skin. If two choices
   both satisfy the laws, pick the bolder one.
7. **What may be the same across all jobs:** the anti-PPT laws, the camera rig,
   determinism, asymmetric enter/exit rhythm, the minimum text size.

### Style directions (pick one; two may be blended consciously)

| Direction | Background | Typography | Signature motion | Good for |
|---|---|---|---|---|
| Cinematic dark | near-black gradation, WebGL particles/nebula, bloom only on objects | clean bold grotesk | push-through, light in front of the lens | creative tools, gaming, technology |
| Poster color-block | large solid color fields changing per scene, no gradation | very heavy display, giant letters cropped by the edge | block wipes, text hitting the frame edge | consumer apps, music, events |
| Editorial light | white/cream, wide empty space, thin lines | display serif + small grotesk | gentle slides, lines that draw, a calm camera | productivity, finance, SaaS |
| Paper & print | paper texture, collage cutouts, stamps, tape | handwriting + serif | objects fly in then land, tilted angles | education, community, food |
| Retro / analog | faded color, grain, scan lines, VHS frame | 70s–90s geometric | controlled glitch, rough zoom, freeze | nostalgia, music, entertainment |
| Brutalist mono | black and white, hard grid, ruled boxes | monospace + condensed | hard cuts, shifting blocks, blinking cursor | developer tools, technical |
| Playful pastel | stacked pastels, big round shapes | heavy rounded sans | elastic bounce, blooming shapes | kids, health, lifestyle |
| Luxury dark | black + gold/bronze, soft shadows, shine | tall wide-spaced serif | slow motion, sweeping beams, depth | fashion, automotive, property |
| Flat pop with photos | light neutral alternating with solid fields in the user's brand color; flat shapes and stickers derived from the geometry of the user's logo + soft 3D illustration | heavy rounded geometric sans + giant words cropped by the edge | cut-out people photos popping up from below, stickers bursting elastically, color fields sweeping/snapping on the beat | consumer apps, fintech, e-commerce, youth brands |
| Grainy gradient | dark/deep-color base; saturated 2–3 color gradient shapes glowing from within; fine grain over the whole frame | small clean grotesk, or minimal heavy display | shape layers slowly opening/rotating, the camera passing through a shape's hole, a guiding light orb | tech, AI, music, fintech, creative launches |

Two openers in a row using the same table row is a warning sign; pick another row or
blend two rows in a way that has not been used.

## Law #4: Text is alive, the background yields

Two openers with the same rig can end up very good or very bad purely because of
typography and contrast. The bad: every title in ALL CAPS weight 800 in the center,
entering the same way, over a field of white light brighter than the letters. The
good: sentence case weight 500, emphasis on keywords (e.g. a pill + star; that is one
project's signature, not a rule, and word highlight itself is optional), punctuation
only when needed, size/direction/position alternating, a calm background under the
text, a background that changes by segment. Full recipes with code: `techniques.md`
sections 1 and 1b. In short:

- Sentence case at weight 500–600. Bold caps only for one emphasis scene.
- Titles, claims, and short phrases are DEFAULT NO PERIOD, especially phrases ≤ 4 words
  and one-line sentences. Punctuation only when it changes meaning or rhythm: `?` for
  a real question, a period for a deliberate style of two short sentences in a row,
  `!` very rarely. The punctuation style is decided once in the style brief and kept
  consistent; when used, it is a separate element that appears last.
- Word highlight (pill, underline, marker, box, color, strike-through) is OPTIONAL and
  decided in the style brief. Even without a highlight, a sentence still has emphasis:
  word by word from dim to full, size/weight, a pause, or an object (icon, UI) standing
  beside the word. When used: one form per video, not required on every sentence,
  different from other projects; ornaments only when derived from a brand shape.
- Two scenes in a row must not be the same in size, entry direction, and text position.
- In the TEXT POCKET (not the whole frame) the background must be DARK (≤ 25 %
  luminance) or LIGHT (≥ 80 %), never "medium busy". Outside the pocket the background
  should instead be rich: gradient, light, texture (§7d); flat single-color is
  rejected. Any background element (particles, shapes, textures, lines): colored from
  the dark side of the palette, opacity ≤ .35 in the text pocket, ≤ 40 bright
  elements visible.
- Consider alternating dark and light when a segment really changes mood; it is not a
  mechanical obligation.

## Workflow

0. **Identify the kind** ("Kinds of work" table). Explainer → open
   `references/explainer.md` and follow "Step zero" there: ONE question
   containing the style (five choices + a recommendation), ratio, length, sound,
   plus the length guard rail. Other kinds → continue; ask only what truly cannot be
   derived from the brief (ratio, length, whether there is music/VO), in one question.
0b. **Write the style brief** (Law #3) and show it with the rundown. Without an
   approved style brief, do not touch code.
1. **Absorb references & brand sources.** Ask for screenshots/clips of the reference
   if there are any; map per shot (duration, movement, transition type, attention
   order), only the RHYTHM, not the skin (Law #3). Colors, logo (the REAL vector paths,
   do not redraw), fonts, and feature claims come from the official sources of the
   PRODUCT being made, not from a reference, not from another project, not invented.
2. **Write the rundown from the chosen concept**, a table `second | scene |
   sentence | visual`. The number and kind of scenes follow the concept
   (`references/opener-concepts.md`), not the pattern hook → feature → feature →
   promise → logo → CTA. Total 25–40 seconds. Ask the user to approve this rundown
   before writing code; reworking a rundown is cheap, reworking code is expensive.
3. **Scaffold the architecture.** Opener/promo/bumper/typography: copy
   `assets/starter-opener.html` (1920×1080 stage, `#world` camera rig, a stateful
   Three.js scene, timeline helpers) then IMMEDIATELY replace the color tokens, font,
   and background language according to the style brief; the starter is deliberately
   gray. Explainer: copy the starter that matches the style:
   `starter-explainer-cartoon/-journalism/-catalog/-sketch.html` (collage
   mode: camera into/settle/look/home over cutouts/photos, say/unsay per word, draw
   annotations, push-through between scenes) or `starter-explainer.html`
   (continuous action: the world flows, hero, world objects, map view, whip). All of
   them already autoplay + loop with no player. The multi-file structure and the
   explanation of each decision are in `references/architecture.md`.
4. **Build scenes one at a time** with the recipes in `references/techniques.md`
   (per-letter split + directional motion blur, per-word 3D pan, transition menu, UI
   mockups). Recipes are tools, not a shopping list: use only what the concept demands.
5. **Verify VISUALLY, not just "the code runs".** You cannot watch a video; you can
   only see FRAMES. Capture 6–20 key seconds (the start of each scene, when text
   appears, transitions) with `scripts/snap.mjs` (puppeteer, opens `file://`, no
   server), assemble a contact sheet, and judge like a director: is text clipped?
   overlapping? does text appear before the camera has finished? does it still feel
   like a slide? Fix, capture again. DO NOT render all frames to check; that is
   thousands of images and not verification. Render the full thing only for the MP4
   export (step 6) when the user asks for it. Without Node: open `?debug=1`, scrub
   manually, take screenshots.
6. **Deliver as ONE `index.html` that can be double-clicked.** The final output must
   not need a server/Node: CSS and JS are written INLINE in the file (a local
   `<script type="module" src="…">` is blocked by CORS when opened through `file://`,
   an inline module is not), libraries from a CDN, assets (icons/images) relative in
   the same folder. The no-cache server (`scripts/serve.py`) is only a WORKING tool
   while editing, not a requirement for watching. No player on screen (see "Player");
   mention `?debug=1` for scrubbing. **Export MP4 only when the user asks for it**:
   `scripts/export-frames.mjs` renders every frame (60 fps) to PNG and then ffmpeg
   merges them. This way is free of frame drops but expensive, so it is not a routine
   step and not a checking tool.

7. **Explainers only: VO script + a request to record**: the closing message must
   include the complete VO script and ask the user to record/generate it and send the
   audio back to be synced. Details of the script format, recording tips, and retime
   are in `references/explainer.md` → "Handover".

## Checklist before delivering

- [ ] Style brief (theme, palette from the brand, a display font with character, one
      background language, signature move, special moment) written and approved
      BEFORE code
- [ ] No leftover starter placeholders (gray, system font, nebula when the style
      direction is different) and no copied reference skin (palette,
      font, texture, layout, sentences)
- [ ] Different from the previous opener/promo: at least three of palette, font,
      background language, signature move
- [ ] Opener/promo: three candidate concepts written and one chosen; structure
      fingerprint written and different from the previous opener; at most two canonical
      components (text zooming → exiting left, three tiles, typed input,
      push-through, light leak, logo + CTA in the center), each demanded by the concept
      (`references/opener-concepts.md`); the concept example was not copied
      (opening/closing differ from its example, ≤ 1 ✦ moment, transformed, palette and
      shapes from the user's brand)
- [ ] App/SaaS: at least one live UI act (assembled, used, producing a result) from
      the user's product components, not a still screenshot being zoomed
      (`references/opener-concepts.md` UI animation section); if the demo feels
      static, important clicks are followed by the camera (close → click → pull
      back/shift), not on every click (`techniques.md` §8)
- [ ] Alive text (Law #4): sentence case weight 500–600, clear emphasis,
      no automatic period (punctuation only when it changes meaning/rhythm),
      size/direction/position alternating between scenes;
      bold caps only in one scene. Word highlight only when the style brief chose it
      (not automatic on every sentence, not the pill + star inherited from another
      project)
- [ ] The background yields (Law #4): under text luminance ≤ 25 % or ≥ 80 %,
      background elements dim and dark-colored in the text pocket; grayscale test:
      no background as bright as the letters
- [ ] Transitions chosen at the boundaries that need them; not every boundary
      automatically given an effect, and not every effect removed. A sweeping object
      has meaning within the scene; speed, amplitude, and pauses were checked.
- [ ] Background surface from the §7d menu: ≥ 2 layers (base + light/texture/
      blob), colors from the palette, not flat single color, not pure black/white
- [ ] Object render style is one family (§7e), or its change is made a moment
- [ ] Photo opener: the photo source was agreed with the user (user photos / MCP
      generated / licensed stock), fictional faces when generated, brand logo/text
      added in code, photos animated (pop, parallax, container), not just Ken Burns
- [ ] When using grainy gradient/grain: the grain is still visible in the encoded MP4
      and the gradient does not band
- [ ] When using video: clips are placed through `clip()` (no `autoplay`/`loop`),
      wrapped in an animated element, the source agreed with the user, the `assets/`
      folder mentioned at handover, and the seconds containing clips were captured
      (`snap.mjs`)
- [ ] Background motion chosen from the §7c menu and DIFFERENT from the previous
      project; no bars/lines crossing sideways unless the theme is speed/flow and it
      was not used in the previous project
- [ ] The background moves in every scene (no still background); a background color
      change is allowed whenever needed as long as it has a visible trigger
- [ ] Passes the 8 points of "Structural prohibitions" (not faded sections, has a
      visual through-line, ≤ 2 text levels, motion every second, varied
      transitions, the right starter)
- [ ] No player on screen; autoplay; loop; `?debug=1` for scrubbing
- [ ] Opener: one main idea with no badge stacks; explainer: one event can hold
      several related beats and objects.
- [ ] Camera, cuts, and object motion chosen to fit the context; there is no
      obligation to move the camera in every segment. When the camera moves, the whole
      world moves with it.
- [ ] No long dead holds: an act without big object action gets a shot-size change
      to an element (wide ↔ medium close-up ↔ close-up) or a slow push;
      camera breathing alone does not count. On-screen labels sit outside the rig and
      are not clipped by the zoom
- [ ] Directional motion blur on all text entering/exiting
- [ ] The background is born from the theme (not automatically dark; light can be a
      gradient, soft colors, color blocks, paper), has depth (not one flat color), is
      NOT busier than the subject; background changes are decided per segment in the
      style brief and, if present, happen behind a wipe/cut
- [ ] Glow is used on objects (tiles, bars, decorative icons); text titles stay CLEAN
      (full white + a thin drop shadow), unless the user asks otherwise
- [ ] Display font ≠ UI mockup font; mockups use the product's real font
      (claim → how → result concept: all text uses the product's UI font)
- [ ] Zero uses of `Date.now()` / `Math.random()` in the render path
- [ ] Captured at key seconds (snap.mjs / ?debug=1) and looked at with the eyes,
      not a full render; MP4 only when asked
- [ ] Sound? The page holds on the first frame if autoplay is blocked and starts
      together with sound on the first gesture, never starting without sound; no
      launcher files (`.cmd`/`.bat`)
- [ ] Collage explainer: the camera has choreography (close-up → glide → zoom
      out), not just elements in/out. See explainer.md "Explainer camera".
      Cartoon stage: no frame with zoom < 1.08; the camera only
      moves inside a stage; between stages a cut or a 96/72 px slide
- [ ] Cartoon stage: joints are rotated through a manual transform proxy (no GSAP
      `transformOrigin`/`rotation` on joints, no `x/y` tween
      on a group that has a `translate`); each stage has ≥10 moving objects; zero
      captions; raster heads have blink + expression variants
- [ ] AE bridge build: CAM zeroed before parenting, all world layers
      parented to CAM, layers created back → front, body-part keyframes
      in parent space, a contact sheet of each stage + the master has been viewed,
      the closing message includes Ctrl+S + delete the test comp + the aerender command
      (`references/ae-bridge-higgsfield.md`)
- [ ] Explainer: the closing message includes the complete VO script + a request to
      record / generate it themselves and send the audio back to be synced;
      `vo-script.md` is saved in the project folder
- [ ] Explainer: style, ratio, length, and sound were asked in ONE
      question (except what the user already stated) before writing code;
      length follows the brief/VO; scene count follows the context, not length ÷ 6
- [ ] Default ratio 16:9 / follows the screen; 9:16 only when asked. No
      subtitles/captions unless asked. The reference's layout (panels, subtitles)
      is not copied, only its principles
- [ ] Action/speed topic explainer: one subject is present from beginning to
      end, the background keeps flowing, numbers live inside the world (the subject
      passes in front of them). See explainer.md "Fifth style: continuous action"
- [ ] Changing viewpoints: no three scenes in a row with the same
      angle; each fact gets its instrument (speedometer, map,
      elevation profile, map race, interior, front view). See
      explainer.md "Viewpoints MUST change"; the camera breathes
- [ ] No text under 30 px on the 1080 stage (body ≥ 44, label ≥ 34,
      credit ≥ 30), since it is watched on phones; ghost text and annotations vary,
      not always outlines / dashed circles
- [ ] Explainer: every person/company/place/product that is MENTIONED shows
      its photo in that scene (see explainer.md → "Mentioned entities")
- [ ] `index.html` opens directly through `file://` (double-click) with no
      server: inline CSS/JS, no local module `src`
- [ ] Numbers that change every frame (clock, counter) use
      `font-variant-numeric:tabular-nums` + `min-width` so the container
      does not change width

## Traps that have already claimed victims

Details and fixes are in `references/techniques.md` under "Traps":
a low bloom threshold → a white screen; an additive nebula → stacks up through the
bloom; a more specific CSS selector beats the initial `opacity:0` state → the element
appears ahead of its animation; a JS module cached by the browser → edits "have no
effect" (use a `Cache-Control: no-store` server); a flat 3D object rotated fully on
the Y axis → becomes a single line (sway it, do not rotate fully); the default SVG
filter box clips the tail of a blur (widen `x/y/width/height`).

## After Effects: directly through the Higgsfield bridge

When After Effects is already open, the Higgsfield `ae_*` MCP bridge is connected, and
the user asks for an animation/explainer to be built in AE, build it directly with
bridge commands. Read `references/ae-bridge-higgsfield.md`: the comp skeleton through
one small Lottie, a `CAM` null per stage (anchor & position zeroed BEFORE parenting),
illustrations from code-made SVG → 2× PNG (`scripts/ae/bridge/svg-assets.py` +
`svg2png.cjs`), characters as real jointed AE shapes
(`scripts/ae/bridge/character-rig.py`, about 90 ops per character), body-part keyframes
in parent space, verification through contact sheets (a relay when r2.dev is blocked).
The cartoon stage laws still apply in full. The bridge cannot save/render and cannot
reorder layers; say so and create layers from back to front. A 10-stage build is about
1 hour, 0 credits.

## Package contents

| File | When to read |
|---|---|
| `references/cartoon-stage.md` | CARTOON STAGE: one stage per scene, camera ≥1.08, cut/96 px slide, jointed rig + manual transforms, raster heads + local expressions, zero captions, flat palette |
| `assets/starter-explainer-stage.html` | cartoon stage EXPLAINER: stage system + a camera per stage, `J()` joints, `character()` (vector or raster head), 96 px whoosh, a two-stage example |
| `scripts/head-expressions.py` | a generated head → happy/worried/surprised variants + blink, made locally (pupil & mouth detection) |
| `references/ae-bridge-higgsfield.md` | BRIDGE: building a cartoon stage directly in AE through the Higgsfield MCP: bridge limits, traps (null 960,540; parenting to a keyframed CAM; reorder breaks), CAM-per-stage architecture, native rig, contact sheet relay, handover |
| `scripts/ae/bridge/svg-assets.py`, `svg2png.cjs`, `character-rig.py` | BRIDGE: illustration assets from code → SVG + manifest → 2× PNG (puppeteer); a ~90-op `ae_batch` generator for one jointed character |
| `references/anti-ppt.md` | before designing scenes |
| `references/opener-concepts.md` | OPENER/PROMO before the rundown: three candidate concepts, a menu of 19 concepts (including object relay, brand system showcase, claim → how → result, living UI ecosystem, flat pop with photos, through gradient shapes, and a product tour with claims, all derived from the brand's service/assets/product), layout-color-rhythm guidance, UI animation guidance for app/SaaS, photo-in-opener guidance (user input / generate via MCP), the feature menu, openings, closings, object-carried transitions without cuts, structure fingerprint: prevents a template skeleton |
| `references/explainer.md` | when an explainer/explainer video is requested (cartoon + VO, photo visual journalism, white catalog, vintage sketch, or continuous action; default 16:9, 9:16 only when asked) |
| `references/architecture.md` | when scaffolding / needing the reasons behind the structure |
| `references/techniques.md` | when building scenes & effects (including shot size §3b, grainy gradient §7d, the object render style menu §7e, and video as footage layers §9b) |
| `references/roadmap.md` | when developing this skill further |
| `assets/starter-opener.html` | starting point for OPENER/promo: architecture + tools (8 text doors, optional transitions); DELIBERATELY without an example scene order, the skeleton comes from `opener-concepts.md` |
| `assets/starter-explainer.html` | EXPLAINER continuous-action style (vector): flow mode (strip + hero + world objects) + map view + whip + a collage-mode example |
| `assets/starter-explainer-cartoon.html` | collage cartoon EXPLAINER: cream paper + grain + stains, illustration cutouts, Bricolage + Caveat, color pills |
| `assets/starter-explainer-journalism.html` | visual journalism EXPLAINER: black + grain, real photos + source tags, Barlow Condensed + Plex Mono, yellow/red highlighter, dashed annotations |
| `assets/starter-explainer-catalog.html` | white catalog EXPLAINER: faint grid, photo cutouts, Archivo Black + Caveat + Inter, yellow highlighter |
| `assets/starter-explainer-sketch.html` | vintage sketch EXPLAINER: sepia paper (CSS texture), multiply engraving cutouts, Playfair + Garamond + Cinzel, rust & gold |
| `scripts/serve.py` | no-cache dev server (optional, needs Python; only when using local modules) |
| `scripts/snap.mjs` | VERIFICATION: capture key seconds → contact sheet (optional, needs Node + puppeteer) |
| `scripts/vo-pauses.html` | detects VO pauses in the browser (a replacement for ffmpeg silencedetect, no install) |
| `scripts/export-frames.mjs` | EXPORT: render all frames → MP4, only when asked (optional, needs Node + puppeteer + ffmpeg) |
