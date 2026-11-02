# Superpowers — A Complete Software Development Methodology for Coding Agents

> 作者：Jesse Vincent 与 [Prime Radiant](https://primeradiant.com) 团队
> 仓库：<https://github.com/obra/superpowers>（MIT）
> 原文：<https://raw.githubusercontent.com/obra/superpowers/main/README.md>
> 发布说明：<https://blog.fsck.com/2025/10/09/superpowers/>
> 抓取时间：2026-10-22

Superpowers is a complete software development methodology for your coding agents, built on top of a set of composable skills and some initial instructions that make sure your agent uses them.

## How it works

It starts from the moment you fire up your coding agent. As soon as it sees that you're building something, it *doesn't* just jump into trying to write code. Instead, it steps back and asks you what you're really trying to do.

Once it's teased a spec out of the conversation, it shows it to you in chunks short enough to actually read and digest.

After you've signed off on the design, your agent puts together an implementation plan that's clear enough for an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing to follow. It emphasizes true red/green TDD, YAGNI (You Aren't Gonna Need It), and DRY.

Next up, once you say "go", it launches a *subagent-driven-development* process, having agents work through each engineering task, inspecting and reviewing their work, and continuing forward. It's not uncommon for your agent to work autonomously for a couple hours at a time without deviating from the plan you put together.

There's a bunch more to it, but that's the core of the system. And because the skills trigger automatically, you don't need to do anything special. Your coding agent just has Superpowers.

## Installation

Installation differs by harness. If you use more than one, install Superpowers separately for each one.

### Claude Code

Superpowers is available via the [official Claude plugin marketplace](https://claude.com/plugins/superpowers):

```bash
/plugin install superpowers@claude-plugins-official
```

Or via the Superpowers marketplace:

```bash
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

### Codex

Available via the [official Codex plugin marketplace](https://github.com/openai/plugins). In the Codex app, click **Plugins** in the sidebar, find `Superpowers` under Coding, click `+`. In Codex CLI, open `/plugins`, search `superpowers`, select `Install Plugin`.

### Cursor

```text
/add-plugin superpowers
```

Or search for "superpowers" in the plugin marketplace.

### Antigravity

```bash
agy plugin install https://github.com/obra/superpowers
```

Antigravity lists each installed skill's description, and the description of the `using-superpowers` skill prompts the model to load that skill at the start of a conversation. Reinstall with the same command to update.

### Gemini CLI

```bash
gemini extensions install https://github.com/obra/superpowers
gemini extensions update superpowers
```

### GitHub Copilot CLI

```bash
copilot plugin marketplace add obra/superpowers-marketplace
copilot plugin install superpowers@superpowers-marketplace
```

### Factory Droid

```bash
droid plugin marketplace add https://github.com/obra/superpowers
droid plugin install superpowers@superpowers
```

### Devin CLI

```bash
devin plugins install obra/superpowers
devin plugins update superpowers
```

### Grok Build CLI

```bash
grok plugin install superpowers@xai-official --trust
```

Or open `/marketplace` in the TUI, search for Superpowers, and install.

### Kimi Code

Open `/plugins`, go to `Marketplace` > `Superpowers` and install, or install directly:

```text
/plugins install https://github.com/obra/superpowers
```

Detailed docs: [docs/README.kimi.md](docs/README.kimi.md).

### OpenCode

OpenCode uses its own plugin install; install Superpowers separately even if you already use it in another harness:

```text
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md
```

Detailed docs: [docs/README.opencode.md](docs/README.opencode.md).

### Pi

```bash
pi install git:github.com/obra/superpowers
```

The Pi package loads the Superpowers skills and a small extension that injects the `using-superpowers` bootstrap at session startup and again after compaction. Pi has native skills, so no compatibility `Skill` tool is required.

### Qwen Code

```bash
qwen extensions install obra/superpowers
qwen extensions update superpowers
```

### Hermes Agent

```bash
hermes plugins install obra/superpowers --enable
```

Restart active Hermes sessions after installing. Note: Hermes has no post-compaction hook, so a very long session that compacts over its first turn loses the bootstrap — start a fresh session if skills stop triggering.

### Muse

```bash
muse plugins install ./
muse plugins approve superpowers
# or
git clone https://github.com/obra/superpowers.git
muse plugins install ./superpowers
muse plugins approve superpowers
```

Version is tracked in `.version-bump.json` so `scripts/bump-version.sh` keeps it in sync.

## The basic workflow

1. **brainstorming** — Activates before building anything. Draws out what you actually want, and why, through questions that get you describing it, then plays its understanding back for correction. Small changes get agreed in chat; projects get a written design document a builder could plan from.

2. **using-git-worktrees** — Activates after design approval. Creates an isolated workspace on a new branch, runs project setup, verifies a clean test baseline.

3. **writing-plans** — Activates with an approved design. Breaks work into bite-sized tasks (2–5 minutes each). Every task has exact file paths, complete code, verification steps.

4. **subagent-driven-development** or **executing-plans** — Activates with a plan. Either dispatches a fresh subagent per task with a review after each (most thorough), or implements every task inline in the current session with one fresh review of the whole branch at the end (cheapest).

5. **test-driven-development** — Activates during implementation. Enforces RED-GREEN-REFACTOR: write a failing test, watch it fail, write minimal code, watch it pass, commit. Deletes code written before tests.

6. **requesting-code-review** — Activates between tasks. Reviews against the plan, reports issues by severity. Critical issues block progress.

7. **finishing-a-development-branch** — Activates when tasks complete. Verifies tests, presents options (merge/PR/keep/discard), cleans up the worktree.

**The agent checks for relevant skills before any task.** Mandatory workflows, not suggestions.

## When something goes wrong

Sometimes a session misbehaves: a skill fires when it shouldn't, stays silent when it should, or the agent ignores its plan, repeats work, or burns more tokens than you'd expect. Ask your coding agent to "figure out what went wrong with superpowers in this session" and it will invoke the **diagnosing-superpowers** skill. To examine an earlier session, name it: "figure out what went wrong with superpowers in session `<id>`".

The skill reads the session transcript, reports what happened with line-level evidence, and, if you want, packages a scrubbed bundle for a bug report.

## What's inside

### Skills library

**Testing**
- **test-driven-development** — RED-GREEN-REFACTOR cycle (includes testing anti-patterns reference)

**Debugging**
- **systematic-debugging** — 4-phase root cause process (includes root-cause-tracing, defense-in-depth, condition-based-waiting techniques)
- **verification-before-completion** — Ensure it's actually fixed
- **diagnosing-superpowers** — Work out what went wrong in a session, with evidence; export a scrubbed bundle or file an issue

**Collaboration**
- **brainstorming** — Drawing out intent before building
- **writing-plans** — Detailed implementation plans
- **executing-plans** — Inline plan execution: one context, one final review
- **dispatching-parallel-agents** — Concurrent subagent workflows
- **requesting-code-review** — Pre-review checklist
- **receiving-code-review** — Responding to feedback
- **using-git-worktrees** — Parallel development branches
- **finishing-a-development-branch** — Merge/PR decision workflow
- **subagent-driven-development** — Fast iteration with two-stage review (spec compliance, then code quality)

**Meta**
- **writing-skills** — Create new skills following best practices (includes testing methodology)
- **using-superpowers** — Introduction to the skills system

## Philosophy

- **Test-Driven Development** — Write tests first, always
- **Systematic over ad-hoc** — Process over guessing
- **Complexity reduction** — Simplicity as primary goal
- **Evidence over claims** — Verify before declaring success

## Contributing

We don't generally accept contributions of new skills, and any updates to skills must work across all of the coding agents we support. We also don't accept agent-written PRs that fix issues filed by someone else unless a maintainer asked for one, even when you hit the same problem; add your report to the existing issue instead.

1. Fork the repository
2. Switch to the `dev` branch
3. Create a branch for your work
4. Follow the `writing-skills` skill for creating and testing new and modified skills
5. Submit a PR, filling in every section of the pull request template, including the summary a human writes in their own words

Skill-behavior tests use the drill eval harness from [superpowers-evals](https://github.com/prime-radiant-inc/superpowers-evals/), cloned into `evals/`; plugin-infrastructure tests live at `tests/` and run via the relevant `run-*.sh` or `npm test`.

## Telemetry

Skills and plugins provide no feedback to creators, so by default the Prime Radiant logo on brainstorming's optional visual companion feature is loaded from the project's website, including the version of Superpowers in use. It does not include any details about your project, prompt, or coding agent. Disable it with `SUPERPOWERS_DISABLE_TELEMETRY`; Superpowers also honors Claude Code's `DISABLE_TELEMETRY` and `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` opt-outs.

## Commercial services

For enterprise use that could benefit from commercial support, additional tooling, or managed spending: sales@primeradiant.com.

## Community

- Discord: <https://discord.gg/35wsABTejz>
- Issues: <https://github.com/obra/superpowers/issues>
- Release announcements: <https://primeradiant.com/superpowers/>

## License

MIT License — see the LICENSE file.
