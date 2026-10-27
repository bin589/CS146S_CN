# 0924-agent-harness — slide transcript

> Unofficial English text extraction from the source `.pptx`, one section per slide, in presentation order.

> Source: [`0924-agent-harness en.pptx`](./0924-agent-harness%20en.pptx) · extracted 2026-10-22 · images in `images/0924/`

## Slide 1

- The Modern Software Developer
- CS146S
- Stanford University, Fall 2026
- Mihail Eric
- themodernsoftware.dev

## Slide 2

- Logistics
- Final project specifications out
   - Allowed 1 additional team member (in addition to a swarm of coding agents)
- Credits for different coding agent providers
   - Claude
   - Factory
   - X.AI
   - Devin
- More details on OSS contributions next week
- Final deadline is 9/27 for course applications
- themodernsoftware.dev

## Slide 3

- The Anatomy of a Modern Coding Agent
- themodernsoftware.dev

**Speaker notes:**

- Which brings us to this course…

## Slide 4

- themodernsoftware.dev

![Slide 4 image 1](images/0924/slide04-01.png)
![Slide 4 image 2](images/0924/slide04-02.png)
![Slide 4 image 3](images/0924/slide04-03.png)
![Slide 4 image 4](images/0924/slide04-04.png)
![Slide 4 image 5](images/0924/slide04-05.png)
![Slide 4 image 6](images/0924/slide04-06.png)
- Recap

**Speaker notes:**

- User interacts with coding agent client (windsurf, cursor, claude code) and runs a loop with an underlying llm. Sometimes the llm issues tool calls which the client executes (off-LLM)

## Slide 5

- themodernsoftware.dev
- Enter a state-of-the-art coding agent

![Slide 5 image 1](images/0924/slide05-01.png)

**Speaker notes:**

- User interacts with coding agent client (windsurf, cursor, claude code) and runs a loop with an underlying llm. Sometimes the llm issues tool calls which the client executes (off-LLM)

## Slide 6

- Modern coding harnesses are more complex
- Harness design is one of the most important problems in coding agents
- Components
   - System prompt
   - Custom configuration files (AGENTS.md, etc)
   - Tool list
   - Plan mode
   - Subagents
   - Skills
   - Hooks
   - Compaction
- themodernsoftware.dev

**Speaker notes:**

- Some of the components in an agent like claude

## Slide 7

- themodernsoftware.dev

![Slide 7 image 1](images/0924/slide07-01.png)

## Slide 8

- Tool List
- Lean but powerful capabilities across search, shell commands, agent tasks
- ~40 built-in tools in the case of Claude
- MCP tools are also available and loaded into context
- Description, names, full signature is a part of the prompt
- themodernsoftware.dev

## Slide 9

- System Prompt
- System level blueprint
- Defines
   - Harness / behaviors
   - Guardrails
   - Environment (ie what is the system, where are we)
- themodernsoftware.dev

## Slide 10

- Agent Configuration Files
- User-level agent customizations like CLAUDE.md/AGENTS.md
- Take precedence over other commands
- themodernsoftware.dev

## Slide 11

- Plan Mode
- Explicit tool prompting agent to make a spec for a change
- Can engage in further questioning with user to clarify requirements
- themodernsoftware.dev

## Slide 12

- Skills
- Describes a written procedure to be performed by agent
- A prompt with tool calls and/or local script invocations
- Can be invoked proactively or explicitly
- themodernsoftware.dev

## Slide 13

- Subagents
- Invoked via an explicit tool call
- Fresh context within session with custom system prompt
- Allows for parallelization (though token costs go up)
- Final result passed back to parent
- themodernsoftware.dev

## Slide 14

- Hooks
- Prompts or snippets of code that are inserted at different points in the harness lifecycle
- Especially interesting if some pre/post-processing needs to get done
- We’ll discuss best practices later
- themodernsoftware.dev

## Slide 15

- Compaction
- Create consolidated summary of key points in agent run when context is almost exceeded
- Replace existing history with summary
- Triggered manually or automatically
- Can be lossy so you may want to adapt your own
- themodernsoftware.dev

## Slide 16

- Principles of Effective Harnesses
- Simplicity
   - Fewer, more powerful tools are preferred (sql, bash, etc)
- Mind the context window – avoid the dumb zone so be careful of tool bloat
   - More on optimal context engineering later
- Prompt contents and lengths will evolve – make it easy to adapt them
- themodernsoftware.dev

## Slide 17

- themodernsoftware.dev
- Questions?
