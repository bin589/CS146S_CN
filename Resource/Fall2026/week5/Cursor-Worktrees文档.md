# Cursor-Worktrees文档

> 来源：<https://cursor.com/docs/configuration/worktrees>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。下文为公开页可读内容的中文整理／翻译。
# Cursor：Worktrees 配置文档

说明 Cursor 如何结合 git worktree 做多 agent／并行隔离开发。

## 英文正文摘录

Worktrees
The UI-native worktrees feature described on this page is only available in the Agents Window. In the IDE, use the Worktree Skills commands below.
Worktrees let Agent work in isolated Git checkouts. Each task gets its own files, dependencies, and changes while your main checkout stays untouched.
Use worktrees when you want to start several agents on the same repo without conflicts.
Create a worktree in the Agents Window
When you start or move an agent into a worktree from the Agents Window, Cursor creates a separate checkout for that agent. The agent continues the task inside the worktree, so changes stay isolated from your main checkout.
After the agent finishes, review the result in the Agents Window. You can keep working in the worktree, create a commit or PR from that checkout, or bring the result back into your main workspace.
How does worktree setup work?
You can customize worktree setup with .cursor/worktrees.json. Cursor checks this file when it creates a worktree in the Agents Window, the IDE, or the Cursor CLI.
Cursor looks for .cursor/worktrees.json in this order:
- In the worktree path
- In the root path of your project
Configuration options
The worktrees.json file supports three setup keys:
- setup-worktree-unix: Commands or a script path for macOS and Linux. This takes precedence over setup-worktree on Unix systems.
- setup-worktree-windows: Commands or a script path for Windows. This takes precedence over setup-worktree on Windows.
- setup-worktree: Generic fallback for all operating systems.
Each key accepts either:
- An array of shell commands: executed sequentially in the worktree
- A string filepath: path to a script file relative to .cursor/worktrees.json
Example setup configurations
Using command arrays
Node.js project
{  "setup-worktree": [    "npm ci",    "cp $ROOT_WORKTREE_PATH/.env .env"  ]}
We do not recommend symlinking dependencies into the worktree. This can cause issues in the main worktree. Use a fast package manager such as bun, pnpm, or uv instead.
Python project with virtual environment
{  "setup-worktree": [    "python -m venv venv",    "source venv/bin/activate && pip install -r requirements.txt",    "cp $ROOT_WORKTREE_PATH/.env .env"  ]}
Project with database migrations
{  "setup-worktree": [    "npm ci",    "cp $ROOT_WORKTREE_PATH/.env .env",    "npm run db:migrate"  ]}
Build and link dependencies
{  "setup-worktree": [    "pnpm install",    "pnpm run build",    "cp $ROOT_WORKTREE_PATH/.env.local .env.local"  ]}
Using script files
For more complex setups, reference script files instead of inline commands:
{  "setup-worktree-unix": "setup-worktree-unix.sh",  "setup-worktree-windows": "setup-worktree-windows.ps1",  "setup-worktree": [    "echo 'Using generic fallback. For better support, define OS-specific scripts.'"  ]}
Place your scripts in the .cursor/ directory next to worktrees.json.
setup-worktree-unix.sh (Unix and macOS):
#!/bin/bashset -e# Install dependenciesnpm ci# Copy environment filecp "$ROOT_WORKTREE_PATH/.env" .env# Run database migrationsnpm run db:migrateecho "Worktree setup complete!"
setup-worktree-windows.ps1 (Windows):
$ErrorActionPreference = 'Stop'# Install dependenciesnpm ci# Copy environment fileCopy-Item "$env:ROOT_WORKTREE_PATH\.env" .env# Run database migrationsnpm run db:migrateWrite-Host "Worktree setup complete!"
OS-specific configurations
You can provide different setup commands for different operating systems:
{  "setup-worktree-unix": [    "npm ci",    "cp $ROOT_WORKTREE_PATH/.env .env",    "chmod +x scripts/*.sh"  ],  "setup-worktree-windows": [    "npm ci",    "copy %ROOT_WORKTREE_PATH%\\.env .env"  ]}
Debugging
If you want to debug worktree setup, open the Output panel in the editor and select Worktrees Setup.
How does Cursor discover existing worktrees?
Cursor 3.5 keeps a modified time checkpoint for the machine worktree root and for each workspace subdirectory. On startup, Cursor re-scans the filesystem unless those timestamps prove nothing changed since the last discovery. This avoids skipping new worktrees that were created while Cursor was closed and eliminates the older worktree.discoveryComplete flag.
Worktrees cleanup
The cleanup behavior in this section reflects Cursor 3.5 and later.
Cursor can clean up older worktrees automatically to limit disk usage. Cleanup runs on an interval and keeps the newest worktrees up to the configured machine-wide maximum count across every workspace on the device.
{  "cursor.worktreeCleanupIntervalHours": 6,  "cursor.worktreeMaxCount": 25}
Use these machine-scoped settings to control cleanup:
- cursor.worktreeCleanupIntervalHours: how often Cursor checks for old worktrees. Cursor 3.5 catches up after restarts by scheduling a delayed cleanup if the last successful run is older than this interval.
- cursor.worktreeMaxCount: the maximum number of worktrees Cursor keeps before cleaning up older ones. The default cap is 25 worktrees per machine, and all workspaces contribute toward the same

*[Snapshot truncated for archival size; images omitted.]*
