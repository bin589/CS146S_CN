# mattpocock/skills — repository landing

> 来源：<https://github.com/mattpocock/skills>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。
> Also cited in week3 1006 PPT; stored once here.
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
Kent Beck, Extreme Programming Explained
"The best modules are deep. They allow a lot of functionality to be accessed through a simple interface."
John Ousterhout, A Philosophy Of Software Design
The Problem: Most apps built with agents are complex and hard to change. Because agents can radically speed up coding, they also accelerate software entropy. Codebases get more complex at an unprecedented rate.
The Fix for this is a radical new approach to AI-powered development: caring about the design of the code.
This is built in to every layer of these skills:
- /to-spec quizzes you about which modules you're touching before creating a spec
And crucially, /improve-codebase-architecture surveys a codebase for deepening opportunities and hands you the candidates. I recommend running it on your codebase once every few days. It is a survey, not a rescue: on a genuinely old codebase it will find real candidates, but it won't untangle the mud for you.
Software engineering fundamentals matter more than ever. These skills are my best effort at condensing these fundamentals into repeatable practices, to help you ship the best apps of your career. Enjoy.
These split on one axis: who can invoke them. User-invoked skills are reachable only when you type them (e.g. /grill-me); their job is to orchestrate. Model-invoked skills can be invoked by you or reached for automatically by the agent when the task fits; they hold the reusable discipline. A user-invoked skill may invoke model-invoked skills, but never another user-invoked one.
Skills I use daily for code work.
User-invoked
- ask-matt: Ask which skill or flow fits your situation. A router over the user-invoked skills in this repo.
- grill-with-docs: Grilling session that also builds your project's domain model, sharpening terminology and updating GLOSSARY.md and ADRs inline.
- triage: Move issues through a state machine of triage roles.
- improve-codebase-architecture: Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
- setup-matt-pocock-skills: Configure this repo for the engineering skills (issue tracker, triage labels, domain doc layout). Run once per repo before using the other engineering skills.
- to-spec: Turn the current conversation into a spec and publish it to the issue tracker. No interview, just synthesizes what you've already discussed.
- to-tickets: Break any plan, spec, or conversation into a set of tracer-bullet tickets, each declaring its blocking edges, written as text in a local file, or as native blocking links on a real tracker.
- implement: Build the work described by a spec or set of tickets, driving /tdd at pre-agreed seams and closing out with /code-review before committing.
- implement-spec: Implement a whole spec on one integration branch. Works the tickets as a task graph, running implementer subagents across the ready frontier for maximum concurrency, then closes out with /code-review.
- wayfinder: Plan a huge chunk of work, more than one agent session can hold, as a shared map of decision tickets on the issue tracker, and resolve them one at a time until the way to the destination is clear.
- retro: Suggest improvements to the coding agent's environment (navigation, automated checks, coding standards, steering files, tooling) after a session, most severe first.
Model-invoked
- prototype: Build a throwaway prototype to answer a design question, either a single shareable HTML file for state/logic questions, or several radically different UI variations toggleable from one route.
- diagnosing-bugs: Disciplined diagnosis loop for hard bugs and performance regressions: build a feedback loop that goes red on this bug → minimise → hypothesise → instrument → fix → regression-test.
- research: Investigate a question against high-trust primary sources and capture the findings as a cited Markdown file in the repo, run as a background agent.
- tdd: Test-driven development with a red-green-refactor loop. Builds fe

*[Snapshot truncated for archival size; images omitted.]*
