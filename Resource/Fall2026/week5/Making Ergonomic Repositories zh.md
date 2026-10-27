# 让我们的 Monorepo 对 Agent 更顺手

> 课程阅读标题：Making Ergonomic Repositories
> 原文：<https://x.com/trybasis/status/2056881705269580023>
> 英文存档：[Making Ergonomic Repositories en.md](./Making%20Ergonomic%20Repositories%20en.md)
> 作者：Basis（[@trybasis](https://x.com/trybasis)）；文末署名 Michael Crabtree（Atlas Tech Lead）、@RyanBMoffat、@BhavdeepSethi、@SethSchiesel
> 发布时间：2026-05-19
> 抓取时间：2026-10-27
> 译文说明：帖子公开 HTML 只有 Open Graph 标题；正文来自同一 status 的公开 FxTwitter 聚合，不是课堂转写。三张原图未下载，位置照英文存档注明。代码块不翻译。非官方译文，版权归原作者所有。

## 我们如何用可验证、可互操作和权威上下文这几条原则，做出一个 agent 原生的代码库

在 Basis，我们被这个问题缠住：怎样让代码库对 agent 更顺手？软件工程里关于“对人类而言设计良好的代码库”已经有几十年的经验（小函数、划定的模块、不要臃肿的文档，等等）。这些经验要怎样为 agent 演化？

负责内部 agent 和上下文的是 [Basis 的 Atlas 团队](https://www.getbasis.ai/blogs/building-a-company-for-the-agi-era)。我们的产品就是代码库本身。代码库同时是两样东西：它是跑在生产里的源代码，也是编码 agent 用来做决定的上下文。所以要让产品对我们的用户真正友好，我们必须把 monorepo 做得尽可能 agent 原生、尽可能顺手。

我们做到了。三个月里，每位开发者的 token 用量增加了 5 倍以上，提交速度增加了 2.5 倍。

## 我们的设想

Basis 把核心赌注押在智能上。从三年前 Basis 一开始，我们就相信大部分代码很快会由 agent 来写，并据此建公司。大约九个月前，我们到了那个智能水平。

到那一刻，很容易想象这样一个世界：agent 稳定地交付高质量、测试充分的代码，工程师则专注于真正做工程决策这件难事。

但我们当时还没到。编码 agent 单独看是有能力的，一旦被丢进一个没有配套基础设施的正在工作的代码库，就容易出错。

这不是新问题；任何一个新员工也是这样。像 Basis 这样长得快的公司，每个月可能要入职多名工程师，所以让代码库容易学，一直都很重要。但和人不一样，agent 必须在每一条轨迹上重新“入职”代码库。随着我们采用编码 agent，Basis 的“入职”突然从一个月几次变成一个月几千次。以这个速率，任何小的不一致、矛盾和缺口都会很快复利，而以前它们可能根本不会被注意到。

## Agent 原生代码库的原则

*[原图略：X Article 中的图片，未下载。]*

赋能编码 agent 的主要杠杆是上下文和工具。为了走到“agent 运用自如”的终态，我们定了五条原则来指导这些杠杆的建设。

1. **权威性（Canonicality）。** 仓库里的每一件制品，要么是关于系统今天如何运作的事实来源，要么是意图和历史的记录。它永远不能两者兼是。读你代码库的 agent 需要一张明确的地图：什么该被信任为对现实的描述，什么该被读成计划、假设或记忆。
2. **就近（Localization）。** 上下文应当尽可能活在它被使用的地方附近。只有当它变得更普遍适用时，才向上移动。这降低 agent 错过相关上下文的可能。
3. **可验证（Verifiability）。** Agent 需要对自己的工作做验证。我们建了机制来强制这一点，包括 sub-agent 角色、pre-commit hooks 和测试。
4. **可互操作（Interoperability）。** 架构的任何一层都不把团队绑死在单一供应商上。AI 技术走得太快，不能押在一个平台上。在 AI 发展这么早的阶段锁进一家供应商，有错过后面巨大收益的风险。
5. **默认不要（Default-no）。** 任何被自动加载的上下文都必须被仔细审视。挣不到行为的 token，是每一次会话都要交的税，由每个 agent 和每个工程师支付。用否定式来陈述是故意的。默认是“包含”时，被加载的文件会膨胀；默认是“排除”时，每一行都得挣到自己的位置。

我们建的架构，就是这些原则在代码里的实现。

## 权威 vs 非权威

应用这些原则的第一步，是把已有上下文分成权威和非权威两类。这是一个严格的过程，迫使团队从代码库各处收集、整理很多种信息，再通过激烈讨论把它们对齐。在这个对齐过程中，我们把做法写进一份文档标准，把仓库里每种制品类型映射到一个权威级别。

权威材料是编码 agent 应当当作“系统今天如何工作”的事实来源的东西。它包括根目录和嵌套的 `AGENTS.md`、skills、`docs/` 目录，以及行内代码注释和 docstring。这些制品说的是：“这是当前状态，以及我们在其中如何工作。”

非权威是有用的上下文，但不是关于当前代码库的事实来源。它包括计划和规格（`.specs/` 和 Linear），以及历史理由（`.notes/`）。

两类都有价值。可能犯的错是把非权威当成权威。一张 Linear 工单可能描述一个从未实现的功能，或实现得和计划不一样。如果 agent 读了那张工单并把它当成真相，它会对世界的正确状态感到困惑。明确标出什么是权威、什么不是，就给了 agent 一套更细致的本体。

这可能引出一个问题：“为什么还允许 agent 看见非权威信息？”答案是，在解析复杂情境时，非权威信息仍然可以极其有价值。Agent 需要一种办法回到历史上的某个具体时刻，回答“我们为什么把这段代码写成这样？”在 agent 之前的世界里，答案是给写那个 commit 的人发一条 Slack 私信。现在答案是 `.notes/`。

例如，当我们的[事故响应 agent Clueso](https://www.getbasis.ai/blogs/clueso-how-we-built-an-agent-that-autonomously-resolves-78-of-bugs) 在调试一份用户报告时，非权威上下文帮助 Clueso 判断这是 bug 还是特性。规格告诉 Clueso 最新的预期行为，笔记则指出原作者考虑过的重要边界情况。

完整映射作为 Authority Map 发布在下面。

*[原图略：原文中的 Authority Map 图片，未下载。]*

## 六层架构

*[原图略：原文中的六层架构图，未下载。]*

Authority Map 给了我们一套干净的六层架构。

**第 1 层：根 `AGENTS.md`。** 我们的工程原则、工作流定义和沟通模式。每次会话都加载。目前大约 300 行。这是仓库里杠杆最高的文件：每个 token 每次都会被每个 agent 看到。对 Claude 用户，我们只是把 `AGENTS.md` 做成符号链接。

**第 2 层：嵌套的 `AGENTS.md`。** monorepo 里有 100 多个，每个限定在自己的目录。后端的 `AGENTS.md` 规定导入约定、并发模式和依赖规则。每个文件都窄，并且是操作性的。

示例：

```markdown
### Imports
All Python imports go at the top of the file.
- Strongly avoid inline/deferred imports to work around circular imports.
A circular import means the module structure is wrong--fix the structure
instead.
- Only acceptable reason for a non-top-level import: the imported module
has expensive load-time side effects and the calling code path is
rarely executed.
```

**第 3 层：Skills。** `.agents/skills/` 目录包含覆盖后端架构、前端模式、测试标准、文档约定，以及产品领域知识的 skill 包。

**第 4 层：Sub-agent 角色。** `.agents/roles/` 目录定义了六个以上的专门 agent，每个有自己的上下文窗口。verifier 跑限定在 diff 上的测试和 pre-commit hooks，然后带可操作的失败细节报告通过／失败。standards-enforcer 对照所有适用的 `AGENTS.md` 和 skills 校验代码，检查过度防御式编程、死代码和缺失的测试覆盖。

```markdown
# verifier.md (frontmatter)
---
id: verifier
name: verifier
description: Runs diff-scoped tests, pre-commit hooks, and relevant lint/type checks, then reports pass/fail status with actionable failure details.
codex_agent_key: verifier
codex_model: gpt-5.5
codex_model_reasoning_effort: low
codex_model_verbosity: low
---
```

**第 5 层：统一的 MCP。** 我们的统一 MCP server 让 agent 能访问外部系统：Linear 提供项目上下文，Slack 提供团队沟通，Better Stack 提供日志，PostHog 提供分析，开发数据库用于验证。调查 bug 的 agent 可以拉相关的 Linear 工单、查生产日志、查询数据库，而不需要工程师把上下文手工拷进提示里。

**第 6 层：测试。** 在进入 CI 之前抓住违反标准的自动化强制。Python 的 lint 和格式用 Ruff，类型检查用 BasedPyright，TypeScript 用 ESLint 和 Prettier，再加上对大文件、私钥和合并冲突的检测。这些 hooks 是最后一道防线；即使 agent（或人）忘了遵守，它们也会强制标准。

## 重写 AGENTS.md

仓库里有很多在我们把原则写成条文之前就写好的 `AGENTS.md`。我们找到大约 20 份，状况很糟。下面是这些 `AGENTS.md` 里最常见的三个问题。

第一，很多文件是在向 agent 描述代码库，而不是在指示它们。例如有一份 `AGENTS.md` 说：“SRC 是我们放所有源代码的地方。”当然，agent 已经知道 `src/` 文件夹是什么；它是在几十万个有这个约定的仓库上训练出来的。

对比一条这样的指令：“使用严格的类型检查”，或“绝不要用内联导入去绕过循环依赖；改掉模块结构”。这些操作性指令会改变 agent 的行为。它们告诉 agent 我们期望它如何工作。

第二，当我们的 `AGENTS.md` 确实包含指令时，它们往往全是高优先级的、“必须遵守”的指令。你用很重的措辞告诉 agent 一切都很重要，结果就是没有什么是重要的。打磨规则时比较难的一部分，是把准确的优先级感稳定地写进行文。默认不要和就近这两条原则在这里帮了我们。去掉不必要的强调，把指令放在它们适用的地方，才得到我们想要的 agent 行为。

第三，我们还需要组织那些跨文件夹、在多种情境下都适用的信息。例如，关于 Tasks 产品细节的知识，不能只正确地住在后端的 `AGENTS.md` 里。前端业务逻辑也需要这份知识。我们把跨文件夹的知识放进 agent 可以按需加载的 skills。起初我们用 `/docs` 文件夹，后来改掉，是为了利用这些模型都经过后训练、能有效加载 skills 这一点。（现在的 docs 是明确给人看的材料。）

我们为 `AGENTS.md` 定了五条写作规则，每一条都是那些原则的推论：

1. **指令质量。** 写给 agent，而不是写给人。`AGENTS.md` 的目标应当是向 agent 解释如何操作。它们不应当变成给人看的永久文档。
2. **层级优先的放置。** 把上下文放在完全拥有它的、最具体的那个目录。信息只有在真正被共享时才向上移动。
3. **耐用的引用。** 用描述性名称，而不是精确的文件路径。路径会变；描述是稳定的。
4. **纯文本、便于搜索的内容。** 不要 ASCII 艺术，不要二进制内容，不要干扰搜索或解析的格式。
5. **默认不要。** agent 在这个目录里的大多数任务是否合理地需要这条信息？如果不需要，它属于别处。

团队重写了大约 20 个文件夹里的 `AGENTS.md`，把情境知识迁到 skills，用操作性指令替换描述性内容。重写后留下来的例子：

- 权威上下文是你可以信任、用来做决定的事实来源。非权威上下文表示意图、笔记、临时状态等。
- 优先用提前返回，而不是深层嵌套。
- 写出不引用其他文件也能看懂的代码。要明确，不要耍聪明。

这些会载入整个 monorepo 的每一次 agent 会话。它们是我们希望无论 agent 在哪里工作都被遵守的指令。根 `AGENTS.md` 目前大约 300 行，每一行都被争论过。

## 清理

指令层重建、架构就位之后，我们终于转向代码库本身。Ryan Moffat 用编码 agent 对照新写成条文的指令审计每个目录，产出一份九个项目、数千行违规的清单。

然后我们部署 agent 去修那些由 agent 延续下来的问题。一直在吸收坏模式的 agent，现在拿到明确的、结构良好的指令，按新标准重写代码。

这次重写触及九个已完成项目里估计 20% 到 30% 的整个代码库。原则告诉我们杠在哪里；清理是把现有代码抬到那根杠上、让它可以充当权威的成本。没有捷径。一个 agent 原生的代码库比只有人的代码库要求更多局部正确性，因为每个文件都是上下文，而 agent 在不断地入职。

用 agent 做重构会碰到自然的极限。技术债常常有结构性原因，agent 解决不了。我们优先处理 agent 能修的、最常被看见的那部分代码库。然后优先处理需要人介入的可见区域。其余的留给正常流程去清理。

## 维持权威上下文

任何人看到我们的架构，第一个问题都是：“你们怎么让这些东西不腐烂？”

维护从所有者开始。Basis 的每一件权威制品，都在文件顶部的 YAML frontmatter 里带一个明确的 owner 字段。一项 CI/CD 检查确保任何新的 skill 或非生产 markdown 文件都有对应的所有者。当我们的自动上下文清理系统标出什么东西时，由所有者负责审阅。

我们有一组审查 monorepo 的云端 agent 自动化。这就是我们所说的 Automatic Context 系统。其中三项自动化直接针对上下文：

- 一项 CI/CD 检查确保合并符合我们的确定性标准：frontmatter 已校验、操作性指令所在之处是描述性散文、语法正确。
- 一个扫描器每天做一次大扫除，检查 skills 和 `AGENTS.md` 是否过时、互相矛盾、指令重复、引用损坏，以及近期改动是否缺上下文。
- 工人每天领取扫描器开出的工单，并实现小而范围明确的修复。

更广的一点是：自动维护上下文之所以可能，是因为我们先同意了什么是权威。扫描器可以扫 `AGENTS.md` 和 skills 找矛盾，是因为权威上下文按定义应当与自身一致。非权威上下文被允许与自身不一致：规格会被修订，计划会被放弃，`.notes/` 里的条目捕捉的是已经不存在的那些时刻所做的决定。如果你不在“必须自洽”和“可以不自洽”之间画线，你就无法对任何一类跑扫描器。

## 把验证回路闭上

除了 agent 写出不合标准的代码这个问题，我们也认识到测试没有标准化。我们的原则之一是 agent 的工作需要验证，所以我们扩展了测试框架。这是另一项努力，平台侧由 Bhavdeep Sethi 带领，agent 行为侧由 Atlas 团队带领。

我们发现一种跨团队结构很成功：把一位专注解决测试的传统技术问题的工程师，和另一位专注 agent 指令的工程师配在一起。Bhavdeep 建了测试基础设施：单元测试、集成测试、合适的 fixture 和 marker、CI 集成。Atlas 团队的贡献是把测试标准嵌进 agent 行为层。这种做法把 agent 行为当成一等要求，而不是事后补上。

我们做了一个测试 skill，定义期望有哪些测试、何时必须有、应当如何组织。我们大量评估这些指南是否会诱导 agent 产出我们想要的测试。有时 agent 太啰嗦。有时它们极度懒惰。把 skill 的语言写对需要一些功夫。这笔投资是值得的，因为 agent 能稳定地按我们的标准产出测试。

## 我们如何判断结果

我们从最简单的指标开始：每位开发者的 token 用量。假设是，如果我们解决了让编码 agent 表现差的那些问题，工程师就能信任 agent 做更多工作，从而同时管理更多 agent，从而增加 token 用量。我们定的目标是一个季度内 token 用量达到 5 倍。这感觉很有野心，因为 Basis 的工程师本来就是编码 agent 的重度用户。当我们达到这个目标时，我们知道我们正在让开发者能更多地并行，并少花时间去修 agent 的输出。

增加 AI 用量只有在提升团队整体生产力时才有意义。这段时间里每周的提交速度增加了 2.5 倍。这项工作结束时，100% 的工程团队都在用多个 worktree 工作。工程师来找我们，要更好的工具来帮他们管理更多 agent。

## 下一步

编码 agent 是代码库的一种新消费者，有自己的失败模式、自己对上下文的胃口，以及自己对“什么算组织良好的仓库”的要求。大多数公司还没有开始认真对待这一点。认真对待的公司会像我们发现的那样看到：工作比预期更大，原则并不显而易见，而回报是实在的。

既然我们已经给了编码 agent 一个能成功的顺手环境，我们正在优化 Basis 整个 AI 原生的软件开发生命周期。这包括证明式开发这类新做法、重新设计代码审查流程，以及试验自动代码维护——把 Automatic Context 这套机制从指令层自然延伸到代码本身。

如果你想加入一家 agent 原生的公司，[我们在招聘](https://www.getbasis.ai/careers)。

Michael Crabtree 是 Basis 的 Atlas Tech Lead。@RyanBMoffat 领导了代码库标准审计，并拥有 Automatic Context 系统。@BhavdeepSethi 建了测试基础设施。@SethSchiesel 对本文有贡献。
