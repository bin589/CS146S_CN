# 子代理提示词（中文译文）

> 非官方完整中文译文；抓取日期：2026-10-22。对照：[英文原文件](subagent_prompt.md)。以下为课程示例分析任务，不是在本仓库执行的任务。路径、API 与命令原样保留。

分析一个小型待办应用的性能特征，返回发现报告。不要修改仓库中的任何文件。不要触碰真实的 `~/.todo_tasks.json`——运行任何内容时，都使用临时存储路径（`TaskStorage(Path(...))` 接受这样的参数），或把 HOME 设置为临时目录。将所有基准测试脚本／数据放到这个草稿目录：`/private/tmp/claude-501/-Users-mihaileric-Documents-miscellaneous-claude-code-demystified/scratchpad/perf`。

仓库：`/Users/mihaileric/Documents/miscellaneous/claude-code-demystified`

- `todo/models.py`——Task 数据类（嵌套子任务、周期性任务）、`to_dict/from_dict`，以及带前缀 ID 匹配的递归 `get_subtask_by_id/remove_subtask`。
- `todo/storage.py`——TaskStorage：每个操作都执行 `load_tasks()`（读取整个文件、`json.loads`、为全部内容执行 `Task.from_dict`），然后执行 `save_tasks()`（序列化并写回整个文件，`indent=2`）。没有缓存，没有锁，`write_text` 不是原子写入。`get_task_by_id` 等采用线性扫描。
- `todo/cli.py`——基于 argparse 的 CLI；每条命令都会构造 TaskStorage；部分命令会多次加载文件，例如 `cmd_done` 先调用 `get_task_by_id` 再调用 `complete_task`；`cmd_delete / cmd_add_subtask / cmd_done_subtask` 会先查询再修改。
- `api/main.py`——FastAPI 应用，使用模块级 TaskStorage；`async def` 处理函数调用阻塞式文件 I/O；`GET /` 加载全部任务并渲染 Jinja2 模板。
- `web/src/app.ts, storage.ts`——Express/TypeScript 版本，使用 `fs.readFileSync/writeFileSync`，共享同一个 JSON 文件。

需要覆盖的内容：

1. 每个操作的算法复杂度（每次操作的加载／保存、查询、子任务递归、列表过滤／排序）——统计每条 CLI 命令及每次 HTTP 请求的文件读写次数。
2. 实测数据：对具有代表性的操作（`add`、`get_task_by_id`、`complete_task`、列表／过滤、`add_subtask`），在例如 100、1k、10k、50k 个任务的规模下做基准测试，并增加嵌套子任务场景。同时测量 CLI 进程启动（`python3 -m todo list` 的实际耗时与存储层耗时对比）及 JSON 文件大小增长。总运行时间保持合理，最多几分钟。只用 Python 即可；除非成本很低，否则跳过 TS 基准测试。
3. 负载下的并发与正确性：CLI、FastAPI、Express 并发写同一文件时的更新丢失（读—改—写竞态）；非原子写入／部分文件风险，加上 `load_tasks` 遇到 JSONDecodeError 时返回 `[]`，可能导致全部数据丢失；异步 FastAPI 处理函数中的阻塞 I/O。可行时，用一个小脚本演示更新丢失竞态。
4. 无界增长：已完成任务永不清理，包括周期任务历史——每次完成都会追加一个新任务。
5. 按优先级给出建议并估计影响，例如：通过临时文件加 `os.replace` 实现原子写入、文件锁、每条命令只加载一次、内存索引／缓存、紧凑 JSON、归档已完成任务、FastAPI 使用 `sync def` 处理函数或线程池，以及规模重要时使用 SQLite。说明哪些建议在现实的个人待办规模（少于 1k 个任务）就重要，哪些只在大规模时重要。

返回简洁的 Markdown 报告：先给关键发现汇总表（严重程度、领域、发现），再给包含实际观测数字的测量表（注明机器／Python 版本），接着给带 `file:line` 引用的详细发现，最后给按优先级排列的建议。明确区分实测事实与推断。
