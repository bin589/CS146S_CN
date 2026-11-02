# Cloudflare内部AI工程栈

> 来源：<https://blog.cloudflare.com/internal-ai-engineering-stack/>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。下文为公开页可读内容的中文整理／翻译。
# Cloudflare 内部 AI 工程栈

Cloudflare 博客：介绍公司内部 AI／agent 工程平台与工具链。注意：本仓库 week6 阅读材料另有一篇 **不同 URL** 的 `ai-code-review`（专项审查 agent 编排）；本篇是幻灯片 speaker notes 引用的 `internal-ai-engineering-stack`。

## 英文正文摘录

The AI engineering stack we built internally — on the platform we ship
In the last 30 days, 93% of Cloudflare’s R&D organization used AI coding tools powered by infrastructure we built on our own platform.
Eleven months ago, we undertook a major project: to truly integrate AI into our engineering stack. We needed to build the internal MCP servers, access layer, and AI tooling necessary for agents to be useful at Cloudflare. We pulled together engineers from across the company to form a tiger team called iMARS (Internal MCP Agent/Server Rollout Squad). The sustained work landed with the Dev Productivity team, who also own much of our internal tooling including CI/CD, build systems, and automation.
Here are some numbers that capture our own agentic AI use over the last 30 days:
- 3,683 internal users actively using AI coding tools (60% company-wide, 93% across R&D), out of approximately 6,100 total employees
- 47.95 million AI requests
- 295 teams are currently utilizing agentic AI tools and coding assistants.
- 20.18 million AI Gateway requests per month
- 241.37 billion tokens routed through AI Gateway
- 51.83 billion tokens processed on Workers AI
The impact on developer velocity internally is clear: we’ve never seen a quarter-to-quarter increase in merge requests to this degree.
As AI tooling adoption has grown the 4-week rolling average has climbed from ~5,600/week to over 8,700. The week of March 23 hit 10,952, nearly double the Q4 baseline.
MCP servers were the starting point, but the team quickly realized we needed to go further: rethink how standards are codified, how code gets reviewed, how engineers onboard, and how changes propagate across thousands of repos.
This post dives deep into what that looked like over the past eleven months and where we ended up. We're publishing now, to close out Agents Week, because the AI engineering stack we built internally runs on the same products we’re shipping and enhancing this week.
The architecture at a glance
The engineer-facing tools layer (OpenCode, Windsurf, and other MCP-compatible clients) include both open-source and third-party coding assistant tools.
Each layer maps to a Cloudflare product or tool we use:
| What we built | Built with | 
|---|---|
| Zero Trust authentication | Cloudflare Access | 
| Centralized LLM routing, cost tracking, BYOK, and Zero Data Retention controls | AI Gateway | 
| On-platform inference with open-weight models | Workers AI | 
| MCP Server Portal with single OAuth | Workers + Access | 
| AI Code Reviewer CI integration | Workers + AI Gateway | 
| Sandboxed execution for agent-generated code (Code Mode) | Dynamic Workers | 
| Stateful, long-running agent sessions | Agents SDK (McpAgent, Durable Objects) | 
| Isolated environments for cloning, building, and testing | Sandbox SDK — GA as of Agents Week | 
| Durable multi-step workflows | Workflows — scaled 10x during Agents Week | 
| 16K+ entity knowledge graph | Backstage (OSS) | 
None of this is internal-only infrastructure. Everything (besides Backstage) listed above is a shipping product, and many of them got substantial updates during Agents Week.
We’ll walk through this in three acts:
- The platform layer — how authentication, routing, and inference work (AI Gateway, Workers AI, MCP Portal, Code Mode)
- The knowledge layer — how agents understand our systems (Backstage, AGENTS.md)
- The enforcement layer — how we keep quality high at scale (AI Code Reviewer, Engineering Codex)
Act 1: The platform layer
How AI Gateway helped us stay secure and improve the developer experience
When you have over 3,600+ internal users using AI coding tools daily, you need to solve for access and visibility across many clients, use cases, and roles.
Everything starts with Cloudflare Access, which handles all authentication and zero-trust policy enforcement. Once authenticated, every LLM request routes through AI Gateway. This gives us a single place to manage provider keys, cost tracking, and data retention policies.
The OpenCode AI Gateway overview: 688.46k requests per day, 10.57B tokens per day, routing to four providers through one endpoint.
AI Gateway analytics show how monthly usage is distributed across model providers. Over the last month, internal request volume broke down as follows.
| Provider | Requests/month | Share | 
|---|---|---|
| Frontier Labs (OpenAI, Anthropic, Google) | 13.38M | 91.16% | 
| Workers AI | 1.3M | 8.84% | 
Frontier models handle the bulk of complex agentic coding work for now, but Workers AI is already a significant part of the mix and handles an increasing share of our agentic engineering workloads.
How we increasingly leverage Workers AI
Workers AI is Cloudflare's serverless AI inference platform which runs open-source models on GPUs across our global network. Beyond huge cost improvements compared to frontier models, a key advantage is that inference stays on the same network as your Workers, Durable Objects, and storage. No cross-cloud hops to deal with

*[Snapshot truncated for archival size; images omitted.]*
