# 我仍然更喜欢 MCP，而不是 Skills

> 作者：David Mohl
> 原文：<https://david.coffee/i-still-prefer-mcp-over-skills>
> 英文存档：[I Still Prefer MCP Over Skills en.md](./I%20Still%20Prefer%20MCP%20Over%20Skills%20en.md)
> 抓取时间：2026-10-27
> 译文说明：保留 MCP、Skills、CLI、OAuth 等专名；代码、命令、产品名与 URL 不翻译。文末 MCP Nest / Warplet 是作者自己的产品介绍，一并译出。非官方译文，版权归原作者所有。

**TL;DR：** AI 圈正在使劲把 “Skills” 推成给 LLM 赋予能力的新标准，但我不买账。Skills 很适合纯知识，也适合教 LLM 怎么用一个已经存在的工具。可是如果要给 LLM 真正访问服务的能力，模型上下文协议（MCP）是远为更好、也更务实的架构选择。我们该做的是连接器，而不是再堆更多 CLI。

也许是因为我在 X 上花的时间太多，最近“MCP 已死”“Skills 才是新标准”这句话被反复敲进我脑子里。我走到哪儿都能看见有人在庆祝模型上下文协议的死亡，转而往仓库里丢一份 `SKILL.md`。

我是很重度的 AI 用户。写代码我用 Claude Code、Codex 和 Gemini。几乎每天都靠 ChatGPT、Claude 和 Perplexity 管理从 Notion 笔记到 DEVONthink 数据库、甚至邮件的一切。

我就是不喜欢 Skills。

我希望 MCP 能留下来。我真的不想要一个未来：每接一个服务都得配一个专用 CLI，再加一份 markdown 说明书。

下面是为什么我认为，把 Skills 当成万能解法是在倒退，以及为什么 MCP 的架构仍然是对的。

## 我喜欢 MCP 的地方

MCP 的核心哲学很简单：它是一层 API 抽象。LLM 不需要懂 how，只需要知道 what。如果 LLM 想和 DEVONthink 交互，它调用 `devonthink.do_x()`，剩下的由 MCP server 处理。

这种关注点分离带来一些很难被打败的好处：

- **零安装的远程使用：** 远程 MCP server 不需要在本地装任何东西。把客户端指到 MCP server 的 URL，它就能用。
- **更新无缝：** 远程 MCP server 加上新工具或资源时，每个客户端立刻拿到最新版。不用推送更新、升级包，或重装二进制。
- **认证更合理：** 认证通常用 OAuth，处理得很体面。客户端完成握手之后就可以对 MCP 执行操作。你不用逼用户把原始 token 和密钥以明文管起来。
- **真正可移植：** 我的远程 MCP server 在哪都能用：Mac、手机、网页。无所谓。只要有客户端，我就能用自己选的 LLM 管理 Notion。
- **沙箱：** 远程 MCP 天然是沙箱化的。它们暴露的是受控接口，而不是把本地环境的原始执行权交给 LLM。
- **聪明的发现：** 现代应用（ChatGPT、Claude 等）内置了工具搜索。它们只在真正需要时才查找并加载工具，省下宝贵的上下文窗口。
- **无摩擦的自动更新：** 即便是本地安装，直接用 `npx -y` 或 `uv` 装上的 MCP 也可以每次启动时自动更新。

## Skills 的摩擦

并非所有 Skill 都一样。纯知识型 skill（教 LLM 怎么格式化 commit message、按某种方式写测试，或使用你们内部行话）其实很好用。问题从 Skill 必须靠一个 CLI 才能真正做事时开始。

我对 Skills 最大的不满，是它假设每个环境都能、或都应该跑任意 CLI。

OpenClaw 或类似来源的大多数“能力型” skill，都要求你先装一个专用 CLI（`gogcli`、`remindctl` 等）才能用。可如果你不在本地终端里呢？ChatGPT 跑不了 CLI。Perplexity 和标准网页版 Claude 也跑不了。除非你在用完整的计算环境（比如 Perplexity Computer、Claude Cowork、Claude Code 或 Codex），任何依赖 CLI 的 skill 一落地就是死的。

这会引出一连串烦人的体验和架构问题：

- **部署一团乱：** CLI 得发布、管理，并通过二进制、NPM、uv 等安装。
- **密钥管理是噩梦：** 认证所需的 API token 放哪？走运的话，环境里有个 `.env`，你可以把明文密钥倒进去。有些临时环境会把自己抹掉，于是 CLI 今天能用，明天就把密钥忘了。
- **生态碎片化：** Skill 的管理目前是西部荒野。skill 一更新，你就得重装。有的工具支持用 `npx skills` 安装，但那只在 Codex 和 Claude Code 里有效，Claude Cowork 或标准 Claude 不行。纯知识 skill 在 Claude 里能用，大多数其他的不行。有的工具有 “skills marketplace”，有的没有。有的能从 GitHub 安装，有的不能。你试着把一个 OpenClaw skill 装进 Claude，它会因为元数据字段对不上、YAML 解析报错而炸开。
- **上下文膨胀：** 用一个 skill 往往要把整份 `SKILL.md` 装进 LLM 的上下文窗口，而不是只暴露它需要的那一个工具签名。这就像别人只想调用 `car.turn_on()`，你却强迫他读完整本汽车用户手册。

如果一份 Skill 的说明以“先安装这个 CLI”开头，你只是多加了一层不必要的抽象和额外步骤。为什么不直接用远程 MCP？

## 连接器 vs 说明书

我不希望 Skills 变成把 LLM 接到服务上的事实标准。我们可以在 Skill 里解释 API 的形状，让 LLM 去 curl，但这怎么会比通过 MCP 提供一个干净、强类型的接口更好？

我认为生态应该是这样：

**什么时候用 MCP：** MCP 应该是给 LLM 一个接口、让它连上某样东西的标准：一个网站、一个服务、一个应用。接口应当由服务或应用自己规定并拥有。

- 以 Google Calendar 为例。一个 gcal CLI 没问题。有问题的是一份 Skill，它让 LLM 去安装它、管理 auth token，再 shell 出去调用。Google 自己拥有的、带 OAuth 的远程 MCP 在协议层处理认证，任何客户端不用安装就能用（[Google 现在提供的正是这个](https://developers.google.com/workspace/calendar/api/guides/configure-mcp-server)）。
- Notion 原生提供 `mcp.notion.so/mcp`，而不是逼我下载 `notion-cli` 再去折腾认证。接口是他们的，所以他们可以随时加工具或打补丁，每个客户端不用重装就能拿到。
- Hopper 内置的 MCP 坐在正在运行的反汇编会话里，所以 `step()` 就是你当前打开的那条指令。一个 hopper-cli 没有这份上下文。
- Xcode 自带的 MCP 坐在当前工程里，所以它已经知道构建、环境和工具链。一个 xcode-cli 没有这份上下文。

**什么时候用 Skills：** Skills 应该是“纯的”。它们应该聚焦知识和上下文。

- **教已有的工具：** 我喜欢有一个 `.claude/skills` 文件夹，教 LLM 怎么用我已经装好的工具。一份解释如何使用 `curl`、`git`、`gh` 或 `gcloud` 的 skill 完全说得通。我们不需要 “curl MCP”。我们只需要教 LLM 怎么构造好的 curl 命令。不过，管理 issue 时，一个专门的远程 GitHub MCP 比依赖 `gh` CLI skill 合理得多。
- **把工作流标准化：** Skills 非常适合教 Claude 你们的业务行话、内部沟通风格或组织结构。
- **教格式处理：** 这是另一个好例子，Anthropic 的 [PDF Skill](https://github.com/anthropics/skills/tree/main/skills/pdf) 也是这么做的：它解释如何处理 PDF，以及如何用 Python 操作它们。
- **密钥管理的模式：** 有一份 skill 告诉 Claude“这个仓库用 fnox，用法是这样”，就很合理。每次碰到密钥，Claude 就把这份 skill 调出来。这比专门做一个 MCP 只为了调用 `get_secret()` 好得多。

洗澡时的念头：也许问题出在术语上。Skills 就该叫 `LLM_MANUAL.md`，MCP 就该叫连接器（Connectors）。

两者各有位置。

MCP 是连到外部事物的接口。Skill 是如何与一个事物交互的说明书。

## Skills + MCP = 给连接器写说明书

一份解释如何使用某个 MCP server 的 skill，其实非常说得通。不是为了取代 MCP，而是在 LLM 开始调用工具之前给它上下文：这个服务做什么、工具之间如何关联、什么时候用哪一个。连接器层上面再加一层知识。这才是我想要的组合。

而且这正是我在实践里越用越多的模式。和 MCP server 一起工作时，我不可避免会发现坑和非显而易见的模式：日期格式必须是 `YYYY-MM-DD` 而不是 `YYYYMMDD`；搜索函数除非你把某个参数调大，否则会截断结果；某个工具的名字和它实际做的事对不上。与其每个会话都重新发现这些，我干脆让 Claude 把我们学到的一切包成一份 Skill。LLM 已经有这次对话的上下文，于是它写出的 Skill 里写进了所有的坑、常见模式和修正过的假设。

结果是一份作为 MCP 备忘单的 Skill，而不是 MCP 的替代品。真正的连接和工具执行仍由 MCP 负责。Skill 只是确保 LLM 不会把 token 浪费在我已经解决过的那些坑上。两者合在一起，体验才真正顺。

与此同时，我仍会维护满是常用流程 Skill 的 dotfiles 仓库，也仍会把 `.claude/skills` 放进我的仓库，用来引导 AI 的行为。

我只是希望行业不要抛弃模型上下文协议。无缝 AI 集成的梦想依赖的是标准化接口，而不是一片东拼西凑的 CLI。我还在等官方的 Skyscanner、Booking.com、Trip.com 和 Agoda.com MCP。

说到远程 MCP：我做 [MCP Nest](https://mcpnest.dev) 就是为了这个问题。很多有用的 MCP server 天生只在本地（stdio），比如 Fastmail、Gmail，或任何跑在你机器上的东西。MCP Nest 把它们托管到云上，于是它们可以远程访问，能从 Claude、ChatGPT、Perplexity 或任何支持 MCP 的客户端、在你所有设备上使用。如果你想让本地 MCP 到处都能用，又不想直接暴露自己的机器，它就是干这个的。

如果你喜欢 MCP，又想在常用的 LLM 里访问跑在 Mac 上的 MCP server，可以看看 [Warplet](https://warplet.app)，它会建立安全的远程隧道。MCP Nest 负责托管；Warplet 从你的 Mac 打隧道出去。
