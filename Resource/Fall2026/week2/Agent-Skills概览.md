# Agent Skills 概览

> 来源：<https://agentskills.io/home>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。下文为公开页可读内容的中文整理／翻译。
# Agent Skills 概览（agentskills.io）

Agent Skills 开放规范／文档站首页。说明什么是 Agent Skill、如何编写与分发、与 MCP／工具调用的关系等。

## 正文摘录

What are Agent Skills?
Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows. At its core, a skill is a folder containing aSKILL.md file. This file includes metadata (name and description, at minimum) and instructions that tell an agent how to perform a specific task. Skills can also bundle scripts, reference materials, templates, and other resources.
Why Agent Skills?
Agents are increasingly capable, but often don’t have the context they need to do real work reliably. Skills solve this by packaging procedural knowledge and company-, team-, and user-specific context into portable, version-controlled folders that agents load on demand. This gives agents:
- Domain expertise: Capture specialized knowledge — from legal review processes to data analysis pipelines to presentation formatting — as reusable instructions and resources.
- Repeatable workflows: Turn multi-step tasks into consistent, auditable procedures.
- Cross-product reuse: Build a skill once and use it across any skills-compatible agent.
How do Agent Skills work?
Agents load skills through progressive disclosure, in three stages:
- Discovery: At startup, agents load only the name and description of each available skill, just enough to know when it might be relevant.
- 
Activation: When a task matches a skill’s description, the agent reads the full SKILL.md instructions into context.
- Execution: The agent follows the instructions, optionally executing bundled code or loading referenced files as needed.
Full instructions load only when a task calls for them, so agents can keep many skills on hand with only a small context footprint.
Where can I use Agent Skills?
Agent Skills are supported by a large number of AI tools and agentic clients — see the Client Showcase to explore some of them!
Open development
The Agent Skills format was originally developed by Anthropic, released as an open standard, and has been adopted by a growing number of agent products. The standard is open to contributions from the broader ecosystem. Come join the discussion on GitHub or Discord!
Get started with Agent Skills
Quickstart
Create your first Agent Skill and see it in action.
Specification
The complete format specification for Agent Skills.
