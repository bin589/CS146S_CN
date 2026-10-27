# Week 4 · 定制 Agent 与仓库（Fall 2026）

> 对应课程：**10/13（周二）** 定制 Agent 配置（CLAUDE.md、AGENTS.md、hooks）；**10/15（周四）** 嘉宾 Boris Cherny。
> 抓取时间：2026-10-27。原文版权归各作者／课程方所有。

幻灯片、嘉宾博客首页及中文译文的对照表见 [Fall 2026 课程资料索引](../README.md)。

## 阅读材料

| # | 主题 | 原文 | 英文存档 | 中文翻译 |
|---|---|---|---|---|
| 1 | 仍然更喜欢 MCP 而不是 Skills | [david.coffee](https://david.coffee/i-still-prefer-mcp-over-skills) | [en.md](./I%20Still%20Prefer%20MCP%20Over%20Skills%20en.md) | [zh.md](./I%20Still%20Prefer%20MCP%20Over%20Skills%20zh.md) |
| 2 | Factory 的 AGENTS.md 文档 | [docs.factory.com](https://docs.factory.com/harness/agents-md) | [en.md](./Factory%20AGENTS.md%20en.md) | [zh.md](./Factory%20AGENTS.md%20zh.md) |
| 3 | 驾驭 Claude Code | [claude.com](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more) | [en.md](./Steering%20Claude%20Code%20en.md) | [zh.md](./Steering%20Claude%20Code%20zh.md) |
| 4 | 写好一份 CLAUDE.md | [hlyr.dev](https://hlyr.dev/blog/writing-a-good-claude-md) | [en.md](./Writing%20a%20Good%20CLAUDE.md%20en.md) | [zh.md](./Writing%20a%20Good%20CLAUDE.md%20zh.md) |

## 各篇要点

1. **MCP Over Skills** — 纯知识型 skill 有用；靠 CLI 才能做事的 skill 在网页客户端里不可用。远程 MCP 负责零安装、更新、OAuth、沙箱和可移植。作者希望的组合是：MCP 做连接器，skill 做连接器的说明书。
2. **Factory AGENTS.md** — 根文件放命令、仓库地图、约定和完成前必须跑的检查；长流程改放 skill。Droid 同时兼容 `CLAUDE.md` 等文件名，但不要为每个名字复制一份。嵌套文件只写真正的差异。初始加载上限 80,000 字符，动态发现 40,000 字符，都是上限不是目标。
3. **Steering Claude Code** — 七种指令面按“何时加载、压缩后还在不在、上下文成本、权威”区分。始终为真的事实放根 `CLAUDE.md`（建议 200 行内）；路径相关的约束放 rules；流程放 skills；旁路任务放 subagents；必须发生或必须禁止的事放 hooks，而不是写进提示词。
4. **Writing a Good CLAUDE.md** — 文件会进入每一次会话，所以只放普遍适用的 WHY / WHAT / HOW。前沿思考模型大约能稳定遵循 150–200 条指令，Claude Code 系统提示本身已约占 50 条。少于 300 行；渐进式披露；不要用 LLM 当 linter；不要用 `/init` 自动生成。

## 没有收录的内容

- 10/13、10/15 的课堂转写在 `themodernsoftware.dev/materials/` 对应路径上返回 404，课程首页也没有替代链接。
- Boris Cherny 的博客只收了首页索引，没有下载各篇文章正文。
