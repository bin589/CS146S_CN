# Sentry MCP

> 来源：<https://docs.sentry.io/product/sentry-mcp/>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。
Sentry MCP Server
Connects AI assistants to Sentry for searching errors, analyzing performance, triaging issues, reading documentation, and managing projects — all via the Model Context Protocol.
All connections use OAuth. The first connection will trigger an authentication flow to connect to your Sentry account.
Connecting
The base MCP server address is: https://mcp.sentry.dev/mcp
You can optionally scope the connection to an organization or project:
- https://mcp.sentry.dev/mcp/{organizationSlug} — scoped to one organization
- https://mcp.sentry.dev/mcp/{organizationSlug}/{projectSlug} — scoped to one project
When scoped, tools automatically default to the constrained org/project and unnecessary discovery tools are hidden. Scoping to a project is recommended when possible.
Query Parameters
- ?experimental=1 — Enable forward-looking tool variants and experimental features
Parameters can be combined: https://mcp.sentry.dev/mcp/my-org/my-project?experimental=1
Setup Instructions
Claude Code
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp/{organizationSlug}/{projectSlug}
Cursor
Use the "Install MCP Server" button, or manually add to MCP settings:
{
  "mcpServers": {
    "sentry": {
      "url": "https://mcp.sentry.dev/mcp/{organizationSlug}/{projectSlug}"
    }
  }
}
VSCode
Command Palette → "MCP: Add Server" → HTTP → enter the endpoint:
https://mcp.sentry.dev/mcp/{organizationSlug}/{projectSlug}
Other Clients
Any MCP-compatible client can connect using the HTTP transport at the endpoint URL above.
