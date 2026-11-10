# Sessions and the dedicated browser

Read this when the user wants to log in, log out or switch accounts, or when a result returns `NEED_LOGIN`.

## The dedicated browser

- All browser channels share one dedicated browser profile, separate from the user's everyday Chrome; the program never closes or modifies the user's everyday browser.
- The engine is CloakBrowser by preference. If the download or install fails, it uses the Chrome already installed locally and remembers this fallback instead of re-downloading each time. Once the network is fixed you can retry with `agent-reach browser setup --retry-cloak`.
- `agent-reach add <channel>` automatically prepares Node, OpenCLI, the engine and the extension. Tools are installed at the versions tested for this release. On Windows with the Chrome fallback, the user may need to click "Add to Chrome" once.
- Headless by default, no window. Only `agent-reach login <channel>` shows a window; while that window is open, queries use it directly and do not close it, and while the user is logging in you wait until they say they are done before querying. Once the window is closed, later queries go back to headless.
- It closes automatically after 10 minutes idle and reopens on the next call; real page actions and Reach calls reset the timer. During login the session is saved periodically, so the user does not need to close the window.
- Parallel calls are allowed: at most 2 at once per platform and 4 in total across platforms, with extra calls queued for up to 2 minutes; only if no slot opens does it return `BUSY`. Leave at least 10 seconds between two searches on the same platform. Opening a login window, logging out and reinstalling the browser wait for running queries to finish first.
- `agent-reach browser status` shows state, `browser setup` prepares the engine and extension, `browser stop` closes the browser the program manages.

## Reusing existing logins automatically

1. The first time a site is used, if the user's Chrome has the OpenCLI extension connected, the program copies that site's login (only that site's cookies) to the dedicated browser once. It does not copy the whole browser directory, other sites, or the password vault, and it does not change the source browser.
2. After a successful copy, the saved session is reused indefinitely and is not re-copied on a timer. The presence of a cookie does not mean the login is valid; go by the result of the real action.
3. If the user's Chrome does not have the extension connected, you cannot promise automatic reuse, and you must not conclude the user is not logged in; in that case use the session Reach has saved.
4. If several browsers on the machine are logged in to the site: `agent-reach browser profiles` lists the sources and `agent-reach browser use <ID>` picks one; it does not switch at random.
5. `agent-reach login <channel> --import-existing` deliberately re-copies that site's login once, without opening a window. If no login to copy is found, or the OpenCLI Bridge is not running, it returns `NEED_SETUP` and the saved session is unchanged.
6. Once the user has logged in personally in the dedicated window, or has run `logout` / `remove`, logins are no longer copied automatically, so that a logged-out session does not come back to life.

## When a personal login is needed

- Ask the user to log in only when `NEED_LOGIN` was actually returned and the remaining task really needs that path. A login button next to the body text does not count as requiring login.
- `agent-reach login <channel>` opens the dedicated browser at that site's login page, and the user completes the login personally. You do not log in for them, ask for passwords, or output cookies.
- If the returned result has steps in `next`, follow them. For some native-tool channels (such as Xueqiu), run `agent-reach login <channel> --sync` again after logging in.
- After the user is done, re-run the original action to verify.

## Platform differences

- BOSS Zhipin in-site search goes through OpenCLI and shares the dedicated browser. If a job detail wrongly demands login because of an upstream false report, do not make the user log in repeatedly.
- Bilibili hands the existing login to Bilibili's official command-line tool only when reading subtitles; ordinary search does not prepare a browser.
- Xueqiu community actions require login; the session expires within a few hours, after which you repeat the login steps.

## Logging out and deleting

- `agent-reach logout <channel>`: clears that site's login and the channel's own state in the dedicated browser; other sites are kept.
- `agent-reach remove <channel>`: removes the channel and also clears that site's login and storage; other sites are kept. If cleanup fails, the channel record is kept and an error is returned so the user can retry.
- After either, that site's login is no longer copied automatically.
