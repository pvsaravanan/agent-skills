# agent-skills

Personal collection of agent skills.

| Skill | Description |
|---|---|
| [`agent-reach`](skills/agent-reach) | Read-only access to content across platforms (GitHub, YouTube, Reddit, Twitter/X, LinkedIn jobs and more) via the Agent Reach CLI. English translation. |
| [`brag`](skills/brag) | Turn a project website into a short, shareable launch video using HyperFrames. |
| [`brag-slim`](skills/brag-slim) | Lightweight single-file version of `brag`: turns a project directory or URL into a launch video with no bundled assets. |
| [`caveman`](skills/caveman) | Terse reply style: answer first, no filler, code and errors kept exact. |
| [`caveman-commit`](skills/caveman-commit) | Writes terse Conventional Commit messages. |
| [`caveman-review`](skills/caveman-review) | One-line-per-finding code review with severity tags. |
| [`cavecrew`](skills/cavecrew) | Guide for delegating to the compact `cavecrew-*` subagents in [`agents/`](agents). Claude Code only. |
| [`surgical-patch`](skills/surgical-patch) | Fix bugs at the narrowest responsible layer, with regression proof. |
| [`verify-and-stop`](skills/verify-and-stop) | Prove acceptance conditions with minimal checks, then stop. |
| [`lean-build`](skills/lean-build) | Build the simplest complete solution; write less code. |
| [`investigate-first`](skills/investigate-first) | Investigate before changing code. |
| [`safe-refactor`](skills/safe-refactor) | Refactor with lower risk. |
| [`migration`](skills/migration) | Handle migrations safely. |
| [`security-audit`](skills/security-audit) | Security guidance and source-first vulnerability review for codebases, APIs, services, CLIs and libraries. |

## Attribution

- `brag` and `brag-slim` are from [latent-spaces/brag](https://github.com/latent-spaces/brag) by Shunit Haviv Hakimi, MIT licensed (see `skills/brag/LICENSE`). Bundled music in `skills/brag/assets/music` is by Sascha Ende ([ende.app](https://ende.app/en)), CC BY 4.0, and is not covered by the MIT license.
- `agent-reach` is an English translation of the skill shipped with [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) (v1.6.1) by Neo Reid, MIT licensed (see `skills/agent-reach/LICENSE`). It requires the `agent-reach` CLI to be installed separately.
- The `caveman*` skills, the work-pattern skills (`surgical-patch`, `verify-and-stop`, `lean-build`, `investigate-first`, `safe-refactor`, `migration`), `cavecrew` and the three `agents/cavecrew-*.md` subagents are from [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) (Apache-2.0, see `third-party/caveman/`). In `caveman`, two references to skills not included here were removed. The "Caveman" name and logo are trademarks of Julius Brussee.

## Agents

`agents/` holds Claude Code subagents. Copy them to `~/.claude/agents/` (or a project's `.claude/agents/`) to use them with the `cavecrew` skill.
