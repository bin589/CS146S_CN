---
name: plan
description: Drafts an implementation plan as a markdown file in plans/ using the design document template, without implementing the change. Use when the user asks to plan a code change, write a plan, or invokes /plan.
disable-model-invocation: true
---

The design document template is [design_doc_template.md](design_doc_template.md) in this skill directory. Open that file wherever the instructions below say `@design_doc_template.md`.

1. Clarify the code change scope, constraints, and timelines before writing anything down.
2. Open `@design_doc_template.md`, mirror its structure, and draft the plan as a `.md` file in `plans/`.
3. Populate current context, requirements, design decisions, and implementation plan with concise, actionable bullets.
4. Note testing, observability, rollout, and security sections only if they influence this change; leave sections blank when they do not apply.
5. Do not actually implement any change. Only create a plan .md reflecting what needs to be implemented.
6. Only make changes that are directly requested. Keep solutions simple and focused.
