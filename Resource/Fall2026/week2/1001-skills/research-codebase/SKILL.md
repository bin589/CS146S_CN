---
name: research-codebase
description: Researches and documents the existing codebase exactly as it is today, with file paths and line references, and writes the document to research/. Use when the user asks to research the codebase, document how something works today, or invokes /research-codebase. Does not suggest improvements.
disable-model-invocation: true
---

Research and document the existing codebase exactly as it is today; no suggestions or evaluations.

## Behavior contract
- Only document what exists today; do not suggest improvements, RCA, or future work
- Provide concrete file paths and line references in findings
- Read any user-mentioned files fully before decomposing work

## Steps after receiving the research query
1. Read directly mentioned files fully.
2. Decompose the query into focused research areas and create an internal checklist.
3. Explore relevant directories and files in parallel when areas are independent. If necessary feel free to inspect the `git` history for potential answers to the research query presented. Additionally if you need to refer to some 3rd party API to better understand how something works, make sure to use `context7` for up-to-date documentation about the API.
4. Synthesize after all exploration completes; prioritize live code findings over historical docs.
5. Produce a structured research document with:
   - Summary of findings answering the question
   - Detailed sections per component/area with code references
   - Cross-component connections and data flows
   - Place the research document in the top level `research/` directory.

## Output format
- High-level summary (3-6 sentences)
- Detailed findings grouped by component/area
- Code references in the form `path/to/file.py:123-145`
