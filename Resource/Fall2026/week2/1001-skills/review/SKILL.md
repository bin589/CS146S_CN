---
name: review
description: Reviews all uncommitted changes (staged and unstaged) and produces a prioritized action list with file and line references. Use when the user asks for a code review of uncommitted changes, a diff review, or invokes /review.
disable-model-invocation: true
---

Perform a comprehensive review of all uncommitted changes (staged and unstaged) and produce prioritized action items.

## What this does
- Gathers and reviews all uncommitted changes in the current branch
- Produces a prioritized list of action items with file:line references

## Steps
1. Collect change context:
   - `git status --porcelain`
   - `git diff`
   - `git diff --cached`
   - `git diff HEAD`
   - `git log --oneline -n 5`
2. Analyze changes for security, performance, style, consistency, missing edge cases, dependency impacts, and integration risks.
3. Output a summary and a single prioritized action list using indicators:
   - 🔴 must-fix
   - 🟡 recommended
   - 🟢 consider

## Output template
```
## Code Review

Summary: <1-2 sentences>

Action Items:
1. <indicator> <action> in `path:line`
2. <indicator> <action> in `path:start-end`
```
