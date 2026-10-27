# make-proposals

> **非官方中文译文。** 本文为课程资料的中文翻译，仅供学习参考；一切以英文原文为准。
>
> - 原文文件：[SKILL.md](./SKILL.md)（`Resource/Fall2026/week2/1001-skills/make-proposals/SKILL.md`）
> - 抓取日期：2026-10-22

---

```yaml
---
name: make-proposals
description: 基于一份研究文档以及一个功能或项目请求，生成最多两个解决方案提议。当用户要求解决方案提议、实现思路，或调用 /make-proposals 时使用。需要一份由 /research-codebase 产出的研究文档。
disable-model-invocation: true
---
```

基于一份已有的研究文档和一个新的功能或项目请求，生成最多两个解决方案提议

## 行为
- 把所提供的 research-codebase Markdown 文档视为需求收集预期与文档结构的权威参考。
- 要求有一份由 `/research-codebase` 产出的研究文档
- 针对所提供的请求，给出两种不同的解决方案，每种都与研究发现相呼应。
- 每个提议都要突出权衡、受影响的系统、验证步骤与待解问题。

## 步骤
1. 需求收集
   - 捕获用户的请求以及可选的研究文档路径。
2. 解析研究文档
   - 完整阅读研究文档。
   - 提取约束、相关模块、依赖、数据流以及此前的决策。
3. 综合解空间
   - 基于研究发现推导候选方案。
   - 对每个方案，注明主要改动、受影响的代码路径、所需的迁移/配置更新，以及发布（rollout）方面的考虑。
   - 方案数量保持在两到三个不同的提议，按与约束的契合度从高到低排序。
4. 验证规划
   - 确定证明每个方案所必需的验证策略（测试、实验、可观测性）。
   - 指出关键的未知项或前置研究。
5. 使用下面的模板交付回复。

## 输出模板
```
## Solution Proposals

Context:
- Request: <short restatement of the ask>
- Research Source: <filename and key sections used>

Proposal 1 — <title>
- Overview: <2-3 sentences>
- Key Changes: <components/modules>
- Trade-offs: <risks vs benefits>
- Validation: <tests/experiments/metrics>
- Open Questions: <gaps or follow-ups>

Proposal 2 — <title>

```

## 说明
- 引用研究文档中的具体内容时，用反引号把代码和章节写成 `path/to/file.py:lines`。
- 当研究没有直接回应请求时，要指出这些缺口，并建议在提出方案之前补充研究。
- 保持简洁；在维持可执行指导的同时，宁可清晰，也不要事无巨细。
