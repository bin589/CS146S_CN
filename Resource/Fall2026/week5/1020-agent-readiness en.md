# 1020-agent-readiness — slide transcript

> Unofficial English text extraction from the source `.pptx`, one section per slide, in presentation order.

> Source: [`1020-agent-readiness en.pptx`](./1020-agent-readiness%20en.pptx) · extracted 2026-10-27 · images in `images/1020/`

## Slide 1

- The Modern Software Developer
- CS146S
- Stanford University, Fall 2026
- Mihail Eric
- themodernsoftware.dev

## Slide 2

- Logistics
- Assignment 4 due Sunday
- How was first OSS contribution?
- Class mid-quarter survey
- Guest lecture - STLC 111 (all Thursday lectures moving forward)
- Eno Reyes
- themodernsoftware.dev

![Slide 2 image 1](images/1020/slide02-01.png)

## Slide 3

- The context story
- themodernsoftware.dev
- Labeled blocks on the slide:
   - System Prompt
   - Memory.md
   - Env info
   - MCP tools
   - Skills
   - AGENTS.md (global)
   - AGENTS.md (local)

## Slide 4

- themodernsoftware.dev
- Creating agent-ready repositories

## Slide 5

- Why
- Most codebases today aren’t set up for agent success
- Much of LLM confusion comes from trying to finish a task with a messy or incomplete developer environment
- Optimize your codebase/environment so that a human and an agent could understand what’s going on
- themodernsoftware.dev

## Slide 6

- What humans can work around
- Insufficient test coverage (manual testing)
- Outdated documentation (bother your teammates)
- No linter (you can check for semicolons)
- Flaky build (retry)
- Complex setup/onboarding (bother your teammates)
- Difficult or missing observability (check logs)
- No security scanning (don’t worry about it right now…)
- Inconsistent programmatic patterns (implicit tribal knowledge)
- themodernsoftware.dev

## Slide 7

- What breaks agents
- No tests → can’t verify correctness
- No docs/standards → can’t ensure consistency
- Unreliable build → can’t verify changes
- No observability → can’t debug
- Complex setup → no environment reproducibility
- No security check → introduces vulnerabilities
- themodernsoftware.dev

**Speaker notes:**

- A messy repo could be as simple as having different access patterns (like for a DB), variable naming, multiple functions that do the same thing

## Slide 8

- Agent-ready environment checklist
- Sufficient test coverage
- Hermetic build system
- Well-documented, consistent design patterns
- No outdated READMEs
- Verifiable checks
- An agent-specific playbook
   - AGENTS.md etc
- themodernsoftware.dev

## Slide 9

- What this enables you to do
- Large task completion (migrations, etc)
- Multiple agent workloads across team members
- Automated code review
- Long-running agentic tasks with verifiable outcomes
- Brownfield codebase agent workloads
- themodernsoftware.dev

## Slide 10

- Agent readiness demo
- themodernsoftware.dev

**Speaker notes:**

- https://factory.ai/news/agent-readiness
- https://factory.ai/agent-readiness
- Let’s check the readiness of some repos: https://app.factory.ai/analytics/readiness/https%253A%252F%252Fgithub.com%252Fvercel%252Fnext.js
- https://x.com/alvinsng/status/2030056110317818206?s=20
- https://github.com/kodustech/agent-readiness

## Slide 11

- themodernsoftware.dev
- Background Coding Agent Workflows

## Slide 12

- Why
- Progression of coding agent capabilities
   - Tab complete (2021)
      - ~15% efficiency gains
   - Synchronous single-task completion (2024)
      - ~25-35% efficiency gains
   - Background multi-task completion (2026+)
      - Unlock: 2x+ efficiency gains
- themodernsoftware.dev

## Slide 13

- What background agents require
- Isolated development environments
- Sufficient test coverage
- Hermetic build system
- Well-documented, consistent design patterns
- No outdated READMEs
- Verifiable checks
- An agent-specific playbook
   - AGENTS.md etc
- themodernsoftware.dev

**Speaker notes:**

- It’s basically the same slide as our the one from building an agent-first development environment!

## Slide 14

- Agent isolation
- Git worktrees
   - `git worktree add -b my-new-branch ../my-new-branch`
- Multi-agent orchestrators
   - Options
      - Conductor
      - Cursor parallel agents
      - Claude Code Swarms
      - Roll your own
   - Abstract away lower level setup like creating worktrees
   - Cons
      - Can have occasionally rigid UIs
      - Shared resources are not completely isolated (databases, ports)
- themodernsoftware.dev

**Speaker notes:**

- These orchestrators can make it difficult to jump between different surface areas like terminal <> IDE <> cloud

## Slide 15

- Cloud agents
- Handle all the complexity of spinning off agents with necessary environments
- You can spin off these agents across surface areas
- Options
   - Browser (Codex, Claude Code, Devin)
   - Code review (Graphite, Claude, Devin Review)
   - Communications platforms (Claude Code, Codex in Slack)
   - Mobile (native app or via 3rd party app like Slack)
   - Your task tracking software (Linear issue)
- themodernsoftware.dev
