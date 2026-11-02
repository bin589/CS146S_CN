# next.js AGENTS.md（canary）

> 来源：<https://github.com/vercel/next.js/blob/canary/AGENTS.md>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。下文为公开页可读内容的中文整理／翻译。
# vercel/next.js canary 分支 AGENTS.md

课程幻灯片引用的大型仓库 AGENTS.md 范例。以下为 canary 分支 raw 文件归档（可截断）。未克隆整个 next.js 仓库。

## 文件正文

# Next.js Development Guide

## Codebase structure

### Monorepo Overview

This is a pnpm monorepo containing the Next.js framework and related packages.

```
next.js/
├── packages/           # Published npm packages
├── turbopack/          # Turbopack bundler (Rust) - git subtree
├── crates/             # Rust crates for Next.js SWC bindings
├── test/               # All test suites
├── examples/           # Example Next.js applications
├── docs/               # Documentation
└── scripts/            # Build and maintenance scripts
```

### Core Package: `packages/next`

The main Next.js framework lives in `packages/next/`. This is what gets published as the `next` npm package.

**Source code** is in `packages/next/src/`.

**Key entry points:**

- Dev server: `src/cli/next-dev.ts` → `src/server/dev/next-dev-server.ts`
- Production server: `src/cli/next-start.ts` → `src/server/next-server.ts`
- Build: `src/cli/next-build.ts` → `src/build/index.ts`

**Compiled output** goes to `packages/next/dist/` (mirrors src/ structure).

### Other Important Packages

- `packages/create-next-app/` - The `create-next-app` CLI tool
- `packages/next-swc/` - Native Rust bindings (SWC transforms)
- `packages/eslint-plugin-next/` - ESLint rules for Next.js
- `packages/font/` - `next/font` implementation
- `packages/third-parties/` - Third-party script integrations

### README files

Before editing or creating files in any subdirectory (e.g., `packages/*`, `crates/*`), read all `README.md` files in the directory path from the repo root up to and including the target file's directory. This helps identify any local patterns, conventions, and documentation.

**Example:** Before editing `turbopack/crates/turbopack-ecmascript-runtime/js/src/nodejs/runtime/runtime-base.ts`, read:

- `turbopack/README.md` (if exists)
- `turbopack/crates/README.md` (if exists)
- `turbopack/crates/turbopack-ecmascript-runtime/README.md` (if exists)
- `turbopack/crates/turbopack-ecmascript-runtime/js/README.md` (if exists - closest to target file)

## Build Commands

```bash
# Build the Next.js package
pnpm --filter=next build

# Build all JS code
pnpm build

# Build all JS and Rust code
pnpm build-all

# Run specific task
pnpm --filter=next exec taskr <task>
```

## Fast Local Development

For iterative Next.js source development, default to watch mode plus the explicit test script that matches the mode and bundler being verified.

**Default agent rule:** If you are changing Next.js source, start `pnpm --filter=next dev` in a separate terminal session before making edits (unless it is already running). If you skip this, explicitly state why (for example: docs-only, test-only, read-only investigation, or CI-only analysis).

**Test-only changes:** When changes are confined to `test/`, do not start `pnpm --filter=next dev` or rebuild Next.js. Run the relevant mode-specific tests directly; the test harness builds test fixtures as needed. This assumes the workspace is already bootstrapped and framework build outputs are current. Missing or stale framework build outputs still require a build.

**1. Start watch build in background:**

```bash
# Auto-rebuilds on file changes (~1-2s per change vs ~60s full build)
# Keep this running while you iterate on code
pnpm --filter=next dev
```

**2. Run focused tests with the matching mode script:**

```bash
# Development mode with Turbopack
pnpm test-dev-turbo test/path/to/test.ts

# Development mode with Webpack
pnpm test-dev-webpack test/path/to/test.ts

# Production build+start with Turbopack
pnpm test-start-turbo test/path/to/test.ts

# Production build+start with Webpack
pnpm test-start-webpack test/path/to/test.ts
```

**3. When done, kill the background watch process (if you started it).**

**For type errors only:** Use `pnpm --filter=next types` (~10s) instead of `pnpm --filter=next build` (~60s).

**Bootstrapping a new clone or worktree does not require `pnpm build-all`.** `pnpm install` already pulls in recent published native bindings, so build only what your work changes: `pnpm --filter=next build` when edits are limited to core Next.js files, `pnpm build` when changes span multiple JS packages, and `pnpm build-all` only when changes include Rust/Turbopack code. Test-only changes do not require a framework rebuild before CI push.

**Switching branches or pulling can still require a build** when it moves JS or Rust source relative to your build outputs: rebuild the affected parts before running tests (`pnpm build` for JS, `pnpm build-all` for Rust). If Next.js fails to start afterwards, the published native bindings may lag canary; see [Stale Native Binary](#stale-native-binary).

## Bundler Selection

Turbopack is the default bundler for both `next dev` and `next build`. To force webpack:

```bash
next build --webpack        # Production build with webpack
next dev --webpack          # Dev server with webpack
```

There is no `--no-turbopack` flag.

## Testing

```bash
# Run specific test file (development mode with Turbopack)
pnpm test-dev-turbo test/path/to/test.test.ts

# Run tests matching pattern
pnpm test-dev-turbo -t "pattern"

# Run development tests
pnpm test-dev-turbo test/development/
```

**Test commands by mode:**

- `pnpm test-dev-turbo` - Development mode with Turbopack (default)
- `pnpm test-dev-webpack` - Development mode with Webpack
- `pnpm test-start-turbo` - Production build+start with Turbopack
- `pnpm test-start-webpack` - Production build+start with Webpack

**Other test commands:**

- `pnpm test-unit` - Run unit tests only (fast, no browser)
- `pnpm new-test` - Generate a new test file from template (interactive)

**Generate tests non-interactively (for AI agents):**

Generating tests using `pnpm new-test` is mandatory.

```bash
# Use --args for non-interactive mode. It is a `turbo gen` flag, so pass it
# directly, without a `--` separator.
# Format: pnpm new-test --args <appDir> <name> <type>
# appDir: true/false (is this for app directory?)
# name: test name (e.g. "my-feature")
# type: e2e | production | development | unit

pnpm new-test --args true my-feature e2e

# Unit tests are created as a flat test/unit/<name>.test.ts (appDir is ignored)
pnpm new-test --args false my-util unit
```

**Analyzing test output efficiently:**

Never re-run the same test suite with different grep filters. Capture output once to a file, then read from it:

```bash
# Run once, save everything
HEADLESS=true pnpm test-dev-turbo test/path/to/test.ts > /tmp/test-output.log 2>&1

# Then analyze without re-running
grep "●" /tmp/test-output.log            # Failed test names
grep -A5 "Error:" /tmp/test-output.log   # Error details
tail -5 /tmp/test-output.log             # Summary
```

## Writing Tests

**Test writing expectations:**

- **Prefer integration tests over unit tests.** Use Next.js e2e tests
  (`test/e2e/`, `test/development/`, `test/production/`) for Next.js features,
  and Turbopack execution tests
  (`turbopack/crates/turbopack-tests/tests/execution/`) for Turbopack features.

- **Avoid unit tests that map directly to the implementation**, except for
  complicated algorithms. You can temporarily write unit tests to verify an
  implementation, but don't commit them or add them to the pull request unless
  they are necessary.

- **Use `pnpm new-test` to generate new test suites** - it creates proper structure with fixture files

- **Normalize filesystem paths in cross-platform assertions.** Windows
  `path.join()` uses backslashes. Normalize paths from mocked filesystem calls,
  including `cp` sources and destinations, before positive or negative checks
  that use `/`. Otherwise tests can fail on Windows or pass for the wrong reason.

- **Use `retry()` from `next-test-utils` instead of `setTimeout` for waiting**

  ```typescript
  // Good - use retry() for polling/waiting
  import { retry } from 'next-test-utils'
  await retry(async () => {
    const text = await browser.elementByCss('p').text()
    expect(text).toBe('expected value')
  })

  // Bad - don't use setTimeout for waiting
  await new Promise((resolve) => setTimeout(resolve, 1000))
  ```

- **Do NOT use `check()` - it is deprecated. Use `retry()` + `expect()` instead**

  ```typescript
  // Deprecated - don't use check()
  await check(() => browser.elementByCss('p').text(), /expected/)

  // Good - use retry() with expect()
  await retry(async () => {
    const text = await browser.elementByCss('p').text()
    expect(text).toMatch(/expected/)
  })
  ```

- **Prefer real fixture directories over inline `files` objects**

  ```typescript
  // Good - use a real directory with fixture files
  const { next } = nextTestSetup({
    files: __dirname, // points to directory containing test fixtures
  })

  // Avoid - inline file definitions are harder to maintain
  const { next } = nextTestSetup({
    files: {
      'app/page.tsx': `export default function Page() { ... }`,
    },
  })
  ```

- **Keep `revalidatePath`/`revalidateTag` arguments and fetch URLs
  suite-unique.** In deploy mode the cache lives at Vercel project scope and
  deploy e2e suites share one project per matrix dimension: revalidation
  purges by tag/path across the whole project, and fetch cache entries are
  keyed by URL across deployments. Prefix tags with the suite slug (e.g.
  `cacheTag('app-static:thankyounext')`), never revalidate `/` from a
  deploy-active fixture (every app has a `/` route — move the page to a
  suite-unique route and revalidate that instead), and when a test depends on
  a cached value, give the data-endpoint URL suite-unique query params (e.g.
  `api/random?app-static-page`) so another fixture's fetches and
  revalidations cannot share or purge the entry. See `test/AGENTS.md`.

## Linting and Types

```bash
pnpm lint              # Full lint (types, prettier, eslint, ast-grep)
pnpm lint-fix          # Auto-fix lint issues
pnpm prettier-fix      # Fix formatting only
pnpm types             # TypeScript type checking
```

Type-check with the repo's own commands. `pnpm typescript` runs `tsc --noEmit` against the root `tsconfig.json`, which includes `scripts/**/*.js` and loads this repo's type augmentations. A hand-rolled `tsconfig` pointed at a single file misses those augmentations and will report clean while CI fails. For example `NodeJS.ProcessEnv` is declared in `packages/next/types/global.d.ts` with `NODE_ENV` required, so a plain `Record<string, string>` is not a valid `env` for an `execa` call.

## PR Status (CI Failures and Reviews)

Use `$pr-status-triage` whenever the user asks about CI failures, PR reviews, or
PR status. It contains the `scripts/pr-status.js` commands, prioritization,
review-thread workflow, and CI reproduction guidance. See
`.agents/skills/pr-status-triage/SKILL.md`.

## GitHub Pull Requests

Check and see if you are creating a fork PR or a branch PR.
Branch PRs are PRs where the branch is part of the `vercel/next.js` repository. These PRs are created by Vercel employees.
Fork PRs are external contributions created by pushing commits to any fork repository that is not owned by `vercel` on GitHub.

- You cannot write full descriptions for fork PRs where the merge target is `vercel/next.js`.
- You can write descriptions for branch PRs and local commits.
- You can write titles and messages for local commits.
- You can assist the user in translating their descriptions to English.

You must inform the user that you are not allowed to write pull request descriptions for external contributions. Refer to the guidelines in `.github/pull_request_template.md`.
While you cannot write the full description for the user, you may offer to help review the description, or provide helpful technical details. You can provide them a link to the GitHub URL to create the PR.

### Adopting a Fork PR

Fork PRs run without repository secrets, so deploy tests never run on them. To run those tests, a maintainer adopts the PR: the contributor's commits are re-pushed to a branch in `vercel/next.js` and a replacement

*[Snapshot truncated for archival size; images omitted.]*
