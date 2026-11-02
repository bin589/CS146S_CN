# Claude Code on the Web

> 来源：<https://code.claude.com/docs/en/claude-code-on-the-web>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。
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
While the cloud container starts, the CLI shows a live checklist of setup steps, such as cloning the repository and running your setup script. It queues messages you type during provisioning and sends them once the session is ready.
--cloud creates cloud sessions. --remote-control is unrelated: it lets you monitor and steer a local CLI session from claude.ai or the Claude app. See Remote Control.
Tips for cloud tasks
Plan locally, execute in the cloud: for complex tasks, start Claude in plan mode to collaborate on the approach, then send work to the cloud:--cloud command creates its own cloud session that runs independently. You can start multiple tasks and they’ll all run simultaneously in separate sessions:
Send local repositories without GitHub
When you runclaude --cloud from a repository that has no git remote, or from a github.com repository that the Claude GitHub App isn’t installed on, Claude Code bundles your local repository and uploads it directly to the cloud session. This applies even if you connected GitHub with /web-setup.
For a full clone, the bundle includes your repository history across all branches, plus uncommitted changes to tracked files.
What happens to uncommitted changes in sensitive files depends on your platform:
- macOS, Linux, and WSL: Claude Code leaves uncommitted changes to files named like credentials or keys out of the upload. This includes .env files, Terraform *.tfvars files, and key files such as id_rsa and *.pem. It also leaves out uncommitted changes to files that a git filter such as Git LFS manages. A Left on this machine: notice names the files left out, and the session starts with the committed version of each, or without the file if none is committed.
- Native Windows: uncommitted changes to tracked files upload as they are, whatever the file’s name. Stash or revert an edit you don’t want in the cloud session before you start it.
To upload a bundle even when Claude Code would otherwise clone from the remote, set
CCR_FORCE_BUNDLE=1:
- The directory must be a git repository with at least one commit
- The bundled repository must be under 100 MB. Larger repositories fall back to bundling only the current branch, then to a single squashed snapshot of the working tree, and fail if the snapshot is still too large
- Untracked files are not included; run git add on files you want the cloud session to see
- On macOS, Linux, and WSL, Claude Code refuses the upload when it can’t follow a git setting that affects which attribute rules apply to your files, such as core.attributesFile set in an included config file. The refusal message names the setting and the fix
- Sessions created from a bundle can push back to a GitHub remote only when your GitHub connection has push access to that repository
On macOS, Linux, and WSL, the upload also needs git 2.31 or later and a checkout layout it supports, while on native Windows Claude Code uploads without either check. When a checkout doesn’t meet those requirements, Claude Code doesn’t start the session. It prints an error that contains
Not uploading this working tree:, names the cause, and says what to change. These are the common causes:
- Older git: the installed git is older than 2.31. Update git, then retry.
- A checkout layout the upload doesn’t support: you started inside a submodule, in a clone made with git clone --separate-git-dir, --shared, or --reference, in a checkout with core.worktree set, or in a repository that keeps its refs in the reftable format. Start from the main checkout of a clone made with a plain git clone instead.
- A linked worktree with a sparse checkout: git sparse-checkout writes settings to the worktree’s own config.worktree file, which the upload doesn’t accept, so a worktree that has those settings isn’t uploaded, and neither is one Claude Code created with worktree.sparsePaths. Start from the repository’s main checkout instead.
- Git configuration kept inside the working tree: your git configuration includes a file that sits inside the checkout, for example an include.path entry that points into the repository. Move that file outside the working tree or remove the include, then retry.
On macOS, Linux, and WSL, a partial clone made with
git clone --filter uploads as a snapshot of its working tree without history, as long as the clone holds every tracked file locally.
For claude --cloud, if the repository is on GitHub, you can avoid the upload and its requirements: push your branch, install the Claude GitHub App on the repository, and start the session again so that it clones from GitHub.
Send follow-ups from the CLI
Once a cloud session is running, wherever it executes, send it a follow-up message from theclaude CLI on any machine where you’re logged in with claude auth login. The CLI authenticates with your Anthropic account credentials and sends no local session state, so the command doesn’t need to run from the machine that started the session.
The command posts one message and exits:
echo "your message" | claude -p --cloud <session-id>

*[Snapshot truncated for archival size; images omitted.]*
