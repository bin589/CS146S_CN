# Claude-Code网页版

> 来源：<https://code.claude.com/docs/en/claude-code-on-the-web>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。下文为公开页可读内容的中文整理／翻译。
# Claude Code 网页版

官方文档：在云端／浏览器中使用 Claude Code 的说明。

## 英文正文摘录

Cloud sessions are available on Pro, Max, Ultra, and Team plans, and for Enterprise users with premium seats or Chat + Claude Code seats. If custom roles govern your access, you also need a role with the cloud sessions permission to start sessions on Anthropic’s infrastructure from the browser, apps, or terminal. Ask an Owner to add it to one of your roles at Organization settings > Roles.
- Browser: claude.ai/code, also called Claude Code on the web
- Mobile: the Code tab in the Claude app
- Desktop app: select an environment under Cloud in the environment selector when you start a session
- Terminal: claude --cloud
- Cloud scheduled tasks: scheduled and triggered runs each run as a cloud session
Once you’re set up, use this page to move work between your terminal and the cloud, manage and share sessions, turn on auto-fix for pull requests, and troubleshoot.
These cases are covered on other pages:
- Starting your first cloud session: Get started with cloud sessions connects GitHub and walks through a task in the browser
- Many cloud sessions for one body of work: a project has Claude start and keep track of them for you
- Steering a local session from another device: sessions in your terminal, IDE, or the Desktop app with Local selected run on your machine, and Remote Control lets you reach them from your phone or browser
Cloud environments
Every cloud session runs in a cloud environment, the saved configuration that controls network access, environment variables, and setup scripts.
- Your first environment: if you don’t have one yet, onboarding sets up a Default environment with Trusted network access, either by creating it for you or by asking you to create it. See The Default environment for which of those happens on your plan
- Which environment a session uses: see The Default environment for how sessions choose an environment when you have more than one
- Change what sessions can reach or run at startup: see Configure cloud environments
- What’s installed without any configuration: see Installed tools
GitHub authentication options
Cloud sessions need access to your GitHub repositories to clone code and push branches. You can grant access in two ways:
These features depend on the Claude GitHub App being installed on the repository:
- Auto-fix: installing the Claude GitHub App on a repository also enables Auto-fix for pull requests in it
- Projects: threads in a project need the Claude GitHub App installed on each repository they clone, whichever method you connected with. See Set up GitHub access
In Anthropic-hosted environments, your GitHub credentials stay encrypted on Anthropic’s servers and never enter a session’s VM. GitHub operations from the VM go through the GitHub proxy, which attaches the credential on the server side. See Connect from your terminal for the
/web-setup walkthrough, including what /web-setup stores and how to remove it.
Organizations with Zero Data Retention enabled, or with the HIPAA configuration applied, can’t use /web-setup or other cloud session features. Organizations that use customer-managed encryption keys (CMEK) can’t start cloud sessions either.
Quick setup for Team and Enterprise
Quick setup is an organization setting that removes steps from members’ GitHub and environment setup. On Team and Enterprise plans it’s off by default. Here’s what changes for members when it’s on:
- /web-setup: members can connect GitHub with /web-setup. While the setting is off, the command is hidden
- GitHub App prompt: browser onboarding skips the Claude GitHub App install prompt
- First environment: browser onboarding creates the Default environment for members instead of showing the environment form
An Owner turns it on with the Quick setup toggle at Organization settings > Claude Code.
Move tasks between terminal and cloud
These workflows require the Claude Code CLI signed in to the same claude.ai account. You can start new cloud sessions from your terminal, or pull cloud sessions into your terminal to continue locally. Cloud sessions persist even if you close your laptop, and you can monitor them from anywhere including the Claude mobile app.
From the CLI, session handoff is one-way: you can pull cloud sessions into your terminal with --teleport, but you can’t push an existing terminal session to the cloud. The --cloud flag with a task description creates a new cloud session for your current repository; with -p and a session ID or claude.ai/code URL it instead queues a message into that existing session. The Desktop app can send a local session in its Code tab to the cloud from its Open in menu.
Start a cloud session from your terminal
Start a cloud session from the command line with the--cloud flag:
Branch <name> is not on GitHub, see Branch is not on GitHub.
--cloud works with a single repository at a time. The task runs in the cloud while you continue working locally. The older --remote spelling still works as a deprecated alias for --cloud.
While the cloud container starts, the 

*[Snapshot truncated for archival size; images omitted.]*
