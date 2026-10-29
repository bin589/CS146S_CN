# 驾驭 Claude Code：何时用 CLAUDE.md、skills、hooks 和 subagents

> 作者：Michael Segner（Anthropic 员工）
> 原文：<https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more>
> 页面摘要：驾驭 Claude Code 的七种方式——CLAUDE.md、rules、skills、subagents、hooks 等——以及按上下文成本和权威程度，各自该在什么时候用。
> 英文存档：[Steering Claude Code en.md](./Steering%20Claude%20Code%20en.md)
> 抓取时间：2026-10-27
> 译文说明：路径、配置片段与 URL 不翻译。非官方译文，版权归原作者／Anthropic 所有。

Claude 被做成按你的工作方式来工作，而在 Claude Code 里你可以定制它。

指示 Claude 行为的方法有七种：`CLAUDE.md` 文件、rules、[skills](https://code.claude.com/docs/en/skills)、[subagents](https://code.claude.com/docs/en/sub-agents)、[hooks](https://code.claude.com/docs/en/hooks-guide)、output styles，以及追加系统提示。

每种方法控制的是：

- 一条指令何时载入上下文；
- 它是否能熬过很长的会话（压缩行为）；
- 它带有多少权威。

下表概括每种方法的关键差别。正文给出更多细节，以及一张决策框架，用来判断你的每条 Claude 指令该放在哪里。

| 方法 | 何时加载 | 压缩行为 | 上下文成本 | 何时使用 |
|---|---|---|---|---|
| `CLAUDE.md`（根目录） | 会话开始；整个会话都留在上下文里 | 记忆化。读一次并在会话内缓存；压缩后清缓存并重新读取 | 高。每一行都花 token，无论相不相关 | 构建命令、目录布局、monorepo 结构、编码约定、团队规范 |
| `CLAUDE.md`（子目录） | 按需：Claude 读到该子目录下的文件时 | 丢失，直到那个子目录再次被碰到 | 低。只在正在处理相关子目录时消耗上下文 | 某个子目录特有的约定 |
| Rules | 会话开始（用户级规则），或只在碰到匹配文件时（按路径限定） | 压缩时重新注入 | 中。除非按路径限定，否则始终开启 | 具体约束或约定（例如所有 API handler 必须用 Zod 校验输入） |
| Skills | 会话开始时只加载名称和描述；调用 skill 时才加载全文 | 已调用的 skills 按一份共享预算重新注入；最旧的先被丢掉 | 低。全文只在被调用时加载，并受已调用 skills 的共享 token 预算约束 | 流程性工作流（部署或发布清单） |
| Subagents | 会话开始时加载名称、描述和工具列表；只有通过 Agent 工具调用时才加载正文 | 只有最终消息（摘要加元数据）回到主会话 | 低。被调用之前在主上下文里成本为零；在自己隔离的上下文窗口里运行 | 并行工作，或应当隔离运行、只返回摘要的旁路任务（深度搜索、日志分析、依赖审计） |
| Hooks | 在生命周期事件上触发 | 完全绕过压缩 | 低。配置活在主上下文之外；部分输出可能返回（例如拦截错误） | 确定性自动化：跑 linter、完成时发到 Slack、拦截命令、在 PreCompact 时备份聊天记录 |
| Output styles | 会话开始；注入系统提示 | 从不被压缩 | 高。占用上下文窗口，但会覆盖默认系统提示 | 显著的角色变化（从代码助手变成通用助手） |
| 追加系统提示 | 会话开始；作为 CLI flag 传入 | 从不被压缩；只对那一次调用生效 | 中等。会话内第一次请求之后会被缓存 | 语气、回复长度、格式偏好 |

## 传递指令的七种方法

定制 Claude Code 行为的方式有七种：用 `CLAUDE.md` 放始终开启的项目上下文，用 rules 放硬约束，用 skills 放可复用流程，用 subagents 放被委派的工作，用 hooks 放确定性自动化，用 output styles 或系统提示追加做全局改变。

每种方法都在上下文成本和权威之间做交换。这些方法影响 Claude 的行为；另外两个旋钮——[你选的模型和努力程度](https://claude.com/resources/articles/claude-model-and-effort-level-in-claude-code)——控制它有多强、工作有多卖力。

## CLAUDE.md 文件

`CLAUDE.md` 是项目根目录的一个 markdown 文件。它在会话开始时载入上下文，并在整个会话中留在那里。

构建命令、目录布局、monorepo 结构、编码约定和团队规范，都自然地属于这里。

有两种，加载方式不同：

- **始终加载：** 第一种是根目录的 `CLAUDE.md`，可以在共享仓库里，和／或保存在本地、作为你对某个项目的个人偏好。这些文件都在会话开始时加载，长会话里也不会丢失或退化。Claude Code 压缩对话时会重新读取它们。
- **按需：** 位于你初始化会话的那个文件夹之下的子目录里的 `CLAUDE.md`。例如 `app/api/CLAUDE.md` 是在 Claude 读到 `app/api` 下的文件时才加载，而不是在会话开始时。它和按路径限定的 rules 有同样的压缩行为：在那个子目录再次被碰到之前，它是消失的。

在共享仓库里，`CLAUDE.md` 会像任何没有主人的配置文件一样长大：每个团队都把自己的指令追加进去，没有东西被删掉。成本会随规模复利。

每一行都会载入仓库里每个工程师的每一次会话，无论和他们的任务相不相关。这消耗 token，并稀释对真正重要的那些指令的遵循。文件变大之后，把团队特有的约定推进按路径限定的 rules，把流程推进 skills，让它们只在相关时加载。

提示：把 `CLAUDE.md` 保持在 200 行以内，给它一个所有者，并像对待代码一样审查对它的修改。内容本身应当遵循任何提示词的同一套规则：[写出有效的提示](https://claude.com/resources/articles/best-practices-for-prompt-engineering)意味着要明确、解释约束背后的为什么，并给出例子。

把这个文件想成是给 Claude 的代码库概览，或是一份索引，指向 Claude 在需要时可以找到更多信息的其他文件。

在 monorepo 里，给每个团队的目录一份自己的子目录 `CLAUDE.md`，这样团队只加载自己的约定；开发者可以用 `claudeMdExcludes` 设置跳过那些自己从不碰的团队的文件。

对必须适用于组织里每一个仓库的标准——安全策略、合规要求——可以通过 MDM 或配置管理，把一份集中管理的 `CLAUDE.md` 部署到开发者机器上，而且个人设置无法把它排除掉。

更多设置说明见 [CLAUDE.md files: Customizing Claude Code for your codebase](https://claude.com/resources/articles/using-claude-md-files)。

## Rules

[Rules](https://code.claude.com/docs/en/memory#organize-rules-with-claude/rules/) 是 `.claude/rules/` 里的 markdown 文件，给 Claude 具体的约束或约定。

不限定范围的 rules 表现得像 `CLAUDE.md`：会话开始时始终加载，压缩时重新注入。即便和手头任务无关，这也会因为加载上下文而浪费 token。

按路径限定的 rules 让你加上一个 `paths` 字段来控制何时加载，从而只在相关时才载入规则。

例如：限定在 `src/api/**` 的规则，在一次只改文档的会话里不会进入上下文。只有当 Claude 读到 `src/api/` 目录里的文件时，它才会被加载。

看起来是这样：

```yaml
---
paths:
  - "src/api/**"
  - "**/*.handler.ts"
---
All API handlers must validate input with Zod before processing.
```

提示：像“迁移只能追加”这种针对文件的约束，最适合做成放在 `paths:` frontmatter 里的规则。当指令针对的是横切关注点、或出现在代码库多个（但不是全部）角落的文件时，用按路径限定的规则，而不是嵌套的 `CLAUDE.md`。

## Skills

[Skills](https://code.claude.com/docs/en/skills) 放在 `.claude/skills/`，是 Claude 动态加载的指令、脚本和资源文件夹。每个 skill 有一份 `SKILL.md`，带名称、描述和正文。

会话开始时只加载名称和描述；全文在 Claude 调用该 skill 时才加载，调用方式可以是 slash 命令（`/code-review`），或按任务自动匹配。

例如 `/code-review` 是内置 skill，它审查你当前的 diff 并报告发现，但不改文件。skill 定义了打法，所以你每次调用时 Claude 都遵循同一套结构化做法。

压缩时，Claude Code 会把已调用的 skills 重新注入，直到所有已调用 skills 的总预算。如果一次会话里调用了很多 skills，最旧的先被丢掉。

提示：流程性的指令，比如部署工作流、发布清单或审查流程，属于 skill，而不是 `CLAUDE.md`。

Claude Code 自带 skills，你也可以写自己的。做法见[为 Claude 构建 skills 的完整指南](https://claude.com/resources/articles/complete-guide-to-building-skills-for-claude)。

## Subagents

[Subagents](https://code.claude.com/docs/en/sub-agents) 是 `.claude/agents/` 里的 markdown 文件，为特定旁路任务定义隔离的助手。每个文件用 YAML frontmatter（`name`、`description`，以及可选的模型和工具访问字段），后面的正文成为该 subagent 的系统提示。

Subagents 和 skills 类似：名称、描述和工具列表在会话开始时加载，但 agent 正文里更大的那块上下文不会自动调用。Claude 通过 Agent 工具调用它们，并传入一段提示字符串。

subagent 正文里更大的那块指令上下文不但不会自动调用，它也根本不会进入父对话。

然后 subagent 在自己全新的上下文窗口里运行，回到主会话的只有它的最终消息（常常是许多子任务的汇总结果）加上元数据。

这个模式可以扩展：subagents 最多可以嵌套五层，而[动态工作流](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code)可以编排几十到几百个后台 agent，而不要求你逐一指定 subagent 架构的每个细节。编排计划和中间结果活在脚本变量里，而不是 Claude 的上下文窗口里，于是可以在不丢失指令保真度的情况下扩大规模。

提示：这种隔离是选择 subagent 而不是 skill 的主要原因之一。当深度搜索、一轮日志分析或依赖审计这类旁路任务会用你不会再引用的中间结果塞满主对话时，用 subagent。当你希望流程在主线程里展开、以便你能看见并驾驭每一步时，用 skill。

## Hooks

[Hooks](https://code.claude.com/docs/en/hooks-guide) 是用户定义的命令、HTTP 端点或 LLM 提示，通过在 Claude 生命周期的[特定事件](https://code.claude.com/docs/en/hooks#hook-lifecycle)上触发——比如文件编辑、工具调用或会话开始——来更确定性地控制 Claude 的行为。

你在 `settings.json`、受管理的策略设置，或 skill／agent 的 frontmatter 里注册 hooks。

hooks 有几种类型：command、HTTP、`mcp_tool`、prompt 和 agent。所有 hooks 都是被确定性地触发的。前三种确定性地执行；后两种（prompt 和 agent）用 Claude 的判断而不是一套规则来决定输出。

hooks 的上下文成本低，因为配置或指令活在主上下文窗口之外。根据类型，harness 会运行处理器（command、http、`mcp_tool`），或在单独的窗口里做模型调用（prompt、agent）。

有些 hook 的输出可能被存进主上下文窗口。例如，一个拦截 hook 的标准错误会被存进上下文，这样 Claude 知道这次调用为什么被拒绝。

但大多数 hook 的输出不会进主窗口，除非配置明确把它返回。如果你用 `PreCompact` 事件在压缩前把聊天记录备份到另一个文件以便日后查阅，Claude 不会知道聊天记录存在哪个文件里。

这使得这些 hook 类型与 `CLAUDE.md`、rules 和 skills 有根本差别。更多见[如何配置 hooks](https://claude.com/resources/articles/how-to-configure-hooks)。

提示：任何应当确定地发生的事都用 hooks：编辑后跑 linter、完成时发到 Slack，或在特定命令执行前拦截它们。一个 `PreToolUse` hook 可以检查任意工具调用，并以退出码 2 拒绝它。

它们的上下文成本低，因为它们是 harness 去跑的代码，而不是载入上下文的、给 Claude 的指令。Skills 和 hooks 也是[设计 agent 循环](https://claude.com/resources/articles/getting-started-with-loops)的构件——重复运行直到满足停止条件的工作流。

## Output styles

[Output styles](https://code.claude.com/docs/en/output-styles) 是 `.claude/output-styles/` 里的文件，把指令注入系统提示。它们从不被压缩，每次会话开始时加载，并在会话内第一次请求之后被缓存，因此上下文成本是中等的。

因为它们坐在系统提示里，output styles 在目前讲过的方法里拥有最高的指令遵循权重，应当克制使用。

改 output style 会替换默认的 output style（除非你在该 style 的 frontmatter 里设置 `keep-coding-instructions: true`）。

在 Claude Code 里，这会拿掉那些告诉 Claude 它在帮用户做软件工程任务的指令，以及其他关键的默认指令，例如：

- 如何限定改动范围；
- 何时添加或省略代码注释；
- 安全方面该怎么处理；
- 验证习惯，比如在宣布工作完成之前跑测试。

默认情况下，自定义 output style 会丢掉所有这些，Claude Code 会更像一个通用助手，而不是软件工程助手。

提示：写自定义 output style 之前，先看内置的。Proactive、Explanatory 和 Learning 覆盖了最常见的需求（自主、教学模式、协作编码），而不需要你维护一份 style 文件。

## 追加系统提示

修改 output styles 的替代方案是 `append-system-prompt` 这个 flag。修改 output style 文件可能对 Claude 的行为造成很大的、非预期的改变，而 append flag 只是在原始系统提示上做加法。它不改变 Claude 的角色，只是往默认角色上加指令。

它也是在调用时传入的，只对那一次调用生效，而不是作为文件跨会话持久化。

和其他传递指令的方法相比，追加系统提示的上下文成本可能更高。它增加输入 token，不过提示缓存会在会话内第一次请求之后降低这笔成本。指示 Claude 用更啰嗦或更长的风格，也会增加输出 token。

提示：追加系统提示最适合用来加具体的编码标准、输出格式或领域知识。记住，用这种方式追加，遵循程度的回报是递减的。一般来说，你用这个方法给的指令越多，Claude 遵循得越不严格，尤其是当它们互相矛盾时。

## 每种方法该在什么时候用

如果你发现自己在做下面这些事，也许该考虑把指令放到别的地方：

- **在 `CLAUDE.md` 里写“每次 X，总是做 Y”。** 如果这个行为应当可靠地发生，比如每次编辑后跑 prettier，或完成时发到 Slack，改用 `settings.json` 里的 hook。模型选择去跑 formatter，和 formatter 自动跑起来，是两回事。
- **在 `CLAUDE.md` 里写“永远不要做这个”。** 当有一件事绝对不能发生时，指令是错误的工具。Claude 大多数时候会遵循指令，但在压力下、在很长的会话或含糊的情境里，或因为任务中访问的某个文件里有提示注入，模型可能不遵循一条被提示出来的规则。真正的护栏必须是确定性的，执行手段是 [hooks](https://code.claude.com/docs/en/hooks) 和 [permissions](https://code.claude.com/docs/en/permissions)。一个 `PreToolUse` hook 可以检查一次调用，并以退出码 2 拦截它。[受管理的设置](https://code.claude.com/docs/en/settings#managed-settings)更进一步：由管理员部署，不能被用户的本地配置覆盖，是强制执行确定性的、全组织护栏的唯一方式。
- **在 `CLAUDE.md` 里放一段 30 行的流程。** 流程属于 skills。`CLAUDE.md` 是给 Claude 应当一直握着的事实：构建命令、monorepo 布局、团队约定。部署手册或安全审查清单应当放在 `.claude/skills/`，正文只在被调用时加载。
- **一条没有 paths 的、针对 API 的规则。** 如果规则只适用于 `src/api/**`，用 `paths:` 限定它，就能让它在无关工作期间待在上下文之外。一条不限定范围的规则，在机制上等同于把内容放进 `CLAUDE.md`：始终加载，始终花 token。
- **把个人偏好写进项目级 `CLAUDE.md`。** 所有基于文件的方法都有一个用户级对应物，无论你在哪个仓库，每次 Claude Code 会话都会加载它。个人偏好用本地文件（比如始终使用语义化 commit message）。项目级文件留给全团队、但针对某一代码库的偏好。

## 开始定制 Claude Code

从配置环境到跨并行会话扩展，更多把 Claude Code 用好的提示和模式，见 [Claude Code 最佳实践](https://code.claude.com/docs/en/best-practices#write-an-effective-claude-md)文档。

当其中几样已经能工作之后，你可以把它们（skills、subagents、hooks、output styles）打成一个 [plugin](https://code.claude.com/docs/en/plugins)，在队友或项目之间分享一套连贯的配置。

本文由 Anthropic 员工 Michael Segner 撰写。
