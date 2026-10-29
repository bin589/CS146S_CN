# Week 6 · Agent 驱动的代码审查（Fall 2026）

> 对应课程：**10/27（周二）** Agentic code review：最佳实践与架构；**10/29（周四）** 嘉宾 Silas Alberti（Chief Research Officer @ Cognition）。
> 抓取时间：2026-10-29。原文版权归各作者／课程方所有。

幻灯片、嘉宾个人主页及中文译文的对照表见 [Fall 2026 课程资料索引](../README.md)。

## 阅读材料

| # | 主题 | 原文 | 英文存档 | 中文翻译 |
|---|---|---|---|---|
| 1 | 分层代码审查与按风险的人类把关 | [x.com/addyosmani](https://x.com/addyosmani/status/2114604912520921136) | [en.md](./Layered%20Code%20Review%20and%20Risk-Based%20Human%20Oversight%20en.md) | [zh.md](./分层代码审查与按风险的人类把关.md) |
| 2 | 大规模协调专项审查 Agent | [blog.cloudflare.com](https://blog.cloudflare.com/ai-code-review) | [en.md](./Coordinating%20Specialist%20Review%20Agents%20at%20Scale%20en.md) | [zh.md](./大规模协调专项审查Agent.md) |
| 3 | 超越 Diff：上下文、测试与模型选择 | [greptile.com](https://greptile.com/blog/how-to-build-a-code-review-agent) | [en.md](./Beyond%20the%20Diff%20Context%20Testing%20and%20Model%20Selection%20en.md) | [zh.md](./超越Diff：上下文测试与模型选择.md) |

## 各篇要点

1. **Layered Code Review…（Addy Osmani / Claude Code 团队）** — X Article 实际标题为 *How the Claude Code team does code review*。六层检查 + 快速回滚；人类时间双边成本；按风险缩放批准；用事故作评测；审查必须收敛。帖子页面本身几乎没有正文；文章文字来自同一 status 的公开 FxTwitter 聚合。附图未下载。
2. **Coordinating Specialist Review Agents…（Cloudflare）** — 围绕 OpenCode 的 CI 原生编排：最多七个专项审查者 + 协调者去重与定级；风险分档（trivial / lite / full）；断路器与模型 failback；30 天内约 13 万次审查运行、中位时长约 3m39s、break glass 约 0.6%。图未下载。
3. **Beyond the Diff…（Greptile / Daksh Gupta）** — 自建审查 agent 的五步改进：提示词、model inversion、代码库上下文（MCP + indexer）、自主测试（computer use）、按子任务选便宜模型。改编自 AIE NYC 2026 演讲。

## 没有收录的内容

- 10/27、10/29 的课堂转写在 `themodernsoftware.dev/materials/` 对应路径（`10-27-26-transcript.txt`、`10-29-26-transcript.txt` 及邻近命名）上返回 404。
- Silas Alberti 的个人站只收了公开主页可读文本与 HTML 快照，不应当作嘉宾课堂讲义；未递归下载项目页。大纲职称 **Chief Research Officer @ Cognition** 以课程首页 JS 为准（幻灯片第 2 页同此）；公开主页正文未重复写出该职称，归档不把页外信息回填进主页文本。
