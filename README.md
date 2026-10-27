# CS146S: The Modern Software Developer

**Stanford University · Fall 2026**

> Unofficial mirror of the official [Syllabus](https://themodernsoftware.dev/) (Course Schedule + Grading). Source: [https://themodernsoftware.dev/](https://themodernsoftware.dev/).
>
> See also: [中文版 README-CN.md](./README-CN.md)

## Course Schedule

### Week 1: The Internals of Coding Agents

**Topics**

- What an LLM actually is, and what the agent loop looks like under the hood
- The core tool set (read, write, edit, bash) and how tasks flow through it
- How production coding agents structure their system prompts and tool definitions

**Reading**

- [Building a Coding Agent](https://youtube.com/watch?v=s7ZzkdvCMDY)
- [Lessons from Building Claude Code](./Resource/Fall2026/week1/Seeing%20like%20an%20Agent%20en.md) · [Original](https://x.com/trq212/status/2027463795355095314?s=20)
- [Dive into Claude Code](./Resource/Fall2026/week1/%20深入剖析%20Claude%20Code%20en.pdf) · [Original](https://arxiv.org/pdf/2604.14228)

**Sessions**

- **Tue 9/22:** Course intro + build Claude Code in 200 lines — [Slides](./Resource/Fall2026/week1/0922-intro-and-coding-agent%20en.pptx) · [Notes](./Resource/Fall2026/week1/0922-intro-and-coding-agent%20en.md) · [Completed code](./Resource/Fall2026/week1/0922-coding-agent.py)
- **Thu 9/24:** How state-of-the-art coding agents are designed: deep dive into the system prompts that define the agent — [Slides](./Resource/Fall2026/week1/0924-agent-harness%20en.pptx) · [Notes](./Resource/Fall2026/week1/0924-agent-harness%20en.md) · [Prompts](./Resource/Fall2026/week1/0924-prompts/) · [Transcript](./Resource/Fall2026/week1/0924-transcript%20en.txt)

### Week 2: Advanced Context Engineering

**Topics**

- Advanced prompting techniques and when each applies
- RePPIT (Research, Propose, Plan, Implement, Test) and spec-driven development
- MCP fundamentals: servers, clients, tools, and transport
- Designing tools for agent ergonomics

**Reading**

- [The Context Tax: When to Compact](./Resource/Fall2026/week2/Context%20Tax%20en.md) · [Original](https://langwatch.ai/blog/context-tax-when-to-compact)
- [OpenSpec](./Resource/Fall2026/week2/OpenSpec%20en.md) · [Original](https://openspec.dev)
- [Superpowers](./Resource/Fall2026/week2/Superpowers%20en.md) · [Original](https://github.com/obra/superpowers)
- [Enterprise MCP (Cloudflare)](./Resource/Fall2026/week2/Enterprise%20MCP%20en.md) · [Original](https://blog.cloudflare.com/enterprise-mcp)

**Sessions**

- **Tue 9/29:** Advanced prompting + agentic dev frameworks (RePPIT, spec-driven development) — [Slides](./Resource/Fall2026/week2/0929-context-engineering%20en.pptx) · [Notes](./Resource/Fall2026/week2/0929-context-engineering%20en.md) · [Transcript](./Resource/Fall2026/week2/0929-transcript%20en.txt)
- **Thu 10/1:** Full introduction to MCP and tool-calling (theory, setup, and advanced tool design) — [Slides](./Resource/Fall2026/week2/1001-mcp-and-tools%20en.pptx) · [Notes](./Resource/Fall2026/week2/1001-mcp-and-tools%20en.md) · [Skills](./Resource/Fall2026/week2/1001-skills/) · [Transcript](./Resource/Fall2026/week2/1001-transcript%20en.txt)

### Week 3: Agent Skills and CLI

**Topics**

- What skills are and how SKILL.md + scripts encode a workflow
- Web skills and extending agent capability beyond the repo
- Working effectively from the CLI

**Reading**

- [pstack](https://github.com/cursor/plugins/tree/main/pstack)
- [Matt Pocock's Skills](https://github.com/mattpocock/skills)
- [browse.sh](https://browse.sh)

**Sessions**

- **Tue 10/6:** All about agent skills (including web skills) — [Slides](./Resource/Fall2026/week3/1006-agent-skills%20en.pptx) · [Notes](./Resource/Fall2026/week3/1006-agent-skills%20en.md)
- **Thu 10/8:** [Guest: Lee Robinson (Model Behavior @ SpaceX)](./Resource/Fall2026/week3/1008-lee-robinson%20en.md) — [Slides](https://drive.google.com/file/d/1b8WiBk_lcB3ue-jZMLijSUMLj6SDiF6Z/view?usp=drive_link) · [Site](https://leerob.com)

### Week 4: Customizing Your Agent and Repository

**Topics**

- CLAUDE.md and AGENTS.md: what to put where
- Hooks for lint gates, test runs, and guardrails
- Subagent patterns (planner / implementer / reviewer)

**Reading**

- [I Still Prefer MCP Over Skills](https://david.coffee/i-still-prefer-mcp-over-skills)
- [AGENTS.md (Factory Docs)](https://docs.factory.com/harness/agents-md)
- [Steering Claude Code: Skills, Hooks, Rules, Subagents, and More](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more)
- [Writing a Good CLAUDE.md](https://hlyr.dev/blog/writing-a-good-claude-md)

**Sessions**

- **Tue 10/13:** Customizing your agentic setup (CLAUDE.md, AGENTS.md, hooks) — [Slides](https://docs.google.com/presentation/d/152VaUifBKH4T6hxd6fCKKM9kJTSAuBmkF8zSYwuTYAo/edit?usp=sharing)
- **Thu 10/15:** [Guest: Boris Cherny (Creator of Claude Code @ Anthropic)](https://borischerny.com)

### Week 5: Agent-Ready Codebases

**Topics**

- What makes a repo agent-ready: structure, docs, tests, and checks
- Scoring and auditing readiness
- Common gaps that block agents in real repos

**Reading**

- [Making Codebases Agent Ready](https://www.youtube.com/watch?v=ShuJ_CN6zr4)
- [Making Ergonomic Repositories](https://x.com/trybasis/status/2056881705269580023)

**Sessions**

- **Tue 10/20:** Agent readiness in your repos (structure, docs, and checks that make repos agent-friendly) — [Slides](https://docs.google.com/presentation/d/1yCxocmUrGIN7IrC42WB6NW08PtYYFLe1ombDj3Ay6_8/edit?usp=drive_link)
- **Thu 10/22:** [Guest: Eno Reyes (CTO @ Factory)](https://www.linkedin.com/in/enoreyes)

### Week 6: Agentic Code Review

**Topics**

- What AI review catches well, and what it misses
- Review architectures and custom rules
- Fitting AI review into a team's PR workflow

**Sessions**

- **Tue 10/27:** Agentic code review: best practices and architectures
- **Thu 10/29:** [Guest: Silas Alberti (SVP Research @ Cognition)](https://sil.as)

### Week 7: Security

**Topics**

- SAST / SCA, dependency and secret-leak vulnerabilities
- Prompt injection and agent-specific attack surfaces
- Agent-assisted triage and remediation

**Sessions**

- **Tue 11/3:** Security in AI codebases
- **Thu 11/5:** [Guest: Isaac Evans (CEO @ Semgrep)](https://www.linkedin.com/in/isaacevans)

### Week 8: Background Agents

**Topics**

- Async, cloud-delegated agents
- Managing fleets of parallel agents
- Issue-to-PR pipelines and triggers (Slack, Linear, GitHub)

**Sessions**

- **Tue 11/10:** Background agents: launching tasks asynchronously
- **Thu 11/12:** [Guest: Rajesh Bhatia (Senior Director @ Cloudflare)](https://www.linkedin.com/in/rajeshbh)

### Week 9: Building an AI-Native Team

**Topics**

- MCP portals and centralized, permissioned tool access
- LLM gateways, model routing, and cost optimization
- Org-wide adoption patterns

**Sessions**

- **Tue 11/17:** [Guest: Elad Gil (Investor @ Gil Capital)](https://eladgil.com)
- **Thu 11/19:** [Guest: Amjad Masad (CEO @ Replit)](https://amasad.me)

### Week 10: The Software Factory + The Future

**Topics**

- Self-running, self-improving software systems
- Running and securing agents post-deployment
- Where AI software engineering goes next

**Sessions**

- **Tue 12/1:** Coding agents in big teams (MCP portals, LLM gateways, org patterns, cost optimization, and model routing)
- **Thu 12/3:** The Software Factory: self-running, self-improving software systems

## Grading

- **Final Project**: 50%
- **Weekly Assignments**: 15%
- **Open Source Contributions**: 30%
- **Class Participation**: 5%

---

*Content synced from the official Fall 2026 syllabus on [https://themodernsoftware.dev/](https://themodernsoftware.dev/). Not affiliated with Stanford University.*
