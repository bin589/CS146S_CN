# Week 6 · Agent 驱动的代码审查（Fall 2026）

> 对应课程：**10/27（周二）** Agentic code review：最佳实践与架构；**10/29（周四）** 嘉宾 Silas Alberti（Chief Research Officer @ Cognition）。
> 抓取时间：2026-10-29。原文版权归各作者／课程方所有。

幻灯片、嘉宾个人主页及中文译文的对照表见 [Fall 2026 课程资料索引](../README.md)。

## 参考资料

> 与 PPT 重叠的篇目只存放在 `PPT引用外链/`，本表直接链过去。

| # | 主题 | 原文 | 英文存档 | 中文翻译 |
|---|---|---|---|---|
| 1 | 分层代码审查与按风险的人类把关 | [x.com/addyosmani](https://x.com/addyosmani/status/2114604912520921136) | [en.md](./PPT引用外链/Layered%20Code%20Review%20and%20Risk-Based%20Human%20Oversight%20en.md) | [zh.md](./PPT引用外链/分层代码审查与按风险的人类把关.md) |
| 2 | 大规模协调专项审查 Agent | [blog.cloudflare.com](https://blog.cloudflare.com/ai-code-review) | [en.md](./参考资料/Coordinating%20Specialist%20Review%20Agents%20at%20Scale%20en.md) | [zh.md](./参考资料/大规模协调专项审查Agent.md) |
| 3 | 超越 Diff：上下文、测试与模型选择 | [greptile.com](https://greptile.com/blog/how-to-build-a-code-review-agent) | [en.md](./PPT引用外链/Beyond%20the%20Diff%20Context%20Testing%20and%20Model%20Selection%20en.md) | [zh.md](./PPT引用外链/超越Diff：上下文测试与模型选择.md) |

## 各篇要点

1. **Layered Code Review…（Addy Osmani / Claude Code 团队）** — X Article 实际标题为 *How the Claude Code team does code review*。六层检查 + 快速回滚；人类时间双边成本；按风险缩放批准；用事故作评测；审查必须收敛。帖子页面本身几乎没有正文；文章文字来自同一 status 的公开 FxTwitter 聚合。附图未下载。
2. **Coordinating Specialist Review Agents…（Cloudflare）** — 围绕 OpenCode 的 CI 原生编排：最多七个专项审查者 + 协调者去重与定级；风险分档（trivial / lite / full）；断路器与模型 failback；30 天内约 13 万次审查运行、中位时长约 3m39s、break glass 约 0.6%。图未下载。
3. **Beyond the Diff…（Greptile / Daksh Gupta）** — 自建审查 agent 的五步改进：提示词、model inversion、代码库上下文（MCP + indexer）、自主测试（computer use）、按子任务选便宜模型。改编自 AIE NYC 2026 演讲。

## 没有收录的内容

- 10/27、10/29 的课堂转写在 `themodernsoftware.dev/materials/` 对应路径（`10-27-26-transcript.txt`、`10-29-26-transcript.txt` 及邻近命名）上返回 404。
- Silas Alberti 的个人站只收了公开主页可读文本与 HTML 快照，不应当作嘉宾课堂讲义；未递归下载项目页。大纲职称 **Chief Research Officer @ Cognition** 以课程首页 JS 为准（幻灯片第 2 页同此）；公开主页正文未重复写出该职称，归档不把页外信息回填进主页文本。

## PPT 引用外链归档

> 抓取时间：2026-11-02。仅归档 week1–6 **PPTX** 超链接／讲者备注中的外链（英文存档 + 中文整理）；**不含** `深入剖析 Claude Code en.pdf` 文献表。YouTube 只记元数据；GitHub 不整库克隆；产品首页为可读快照。

| 主题 | 原文 URL | 英文存档 | 中文版 | 来自哪份 PPT |
|---|---|---|---|---|
| 代码审查要点-Blake-Smith | [blakesmith.me/2015/02/09/code-review-essentials-for-software](https://blakesmith.me/2015/02/09/code-review-essentials-for-software-teams.html) | [Code Review Essentials Blake Smith en.md](./PPT引用外链/Code%20Review%20Essentials%20Blake%20Smith%20en.md) | [代码审查要点-Blake-Smith.md](./PPT引用外链/代码审查要点-Blake-Smith.md) | `1027-agentic-code-review` |
| Cloudflare内部AI工程栈 | [blog.cloudflare.com/internal-ai-engineering-stack/](https://blog.cloudflare.com/internal-ai-engineering-stack/) | [Cloudflare Internal AI Engineering Stack en.md](./PPT引用外链/Cloudflare%20Internal%20AI%20Engineering%20Stack%20en.md) | [Cloudflare内部AI工程栈.md](./PPT引用外链/Cloudflare内部AI工程栈.md) | `1027-agentic-code-review` |
| vercel-labs-deepsec仓库 | [github.com/vercel-labs/deepsec](https://github.com/vercel-labs/deepsec) | [vercel-labs-deepsec仓库 en.md](./PPT引用外链/vercel-labs-deepsec仓库%20en.md) | [vercel-labs-deepsec仓库.md](./PPT引用外链/vercel-labs-deepsec仓库.md) | `1027-agentic-code-review` |
| Semgrep官网 | [semgrep.dev/](https://semgrep.dev/) | [Semgrep homepage en.md](./PPT引用外链/Semgrep%20homepage%20en.md) | [Semgrep官网.md](./PPT引用外链/Semgrep官网.md) | `1027-agentic-code-review` |
| Augment-Cosmos代码审查 | [www.augmentcode.com/blog/solving-code-review-with-cosmos](https://www.augmentcode.com/blog/solving-code-review-with-cosmos) | [Augment Cosmos code review en.md](./PPT引用外链/Augment%20Cosmos%20code%20review%20en.md) | [Augment-Cosmos代码审查.md](./PPT引用外链/Augment-Cosmos代码审查.md) | `1027-agentic-code-review` |
| 超越Diff：上下文测试与模型选择（已有阅读材料） | [www.greptile.com/blog/how-to-build-a-code-review-agent](https://www.greptile.com/blog/how-to-build-a-code-review-agent) | [Beyond the Diff Context Testing and Model Selection en.md](./PPT引用外链/Beyond%20the%20Diff%20Context%20Testing%20and%20Model%20Selection%20en.md) | [超越Diff：上下文测试与模型选择.md](./PPT引用外链/超越Diff：上下文测试与模型选择.md) | `1027-agentic-code-review` |
| Wiz官网 | [www.wiz.io/](https://www.wiz.io/) | [Wiz homepage en.md](./PPT引用外链/Wiz%20homepage%20en.md) | [Wiz官网.md](./PPT引用外链/Wiz官网.md) | `1027-agentic-code-review` |
| 分层代码审查与按风险的人类把关（已有阅读材料） | [x.com/addyosmani/status/2114604912520921136?s=43](https://x.com/addyosmani/status/2114604912520921136?s=43) | [Layered Code Review and Risk-Based Human Oversight en.md](./PPT引用外链/Layered%20Code%20Review%20and%20Risk-Based%20Human%20Oversight%20en.md) | [分层代码审查与按风险的人类把关.md](./PPT引用外链/分层代码审查与按风险的人类把关.md) | `1027-agentic-code-review` |
