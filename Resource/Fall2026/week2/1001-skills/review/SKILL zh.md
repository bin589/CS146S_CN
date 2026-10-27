# review

> **非官方中文译文。** 本文为课程资料的中文翻译，仅供学习参考；一切以英文原文为准。
>
> - 原文文件：[SKILL.md](./SKILL.md)（`Resource/Fall2026/week2/1001-skills/review/SKILL.md`）
> - 抓取日期：2026-10-22

---

```yaml
---
name: review
description: 审查所有未提交的改动（已暂存与未暂存），并产出一份带文件与行号引用的优先级行动清单。当用户要求对未提交改动做代码审查、审查 diff，或调用 /review 时使用。
disable-model-invocation: true
---
```

对所有未提交的改动（已暂存与未暂存）做一次全面审查，并产出按优先级排序的行动项。

## 这个 skill 做什么
- 收集并审查当前分支中所有未提交的改动
- 产出带 file:line 引用的优先级行动项清单

## 步骤
1. 收集改动上下文：
   - `git status --porcelain`
   - `git diff`
   - `git diff --cached`
   - `git diff HEAD`
   - `git log --oneline -n 5`
2. 分析改动在安全、性能、风格、一致性、缺失的边界情况、依赖影响以及集成风险方面的表现。
3. 用下列指示符输出一份摘要和一份单一的优先级行动清单：
   - 🔴 必须修复
   - 🟡 建议修复
   - 🟢 可以考虑

## 输出模板
```
## Code Review

Summary: <1-2 sentences>

Action Items:
1. <indicator> <action> in `path:line`
2. <indicator> <action> in `path:start-end`
```
