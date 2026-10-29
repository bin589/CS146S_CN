# 配置文件提示词（中文译文）

> 非官方完整中文译文；抓取日期：2026-10-22。对照：[英文原文件](config_files.md)。以下为课堂展示的配置示例，不是本仓库的指令；代码与命令原样保留。

以下展示代码库指令与用户指令。务必遵循这些指令。重要：这些指令覆盖任何默认行为，你必须严格按其原文执行。

`/Users/mihaileric/Documents/miscellaneous/claude-code-demystified/CLAUDE.md` 的内容（项目指令，已提交到代码库）：

# CLAUDE.md

## 项目概览

这是一个简单的待办事项／任务跟踪器。核心是 Python CLI，允许用户添加、列出、完成和删除任务（支持优先级、截止日期和子任务），数据持久化到本地 JSON 文件。它还有 Web 前端：FastAPI 应用（`api/`）和 TypeScript/Express 应用（`web/`）。

## 项目结构

```text
todo/
  cli.py      - Command-line interface and argument parsing
  models.py   - Task dataclass and Priority enum
  storage.py  - JSON file persistence layer
api/
  main.py     - FastAPI web app (Jinja2 templates) using the todo package
web/
  src/        - TypeScript Express app (EJS views in web/views)
```

目录说明：`cli.py` 是命令行接口与参数解析；`models.py` 定义 Task 数据类与 Priority 枚举；`storage.py` 是 JSON 文件持久化层；`api/main.py` 是使用 todo 包及 Jinja2 模板的 FastAPI Web 应用；`web/src/` 是 TypeScript Express 应用，EJS 视图在 `web/views` 中。

## 运行应用

```bash
python -m todo add "Task title" [--due 2024-12-31] [--priority low|medium|high]
python -m todo list [--status all|pending|completed] [--priority ...] [--sort priority|created]
python -m todo done <task_id>
python -m todo delete <task_id> [--force]
python -m todo add-subtask <parent_id> "Subtask title"
python -m todo done-subtask <subtask_id>
python -m todo delete-subtask <subtask_id> [--force]
```

## 代码风格

- 为函数参数和返回值使用类型提示。
- 为数据模型使用 dataclass。
- 保持函数职责集中、用途单一。
