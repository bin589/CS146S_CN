# Week 2 · 高级 Context Engineering（Fall 2026）

> 对应课程：**9/29（周二）** 高级 prompting + Agentic 开发框架（RePPIT、spec-driven development）；**10/1（周四）** MCP 与 tool calling 全面介绍。
> 抓取时间：2026-10-22。原文版权归各作者/机构所有。

## 课程安排资料

9/29 与 10/1 的幻灯片、课堂转写、Skills 文件及各自完整中文译文，见 [Fall 2026 前三周课程资料索引](../README.md)。以下为此前整理的阅读材料，继续保留。

## 参考资料

> 与 PPT 重叠的篇目只存放在 `PPT引用外链/`，本表直接链过去。

| # | 主题 | 原文 | 英文存档 | 中文翻译 |
|---|---|---|---|---|
| 1 | 上下文税：何时压缩上下文 | [langwatch.ai](https://langwatch.ai/blog/context-tax-when-to-compact) | [Context Tax en.md](./参考资料/Context%20Tax%20en.md) | [上下文税.md](./参考资料/上下文税.md) |
| 2 | OpenSpec：轻量 spec 框架 | [openspec.dev](https://openspec.dev/) | [OpenSpec en.md](./PPT引用外链/OpenSpec%20en.md) | [OpenSpec中文.md](./PPT引用外链/OpenSpec中文.md) |
| 3 | Superpowers：agent 开发方法论 | [github.com/obra/superpowers](https://github.com/obra/superpowers) | [Superpowers en.md](./PPT引用外链/Superpowers%20en.md) | [Superpowers中文.md](./PPT引用外链/Superpowers中文.md) |
| 4 | 企业级 MCP 参考架构（Cloudflare） | [blog.cloudflare.com](https://blog.cloudflare.com/enterprise-mcp) | [Enterprise MCP en.md](./参考资料/Enterprise%20MCP%20en.md) | [企业级MCP.md](./参考资料/企业级MCP.md) |

## 各篇要点

1. **Context Tax** — 上下文成本是幂律（每翻一倍大约变为 6 倍），窗口从 50k 涨到 600k 时实际在用部分几乎不变（47.5% → 2.5%）；压缩甜点约 220k–250k，构建/代码理解可到 300k–450k；压缩后 5 步内纠正率 41.9%（基线 17.7%），且持续 30+ 步。保留 30k–60k 逐字尾部比 4.4k 摘要更划算。
2. **OpenSpec** — Explore → Propose → Review → Apply → Archive 五步闭环；产物 `proposal.md` / `specs/<capability>/spec.md` / `design.md` / `tasks.md`；delta spec 用 ADDED/MODIFIED/REMOVED/RENAMED，场景必须四个 `####`；实现前先评审 specs，实现时用干净上下文。
3. **Superpowers** — brainstorming → worktree → writing-plans → subagent-driven-development/executing-plans → TDD → code review → finish branch；skills 自动触发、强制而非建议；理念是 TDD、系统化、降低复杂度、证据优先。
4. **Enterprise MCP** — 远程 MCP server + Cloudflare Access（OAuth/SSO/MFA）+ MCP server portals（集中发现、DLP、按组按工具授权）+ Code Mode（52 工具 9.4k tokens → 2 工具 600 tokens，降 94%）+ AI Gateway（成本/模型路由）+ Gateway 检测 Shadow MCP（JSON-RPC `"method"` 正则）。

## 参考资料目录

```text
week2/
├── 参考资料/Context Tax en.md / 上下文税.md
├── PPT引用外链/OpenSpec en.md / OpenSpec中文.md
├── PPT引用外链/Superpowers en.md / Superpowers中文.md
├── 参考资料/Enterprise MCP en.md / 企业级MCP.md
└── images/       文章配图（PNG）
```

## PPT 引用外链归档

> 抓取时间：2026-11-02。仅归档 week1–6 **PPTX** 超链接／讲者备注中的外链（英文存档 + 中文整理）；**不含** `深入剖析 Claude Code en.pdf` 文献表。YouTube 只记元数据；GitHub 不整库克隆；产品首页为可读快照。

| 主题 | 原文 URL | 英文存档 | 中文版 | 来自哪份 PPT |
|---|---|---|---|---|
| AGENTS-md规范站点 | [agents.md](http://agents.md) | [AGENTS-md规范站点 en.md](../week1/PPT引用外链/AGENTS-md规范站点%20en.md) | [AGENTS-md规范站点.md](../week1/PPT引用外链/AGENTS-md规范站点.md) | `0929-context-engineering` |
| Claude-md短链落地页 | [claude.md](http://claude.md) | [Claude-md短链落地页 en.md](../week1/PPT引用外链/Claude-md短链落地页%20en.md) | [Claude-md短链落地页.md](../week1/PPT引用外链/Claude-md短链落地页.md) | `0929-context-engineering` |
| OpenSpec中文（已有阅读材料） | [github.com/Fission-AI/OpenSpec/](https://github.com/Fission-AI/OpenSpec/) | [OpenSpec en.md](./PPT引用外链/OpenSpec%20en.md) | [OpenSpec中文.md](./PPT引用外链/OpenSpec中文.md) | `0929-context-engineering` |
| Superpowers中文（已有阅读材料） | [github.com/obra/superpowers](https://github.com/obra/superpowers) | [Superpowers en.md](./PPT引用外链/Superpowers%20en.md) | [Superpowers中文.md](./PPT引用外链/Superpowers中文.md) | `0929-context-engineering` |
| 禁止纯感觉：复杂代码库中的上下文工程 | [www.youtube.com/watch?v=rmvDxxNubIg](https://www.youtube.com/watch?v=rmvDxxNubIg) | [No Vibes Allowed Context Engineering en.md](./PPT引用外链/No%20Vibes%20Allowed%20Context%20Engineering%20en.md) | [禁止纯感觉：复杂代码库中的上下文工程.md](./PPT引用外链/禁止纯感觉：复杂代码库中的上下文工程.md) | `0929-context-engineering` |
| Skills-md规范站点 | [skills.md](http://skills.md) | [Skills-md规范站点 en.md](./PPT引用外链/Skills-md规范站点%20en.md) | [Skills-md规范站点.md](./PPT引用外链/Skills-md规范站点.md) | `1001-mcp-and-tools` |
| Agent-Skills概览 | [agentskills.io/home](https://agentskills.io/home) | [Agent Skills Overview en.md](./PPT引用外链/Agent%20Skills%20Overview%20en.md) | [Agent-Skills概览.md](./PPT引用外链/Agent-Skills概览.md) | `1001-mcp-and-tools` |
| anthropics-skills目录 | [github.com/anthropics/skills/tree/main/skills](https://github.com/anthropics/skills/tree/main/skills) | [anthropics-skills目录 en.md](./PPT引用外链/anthropics-skills目录%20en.md) | [anthropics-skills目录.md](./PPT引用外链/anthropics-skills目录.md) | `1001-mcp-and-tools` |
| mattpocock-skills仓库 | [github.com/mattpocock/skills](https://github.com/mattpocock/skills) | [mattpocock-skills仓库 en.md](./PPT引用外链/mattpocock-skills仓库%20en.md) | [mattpocock-skills仓库.md](./PPT引用外链/mattpocock-skills仓库.md) | `1001-mcp-and-tools` |
