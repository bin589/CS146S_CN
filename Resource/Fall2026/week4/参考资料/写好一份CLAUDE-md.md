# 写好一份 CLAUDE.md

> 作者：[Kyle](https://twitter.com/0xblacklight)（HumanLayer）
> 原文：<https://hlyr.dev/blog/writing-a-good-claude-md>（2025-11-25，不到 10 分钟）
> 英文存档：[Writing a Good CLAUDE.md en.md](./Writing%20a%20Good%20CLAUDE.md%20en.md)
> 抓取时间：2026-10-27
> 译文说明：作者注明本文同样适用于 `AGENTS.md`。代码、路径、配置片段与 URL 不翻译。原文 “expotential” 按 “exponential” 理解后译出，并在对应处注明。非官方译文，版权归原作者所有。

说明：本文同样适用于 `AGENTS.md`，也就是 `CLAUDE.md` 在 OpenCode、Zed、Cursor、Codex 等 agent 与 harness 上的开源对应物。

## 原则：LLM（大体上）是无状态的

LLM 是无状态函数。等到拿来做推理时，权重已经冻结，所以它们不会随着时间学习。模型对你的代码库所知道的全部，就是你放进去的那些 token。

同样，Claude Code 这类编码 agent harness 通常要求你显式管理 agent 的记忆。`CLAUDE.md`（或 `AGENTS.md`）是默认会进入你和 agent 的每一次对话的唯一文件。

这有三个重要推论：

- 每次会话开始时，编码 agent 对你的代码库一无所知。
- 每次开一个会话，都必须把代码库里重要的事情再告诉 agent 一遍。
- `CLAUDE.md` 是做这件事的首选方式。

## CLAUDE.md 是在给 Claude 做代码库入职

既然每次会话开始时 Claude 对代码库一无所知，你就应该用 `CLAUDE.md` 给 Claude 做入职。从高处看，它应该覆盖：

- **WHAT（是什么）：** 告诉 Claude 技术、技术栈、项目结构。给 Claude 一张代码库地图。这在 monorepo 里尤其重要。告诉 Claude 有哪些 app、哪些共享包、每样东西是干什么的，这样它才知道去哪找。
- **WHY（为什么）：** 告诉 Claude 项目的目的，以及仓库里每样东西在做什么。项目各部分的目的和功能是什么？
- **HOW（怎么做）：** 告诉 Claude 它应该如何在这个项目上工作。比如你们用 bun 而不是 node？你要把它真正能干出有意义的工作所需的信息都放进去。Claude 如何验证自己的改动？如何跑测试、类型检查和编译？

但做法很重要。不要试图把 Claude 可能需要跑的每一条命令都塞进 `CLAUDE.md`——你会得到次优的结果。

## Claude 经常忽略 CLAUDE.md

不管你用哪个模型，你都可能注意到 Claude 经常忽略 `CLAUDE.md` 的内容。

你可以自己查：用 `ANTHROPIC_BASE_URL` 在 claude code CLI 和 Anthropic API 之间放一个日志代理。Claude Code 会把下面这段 system reminder 和你的 `CLAUDE.md` 一起注入到给 agent 的用户消息里：

```text
<system-reminder>
      IMPORTANT: this context may or may not be relevant to your tasks.
      You should not respond to this context unless it is highly relevant to your task.
</system-reminder>
```

于是，如果 Claude 判定这些内容和当前任务不太相关，它就会忽略你的 `CLAUDE.md`。文件里那些并不能普遍适用于你交给它的任务的信息越多，它就越可能忽略文件里的指令。

Anthropic 为什么要加这个？很难说死，但可以推测一下。我们见到的大多数 `CLAUDE.md` 里都塞了一堆并不普遍适用的指令。很多用户把这个文件当成给不喜欢的行为打“热修补”的地方，往里追加大量并不普遍适用的指令。

我们只能假设：Claude Code 团队发现，告诉 Claude 忽略那些糟糕指令之后，harness 的实际结果更好。

## 写一份好的 CLAUDE.md

下面是若干建议，依据的是[上下文工程的最佳实践](https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-03-own-your-context-window.md)。

效果因人而异。这些规则并不必然对每种配置都最优。和其他事情一样，你可以打破规则，只要……

- 你明白什么时候、为什么可以打破
- 你有充分的理由这么做

### 指令越少越好

把 Claude 可能要跑的每一条命令，连同代码标准和风格指南，全塞进 `CLAUDE.md`，这种诱惑很大。我们建议不要这么做。

这个题目还没有被极其严格地研究过，但[已有一些研究](https://arxiv.org/pdf/2507.11538)表明：

- 前沿的思考型 LLM 可以比较稳定地遵循大约 150–200 条指令。更小的模型能顾及的指令比大模型少，非思考模型能顾及的比思考模型少。
- 小模型变差的速度要快得多。具体说，随着指令数量增加，小模型的指令遵循表现倾向于指数衰减（原文写的是 “expotential decay”），而更大的前沿思考模型是线性衰减。因此我们不建议用小模型做多步任务或复杂的实现计划。
- LLM 偏向提示词两端的指令：最开头（Claude Code 的系统消息和 `CLAUDE.md`），以及最末尾（最近的用户消息）。
- 指令数量增加时，遵循质量是均匀下降的。也就是说，你给的指令越多，它不是只忽略较新的（“文件更靠下的”）指令，而是开始均匀地忽略所有指令。

我们对 Claude Code harness 的分析表明，它的系统提示里大约有 50 条独立指令。取决于你用的模型，这已经接近 agent 能可靠遵循的指令量的三分之一——而这还没算上 rules、插件、skills 或用户消息。

这意味着你的 `CLAUDE.md` 应该尽可能少放指令——理想情况下只放那些对你的任务普遍适用的。

### 文件长度与适用性

其他条件相同时，如果上下文窗口里装满聚焦、相关的上下文（例子、相关文件、工具调用和工具结果），LLM 在任务上的表现会好于窗口里有大量无关上下文的时候。

既然 `CLAUDE.md` 会进入每一次会话，就应该确保它的内容尽可能普遍适用。

例如，不要放“如何设计一个新的数据库 schema”这类指令——你在做别的无关事情时，它既没用，还会分散模型的注意力。

长度上同样是越少越好。Anthropic 没有官方建议 `CLAUDE.md` 该多长，普遍共识是少于 300 行最好，更短更好。

在 HumanLayer，我们根目录的 `CLAUDE.md` 不到六十行。

### 渐进式披露（Progressive Disclosure）

写出一份简洁、又能覆盖你希望 Claude 知道的一切的 `CLAUDE.md`，可能很难，尤其是大项目。

为此可以用渐进式披露：让 Claude 只在需要时才看到针对某项任务或某个子项目的指令。

不要把构建项目、跑测试、代码约定或其他重要上下文的各种指令全放进 `CLAUDE.md`。我们建议把针对具体任务的指令放在项目某处、文件名自解释的独立 markdown 里。

例如：

```text
agent_docs/
  |- building_the_project.md
  |- running_tests.md
  |- code_conventions.md
  |- service_architecture.md
  |- database_schema.md
  |- service_communication_patterns.md
```

然后在 `CLAUDE.md` 里列出这些文件，各附一句简短说明，并指示 Claude 判断哪些（如果有）相关，在开工前读它们。或者让 Claude 先把想读的文件拿给你批准，再去读。

优先用指针，不要用拷贝。这些文件里尽量不要放代码片段——它们很快会过时。改成用 `file:line` 引用，把 Claude 指到权威上下文。

概念上这和 [Claude Skills](https://code.claude.com/docs/en/skills) 的设计意图很像，只不过 skills 更侧重工具使用，而不是指令。

### Claude（并）不是一台昂贵的 linter

我们最常看到人们放进 `CLAUDE.md` 的，是代码风格指南。永远不要派一个 LLM 去做 linter 的工作。和传统 linter、formatter 相比，LLM 又贵又慢得离谱。只要能用确定性工具，就应该用。

代码风格指南不可避免地会往上下文窗口里加一堆指令和大多无关的代码片段，拉低 LLM 的表现和指令遵循，并吃掉上下文窗口。

LLM 是上下文内的学习者。如果你的代码遵循某一套风格或模式，你会发现：只要让 agent 在代码库里搜几下（或给它一份好的调研文档），它往往会自己跟上既有的代码模式和约定，不必被明确告知。

如果你对此非常坚持，甚至可以设一个 [Claude Code Stop hook](https://code.claude.com/docs/en/hooks#stop)，跑 formatter 和 linter，再把错误交给 Claude 去修。不要让 Claude 自己去找格式问题。

加分项：用一个能自动修复的 linter（我们喜欢 Biome），并仔细调哪些规则可以安全地自动修，以换取最大的（安全）覆盖。

你也可以做一个 [Slash Command](https://code.claude.com/docs/en/slash-commands)，放进代码规范，并把 Claude 指向版本控制里的改动、git status 或类似的东西。这样实现和格式化可以分开处理。两边的结果都会更好。

### 不要用 /init，也不要自动生成 CLAUDE.md

Claude Code，以及其他带 OpenCode 的 harness，都有自动生成 `CLAUDE.md`（或 `AGENTS.md`）的办法。

因为 `CLAUDE.md` 会进入 Claude Code 的每一次会话，它是 harness 上杠杆最高的点之一——用得好是好事，用得差就是坏事。

一行坏代码就是一行坏代码。实现计划里的一行坏内容，有可能制造出很多行坏代码。一份误解了系统如何工作的调研里的一行坏内容，有可能让计划里出现很多坏行，进而再制造更多坏代码。

而 `CLAUDE.md` 影响工作流的每一个阶段，以及它产出的每一件制品。所以我们认为，你应该花时间非常仔细地想清楚放进去的每一行。

## 结论

- `CLAUDE.md` 是用来给 Claude 做代码库入职的。它应该定义项目的 WHY、WHAT 和 HOW。
- 指令越少越好。不该省略必要的指令，但文件里应该只放合理范围内尽可能少的指令。
- 让 `CLAUDE.md` 的内容保持简短，并且普遍适用。
- 使用渐进式披露——不要把你可能希望它知道的全部信息都告诉 Claude。告诉它如何找到重要信息，让它在需要时再找、再用，以免撑大上下文窗口或指令数量。
- Claude 不是 linter。用 linter 和代码格式化工具，并在需要时用 [Hooks](https://code.claude.com/docs/en/hooks) 和 [Slash Commands](https://code.claude.com/docs/en/slash-commands)。
- `CLAUDE.md` 是 harness 上杠杆最高的点，所以不要自动生成它。为了最好的结果，你应该仔细打磨它的内容。
