# AGENTS.md

> 来源：Factory Docs · <https://docs.factory.com/harness/agents-md>
> 页面说明：Give Droid durable project instructions, commands, and guardrails with AGENTS.md.
> 抓取时间：2026-10-27
> 说明：按文档页正文整理。示例命令、文件名与路径照录。文内相对链接按文档站补成绝对 URL。版权归 Factory 所有。

AGENTS.md gives Droid the project briefing it should carry into every session: how to install, run, test, edit, verify, and stay inside your repository's boundaries.

Use it for guidance that should be loaded before Droid writes code. Keep it short, specific, and easy to verify.

## Create your first AGENTS.md

1. **Create one root file.** Add `AGENTS.md` at the repository root. Start with one file, then add nested files only where a package, app, or service needs different rules.
2. **Put commands first.** List the exact install, development, test, type check, lint, and build commands Droid should run. Add flags or package filters when broad commands are too expensive.
3. **Add conventions and safety rules.** Capture repository layout, generated-file rules, security boundaries, ownership boundaries, and required proof before Droid calls work finished.
4. **Commit it with the project.** Project instructions belong in git so every teammate and automation session gets the same operating context.

```markdown
# Repository guide

## Commands

- Install dependencies: `pnpm install`
- Start local server: `pnpm dev`
- Run unit tests: `pnpm test`
- Run type checks: `pnpm typecheck`
- Run lint: `pnpm lint`

## Project layout

- `app/` contains routes and server-rendered pages.
- `components/` contains reusable UI components.
- `lib/` contains shared business logic and integrations.
- Tests live next to the code they cover as `*.test.ts` or `*.test.tsx`.

## Coding conventions

- Prefer small, focused modules with explicit types.
- Keep business logic in pure functions where possible.
- Match existing component and file naming patterns.
- Do not add a new dependency unless the existing stack cannot solve the problem.

## Verification

Before calling work finished, run:

1. `pnpm test`
2. `pnpm typecheck`
3. `pnpm lint`

If a command fails, fix the issue and rerun it.
```

Keep human onboarding, screenshots, and contributor background in `README.md`. Put Droid-specific commands, guardrails, and completion criteria in `AGENTS.md`.

## What to include

| Section | What good looks like |
|---|---|
| Project overview | One short paragraph explaining the product, architecture, or package. |
| Commands | Exact install, local run, test, lint, type check, build, and regeneration commands. |
| Repository map | Directories Droid must understand before editing. |
| Conventions | Project-specific patterns that are not obvious from code. |
| Testing rules | Focused test commands, full gate commands, and when to add tests. |
| Generated files | Which files are generated, what source to edit, and how to regenerate. |
| Security rules | Secret handling, production boundaries, approval rules, and migration safety. |
| PR expectations | Required evidence, screenshots, changelog notes, or review checks. |

Prefer concrete rules that change how Droid works:

```markdown
## Testing

- Run `pnpm test -- path/to/file.test.ts` for focused changes.
- Run `pnpm test` before completing broad refactors.
- Add a regression test for every bug fix when practical.
```

Avoid vague rules that cannot be checked:

```markdown
## Testing

- Be careful.
- Make sure everything works.
```

## Choose the right instruction surface

Use the narrowest durable surface for the job.

| Surface | Use for | How Droid treats it |
|---|---|---|
| `AGENTS.md` and compatible names | Always-on coding instructions, commands, repository conventions, and safety rules. | Loaded as coding guidelines at startup and during dynamic discovery. |
| `DESIGN.md`, `Design.md`, and `design.md` | Always-on design-system, UX, visual, and interaction guidance. | Loaded separately as design guidelines. |
| `SKILL.md` | Reusable workflows, checklists, or domain expertise that should load only when relevant. | Discovered as a skill. The full body loads when invoked. |
| `.factory/commands/*` | Simple user-invoked prompt or executable shortcuts. | Exposed as custom slash commands. |
| `.factory/settings.json` | Droid preferences, defaults, and policy settings. | Parsed as configuration, not as prose instructions. |

Do not paste long run books into `AGENTS.md`. Link to the source of truth, or move reusable procedures into [skills](https://docs.factory.com/docs/harness/skills) so the extra context loads only when needed.

## Discovery and precedence

When a git root is present, Droid searches from the current working directory up to the git root. At each level, it checks the directory itself and these context directories:

| Context directory | Common use |
|---|---|
| `.factory/` | Factory-specific project instructions. |
| `.agents/` | Compatibility with shared agent folder conventions. |
| `.agent/` | Compatibility with singular agent folder conventions. |

Droid also checks personal instruction directories in your home folder:

| Personal directory | Common use |
|---|---|
| `~/.factory/` | Your default Droid preferences across projects. |
| `~/.agents/` | Compatible personal instructions. |
| `~/.agent/` | Compatible personal instructions. |

When multiple instruction files apply, use this mental model:

- The current user request takes priority over standing instructions.
- Nested project files refine root project files for a specific directory tree.
- Project files should override personal defaults.
- Personal files should describe preferences, not requirements that fight repository rules.

## Compatible filenames

Use `AGENTS.md` for new guidance. Droid also reads compatible filenames so existing instruction files from other coding tools keep working.

| Filename | Use it when |
|---|---|
| `AGENTS.md` | Recommended for new project guidance. |
| `agents.md` | Lowercase compatibility variant. |
| `Agents.md` | Title-case compatibility variant. |
| `CLAUDE.md` | Compatibility with existing Claude-oriented instructions. |
| `Claude.md` | Title-case compatibility variant. |

This is a compatibility set, not a setup checklist. Do not create every file. Duplicating rules across supported filenames spends context without adding signal.

## Nested instructions

Nested files are useful when a directory tree has different commands, conventions, generated assets, or ownership rules.

```text
repository/
  AGENTS.md
  apps/
    web/
      AGENTS.md
      src/
        page.tsx
```

If Droid starts at `repository/`, it loads the root guidance. When Droid later reads files under `apps/web/`, it can discover `apps/web/AGENTS.md` and apply the more specific guidance to that directory tree.

Use nested files for real differences:

- A package uses another package manager or test runner.
- A service has generated code that must not be edited by hand.
- A frontend area has design-system rules that do not apply elsewhere.
- A deployment or migration path requires extra approval.

Do not use nested files to repeat root rules.

## Context budget

Instruction files count against the session context. Keep the top of each file dense with the rules Droid most needs.

| Load phase | Limit |
|---|---|
| Initial AGENTS-style guideline load | 80,000 characters |
| Dynamic Read-path guideline discovery | 40,000 characters |

These are caps, not targets. Smaller files are usually better.

## Root template

```markdown
# Repository guide

## What this project is

One or two sentences describing the product, service, or package.

## Commands

- Install: `REPLACE_ME`
- Run locally: `REPLACE_ME`
- Run tests: `REPLACE_ME`
- Run type checks: `REPLACE_ME`
- Run lint: `REPLACE_ME`
- Build: `REPLACE_ME`

## Project layout

- `REPLACE_ME/` contains ...
- `REPLACE_ME/` contains ...
- `REPLACE_ME/` contains ...

## Conventions

- Match existing patterns before introducing new ones.
- Keep changes scoped to the requested task.
- Prefer existing utilities and dependencies.
- Add or update tests when changing behavior.

## Verification

Before completing work, run the relevant focused checks and then the required project checks:

1. `REPLACE_ME`
2. `REPLACE_ME`
3. `REPLACE_ME`

## Safety

- Do not commit secrets or credentials.
- Do not run destructive commands without explicit approval.
- Do not modify generated files by hand. Regenerate them with `REPLACE_ME`.
```

## Nested template

```markdown
# Subproject guide

This file applies when working inside this directory tree. Follow the root `AGENTS.md` unless this file gives a more specific rule.

## Local commands

- Run this package's tests: `REPLACE_ME`
- Run this package's lint: `REPLACE_ME`
- Regenerate local artifacts: `REPLACE_ME`

## Local conventions

- Use `REPLACE_ME` for ...
- Do not use `REPLACE_ME`; this package uses `REPLACE_ME` instead.
- Keep public exports in `REPLACE_ME`.

## Verification

For changes in this directory tree, run:

1. `REPLACE_ME`
2. `REPLACE_ME`
```

## What to avoid

Do not use `AGENTS.md` as a dumping ground. Avoid:

- Secrets, credentials, private tokens, or private host names.
- Full copies of long docs that already live elsewhere.
- Stale directory inventories that drift from the repository.
- Personal preferences that conflict with project rules.
- Temporary task notes that belong in an issue, PR, or spec.
- Instructions to skip validation without a narrow, explicit reason.

If guidance is useful for one workflow, make it a skill. If it is useful for one project area, put it in a nested `AGENTS.md`.
