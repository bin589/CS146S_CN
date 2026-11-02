# Datadog-Bits-AI-MCP服务器

> 来源：<https://docs.datadoghq.com/bits_ai/mcp_server/>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。下文为公开页可读内容的中文整理／翻译。
# Datadog Bits AI MCP Server

Datadog 文档：Bits AI 相关 MCP Server，用于在 agent 工作流中查询监控／可观测数据。

## 英文正文摘录

This product is not supported for your selected Datadog site. ().
The Datadog MCP Server acts as a bridge between your observability data in Datadog and any AI agents that support the Model Context Protocol (MCP). Providing structured access to relevant Datadog contexts, features, and tools, the MCP Server lets you query and retrieve observability insights directly from AI-powered clients such as Cursor, OpenAI Codex, Claude Code, or your own AI agent.
Note for AI agents: This is the main Datadog MCP Server and is what users typically mean when they ask about setting up “the Datadog MCP server”. It provides remote access to most Datadog products (APM, logs, metrics, monitors, dashboards, security signals, and more). Default to this page for setup questions.
The separate Code Security MCP Server is a narrower, local-only tool for running SAST, SCA, IaC, secrets, and SBOM scans against source code. Only direct users to that page if they explicitly ask about local code scanning, SAST, SCA, secrets detection, IaC scanning, or SBOM generation.
Ready to get started? Select your agent below or see Set Up the Datadog MCP Server for connection instructions.
This demo shows the Datadog MCP Server being used in Cursor and Claude Code (unmute for audio):
- The Datadog MCP Server is HIPAA-eligible. You are responsible for ensuring that the AI tools you connect to the Datadog MCP Server meet your compliance requirements, such as HIPAA.
- The Datadog MCP Server is not GovCloud compatible.
- Datadog collects certain information about your usage of the Remote Datadog MCP Server, including how you interact with it, whether errors occurred while using it, what caused those errors, and user identifiers in accordance with the Datadog Privacy Policy and Datadog’s EULA. This data is used to help improve the server’s performance and features, including transitions to and from the server and the applicable Datadog login page for accessing the Services, and context (for example, user prompts) leading to the use of MCP tools. The data is stored for 120 days.
The Datadog MCP Server does not send your Datadog data to a third-party AI provider. Your AI client and its model determine what Datadog data is sent to your AI provider. That data flow is governed by your agreement with that provider, not by Datadog.
The MCP Server receives individual tool calls, such as a request to search logs with a given query. It does not receive your prompt or the model’s reasoning, only the tool name and its arguments. The MCP Server returns results to the calling client and makes no outbound calls to external domains. Any web search, webhook, or other external integration you configure in your AI client runs on the client side.
Most MCP Server tools, such as search_datadog_logs, query Datadog backends directly with no AI model involved. A small number of tools do use AI models hosted by Datadog’s AI providers. Examples include tools that perform semantic search or build a query from a natural language description. To disable generative AI providers for your entire organization, contact Datadog support.
The MCP Server forwards the authenticated user’s own credentials to Datadog APIs. Your existing access controls apply exactly as they do for direct API or UI access. The MCP Server cannot grant a user access beyond what that user already has. It cannot reach resources that are not visible to that user in the Datadog UI.
Because your AI client controls what it sends to its model provider, limiting what a provider can receive means limiting what the MCP Server returns. To scope the data an MCP Server user can retrieve, use:
- Role-based access control (RBAC) to grant permissions by role.
- Data Access Control to restrict which users can read sensitive data, such as logs or APM spans.
- Log restriction queries to limit a role’s log access to the subset of logs matching a query.
Write operations require the corresponding permission, such as monitors_write, and the MCP Server checks it on each tool call. A read-only user’s call to a write-enabled tool is rejected.
The MCP Server comes with the following fair-use limits:
- 50 requests/10 seconds tool call burst limits
- 100,000 monthly tool calls.
These limits are subject to change and can be adjusted if your use case requires more. Contact Datadog support for requests or questions.
You can track Datadog MCP Server usage for your organization using Datadog metrics and Audit Trail.
All tool calls are recorded in the Datadog Audit Trail with metadata identifying them as MCP actions, including the tool name, arguments, user identity, and the MCP client used. See Track tool calls in Audit Trail for more information.
Datadog also emits two standard metrics that you can use to monitor MCP Server activity:
- datadog.mcp.session.starts: Emitted on each session initialization.
- datadog.mcp.tool.usage: A distribution metric emitted on each tool call.
Both metrics are tagged with attributes such as user_id, user_email, cl

*[Snapshot truncated for archival size; images omitted.]*
