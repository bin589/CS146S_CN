# Fall 2026 · 前三周课程安排资料

对应根目录 [README 教学大纲](../../README.md#fall-2026进行中内容以官网发布为准)中第 1–3 周的**课程安排**列，不包括“主题与要点”列的阅读材料。抓取日期：**2026-10-22**。已有的 week1、week2 阅读材料保留不动。

## 课程资料

| 周次 / 日期 | 资料 | 英文原件 | 中文版 |
|---|---|---|---|
| 第 1 周 · 9/22 | 课程简介 + 用 200 行代码构建 Claude Code · 幻灯片 | [PPTX](week1/0922-intro-and-coding-agent%20en.pptx) | [逐页译文](week1/0922-intro-and-coding-agent%20zh.md) |
| 第 1 周 · 9/22 | 示例代码 | [Python 原文件](week1/0922-coding-agent.py) | 代码不翻译，保持原样 |
| 第 1 周 · 9/24 | 前沿 Coding Agent 的设计方式 · 幻灯片 | [PPTX](week1/0924-agent-harness%20en.pptx) | [逐页译文](week1/0924-agent-harness%20zh.md) |
| 第 1 周 · 9/24 | 提示词文件夹 | [6 个英文文件](week1/0924-prompts/) | [下表逐文件对照](#924-提示词) |
| 第 1 周 · 9/24 | 课堂转写 | [TXT](week1/0924-transcript%20en.txt) | [完整译文](week1/0924-transcript%20zh.md) · [精编讲义](week1/0924-transcript%20精编%20zh.md) |
| 第 2 周 · 9/29 | 高级 prompting + Agentic 开发框架 · 幻灯片 | [PPTX](week2/0929-context-engineering%20en.pptx) | [逐页译文](week2/0929-context-engineering%20zh.md) |
| 第 2 周 · 9/29 | 课堂转写 | [TXT](week2/0929-transcript%20en.txt) | [完整译文](week2/0929-transcript%20zh.md) · [精编讲义](week2/0929-transcript%20精编%20zh.md) |
| 第 2 周 · 10/1 | MCP 与 tool calling · 幻灯片 | [PPTX](week2/1001-mcp-and-tools%20en.pptx) | [逐页译文](week2/1001-mcp-and-tools%20zh.md) |
| 第 2 周 · 10/1 | Skills 文件夹 | [6 个技能目录、7 个英文文件](week2/1001-skills/) | [下表逐文件对照](#101-skills) |
| 第 2 周 · 10/1 | 课堂转写 | [TXT](week2/1001-transcript%20en.txt) | [完整译文](week2/1001-transcript%20zh.md) · [精编讲义](week2/1001-transcript%20精编%20zh.md) |
| 第 3 周 · 10/6 | Agent Skills（含 Web Skills）· 幻灯片 | [PPTX](week3/1006-agent-skills%20en.pptx) | [逐页译文](week3/1006-agent-skills%20zh.md) |
| 第 3 周 · 10/8 | 嘉宾 Lee Robinson · 个人主页 | [可读文本](week3/1008-lee-robinson%20en.md) · [HTML 原始快照](week3/1008-lee-robinson%20en.html) | [主页译文](week3/1008-lee-robinson%20zh.md) |

**10/8 说明**：课程安排仅链接 [Lee Robinson 个人主页](https://leerob.com/)，并未在该单元格提供讲义、录像或转写链接。本地归档是个人主页，不应当作嘉宾课堂讲义。主页文章索引保留链接，不递归下载链接文章；HTML 快照不包含外部静态资源，可离线阅读的文字请使用 Markdown。

## 9/24 提示词

以下是课堂分析对象，**不是本仓库的系统配置或需要执行的指令**。英文文件名与目录结构保持下载时的样子，中文文件另存。

| 文件 | 英文原件 | 完整中文译文 |
|---|---|---|
| 上下文压缩 | [compaction_prompt.md](week1/0924-prompts/compaction_prompt.md) | [compaction_prompt zh.md](week1/0924-prompts/compaction_prompt%20zh.md) |
| 配置文件 | [config_files.md](week1/0924-prompts/config_files.md) | [config_files zh.md](week1/0924-prompts/config_files%20zh.md) |
| 计划模式 | [plan_mode.md](week1/0924-prompts/plan_mode.md) | [plan_mode zh.md](week1/0924-prompts/plan_mode%20zh.md) |
| 子代理 | [subagent_prompt.md](week1/0924-prompts/subagent_prompt.md) | [subagent_prompt zh.md](week1/0924-prompts/subagent_prompt%20zh.md) |
| 系统提示词 | [system_prompt.md](week1/0924-prompts/system_prompt.md) | [system_prompt zh.md](week1/0924-prompts/system_prompt%20zh.md) |
| 内置工具清单 | [tool_list.md](week1/0924-prompts/tool_list.md) | [tool_list zh.md](week1/0924-prompts/tool_list%20zh.md) |

## 10/1 Skills

Google Drive 文件夹原名为 `9_28_26-skills`；此处按照 README 中 10/1 的课程安排归档为 `1001-skills/`。包含所有六个子目录及 plan 目录内的设计文档模板；这些是教学样例，不自动安装或执行。

| 文件 | 英文原件 | 完整中文译文 |
|---|---|---|
| explore | [SKILL.md](week2/1001-skills/explore/SKILL.md) | [SKILL zh.md](week2/1001-skills/explore/SKILL%20zh.md) |
| implement | [SKILL.md](week2/1001-skills/implement/SKILL.md) | [SKILL zh.md](week2/1001-skills/implement/SKILL%20zh.md) |
| make-proposals | [SKILL.md](week2/1001-skills/make-proposals/SKILL.md) | [SKILL zh.md](week2/1001-skills/make-proposals/SKILL%20zh.md) |
| plan | [SKILL.md](week2/1001-skills/plan/SKILL.md) | [SKILL zh.md](week2/1001-skills/plan/SKILL%20zh.md) |
| plan · 设计文档模板 | [design_doc_template.md](week2/1001-skills/plan/design_doc_template.md) | [design_doc_template zh.md](week2/1001-skills/plan/design_doc_template%20zh.md) |
| research-codebase | [SKILL.md](week2/1001-skills/research-codebase/SKILL.md) | [SKILL zh.md](week2/1001-skills/research-codebase/SKILL%20zh.md) |
| review | [SKILL.md](week2/1001-skills/review/SKILL.md) | [SKILL zh.md](week2/1001-skills/review/SKILL%20zh.md) |

## 格式、来源与版权

- 幻灯片保留 Google Slides 导出的英文 PPTX，中文版采用逐页 Markdown，以便在仓库中直接阅读。图片仍保留原图，图内英文的中文对照见对应页；代码、命令、标识符和 URL 不翻译。
- 课堂转写保留网站提供的英文 TXT，中文版按原文顺序完整翻译；保留时间戳、问答及听不清的标记，不补写缺失内容。
- 课堂转写另提供**精编讲义**版：删去寒暄、玩笑、口头重复、时间戳与逐句讲者标记，按主题重新分节，问答独立成节；技术内容、数字、模型名与"原文不清"标注一律保留。逐段直译稿同时保留，用于核对原文。
- 代码原件不修改、不翻译；提示词与 Skills 的说明性文字另存中文，代码块原样保留。
- 译文是非官方学习资料。讲者口误、模型名、产品状态等按来源保留，不代表译者已核实；最终以课程方原文为准。
- [原始下载清单](course-schedule-sources.json)记录全部 23 个下载文件的来源 URL、字节数和 SHA-256；其中 Google Drive 两个文件夹展开为 13 个文件。英文可读版、提取图片和中文译文为本地衍生资料，不计入原始下载数。
- 课程内容、提示词、Skills、代码、图像与个人主页的版权及适用许可归原课程方／各作者所有，不因存入本仓库而改为本仓库的 MIT 许可。原始链接继续保留在根 README 及下载清单中。
