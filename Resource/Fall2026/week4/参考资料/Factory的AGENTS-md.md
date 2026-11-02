# AGENTS.md（Factory 文档）

> 来源：Factory Docs · <https://docs.factory.com/harness/agents-md>
> 页面说明：用 AGENTS.md 给 Droid 持久的项目指令、命令和护栏。
> 英文存档：[Factory AGENTS.md en.md](./Factory%20AGENTS.md%20en.md)
> 抓取时间：2026-10-27
> 译文说明：示例命令、文件名、路径与模板代码保持原文。文内链接按文档站写成绝对 URL。非官方译文，版权归 Factory 所有。

`AGENTS.md` 给 Droid 一份每次会话都该带着的项目简报：如何安装、运行、测试、修改、验证，以及如何待在仓库的边界之内。

把它用于应当在 Droid 写代码之前就加载的指导。保持简短、具体、容易核对。

## 创建你的第一份 AGENTS.md

1. **只建一个根文件。** 在仓库根目录放 `AGENTS.md`。先从一个文件开始，只在某个包、应用或服务需要不同规则时才加嵌套文件。
2. **命令放在前面。** 列出 Droid 应该跑的确切安装、开发、测试、类型检查、lint 和构建命令。宽泛命令太贵时，加上 flag 或包过滤器。
3. **补上约定和安全规则。** 写下仓库布局、生成文件的规则、安全边界、所有权边界，以及 Droid 宣布工作完成之前必须给出的证明。
4. **和项目一起提交。** 项目指令属于 git，这样每个队友和每次自动化会话拿到的都是同一份操作上下文。

```markdown
# Repository guide

## Commands

- Install dependencies: `pnpm install`
- Start local server: `pnpm dev`
- Run unit tests: `pnpm test`
- Run type checks: `pnpm typecheck`
- Run lint: `pnpm lint`

## Project layout

- `app/` contains routes and server-rendered pages.
- `components/` contains reusable UI components.
- `lib/` contains shared business logic and integrations.
- Tests live next to the code they cover as `*.test.ts` or `*.test.tsx`.

## Coding conventions

- Prefer small, focused modules with explicit types.
- Keep business logic in pure functions where possible.
- Match existing component and file naming patterns.
- Do not add a new dependency unless the existing stack cannot solve the problem.

## Verification

Before calling work finished, run:

1. `pnpm test`
2. `pnpm typecheck`
3. `pnpm lint`

If a command fails, fix the issue and rerun it.
```

给人看的入职说明、截图和贡献者背景留在 `README.md`。把 Droid 专用的命令、护栏和完成标准放进 `AGENTS.md`。

## 该放什么

| 小节 | 写好了是什么样 |
|---|---|
| 项目概览 | 一段短文，说明产品、架构或这个包。 |
| 命令 | 确切的安装、本地运行、测试、lint、类型检查、构建和重新生成命令。 |
| 仓库地图 | Droid 在修改之前必须理解的目录。 |
| 约定 | 从代码里看不出来的、本项目特有的模式。 |
| 测试规则 | 聚焦的测试命令、完整门禁命令，以及何时要加测试。 |
| 生成文件 | 哪些文件是生成的、该改哪份源、如何重新生成。 |
| 安全规则 | 密钥处理、生产边界、审批规则，以及迁移的安全性。 |
| PR 预期 | 必须提供的证据、截图、changelog 说明或审查检查。 |

优先写会改变 Droid 做法的具体规则：

```markdown
## Testing

- Run `pnpm test -- path/to/file.test.ts` for focused changes.
- Run `pnpm test` before completing broad refactors.
- Add a regression test for every bug fix when practical.
```

避免无法核对的空话：

```markdown
## Testing

- Be careful.
- Make sure everything works.
```

## 选对指令落点

用这项工作所需要的、最窄的那一层持久表面。

| 表面 | 用来放 | Droid 如何对待它 |
|---|---|---|
| `AGENTS.md` 及兼容文件名 | 始终开启的编码指令、命令、仓库约定和安全规则。 | 在启动时以及动态发现期间作为编码指南加载。 |
| `DESIGN.md`、`Design.md`、`design.md` | 始终开启的设计系统、UX、视觉和交互指导。 | 单独作为设计指南加载。 |
| `SKILL.md` | 只在相关时才应加载的可复用工作流、清单或领域知识。 | 作为 skill 被发现。完整正文在被调用时加载。 |
| `.factory/commands/*` | 用户主动调用的简单提示或可执行快捷方式。 | 暴露为自定义 slash 命令。 |
| `.factory/settings.json` | Droid 的偏好、默认值和策略设置。 | 当作配置解析，而不是散文指令。 |

不要把长篇操作手册粘进 `AGENTS.md`。链到事实来源，或把可复用流程挪到 [skills](https://docs.factory.com/docs/harness/skills)，让额外上下文只在需要时加载。

## 发现与优先级

有 git 根目录时，Droid 从当前工作目录向上搜到 git 根。每一层它都会检查该目录本身，以及这些上下文目录：

| 上下文目录 | 常见用途 |
|---|---|
| `.factory/` | Factory 专用的项目指令。 |
| `.agents/` | 兼容共享的 agent 文件夹约定。 |
| `.agent/` | 兼容单数形式的 agent 文件夹约定。 |

Droid 也会检查家目录里的个人指令目录：

| 个人目录 | 常见用途 |
|---|---|
| `~/.factory/` | 你在各个项目上的默认 Droid 偏好。 |
| `~/.agents/` | 兼容的个人指令。 |
| `~/.agent/` | 兼容的个人指令。 |

多份指令文件同时适用时，用这个心智模型：

- 当前的用户请求优先于常驻指令。
- 嵌套的项目文件为某一棵目录树细化根项目文件。
- 项目文件应当覆盖个人默认值。
- 个人文件应当描述偏好，而不是和仓库规则对着干的要求。

## 兼容的文件名

新的指导用 `AGENTS.md`。Droid 也会读兼容文件名，这样其他编码工具里已有的指令文件还能继续工作。

| 文件名 | 什么时候用 |
|---|---|
| `AGENTS.md` | 新的项目指导推荐用这个。 |
| `agents.md` | 全小写的兼容变体。 |
| `Agents.md` | 首字母大写的兼容变体。 |
| `CLAUDE.md` | 兼容已有的、面向 Claude 的指令。 |
| `Claude.md` | 首字母大写的兼容变体。 |

这是一组兼容名，不是一份安装清单。不要每个文件都建一份。把规则复制到所有受支持的文件名上，只会花掉上下文，并不增加信号。

## 嵌套指令

当一棵目录树有不同的命令、约定、生成产物或所有权规则时，嵌套文件就有用。

```text
repository/
  AGENTS.md
  apps/
    web/
      AGENTS.md
      src/
        page.tsx
```

如果 Droid 从 `repository/` 开始，它加载根指导。之后当它读到 `apps/web/` 下的文件时，可以发现 `apps/web/AGENTS.md`，并把更具体的指导用到那棵目录树上。

嵌套文件只用于真正的差异：

- 某个包用了另一套包管理器或测试运行器。
- 某个服务有不能手工改的生成代码。
- 某一块前端有别处不适用的设计系统规则。
- 某条部署或迁移路径需要额外审批。

不要用嵌套文件去重复根规则。

## 上下文预算

指令文件计入会话上下文。把每个文件的开头写密，放上 Droid 最需要的规则。

| 加载阶段 | 上限 |
|---|---|
| 初始的 AGENTS 风格指南加载 | 80,000 个字符 |
| 动态的 Read 路径指南发现 | 40,000 个字符 |

这些是上限，不是目标。文件更小通常更好。

## 根模板

```markdown
# Repository guide

## What this project is

One or two sentences describing the product, service, or package.

## Commands

- Install: `REPLACE_ME`
- Run locally: `REPLACE_ME`
- Run tests: `REPLACE_ME`
- Run type checks: `REPLACE_ME`
- Run lint: `REPLACE_ME`
- Build: `REPLACE_ME`

## Project layout

- `REPLACE_ME/` contains ...
- `REPLACE_ME/` contains ...
- `REPLACE_ME/` contains ...

## Conventions

- Match existing patterns before introducing new ones.
- Keep changes scoped to the requested task.
- Prefer existing utilities and dependencies.
- Add or update tests when changing behavior.

## Verification

Before completing work, run the relevant focused checks and then the required project checks:

1. `REPLACE_ME`
2. `REPLACE_ME`
3. `REPLACE_ME`

## Safety

- Do not commit secrets or credentials.
- Do not run destructive commands without explicit approval.
- Do not modify generated files by hand. Regenerate them with `REPLACE_ME`.
```

## 嵌套模板

```markdown
# Subproject guide

This file applies when working inside this directory tree. Follow the root `AGENTS.md` unless this file gives a more specific rule.

## Local commands

- Run this package's tests: `REPLACE_ME`
- Run this package's lint: `REPLACE_ME`
- Regenerate local artifacts: `REPLACE_ME`

## Local conventions

- Use `REPLACE_ME` for ...
- Do not use `REPLACE_ME`; this package uses `REPLACE_ME` instead.
- Keep public exports in `REPLACE_ME`.

## Verification

For changes in this directory tree, run:

1. `REPLACE_ME`
2. `REPLACE_ME`
```

## 要避免什么

不要把 `AGENTS.md` 当成垃圾场。避免：

- 密钥、凭证、私有 token 或私有主机名。
- 把别处已经有的长文档整份拷进来。
- 会和仓库漂移的、过时的目录清单。
- 和项目规则冲突的个人偏好。
- 属于 issue、PR 或 spec 的临时任务笔记。
- 在没有狭窄、明确理由的情况下指示跳过验证。

如果某条指导只对一条工作流有用，把它做成 skill。如果只对项目的一块区域有用，放进嵌套的 `AGENTS.md`。
