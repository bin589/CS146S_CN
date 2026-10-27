# Week 2 · 高级 Context Engineering（Fall 2026）

> 对应课程：**9/29（周二）** 高级 prompting + Agentic 开发框架（RePPIT、spec-driven development）；**10/1（周四）** MCP 与 tool calling 全面介绍。
> 抓取时间：2026-10-22。原文版权归各作者/机构所有。

## 课程安排资料

9/29 与 10/1 的幻灯片、课堂转写、Skills 文件及各自完整中文译文，见 [Fall 2026 前三周课程资料索引](../README.md)。以下为此前整理的阅读材料，继续保留。

## 阅读材料

| # | 主题 | 原文 | 英文存档 | 中文翻译 |
|---|---|---|---|---|
| 1 | 上下文税：何时压缩上下文 | [langwatch.ai](https://langwatch.ai/blog/context-tax-when-to-compact) | [Context Tax en.md](./Context%20Tax%20en.md) | [Context Tax zh.md](./Context%20Tax%20zh.md) |
| 2 | OpenSpec：轻量 spec 框架 | [openspec.dev](https://openspec.dev/) | [OpenSpec en.md](./OpenSpec%20en.md) | [OpenSpec zh.md](./OpenSpec%20zh.md) |
| 3 | Superpowers：agent 开发方法论 | [github.com/obra/superpowers](https://github.com/obra/superpowers) | [Superpowers en.md](./Superpowers%20en.md) | [Superpowers zh.md](./Superpowers%20zh.md) |
| 4 | 企业级 MCP 参考架构（Cloudflare） | [blog.cloudflare.com](https://blog.cloudflare.com/enterprise-mcp) | [Enterprise MCP en.md](./Enterprise%20MCP%20en.md) | [Enterprise MCP zh.md](./Enterprise%20MCP%20zh.md) |

## 各篇要点

1. **Context Tax** — 上下文成本是幂律（每翻倍约 6 倍），窗口从 50k 涨到 600k 时实际在用部分几乎不变（47.5% → 2.5%）；压缩甜点约 220k–250k，构建/代码理解可到 300k–450k；压缩后 5 步内纠正率 41.9%（基线 17.7%），且持续 30+ 步。保留 30k–60k 逐字尾部比 4.4k 摘要更划算。
2. **OpenSpec** — Explore → Propose → Review → Apply → Archive 五步闭环；产物 `proposal.md` / `specs/<capability>/spec.md` / `design.md` / `tasks.md`；delta spec 用 ADDED/MODIFIED/REMOVED/RENAMED，场景必须四个 `####`；实现前先评审 specs，实现时用干净上下文。
3. **Superpowers** — brainstorming → worktree → writing-plans → subagent-driven-development/executing-plans → TDD → code review → finish branch；skills 自动触发、强制而非建议；理念是 TDD、系统化、降低复杂度、证据优先。
4. **Enterprise MCP** — 远程 MCP server + Cloudflare Access（OAuth/SSO/MFA）+ MCP server portals（集中发现、DLP、按组按工具授权）+ Code Mode（52 工具 9.4k tokens → 2 工具 600 tokens，降 94%）+ AI Gateway（成本/模型路由）+ Gateway 检测 Shadow MCP（JSON-RPC `"method"` 正则）。

## 阅读材料目录

```text
week2/
├── Context Tax en.md / Context Tax zh.md
├── OpenSpec en.md / OpenSpec zh.md
├── Superpowers en.md / Superpowers zh.md
├── Enterprise MCP en.md / Enterprise MCP zh.md
└── images/       文章配图（PNG）
```
