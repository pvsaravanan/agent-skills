# Maintenance

Read this when an update fails, the browser will not start, a channel reports an error, or the user wants to uninstall.

- Update: `agent-reach update` upgrades Agent Reach, the tools for added channels, and the skill; `agent-reach update --check` only checks whether a new version exists. Run it only after the user agrees.
- Status: `agent-reach doctor --text` reads local state without using the network; `agent-reach check <channel> --text` runs one live test over the network (`--search` tests only search/jobs). A successful install is not the same as passing a live test.
- Browser: `agent-reach browser status` shows state, `browser setup` prepares the engine and extension, `browser stop` closes it; after a CloakBrowser download failure, once the network is fixed run `browser setup --retry-cloak`.
- Tell failure stages apart: dependency download, browser connection, login, page load and platform rate limiting are each separate. Do not describe a network timeout as an expired login.
- Upstream tool errors: note the error and version, and with the user's consent run `agent-reach update` once; do not modify the upstream tool's installed files and do not retry in a loop.
- On `PLATFORM_BLOCKED`, `RATE_LIMITED`, `NEED_LOGIN` or `BUSY`, stop this attempt and continue only after the user has dealt with it; do not repeatedly open windows.
- Keys and proxy: `agent-reach configure groq-key | openai-key | proxy | github-token`; the user provides the values personally.
- Port conflict (`Port <n> belongs to an unmanaged browser`): another program is using the dedicated browser's port (default 9222). Do not close the user's program; with their consent run `agent-reach configure browser-port <free port>`.
- Uninstall: first `agent-reach uninstall --dry-run` to show the user the scope, then `agent-reach uninstall` once they confirm. It removes only what Reach itself installed; the user's other files and browser are kept.
