# 《现代软件开发者》第 4 讲：MCP、工具调用与更多

> **非官方中文翻译**，仅供学习参考，不代表原作者或斯坦福大学。
> 源幻灯片：[`1001-mcp-and-tools en.pptx`](./1001-mcp-and-tools%20en.pptx)
> 抓取日期：2026-10-22
> 说明：按原 pptx 逐页全文翻译，保留原始 URL、代码、专名与时间戳；内嵌图片提取到 [`images/1001/`](images/1001/)，图中英文在图片下方给出中文对照。代码与命令保持原文，不执行。

## 第 1 页：现代软件开发者

**现代软件开发者**

CS146S

斯坦福大学，2026 年秋季

Mihail Eric

themodernsoftware.dev

## 第 2 页：课程事务

**课程事务**

- 开源合作伙伴作业今晚发布。
  - “AI 垃圾代码”（AI slop）得 0 分。
- 项目提案今晚截止。
- Ashley Jepson（Factory）将带来一场工作坊。

## 第 3 页：MCP、工具调用与更多

**MCP、工具调用与更多**

> **演讲者备注**：这就引出了我们这门课……

## 第 4 页：为什么需要 MCP

**为什么**

- LLM 拥有广博（但静态）的世界知识，只有重新训练时才会更新。
- 要构建完全自主的系统，我们需要可靠的方式把动态数据喂给模型。

## 第 5 页：MCP

**MCP**

- **Model Context Protocol**（模型上下文协议）。
  - 一种开放协议，让各种系统能够以可跨集成泛化的方式，为 AI 模型提供上下文。
    - 用大白话说：一种把工具暴露给 LLM 的标准格式。

## 第 6 页：基础

**基础**

- **MCP**
  - 不再需要为每个 LLM 宿主/agent 到每个底层工具都构建 M×N 个连接器。
    - 不需要重复实现认证、错误处理、限流等。
    - 使用 JSON-RPC 强制统一输出格式。
  - 与工具集成的方式从 M×N 个连接器变为 M+N 个连接器。

## 第 7 页：原来的集成方式

![M×N 集成示意图（原始方式）](images/1001/slide07-01.png)
![模型/客户端标志](images/1001/slide07-02.png)
![API 图标](images/1001/slide07-03.png)
![API 文档截图](images/1001/slide07-04.png)
![API 图标](images/1001/slide07-05.png)
![API 图标](images/1001/slide07-06.png)
![LLM 通用模型标志](images/1001/slide07-07.png)
![LLM 标志](images/1001/slide07-08.png)
![LLM 标志](images/1001/slide07-09.png)

**Originally（最初）**

图中文字中文对照与结构说明：左侧是 3 个 LLM/客户端标志，右侧是 3 个 API/服务图标；原图中每个 LLM 都要单独连到每个 API，形成 3×3 = 9 条连接，这就是 M×N 集成问题。图中可辨识的英文只有 **LLM**（大语言模型）；其余为产品徽标，未包含可读文字。

右侧的几张代码/文档截图分别展示文档糟糕的 API 示例，用来说明“每接一个服务都要重新处理认证、字段、错误和限流”的痛苦：

- **Twitter API v2 示例**：函数名为 `poorly_documented_twitter_search`。注释列出的问题是：`query` 参数解释含糊；`tweet.fields` 的可选字段文档不完整；`max_results` 的合法范围没有说明或前后不一致；错误响应含糊、帮助不大。代码中写着 `# Parameters: poorly documented, often trial and error`（参数文档很差，往往只能反复试错）。
- **Facebook Graph API 示例**：函数名为 `poorly_documented_facebook_graph_api`。问题包括：`fields` 的含义模糊；端点经常变更且不向后兼容；权限（scope）与端点不匹配且缺少文档；错误信息晦涩，不说明如何修复。
- **SOAP API 示例**：函数名为 `poorly_documented_soap_call`。问题包括：没有 WSDL 时 SOAP body 结构不清楚，字段只能猜；命名空间是必需的但文档没解释；`SOAPAction` 头有时要求、有时不要求；错误通常只返回通用的 SOAP fault，没有可操作的细节。

> **演讲者备注**：每个 LLM 到每个 API 都需要单独的连接器。

## 第 8 页：使用 MCP 之后

![M+N 集成示意图（使用 MCP）](images/1001/slide08-01.png)
![模型/客户端标志](images/1001/slide08-02.png)
![API 图标](images/1001/slide08-03.png)
![API 文档截图](images/1001/slide08-04.png)
![API 图标](images/1001/slide08-05.png)
![API 图标](images/1001/slide08-06.png)
![LLM 通用模型标志](images/1001/slide08-07.png)
![LLM 标志](images/1001/slide08-08.png)
![LLM 标志](images/1001/slide08-09.png)

**Now with MCP（现在使用 MCP）**

图中文字中文对照：与上一页相同的 3 个 LLM/客户端和 3 个 API/服务，现在都连接到中间的 **MCP**（模型上下文协议）枢纽。连接方式变成每个 LLM 连一次 MCP、MCP 再连每个 API，总数从 M×N 降为 M+N。图中英文标签为 **MCP**（模型上下文协议）。

## 第 9 页：进一步理解 MCP

**进一步理解 MCP**

**术语**

- **Host（宿主）**：Cursor、Claude Desktop。
- **MCP Client（MCP 客户端）**：嵌入在宿主中的库（每个服务器一个有状态的会话）。
- **MCP Server（MCP 服务器）**：位于工具前面的轻量封装。
- **Tool（工具）**：可调用的函数（可以是数据源、API）。

**流程**

- 客户端向 MCP 服务器调用 `tools/list`（你能做什么？）。
- 服务器返回描述每个工具的 JSON（名称、摘要、JSON Schema）。
- 宿主把这份 JSON 注入模型的上下文。
- 用户提示触发模型，模型发出结构化的工具调用。
- MCP 服务器执行，对话继续。
- MCP 提供 stdio 与可流式 HTTP 传输层。

## 第 10 页：MCP 请求流程

![MCP 客户端与服务器交互流程图](images/1001/slide10-01.png)
![聊天/模型图标](images/1001/slide10-02.png)
![模型图标](images/1001/slide10-03.png)
![MCP 客户端图标](images/1001/slide10-04.png)
![工具/服务器图标](images/1001/slide10-05.png)
![MCP 服务器图标](images/1001/slide10-06.png)
![数据源图标](images/1001/slide10-07.png)
![数据源图标](images/1001/slide10-08.png)
![数据源图标](images/1001/slide10-09.png)
![数据源图标](images/1001/slide10-10.png)
![LLM 图标](images/1001/slide10-11.png)

图中文字中文对照：

- 用户输入：**Summarize my emails from Jack**（总结 Jack 发来的邮件）。
- 左侧标注 **MCP client**（MCP 客户端），右侧标注 **MCP server**（MCP 服务器）。
- 编号流程：
  1. **Ask query**（提出查询）。
  2. **Get tools**（获取工具列表）。
  3. **Send query and pick tool with params**（发送查询，并选择带参数的工具）。
  4. **Call function for tool and get response**（调用工具函数并获得响应）。
  5. **Send response**（把响应发回）。

图中说明：左侧是用户、聊天界面/MCP 客户端与模型；右侧是 MCP 服务器以及邮件等数据源。MCP 客户端先从服务器获取工具定义，再把用户查询和选中的工具及参数发给服务器，服务器调用底层数据源后把结果返回对话。

## 第 11 页：如何设计一个好的 MCP 服务器（方案 1）

**如何设计一个好的 MCP 服务器（方案 1）**

- MCP 不是 REST API 的包装层。
  - 工具太多、太小。
  - 上下文变得庞大而复杂。
  - Agent 把过多时间花在编排逻辑上。

**最佳实践**

- 按结果设计，而不是按操作设计。
  - 用 `send_payment(user_email)`，而不是 `get_users(user_id)` → `list_account(user_email)` → `send_payment(account_id)`。
- 参数要显式。
  - 不要用嵌套的字典输入。
- 说明文字就是上下文。
  - Docstring、错误信息等，都是提示词。
- 工具命名要便于发现。
  - 用服务名前缀命名工具。

## 第 12 页：如何设计一个好的 MCP 服务器（方案 2）

**如何设计一个好的 MCP 服务器（方案 2）**

- 随着 MCP 服务器数量爆炸式增长，只暴露两个工具：`search` 和 `execute`。
- Agent 调用 `search` 来找到相关工具和定义。
- `execute` 生成确定性的代码来执行操作。
- 大幅减少上下文，而且无论有多少个 MCP 服务器，这套方法都适用。
- Token 减少 90% 以上。

> **演讲者备注**：按需加载工具，在数据到达模型之前先过滤，并用一个简单步骤执行复杂逻辑。

## 第 13 页：方案 2 的代码示例

**如何设计一个好的 MCP 服务器（方案 2）**

**任务：找到一张 Jira 工单，并用 Google Drive 中的信息更新它。**

![筛选 Jira 与 Drive 工具的代码截图](images/1001/slide13-01.png)

图中代码（按截图转录；截图右侧被裁切，末尾不完整）：

```js
async () => {
  const tools = await codemode.tools();
  return tools
    .filter(t => t.name.includes("jira") || t.name.includes("drive"))
    .map(t => ({
      name: t.name, params: Object.keys(t.inputSchema.properties)
```

中文说明：这段代码从 `codemode.tools()` 取出全部工具，只保留名称中包含 `jira` 或 `drive` 的工具，并映射出工具名和参数名。也就是说，agent 先“搜索”出与任务相关的工具，而不是把全部工具定义都塞进上下文。

![调用 Jira 与 Google Drive 的代码截图](images/1001/slide13-02.png)

图中代码（按截图转录，补全了 OCR 对个别括号的误识别）：

```js
async () => {
  const tickets = await codemode.jira_search_jira_with_jql({
    jql: 'project = BLOG AND status = "In Progress"',
    fields: ["summary", "description"]
  });
  const doc = await codemode.google_workspace_drive_get_content({
    fileId: "1aBcDeFgHiJk"
  });
  await codemode.jira_update_jira_ticket({
    issueKey: tickets[0].key,
    fields: { description: tickets[0].description + "\n\n" + doc.content }
  });
  return { updated: tickets[0].key };
}
```

中文说明：这段代码先用 JQL 查询 `BLOG` 项目中状态为“进行中”的工单，读取摘要和描述；再从 Google Drive 读取指定文件内容；最后把 Drive 内容追加到工单描述后面，完成更新并返回被更新的工单 key。

> **演讲者备注**：按需加载工具，在数据到达模型之前先过滤，并用一个简单步骤执行复杂逻辑。

## 第 14 页：高级 MCP 架构设计

![企业级 MCP 服务器门户架构图](images/1001/slide14-01.png)

图中文字中文对照与结构说明：

- 左侧 **MCP clients**（MCP 客户端）：**ChatGPT**、**CURSOR**。
- 中央 **MCP server portals**（MCP 服务器门户）。
- 门户与远程服务器之间经过 **ZTNA (Access)**（零信任网络访问/访问控制）。
- 中间 **Remote MCP servers**（远程 MCP 服务器）：**CLOUDFLARE**。
- 右上 **Internal services**（内部服务）：**ClickHouse**、**snowflake**。
- 右下 **SaaS MCP servers**（SaaS 类 MCP 服务器）：**slack**、**salesforce**、**Jira**、**PayPal**、**shopify**、**GitHub**。

中文说明：员工把自己的 MCP 客户端连接到企业的 MCP 服务器门户后，门户会立即列出其有权使用的所有内部和第三方 MCP 服务器。门户还提供集中式日志、统一的策略执行和数据丢失防护（DLP）护栏。

> **演讲者备注**：员工只需把 MCP 客户端连接到 MCP 服务器门户，门户就会立即显示他们被授权使用的所有内部和第三方 MCP 服务器。除此之外，我们的 MCP 服务器门户还提供集中式日志、一致的策略执行和数据丢失防护护栏。

## 第 15 页：Agent 技能

**Agent 技能**

- 一种动态加载 agent 能力的标准。
  - 领域特定（Domain-specific）。
  - 结合代码与提示词。
  - 由 agent 按需加载。

**用例**

- 文档撰写。
- 制作 PowerPoint。
- 数据分析。
- ……以及更多。

> **演讲者备注**：<https://agentskills.io/home>

## 第 16 页：Agent 技能的文件结构

**Agent 技能**

![SKILL.md 文件结构截图](images/1001/slide16-01.png)

图中文字中文对照（左侧为行号 1–20，内容是技能文件的 YAML 元数据与 Markdown 正文）：

```markdown
name: my-skill
description: Short description of what this skill does and when to use it.

# My Skill

Detailed instructions for the agent.

## When to Use

- Use this skill when...
- This skill is helpful for...

## Instructions

- Step-by-step guidance for the agent
- Domain-specific conventions
- Best practices and patterns
- Use the ask questions tool if you need to clarify requirements with the user
```

中文含义：

- `name`：技能名称（`my-skill`）。
- `description`：简短描述这个技能做什么、什么时候使用。
- `# My Skill`：技能标题。
- `Detailed instructions for the agent.`：给 agent 的详细指令。
- `## When to Use`：何时使用；下面是触发场景与适用情况。
- `## Instructions`：具体指令；包括分步指导、领域特定约定、最佳实践与模式。
- 最后一条：如果需要向用户澄清需求，使用提问工具（`ask questions`）。

> **演讲者备注**：提供一个 `skills.md`。示例见 gws agent skills：<https://github.com/mattpocock/skills>。

## 第 17 页：API、MCP 与技能的区别

**API vs MCP vs Skills（API、MCP 与技能）**

**APIs**

- **是什么**：应用暴露给开发者调用的 HTTP/REST/GraphQL 服务接口。
- **谁来用**：你本人，或者某个 SDK。
- **使用方式**：认证、重试、分页、输入校验等都由你自己决定。

**MCP**

- **是什么**：服务器暴露的工具定义，让 LLM agent 能以标准化的方式调用。
- **谁来用**：模型/agent 运行时（以“工具调用”的形式），而不是每次都由人类开发者编写定制集成。
- **使用方式**：与外部资源、数据、服务交互的主要机制。

**Skills**

- **是什么**：可复用的任务包/流程，教 agent 如何完成一项工作，通常通过编排多个工具/端点来实现。
- **谁来用**：agent 或 agent 框架，把它当作可以主动取用的更高层能力。
- **使用方式**：工作流抽象——“这是完成 X 的可重复做法。”
