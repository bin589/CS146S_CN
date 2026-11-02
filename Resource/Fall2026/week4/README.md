# Week 4 · 定制 Agent 与仓库（Fall 2026）

> 对应课程：**10/13（周二）** 定制 Agent 配置（CLAUDE.md、AGENTS.md、hooks）；**10/15（周四）** 嘉宾 Boris Cherny。
> 抓取时间：2026-10-27。原文版权归各作者／课程方所有。

幻灯片、嘉宾博客首页及中文译文的对照表见 [Fall 2026 课程资料索引](../README.md)。

## 阅读材料

| # | 主题 | 原文 | 英文存档 | 中文翻译 |
|---|---|---|---|---|
| 1 | 仍然更喜欢 MCP 而不是 Skills | [david.coffee](https://david.coffee/i-still-prefer-mcp-over-skills) | [en.md](./I%20Still%20Prefer%20MCP%20Over%20Skills%20en.md) | [zh.md](./仍然更喜欢MCP而不是Skills.md) |
| 2 | Factory 的 AGENTS.md 文档 | [docs.factory.com](https://docs.factory.com/harness/agents-md) | [en.md](./Factory%20AGENTS.md%20en.md) | [zh.md](./Factory的AGENTS-md.md) |
| 3 | 驾驭 Claude Code | [claude.com](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more) | [en.md](./Steering%20Claude%20Code%20en.md) | [zh.md](./驾驭Claude-Code.md) |
| 4 | 写好一份 CLAUDE.md | [hlyr.dev](https://hlyr.dev/blog/writing-a-good-claude-md) | [en.md](./Writing%20a%20Good%20CLAUDE.md%20en.md) | [zh.md](./写好一份CLAUDE-md.md) |

## 各篇要点

1. **MCP Over Skills** — 纯知识型 skill 有用；靠 CLI 才能做事的 skill 在网页客户端里不可用。远程 MCP 负责零安装、更新、OAuth、沙箱和可移植。作者希望的组合是：MCP 做连接器，skill 做连接器的说明书。
2. **Factory AGENTS.md** — 根文件放命令、仓库地图、约定和完成前必须跑的检查；长流程改放 skill。Droid 同时兼容 `CLAUDE.md` 等文件名，但不要为每个名字复制一份。嵌套文件只写真正的差异。初始加载上限 80,000 字符，动态发现 40,000 字符，都是上限不是目标。
3. **Steering Claude Code** — 七种指令面按“何时加载、压缩后还在不在、上下文成本、权威”区分。始终为真的事实放根 `CLAUDE.md`（建议 200 行内）；路径相关的约束放 rules；流程放 skills；旁路任务放 subagents；必须发生或必须禁止的事放 hooks，而不是写进提示词。
4. **Writing a Good CLAUDE.md** — 文件会进入每一次会话，所以只放普遍适用的 WHY / WHAT / HOW。前沿思考模型大约能稳定遵循 150–200 条指令，Claude Code 系统提示本身已约占 50 条。少于 300 行；渐进式披露；不要用 LLM 当 linter；不要用 `/init` 自动生成。

## 没有收录的内容

- 10/13、10/15 的课堂转写在 `themodernsoftware.dev/materials/` 对应路径上返回 404，课程首页也没有替代链接。
- Boris Cherny 的博客只收了首页索引，没有下载各篇文章正文。

## PPT 引用外链归档

> 抓取时间：2026-11-02。仅归档 week1–6 **PPTX** 超链接／讲者备注中的外链（英文存档 + 中文整理）；**不含** `深入剖析 Claude Code en.pdf` 文献表。YouTube 只记元数据；GitHub 不整库克隆；产品首页为可读快照。

| 主题 | 原文 URL | 英文存档 | 中文版 | 来自哪份 PPT |
|---|---|---|---|---|
| AGENTS-md规范站点 | [agents.md](http://agents.md) | [AGENTS-md规范站点 en.md](../week1/PPT引用外链/AGENTS-md规范站点%20en.md) | [AGENTS-md规范站点.md](../week1/PPT引用外链/AGENTS-md规范站点.md) | `1013-agent-config` |
| api-gateway-md短链说明 | [api-gateway.md](http://api-gateway.md) | [api-gateway-md短链说明 en.md](./PPT引用外链/api-gateway-md短链说明%20en.md) | [api-gateway-md短链说明.md](./PPT引用外链/api-gateway-md短链说明.md) | `1013-agent-config` |
| Claude-md短链落地页 | [claude.md](http://claude.md) | [Claude-md短链落地页 en.md](../week1/PPT引用外链/Claude-md短链落地页%20en.md) | [Claude-md短链落地页.md](../week1/PPT引用外链/Claude-md短链落地页.md) | `1013-agent-config` |
| Arize-Phoenix-MCP服务器 | [arize.com/docs/phoenix/integrations/phoenix-mcp-server](https://arize.com/docs/phoenix/integrations/phoenix-mcp-server) | [Arize Phoenix MCP Server en.md](./PPT引用外链/Arize%20Phoenix%20MCP%20Server%20en.md) | [Arize-Phoenix-MCP服务器.md](./PPT引用外链/Arize-Phoenix-MCP服务器.md) | `1013-agent-config` |
| AWS-Redshift-MCP服务器 | [awslabs.github.io/mcp/servers/redshift-mcp-server](https://awslabs.github.io/mcp/servers/redshift-mcp-server) | [AWS Redshift MCP Server en.md](./PPT引用外链/AWS%20Redshift%20MCP%20Server%20en.md) | [AWS-Redshift-MCP服务器.md](./PPT引用外链/AWS-Redshift-MCP服务器.md) | `1013-agent-config` |
| Notion-MCP | [developers.notion.com/guides/mcp/mcp](https://developers.notion.com/guides/mcp/mcp) | [Notion MCP en.md](./PPT引用外链/Notion%20MCP%20en.md) | [Notion-MCP.md](./PPT引用外链/Notion-MCP.md) | `1013-agent-config` |
| Datadog-Bits-AI-MCP服务器 | [docs.datadoghq.com/bits_ai/mcp_server/](https://docs.datadoghq.com/bits_ai/mcp_server/) | [Datadog Bits AI MCP Server en.md](./PPT引用外链/Datadog%20Bits%20AI%20MCP%20Server%20en.md) | [Datadog-Bits-AI-MCP服务器.md](./PPT引用外链/Datadog-Bits-AI-MCP服务器.md) | `1013-agent-config` |
| Sentry-MCP | [docs.sentry.io/product/sentry-mcp/](https://docs.sentry.io/product/sentry-mcp/) | [Sentry MCP en.md](./PPT引用外链/Sentry%20MCP%20en.md) | [Sentry-MCP.md](./PPT引用外链/Sentry-MCP.md) | `1013-agent-config` |
| upstash-context7仓库 | [github.com/upstash/context7](https://github.com/upstash/context7) | [upstash-context7仓库 en.md](./PPT引用外链/upstash-context7仓库%20en.md) | [upstash-context7仓库.md](./PPT引用外链/upstash-context7仓库.md) | `1013-agent-config` |
| next.js的AGENTS-md | [github.com/vercel/next.js/blob/canary/AGENTS.md](https://github.com/vercel/next.js/blob/canary/AGENTS.md) | [next.js AGENTS.md en.md](./PPT引用外链/next.js%20AGENTS.md%20en.md) | [next.js的AGENTS-md.md](./PPT引用外链/next.js的AGENTS-md.md) | `1013-agent-config` |
| Linear-MCP | [linear.app/docs/mcp](https://linear.app/docs/mcp) | [Linear MCP en.md](./PPT引用外链/Linear%20MCP%20en.md) | [Linear-MCP.md](./PPT引用外链/Linear-MCP.md) | `1013-agent-config` |
| Atlassian远程MCP服务器 | [www.atlassian.com/blog/announcements/remote-mcp-server](https://www.atlassian.com/blog/announcements/remote-mcp-server) | [Atlassian Remote MCP Server en.md](./PPT引用外链/Atlassian%20Remote%20MCP%20Server%20en.md) | [Atlassian远程MCP服务器.md](./PPT引用外链/Atlassian远程MCP服务器.md) | `1013-agent-config` |
| Boris-Cherny关于subagents的帖子 | [x.com/bcherny/status/2007179850139000872?s=20](https://x.com/bcherny/status/2007179850139000872?s=20) | [Boris Cherny subagents X post en.md](./PPT引用外链/Boris%20Cherny%20subagents%20X%20post%20en.md) | [Boris-Cherny关于subagents的帖子.md](./PPT引用外链/Boris-Cherny关于subagents的帖子.md) | `1013-agent-config` |
| Boris-Cherny关于PostToolUse钩子的帖子 | [x.com/bcherny/status/2007179852047335529?s=20](https://x.com/bcherny/status/2007179852047335529?s=20) | [Boris Cherny PostToolUse hook X post en.md](./PPT引用外链/Boris%20Cherny%20PostToolUse%20hook%20X%20post%20en.md) | [Boris-Cherny关于PostToolUse钩子的帖子.md](./PPT引用外链/Boris-Cherny关于PostToolUse钩子的帖子.md) | `1013-agent-config` |
