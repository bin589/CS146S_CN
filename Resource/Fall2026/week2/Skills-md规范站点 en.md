# skills.md — specification site

> 来源：<http://skills.md>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。
> Resolved from http://skills.md → https://skills.md/
Skills for agents.
Your agent finds the skill, runs it on skills.md and the files come back. For Claude Code, Codex, Antigravity, Cursor and any MCP host.
Paste it to Claude Code, Codex, Cursor or any MCP host. It installs the CLI, signs in and registers the MCP server.
Or run the commands yourself
bun install -g @hasna/skillsskills loginskills mcp --register <agent>
Claude Code session in ~/acme.
User asks: Design a logo for Acme, our developer tool. Clean geometric mark, navy and white, a few options.
- Bash: skills search --remote logo
- Output: logo-design [Design & Branding]
- Output: Generate premium multi-variant logo packages with transparent PNGs, vector-style SVGs, usage notes, and manifests
- Fetch: https://skills.md/api/v1/skills/logo-design/skill.md
- Output: # Logo Design … --brief, --brand, --style, --palette, --variations
- Agent: Only this SKILL.md is in context. It runs on skills.md, so I'll check with you first.
- Agent asks: Run logo-design on skills.md with four variations? User chooses: Yes, run it.
- Bash: skills run --remote --yes --wait logo-design --brief "clean geometric mark for a developer tool" --brand "Acme" --palette "navy,white" --variations 4
- Output: Completed remote run for logo-design
- Output: Run: 7c1e9b42-5d0a-4f3e-9a61-2b8c4e0d7f15
- Bash: skills exports download 7c1e9b42-5d0a-4f3e-9a61-2b8c4e0d7f15
- Output: Downloaded 12 artifacts
- Output: Exports: .skills/exports/logo-design/7c1e9b42-5d0a-4f3e-9a61-2b8c4e0d7f15
- Result: Four logo concepts are in .skills/exports/logo-design/…/transparent/ (PNG) and vector/ (SVG), with usage-notes.md and logo-brief.md beside them.
300+ curated skills, each built and validated before it ships.
Logo Design, Brand Kit, Pitch Deck, One Page Website, Market Research Report, Short Video Pack and the rest are one skills search --remote away.
Add your own. skills push <name> publishes a skill from your machine; every push is a version, and skills versions <name> lists them.
Plans and credits.
- Free $0 + pay per run Public skills, all agents. Trial credits for new accounts. Hosted skills are quoted first; you approve a credit limit per run. No subscription required. Sign upBuy credits
- Pro $12/month 1,500 credits every month (20% off). Extra credits at the normal pack price. SubscribeExisting subscriber? Manage billing
Credit packs: $1, $5, $20, $50 or $100. Purchased credits last 365 days. Companies: support@hasna.com.
