# Factory-Agent就绪度新闻

> 来源：<https://factory.ai/news/agent-readiness>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。下文为公开页可读内容的中文整理／翻译。
# Factory：Introducing Agent Readiness

Factory 新闻稿／产品文：提出 **Agent Readiness**——衡量代码库是否适合让 coding agent 可靠工作的框架与报告能力。

## 英文正文摘录

Introducing Agent Readiness
By Factory Team - January 20, 2026 - 3 minute read
Product
Share
Factory can now evaluate how well your codebase supports autonomous development. Run /readiness-report to see where you stand across eight technical pillars and five maturity levels, with specific recommendations for what to fix first.
Teams deploying AI coding agents often see uneven results. They blame the model, try a different agent, get the same thing. The real problem is usually the codebase itself.
The agent is not broken. The environment is. Missing pre-commit hooks mean the agent waits ten minutes for CI feedback instead of five seconds. Undocumented environment variables mean the agent guesses, fails, and guesses again. Build processes requiring tribal knowledge from Slack threads mean the agent has no idea how to verify its own work.
These are environment problems, not agent problems. And they compound. A codebase with poor feedback loops will defeat any agent you throw at it. A codebase with fast feedback and clear instructions will make any agent dramatically more effective.
Agent Readiness evaluates repositories across eight technical pillars. Each one addresses a specific failure mode we have observed in production deployments. Click through to see what each pillar catches and what happens without it.
Style & Validation
Linters, type checkers, formatters
Automated tools that catch bugs instantly. Without them, agents waste cycles on syntax errors and style drift that could be caught in seconds.
Examples
- •ESLint / Biome
- •TypeScript strict mode
- •Prettier / Black
Without this: Agent submits code with formatting issues, waits for CI, fixes blindly, repeats
Repositories progress through five levels. Each level represents a qualitative shift in what autonomous agents can accomplish. Select a level to see its requirements and what agents can do at that stage.
Level 3: Standardized
Production-ready for agents
Clear processes defined and enforced. Minimum bar for production-grade autonomous operation.
Key Signals
- E2E tests exist
- Docs maintained
- Security scanning
- Observability
Agent Capability
Routine maintenance: bug fixes, tests, docs, dependency upgrades.
FastAPI,GitHub CLI,pytest
Level 3 is the target. Most teams should aim here first.
We have published Agent Readiness reports for popular open source projects. You can explore them at factory.com/agent-readiness to see what different maturity levels look like in practice.
CockroachDBGo
cockroachdb/cockroach
L4
74%
FastAPIPython
fastapi/fastapi
L3
53%
ExpressTypeScript
expressjs/express
L2
28%
The contrast is instructive. CockroachDB at Level 4 has extensive CI, comprehensive testing, clear documentation, and security scanning. Express at Level 2 lacks several foundational signals. Both are successful, widely-used projects. But an agent will have a much easier time contributing to CockroachDB.
There are three ways to interact with Agent Readiness in Factory.
Run /readiness-report in Droid to evaluate any repository. The report shows your current level, which criteria pass and fail, and prioritized suggestions for what to fix first.
View your organization's readiness scores at app.factory.ai/analytics/readiness. Track progress over time, see the distribution of repositories across maturity levels, and identify which active repositories need attention.
The dashboard surfaces your lowest-scoring active repositories (those with commits in the last 90 days) with specific remediation suggestions.
Access reports via the Readiness Reports API to integrate with your existing tooling. Run readiness checks in CI/CD, build custom dashboards, or set up alerting when scores drop below thresholds.
GET/api/organization/maturity-level-reports
View full docs →
curl -X GET "https://app.factory.ai/api/organization/maturity-level-reports?limit=10" \
  -H "Authorization: Bearer fk-your-api-key"
repoIdFilter reports by repository IDlimitMaximum number of reports to returnstartAfterReport ID for pagination cursor
200 OK
~120ms
Agent Readiness evaluates 60+ criteria using LLMs, which introduces a challenge: non-determinism. The same repository could receive different scores on consecutive runs, undermining trust. We solved this by grounding each evaluation on the previous report for that repository. Before the fix, variance averaged 7% with spikes to 14.5%. After grounding, variance dropped to 0.6% and has stayed there for six weeks across 9 benchmark repositories spanning low, medium, and high readiness tiers.
Each criterion is binary: pass or fail. Most signals are file existence checks or configuration parsing. Does the linter config exist? Is branch protection enabled? Can tests run locally?
Criteria evaluate at two scopes. Repository-scoped criteria run once for the entire repo (CODEOWNERS exists, branch protection enabled). Application-scoped criteria run per application in monorepos (linter configured for each app, unit tests exist for each app). Monorepos see sc

*[Snapshot truncated for archival size; images omitted.]*
