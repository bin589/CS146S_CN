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
- [Lessons from Building Claude Code](https://x.com/trq212/status/2027463795355095314?s=20)
- [Dive into Claude Code](https://arxiv.org/pdf/2604.14228)

**课时（Sessions）**

- **Tue 9/22:** 课程导论 + 用约 200 行代码构建 Claude Code — [幻灯片](https://docs.google.com/presentation/d/1uztIhjHAG6O_9QOD1N_3wdhwhABml1fANXEN2dGwdbg/edit?usp=drive_link) · [完成代码](https://drive.google.com/file/d/1DxKa_autBOu9s8DvItodgUAwH_pBg7aR/view?usp=drive_link)
- **Thu 9/24:** 顶尖 Coding Agent 如何设计：深入拆解定义 Agent 的系统提示词 — [幻灯片](https://docs.google.com/presentation/d/1RZu-p18Qybbgm8WVP2RH04ESc4Bn377B-T9j5-TBFdQ/edit?usp=drive_link) · [提示词](https://drive.google.com/drive/folders/1c6_atVW0RrqEBWsNIscG2KNwCiuPxWQG?usp=drive_link) · [讲稿记录](https://themodernsoftware.dev/materials/9-24-26-transcript.txt)

### 第 2 周：高级上下文工程

**主题（Topics）**

- 高级提示技巧及各自适用场景
- RePPIT（Research / Propose / Plan / Implement / Test）与规格驱动开发
- MCP 基础：server、client、tools 与 transport
- 面向 Agent 可用性的工具设计

**阅读（Reading）**

- [The Context Tax: When to Compact](https://langwatch.ai/blog/context-tax-when-to-compact)
- [OpenSpec](https://openspec.dev)
- [Superpowers](https://github.com/obra/superpowers)
- [Enterprise MCP (Cloudflare)](https://blog.cloudflare.com/enterprise-mcp)

**课时（Sessions）**

- **Tue 9/29:** 高级提示 + Agent 开发框架（RePPIT、规格驱动开发） — [幻灯片](https://docs.google.com/presentation/d/17brqoQQZHF3K82WgYaV6urAV3Q7iIwyGUBYRvSuY8QY/edit?usp=sharing) · [讲稿记录](https://themodernsoftware.dev/materials/9-29-26-transcript.txt)
- **Thu 10/1:** MCP 与工具调用全解（理论、搭建与进阶工具设计） — [幻灯片](https://docs.google.com/presentation/d/1q2cB1a7P4XsR0UJqE0RmtZFeggNOLdPaSnOpbBVewHA/edit?usp=sharing) · [Skills 材料](https://drive.google.com/drive/folders/1aEHCXzZKkokuA4AYjD_2i6OrcM5iQosW?usp=drive_link) · [讲稿记录](https://themodernsoftware.dev/materials/10-1-26-transcript.txt)

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

- **Tue 10/6:** Agent Skills 全解（含 web skills） — [幻灯片](https://docs.google.com/presentation/d/15bPu5c-i8D8McTh6l7SpUPk2n9M_Y-CdDQLfyzL8RD8/edit?usp=sharing)
- **Thu 10/8:** [嘉宾：Lee Robinson（Model Behavior @ SpaceX）](https://leerob.com) — [幻灯片](https://drive.google.com/file/d/1b8WiBk_lcB3ue-jZMLijSUMLj6SDiF6Z/view?usp=drive_link)

### 第 4 周：定制 Agent 与仓库

**主题（Topics）**

- CLAUDE.md 与 AGENTS.md：各自放什么
- 用于 lint 门禁、测试运行与护栏的 Hooks
- 子 Agent 模式（planner / implementer / reviewer）

**阅读（Reading）**

- [I Still Prefer MCP Over Skills](https://david.coffee/i-still-prefer-mcp-over-skills)
- [AGENTS.md (Factory Docs)](https://docs.factory.com/harness/agents-md)
- [Steering Claude Code: Skills, Hooks, Rules, Subagents, and More](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more)
- [Writing a Good CLAUDE.md](https://hlyr.dev/blog/writing-a-good-claude-md)

**课时（Sessions）**

- **Tue 10/13:** 定制你的 Agent 配置（CLAUDE.md、AGENTS.md、hooks） — [幻灯片](https://docs.google.com/presentation/d/152VaUifBKH4T6hxd6fCKKM9kJTSAuBmkF8zSYwuTYAo/edit?usp=sharing)
- **Thu 10/15:** [嘉宾：Boris Cherny（Claude Code 创建者 @ Anthropic）](https://borischerny.com)

### 第 5 周：Agent 友好的代码库

**主题（Topics）**

- 怎样的仓库才算 Agent-ready：结构、文档、测试与检查
- 就绪度评分与审计
- 真实仓库里阻碍 Agent 的常见缺口

**阅读（Reading）**

- [Making Codebases Agent Ready](https://www.youtube.com/watch?v=ShuJ_CN6zr4)
- [Making Ergonomic Repositories](https://x.com/trybasis/status/2056881705269580023)

**课时（Sessions）**

- **Tue 10/20:** 仓库的 Agent 就绪度（结构、文档与检查项） — [幻灯片](https://docs.google.com/presentation/d/1yCxocmUrGIN7IrC42WB6NW08PtYYFLe1ombDj3Ay6_8/edit?usp=drive_link)
- **Thu 10/22:** [嘉宾：Eno Reyes（CTO @ Factory）](https://www.linkedin.com/in/enoreyes)

### 第 6 周：Agent 驱动的代码审查

**主题（Topics）**

- AI 审查擅长发现什么、容易漏掉什么
- 审查架构与自定义规则
- 把 AI 审查嵌入团队的 PR 流程

**课时（Sessions）**

- **Tue 10/27:** Agent 驱动的代码审查：最佳实践与架构
- **Thu 10/29:** [嘉宾：Silas Alberti（SVP Research @ Cognition）](https://sil.as)

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
