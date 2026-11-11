# Anti-PPT: laws of scene design

This document is the reason this skill exists: a result that is "technically correct"
still fails if it feels like a PPT presentation.

## Why models always fall into the slide pattern

Models are trained to organize INFORMATION: title → explanation → supporting evidence.
That structure is great for documents and fatal for motion graphics.
A promo video does not explain. It **states**, one punch per shot,
and lets movement + music carry the emotion. If you feel
a scene is "missing information", that is actually a sign the scene is right.

## Violation → fix table

| Violation | Fix |
|---|---|
| Kicker "02 — FEATURES" + a 2-line title + 2 lines of body copy + 4 badge chips, in a left-right column layout | One sentence of ≤ 5 words top-center + one product object rising to the center |
| Three lines of big text holding three "WITHOUT …" claims | A 2-word headline + one way from the feature menu (`opener-concepts.md`): one feature demoed, words that swap, an object that transforms, shuffled cards, a tile grid… chosen per project |
| Product B's opener uses product A's opener skin (same palette, glow, nebula, font) because it was taken from the starter/an old project | Derive the style from brand B through the style brief: palette from B's logo/icon, a different display font, a different background language, a different signature move (SKILL.md Law #3) |
| All titles in ALL CAPS, wide font weight 800, always centered, entering with the same letter stagger: feels stiff | Sentence case weight 500, emphasis on keywords (word highlight is optional; it can also be word by word, size, pauses, an object beside the word), no automatic period (punctuation only when it changes meaning), size/direction/position alternating (techniques.md §1) |
| Every title/claim ends with a period, including two-word phrases: feels stiff and template-like | Default no period; `?` for real questions, a period only for a deliberate and consistent style of two short sentences (techniques.md §1 rule 5) |
| A field of 96 white light bars with bloom behind the title: a busy background, the text lacks contrast | A dark pocket under the text, particles in the dark side of the palette and dimmed, ≤ 40 bright elements, bloom only on objects (techniques.md §1b) |
| All openers dark with a nebula/particles, the background never considered per segment | A background from the theme (light gradient, soft colors, color blocks, paper, photo, or dark); changes decided per segment in the style brief and happening behind a cut/wipe (techniques.md §7b) |
| Every opener gives a highlight word (underline/pill) in every sentence, or uses the exact same pill + star as another project | Word highlight is optional and decided in the style brief; when used, one form per video chosen per project, not on every sentence, ornaments only from a brand shape (techniques.md §1) |
| An app/SaaS opener shows only a still screenshot being zoomed or panned | The UI is rebuilt from product components, used (a cursor, a finger, or a UI that reacts by itself), data fills in, the transition is carried by the UI (`opener-concepts.md` UI animation section) |
| A video pasted full screen with `autoplay loop`, running on its own clock, and other animation stops while the clip plays | The clip is placed through `clip()` as a footage layer tied to the timeline, wrapped in a container/device/frame that is animated too, with text and annotations still alive on top (techniques.md §9b) |
| Two openers for different products both have a background of bars/pieces of light shooting sideways ("lane" / "range"), the result of the rule "an object crosses every second" | Background motion picked from the techniques.md §7c menu (drifting gradient, blobs, live grain, light sweep, rotating shapes, rising particles, breathing grid…) and different from the previous project; horizontal flow only for speed/flow themes |
| Transition: a giant flat-color block/square sweeping diagonally at every cut ("a weird square box"), or a thin line sweeping | The techniques.md §4c transition menu: 3D push-through, a card spinning from depth, a thick object passing the lens, a brand-shape mask, a light sweep; at least two kinds, one with depth, wipes ≤ 2 |
| A flat single-color background (dark or light) from start to finish | A background surface of ≥ 2 layers from the §7d menu: horizon glow, diagonal duotone, mesh blobs, spotlight + tint, a layered sky, texture, with colors from the palette |
| A still background, or a background color that never changes even though the segment/energy changes | The background always moves (§7c); the background color may change whenever needed as long as there is a visible trigger: an object covering the lens, a UI action, a push into a color field, a field sweeping, a cut on the beat (techniques.md §7b) |
| Copying the palette, font, and layout of a reference video the user supplied | Take only its rhythm and energy; the skin is born from the product's theme. Tell the user in one sentence |
| Showing `com.example.app` (a package name) in the CTA scene | Removed. The user does not care; if needed, a store search result line is enough |
| Text in/out with a static camera | The shot size changes to the element that is telling the story (techniques.md §3b) + choreography of overlapping elements (§4b); camera breathing as a base layer; push-through only when motivated, about 1 per video |
| "Zoom in-out" done as a few percent of camera breathing: invisible, the video still feels static | A clear shot-size change: the camera moves in to an element (medium close-up / close-up) then pulls back to wide when the composition needs the whole frame; labels on the screen layer so they are not clipped (techniques.md §3b) |
| A thick 4-layer glow on all titles | Clean white titles + a thin drop shadow; keep glow for OBJECTS (product objects, ornaments) |
| A warp background of 520 long white lines | 300 short particles in a matching dark color: the background must not compete with the subject |
| A flat, even blue background | A firm vertical gradation: nearly black at the top, glowing at the bottom horizon |
| A UI element (a status badge) appearing ahead of its main sentence | Attention order: sentence → main object → supporting detail |
| A push-through zoom used in ALL transitions | A motion library: spin, 3D yaw, roll, an element flying past the lens; zoom only when motivated (e.g. diving into a mockup screen). "One kind of transition on every cut" = a PPT transition template, just an expensive version |
| Translational whip-pan: the stage edge is exposed as a black gap | Reads as "turning the page". Never shift the world so far that its edge shows |
| Sudden spin/yaw/roll (a sudden zoom+rotate with blur at every cut) | That is the language of video editor PRESETS, not motion design. Replace with: a breathing camera + overlapping element choreography + object wipe |
| A static-feeling UI demo: the whole UI in frame, a still camera, only the cursor moving, clicks too small to read | The camera follows the interaction when needed: approach the area about to be clicked (scale 1.4–2.2, 0.6–0.9 s ease in-out), the click reads, then pull back/shift to the result; not on every click (techniques.md §8) |
| Openers for different products come out with the same skeleton: text zooms then exits left, three feature tiles, a typed input box, hook → feature → feature → promise → logo → CTA: it feels like a template even with new colors | Three candidate concepts from `opener-concepts.md`, one chosen from the nature of the product; a structure fingerprint different from the previous opener; at most two canonical components and only when the concept demands them |

## Common failure patterns in explainers

An example 30 s history explainer, 6 scenes, that felt like PPT. Its code:

| What was made | Why it is PPT | What it should be |
|---|---|---|
| 6 × `<section class="scene">` holding full-bleed photos, switched on by `autoAlpha` in turn | Changing sections = changing slides, whatever the transition | One flowing world; scenes change because the camera/world moves or whips to another corner |
| Each section: eyebrow (kicker) + a 2-line title + credit | Three text levels = slide layout | One big number/sentence + one label that lives in the world |
| Motion only a photo Ken Burns 1.08 → 1.015 and a `#world` scale bump 1.12 → .96 at every cut | The same motion on all cuts = a template | Parallax, objects crossing, whips, instruments (map/profile/speedometer), a camera that breathes differently per moment |
| A light leak on every cut | A video editor preset | Save it for one special moment |
| No subject persisting between scenes | Nothing is "carried" by the viewer | A hero present > 60 % of the duration |

Lesson: narrative laws alone are not enough; you need structural prohibitions that can be checked from code
(SKILL.md → "Structural prohibitions") and starters that force the right rig
(`assets/starter-explainer.html`).

## Principles that carry to any project

1. **One shot = one statement.** A sentence of ≤ 5 words is stronger than
   a full sentence. "Two words. One punch." beats "This app
   can do X, Y, and Z for you".
2. **Attention hierarchy per scene:** sentence first, main object next,
   detail last. Never reversed.
3. **Long text is a bug.** If a claim needs > 6 words,
   split it into two scenes or turn it into a visual (icon, number, mockup).
4. **Metadata is not content.** Package names, long URLs, versions, footnotes:
   drop them. A lay viewer does not read them, a technical viewer does not need them.
5. **A UI mockup is the exception to heavy text.** An app screen may be full of
   small text because it is read as a PICTURE, not as text. For that very reason, the
   mockup must be faithful to the real app (font, colors, layout).
6. **Movement is a sentence too.** Zooming in = emphasis; panning along =
   gradual revelation; pulling back = reveal; a small bounce = playful.
   Pick movement that means the same as the sentence, not random.
7. **Transitions like a motion designer, not an editor preset.** Two common
   failures: a translational whip exposes the edge ("turning the page"); a sudden
   spin/yaw reads as an editor preset effect. The right way:
   (a) the camera BREATHES, a slow endless zoom drift that never
   jolts; (b) the change is done by ELEMENT CHOREOGRAPHY, elements exiting and
   entering overlapped in time; (c) OBJECT WIPE, an element/ornament sweeps
   near the lens to cover the frame and the scene changes behind it; (d) a fast zoom
   only when MOTIVATED (diving into a mockup screen). Any sudden effect
   (a sudden zoom/rotate + blur at every cut) is a warning sign.
8. **The camera is the unifier.** Once you have a camera rig that moves
   the whole world, separate scenes feel like one film. Without it,
   however much polish each scene gets, the result is still an autoplayed deck.
9. **Asymmetric enter/exit rhythm.** Enter slow and firm (0.7–1.3 seconds,
   `power4.out`), exit fast (0.35–0.55 seconds, `power2.in`). Symmetric
   feels mechanical.
10. **Pick 1–2 special moments.** The most expensive effects (per-word 3D pan, logo
   build-on) are used once or twice only. Used everywhere,
   they stop feeling special.
11. **When in doubt, darken the background and enlarge the text.** Contrast is the
    cheapest production value and the one most often forgotten.

## Taste calibration (quick heuristics)

Screenshot a frame and ask:

- Could this frame be a corporate slide unchanged? → fail, rework.
- Does my eye know where to look within 0.2 seconds? → if not,
  reduce elements.
- If all text is hidden, is the background still interesting but not
  noisy? → both must be yes.
- Is something MOVING because of the camera, not because an element
  animates itself? → must be yes at every transition.
