# Capability scope

Read this when the user asks what can be fetched or how complete a result is. The table below lists declared capabilities, not guaranteed results: it does not mean every network, account and piece of content has been tested.

## Three layers

- **Public, worth trying**: the agent's existing web tools, native tools or public endpoints may already satisfy the task; no browser install or login is required. Answer based on the evidence actually obtained.
- **Reach adds**: the actions declared by the current release; see `agent-reach channels`. When setup is needed, first reuse a session already saved in the dedicated browser, and ask the user to log in personally only when the chosen path actually requires it.
- **Verified on this machine**: lists only the specific actions that most recently passed acceptance on this machine. A successful install, a saved session and network reachability are not the same as business-level acceptance.

## Channels in this version

| Channel | Public path worth trying | What Reach adds, and its limits |
|---|---|---|
| GitHub | Public repositories, READMEs, issues/PRs | Repository search; reading repositories, issues and PRs, plus the comments returned; private access is judged separately |
| YouTube | Search, title, description; native tools may get some comments and subtitle text | search/read/subtitle/transcribe; there is currently no unified comments action; a track list is not the subtitle text; when there are no subtitles, transcription depends on the relevant tool |
| Bilibili | Search, description; some public endpoints can return comments with parent/child IDs | search/read/hot/subtitle; there is currently no unified comments action; subtitles vary by video and access path |
| Reddit | Search, body text, some comments; some public JSON can include parent/child IDs | Browser search/read/subreddit; login depends on the chosen path; the full comment tree and all replies are not guaranteed; no posting of comments |
| X/Twitter | Public single posts that show up in search; some official public embeds return the full text | search/profile/tweets/thread; being able to read a single post does not mean the reply stream is readable; the full comment tree is not guaranteed |
| Xiaohongshu | Public lists or indexes may show note ID, author, title; empty fields must not be guessed | search/read/comments; text description, top-level comments and loaded replies; not all comments are guaranteed; does not claim to understand images/video |
| Instagram | Some index and shallow profile information; an HTML app shell does not count as a post | search finds users, profile gets a profile, posts gets a given user's post captions; no unified comments action; does not claim to understand images/video |
| Facebook | Some index or HTML snippets; snippets may be truncated | search/profile; no unified detail or comments action; do not treat a search snippet as the full text |
| LinkedIn | Search public jobs, read public job descriptions | jobs/read first tries public web pages; only when opencli is specified does it go directly in-site; not every job is guaranteed readable |
| BOSS Zhipin | The search index may have job snippets | search/read job lists and job descriptions; never guess numbers from encoded salaries; fallback capability for details depends on the channel declaration |
| V2EX | Topics, body text and public replies | hot/node/read/user; the returned range is whatever this response contains; hidden or missing replies are not guaranteed |
| Xueqiu | Some public quotes and index information | quote/search/hot_posts/hot_stocks; quotes and community paths are accepted separately |
| Web | The agent's built-in search/read | Reach web search/read is an anonymous fallback; a snippet, an app shell and a verification page cannot be treated as the full body text |
| Xiaoyuzhou | Episode page title and description | transcribe converts a whole episode to text; requires the user to provide a Groq key (`agent-reach configure groq-key`) |

For capabilities after login, say "can enable / try the browser actions above"; do not say "supports all comments after login". If the user skips login, deliver the public evidence already obtained.
