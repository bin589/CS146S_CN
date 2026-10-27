# OpenSpec —— 面向 Coding Agent 的轻量规格框架

> 来源：<https://openspec.dev/>（官网）与 <https://openspec.dev/docs>（官方文档）
> 仓库：<https://github.com/Fission-AI/OpenSpec>（MIT，v1.14.2，72.1k stars）
> 英文原文：[OpenSpec en.md](./OpenSpec%20en.md)
> 抓取时间：2026-10-22
> 译文说明：`spec / proposal / design / tasks`、`delta spec`、`capability`、`skill`、`command` 等术语保留英文，命令与代码照录。

## 它是什么

> **用于「构建正确的东西」并「正确地构建」的规格框架**

OpenSpec 是一个轻量、可配置的软件规格创建与管理框架。用 OpenSpec，你把想构建的东西写进一份 spec，并在工作演进过程中让团队和 coding agent 始终保持一致。它帮助你打磨需求、验证需求描述的是对的东西，并核对实现是否与之相符。

本质上，OpenSpec 帮你 build the right thing and build it right（构建正确的东西，并正确地构建）。

数据（官网，2026-10）：GitHub **72.1k** stars，**每两秒**就有一份新 spec 被创建，每月超过 **26.5 万**开发者使用，MIT 许可。

## 理念

```text
→ 流动，不僵化
→ 迭代，不瀑布
→ 简单，不复杂
→ 为 brownfield 而生，不只是 greenfield
→ 从个人项目扩展到企业
```

## 团队为什么采用它

当需求只活在聊天记录里时，AI coding assistant 很强大但不可预测。OpenSpec 加了一层轻量 spec，让你在写任何代码之前先就「要构建什么」达成一致。

- **先对齐再构建** —— 人和 AI 在写代码前先对齐 spec
- **保持有序** —— 每个 change 有自己的目录：proposal、specs、design、tasks
- **自由流动** —— 任何产物随时可改，没有僵硬的阶段闸门
- **用你现有的工具** —— 通过 slash command 支持 30+ AI 助手

对比：

| 对比对象 | 权衡 |
|---|---|
| [Spec Kit](https://github.com/github/spec-kit)（GitHub） | 完备但笨重：僵硬的阶段闸门、大量 Markdown、Python 环境配置。OpenSpec 更轻，允许自由迭代。 |
| [Kiro](https://kiro.dev)（AWS） | 强大但把你锁进它的 IDE 和 Claude 模型。OpenSpec 用你已有的工具即可。 |
| 什么都不用 | 模糊的 prompt，不可预测的结果。OpenSpec 带来可预测性，而不增加仪式感。 |

## 安装

需要 **Node.js 20.19.0 或更高**（`node --version`）。全局安装：

```bash
npm install -g @fission-ai/openspec@latest
# 或
brew install openspec
```

用 `openspec --version` 验证。其他安装方式：Deno（`deno install --global ...`）、Nix（`nix profile install github:Fission-AI/OpenSpec`）、bun/pnpm（CLI 仍然需要 PATH 上有 Node）。升级 CLI 用 `npm install -g @fission-ai/openspec@latest`（或 `brew upgrade openspec`），然后在**每个项目里**跑 `openspec update` 刷新生成的 skills 和 commands——它们不会自动更新。

也可以让 agent 帮你装：把 `Fetch https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/install.md and follow it.` 粘进 AI 聊天窗口。

## 项目初始化

```bash
cd your-project
openspec init
```

init 会问你在用哪些 AI 工具，为你选中的工具写工作流文件，并报告结果：

```text
OpenSpec Setup Complete

Created: Claude Code
6 skills and 6 commands in .claude/
Config: openspec/config.yaml (schema: spec-driven)
```

重复跑 init 是安全的：已配置的工具会打印 `Refreshed`，新增工具会追加，`--tools` 可跳过选择器。重启 IDE 让命令生效。

init 创建两样东西：

```text
openspec/
├── config.yaml     项目设置与给 AI 的上下文
├── specs/          你的规格（此时为空）
└── changes/        进行中的变更（此时为空）
    └── archive/    已完成的变更移到这里
```

以及你所用工具目录（`.agents/`、`.claude/` 等）下的工作流文件：

```text
.agents/skills/
├── openspec-explore/              先把一个想法想透
├── openspec-propose/              提出一个变更
├── openspec-apply-change/         实现某个变更的任务
├── openspec-update-change/        修订某个变更的计划
├── openspec-sync-specs/           把变更的 spec 更新同步进 specs/
├── openspec-archive-change/       把完成的变更移到归档
├── openspec-verify-change/        核对实现是否与计划一致（默认不装）
└── openspec-bulk-archive-change/  一次归档多个变更（默认不装）
```

默认情况下每个工作流以两种形态安装：**skill**（`openspec-apply-change`，agent 在你提出工作时自行取用）和 **command**（Claude Code 里的 `/opsx:apply`，同样指令的键入式入口）。部分工具只装 skill 形态。项目更偏好 skill，并预期最终会淘汰 command。

## 工作流

每个变更都走同样的五步：你和 agent 一起把想法想透，它起草计划，你在任何代码存在之前修正计划，agent 据此构建，归档时把实际交付的内容吸收进 specs。

```mermaid
flowchart LR
  explore["1 · Explore<br/>一起把想法想透"] --> propose["2 · Propose<br/>agent 起草计划"]
  propose --> review["3 · Review<br/>你修正计划"]
  review --> apply["4 · Apply<br/>agent 逐任务构建"]
  apply --> archive["5 · Archive<br/>specs 吸收这次变更"]
  archive -. "下一个变更" .-> explore
```

官网对 slash command 表面的概括：

```text
/opsx:explore    梳理问题、理解代码库
/opsx:propose    起草 proposal.md、specs/、design.md、tasks.md
/opsx:apply      按规格实现任务
/opsx:verify     核对实现是否与规格一致
/opsx:archive    归档已完成的变更
```

### 第 1 步：Explore

Explore 是思考模式。agent 调研你的代码库、问关键问题、勾勒选项、挑战假设。它从不写代码。输出是一个更锐利的想法。

```text
Help me explore how rate limiting should work in this app.
```

当形状对了，用 `Propose the change we just discussed.` 交接过去。

### 第 2 步：Propose

Propose 把想法变成一个可评审的计划，并且就停在那里——还没有代码。

```text
Propose a change to add rate limiting.
```

```text
openspec/changes/add-rate-limiting/
├── proposal.md    为什么做，以及改什么
├── specs/         「做完」意味着什么，写成可测的需求
├── design.md      技术决策（只有变更需要时才生成）
└── tasks.md       实现清单
```

### 第 3 步：评审并修正计划

趁计划还只是文字时修好它。按这个顺序读：

- **`proposal.md`**：问题选对了吗？规模对吗？
- **`specs/`**：价值最高的阅读。这些需求你愿意接受为「已完成」吗？
- **`tasks.md`**：任务覆盖了 specs 吗，且没有多余的吗？

两种修法都行：自己改 Markdown 文件，或告诉 agent 哪里不对（「spec 漏了未认证的情况」）。

### 第 4 步：Apply

开一个全新的聊天会话，因为实现更适合在干净的上下文窗口上进行。

```text
Apply the add-rate-limiting change.
```

agent 顺着 `tasks.md` 逐条实现，落地一条就勾一条。中断了或者上下文用完了？在新会话里重新要求 apply，它会从第一个未勾选的任务继续。进度就在复选框里——没有隐藏状态。

### 第 5 步：Archive

归档做两件事：把变更的需求合并进主 specs，并把 change 目录移进 `openspec/changes/archive/`，加日期前缀。什么都不删除。

```text
Archive the add-rate-limiting change.
```

```text
# 之前
openspec/
├── specs/                                   （还没有 rate-limiting spec）
└── changes/add-rate-limiting/{proposal.md,tasks.md,specs/rate-limiting/spec.md}

# 之后
openspec/
├── specs/rate-limiting/spec.md              系统构建完成后的 spec
└── changes/archive/2026-08-08-add-rate-limiting/...
```

`changes/` 清空以迎接下一个变更；`specs/` 是「系统做什么」的唯一真相；`archive/` 是「它是怎么走到那里的」历史。Git 是另一件事：把 change 目录和代码一起提交。

## 默认 `spec-driven` schema 的产物

| 产物 | 文件 | 用途 |
|---|---|---|
| `proposal` | `proposal.md` | 为什么需要这个变更 |
| `specs` | `specs/<capability-path>/spec.md`，每个 capability 一份 | 哪些行为改变 |
| `design` | `design.md` | 怎么构建 |
| `tasks` | `tasks.md` | 实现清单 |

起草顺序：

```text
             ┌─ specs ──┐
proposal ────┤          ├── tasks ── apply
             └─ design ─┘
```

proposal 最先。specs 和 design 顺序可换，tasks 需要两者。`design` 在下列条件都不成立时才跳过：跨切面变更、新依赖或数据模型变化、安全/性能/迁移复杂度、值得在写码前解决的歧义。只有变更的 `.openspec.yaml` 里设置 `skip_specs: true` 才跳过 `specs`——而 `openspec validate` 会拒绝零 delta 且没有该标记的变更，所以别为了通过校验去编造需求。

spec 是行为契约，不是实现计划。要写可观测行为、输入输出、错误条件、外部约束、可测场景；不要写内部类名、库选择或逐步实现步骤。快速检验：**如果实现可以改变而不改变外部可见行为，它多半不该出现在 spec 里。**

Delta spec 的形状：

```markdown
# Spec Delta

## Purpose
<!-- 仅新 capability：一两句话说明这个 capability 是干什么的 -->

## ADDED Requirements

### Requirement: User can export data
The system SHALL allow users to export their data in CSV format.

#### Scenario: Successful export
- **WHEN** user clicks "Export" button
- **THEN** system downloads a CSV file with all user data
```

delta 操作有 `## ADDED Requirements`、`## MODIFIED Requirements`（必须给完整更新内容，标题与原文精确匹配）、`## REMOVED Requirements`（必须带 **Reason** 和 **Migration**）、`## RENAMED Requirements`（FROM:/TO: 格式）。规范需求用 SHALL/MUST；每条需求至少一个场景；场景必须正好用四个井号（`####`）——三个或项目符号会静默失败。

`tasks.md` 会被解析以追踪进度：只含 `x` 的方框算完成；其他任何标记（`- [~]`、`- [-]`、`- []`）都算未完成。每个任务必须写明如何验证完成；每个任务组必须交付自身工作所需的测试与文档——不要把测试集中到最后一组，否则失败会沿着中间的每一组级联回来。

## Profiles 与定制

默认 `core` profile 安装六个工作流，覆盖整个闭环：`explore`、`propose`、`apply`、`update`、`sync`、`archive`。另有六个可选——`new`、`continue`、`ff`（逐件创建产物，而不是一次全出）、`verify`、`bulk-archive`、`onboard`。用 `openspec config profile` 改集合；任何不正好是 core 六件的选择都会存为 `custom`。

交付形态与工作流集合是分开的：`both`（默认）、`skills` 或 `commands`。

```bash
openspec config set delivery skills   # 或：both、commands
```

定制分两层：

| 选项 | 改什么 | 什么时候用 |
|---|---|---|
| Profiles | 装哪些工作流，以及装成 skill、command 还是两者 | 想要额外工作流，或删掉用不上的 |
| 项目配置（`config.yaml`） | 注入每次工作流运行的指令：上下文、规则、操作指引 | 想让变更按你的方式来规划，比如 tasks 永远包含 Playwright 测试 |
| Schemas | OpenSpec 产出什么：产物、顺序、模板 | 变更应该产出不同的规划文件、章节或格式 |

config 只能在核心工作流之上做加法：它能加「tasks 永远包含测试」，但不能删掉 `design.md` 或给文件改名。那是 schema 的地盘（`openspec schema fork`）。

## Stores（beta）

面向多仓库场景，**Stores** 把规划放进一个独立仓库——还是同样的 `openspec/` 形状（specs 与 changes），像其他东西一样用 `git push` 共享。一个全团队和每个 coding agent 都能读的唯一真相，跨所有仓库。

- **跨仓库特性** —— 一个变更、一个计划，即使代码落在三个仓库。
- **共享需求** —— 平台团队拥有 specs；产品团队只读引用。
- **先计划后代码** —— 现在就把计划记进 store；代码仓库之后再跟上。

## 使用建议

- **模型选择**：OpenSpec 最适合高推理模型。项目推荐 planning 和 implementation 都用 Codex 5.5 与 Opus 4.7。
- **上下文卫生**：OpenSpec 受益于干净的上下文窗口。开始实现前清空上下文（这正是本周另一篇阅读《上下文税》的论点）。
- **遥测**：只收集匿名的命令名与版本；不含参数、路径、内容或 PII。用 `openspec config set telemetry.enabled false`、`OPENSPEC_TELEMETRY=0` 或 `DO_NOT_TRACK=1` 关闭。

## 支持的工具

Claude Code、Codex、Cursor、GitHub Copilot、Gemini CLI、OpenCode、Amazon Q Developer、Antigravity、Auggie、IBM Bob、Shell、Cline、Command Code、CodeArts、CodeBuddy、Devin Desktop、ForgeCode、Continue、CoStrict、Crush、Factory Droid、Hermes Agent、iFlow、Junie、Kilo Code、Kimi Code、Kiro、Lingma、MiniMax Code、Mistral Vibe、Oh My Pi、Pi、SourceCraft、Qoder、Qwen Code、Rovo Dev CLI、Zoo Code、Trae、Zed Agent、ZCode，以及另外 33 个。

`/opsx:propose` 是规范名；你的工具可能写成 `/opsx-propose`（Cursor、GitHub Copilot）、`@opsx-propose`（Amazon Q）或 `$openspec-propose`（Codex）。`openspec init` 会打印你所选工具的正确形式。

## 来源

- <https://openspec.dev/> —— 首页、数据、工作流概要、兼容列表
- <https://openspec.dev/docs/installation> —— 安装/更新/卸载
- <https://openspec.dev/docs/setup> —— `openspec init`、目录布局、skills vs commands
- <https://openspec.dev/docs/quickstart> —— 五步闭环详解
- <https://openspec.dev/docs/profiles> —— core 集合、可选工作流、交付形态
- <https://openspec.dev/docs/customize> —— profiles vs config vs schemas
- <https://openspec.dev/docs/schemas/spec-driven> —— 产物、模板、apply 契约
- <https://github.com/Fission-AI/OpenSpec> —— README、理念、对比、stores
