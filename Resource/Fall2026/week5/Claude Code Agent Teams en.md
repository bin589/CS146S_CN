# Claude Code Agent Teams

> 来源：<https://code.claude.com/docs/en/agent-teams>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。
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
To override the default, set teammateMode in ~/.claude/settings.json:
--teammate-mode flag is experimental and doesn’t appear in claude --help.
Split-pane mode requires either tmux or iTerm2 with the it2 CLI. To install manually:
- tmux: install through your system’s package manager. See the tmux wiki for platform-specific instructions.
- iTerm2: install the it2 CLI, then enable the Python API in iTerm2 → Settings → General → Magic → Enable Python API.
Specify teammates and models
Claude decides the number of teammates to spawn based on your task, or you can specify exactly what you want:
- The model your spawn prompt names for that teammate.
- For a teammate spawned from a subagent definition, the definition’s model, where inherit selects the lead’s model.
- CLAUDE_CODE_SUBAGENT_MODEL, when it’s set to anything other than inherit.
- The lead’s current model.
If an installed mod sets a model in its
agent.spawn hook, Claude Code uses that model in place of the first source.
If you set CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1, the first two sources don’t apply. Claude Code picks every teammate’s model from CLAUDE_CODE_SUBAGENT_MODEL when it’s set to anything other than inherit, and from the lead’s current model otherwise. Requires Claude Code v2.1.257 or later.
Before v2.1.251, CLAUDE_CODE_SUBAGENT_MODEL came first in this order.
teammateDefaultModel was removed in v2.1.234; Claude Code ignores a leftover value. Name the model in your prompt instead.availableModels allowlist. When the allowlist blocks a value, Claude Code substitutes another model:
- Family alias such as opus: On the Anthropic API and Claude Platform on AWS, Claude Code runs the teammate on the newest version of that family the allowlist permits. On providers with provider-specific model IDs, where the substitution doesn’t operate, a blocked alias falls back like any other blocked value per the next bullet
- Any other blocked value, including a family alias on providers where the substitution doesn’t operate, or one whose family has no permitted version: Claude Code runs the teammate on the lead’s model instead. If you set CLAUDE_CODE_SUBAGENT_MODEL, Claude Code tries that model first, under these same rules
By default, teammates inherit the lead’s effort level. In split-pane mode this applies from v2.1.186; earlier versions did not pass the lead’s session effort to split-pane teammates.
Have teammates plan before implementing
For complex or risky tasks, you can have teammates plan before implementing. A teammate that Claude spawns while the lead is in plan mode works in read-only plan mode until its plan is ready. Switch the lead into plan mode first, then ask for the teammate:Shift+Tab while viewing its session, the lead reviews that run’s plan instead of Claude Code approving it. You aren’t asked to approve it; the lead approves it or sends it back for revision.
Talk to teammates directly
Each teammate is a full, independent Claude Code session. You can message any teammate directly to give additional instructions, ask follow-up questions, or redirect their approach.
- In-process mode: use the up and down arrow keys in the agent panel to select a teammate, then press Enter to view its session and type to send it a message. Press x on a selected teammate to stop it. Press Ctrl+T to toggle the task list.
- Split-pane mode: click into a teammate’s pane to interact with their session directly. Each teammate has a full view of their own terminal.
While you’re viewing an in-process teammate, plain text and skills go to that teammate, and built-in commands go to the lead’s session, with these safeguards:
- /compact, /clear, and /rewind act on the lead’s conversation, so Claude Code asks you to confirm before running one of them from this view.
- /model and /fast set the lead’s model and fast mode, not the teammate’s, so they don’t run from this view. A notice tells you why.
A teammate’s model and fast mode are fixed when it spawns.
Assign and claim tasks
The shared task list coordinates work across the team. The lead creates tasks and teammates work through them. Tasks have three states: pending, in progress, and completed. A task can also depend on other tasks and shows as blocked in the task list until they’re completed. Teammates don’t self-claim a blocked task, but you or the lead can still assign it. Agents without the Task tools coordinate through messages instead of the shared task list. The lead can assign tasks explicitly, or teammates can self-claim:
- Lead assigns: tell the lead which task to give to which teammate
- Self-claim: after finishing a task, a teammate picks up the next unassigned, unblocked task on its own
Task claiming uses file locking to prevent race conditions when multiple teammates try to claim the same task simultaneously.
Shut down teammates
To gracefully end a teammate’s session, refer to it by name. For example, with a teammate named researcher:
Enforce quality gates with hooks
Use hooks to enforce rules when teammates finish wor

*[Snapshot truncated for archival size; images omitted.]*
