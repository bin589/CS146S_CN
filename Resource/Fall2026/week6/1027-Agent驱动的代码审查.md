# 《现代软件开发者》第 8 讲：Agent 驱动的代码审查

> **非官方中文翻译**，仅供学习参考，不代表原作者或斯坦福大学。
> 源幻灯片：[`1027-agentic-code-review en.pptx`](./1027-agentic-code-review%20en.pptx)
> 抓取日期：2026-10-29
> 说明：按原 pptx 逐页全文翻译，保留原始 URL、代码、专名与时间戳；内嵌图片提取到 [`images/1027/`](images/1027/)，图中英文在图片下方给出中文对照。代码与命令保持原文，不执行。

## 第 1 页：现代软件开发者

**现代软件开发者**

CS146S

斯坦福大学，2026 年秋季

Mihail Eric

themodernsoftware.dev

## 第 2 页：课程事务

**课程事务**

- 第 5 次作业周日截止。
- 剩余额度（Grok、Cognition）。
- 客座讲座在 STLC 111（此后所有周四课都在这里）。
- Silas Alberti，Chief Research Officer @ Cognition

![嘉宾照片](images/1027/slide02-01.png)

图中说明：一张人物照片，放在嘉宾姓名旁。图中没有文字。

## 第 3 页：Agent 驱动的代码审查

**Agent 驱动的代码审查**（Agentic Code Review）

## 第 4 页：为什么

**为什么**

- 软件代码审查是你能做的、对提升工程师能力与团队整体代码质量杠杆最高的活动之一。
- 在上线前发现并修复缺陷。
- 在团队里形成共享心智模型。

## 第 5 页：审查能抓住什么

**审查能抓住什么**

- 逻辑与正确性错误
- 可读性与可维护性
- 性能
- 安全
- 最佳实践（部落知识 / tribal knowledge）

## 第 6 页：代码审查的需求层次

![第 6 页图](images/1027/slide06-01.png)

- 来源：Blake Smith

图中说明：标题 **Code Review: Hierarchy of Needs**（代码审查的需求层次）。蓝色金字塔自下而上为：Mental Alignment（心智对齐，最重要）→ Correct Solution（正确方案）→ Design Discussion（设计讨论）→ Find Bugs（找缺陷）→ Style（风格，最不重要）。左侧箭头标注 Most Important（底）到 Least Important（顶）。

**讲者备注：**

- 帮助团队成员在系统变化时更新心智模型
- 确保改动真正解决了问题
- 打开对设计优缺点的讨论
- 在进入生产前抓住缺陷
- 保持代码风格与组织结构一致

## 第 7 页：AI 原生代码审查

**AI 原生代码审查**

- 代码审查成了新瓶颈 → 跟不上代码生成的速度
- 成熟度阶梯（Maturity ladder）
- Stage 0：人审一切 — 无法规模化
- Stage 1：单 agent 审查 — 尤其配合自动修复循环会更好，但仍留有空间
- Stage 2：按风险分层的多智能体审查，并内建自我改进 — 工程代码标准存放在 skill 知识库；许多公司正在收敛到这一最佳实践

## 第 8 页：分层，而不是单一闸门

![第 8 页图](images/1027/slide08-01.png)

图中说明：标题 **Layers, not one gate**（分层，而不是单一闸门）；副标题 **Six layers of checks, with rollback under them**（六层检查，底下还有回滚）。瑞士奶酪模型式图示，自上而下六层：verification → required CI → AI review → security review → human approval → merge queue + flags；穿透所有孔洞的问题最终被底部的 **fast rollback**（快速回滚）兜住。

**讲者备注：**

- https://x.com/addyosmani/status/2114604912520921136?s=43

## 第 9 页：按风险路由的审查架构

![第 9 页图](images/1027/slide09-01.png)

图中说明：流程图。PR Author（端到端拥有 PR 生命周期）→ PR Risk Analyzer（按风险路由）→ 分支为 Auto-Approve（自动批准低风险）与 Deep Code Review（逐行分析正确性）→ Review Outcome（发评论、批准或要求修改）→ Code Review Memory（组织级记忆，存放 agent skills 与开发者最佳实践）；记忆再反馈给作者。

**讲者备注：**

- https://www.augmentcode.com/blog/solving-code-review-with-cosmos

## 第 10 页：多智能体审查

**AI 原生代码审查**

- Pull request → Aggregate Judge（聚合裁判）
- 专项：Security Review、Architecture Review、Code Quality Review、Performance Review

**讲者备注：**

- 多智能体：不同方面由不同 agent 负责
- https://blog.cloudflare.com/internal-ai-engineering-stack/

## 第 11 页：安全审查提示词摘录

![第 11 页图](images/1027/slide11-01.png)

图中可见文本（安全审查 agent 提示词摘录）：

**要标记（What to Flag）**

- 注入类漏洞（SQL、XSS、命令、路径穿越）
- 变更代码中的认证／授权绕过
- 硬编码密钥、凭证或 API key
- 不安全的密码学用法
- 信任边界上对不可信数据缺少输入校验

**不要标记（What NOT to Flag）**

- 需要极不可能前置条件的理论风险
- 主防御已足够时的纵深防御建议
- 本 MR 未触及的未改代码中的问题
- 「考虑换用库 X」这类建议

**讲者备注：**

- Security review agent

## 第 12 页：审查结果示例

**AI 原生代码审查**

![第 12 页图](images/1027/slide12-01.png)

图中说明：OpenCode Code Review（`@gsa_claude`）在合并请求上的结构化评论示例，状态为 **Approved**。分节 Security / AGENTS.md / Code Quality / Performance，均为 LGTM；并列出 token 处理、路径穿越、`Zod` 校验、已修复的错误隔离等问题细节。

**讲者备注：**

- 多智能体：不同方面由不同 agent 负责
- https://blog.cloudflare.com/internal-ai-engineering-stack/

## 第 13 页：Agent 审查器设计 · 模型与上下文

**Agent 代码审查器的设计**

- 审查所用模型要与生成所用模型错开（diversify）
- Model inverter（模型反转／交叉审查）
- Thoughtful context（有意识地提供上下文）

![第 13 页图](images/1027/slide13-01.png)

图中说明：Docs + tickets（Jira、Linear、文档）→ MCP gateway；Codebase → Codebase indexer；二者汇入 Review agent。

**讲者备注：**

- https://www.greptile.com/blog/how-to-build-a-code-review-agent

## 第 14 页：Agent 审查器设计 · 验证、成本与评测

**Agent 代码审查器的设计**

- Verify（验证）：拉起开发容器，测试不同代码路径
- Cost efficiency（成本效率）：按任务复杂度选模型
  - 代码上下文 → 便宜／快速模型
  - Browser use → 较小／中等模型、更高推理
  - 深度缺陷分析 → 前沿模型
- Evaluations（评测）
  - 带已知缺陷的历史 PR
  - 伴随回滚的已发现事故

## 第 15 页：可选工具

**选项**

- 通用：Claude Code、Greptile、Coderabbit、Devin
- 安全：Vercel deepsec、Wiz security、Semgrep

## 第 16 页：提问

**有问题吗？**
