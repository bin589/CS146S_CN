# kodustech-agent-readiness仓库

> 来源：<https://github.com/kodustech/agent-readiness>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。
@kodus/agent-readiness — the open-source alternative to Factory.ai's Agent Readiness.
Evaluate how ready your codebase is for autonomous AI coding agents like Claude Code, Cursor, GitHub Copilot, and Codex. 39 automated checks, 7 pillars, 10+ languages. One command:
npx @kodus/agent-readiness .$ bunx @kodus/agent-readiness .
  @kodus/agent-readiness v0.1.2
  Repository: my-project
  Project types: node
  ──────────────────────────────────────────
  Maturity Level: 3 - Structured ███████████░░░░░ 65%
  ┌───────────────────────┬────────┬───────┐
  │ Pillar                │ Score  │ Status│
  ├───────────────────────┼────────┼───────┤
  │ 🎨 Style & Linting   │  4/6   │  67%  │
  │ 🧪 Testing           │  3/6   │  50%  │
  │ 📚 Documentation      │  5/8   │  63%  │
  │ 🔧 Dev Environment   │  4/5   │  80%  │
  │ ⚙️  CI/CD             │  4/6   │  67%  │
  │ 💚 Code Health        │  1/3   │  33%  │
  │ 🔒 Security           │  3/5   │  60%  │
  └───────────────────────┴────────┴───────┘
  Recommendations:
  [LOW]  Add .editorconfig for consistent formatting
  [MED]  Configure test coverage reporting
  [MED]  Add architecture decision records
AI coding agents like Claude Code, Cursor, GitHub Copilot, OpenAI Codex, and Devin are transforming how software gets built. But their effectiveness depends heavily on how your codebase is structured.
Repos with clear conventions, solid test suites, good documentation, and consistent CI/CD pipelines let AI agents work autonomously with fewer errors and hallucinations. Repos without these foundations force agents into guesswork.
Agent readiness is the measure of how well your codebase supports autonomous AI coding. Factory.ai popularized this concept, but their solution is proprietary and cloud-only. @kodus/agent-readiness brings the same evaluation to everyone -- open source, free, and running entirely on your machine.
Factory.ai popularized the concept of "Agent Readiness" — but their solution is proprietary, cloud-only, and tied to their own AI agents.
We believe every team deserves to know how ready their codebase is, without sending code to third-party servers or paying for a score. @kodus/agent-readiness runs entirely on your machine, works with any AI agent, and is free forever.
| Feature | @kodus/agent-readiness | Factory.ai | 
|---|---|---|
| Open Source | MIT License | Proprietary | 
| Pricing | Free forever | Token-based billing | 
| Vendor lock-in | None -- agent-agnostic | Tied to Factory Droids | 
| Self-hosted | Runs locally on your machine | Cloud only | 
| Data privacy | Your code never leaves your machine | Sent to their servers | 
| Customizable | Fully configurable via .kodus-readiness.yml | Limited | 
| CI/CD integration | --ci + --min-level flags | API only | 
| Languages | Node, Python, Go, Rust, Java, Kotlin, C#, Ruby, PHP, Swift | Limited | 
- 39 automated checks across 7 pillars of codebase readiness
- 5 maturity levels from Foundational to Autonomous
- Interactive web dashboard with radar charts and detailed breakdowns
- AI-powered analysis (optional) via --ai flag for deeper code evaluation
- Multi-language support: Node.js, Python, Go, Rust, Java, Kotlin, C#/.NET, Ruby, PHP, Swift
- Monorepo detection: npm/yarn/pnpm workspaces, Lerna, Nx, Turborepo
- CI/CD gates with --ci and --min-level for quality enforcement
- Fully configurable via .kodus-readiness.yml
- JSON output for programmatic integrations
Run it instantly with no installation:
# Using npx (works everywhere)
npx @kodus/agent-readiness .
# Using bun
bunx @kodus/agent-readiness .
# Evaluate a specific repository
npx @kodus/agent-readiness /path/to/repo
# With AI-powered analysis
npx @kodus/agent-readiness . --ai --api-key sk-your-key
# JSON output for integrations
npx @kodus/agent-readiness . --format json
# CI mode with minimum level gate
npx @kodus/agent-readiness . --ci --min-level 3
Agent readiness is evaluated across seven pillars, each covering a critical aspect of codebase health for AI agents:
| Pillar | Description | Checks | 
|---|---|---|
| 🎨 Style & Linting | Consistent code style and static analysis enforcement | Linter, formatter, type checker, pre-commit hooks, editorconfig, naming conventions | 
| 🧪 Testing | Presence, breadth, and automation of your test suite | Test framework, test files, test script, coverage config, E2E tests, test quality | 
| 📚 Documentation | Quality and breadth of documentation for humans and AI | README, contributing guide, API docs, CODEOWNERS, AI context files, architecture docs, README quality, agent-friendliness | 
| 🔧 Dev Environment | Reproducible, well-documented developer setup | Lock file, containerization, env documentation, setup scripts, version pinning | 
| ⚙️ CI/CD | Continuous integration and delivery pipeline coverage | CI config, CI runs tests, CI runs linters, build automation, deploy pipeline, branch protection | 
| 💚 Code Health | Dependency freshness, dead code, and bundle hygiene | Outdated deps detection, dead code detection, bundle analysis | 
| 🔒 Security | Security posture including scanning and secret detection | License, security scanning, secrets detection, security policy, dependency update automation | 
Your codebase is assigned a maturity level based on which criteria pass at each tier. You must pass at least 80% of criteria at a level to advance to the next.
| Level | Name | Description | 
|---|---|---|
| 1 | Foundational | Basic setup and essential files present (README, license, lock file, editorconfig) | 
| 2 | Guided | Core tooling configured -- linters, formatters, test frameworks, CI basics | 
| 3 | Structured | Good practices established -- type checking, pre-commit hooks, security policies, containerization | 
| 4 | Optimized | Advanced practices -- coverage reporting, E2E tests, deploy pipelines, security scanning | 
| 5 | Autonomous | Maximum AI agent readiness -- AI context files, architecture docs, naming conventions, bundle analysis | 
Usage: agent-readiness [path] [options]
Arguments:
  path                   Path to the repository to evaluate (default: current directory)
Options:
  --ai                   Enable AI-powered criteria evaluation
  --api-key <key>        API key for AI evaluations (or set KODUS_API_KEY / OPENAI_API_KEY)
  --api-base-url <url>   Base URL for the LLM API (OpenAI-compatible)
  --model <model>        LLM model to use for AI evaluations
  --ci                   Run in CI mode (non-interactive, exit code reflects level)
  --format <format>      Output format: "text" or "json" (default: "text")
  --min-level <n>        Minimum maturity level required (1-5). Exits with code 1 if below threshold
  --no-color             Disable colored output
  --no-web               Disable the web dashboard
  --init                 Generate a .kodus-readiness.yml config file and exit
  -V, --version          Show version number
  -h, --help             Show help
| Variable | Description | 
|---|---|
| KODUS_API_KEY | API key for AI-powered evaluations | 
| OPENAI_API_KEY | Fallback API key for AI evaluations | 
| CI | When set to "true", automatically enables CI mode | 
After running an evaluation, an interactive web dashboard opens automatically in your browser. It provides:
- Radar chart visualizing scores across all 7 pillars
- Detailed criterion breakdown with pass/fail status and messages
- Recommendations prioritized by impact and effort
- Project overview including detected languages and monorepo structure
To disable the dashboard, use the --no-web flag:
bunx @kodus/agent-readiness . --no-web
Generate a default configuration file:
bunx @kodus/agent-readiness --init
This creates a .kodus-readiness.yml in your repository root:
# Toggle entire pillars on or off
pillars:
  style-linting: true
  testing: true
  documentation: true
  dev-environment: true
  ci-cd: true
  code-health: true
  security: true
# Fine-grained toggles for individual criteria
criteria:
  # Style & Linting
  linter: true
  formatter: true
  type-checker: true
  pre-commit-hooks: true
  editorconfig: true
  naming-conventions: true
  # Testing
  test-framework: true
  test-files-exist: true
  test-script: true
  coverage-config: true
  e2e-tests: true
  test-quality: true
  # Documentation
  readme: true
  contributing: true
  api-docs: true
  codeowners: true
  ai-context: true
  architecture-docs: true
  readme-quality: true
  docs-agent-friendliness: true
  # Dev Environment
  lock-file: true
  containerization: true
  env-documentation: true
  setup-script: true
  version-pinned: true
  # CI/CD
  ci-config: true
  ci-runs-tests: true
  ci-runs-linters: true
  build-automated: true
  deploy-pipeline: true
  branch-protection: true
  # Code Health
  no-outdated-deps: true
  dead-code-detection: true
  bundle-analysis: true
  # Security
  license: true
  security-scanning: true
  secrets-detection: true
  security-policy: true
  dep-update-automation: true
# Thresholds
thresholds:
  # Minimum percentage of criteria that must pass to reach a level (default: 0.8)
  # level-pass: 0.8
# AI Settings
# aiEnabled: false
# apiKey: ""           # Or set KODUS_API_KEY env variable
# apiBaseUrl: ""       # Custom endpoint for the LLM API
CLI flags always override config file values.
Use @kodus/agent-readiness as a quality gate in your CI pipeline. The --ci flag enables non-interactive mode, and --min-level fails the build if your codebase doesn't meet the required maturity level.
name: Agent Readiness Check
on: [push, pull_request]
jobs:
  readiness:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: oven-sh/setup-bun@v2
        with:
          bun-version: latest
      - name: Check AI Agent Readiness
        run: bunx @kodus/agent-readiness . --ci --min-level 3      - name: Check AI Agent Readiness (with AI)
        run: bunx @kodus/agent-readiness . --ci --min-level 3 --ai
        env:
          KODUS_API_KEY: ${{ secrets.KODUS_API_KEY }}
| Code | Meaning | 
|---|---|
| 0 | Passed -- maturity level mee

*[Snapshot truncated for archival size; images omitted.]*
