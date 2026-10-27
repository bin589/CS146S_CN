# 1006-agent-skills — slide transcript

> Unofficial English text extraction from the source `.pptx`, one section per slide, in presentation order.

> Source: [`1006-agent-skills en.pptx`](./1006-agent-skills%20en.pptx) · extracted 2026-10-22 · images in `images/1006/`

## Slide 1

- The Modern Software Developer
- CS146S
- Stanford University, Fall 2026
- Mihail Eric
- themodernsoftware.dev

## Slide 2

- Logistics
- Assignment 3 due Friday
- Claude Code credits
- Cursor credits
- Austin from Cmux!
- Guest lecture
   - Lee Robinson
- themodernsoftware.dev

![Slide 2 image 1](images/1006/slide02-01.png)

## Slide 3

- Agent Skills
- themodernsoftware.dev

**Speaker notes:**

- Which brings us to this course…

## Slide 4

- Why
- MCP is good for 3rd party integrations for coding agents
- LLMs are amazingly good at following longer form procedures and exposing such capabilities is an important part of any harness
- themodernsoftware.dev

## Slide 5

- Agent skills
- themodernsoftware.dev
- A standard for dynamically loaded agent capabilities
   - Domain-specific
   - Combine code and prompts
   - Loaded by agent as needed
- Use cases
   - Document authoring
   - Powerpoint creation
   - Data analysis
   - …and more

**Speaker notes:**

- Like scripts for agents

## Slide 6

- themodernsoftware.dev
- DEMO

**Speaker notes:**

- Provide a skills.md

## Slide 7

- Skill categories
- Code understanding and planning
- Verification
- Code style
- Miscellaneous
   - Browser parsing
- themodernsoftware.dev

## Slide 8

- Code understanding and planning
- RePPIT skills
- grill-me / grill-with-docs - Matt Pocock
   - Develop a mental model of a task
- themodernsoftware.dev

## Slide 9

- Verification
- create-verification-skill
- themodernsoftware.dev

## Slide 10

- Code style
- Define code-level best practices
- Useful for code review agents
- themodernsoftware.dev

**Speaker notes:**

- Demo

## Slide 11

- Miscellaneous
- Browser parsing
   - https://browse.sh/
- themodernsoftware.dev

**Speaker notes:**

- Demo

## Slide 12

- Best practices
- Keep scope focused
   - One skill, one clearly defined task
- Maintain your own collection of skills that you can easily port across projects
- Mine your own transcripts
   - Skills are processes written as markdown – dig your own chats to see where you intervened or corrected
   - Chefs bring their own knives between kitchens - poteto
- Don’t burn tokens/time reinventing the wheel
   - Equip agents with a CLI tool and wrap the boilerplate in a skill
- themodernsoftware.dev

## Slide 13

- Best practices
- Include situations and request phrases that should trigger the skill
- Progressive disclosure
   - Reference specific files as needed with additional context
   - Modularize and compose skills
- Maintain a verification skill to have an agent check its work
   - Allows for improvement loop
- themodernsoftware.dev

## Slide 14

- APIs vs MCP vs Skills
- themodernsoftware.dev
- APIs
   - What: HTTP/REST/GraphQL service interfaces exposed by app for developers to call
   - Who: You call or an SDK
   - Usage: You decide auth, retries, paginations, input validation, etc
- MCP
   - What: Tool definitions exposed by a server so an LLM agent can invoke them in a standardized way
   - Who:  model/agent runtime (as “tool calls”), not a human developer writing bespoke integrations each time
   - Usage: Main mechanism for interacting with external resources, data, services
- Skills
   - What: Reusable task packages / procedures that teach an agent how to do a job, often by orchestrating multiple tools/endpoints
   - Who: Agent or agent framework as higher level capability it can reach for
   - Usage: Workflow abstraction - “here’s the repeatable way to complete X.”

## Slide 15

- themodernsoftware.dev
- Questions
