# mattpocock/skills 仓库说明

> 来源：<https://github.com/mattpocock/skills>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。下文为公开页可读内容的中文整理／翻译。
> week3 的 1006 PPT 亦引用；只在 week2 存一份。
# mattpocock/skills 仓库说明

GitHub 仓库落地页归档（README 级文字）。week3 幻灯片再次引用同一仓库，见 week3 README 交叉链接，不重复存档。

## 正文摘录

My agent skills that I use every day to do real engineering - not vibe coding.
Developing real applications is hard. Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve.
These skills are designed to be small, easy to adapt, and composable. They work with any model. They're based on decades of engineering experience. Hack around with them. Make them your own. Enjoy.
If you want to keep up with changes to these skills, and any new ones I create, you can join ~60,000 other devs on my newsletter:
A plugin updates itself. skills.sh copies editable files into your project, and you update them by hand. Pick one per agent, because installing both gives you every skill twice.
Claude Code
claude plugin install mattpocock-skills@claude-plugins-official
Updates itself by default.
Codex
codex plugin marketplace add mattpocock/skills
codex plugin add mattpocock-skills@mattpocock
Updates itself at startup.
GitHub Copilot (CLI and VS Code)
copilot plugin marketplace add mattpocock/skills
copilot plugin install mattpocock-skills@mattpocock
Then, once, add to ~/.copilot/settings.json:
{
  "extraKnownMarketplaces": {
    "mattpocock": { "source": { "source": "github", "repo": "mattpocock/skills" }, "autoUpdate": true }
  }
}
In VS Code, run Chat: Install Plugin From Source and enter https://github.com/mattpocock/skills. It updates daily.
Gemini CLI (manual updates)
gemini skills install https://github.com/mattpocock/skills.git --path skills/engineering
gemini skills install https://github.com/mattpocock/skills.git --path skills/productivity
Re-run both commands to update.
Any other agent, or editable files (manual updates)
npx skills@latest add mattpocock/skills -a <agent>  # cursor, opencode, devin, windsurf, amp, pi; omit -a to choose
When the installer asks which skills to take, include setup-matt-pocock-skills. To update, run npx skills@latest update, and re-run add to pick up new skills.
In your agent, run it once per repo. It will:
- Ask you which issue tracker you want to use (GitHub, GitLab, local files, or anything else you describe)
- Ask you what labels you apply to tickets when you triage them (/triage uses labels)
- Ask you where you want to save any docs we create
I built these skills as a way to fix common failure modes I see with Claude Code, Codex, and other coding agents.
"No-one knows exactly what they want"
David Thomas & Andrew Hunt, The Pragmatic Programmer
The Problem. The most common failure mode in software development is misalignment. You think the dev knows what you want. Then you see what they've built - and you realize it didn't understand you at all.
This is just the same in the AI age. There is a communication gap between you and the agent. The fix for this is a grilling session - getting the agent to ask you detailed questions about what you're building.
The Fix is to use:
- /grill-me - for non-code uses
- /grill-with-docs - same as /grill-me, but adds more goodies (see below)
These are my most popular skills. They help you align with the agent before you get started, and think deeply about the change you're making. Use them every time you want to make a change.
With a ubiquitous language, conversations among developers and expressions of the code are all derived from the same domain model.
Eric Evans, Domain-Driven-Design
The Problem: At the start of a project, devs and the people they're building the software for (the domain experts) are usually speaking different languages.
I felt the same tension with my agents. Agents are usually dropped into a project and asked to figure out the jargon as they go. So they use 20 words where 1 will do.
The Fix for this is a shared language. It's a document that helps agents decode the jargon used in the project.
Example
Here's an example glossary (still named CONTEXT.md at that pinned commit, from before the skills renamed the convention), from my course-video-manager repo. Which one is easier to read?
- BEFORE: "There's a problem when a lesson inside a section of a course is made 'real' (i.e. given a spot in the file system)"
- AFTER: "There's a problem with the materialization cascade"
This concision pays off session after session.
This is built into /grill-with-docs. It's a grilling session, but that helps you build a shared language with the AI, and document hard-to-explain decisions in ADR's.
It's hard to explain how powerful this is. It might be the single coolest technique in this repo. Try it, and see.
Tip
A shared language has many other benefits than reducing verbosity:
- Variables, functions and files are named consistently, using the shared language
- As a result, the codebase is easier to navigate for the agent
- The agent also spends fewer tokens on thinking, because it has access to a more concise language
"Always take small, deliberate steps. The rate of feedback is your speed limit. Never take on a task that’s too big."
David Thomas & Andrew Hunt, The Pragmatic Programmer
The Problem: Let's say that you and the agent are aligned on what to build. What happens when the agent still produces crap?
It's time to look at your feedback loops. Without feedback on how the code it produces actually runs, the agent will be flying blind.
The Fix: You need the usual tranche of feedback loops: static types, browser access, and automated tests.
For automated tests, a red-green-refactor loop is critical. This is where the agent writes a failing test first, then fixes the test. This helps give the agent a consistent level of feedback that results in far better code.
I've built a /tdd skill you can slot into any project. It encourages red-green-refactor and gives the agent plenty of guidance on what makes good and bad tests.
For debugging, I've also built a /diagnosing-bugs skill that wraps best debugging practices into a disciplined loop, gated phase by phase.
"Invest in the design of the system every day."
Kent Beck, Extr

*[Snapshot truncated for archival size; images omitted.]*
