# Cloudflare Internal AI Engineering Stack

> 来源：<https://blog.cloudflare.com/internal-ai-engineering-stack/>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。
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
Workers AI is Cloudflare's serverless AI inference platform which runs open-source models on GPUs across our global network. Beyond huge cost improvements compared to frontier models, a key advantage is that inference stays on the same network as your Workers, Durable Objects, and storage. No cross-cloud hops to deal with, which cause more latency, network flakiness, and additional networking configuration to manage.
Workers AI usage in the last month: 51.47B input tokens, 361.12M output tokens.
Kimi K2.5, launched on Workers AI in March 2026, is a frontier-scale open-source model with a 256k context window, tool calling, and structured outputs. As we described in our Kimi K2.5 launch post, we have a security agent that processes over 7 billion tokens per day on Kimi. That would cost an estimated $2.4M per year on a mid-tier proprietary model. But on Workers AI, it's 77% cheaper.
Beyond security, we use Workers AI for documentation review in our CI pipeline, for generating AGENTS.md context files across thousands of repositories, and for lightweight inference tasks where same-network latency matters more than peak model capability.
As open-source models continue to improve, we expect Workers AI to handle a growing share of our internal workloads.
One thing we got right early: routing through a single proxy Worker from day one. We could have had clients connect directly to AI Gateway, which would have been simpler to set up initially. But centralizing through a Worker meant we could add per-user attribution, model catalog management, and permission enforcement later without touching any client configs. Every feature described in the bootstrap section below exists because we had that single choke point. The proxy pattern gives you a control plane that direct connections don't, and if we plug in additional coding assistant tools later, the same Worker and discovery endpoint will handle them.
How it works: one URL to configure everything
The entire setup starts with one command:
opencode auth login https://opencode.internal.domain
That command triggers a chain that configures providers, models, MCP servers, agents, commands, and permissions, without the user touching a config file.
Step 1: Discover auth requirements. OpenCode fetches config from a URL like https://opencode.internal.domain/.well-known/opencode. 
This discovery endpoint is served by a Worker and the response has an auth block telling OpenCode how to authenticate, along with a config block with providers, MCP servers, agents, commands, and default permissions:
{
  "auth": {
    "command": ["cloudflared", "access", "login", "..."],
    "env": "TOKEN"
  },
  "config": {
    "provider": { "..." },
    "mcp": { "..." },
    "agent": { "..." },
    "command": { "..." },
    "permission": { "..." }
  }
}
Step 2: Authenticate via Cloudflare Access. OpenCode runs the auth command and the user authenticates through the same SSO they use for everything else at Cloudflare. cloudflared returns a signed JWT. OpenCode stores it locally and automatically attaches it to every subsequent provider request.
Step 3: Config is merged into OpenCode. The config provided is shared defaults for the entire organization, but local configs always take priority. Users can override the default model, add their own agents, or adjust project and user scoped permissions without affecting anyone else.
Inside the proxy Worker. The Worker is a simple Hono app that does three things:
- Serves the shared config. The config is compiled at deploy time from structured source files and contains placeholder values like {baseURL} for the Worker's origin. At request time, the Worker replaces these, so all provider requests route through the Worker rather than directly to model providers. Each provider gets a path prefix (/anthropic, /openai, /google-ai-studio/v1beta, /compat for Workers AI) that the Worker forwards to the corresponding AI Gateway route.
- Proxies requests to AI Gateway. When OpenCode sends a request like POST /anthropic/v1/messages, the Worker validates the Cloudflare Access JWT, then rewrites headers before forwarding:
Stripped:   authorization, cf-access-token, host
Added:      cf-aig-authorization: Bearer <API_KEY>
            cf-aig-metadata: {"userId": "<anonymous-uuid>"}
- The request goes to AI Gateway, which routes it to the appropriate provider. The response passes straight through with zero buffering. The apiKey field in the client config is empty because the Worker injects the real key server-side. No API keys exist on user machines.
- Keeps the model catalog fresh. An hourly cron trigger fetches the current OpenAI model list from models.dev, caches it in Workers KV, and injects store: false on every model for Zero Data Retention. New models get ZDR automatically without a config redeploy.
Anonymous user tracking. After JWT validation, the Worker maps the user's email to a UUID using D1 for persistent storage and KV as a read cache. AI Gateway only ever sees the anonymous UUID in cf-aig-metadata, never the email. This gives us per-user cost tracking and usage analytics without exposing identities to model providers or Gateway logs.
Config-as-code. Agents and commands are authored as markdown files with YAML frontmatter. A build script compiles them into a single JSON config validated against the OpenCode JSON schema. Every new session picks up the latest version automatically.
The overall architecture is simple and easy for anyone to deploy with our developer platform: a proxy Worker, Cloudflare Access, AI Gateway, and a client-accessible discovery endpoint that configures everything automatically. Users run one command and they're done. There’s nothing for them to configure manually, no API keys on laptops or MCP server connections to manually set up. Making changes to our agentic tools and updating what 3,000+ people get in their coding environment is just a wrangler deploy away.
The MCP Server Portal: one OAuth, multiple MCP tools
We described our full approach to governing MCP at enterprise scale in a separate post, including how we use MCP Server Portals, Cloudflare Access, and Code Mode together. Here's the short version of what we built internally.
Our internal portal aggregates 13 production MCP servers exposing 182+ tools across Backstage, GitLab, Jira, Sentry, Elasticsearch, Prometheus, Google Workspace, our internal Release Manager, and more. This unifies access and simplifies everything giving us one endpoint and one Cloudflare Access flow governing access to every tool.
Each MCP server is built on the same foundation: McpAgent from the Agents SDK, workers-oauth-provider for OAuth, and Cloudflare Access for identity. The whole thing lives in a single monorepo with shared auth infrastructure, Bazel builds, CI/CD pipelines, and catalog-info.yaml for Backstage registration. Adding a new server is mostly copying an existing one and changing the API it wraps. For more on how this works and the security architecture behind it, see our enterprise MCP reference architecture.
Code Mode at the portal layer
MCP is the right protocol for connecting AI agents to tools, but it has a practical problem: every tool definition consumes context window tokens before the model even starts working. As the number of MCP servers and tools grows, so does the token overhead, and at scale, this becomes a real cost. Code Mode is the emerging fix: instead of loading every tool schema up front, the model discovers and calls tools through code.
Our GitLab MCP server originally exposed 34 individual tools (get_merge_request, list_pipelines, get_file_content, and so on). Those 34 tool schemas consumed roughly 15,000 tokens of context window per request. On a 200K context window, that's 7.5% of the budget gone before asking a question. Multiplied across every request, every engineer, every day, it adds up.
MCP Server Portals now support Code Mode proxying, which lets us solve that problem centrally instead of one server at a time. Rather than exposing every upstream tool definition to the client, the portal collapses them into two portal-level tools: portal_codemode_search and portal_codemode_execute.
The nice thing about doing this at the portal layer is that it scales cleanly. Without Code Mode, every new MCP server adds more schema overhead to every request. With portal-level Code Mode, the client still only sees two tools even as we connect more servers behind the portal. That means less context bloat, lower token cost, and a cleaner architecture overall.
Act 2: The knowledge layer
Backstage: the knowledge graph underneath all of it
Before the iMARS team could build MCP servers that were actually useful, we needed to solve a more fundamental problem: structured data about our services and infrastructure. We need our agents to understand context outside the code base, like who owns what, how services depend on each other, where the documentation lives, and what databases a service talks to.
We run Backstage, the open-source internal developer portal originally built by Spotify, as our service catalog. It's self-hosted (not on Cloudflare products, for the record) and it tracks things like:
- 2,055 services, 167 libraries, and 122 packages
- 228 APIs with schema definitions
- 544 systems (products) across 45 domains
- 1,302 databases, 277 ClickHouse tables, 173 clusters
- 375 teams and 6,389 users with ownership mappings
- Dependency graphs connecting services to the databases, Kafka topics, and cloud resources they rely on
Our Backstage MCP server (13 tools) is available through our MCP Portal, and an agent can look up who owns a service, check what it depends on, find related API specs, and pull Tech Insights scores, all without leaving the coding session.
Without this structured data, agents are working blind. They can read the code in front of them, but they can't see the system around it. The catalog turns individual repos into a connected map of the engineering organization.
AGENTS.md: getting thousands of repos ready for AI
Early in the rollout, we kept seeing the same failure mode: coding agents produced changes that looked plausible and were still wrong for the repo. Usually the problem was local context: the model didn't know the right test command, the team's current conventions, or which parts of the codebase were off-limits. That pushed us toward AGENTS.md: a short, structured file in each repo that tells coding agents how the codebase actually works and forces teams to make that context explicit.
What AGENTS.md looks like
We built a system that generates AGENTS.md files across our GitLab instance. Because these files sit directly in the model's context window, we wanted them to stay short and high-signal. A typical file looks like this:
# AGENTS.md
## Repository
- Runtime: cloudflare workers
- Test command: `pnpm test`
- Lint command: `pnpm lint`
## How to navigate this codebase
- All cloudflare workers  are in src/workers/, one file per worker
- MCP server definitions are in src/mcp/, each tool in a separate file
- Tests mirror source: src/foo.ts -> tests/foo.test.ts
## Conventions
- Testing: use Vitest with `@cloudflare/vitest-pool-workers` (Codex: RFC 021, RFC 042)
- API patterns: Follow internal REST conventions (Codex: API-REST-01)
## Boundaries
- Do not edit generated files in `gen/`
- Do not introduce new background jobs without updating `config/`
## Dependencies
- Depends on: auth-service, config-service
- Depended on by: api-gateway, dashboard
When an agent reads this file, it doesn't have to infer the repo from scratch. It knows how the codebase is organized, which conventions to follow and which Engineering Codex rules apply.
How we generate them at scale
The generator pipeline pulls entity metadata from our Backstage service catalog (ownership, dependencies, system relationships), analyzes the repository structure to detect the language, build system, test framework, and directory layout, then maps the detected stack to relevant Engineering Codex standards. A capable model then generates the structured document, and the system opens a merge request so the owning team can review and refine it.
We've processed roughly 3,900 repositories this way. The first pass wasn't always perfect, especially for polyglot repos or unusual build setups, but even that baseline was much better than asking agents to infer everything from scratch.
The initial merge request solved the bootstrap problem, but keeping these files current mattered just as much. A stale AGENTS.md can be worse than no file at all. We closed that loop with the AI Code Reviewer, which can flag when repository changes suggest that AGENTS.md should be updated.
Act 3: The enforcement layer
The AI Code Reviewer
Every merge request at Cloudflare gets an AI code review. Integration is straightforward: teams add a single CI component to their pipeline, and from that point every MR is reviewed automatically.
We use GitLab's self-hosted solution as our CI/CD platform. The reviewer is implemented as a GitLab CI component that teams include in their pipeline. When an MR is opened or updated, the CI job runs OpenCode with a multi-agent review coordinator. The coordinator classifies the MR by risk tier (trivial, lite, or full) and delegates to specialized review agents: code qua

*[Snapshot truncated for archival size; images omitted.]*
