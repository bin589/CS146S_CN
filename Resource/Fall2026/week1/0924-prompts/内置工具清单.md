# 内置工具（中文译文）

> 非官方完整中文译文；抓取日期：2026-10-22。对照：[英文原文件](tool_list.md)。以下是课程中展示的工具清单，工具名保留原样；不表示本仓库配置了这些工具。

## 文件

- **Read**——读取本地文件、图像或 PDF。
- **Edit**——替换文件中的精确字符串。
- **Write**——创建文件，或完全覆盖已有文件。
- **NotebookEdit**——替换、插入或删除 Jupyter notebook 中的单元格。

## Shell

- **Bash**——运行 shell 命令并返回输出。
- **Monitor**——以流式方式接收长时间运行的后台脚本事件。

## 搜索与代码智能

- **WebSearch**——搜索网页，返回结果标题和 URL。
- **WebFetch**——获取一个 URL，并依据该页面回答给定的 prompt。
- **LSP**——向语言服务器查询定义、引用、悬停信息和符号。

## 代理

- **Agent**——为复杂、并行或委派工作启动子代理。
- **ListAgents**——列出本会话可发送消息的代理。
- **SendMessage**——向另一代理发送消息。
- **TaskStop**——停止运行中的后台任务或代理。
- **Workflow**——在后台运行多代理工作流脚本。

## 规划与隔离

- **EnterPlanMode**——在非平凡的实现前切换到计划模式。
- **ExitPlanMode**——提交写好的计划，供用户批准。
- **EnterWorktree**——创建隔离的 git worktree，并将会话切换进去。
- **ExitWorktree**——离开会话的 worktree，返回原目录。

## 调度

- **CronCreate**——调度一次性或周期性提示词。
- **CronDelete**——取消本会话中调度的 cron 任务。
- **CronList**——列出本会话中调度的 cron 任务。
- **ScheduleWakeup**——在 `/loop` 动态模式下，调度下一次自主节奏的唤醒。
- **RemoteTrigger**——创建、更新、运行和检查 claude.ai 的远程触发器。

## Artifacts

- **Artifact**——将 HTML 页面发布为私有 claude.ai artifact。
- **ArtifactComments**——读取并回复已发布 artifact 中的评论线程。
- **ArtifactData**——读取和写入已发布 artifact 的共享数据库。

## MCP 资源

- **ListMcpResourcesTool**——列出已配置 MCP 服务器提供的资源。
- **ReadMcpResourceTool**——根据服务器名称和 URI 读取某个资源。
- **ReadMcpResourceDirTool**——列出 MCP 目录资源的直接子项。

## 交互

- **AskUserQuestion**——通过可选项向用户提出阻塞性决策问题。
- **Skill**——加载当前任务所需的已打包技能指令。
- **PushNotification**——发送桌面通知；如果连接了 Remote Control，还会向手机推送。
- **SendFeedback**——起草关于 Claude Code 产品或模型问题的反馈。
- **EndConversation**——在持续的不当对待（abuse），或用户明确要求演示之后，结束对话。

## 设计与审查

- **DesignSync**——将本地组件库与 claude.ai 设计系统项目同步。
- **ReportFindings**——向宿主 UI 提交有类型结构的代码审查发现。
