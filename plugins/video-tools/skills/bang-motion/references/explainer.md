# Explainer: an illustrated story, not a promo

For a flat educational cartoon with characters (style 6, **cartoon stage**: one stage
per scene, a jointed rig, zero captions), read [cartoon-stage.md](cartoon-stage.md).
The number of sentences does not determine the number of shots; more camera movement
is not automatically more interesting either. The collage recipe sections below are
an option, not a mandatory pattern for every explainer.

The two explainer styles used most often:

| | Cartoon + VO | Visual journalism (photo) |
|---|---|---|
| Good for | science/education, ±75 s, 9:16 | news/geopolitics, ±75 s, 9:16 |
| Background | textured cream paper + color stains | pitch black + thin grain |
| Pictures | generated flat illustration (GPT Image 2), then the background removed → cutouts | real freely licensed photos (Wikimedia Commons, NASA, DVIDS) |
| Text | heavy Bricolage Grotesque + Caveat (handwriting) | heavy Barlow Condensed + IBM Plex Mono (kicker) |
| Accent | color pills (orange/teal/red/mustard), marker scribbles | yellow highlighter, red for warnings, dashed lines |
| Sound | VO tied to the timeline | no VO: text carries the story, 3–5 s beats to read |

An opener sells one feeling; an explainer **delivers one argument**. The anti-PPT laws
still apply, but with two allowances: a scene may have a sentence + one
number/annotation, and a mockup/map/chart may be "dense" because it is read as a picture.

## Step zero: settle the style, ratio, length, sound

Users often just say "make an explainer about X". Left alone, the model invents the
style, ratio, AND length, which could come out as 10 minutes. Before writing anything,
ask ONE question (use your agent's question mechanism if it has one; otherwise write the
list and wait for an answer) holding four things. Skip the parts the user has already
named; if there is a reference video, the style is taken from it (its rhythm; see
SKILL.md Law #3).

**Style** (include a one-line recommendation: history → 4 or 1; news → 2;
product → 3; motion/route → 5; science/education with characters → 6; a light topic → 1):

| # | Style | Feel | Good for | Assets |
|---|---|---|---|---|
| 1 | Collage cartoon | cream paper, flat illustration cutouts, color pills, handwriting | science/children's education, light topics | generated illustrations → background removed |
| 2 | Visual journalism | black, real photos, yellow highlighter, source tags | news, viral issues, geopolitics | freely licensed photos (Wikimedia/NASA) |
| 3 | White catalog | white with a grid, photo cutouts, mixed typography, scribbles | products, brands, company profiles | product/people photos, background removed |
| 4 | Vintage sketch | sepia paper, engraving/etching, classic serifs, rust annotations | history, biography, inventions | generated engraving-style illustrations |
| 5 | Continuous action (vector) | the world flows, one subject, numbers inside the world, changing angles | speed, routes, transport, sports, processes | 100 % hand-drawn SVG, no generation |
| 6 | Cartoon stage | bright flat, one stage per scene, jointed characters acting, machines/water/plants alive, no captions | science/social education with characters, process & impact, stories | vector body & world; the head is generated → local expressions |

**Three other things in the same question:**

| Item | Choices | Default if "whatever" |
|---|---|---|
| Ratio | 16:9 (YouTube/screen) · 9:16 (Reels/TikTok/Shorts) · 1:1 | 16:9 |
| Length | 30 s · 60 s · 90 s | 60 s |
| Sound | no sound · VO sent by the user later (build first, retime later) · music only | no sound, the VO script is still written |

What is NOT asked: captions (default none) and a player (default none,
autoplay + loop).

**Length guard rail:** follow the brief and the VO length; the default stays concise.
The number of scenes is determined by the context that changes. Several sentences may
share one world with a developing activity. Excess material is cut, the video is not
lengthened. A "10 minutes" request → confirm, then split
into chapters of ≤ 90 s as separate files.

## Handover: the VO script goes in the message, the user fills in the voice

An explainer almost always ends with a VO from the user (recorded themselves or
generated on the TTS service of their choice). So the fixed order: build with no sound
at reading timing → hand over `index.html` + the VO script IN the
closing message → ask the user to record/generate and send the audio back → retime the
video to that audio. An example closing:

> VO script (one paragraph = one scene, numbers written as words):
> 1. …
> 2. …
> Record or generate it with the voice of your choice: speak naturally, pause ±1 second
> between paragraphs, any wav/mp3 format, then send it here; I will
> sync the video to that voice.

The same script is saved as `vo-script.md`. Do not just write
"the script is in the file": the user reads the message, not the folder.

## Start from the right starter

An explainer ALWAYS starts from the starter for its style (the `assets/` folder):
`starter-explainer-cartoon.html`, `starter-explainer-journalism.html`,
`starter-explainer-catalog.html`, `starter-explainer-sketch.html`, or
`starter-explainer.html` for continuous action. All five share one rig; only the
SURFACE differs (background texture, asset type, font, colors). Two motion modes:

| Mode | World | Main motion | Styles that use it |
|---|---|---|---|
| FLOW | a parallax strip flowing from a speed profile, the subject still in frame, world objects crossing | the world moves | continuous action (vector) |
| COLLAGE | a still paper/photo/white sheet holding cutouts & photos, may be larger than the frame | the camera: `into` → `settle` → `look` → `home` then STILL; assets `fly` and keep swaying | collage cartoon, photo journalism, white catalog, vintage sketch |

The two may be mixed in one video (e.g. collage for history, then a whip
to a simulation map). The collage starter already holds the mandatory choreography
example: start with a close-up of asset A → `look` to asset B → `home` (zoom out
finished) → only then `say` the sentence + `draw` annotation + labels → `unsay` → `into`/`settle`
push-through to scene 2, which sits outside the frame (not a faded
section).

A scrub trap: GSAP's `tl.pause(t)` suppresses callbacks (`suppressEvents`), so
`onUpdate: applyCam` does not run during a snapshot/scrub even though it runs in normal
playback. `seek` must be `tl.pause(t,false)` then `applyCam()`. What is not allowed:
writing from scratch or from the opener starter; that almost certainly ends in
"faded sections".

## Defaults often mistaken

- **Ratio: default 16:9 (1920×1080) or following the user's screen.** 9:16 ONLY
  when the user asks (Reels/TikTok/Shorts). Do not assume explainer =
  vertical.
- **No player.** Autoplay + loop; the scrub panel only with `?debug=1`.
- **No subtitles/captions.** By default there is no text accompanying the VO at the bottom
  of the screen; captions only when the user asks. Information is carried by big numbers,
  labels that live inside the world (name signs, station signs), and pictures.
- **Learn the reference's principles, do not copy its layout devices.** A three-column
  panel, bottom subtitles, an odometer shape: if the reference uses them,
  they are examples, not recipes. Take the principle (numbers in the world, a subject
  that keeps moving) then realize it your own way.
- **The stage is scaled to the window with `position:absolute; left:50%;
  top:50%; transform:translate(-50%,-50%) scale(s)`**, not a `place-items:center`
  grid: the grid cell follows the raw stage height, so the stage is pushed
  down and clipped.

## The structure learned from references (not imitated)

A good collage explainer and a visual-journalism explainer share
the same bones, and these bones may be reused:

1. **Hook** = one picture + one claim that creates curiosity (viral, a
   strange number, a question).
2. **An explicit question** on screen ("Why is that possible?", "Why this year?").
3. **Visual context**: a map / location photo / world illustration, with a label
   and one red circle at the key point.
4. **A big number** that counts up, then is compared (a before/after bar).
5. **A timeline** of 2–3 dates, one sentence per date.
6. **A chart** that draws itself (a price line, the area beneath it).
7. **Impact on the viewer** ("felt in the everyday wallet").
8. **A closing that echoes the hook** + a small list of sources.

Do not take: the palette, font, exact layout, mascot, sentences. Replace them all.

## One scene = 3–5 stacking elements (not one picture)

A common failure: each scene has only ONE cutout + one sentence. Even if the camera
moves, the viewer does not know "what it looks like" for the thing being told; one
symbol does not explain enough. A good journalistic explainer (±20 beats per
30 s) uses this pattern:

1. **Accretion per phrase.** Each VO phrase ADDS one element; the old elements
   stay in place. The scene ends with 3–5 elements (maximum 5) that
   explain together: a subject (photo/cutout) + evidence (document, clipping,
   screen) + scale (a number or a repeating grid) + a label/date stamp +
   scribbles. Example "the enemy's message cannot be read" = a ship → a submarine crossing
   → an eavesdropping radio → a telegram sheet holding a cipher that keeps changing + a
   SECRET stamp → the sentence.
2. **Evidence, not decoration.** Pick elements that answer "what does it look
   like?": a typed document with a stamp (case name · GUILTY),
   a newspaper clipping with a highlighted phrase, a source card (media badge + headline),
   a screen/mockup, a date block. Documents are built in HTML (white paper +
   thin border + mono + a tilted red stamp), with no need to generate them.
3. **Repetition for scale.** One picture multiplied into a grid (a schoolchild photo
   becomes dozens; one machine rotor becomes 12 rotors)
   with a `back.out` stagger, which is felt more than a number alone. The number
   is still there, but not the only thing.
4. **Photo → document.** The photo zooms out and turns out to be on a magazine /
   newspaper cover; a year block appears beside it. One asset, two meanings.
5. **Elements that move by themselves** (deterministic from `tl.time()`):
   cipher letters changing then resolving into readable text, clock hands racing to
   midnight, a number counting up, a judge's gavel striking.
6. **The camera stays one per scene**: elements stack in the same area;
   the camera `look`s slightly (±200 px, z 1–1.15) to welcome the new element.
   New element = a small look, not a cut.
7. **The text limit does not change**: one big sentence + one label per scene.
   Documents/stamps/date blocks/handwritten notes count as OBJECTS (read as
   pictures), not text levels; the condition is contents of ≤ 3 short lines.
8. **Quick extra assets**: photoreal props "studio product photo,
   isolated on pure white" (Higgsfield `gpt_image_2_5`, with no real
   people's faces) stacked with `mix-blend-mode:multiply`: the white background vanishes
   over the grid without removing the background. Do not give `drop-shadow` to a multiply
   element (the shadow becomes a square); the shadow is already in the photo. Archive photos
   with a complicated background still go through `image_background_remover` (needs a `prompt`),
   then trim the transparent margin (alpha bbox) so the CSS size = the contents.
9. If `remove_background` removes the subject (the ship vanishes, leaving the bow of
   another ship), do not force it; generate a replacement prop.

Helpers in `assets/starter-explainer-catalog.html`: `slam` (a stamp
slammed down), `block` (a date block revealed from the left), `multiply` (a grid
in sequence); CSS `.doc`, `.stampblk`, `.pnote`, `.grid`, `.cut.card`.

## Technical recipes

**A 9:16 stage**: `#stage` 1080×1920, `fit()` the same as 16:9. Titles
88–168 px, mono kicker 26 px, photo credit 20 px bottom-left.

**Sentence per word** (`say/unsay`): each word is a `<span class="wd">` (nowrap)
entering `yPercent 60→0, scaleY 1.3→1`, stagger 0.07–0.12, vertical blur;
a keyword is `<span class="wd hl"><i></i>word</span>`: the `<i>` is a
highlighter that goes `scaleX 0→1` from the left AFTER its words finish
(`hlAt`). A phrase that must be able to wrap lines must NOT be made one `.wd`
(that is why text overflows the frame at 9:16).

**Photos** (`photo(sel, at, end, {from,to,x,y})`): `object-fit:cover`, entering
with directional blur, then Ken Burns `scale 1→1.12–1.25` + a slight shift
across the scene (`ease:'none'`). A dark gradation at the top/bottom (`.dim`,
`.top`) so text has contrast. Light grain `mix-blend-mode:overlay`.

**Illustration cutouts** (`enter/leave`): entering from below with a `back.out(1.4)`
overshoot, drop-shadow on the wrapper element. Put the color filter (grayscale)
on the `<img>`, not the wrapper: `blurTween` writes `filter` on the
wrapper and removes other filters.

**SVG annotations** (`draw`): `strokeDasharray = L`, `strokeDashoffset L→0`.
Set `opacity:0` until its start second; a round linecap at length 0 shows up
as a stray dot. Dashed lines cannot use dashoffset (they would
"walk"); use a `clip-path: inset()` that opens from the left (`drawDash`).

**Maps**: a public-domain satellite image (NASA MODIS/Worldview) as the base +
mono `.tag` labels with a yellow left line + a red circle + a dashed
route line. More honest and faster than drawing your own map.

**Line charts**: compute points from the data in JS, draw the `path` with
dashoffset, a gradient area fading in after, data points popping in a stagger, labels
only for 2–3 key points (the start, the peak, the last).

**Big numbers**: tween an object `{v}` → `textContent = Math.round(v)`;
`font-variant-numeric: tabular-nums`.

**Tint per scene**: a full-frame `.tint` layer (night/cold/dark) inside
`#world`, its opacity tweened: cheap and immediately changes the mood.

**Cuts between scenes** (`cut`): push the world 1.05× then the new scene is
born at 1.08–1.12× and settles to 1 in 0.8 s; the old elements exit upward with blur
WHILE the new ones enter. The camera keeps breathing in between.

**Retiming to a VO that arrives later** (the video was designed first with no sound).
Without ffmpeg: open `scripts/vo-pauses.html`, pick the audio, copy `SEG`
(the start of each speech segment), `PARA` (the start of each paragraph = a scene) and
`DUR`; the numbers are identical to `silencedetect` (threshold -30 dB relative to the
peak, pause >= 0.45 s, paragraph >= 0.8 s; change if the VO is noisy).
The steps:
do not rewrite build(). Wrap `tl.to/fromTo/set` with a linear position mapping
per scene `T(t)` from the old scene boundaries (OLD) to the VO paragraph starts
(NEW, from silencedetect pauses ≥0.9 s; a noisy VO needs a
−25 dB threshold). Tween durations stay; only their positions stretch. Push-through
transitions are computed directly in the new time (`T(cut)-.9`) so they stay
precise. One VO file is easier than eight clips.

**VO tied to the timeline** (if there is one): an `<audio>` per clip + `syncAudio()` in the
rAF loop: if the timeline is playing and `t` is inside the clip's range → `currentTime =
t - start`, play; otherwise → pause. A first "Start" button is needed because of
autoplay. Scene duration follows the clip duration (measure first with ffprobe).

## Image sources

- **Generated** (cartoon): Higgsfield `gpt_image_2` (1k, medium), a prompt
  of one style for all assets ("flat vector, thick brown outline, warm colors,
  plain white background"), then `remove_background` → a transparent PNG.
  Generate in one batch so the style is uniform.
- **Real photos** (journalistic): the Wikimedia Commons API
  `action=query&generator=search&gsrnamespace=6&prop=imageinfo&iiprop=url|extmetadata&iiurlwidth=1920`
  → check `LicenseShortName` (Public domain / CC BY / CC BY-SA), download the 1920 px
  thumb, write the credit on screen. NASA (MODIS/Worldview) and DVIDS/DoD
  are public domain. Do not use news/TV screenshots.
- If an exact location photo does not exist, use a similar photo and label it
  "illustration"; do not pretend.
- **Supplementary video**: 3–8 s clips as footage layers (`techniques.md` §9b), from the user,
  licensed stock, or generated through the MCP if approved (a label "illustration/reconstruction" on
  factual topics). A clip is still wrapped in the scene design: cards, frames, annotations, numbers.

## Mentioned entities MUST be shown (a crucial rule)

A common failure: a company name is said without a photo of the company, an
inventor's name is said without their face, "17 factories" without the factories, a product is said
without its packaging; the viewer cannot link the word to a picture. The procedure:

1. From the script, write an **entity list**: people, companies, buildings/cities,
   products/variants, events. Each entity = one picture in its scene.
2. Source order: a freely licensed photo (Commons/NASA) → an official photo from the
   product site/article (the page's `og:image`, credit stated) → a photo sent by the
   user → a photoreal generation labeled "illustration" only for generic places/objects
   (a factory, a production line), **never** for the faces of real people.
3. A photo of a person from a composite/meme (e.g. a viral screenshot) may be cropped
   and have its background removed into a cutout; the result actually suits the collage
   style. State the source.
4. If everything fails, ask the user before using a silhouette/placeholder.

## Readability on phones (a hard rule)

An illustration caption of 22 px and a name sub-label of 26 px are nearly unreadable,
let alone on a phone. A 9:16 video is watched on a screen of ±6 inches,
and a safe-area scale of 0.78 shrinks everything again. The MINIMUM sizes on a
1080 px stage (before the safe-scale):

| text kind | minimum |
|---|---|
| body copy / caption | 44 px |
| name label, kicker, year | 34 px (sub-label 32 px) |
| credit / source | 30 px, enough contrast (opacity ≥ .6) |
| handwritten annotation | 48 px |
| title | 100 px and up |

If using safe-scale, multiply by 1/0.78 first. There is no text under
30 px, period. If some information "does not fit", split it into another scene
or drop it; do not shrink it.

## Variation, not a fixed pattern

Two habits that make a video feel "always the same":

- **Ghost text / giant year numbers**: pick ONE style for one video
  (an outline in one scene and a fill in another feels
  inconsistent), and make sure it is visible: a transparent fill ≥ .18–.25, not
  .08–.12 because that blends into the background. Other styles (outline, blur, cropped by
  the edge) are used in other videos, not mixed within one video.
- **Circles / annotations** do not have to be dashed. Alternate: a thin solid
  line, an accent-color line, a double line, a corner box, a hand underline,
  or no circle at all.

## Assets must feel alive

A cutout swaying ±10 px for 2 s looks static. Minimum:
a sway of ±22–28 px with a duration of 1.3–1.8 s (`sine.inOut`, yoyo), plus
a small rotation of ±1.5° and a slow scale growth 1→1.06 across the scene,
and an x shift of a dozen or so px. Give a different phase/duration per object so
they are not in unison. For big objects (a ship, a city) add directional motion
(sailing, a camera push) with `ease:'none'`.

## The collage camera recipe: close-up → glide → zoom out

The general shot-size principle for all kinds of video is in `techniques.md` §3b.
This is one recipe for text collage. For character/process animation, the camera may
rest, follow the subject, or travel along the system after the initial reveal. Do not
force this recipe on every segment; use the narrative's need as the reason.

This recipe answers three common failures: (a) animation that is only
"elements enter, elements exit" feels PPT; (b) after the camera zooms out and then
pushes in again to a note, "other info gets clipped"; and a direct cut from
wide to close-up "feels sudden because the background suddenly zooms in".

- The `#world` rig = the camera: a state `C={x,y,z}` (the focus point in scene
  coordinates + zoom), applied every frame: `transformOrigin:'0 0'; scale:z;
  x:540-sx*z; y:960-sy*z` with (sx,sy) the focus point after the safe-scale.
  A helper `look(at,x,y,z,dur,ease)`; `HOME` = the identity position (the center of the frame,
  z 1), computed from the safe-scale, not just (540,960).
- **Pattern per scene**: born in a close-up of the first asset (z ≈ 1.4, settling
  to 1.32) → glide to the second asset as it enters → zoom out to HOME when the
  title appears → **hold still** at HOME until the transition. No more pushing
  after the zoom out; notes/routes just have their elements animated.
- **Transition = push-through** (not a jump): 0.9 s before the cut, the old elements
  have gone and the camera pushes (`power2.in`) to the point of the next scene's first asset;
  exactly at the cut the new scene is born in that framing and the camera
  settles (`power3.out`). A continuous background makes the cut unnoticeable.
  The first asset must already have entered ≤ 0.1 s after the cut so the close-up is not
  empty.
- **Mandatory order: the zoom out FINISHES first, then the text appears.** The reason:
  text born together with (or before) the zoom out "feels
  clipped". Title, body, year label, handwritten notes: all
  scheduled ≥ 0.1 s after `home()` finishes. The zoom out is kept short
  (1.0–1.2 s) so there is still time to read; if it does not fit, drop a
  sentence (an opening sentence already carried by the VO is the first candidate).
- Panoramas (a city, a ship): a pan travelling along for 2.5–3 s at z 1.3–1.5, then to
  HOME. Objects entering from the side are "welcomed" by the camera moving along.
- Required: the background/paper far larger than the frame (`inset:-1400px`) and the
  vignette OUTSIDE the rig; do not stack another scale tween on the rig (camera
  breathing is replaced by this choreography).

## Social formats (IG Reels / TikTok / Shorts)

- **Safe area**: wrap all scenes in `.safe{transform:scale(.78);
  transform-origin:50% 45%}` → a top margin of ±190 px, bottom ±230 px at
  1080×1920 so they are not covered by captions/navigation. The grid/background stays full.
- **No controls**: no Play overlay or slider. R = replay,
  space = pause. `?clean=1` is still there for rendering.
- **Sound must be audible from the start.** Browsers block autoplay audio without a
  gesture (also on `file://`), and users take "the sound did not appear"
  for a bug. Two layers:
  1. On the page: try `vo.play()`; if it succeeds → play from 0 with sound.
  2. If it is refused: **DO NOT start without sound**. Hold on the first frame with
     a small hint "tap / press any key", then the first gesture
     starts the video + sound together from 0. (Playing the visuals first and then restarting
     on a tap feels like the sound is missing.)
  Do not make a launcher file (`.cmd`, `.bat`, a shell script) to force
  autoplay; the deliverable is just `index.html` (+ `assets/`). The
  play-muted-then-unmute trick does not work either: unmuting without a gesture is still
  blocked.

## Facts

A news explainer must have sources: search first (EIA/official institutions, major media,
Wikipedia Current Events for dates), keep the list of sources in the README
and show a summary on the closing card. Numbers that are not verified
are not shown; write only the qualitative claim.

## Traps that have already happened

| Symptom | Cause | Remedy |
|---|---|---|
| A sentence overflows the 9:16 frame | one long phrase made into one nowrap `.wd` | split per word |
| A phone mockup covers the 3rd line of the title | the phone position was computed for a 2-line title | measure the real title height, the phone starts ≥ 60 px below it |
| A cutout stays colored even though it was given grayscale | `blurTween` overwrites the wrapper's `filter` | the color filter on the `<img>` |
| A stray red dot before the scribble is drawn | a round linecap at dash length 0 | `opacity:0` until `draw` starts |
| A WebGL canvas background is not needed | a 2D explainer | skip Three.js; the `#world` rig + tint + grain is enough |


## Third style: "white catalog" (photo cutouts on a white background)

Style traits: a white background with a thin grid, product cutouts, objects flying past the
lens, dashed circles, script typography + heavy italic sans.
Good for product or brand explainers (±60 s, 9:16, no VO) with real
colors and photos, not black and white, not cartoon.

- A `#fff` background + a 120 px grid `rgba(0,0,0,.07)` faded toward the edges (a radial
  mask). No grain, no vignette: clean.
- **Cutouts** = Commons photos with the background removed (import the URL into Higgsfield
  `media_import_url` → `remove_background`; more reliable than upload +
  PUT). A two-layer `drop-shadow` (a far soft one + a near thin one).
- **Supporting props** (chopsticks, a globe, a noodle block) may be generated photoreal
  "studio product photo, isolated on pure white" then have the background removed.
- **Mixed typography** per beat: script (Caveat) for connectors ("see
  how", "then…"), sans 900 for the subject, italic 900 for numbers/claims,
  a mono-ish uppercase wide-spaced kicker, small gray body copy.
  Entry: script `scale .7→1 back.out`, bold from the left with horizontal blur,
  body per line.
- **Dashed circles** around the main object: a fixed `stroke-dasharray`,
  drawn with `clip-path: inset()` from the left (not dashoffset).
- **An object passing the lens** (`pass`): a big cutout flies diagonally with constant
  horizontal blur, 1.2–1.3 s, then disappears; used 1–2× per scene.
- A world map in SVG opacity ~.16 + a red dot + a dashed route line.
- Trap: tall cutouts (portrait photos) easily collide with body copy; compute the
  height from the photo ratio; put the body copy ABOVE the map/object if needed.
- **Evidence elements** (a historical-figure explainer ±50 s, 9:16, VO): photo cards
  (`.cut.card`: an archive photo in a 16 px white frame, light grayscale),
  typed documents (`.doc`: an Inter wide-spaced title + Plex Mono + a red/green
  `.stamp` slammed with `slam`), date blocks (`.stampblk`
  black/yellow revealed with `block`), handwritten notes (`.pnote` Caveat on
  cream paper), a repetition grid (`.grid` + `multiply`), an SVG clock with
  hands tweened by `rotation` + `svgOrigin`. See the section "One scene =
  3–5 elements".
- 9:16: W=1080, H=1920, wrap `#world` in `.safe` (scale .78);
  the 1080×1920 scene areas are laid out in the world (1600 px apart horizontally, 2400–3000
  px apart vertically so leftover cutouts from the previous scene are not visible), and the grid
  paper is made 14000×12500 px so all areas are covered.


## Fourth style: "vintage sketchbook" (sepia engraving on old paper)

Used for a history explainer (a steam engine, 64 s, 9:16, no sound).

- All pictures are generated in one batch with the same prompt prefix:
  "Vintage 19th-century copperplate engraving illustration, fine sepia ink
  cross-hatching, etching style … isolated on a plain white background, no
  text, no border". Portraits of historical figures: "engraved portrait … bust inside an
  oval". Name the era/profession, not the name, then put a name label on screen
  and the credit "engraving-style illustration".
- The background is removed (remove background) then the cutouts are placed with
  `mix-blend-mode:multiply` over a paper texture (also generated, 9:16)
  so the ink "soaks" into the paper; shadows only for big objects.
- Typography: a heavy display serif (Playfair Display 900) + Garamond italic
  for connecting sentences + wide-spaced small caps (Cinzel) for year/name labels;
  rust-colored handwritten annotations; a transparent gold highlighter.
- A big year as an outline "ghost" at the top, a "Place · Year" label
  beneath it: this is a timeline with no timeline line.
- The generator's rate limit (max 4 simultaneous jobs): send background removals
  in stages of 3–4 at once.


## Fifth style: "continuous action" — one subject that never stops

A remedy for an explainer that "feels like PPT slides" even though the camera is
choreographed. An example of the pattern: a high-speed sports explainer (flat
illustration, 16:9): all facts are delivered WITHOUT stopping the action. It can be 100 %
SVG vector drawn procedurally in JS (no generated images); that is exactly
what gives the After Effects motion-graphic feel.

Principles (order matters):

1. **One hero, from second 0 to the end.** The main subject (an athlete, a train,
   a motorcycle, a courier) never leaves the frame. What changes is the WORLD around
   it, not the subject. If there are 10 scenes, the hero is present in all 10.
2. **Always moving.** The background flows (parallax 2–3 layers, looping), there are
   speed lines, sparks/dust/smoke particles, the subject itself sways
   gently. Not a single second is completely still, even while a big number
   is being read.
3. **Numbers are stage props, not overlays.** A big number stands
   inside the world (behind the subject, with parallax depth), then the subject
   CROSSES IN FRONT OF IT and sweeps the number out. A changing number
   (35 → 43) spins like an odometer in place, not a fade in/out.
4. **The viewpoint changes, the subject stays in the center.** Side → front
   (head-on) → tilted following a bend (the whole world rotated 8–15°) →
   top (top-down). A viewpoint change = a scene change; no cut needed.
5. **A palette change = a tempo change.** When the story rises (speed,
   danger), the background changes color within 0.3 s + motion blur; the subject stays.
   Return to the original palette when the tempo drops.
6. **Comparisons stay inside the same world** (the comparison number
   stands in the background, the comparison object passes on another track), not a
   screen split into panels: splitting the screen feels "template" and stops
   the world.
7. **Text has only two levels: a big number + a world label.** No subtitles
   (see "Defaults often mistaken"); no kicker/body/badge.

Technical recipe (HTML + GSAP):

- The hero = several PNG layers (body, head/helmet, vehicle, shadow)
  in one `#hero` so each part can have its own sway
  (`yoyo` ±6–10 px with different periods) + `#hero` nudged ±25 px.
- The background = 2–3 wide strips (`width:300%`) with a looping `x`
  (`repeat:-1`, `ease:'none'`); the back layer's speed is ½ of the front's.
  Change the "place" by swapping the strip contents while out of frame.
- World numbers: an element in the `.deep` layer (scale .9, moving at ¾ of the front
  background's speed) so the subject in front covers it as it crosses.
  Odometer: two stacked `<span>`s in an `overflow:hidden`, tween `y`.
- Changing the viewpoint: prepare 2–3 hero image sets (side/front/top) generated
  in one batch with the same style; when switching, whip for 0.25 s
  (directional motion blur + a 60 px shift) and the next set is already moving.
- A bend: `rotate` the whole `#world` 8–15° for 1.5 s, the subject tilts
  slightly more (lead 3–5°).
- Palette: all colors through CSS variables; tween `--bg`, `--ink` with gsap
  (registerPlugin not needed; tween an object then `style.setProperty`).
- World objects are given `t0` (enter) and `t1` (discard) so a mountain/portal
  that has already been "passed through" does not stay drawn in front of the subject.
- Hiding a view with `visibility:hidden` does NOT hide an
  SVG child that has its own `visibility="visible"` attribute: the child's attribute
  beats the parent, and the object "bleeds through" to another view (a map marker shows up
  over the side-view train, and looks blurry because the old view still has a filter).
  To show a child, REMOVE its attribute (`removeAttribute('visibility')`),
  do not set 'visible'.
- A building/platform that "floats": only a canopy + thin poles with no wall
  behind the subject and a floor in front of the wheels. Give it a windowed wall in the back
  layer and a platform floor in the front layer covering the bogie.
- An SVG group scaled/rotated from its local (0,0) point (a train that
  approaches, a tilting subject): write the `transform` attribute directly
  (`translate(x y) scale(s)`), not `gsap.set`: GSAP's `transformOrigin`
  is measured from the element's bounding box and `svgOrigin` from global coordinates,
  so the object jumps or disappears when small.
- Text size still follows the rule "Readability on phones".

**The viewpoint MUST change.** "A subject from the side + text" from start
to end feels static and monotonous even though the background flows and the camera
moves. The rule: no three scenes in a row with the same
angle, and each new fact should ideally get its own "instrument".
A catalog of angles that has proven itself (all vector, all from the same rig):

| Fact | Angle / instrument |
|---|---|
| opening & closing | side (a visual anchor; only here may the subject "just pass by") |
| speed | a driver's cab: a speedometer needle sweeping + a digital number following, rails flowing on the windshield |
| route / distance / stops | a map simulation: the route drawn, a moving marker, popping points, the camera zooming from the start → the whole route |
| terrain / tunnels / slopes | an elevation profile (a contour chart), the route cutting through hills, tunnels as hollow segments, the longest highlighted then zoomed |
| time comparison | a race on the map: three markers set off together on their own tracks, one travel hour running, the winner arrives while the others are only ¼ of the way, not a panel |
| count / capacity | interior: a perspective cabin aisle, a row of seats lighting in sequence, windows with scenery flowing |
| closeness / scale | front view: the subject approaches from the vanishing point until it fills the frame |

A pleasant order: side → cab → map → profile → map race → front →
interior → side. Each view = one `<div class="view">` holding its own
SVG, swapped with a whip (blur + 0.3 s shift); each view's render remains
a pure function of time & the same world distance, so VO sync
is not disturbed when views are swapped.

The cheapest monotony breaker if you only have time for one: a **route map
simulation**. A stylized vector map (coastline, rivers, reservoirs, mountain icons, thin
toll roads, city blobs, compass + scale), the route drawn with
`stroke-dasharray = length` and a `dashoffset` following progress; the subject
marker moves through `getPointAtLength` and is rotated to follow the tangent;
stations/points "pop" (scale 0→1 with a slight overshoot) when progress
passes their fraction of the length; the map camera starts zoomed 2–2.5× at the start point,
follows the marker, then loosens to the whole route (`translate(center)
scale(z) translate(-cx -cy)` computed from progress). The total numbers (distance,
time) appear after the zoom out. Without this, "subject + text" from start
to end still feels static even though the background flows.

The side camera must also "breathe": a series of `[t, zoom, cx, cy]`
keyframes (pushing in 1.06–1.12× at key moments: a big number, a tunnel
portal, an arrival) + a slow ±0.6 % oscillation, applied
to a single `<g>` wrapping the SVG contents, not to the HTML text stuck to
the camera.

A trap: if the hero swaps pictures every scene (a new pose, new colors),
the "one subject" effect is lost; keep the silhouette, colors, and position in the frame. And
do not stop the background to read text; slow it to 40 % only.
