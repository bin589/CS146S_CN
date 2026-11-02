# Week 5 · Agent 友好的代码库（Fall 2026）

> 对应课程：**10/20（周二）** 仓库的 Agent 就绪度；**10/22（周四）** 嘉宾 Eno Reyes。
> 抓取时间：2026-10-27。原文版权归各作者／课程方所有。

幻灯片、LinkedIn 公开页及中文译文的对照表见 [Fall 2026 课程资料索引](../README.md)。

## 阅读材料

| # | 主题 | 原文 | 英文存档 | 中文翻译 |
|---|---|---|---|---|
| 1 | 让代码库为 Agent 做好准备 | [YouTube](https://www.youtube.com/watch?v=ShuJ_CN6zr4) | [元数据条目](./Making%20Codebases%20Agent%20Ready%20en.md) | [中文条目](./让代码库为Agent做好准备.md) |
| 2 | 让 Monorepo 对 Agent 更顺手 | [x.com/trybasis](https://x.com/trybasis/status/2056881705269580023) | [en.md](./Making%20Ergonomic%20Repositories%20en.md) | [zh.md](./让仓库对Agent更顺手.md) |

## 各篇要点

1. **Making Codebases Agent Ready** — Eno Reyes（Factory AI）2025-12-22 的演讲，15 分 33 秒。视频说明把瓶颈放在环境就绪而不是模型：快反馈、明确指令、可预测的环境。章节从 Software 2.0 / 验证不对称讲到 DevX 反馈飞轮。本地只存元数据和说明文字，没有视频文件，也没有逐句字幕。
2. **Making Ergonomic Repositories** — Basis 的 X Article。五条原则：权威性、就近、可验证、可互操作、默认不要。六层：根 `AGENTS.md`、嵌套 `AGENTS.md`、skills、sub-agent 角色、统一 MCP、测试。三个月内人均 token 用量超过 5 倍，提交速度 2.5 倍。帖子页面本身几乎没有正文；文章文字来自同一 status 的公开 FxTwitter 聚合。原文三张图未下载。

## 没有收录的内容

- 10/20、10/22 的课堂转写在 `themodernsoftware.dev/materials/` 对应路径上返回 404。
- LinkedIn 未登录页面不包含完整履历。公开页职位字段被打码；大纲中的 “CTO @ Factory” 没有写回那一栏。动态流里他人的转发和点赞留在 HTML 快照中，不当作讲稿。

## PPT 引用外链归档

> 抓取时间：2026-11-02。仅归档 week1–6 **PPTX** 超链接／讲者备注中的外链（英文存档 + 中文整理）；**不含** `深入剖析 Claude Code en.pdf` 文献表。YouTube 只记元数据；GitHub 不整库克隆；产品首页为可读快照。

| 主题 | 原文 URL | 英文存档 | 中文版 | 来自哪份 PPT |
|---|---|---|---|---|
| AGENTS-md规范站点 | [agents.md](http://agents.md) | [AGENTS-md规范站点 en.md](../week1/PPT引用外链/AGENTS-md规范站点%20en.md) | [AGENTS-md规范站点.md](../week1/PPT引用外链/AGENTS-md规范站点.md) | `1020-agent-readiness` |
| Factory对Next.js的就绪度演示 | [app.factory.ai/analytics/readiness/https%253A%252F%252Fgithu](https://app.factory.ai/analytics/readiness/https%253A%252F%252Fgithub.com%252Fvercel%252Fnext.js) | [Factory Next.js readiness demo en.md](./PPT引用外链/Factory%20Next.js%20readiness%20demo%20en.md) | [Factory对Next.js的就绪度演示.md](./PPT引用外链/Factory对Next.js的就绪度演示.md) | `1020-agent-readiness` |
| Claude-Code-Agent团队 | [code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams) | [Claude Code Agent Teams en.md](./PPT引用外链/Claude%20Code%20Agent%20Teams%20en.md) | [Claude-Code-Agent团队.md](./PPT引用外链/Claude-Code-Agent团队.md) | `1020-agent-readiness` |
| Claude-Code网页版 | [code.claude.com/docs/en/claude-code-on-the-web](https://code.claude.com/docs/en/claude-code-on-the-web) | [Claude Code on the Web en.md](./PPT引用外链/Claude%20Code%20on%20the%20Web%20en.md) | [Claude-Code网页版.md](./PPT引用外链/Claude-Code网页版.md) | `1020-agent-readiness` |
| Claude-Code-GitHub-Actions | [code.claude.com/docs/en/github-actions](https://code.claude.com/docs/en/github-actions) | [Claude Code GitHub Actions en.md](./PPT引用外链/Claude%20Code%20GitHub%20Actions%20en.md) | [Claude-Code-GitHub-Actions.md](./PPT引用外链/Claude-Code-GitHub-Actions.md) | `1020-agent-readiness` |
| Claude-Code与Slack | [code.claude.com/docs/en/slack](https://code.claude.com/docs/en/slack) | [Claude Code in Slack en.md](./PPT引用外链/Claude%20Code%20in%20Slack%20en.md) | [Claude-Code与Slack.md](./PPT引用外链/Claude-Code与Slack.md) | `1020-agent-readiness` |
| Devin-Review博客 | [cognition.ai/blog/devin-review](https://cognition.ai/blog/devin-review) | [Devin Review Cognition blog en.md](./PPT引用外链/Devin%20Review%20Cognition%20blog%20en.md) | [Devin-Review博客.md](./PPT引用外链/Devin-Review博客.md) | `1020-agent-readiness` |
| Cursor-Worktrees文档 | [cursor.com/docs/configuration/worktrees](https://cursor.com/docs/configuration/worktrees) | [Cursor Worktrees docs en.md](./PPT引用外链/Cursor%20Worktrees%20docs%20en.md) | [Cursor-Worktrees文档.md](./PPT引用外链/Cursor-Worktrees文档.md) | `1020-agent-readiness` |
| OpenAI-Codex-Cloud | [developers.openai.com/codex/cloud/](https://developers.openai.com/codex/cloud/) | [OpenAI Codex Cloud en.md](./PPT引用外链/OpenAI%20Codex%20Cloud%20en.md) | [OpenAI-Codex-Cloud.md](./PPT引用外链/OpenAI-Codex-Cloud.md) | `1020-agent-readiness` |
| OpenAI-Codex与Slack集成 | [developers.openai.com/codex/integrations/slack/](https://developers.openai.com/codex/integrations/slack/) | [OpenAI Codex Slack integration en.md](./PPT引用外链/OpenAI%20Codex%20Slack%20integration%20en.md) | [OpenAI-Codex与Slack集成.md](./PPT引用外链/OpenAI-Codex与Slack集成.md) | `1020-agent-readiness` |
| Devin官网 | [devin.ai/](https://devin.ai/) | [Devin homepage en.md](./PPT引用外链/Devin%20homepage%20en.md) | [Devin官网.md](./PPT引用外链/Devin官网.md) | `1020-agent-readiness` |
| Ramp自建后台Agent-Inspect | [engineering.ramp.com/post/why-we-built-our-background-agent](https://engineering.ramp.com/post/why-we-built-our-background-agent) | [Ramp Inspect background agent en.md](./PPT引用外链/Ramp%20Inspect%20background%20agent%20en.md) | [Ramp自建后台Agent-Inspect.md](./PPT引用外链/Ramp自建后台Agent-Inspect.md) | `1020-agent-readiness` |
| Factory-Agent就绪度报告页 | [factory.ai/agent-readiness](https://factory.ai/agent-readiness) | [Factory Agent Readiness Reports en.md](./PPT引用外链/Factory%20Agent%20Readiness%20Reports%20en.md) | [Factory-Agent就绪度报告页.md](./PPT引用外链/Factory-Agent就绪度报告页.md) | `1020-agent-readiness` |
| Factory-Agent就绪度新闻 | [factory.ai/news/agent-readiness](https://factory.ai/news/agent-readiness) | [Factory Agent Readiness news en.md](./PPT引用外链/Factory%20Agent%20Readiness%20news%20en.md) | [Factory-Agent就绪度新闻.md](./PPT引用外链/Factory-Agent就绪度新闻.md) | `1020-agent-readiness` |
| kodustech-agent-readiness仓库 | [github.com/kodustech/agent-readiness](https://github.com/kodustech/agent-readiness) | [kodustech-agent-readiness仓库 en.md](./PPT引用外链/kodustech-agent-readiness仓库%20en.md) | [kodustech-agent-readiness仓库.md](./PPT引用外链/kodustech-agent-readiness仓库.md) | `1020-agent-readiness` |
| Graphite官网 | [graphite.com/](https://graphite.com/) | [Graphite homepage en.md](./PPT引用外链/Graphite%20homepage%20en.md) | [Graphite官网.md](./PPT引用外链/Graphite官网.md) | `1020-agent-readiness` |
| Cyrus官网 | [www.atcyrus.com/](https://www.atcyrus.com/) | [Cyrus homepage en.md](./PPT引用外链/Cyrus%20homepage%20en.md) | [Cyrus官网.md](./PPT引用外链/Cyrus官网.md) | `1020-agent-readiness` |
| Conductor官网 | [www.conductor.build/](https://www.conductor.build/) | [Conductor homepage en.md](./PPT引用外链/Conductor%20homepage%20en.md) | [Conductor官网.md](./PPT引用外链/Conductor官网.md) | `1020-agent-readiness` |
| Alvin-Sng关于Factory-CI的帖子 | [x.com/alvinsng/status/2030056110317818206?s=20](https://x.com/alvinsng/status/2030056110317818206?s=20) | [Alvin Sng Factory CI X post en.md](./PPT引用外链/Alvin%20Sng%20Factory%20CI%20X%20post%20en.md) | [Alvin-Sng关于Factory-CI的帖子.md](./PPT引用外链/Alvin-Sng关于Factory-CI的帖子.md) | `1020-agent-readiness` |
