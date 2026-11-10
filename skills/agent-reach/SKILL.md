---
name: agent-reach
description: >
  Read-only access to content across platforms: search, read posts, view comments,
  fetch subtitles, check stock quotes and job listings.
  Use when the user mentions or pastes a link from: Xiaohongshu (RedNote), Bilibili,
  Twitter/X, Reddit, YouTube (subtitles, transcription), GitHub, V2EX, Xueqiu / stock
  quotes, LinkedIn / BOSS Zhipin jobs, Instagram, Facebook, Xiaoyuzhou podcasts; or says
  "search for / look at / read this link" and the built-in web search/read tools are
  unavailable, failed, or did not return the body text; or wants to install, add or remove
  a platform, log in or out, check status, update, or uninstall Agent Reach.
  Does not: post, comment, like, send DMs, or perform any write action; does not log in
  for the user or ask for passwords.
  For public content, prefer the agent's built-in tools; Reach fills the gaps.
metadata:
  homepage: https://github.com/Panniantong/Agent-Reach
  version: "1.6.1"
---

# Agent Reach

One command to read every platform: `agent-reach`. Read-only. Output is a single line of JSON by default.

Before acting, say one sentence: "Using the agent-reach skill (X channel)". Once this skill is invoked, the rules below apply for the rest of the session.

## Choosing a path

- For public content, use your own search/read tools first (you can add `site:domain`). Check separately whether you actually got the body text, the comments, and the subtitles. If that is enough, answer directly: do not install channels or log in.
- Use Reach when your own tools are unavailable, the result is missing the part the user wants, or the user wants an in-site action that a channel declares. If unsure which actions and parameters exist, run `agent-reach channels` first.
- If a channel is already added (a default channel or one you ran `add` for), search/read goes straight through that site's tool. For channels not added yet, search/read first tries login-free public web pages, and the result marks the source with `backend: public-web`. `--backend public-web` queries only public web pages; `--backend <backend>` selects the in-site tool.
- A platform name or link is only used to recognise the source. It never triggers an install or login on its own.
- A snippet, an app shell page, a comment count, or a list of subtitle tracks is not the body text, the comments, or the subtitles themselves; report them separately. If the user skips login, deliver the public results already obtained.

```bash
agent-reach channels                      # actions and parameters for every channel
agent-reach <channel> <action> [args]     # e.g. agent-reach xiaohongshu search "coffee" --limit 5
agent-reach read <url>                    # pick the channel automatically from the link
```

## Results and errors

- `ok: true` → content is in `items`; each has `title / url / author / published_at / text`, and the raw data is in `raw`.
- `ok: false` → look at `error.code` and follow `error.hint`:

| error.code | What to do |
|---|---|
| `NEED_SETUP` | A dependency or key is missing. Follow the hint: `agent-reach add <channel>`. If a key is needed, ask the user to provide it themselves, then `agent-reach configure <key>` |
| `NEED_LOGIN` | Keep any results you already have and tell the user a login is needed. `agent-reach login <channel>` opens a browser and the user logs in personally. Never log in for them and never ask for a password |
| `UPSTREAM_BROKEN` | The platform is temporarily broken; `message` is the verbatim error. Tell the user which platform is temporarily unavailable and roughly why, using the platform name and not the tool name. Only if the message shows the tool is outdated, and the user agrees, run `agent-reach update` once. Do not retry in a loop |
| `TIMEOUT` | Check the failing stage and channel status (`agent-reach doctor --text`). Do not retry repeatedly or repeatedly open windows |
| `RATE_LIMITED` | The platform is rate-limiting; Reach has paused the channel. Wait per `retry_after_seconds`; do not switch backends |
| `PLATFORM_BLOCKED` | The platform requires verification (CAPTCHA / risk control). Stop and ask the user to handle it on the official page. Do not switch accounts or backends |
| `BUSY` | The browser stayed full after queuing for 2 minutes, or the user has a login window open. Try again later, or after the user says they have finished logging in. Do not close the window or switch profiles |
| `NOT_FOUND` | The content does not exist; check the link or ID |
| `BAD_INPUT` | Wrong parameters; run `agent-reach channels` to see usage |

On `PLATFORM_BLOCKED`, `RATE_LIMITED`, `NEED_LOGIN` or `BUSY`, stop this attempt. Do not switch accounts, backends or browsers and keep requesting. A network failure, or a failure on one machine, must not be described as "the platform requires login".

## Login and the dedicated browser

All browser channels share one dedicated browser (CloakBrowser preferred; the local Chrome if it cannot be installed). It is headless by default (no window), closes after 10 minutes idle, and reopens automatically on the next call. Calls can run in parallel (including sub-agents querying at the same time): at most 2 at once per platform and 4 in total across platforms, with extra calls queued automatically; leave at least 10 seconds between two searches on the same platform.

The first time a site is used, if the user's Chrome has the OpenCLI extension connected, the program copies that site's login to the dedicated browser once and reuses it from then on. It copies only that site and does not touch the original browser. Only when the login has expired or there is nothing to copy should you ask the user to run `agent-reach login <channel>` themselves. For refreshing, choosing a source, logging out and other details, see [Sessions and the dedicated browser](references/sessions.md): read it when the user wants to log in, log out or switch accounts, or when you hit `NEED_LOGIN`.

## Platform notes

- Xiaohongshu `read` returns only the text description. Do not claim to have understood the images or video.
- When a BOSS Zhipin search result has `salary_encoded=true`, never guess salary numbers. Use `read` on the job link to get the readable salary in the details.
- For what each platform allows publicly and what Reach adds, see [Capability scope](references/capabilities.md): read it when the user asks "what can you fetch / is the result complete?" or when you need to judge how complete a result is.

## Channels

| channel | level | actions | login |
|---|---|---|---|
| github | default | search, read | - |
| twitter | experimental | search, profile, tweets, thread | `agent-reach login twitter` |
| youtube | default | read, search, subtitle, transcribe | - |
| reddit | optional | search, read, subreddit | browser path, as needed |
| facebook | experimental | search, profile | `agent-reach login facebook` |
| instagram | experimental | search, profile, posts | `agent-reach login instagram` |
| bilibili | default | search, read, hot, subtitle | `agent-reach login bilibili` |
| xiaohongshu | optional | search, read, comments | `agent-reach login xiaohongshu` |
| linkedin | optional | jobs, read | `agent-reach login linkedin` |
| boss | optional | search, read | `agent-reach login boss` |
| v2ex | default | hot, node, read, user | - |
| xueqiu | optional | quote, search, hot_posts, hot_stocks | `agent-reach login xueqiu` |
| xiaoyuzhou | optional | transcribe | - |
| web | default | search, read | - |

`default` channels are installed by default and can be removed; once removed, updates do not add them back. The `login` column is the authentication entry point, not a prerequisite for reading public content.

## When installation finishes

After `agent-reach setup`, show `result.installation_report.markdown` to the user exactly as output: do not add, remove or reorder anything, and do not add your own greeting or tables. The report is generated by the program.

## When the user wants to manage Agent Reach

| User says | You run |
|---|---|
| Add a platform | `agent-reach add <channel>`; dependencies install automatically. Tell the user only what they must do (log in or provide a key) |
| Remove a platform | `agent-reach remove <channel>` |
| Log in / login expired | `agent-reach login <channel>`; the user logs in personally in the window that opens |
| Log out | `agent-reach logout <channel>` |
| Check status / what works | `agent-reach doctor --text`; for a live test run `agent-reach check <channel> --text` |
| Upgrade / update | `agent-reach update` |
| Uninstall | First `agent-reach uninstall --dry-run` to show the user, then `agent-reach uninstall` once they confirm |
| Make another AI able to use it | `agent-reach skill link <that AI's skill directory>`; `agent-reach skill` shows where it currently lives |

For troubleshooting, browser maintenance and uninstall details, see [Maintenance](references/maintenance.md): read it when an update fails, the browser will not start, or the user wants to uninstall.

## When a new version is available

If `meta.update` appears in a result, a new version exists. Mention it once per conversation, in plain language in the user's language:

1. Tell the user a new version is available (`meta.update.latest`).
2. Pick 1 to 3 key points from `meta.update.notes` and say what changed.
3. Ask whether they want to update; run `agent-reach update` only after they agree.

## Red lines

- Read-only. Never post, comment, like or send DMs.
- Never log in for the user, and never ask for or output passwords, cookies or other credentials.
- Ordinary queries do not change dependencies or update automatically.
