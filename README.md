# agent-skills

Personal collection of agent skills.

| Skill | Description |
|---|---|
| [`agent-reach`](skills/agent-reach) | Read-only access to content across platforms (GitHub, YouTube, Reddit, Twitter/X, LinkedIn jobs and more) via the Agent Reach CLI. English translation. |
| [`brag`](skills/brag) | Turn a project website into a short, shareable launch video using HyperFrames. |
| [`brag-slim`](skills/brag-slim) | Lightweight single-file version of `brag`: turns a project directory or URL into a launch video with no bundled assets. |
| [`caveman`](plugins/caveman) (plugin bundle) | Terse output style, commit and review helpers, six work-pattern skills (`surgical-patch`, `verify-and-stop`, `lean-build`, `investigate-first`, `safe-refactor`, `migration`), and the `cavecrew` subagents. Adapted from JuliusBrussee/caveman. |
| [`vox-explainer`](skills/vox-explainer) | One-topic-to-finished-film pipeline for Vox-style explainer videos (script, voiceover, keyframes, animation, music, ffmpeg assembly) via the Atlas Cloud API. |
| [`bang-motion`](skills/bang-motion) | HTML + CSS + GSAP (+ Three.js) motion graphics delivered as a single `index.html`: openers, promos, and explainers, with a style brief first, deterministic timelines, a camera rig, and optional frame export. English translation. |
| [`founder-board`](skills/founder-board), [`founder-marketing`](skills/founder-marketing), [`founder-cfo`](skills/founder-cfo), [`founder-consumer`](skills/founder-consumer), [`founder-launch`](skills/founder-launch), [`founder-pricing`](skills/founder-pricing), [`founder-offer`](skills/founder-offer), [`founder-competitors`](skills/founder-competitors), [`founder-brand`](skills/founder-brand), [`founder-ops`](skills/founder-ops), [`founder-plan`](skills/founder-plan) | The founder pack: eleven skills that test a business idea before launch (a three-lens board, marketing director, CFO unit economics, a 100-agent consumer panel, pricing, offer, competitors, brand, ops, launch, and plan compilation). Some include small Python helpers (Python 3.8+, no dependencies). The skills reference each other by sibling folder, so keep them together. |
| [`security-audit`](skills/security-audit) | Security guidance and source-first vulnerability review for codebases, APIs, services, CLIs and libraries. |

## Attribution

- `brag` and `brag-slim` are from [latent-spaces/brag](https://github.com/latent-spaces/brag) by Shunit Haviv Hakimi, MIT licensed (see `skills/brag/LICENSE`). Bundled music in `skills/brag/assets/music` is by Sascha Ende ([ende.app](https://ende.app/en)), CC BY 4.0, and is not covered by the MIT license.
- `agent-reach` is an English translation of the skill shipped with [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) (v1.6.1) by Neo Reid, MIT licensed (see `skills/agent-reach/LICENSE`). It requires the `agent-reach` CLI to be installed separately.
- `plugins/caveman` is adapted from [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) (Apache-2.0, see `plugins/caveman/LICENSE` and `NOTICE`). The "Caveman" name and logo are trademarks of Julius Brussee.
- `vox-explainer` is from [CK42BB/vox-explainer-skill](https://github.com/CK42BB/vox-explainer-skill), MIT licensed (see `skills/vox-explainer/LICENSE`). It needs an `ATLASCLOUD_API_KEY` and `ffmpeg`.
- `bang-motion` is from [bangtutorial/bang-motion](https://github.com/bangtutorial/bang-motion) by Bang Tutorial, MIT licensed (see `skills/bang-motion/LICENSE`); this copy is an English translation (docs/gallery, README and plugin metadata omitted). It needs a browser with CDN access (GSAP, Three.js, fonts); Node + puppeteer and ffmpeg are optional for snapshots and MP4 export.
- The `founder-*` skills are from [Jakeschincariol/founder-skill](https://github.com/Jakeschincariol/founder-skill) by Jake Schincariol, MIT licensed (license copy in `skills/founder-board/LICENSE`).
