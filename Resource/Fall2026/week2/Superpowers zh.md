# Superpowers —— 给 Coding Agent 的一套完整软件开发方法论

> 作者：Jesse Vincent 与 [Prime Radiant](https://primeradiant.com) 团队
> 仓库：<https://github.com/obra/superpowers>（MIT）
> 原文：<https://raw.githubusercontent.com/obra/superpowers/main/README.md>
> 英文原文：[Superpowers en.md](./Superpowers%20en.md)
> 发布说明：<https://blog.fsck.com/2025/10/09/superpowers/>
> 抓取时间：2026-10-22
> 译文说明：`skill`、`subagent`、`TDD`、`worktree`、`RED-GREEN-REFACTOR` 等术语保留英文，安装命令照录。

Superpowers 是一套完整的软件开发方法论，为你的 coding agent 而建，建立在一组可组合的 skills 之上，外加一段初始指令，确保 agent 真的会用它们。

## 它是怎么工作的

从你启动 coding agent 的那一刻就开始了。它一旦看到你在构建什么，**不会**直接扑上去写代码。相反，它退后一步，问清楚你到底想做什么。

等它从对话里把 spec 梳理出来，会以短到真正能读进去、能消化的分块展示给你。

你对设计点头之后，agent 会整理出一份实现计划，清晰到「一个热情但品味差、没判断力、没有项目上下文、还讨厌测试的初级工程师」都能照着做。它强调真正的 red/green TDD、YAGNI（You Aren't Gonna Need It）和 DRY。

接下来，你说「go」，它就启动 **subagent-driven-development** 流程：让 agent 逐个工程任务推进，检查并评审它们的工作，然后继续向前。你的 agent 连续自主工作几个小时而不偏离你们一起制定的计划，这并不罕见。

细节还有很多，但这就是系统的核心。而且因为 skills 会自动触发，你不需要做任何特别的事。你的 coding agent 就是有 Superpowers。

## 安装

安装方式因 harness 而异。如果你用多个，需要分别安装。

### Claude Code

可通过 [Claude 官方插件市场](https://claude.com/plugins/superpowers) 安装：

```bash
/plugin install superpowers@claude-plugins-official
```

或通过 Superpowers 市场：

```bash
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

### Codex

通过 [Codex 官方插件市场](https://github.com/openai/plugins) 提供。Codex app 里点击侧边栏 **Plugins**，在 Coding 区找到 `Superpowers`，点 `+`。Codex CLI 里打开 `/plugins`，搜索 `superpowers`，选择 `Install Plugin`。

### Cursor

```text
/add-plugin superpowers
```

或在插件市场里搜索 "superpowers"。

### Antigravity

```bash
agy plugin install https://github.com/obra/superpowers
```

Antigravity 会列出每个已安装 skill 的描述，而 `using-superpowers` 这个 skill 的描述会提示模型在对话开始时加载它。用同一命令重装即可更新。

### Gemini CLI

```bash
gemini extensions install https://github.com/obra/superpowers
gemini extensions update superpowers
```

### GitHub Copilot CLI

```bash
copilot plugin marketplace add obra/superpowers-marketplace
copilot plugin install superpowers@superpowers-marketplace
```

### Factory Droid

```bash
droid plugin marketplace add https://github.com/obra/superpowers
droid plugin install superpowers@superpowers
```

### Devin CLI

```bash
devin plugins install obra/superpowers
devin plugins update superpowers
```

### Grok Build CLI

```bash
grok plugin install superpowers@xai-official --trust
```

或在 TUI 里打开 `/marketplace`，搜索 Superpowers 并安装。

### Kimi Code

打开 `/plugins`，进入 `Marketplace` > `Superpowers` 安装，或直接：

```text
/plugins install https://github.com/obra/superpowers
```

详细文档：[docs/README.kimi.md](docs/README.kimi.md)。

### OpenCode

OpenCode 用自己的插件安装机制；即使你在别的 harness 里已经装了 Superpowers，也要单独再装：

```text
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md
```

详细文档：[docs/README.opencode.md](docs/README.opencode.md)。

### Pi

```bash
pi install git:github.com/obra/superpowers
```

Pi 包会加载 Superpowers skills，以及一个小扩展：在会话启动时、以及压缩之后再次注入 `using-superpowers` 引导。Pi 原生支持 skills，所以不需要兼容用的 `Skill` 工具。

### Qwen Code

```bash
qwen extensions install obra/superpowers
qwen extensions update superpowers
```

### Hermes Agent

```bash
hermes plugins install obra/superpowers --enable
```

安装后重启活跃的 Hermes 会话。注意：Hermes 没有压缩后钩子，所以一个极长、在首轮之后就发生压缩的会话会丢失引导——如果 skills 不再触发，开一个新会话。

### Muse

```bash
muse plugins install ./
muse plugins approve superpowers
# 或
git clone https://github.com/obra/superpowers.git
muse plugins install ./superpowers
muse plugins approve superpowers
```

版本记录在 `.version-bump.json` 里，由 `scripts/bump-version.sh` 保持同步。

## 基本工作流

1. **brainstorming** —— 在构建任何东西之前激活。通过提问让你描述出你真正想要什么、为什么，然后复述它的理解请你纠正。小改动在聊天里达成一致；项目会产出一份构建者能据此规划的书面设计文档。

2. **using-git-worktrees** —— 设计获批后激活。在新分支上创建隔离工作区，运行项目初始化，验证干净的测试基线。

3. **writing-plans** —— 有获批设计后激活。把工作拆成小到一口能吃掉的任务（每个 2–5 分钟）。每个任务都有精确文件路径、完整代码、验证步骤。

4. **subagent-driven-development** 或 **executing-plans** —— 有计划后激活。前者每个任务派一个新的 subagent，每个任务后评审一次（最彻底）；后者在当前会话里内联实现所有任务，最后对整个分支做一次新评审（最省）。

5. **test-driven-development** —— 实现期间激活。强制 RED-GREEN-REFACTOR：先写失败测试，看它失败，写最小代码，看它通过，提交。删除在测试之前写的代码。

6. **requesting-code-review** —— 任务之间激活。对照计划评审，按严重度报告问题。严重问题会阻塞进度。

7. **finishing-a-development-branch** —— 任务完成时激活。验证测试，给出选项（合并/PR/保留/丢弃），清理 worktree。

**agent 在任何任务之前都会检查相关 skills。** 这是强制工作流，不是建议。

## 出问题时

有时一个会话会不听话：skill 在不该触发时触发、该说话时沉默，或者 agent 无视自己的计划、重复劳动、烧掉超出预期的 tokens。让你的 coding agent「figure out what went wrong with superpowers in this session」，它就会调用 **diagnosing-superpowers** skill。要检查更早的会话，点名它：「figure out what went wrong with superpowers in session `<id>`」。

这个 skill 读取会话 transcript，带行级证据报告发生了什么，并且（如果你需要）打包一个脱敏 bundle 用于报 bug。

## 里面有什么

### Skills 库

**测试**
- **test-driven-development** —— RED-GREEN-REFACTOR 循环（含测试反模式参考）

**调试**
- **systematic-debugging** —— 四阶段根因流程（含 root-cause-tracing、defense-in-depth、condition-based-waiting 技巧）
- **verification-before-completion** —— 确保真的修好了
- **diagnosing-superpowers** —— 带证据定位会话中出了什么问题；导出脱敏 bundle 或提 issue

**协作**
- **brainstorming** —— 构建前把意图挖出来
- **writing-plans** —— 详细实现计划
- **executing-plans** —— 内联执行计划：一个上下文，最后一次评审
- **dispatching-parallel-agents** —— 并发 subagent 工作流
- **requesting-code-review** —— 评审前检查清单
- **receiving-code-review** —— 如何回应反馈
- **using-git-worktrees** —— 并行开发分支
- **finishing-a-development-branch** —— 合并/PR 决策流程
- **subagent-driven-development** —— 带两阶段评审的快速迭代（先 spec 合规，再代码质量）

**元**
- **writing-skills** —— 按最佳实践创建新 skill（含测试方法论）
- **using-superpowers** —— skills 系统入门

## 理念

- **测试驱动开发** —— 永远先写测试
- **系统化胜于临时应付** —— 用流程，不靠猜
- **降低复杂度** —— 简单是首要目标
- **证据胜于声明** —— 宣布成功之前先验证

## 贡献

我们一般**不**接受新增 skill 的贡献；对 skill 的任何修改都必须在我们支持的所有 coding agent 上工作。我们也不接受 agent 代写的、用来修复别人所提 issue 的 PR，除非维护者主动邀请，即使你也撞上了同样的问题——请把报告追加到已有 issue。

1. Fork 仓库
2. 切到 `dev` 分支
3. 为你的工作建分支
4. 按 `writing-skills` skill 创建并测试新的或修改的 skill
5. 提交 PR，填满 PR 模板的每一节，包括由人用自己的话写的总结

Skill 行为测试用 [superpowers-evals](https://github.com/prime-radiant-inc/superpowers-evals/) 里的 drill eval harness，克隆到 `evals/`；插件基础设施测试在 `tests/`，通过相应的 `run-*.sh` 或 `npm test` 运行。

## 遥测

skills 和插件不会给作者任何反馈，所以默认情况下，brainstorming 可选的可视化伴侣功能上的 Prime Radiant logo 会从项目网站加载，并带上正在使用的 Superpowers 版本。它不包含你的项目、prompt 或 coding agent 的任何细节。用 `SUPERPOWERS_DISABLE_TELEMETRY` 关闭；Superpowers 也尊重 Claude Code 的 `DISABLE_TELEMETRY` 和 `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` 退出开关。

## 商业服务

如果企业使用需要商业支持、额外工具或托管支出：sales@primeradiant.com。

## 社区

- Discord：<https://discord.gg/35wsABTejz>
- Issues：<https://github.com/obra/superpowers/issues>
- 版本公告：<https://primeradiant.com/superpowers/>

## 许可

MIT License —— 见 LICENSE 文件。
