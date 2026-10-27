# 《现代软件开发者》第 7 讲：打造 Agent 就绪的仓库

> **非官方中文翻译**，仅供学习参考，不代表原作者或斯坦福大学。
> 源幻灯片：[`1020-agent-readiness en.pptx`](./1020-agent-readiness%20en.pptx)
> 抓取日期：2026-10-27
> 说明：按原 pptx 逐页全文翻译，保留原始 URL、代码、专名与时间戳；内嵌图片提取到 [`images/1020/`](images/1020/)，图中英文在图片下方给出中文对照。代码与命令保持原文，不执行。

## 第 1 页：现代软件开发者

**现代软件开发者**

CS146S

斯坦福大学，2026 年秋季

Mihail Eric

themodernsoftware.dev

## 第 2 页：课程事务

**课程事务**

- 第 4 次作业周日截止。
- 第一次开源贡献怎么样？
- 课程期中问卷。
- 客座讲座改在 STLC 111（此后所有周四课都在这里）。
- Eno Reyes

![嘉宾照片](images/1020/slide02-01.png)

图中说明：一张人物照片，放在 “Eno Reyes” 条目旁。图中没有文字。

## 第 3 页：上下文的故事

**上下文的故事**

幻灯片上的标注块：

- System Prompt
- `Memory.md`
- Env info（环境信息）
- MCP tools
- Skills
- `AGENTS.md`（全局）
- `AGENTS.md`（局部）

## 第 4 页：创建 Agent 就绪的仓库

**创建 agent 就绪的仓库**

## 第 5 页：为什么

**为什么**

- 今天大多数代码库并没有为 agent 的成功做好准备。
- LLM 的很多困惑，来自试图在一个混乱或不完整的开发环境里把任务做完。
- 优化你的代码库／环境，让人和 agent 都能看懂正在发生什么。

## 第 6 页：人类可以绕过去的东西

**人类可以绕过去的东西**

- 测试覆盖不足（手动测试）。
- 文档过时（去烦同事）。
- 没有 linter（你可以自己看分号）。
- 构建不稳定（重试）。
- 环境搭建／上手很复杂（去烦同事）。
- 可观测性很难用或干脆没有（去看日志）。
- 没有安全扫描（现在先别担心……）。
- 程序化模式不一致（隐含的部落知识）。

## 第 7 页：什么会让 agent 失败

**什么会让 agent 失败**

- 没有测试 → 无法验证正确性。
- 没有文档／标准 → 无法保证一致性。
- 构建不可靠 → 无法验证改动。
- 没有可观测性 → 无法调试。
- 环境搭建复杂 → 环境不可复现。
- 没有安全检查 → 引入漏洞。

> **演讲者备注**：一个混乱的仓库可以简单到：访问模式不统一（比如数据库）、变量命名不统一、多个函数做同一件事。

## 第 8 页：Agent 就绪环境清单

**Agent 就绪环境清单**

- 足够的测试覆盖。
- 封闭（hermetic）的构建系统。
- 文档清楚、前后一致的设计模式。
- 没有过时的 README。
- 可验证的检查。
- 一份专门给 agent 的操作手册。
  - `AGENTS.md` 等。

## 第 9 页：这让你能做什么

**这让你能做什么**

- 完成大型任务（迁移等）。
- 团队成员各自跑多份 agent 工作负载。
- 自动化代码审查。
- 长时间运行、结果可验证的 agent 任务。
- 在存量（brownfield）代码库上跑 agent 工作负载。

## 第 10 页：Agent 就绪度演示

**Agent 就绪度演示**

> **演讲者备注**：
>
> - <https://factory.ai/news/agent-readiness>
> - <https://factory.ai/agent-readiness>
> - 来看看一些仓库的就绪度：<https://app.factory.ai/analytics/readiness/https%253A%252F%252Fgithub.com%252Fvercel%252Fnext.js>
> - <https://x.com/alvinsng/status/2030056110317818206?s=20>
> - <https://github.com/kodustech/agent-readiness>

## 第 11 页：后台编码 Agent 工作流

**后台编码 Agent 工作流**

## 第 12 页：为什么

**为什么**

编码 agent 能力的演进：

- Tab 补全（2021）
  - 大约 15% 的效率提升
- 同步的单任务完成（2024）
  - 大约 25–35% 的效率提升
- 后台多任务完成（2026+）
  - 解锁：2 倍以上的效率提升

## 第 13 页：后台 agent 需要什么

**后台 agent 需要什么**

- 隔离的开发环境。
- 足够的测试覆盖。
- 封闭的构建系统。
- 文档清楚、前后一致的设计模式。
- 没有过时的 README。
- 可验证的检查。
- 一份专门给 agent 的操作手册。
  - `AGENTS.md` 等。

> **演讲者备注**：这页基本上就是我们讲“构建 agent-first 开发环境”时的那一页。原文备注是 “It’s basically the same slide as our the one from building an agent-first development environment!”

## 第 14 页：Agent 隔离

**Agent 隔离**

- Git worktrees

```bash
git worktree add -b my-new-branch ../my-new-branch
```

- 多 agent 编排器
  - 选项
    - Conductor
    - Cursor parallel agents
    - Claude Code Swarms
    - 自己写一个
  - 把创建 worktree 这类底层搭建抽象掉。
  - 缺点
    - UI 有时会比较死板。
    - 共享资源并没有完全隔离（数据库、端口）。

> **演讲者备注**：这些编排器会让你很难在终端、IDE、云端这些不同界面之间跳转。

## 第 15 页：云端 agent

**云端 agent**

- 把拉起 agent 并配好所需环境的全部复杂性都包掉。
- 你可以在各种界面上拉起这些 agent。

**选项**

- 浏览器（Codex、Claude Code、Devin）
- 代码审查（Graphite、Claude、Devin Review）
- 沟通平台（Slack 里的 Claude Code、Codex）
- 移动端（原生应用，或经由 Slack 这类第三方应用）
- 你的任务跟踪软件（Linear issue）
