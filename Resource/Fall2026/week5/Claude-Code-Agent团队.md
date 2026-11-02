# Claude-Code-Agent团队

> 来源：<https://code.claude.com/docs/en/agent-teams>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。下文为公开页可读内容的中文整理／翻译。
# Claude Code：Agent Teams

官方文档：如何编排多会话／团队式 Claude Code 工作（并行 agent、协调方式等）。

## 英文正文摘录

Agent teams let you coordinate multiple Claude Code instances working together. One session acts as the team lead, coordinating work, assigning tasks, and synthesizing results. Teammates work independently, each in its own context window, and communicate directly with each other. You can also talk to any teammate directly without going through the lead. Before you set up a team, check whether a lighter option does the job. Subagents work within a single session, and with cross-session messaging Claude can pass findings between the sessions you run yourself.
When to use agent teams
Agent teams are most effective for tasks where parallel exploration adds real value. See use case examples for full scenarios. The strongest use cases are:
- Research and review: multiple teammates can investigate different aspects of a problem simultaneously, then share and challenge each other’s findings
- New modules or features: teammates can each own a separate piece without stepping on each other
- Debugging with competing hypotheses: teammates test different theories in parallel and converge on the answer faster
- Cross-layer coordination: changes that span frontend, backend, and tests, each owned by a different teammate
Agent teams add coordination overhead and use significantly more tokens than a single session. They work best when teammates can operate independently. For sequential tasks, same-file edits, or work with many dependencies, a single session or subagents are more effective.
Compare with subagents
Both agent teams and subagents let you parallelize work, but they operate differently. For separate sessions that pass messages to each other without a team, see cross-session messaging.
Use subagents when you need quick, focused workers that report back. Use agent teams when teammates need to share findings, challenge each other, and coordinate on their own.
Enable agent teams
Agent teams are disabled by default. Enable them by setting theCLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS environment variable to 1, either in your shell environment or through settings.json:
settings.json
-p flag, including Agent SDK sessions, Claude doesn’t spawn teammates, and a subagent that Claude names runs as an ordinary subagent even with agent teams enabled.
Start your first agent team
After enabling agent teams, describe the task and the teammates you want in natural language. Claude spawns them and coordinates work based on your prompt. This example works well because the three roles are independent and can explore the problem without waiting on each other:
- Up and down arrows: select a teammate
- Enter: open the selected teammate’s transcript and message it directly
- Escape: clear the selection. While you’re viewing a teammate’s transcript, Escape interrupts that teammate’s current turn
An idle teammate’s row stays in the panel while any teammate or subagent is still working, so you can select it to review its transcript or send it more work. Once every agent in the panel is idle, idle rows hide after 30 seconds and reappear on the teammate’s next turn; the teammate stays running and addressable while hidden. When more than three teammates are idle at once, the rows beyond the first three collapse into a single row that counts the collapsed teammates, such as
2 idle agents when five are idle. Select it and press Enter to expand the collapsed rows, or press Esc to collapse them again. Working teammates, failed teammates, and the teammate you’re viewing always keep their own rows.
If you want each teammate in its own split pane, see Choose a display mode.
Control your agent team
Tell the lead what you want in natural language. It handles team coordination, task assignment, and delegation based on your instructions.
Choose a display mode
Agent teams support two display modes:
- In-process: all teammates run inside your main terminal. Use the up and down arrow keys in the agent panel to select a teammate, then press Enter to view it and type to message it directly. Works in any terminal, no extra setup required.
- Split panes: each teammate gets its own pane. You can see everyone’s output at once and click into a pane to interact directly. Requires tmux, or iTerm2.
tmux has known limitations on certain operating systems and traditionally works best on macOS. Using tmux -CC in iTerm2 is the suggested entrypoint into tmux."in-process". Set "auto" to enable split panes when you’re already running inside a tmux session, or when your terminal is iTerm2 with the it2 CLI installed, falling back to in-process otherwise. The "tmux" setting enables split-pane mode and auto-detects whether to use tmux or iTerm2 based on your terminal.
Set "iterm2" to use iTerm2 native split panes explicitly. This mode requires the it2 CLI and shows an error with the install command if it2 is missing. The setup prompt that offers to install it2 or switch to tmux appears under "auto" or "tmux" when your terminal is iTerm2 and tmux is available as a fallback.
To overrid

*[Snapshot truncated for archival size; images omitted.]*
