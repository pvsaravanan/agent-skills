# caveman

A bundle of skills and subagents adapted from [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) (Apache-2.0). It keeps only the parts that work as plain instructions: no hooks, CLI, proxy or cloud account.

## Skills (`skills/`)

| Skill | What it does |
|---|---|
| `caveman` | Terse reply style: answer first, no filler, code and errors kept exact. Stays on for the conversation until switched off. |
| `caveman-commit` | Writes terse Conventional Commit messages. Never runs git. |
| `caveman-review` | One-line-per-finding code review with line numbers and severity tags. |
| `cavecrew` | Guide for delegating to the `cavecrew-*` subagents below. |
| `surgical-patch` | Fix bugs at the narrowest responsible layer, with regression proof. |
| `verify-and-stop` | Prove acceptance conditions with minimal checks, then stop. |
| `lean-build` | Build the simplest complete solution; write less code. |
| `investigate-first` | Investigate before changing code. |
| `safe-refactor` | Refactor with lower risk. |
| `migration` | Handle migrations safely. |

## Agents (`agents/`, Claude Code only)

- `cavecrew-investigator`: read-only code locator that returns a compact `path:line` table.
- `cavecrew-builder`: small edits in 1-2 files, returns a short receipt.
- `cavecrew-reviewer`: one finding per line with a severity tag.

These files do not declare a `tools:` list, so their read-only and no-shell limits are instructions only. Add a `tools:` line to each if you want hard limits.

## Use

- Claude Code plugin: install this folder as a plugin once the repo's marketplace file is in place.
- Manual: copy `skills/*` into `~/.claude/skills/` and `agents/*.md` into `~/.claude/agents/`.

Without hooks, `caveman` does not turn on automatically at session start. Invoke it with `/caveman` each session.

## Changes from upstream

Two sentences in `skills/caveman/SKILL.md` that referred to skills not included here (`ultracave`, `megacave`, `caveman-compress`) were removed. Only English text is included. The "Caveman" name and logo are trademarks of Julius Brussee. See `LICENSE` and `NOTICE`.
