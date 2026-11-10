# Roadmap: development document for this skill

Written so that anyone (human or AI) who opens this skill later
knows where it came from, what has been proven, and which way it is being refined.

## Composition principle

The laws in `anti-ppt.md` and the recipes in `techniques.md` start from one
problem: results that feel like a presentation. The composition principle:
**only generalized lessons go into the skill**, not
the colors, brand, or sentences specific to the project they came from.

## What has been proven (do not go back on this)

- The one-sentence-one-object-per-scene law
- The `#world` camera rig (the background gets zoomed too); push-through only when motivated
- Per-word 3D pan as a rationed special effect
- Directional motion blur via an SVG filter
- Full determinism → exact scrubbing + frame-by-frame export
- Visual verification with scrub-screenshots before delivering
- Interrogating the real brand sources (vector logo, color tokens, feature claims)

## Development directions (in rough priority order)

1. **Real audio.** Right now the spectrum/beat is procedural (sine + constant BPM).
   Add a path: load an audio file → precompute the FFT per frame (offline, once)
   → save JSON → deterministic playback stays intact. DO NOT analyze
   in real time in the render loop; that kills determinism and export.
2. **A transition library.** There are only push-through, 3D pan, and light leak so far.
   Candidates: horizontal whip-pan, roll (rig rotation), rack-focus (blur
   swapping between two layers), shape match-cut (a spectrum circle → a
   round icon), zoom-through of the letter O/a logo hole.
3. **A concept menu, not a rundown template.** Rundown templates per genre
   (e.g. hook→feature→feature→promise→logo→CTA) tend to make all openers
   share one skeleton. What gets developed is the menu in
   `opener-concepts.md`: add new concepts from accepted projects,
   do not add fixed orders.
4. **A multi-file starter.** `assets/starter-opener.html` is deliberately one file so it is
   easy to copy; also provide a split version (structure in
   `architecture.md`) once the skill ecosystem supports template folders.
5. **Smoother export.** Alternatives to puppeteer: `MediaRecorder` +
   `canvas.captureStream` (fast, lower quality), or WebCodecs
   `VideoEncoder` (best, needs more code). Also an ffmpeg preset for
   vertical 1080×1920 (change the stage constants → all recipes still work).
6. **Review accessibility.** A small script that automatically screenshots
   N key moments (`tl.time(x)` → capture) and builds a contact sheet,
   speeding up the visual verification loop that is manual today.
7. **Further taste calibration.** Collect more failure→success pairs from
   later projects into the table in `anti-ppt.md`.
   That table is this skill's most valuable asset.

## Anti-patterns that are tempting but should be avoided

- **Making the starter hold example content that is too finished.** The model will
  copy its style raw. A starter must be plain in content, and
  plain in ORDER: no example scenes whose skeleton can be imitated.
- **One right answer per failure.** A failure → success table that holds
  only one fix becomes a new template. Write fixes as a menu
  (see `opener-concepts.md`).
- **Adding effect after effect.** Every new effect must pass a test: is it
  a camera move / a revelation of meaning, or just a gimmick? Gimmicks age
  within months.
- **Writing MUST/DO NOT without a reason.** This skill's format: rule + why +
  an example of the failure. A rule without a story will be broken by the next model.
- **Locking to one library.** GSAP + Three.js are the default choice,
  not an identity. The principles (camera, determinism, anti-PPT) apply to
  Remotion, Motion One, or plain canvas too.

## Using this skill with another AI

This folder is portable: `SKILL.md` + `references/` + `assets/` + `scripts/`
are just markdown, HTML, and scripts. For an AI without a skill system:
paste the contents of `SKILL.md` as instructions, attach `anti-ppt.md` +
`techniques.md` during a design session, `architecture.md` during a coding session,
and give `starter-opener.html` as the code starting point.


## Already done

- Explainer: two styles (cartoon+VO, photo journalism without VO) in 9:16:
  `references/explainer.md`. There is no explainer-specific starter yet; the next
  candidate: `assets/starter-explainer.html` (9:16 stage, say/unsay/photo/draw/cut/tint
  helpers, syncAudio) so it need not be rewritten.
- A single-file deliverable with no server; synchronous `seek()`; tabular numbers.
