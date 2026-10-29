# 《现代软件开发者》第 6 讲：定制你的 Agent 配置

> **非官方中文翻译**，仅供学习参考，不代表原作者或斯坦福大学。
> 源幻灯片：[`1013-agent-config en.pptx`](./1013-agent-config%20en.pptx)
> 抓取日期：2026-10-27
> 说明：按原 pptx 逐页全文翻译，保留原始 URL、代码、专名与时间戳；内嵌图片提取到 [`images/1013/`](images/1013/)，图中英文在图片下方给出中文对照。代码与命令保持原文，不执行。

## 第 1 页：现代软件开发者

**现代软件开发者**

CS146S

斯坦福大学，2026 年秋季

Mihail Eric

themodernsoftware.dev

## 第 2 页：课程事务

**课程事务**

- 项目技术规格周四截止。
- 第一次开源贡献周日截止。
- 客座讲座改在 STLC 111（此后所有周四课都在这里）。
- Boris Cherny

![嘉宾照片](images/1013/slide02-01.png)

图中说明：一张人物照片，放在 “Boris Cherny” 条目旁。图中没有文字。

## 第 3 页：API、MCP 与 Skills

**API vs MCP vs Skills**

**API**

- 是什么：应用暴露给开发者调用的 HTTP/REST/GraphQL 服务接口。
- 谁来用：你自己调用，或通过 SDK。
- 用法：认证、重试、分页、输入校验等都由你决定。

**MCP**

- 是什么：由服务器暴露的工具定义，让 LLM agent 能以标准化方式调用它们。
- 谁来用：模型／agent 运行时（以 “tool calls” 的形式），而不是每次都由人类开发者写一套专门的集成。
- 用法：与外部资源、数据、服务交互的主要机制。

**Skills**

- 是什么：可复用的任务包／流程，教 agent 如何完成一项工作，通常会编排多个工具或端点。
- 谁来用：agent 或 agent 框架，把它当作可以伸手去用的更高层能力。
- 用法：工作流抽象——“完成 X 的可重复做法在这里。”

## 第 4 页：MCP 的额外好处

**MCP 的额外好处**

- 认证无缝衔接。
- 版本与更新都很容易。
- 可以在不同客户端之间迁移。
- 远程 MCP 的能力自带沙箱。

## 第 5 页：定制你的 Agent 配置

**定制你的 Agent 配置**

> **演讲者备注**：这就引出了我们这门课……

## 第 6 页：为什么

**为什么**

- 要把编码 agent 的生产力拉到最高，你得自己掌控整套技术栈。
- 可供定制的机制有很多。

## 第 7 页：定制 agent 的几种手法

**定制 agent 的手法**

- Agent 行为文件（`Claude.md` / `AGENTS.md`）
- Hooks
- Skills
- Subagents（子 agent）

> **演讲者备注**：看看这些东西在真实环境里的例子。

## 第 8 页：设计一份好用的 AGENTS.md

**设计一份最优的 AGENTS.md**

- 给 agent 看的 README。

**结构**

- 项目概览（代码库地图）。
- 构建与测试命令（用 maven，不要用 gradle）。
- 代码风格指南。
- 测试说明。
- 安全方面的考虑。
- 语言或技术栈特有的坑（React 18 + TypeScript、Vite，**不是** React）。

**写法**

- 让指令尽可能普遍适用。
- 避免贴代码片段，它们很快就会过时。
- 注意篇幅（少于 300 行）。
- 大型仓库应使用嵌套配置文件，根目录的 `AGENTS.md` 充当路由器。
  - 例如：关于 API gateway 设计的更多细节，请参阅 `docs/API-GATEWAY.md`。

> **演讲者备注**：同样的原则也适用于 `CLAUDE.md` 等文件。示例：<https://github.com/vercel/next.js/blob/canary/AGENTS.md>。关于加载顺序：`CLAUDE.md` 按从根目录到最近的 `.md` 文件依次处理，这样与当前工作最直接相关的指令会最后进入 LLM。自定义服务或团队目录会有不同的约定。

## 第 9 页：Hooks

**Hooks**

确定性脚本，在预定义的事件类型上运行。

- `PreToolUse`
- `PostToolUse`
- `UserPromptSubmit`
- `PreCompact`
- ……以及更多

**用例**

- 清洗用户提示。
- 拦截敏感操作。
- 对生成的代码运行 linter／formatter。
- 任务完成后运行测试。

> **演讲者备注**：Claude Code / Cursor 都支持。示例：<https://x.com/bcherny/status/2007179852047335529?s=20>。讲一讲 ponytail hooks。

## 第 10 页：Skills

**Skills**

把常用提示写成文件，让 agent 可以执行。

**用例**

- 跑测试
- 制定计划
- 做调研
- 审查代码
- 核验输出

> **演讲者备注**：给一个样例。Claude Code 里的 ship-it 命令。展示 Cursor 的 “deslop” 命令。

## 第 11 页：Subagents

**Subagents**

运行时委托。子 agent 的目的是：

- 把不同工作流的上下文干净地分开。
- 只把最终消息返回来。
- 名称、描述、工具列表在会话开始时加载。
- 可以隐式或显式调用。
- 把最常见的工作流自动化。

**用例**

- 探索／理解你的代码库。
- 改完代码后做简化。
- 端到端测试你的应用。
- 特别适合旁路任务。

> **演讲者备注**：对比 `Claude.md` 一类文件，那些更偏向锚定行为。示例：<https://x.com/bcherny/status/2007179850139000872?s=20>

## 第 12 页：MCP 服务器

**MCP 服务器**

**用例**

- 产品管理软件
  - Jira / Linear
  - 创建并更新 issue
  - 拉取 issue 信息并开工
- 文档软件
  - Notion / Confluence
  - 根据功能规格创建 issue
- 可观测性
  - Datadog / Sentry
  - 实时的生产环境调试
- 数据库
  - Redshift
  - 排查数据问题
  - 弄清数据是怎么组织的
- 技术文档
  - Context7
  - 永远不要用过期的库定义
  - 降低幻觉的可能性
- 实验跟踪
  - Arize
  - 拿一次测试运行的输出，用来建议新的实验运行

## 第 13 页：上下文的故事

**上下文的故事**

幻灯片上的标注块：

- System Prompt
- `Memory.md`
- Env info（环境信息）
- MCP tools
- Skills
- `AGENTS.md`（全局）
- `AGENTS.md`（局部）

## 第 14 页：提问

**提问**
