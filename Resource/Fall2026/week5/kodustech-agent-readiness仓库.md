# kodustech-agent-readiness仓库

> 来源：<https://github.com/kodustech/agent-readiness>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。下文为公开页可读内容的中文整理／翻译。
# kodustech/agent-readiness 仓库

开源的 Agent Readiness 相关项目（Factory 方案的开源替代叙述）。仅归档 GitHub 落地页，未克隆。

## 英文正文摘录

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
| 💚 Code Health | Dependency freshness, dead code, and bundle hygiene | Outdated deps detection, dead code detection, bundl

*[Snapshot truncated for archival size; images omitted.]*
