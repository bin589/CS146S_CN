# Claude-Code与Slack

> 来源：<https://code.claude.com/docs/en/slack>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。下文为公开页可读内容的中文整理／翻译。
# Claude Code 与 Slack

官方文档：在 Slack 中调用／协作 Claude Code 的集成说明。

## 英文正文摘录

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
Slack works

*[Snapshot truncated for archival size; images omitted.]*
