# Arize-Phoenix-MCP服务器

> 来源：<https://arize.com/docs/phoenix/integrations/phoenix-mcp-server>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。下文为公开页可读内容的中文整理／翻译。
# Arize Phoenix MCP Server 文档

Phoenix 可观测性产品的 MCP Server 集成说明：如何通过 Model Context Protocol 把 tracing／评估等能力暴露给 agent 客户端。

## 英文正文摘录

The Remote MCP Server (beta) is built into Phoenix at
/mcp, so any MCP client can read and act on your Phoenix data with nothing to install. Agents with a shell can reach the same data through the Phoenix CLI; see CLI or MCP server?.
Remote MCP Server
The URL is your Phoenix endpoint plus/mcp: http://localhost:6006/mcp for a local Phoenix. Requires Phoenix 19.0.0 or later.
Connect
The Phoenix CLI writes the config for you:gemini or code command on your PATH.
To configure by hand, or for other clients, use the steps below with your own endpoint in place of http://localhost:6006.
Claude Code
The Claude Code plugin registers this server and the skills together. To add the server alone:Then run /mcp in Claude Code, select phoenix, and log in.
Codex (OpenAI)
The Codex plugin registers this server for you. By hand, create a Phoenix API key, export it as PHOENIX_API_KEY, and add to ~/.codex/config.toml:Run /mcp in Codex to confirm it connected.
Cursor, VS Code, and OpenCode
Add the server to the client’s MCP config. Each prompts a browser login on first use.In Cursor, add it to ~/.cursor/mcp.json, or project .cursor/mcp.json:In VS Code, add it to .vscode/mcp.json, or run MCP: Add Server from the Command Palette:In OpenCode, add it to ~/.config/opencode/opencode.json, or project opencode.json:
Gemini CLI
Gemini CLI’s mcp add mirrors Claude Code’s flags:--scope project writes .gemini/settings.json in the current directory instead.Gemini disables all MCP servers in untrusted folders, so trust the folder when prompted. Then gemini mcp list shows phoenix connected; run /mcp inside Gemini CLI to log in.Antigravity is a different tool that also writes under ~/.gemini/; see Antigravity and other clients below.
Claude Desktop
Claude Desktop connects from Anthropic’s cloud, so your Phoenix must be reachable on the public internet; localhost is not. Add a custom connector in its connector settings:
- Name: Phoenix
- URL: https://your-phoenix.example.com/mcp
It opens the browser login on first use.
Antigravity and other clients
Any client with streamable HTTP and OAuth works: set the URL to <your-phoenix-endpoint>/mcp and log in on first use. Clients without OAuth use an API key.Antigravity is one. Create a Phoenix API key and add to ~/.gemini/config/mcp_config.json (or Manage MCP Servers → View raw config):Omit headers if your Phoenix has no authentication.
/mcp in Claude Code or Codex, or claude mcp list: phoenix shows as connected. With auth on, first use opens a browser login.
What your agent can do with it
Everything the Phoenix REST API can do, and the agent composes the operations it needs in one call. Try:default.
Learn more
- Connect Your Coding Agent: the install for each agent, and the plugins that register this server.
- Phoenix CLI: the alternative for agents with a shell.
- Skills: what load_skill serves.
- API Keys: for clients that cannot log in through a browser.
Reference
Fallback: API keys
For CI, sandboxes, or clients that cannot log in through a browser, pass a Phoenix API key as a Bearer header:${PHOENIX_API_KEY} at runtime, so the key never lands in the config. In JSON configs:
How it works
By default the server exposes seven code-mode tools for discovering and composing Phoenix operations.
The catalog is generated from the Phoenix REST API, so it always matches your Phoenix version. Alongside those operations it carries two query surfaces: 
describeSqlSchema and executeSql run read-only analytics SQL over telemetry, datasets, and experiments, and describeGraphqlSchema and executeGraphqlQuery run read-only queries against Phoenix’s GraphQL schema, reaching data the REST API does not cover. On a deployment that can write, executeGraphqlMutation runs GraphQL mutations too; see Security. execute runs Python in Monty, Pydantic’s sandboxed interpreter; see Security for its limits. PHOENIX_ENABLE_MCP_CODE_MODE=false turns code mode off and exposes each operation as its own tool.
Server configuration
PHOENIX_ENABLE_MCP_SERVER=false removes /mcp; PHOENIX_ENABLE_MCP_CODE_MODE=false drops execute. Both are listed under self-hosting configuration. PHOENIX_SKILLS_PATHS serves your own skills.
Security and troubleshooting
Security
Clients discover auth on their own: /mcp advertises RFC 9728 metadata at /.well-known/oauth-protected-resource/mcp pointing at Phoenix’s authorization server. See Agent Authentication Discovery.
- Browser login uses Phoenix’s built-in OAuth2 authorization server, with its own switch (PHOENIX_ENABLE_OAUTH2_AUTHORIZATION_SERVER), grant expiry, registration modes, redirect allowlists, and rate limits.
- Tokens are audience-scoped to /mcp and cannot be replayed elsewhere. API keys carry their creator’s permissions.
- Code is sandboxed. Monty has no filesystem or network access and runs in worker subprocesses. It allows a restricted standard library (json, re, datetime) and blocks subprocess, socket, importlib, and third-party packages. Each execute is capped at 30 s of code, 100 MB, 50 operati

*[Snapshot truncated for archival size; images omitted.]*
