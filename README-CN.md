# CS146S：现代软件开发者（The Modern Software Developer）

**斯坦福大学 · Fall 2026**

> 非官方镜像：对应官网 [Syllabus](https://themodernsoftware.dev/)（课程日程 + 评分）。原文来源：[https://themodernsoftware.dev/](https://themodernsoftware.dev/)。
>
> 英文原版见：[README.md](./README.md)

## 课程日程（Course Schedule）

### 第 1 周：Coding Agent 内部机制

**主题（Topics）**

- LLM 实际是什么，以及 Agent Loop 在底层如何运转
- 核心工具集（read / write / edit / bash）以及任务如何在其中流转
- 生产级 Coding Agent 如何组织系统提示词与工具定义

**阅读（Reading）**

- [Building a Coding Agent](https://youtube.com/watch?v=s7ZzkdvCMDY)
- [Lessons from Building Claude Code](./Resource/Fall2026/week1/像Agent一样观察.md) · [原文](https://x.com/trq212/status/2027463795355095314?s=20)
- [Dive into Claude Code](./Resource/Fall2026/week1/深入剖析Claude-Code.md) · [原文](https://arxiv.org/pdf/2604.14228)

**课时（Sessions）**

- **Tue 9/22:** 课程导论 + 用约 200 行代码构建 Claude Code — [幻灯片](./Resource/Fall2026/week1/0922-导论与编码Agent.md) · [PPTX](./Resource/Fall2026/week1/0922-intro-and-coding-agent%20en.pptx) · [完成代码](./Resource/Fall2026/week1/0922-coding-agent.py)
- **Thu 9/24:** 顶尖 Coding Agent 如何设计：深入拆解定义 Agent 的系统提示词 — [幻灯片](./Resource/Fall2026/week1/0924-现代编码Agent解剖.md) · [PPTX](./Resource/Fall2026/week1/0924-agent-harness%20en.pptx) · [提示词](./Resource/Fall2026/week1/0924-prompts/) · [讲稿记录](./Resource/Fall2026/week1/0924-课堂转写精编.md) · [全文](./Resource/Fall2026/week1/0924-课堂转写.md)

### 第 2 周：高级上下文工程

**主题（Topics）**

- 高级提示技巧及各自适用场景
- RePPIT（Research / Propose / Plan / Implement / Test）与规格驱动开发
- MCP 基础：server、client、tools 与 transport
- 面向 Agent 可用性的工具设计

**阅读（Reading）**

- [The Context Tax: When to Compact](./Resource/Fall2026/week2/上下文税.md) · [原文](https://langwatch.ai/blog/context-tax-when-to-compact)
- [OpenSpec](./Resource/Fall2026/week2/OpenSpec中文.md) · [原文](https://openspec.dev)
- [Superpowers](./Resource/Fall2026/week2/Superpowers中文.md) · [原文](https://github.com/obra/superpowers)
- [Enterprise MCP (Cloudflare)](./Resource/Fall2026/week2/企业级MCP.md) · [原文](https://blog.cloudflare.com/enterprise-mcp)

**课时（Sessions）**

- **Tue 9/29:** 高级提示 + Agent 开发框架（RePPIT、规格驱动开发） — [幻灯片](./Resource/Fall2026/week2/0929-上下文工程.md) · [PPTX](./Resource/Fall2026/week2/0929-context-engineering%20en.pptx) · [讲稿记录](./Resource/Fall2026/week2/0929-课堂转写精编.md) · [全文](./Resource/Fall2026/week2/0929-课堂转写.md)
- **Thu 10/1:** MCP 与工具调用全解（理论、搭建与进阶工具设计） — [幻灯片](./Resource/Fall2026/week2/1001-MCP与工具调用.md) · [PPTX](./Resource/Fall2026/week2/1001-mcp-and-tools%20en.pptx) · [Skills 材料](./Resource/Fall2026/week2/1001-skills/) · [讲稿记录](./Resource/Fall2026/week2/1001-课堂转写精编.md) · [全文](./Resource/Fall2026/week2/1001-课堂转写.md)

### 第 3 周：Agent Skills 与 CLI

**主题（Topics）**

- Skill 是什么，以及 SKILL.md + 脚本如何编码工作流
- Web skills，以及把 Agent 能力扩展到仓库之外
- 在 CLI 中高效工作

**阅读（Reading）**

- [pstack](https://github.com/cursor/plugins/tree/main/pstack)
- [Matt Pocock's Skills](https://github.com/mattpocock/skills)
- [browse.sh](https://browse.sh)

**课时（Sessions）**

- **Tue 10/6:** Agent Skills 全解（含 web skills） — [幻灯片](./Resource/Fall2026/week3/1006-Agent技能.md) · [PPTX](./Resource/Fall2026/week3/1006-agent-skills%20en.pptx)
- **Thu 10/8:** [嘉宾：Lee Robinson（Model Behavior @ SpaceX）](./Resource/Fall2026/week3/1008-嘉宾Lee-Robinson主页.md) — [幻灯片](https://drive.google.com/file/d/1b8WiBk_lcB3ue-jZMLijSUMLj6SDiF6Z/view?usp=drive_link) · [官网](https://leerob.com)

### 第 4 周：定制 Agent 与仓库

**主题（Topics）**

- CLAUDE.md 与 AGENTS.md：各自放什么
- 用于 lint 门禁、测试运行与护栏的 Hooks
- 子 Agent 模式（planner / implementer / reviewer）

**阅读（Reading）**

- [I Still Prefer MCP Over Skills](./Resource/Fall2026/week4/仍然更喜欢MCP而不是Skills.md) · [原文](https://david.coffee/i-still-prefer-mcp-over-skills)
- [AGENTS.md (Factory Docs)](./Resource/Fall2026/week4/Factory的AGENTS-md.md) · [原文](https://docs.factory.com/harness/agents-md)
- [Steering Claude Code: Skills, Hooks, Rules, Subagents, and More](./Resource/Fall2026/week4/驾驭Claude-Code.md) · [原文](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more)
- [Writing a Good CLAUDE.md](./Resource/Fall2026/week4/写好一份CLAUDE-md.md) · [原文](https://hlyr.dev/blog/writing-a-good-claude-md)

**课时（Sessions）**

- **Tue 10/13:** 定制你的 Agent 配置（CLAUDE.md、AGENTS.md、hooks） — [幻灯片](./Resource/Fall2026/week4/1013-定制Agent配置.md) · [PPTX](./Resource/Fall2026/week4/1013-agent-config%20en.pptx)
- **Thu 10/15:** [嘉宾：Boris Cherny（Claude Code 创建者 @ Anthropic）](./Resource/Fall2026/week4/1015-嘉宾Boris-Cherny博客.md) — [官网](https://borischerny.com)

### 第 5 周：Agent 友好的代码库

**主题（Topics）**

- 怎样的仓库才算 Agent-ready：结构、文档、测试与检查
- 就绪度评分与审计
- 真实仓库里阻碍 Agent 的常见缺口

**阅读（Reading）**

- [Making Codebases Agent Ready](./Resource/Fall2026/week5/让代码库为Agent做好准备.md) · [原文](https://www.youtube.com/watch?v=ShuJ_CN6zr4)
- [Making Ergonomic Repositories](./Resource/Fall2026/week5/让仓库对Agent更顺手.md) · [原文](https://x.com/trybasis/status/2056881705269580023)

**课时（Sessions）**

- **Tue 10/20:** 仓库的 Agent 就绪度（结构、文档与检查项） — [幻灯片](./Resource/Fall2026/week5/1020-仓库Agent就绪度.md) · [PPTX](./Resource/Fall2026/week5/1020-agent-readiness%20en.pptx)
- **Thu 10/22:** [嘉宾：Eno Reyes（CTO @ Factory）](./Resource/Fall2026/week5/1022-嘉宾Eno-Reyes.md) — [LinkedIn](https://www.linkedin.com/in/enoreyes)

### 第 6 周：Agent 驱动的代码审查

**主题（Topics）**

- AI 审查擅长发现什么、容易漏掉什么
- 审查架构与自定义规则
- 把 AI 审查嵌入团队的 PR 流程

**阅读（Reading）**

- [Layered Code Review and Risk-Based Human Oversight](./Resource/Fall2026/week6/分层代码审查与按风险的人类把关.md) · [原文](https://x.com/addyosmani/status/2114604912520921136)
- [Coordinating Specialist Review Agents at Scale](./Resource/Fall2026/week6/大规模协调专项审查Agent.md) · [原文](https://blog.cloudflare.com/ai-code-review)
- [Beyond the Diff: Context, Testing, and Model Selection](./Resource/Fall2026/week6/超越Diff：上下文测试与模型选择.md) · [原文](https://greptile.com/blog/how-to-build-a-code-review-agent)

**课时（Sessions）**

- **Tue 10/27:** Agent 驱动的代码审查：最佳实践与架构 — [幻灯片](./Resource/Fall2026/week6/1027-Agent驱动的代码审查.md) · [PPTX](./Resource/Fall2026/week6/1027-agentic-code-review%20en.pptx)
- **Thu 10/29:** [嘉宾：Silas Alberti（Chief Research Officer @ Cognition）](./Resource/Fall2026/week6/1029-嘉宾Silas-Alberti主页.md) — [官网](https://sil.as)

### 第 7 周：安全

**主题（Topics）**

- SAST / SCA、依赖与密钥泄露类漏洞
- 提示注入与面向 Agent 的攻击面
- Agent 辅助的分诊与修复

**课时（Sessions）**

- **Tue 11/3:** AI 代码库中的安全
- **Thu 11/5:** [嘉宾：Isaac Evans（CEO @ Semgrep）](https://www.linkedin.com/in/isaacevans)

### 第 8 周：后台 Agent

**主题（Topics）**

- 异步、云端委派的 Agent
- 管理并行 Agent 集群
- Issue 到 PR 的流水线与触发器（Slack、Linear、GitHub）

**课时（Sessions）**

- **Tue 11/10:** 后台 Agent：异步启动任务
- **Thu 11/12:** [嘉宾：Rajesh Bhatia（Senior Director @ Cloudflare）](https://www.linkedin.com/in/rajeshbh)

### 第 9 周：打造 AI 原生团队

**主题（Topics）**

- MCP 门户与集中、带权限的工具访问
- LLM 网关、模型路由与成本优化
- 组织级落地模式

**课时（Sessions）**

- **Tue 11/17:** [嘉宾：Elad Gil（Investor @ Gil Capital）](https://eladgil.com)
- **Thu 11/19:** [嘉宾：Amjad Masad（CEO @ Replit）](https://amasad.me)

### 第 10 周：Software Factory 与未来

**主题（Topics）**

- 可自运行、自改进的软件系统
- 部署后运行与加固 Agent
- AI 软件工程接下来往哪走

**课时（Sessions）**

- **Tue 12/1:** 大团队中的 Coding Agent（MCP 门户、LLM 网关、组织模式、成本优化与模型路由）
- **Thu 12/3:** Software Factory：可自运行、自改进的软件系统

## 评分（Grading）

- **期末项目**：50%
- **每周作业**：15%
- **开源贡献**：30%
- **课堂参与**：5%

---

*内容同步自官网 Fall 2026 Syllabus：[https://themodernsoftware.dev/](https://themodernsoftware.dev/)。与斯坦福大学无隶属关系。*
