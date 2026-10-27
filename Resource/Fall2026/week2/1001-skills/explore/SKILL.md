---
name: explore
description: Explores an unfamiliar area of the codebase and briefs the user on purpose, entry points, call graph, file layout, and data flow. Use when the user asks to explore the codebase, get oriented in an area, or invokes /explore. Do not execute code unless asked.
disable-model-invocation: true
---

Explore the unfamiliar area of this codebase and brief me. Focus on clarity and concision.

What to produce:
- Short overview of the feature/area and its purpose.
- Key entry points/functions, with file paths and what each does.
- Call graph/dependencies: how major functions/modules interact; note external libs/services.
- File and directory structure: where related code lives and how it is organized.
- Data flow and state: important models, inputs/outputs, side effects.

How to explore:
- Start by reading the primary entry file, then follow imports to map dependencies.
- Skim tests, fixtures, or example scripts to see intended behavior.
- Note any setup steps required to run or reproduce behavior, but do not execute unless asked.
