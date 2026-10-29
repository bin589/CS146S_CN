# plan

> **非官方中文译文。** 本文为课程资料的中文翻译，仅供学习参考；一切以英文原文为准。
>
> - 原文文件：[SKILL.md](./SKILL.md)（`Resource/Fall2026/week2/1001-skills/plan/SKILL.md`）
> - 抓取日期：2026-10-22

---

```yaml
---
name: plan
description: 使用设计文档模板，在 plans/ 目录下以 Markdown 文件的形式起草实现计划，但不实施改动。当用户要求为某个代码改动做计划、写计划，或调用 /plan 时使用。
disable-model-invocation: true
---
```

设计文档模板是本 skill 目录下的 [design_doc_template.md](design_doc_template.md)。下文说明中凡出现 `@design_doc_template.md` 的地方，都请打开那个文件。

1. 在动笔之前，先澄清代码改动的范围、约束与时间安排。
2. 打开 `@design_doc_template.md`，照着它的结构，在 `plans/` 下以 `.md` 文件的形式起草计划。
3. 用简洁、可执行的条目填充当前上下文、需求、设计决策与实现计划。
4. 只有在测试、可观测性、发布（rollout）与安全这几节会影响本次改动时才填写；不适用时留空。
5. 不要真正实施任何改动。只创建一份反映需要实现内容的计划 .md 文件。
6. 只做被直接要求的改动。保持方案简单、聚焦。
