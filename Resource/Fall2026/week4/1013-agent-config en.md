# 1013-agent-config — slide transcript

> Unofficial English text extraction from the source `.pptx`, one section per slide, in presentation order.

> Source: [`1013-agent-config en.pptx`](./1013-agent-config%20en.pptx) · extracted 2026-10-27 · images in `images/1013/`

## Slide 1

- The Modern Software Developer
- CS146S
- Stanford University, Fall 2026
- Mihail Eric
- themodernsoftware.dev

## Slide 2

- Logistics
- Project tech spec due Thursday
- First OSS contribution due Sunday
- Guest lecture - STLC 111 (all Thursday lectures moving forward)
- Boris Cherny
- themodernsoftware.dev

![Slide 2 image 1](images/1013/slide02-01.png)

## Slide 3

- APIs vs MCP vs Skills
- themodernsoftware.dev
- APIs
   - What: HTTP/REST/GraphQL service interfaces exposed by app for developers to call
   - Who: You call or an SDK
   - Usage: You decide auth, retries, paginations, input validation, etc
- MCP
   - What: Tool definitions exposed by a server so an LLM agent can invoke them in a standardized way
   - Who: model/agent runtime (as “tool calls”), not a human developer writing bespoke integrations each time
   - Usage: Main mechanism for interacting with external resources, data, services
- Skills
   - What: Reusable task packages / procedures that teach an agent how to do a job, often by orchestrating multiple tools/endpoints
   - Who: Agent or agent framework as higher level capability it can reach for
   - Usage: Workflow abstraction - “here’s the repeatable way to complete X.”

## Slide 4

- Additional MCP Perks
- Seamless auth
- Versioning and updates are easy
- Portability across clients
- Native sandboxing of capabilities for remote MCP
- themodernsoftware.dev

## Slide 5

- Customizing Your Agent Setup
- themodernsoftware.dev

**Speaker notes:**

- Which brings us to this course…

## Slide 6

- Why
- Achieving maximum productivity with coding agents requires taking control of your stack
- There are many mechanisms available to us for customization
- themodernsoftware.dev

## Slide 7

- Techniques for customizing agents
- Agent behavior files (Claude.md/AGENTS.md)
- Hooks
- Skills
- Subagents
- themodernsoftware.dev

**Speaker notes:**

- See examples of all of these IRL

## Slide 8

- Designing an optimal AGENTS.md
- README for agent
- Structure
   - Project overview (map of your codebase)
   - Build and test commands (use maven instead of gradle)
   - Code style guidelines
   - Testing instructions
   - Security considerations
   - Language or stack-specific gotchas (React 18 with Typescript, Vite NOT React)
- Make instructions as universally applicable as possible
- Avoid code snippets as they become outdated quickly
- Be mindful of length (<300 lines)
- Large repos should use nested configuration files with the root AGENTS.md as a router
   - For more details about API gateway design, refer to docs/API-GATEWAY.md
- themodernsoftware.dev

**Speaker notes:**

- Same principles apply to a CLAUDE.md, etc
- Examples
   - https://github.com/vercel/next.js/blob/canary/AGENTS.md
- Notes about loading order (CLAUDE.md follows root -> nearest .md file in order so most directly relevant instructions are processed last by LLM)
- Custom services or team directories have different conventions

## Slide 9

- Hooks
- Deterministic scripts that run on predefined event types
   - PreToolUse
   - PostToolUse
   - UserPromptSubmit
   - PreCompact
   - …and more
- Use-cases
   - Sanitize user prompt
   - Block sensitive actions
   - Run linter/formatter on generated code
   - Run tests post completion of task
- themodernsoftware.dev

**Speaker notes:**

- Supported in claude code / cursor
- Examples
   - https://x.com/bcherny/status/2007179852047335529?s=20
- Talk about ponytail hooks

## Slide 10

- Skills
- Provide frequently-used prompts as files that the agent can execute
- Use cases
   - Running tests
   - Creating a plan
   - Doing research
   - Reviewing code
   - Verifying outputs
- themodernsoftware.dev

**Speaker notes:**

- Provide a sample
- Ship-it command in claude code
- Show “deslop” command from Cursor

## Slide 11

- Subagents
- Runtime delegation
- Purposes of a subagent is to
   - Cleanly separate contexts for different work streams
   - Only final message is returned
   - Name, description, tool list loaded at session start
   - Implicitly or explicitly invoked
   - Automate most common workflows done
- Use-cases
   - Explore/understand your codebase
   - Simplify code after a change is made
   - Test your app end-to-end
   - Perfect for side tasks
- themodernsoftware.dev

**Speaker notes:**

- Compare to Claude.md files which are more about anchoring behavior
- Examples: https://x.com/bcherny/status/2007179850139000872?s=20

## Slide 12

- MCP Servers
- Use-cases
   - Product management software
      - Jira / Linear
      - Create and update new issues
      - Pull issue information and kick off tasks
   - Documentation software
      - Notion / Confluence
      - Create issues from feature specs
   - Observability
      - Datadog / Sentry
      - Real-time, production debugging
   - Database
      - Redshift
      - Debug data issues
      - Explore how data is organized
   - Technical documentation
      - Context7
      - Never use stale library definitions
      - Reduces likelihood of hallucinations
   - Experiment tracking
      - Arize
      - Take the output of a test run and use it to suggest new experimental runs
- themodernsoftware.dev

## Slide 13

- The context story
- themodernsoftware.dev
- Labeled blocks on the slide:
   - System Prompt
   - Memory.md
   - Env info
   - MCP tools
   - Skills
   - AGENTS.md (global)
   - AGENTS.md (local)

## Slide 14

- themodernsoftware.dev
- Questions
