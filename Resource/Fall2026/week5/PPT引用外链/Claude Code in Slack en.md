# Claude Code in Slack

> 来源：<https://code.claude.com/docs/en/slack>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。
Claude Code in Slack brings the power of Claude Code directly into your Slack workspace. When you mention
@Claude with a coding task, Claude automatically detects the intent and creates a Claude Code cloud session, allowing you to delegate development work without leaving your team conversations.
This integration is built on the existing Claude for Slack app but adds intelligent routing to Claude Code cloud sessions for coding-related requests. Each session runs under your own Claude account, using your connected repositories and your plan limits.
Use cases
- Bug investigation and fixes: Ask Claude to investigate and fix bugs as soon as they’re reported in Slack channels.
- Quick code reviews and modifications: Have Claude implement small features or refactor code based on team feedback.
- Collaborative debugging: When team discussions provide crucial context (for example, error reproductions or user reports), Claude can use that information to inform its debugging approach.
- Parallel task execution: Kick off coding tasks in Slack while you continue other work, receiving notifications when complete.
Prerequisites
Before using Claude Code in Slack, ensure you have the following:
Setting up Claude Code in Slack
1
Install the Claude App in Slack
A workspace administrator must install the Claude app from the Slack App Marketplace. Visit the Slack App Marketplace and click “Add to Slack” to begin the installation process.
2
Connect your Claude account
After the app is installed, authenticate your individual Claude account:
- Open the Claude app in Slack by clicking on “Claude” in your Apps section
- Open the App Home tab
- Click “Connect” to link your Slack account with your Claude account
- Complete the authentication flow in your browser
3
Configure cloud sessions
Ensure cloud sessions are properly configured for your account:
- Visit claude.ai/code and sign in with the same account you connected to Slack
- Connect your GitHub account if not already connected
- Authenticate at least one repository that you want Claude to work with
4
Choose your routing mode
After connecting your accounts, configure how Claude handles your messages in Slack. Open the Claude App Home in Slack to find the Routing Mode setting.In Code + Chat mode, if Claude routes a message to Chat but you wanted a coding session, you can click “Retry as Code” to create a Claude Code session instead. Similarly, if it’s routed to Code but you wanted a Chat session, you can choose that option in that thread.
5
Add Claude to channels
Claude is not automatically added to any channels after installation. To use Claude in a channel, invite it by typing /invite @Claude in that channel. Claude can only respond to @mentions in channels where it has been added.
How it works
Automatic detection
In Code + Chat routing mode, when you mention @Claude in a Slack channel or thread, Claude automatically detects whether your message is a coding task. Coding tasks go to a Claude Code cloud session. Anything else gets a regular chat reply. In Code only mode, every @mention goes to Claude Code. You can also explicitly tell Claude to handle a request as a coding task, even if it doesn’t automatically detect it.
Claude Code in Slack only works in channels (public or private). It does not work in direct messages (DMs).
Context gathering
From threads: When you @mention Claude in a thread, it gathers context from all messages in that thread to understand the full conversation. From channels: When mentioned directly in a channel, Claude looks at recent channel messages for relevant context. This context helps Claude understand the problem, select the appropriate repository, and inform its approach to the task.
Session flow
- Initiation: You @mention Claude with a coding request
- Detection: Claude analyzes your message and detects coding intent
- Session creation: A new Claude Code session is created on claude.ai/code
- Progress updates: Claude posts status updates to your Slack thread as work progresses
- Completion: When finished, Claude @mentions you with a summary and action buttons
- Review: Click “View Session” to see the full transcript, or “Create PR” to open a pull request
User interface elements
Message actions
- View Session: Opens the full Claude Code session in your browser where you can see all work performed, continue the session, or make additional requests.
- Create PR: Creates a pull request directly from the session’s changes.
- Retry as Code: If Claude initially responds as a chat assistant but you wanted a coding session, click this button to retry the request as a Claude Code task.
- Change Repo: Lets you select a different repository if Claude chose incorrectly.
Repository selection
Claude automatically selects a repository based on context from your Slack conversation. If multiple repositories could apply, Claude may display a dropdown allowing you to choose the correct one.
Access and permissions
User-level access
Workspace-level access
Slack workspace administrators control whether the Claude app is available in their workspace:
Channel-based access control
Installing the app doesn’t add Claude to any channels. Claude responds to @mentions only in channels where it has been added; invite it with/invite @Claude. It works in both public and private channels. Admins can control who uses Claude Code by managing which channels Claude is invited to and who has access to those channels. This adds a layer of access control beyond workspace-level permissions.
What’s accessible where
In Slack: You’ll see status updates, completion summaries, and action buttons. The full transcript is preserved and always accessible. At claude.ai/code: The complete Claude Code session with full conversation history, all code changes, and file operations. Sessions stay in your Claude Code history at claude.ai/code, where you can continue past sessions, reference them, or create pull requests. For Enterprise and Team accounts, sessions created from Claude in Slack are automatically visible to the organization. See cloud session sharing for more details.
Best practices
Writing effective requests
- Be specific: Include file names, function names, or error messages when relevant.
- Provide context: Mention the repository or project if it’s not clear from the conversation.
- Define success: Explain what “done” looks like. Should Claude write tests? Update documentation? Create a PR?
- Use threads: Reply in threads when discussing bugs or features so Claude can gather the full context.
When to use Slack vs. web
Use Slack when: Context already exists in a Slack discussion, you want to start a task asynchronously, or you’re collaborating with teammates who need visibility. Use the web directly when: You need to upload files, want real-time interaction during development, or are working on longer, more complex tasks.
Troubleshooting
“This workspace isn’t set up for Claude Tag yet”
@Claude replies in the thread with this notice instead of an answer when both of these are true:
- No organization has connected your Slack workspace to Claude Tag.
- The Claude account you linked in Slack isn’t on a Pro, Max, or Ultra plan.
Claude Tag is available on Team and Enterprise plans. To connect the workspace, start with the
@Claude connect command the notice names, then follow Set up Claude Tag.
“The legacy Claude in Slack bot is retired”
The notice opens withThe legacy Claude in Slack bot is retired effective October 5, 2026 and no longer responds in channels. Your Slack workspace is connected to a Claude organization. The earlier version is still selected for the channel, the workspace, or the organization default in that organization’s Claude Tag settings. The notice doesn’t depend on your own plan, so Pro, Max, and Ultra accounts get it too.
If you’re an Owner of that organization, open Claude admin settings and turn on Claude Tag for the channel. To fix every channel that inherits the setting, change it on the workspace or the organization default instead. For the full move, see Migrate from the earlier Claude in Slack. If you’re not an Owner, send this entry to one.
”Claude Code is not enabled for your account”
This error means your Claude account has no cloud environment yet. Sign in at claude.ai/code once with the same account you connected to Slack and finish web onboarding, which creates your default cloud environment or asks you to create it. The error clears on your next mention. Each user must do this individually.
Sessions not starting
- Verify your Claude account is connected in the Claude App Home
- Check that cloud sessions are enabled for your account
- Ensure you have at least one GitHub repository connected to Claude Code
Sessions from a Claude Tag channel fail to start
This entry applies to workspaces using Claude Tag. If you created the channel’s cloud environment at claude.ai/code, it belongs to your personal account, and Claude can’t start channel sessions in a personal environment. Claude Code fails the session immediately, and retrying doesn’t help. If you’re an Owner and the environment is your own, share it with the organization from the environment selector. Otherwise, an Owner recreates it as an organization-shared environment from the Cloud environments page in admin settings. You can apply it in two ways:
- Set it as the organization default at claude.ai/admin-settings/claude-code.
- Set it on the channel in the Claude Tag admin settings.
If you’re not an Owner, send this entry to one.
Repository not showing
- Connect the repository at claude.ai/code
- Verify your GitHub permissions for that repository
- Try disconnecting and reconnecting your GitHub account
Wrong repository selected
- Click the “Change Repo” button to select a different repository
- Include the repository name in your request for more accurate selection
Authentication errors
- Disconnect and reconnect your Claude account in the App Home
- Ensure you’re signed into the correct Claude account in your b

*[Snapshot truncated for archival size; images omitted.]*
