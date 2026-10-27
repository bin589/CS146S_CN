# 0929-context-engineering — slide transcript

> Unofficial English text extraction from the source `.pptx`, one section per slide, in presentation order.

> Source: [`0929-context-engineering en.pptx`](./0929-context-engineering%20en.pptx) · extracted 2026-10-22 · images in `images/0929/`

## Slide 1

- The Modern Software Developer
- CS146S
- Stanford University, Fall 2026
- Mihail Eric
- themodernsoftware.dev

## Slide 2

- Logistics
- Factory workshop
   - Thursday, 6:20-645pm
- Announcing the OSS partners program
   - Anyscale (Ray)
   - Arize AI (Phoenix)
   - Browserbase
   - cmux
   - CopilotKit
   - CrewAI
   - HeyGen
   - Marimo
   - OpenHands
   - Pi
   - Unsloth AI
   - Vercel
   - Warp
   - Zilliz
- themodernsoftware.dev

## Slide 3

- Advanced Prompting and Context Engineering for Complex Codebases
- themodernsoftware.dev

**Speaker notes:**

- Which brings us to this course…

## Slide 4

- Orientation
- themodernsoftware.dev
- Objective
   - Move beyond ad-hoc prompting to a robust and reliable synchronous AI development workflow
   - Use AI to rapidly onboard to unfamiliar codebases and systematically complete complex coding tasks
- Lesson Plan
   - Learn how to onboard to large unfamiliar codebases rapidly
   - Learn spec-driven engineering via the RePPIT framework
      - Research
      - Propose
      - Plan
      - Implement
      - Test
   - Learn about other spec-driven AI development frameworks

## Slide 5

- themodernsoftware.dev

![Slide 5 image 1](images/0929/slide05-01.png)

## Slide 6

- Vibe coding confuses expectations
- themodernsoftware.dev

**Speaker notes:**

- Vibe coding has different definitions but the standard one of just YOLO-ing and tab-accepting AI code is not the focus here

## Slide 7

- How would you build a Mint clone?
- themodernsoftware.dev

![Slide 7 image 1](images/0929/slide07-01.png)

## Slide 8

- Writing production AI code requires being methodical
- themodernsoftware.dev

**Speaker notes:**

- You should have an active, functional mental model of how you would build your solution

## Slide 9

- Principles of Production AI Code
- Understand an unfamiliar codebase
- Propose some solutions
- Plan out the most promising solution
- Implement it
- Test it
- themodernsoftware.dev

**Speaker notes:**

- These days bad code is both architecturally wrong decisions but also functionally incorrect software (from hallucinating LLMs)

## Slide 10

- Use RePPIT
- themodernsoftware.dev

## Slide 11

- themodernsoftware.dev
- R  esearch
- P  ropose
- P  lan
- I   mplement
- T  est

**Speaker notes:**

- This is something you should iterate on to find what works for you but these high level points should be a solid starting point for your own workflow

## Slide 12

- Demo
- themodernsoftware.dev
- Feature: Include a trend line showing spending by category over time.

## Slide 13

- themodernsoftware.dev
- ½-¾ of “smart” tokens
- in context window
- System prompt
- AGENTS.md/CLAUDE.md
- Task-specific context
- the “dumb” zone

## Slide 14

- Review your specs very carefully
- For very large features, break your task down into task lists
   - When an item is finished, document your agent’s work in a written artifact
   - This becomes context with which the next item can be continued
- Be very mindful of your context window (½-¾ of “smart” tokens)
- themodernsoftware.dev
- Best practices

## Slide 15

- Task delegation taxonomy
- themodernsoftware.dev
- Approaches
   - Simple prompting
   - Make a plan
   - Research then plan
   - (Research then plan) x N
- When to apply each?

## Slide 16

- Task delegation taxonomy
- themodernsoftware.dev

![Slide 16 image 1](images/0929/slide16-01.png)
- Source

## Slide 17

- Superpowers
   - Opinionated end-to-end, guided workflow for solving complex tasks
   - TDD-based
   - A set of agent skills that can be used for spec/plan creation, implementation, and testing
   - Built-in parallelism
- Openspec
   - Lightweight flow for developing specs, implementation plans, etc
   - Neat methodology around tracking changes in source-of-truth specs and merging them after a diff is made
- themodernsoftware.dev
- Other popular frameworks

## Slide 18

- Where do specs live?
   - Linear or locally/Git (as per OpenSpec)
- Design tradeoffs / decision points for parts of the codebase can live in .notes/
- themodernsoftware.dev
- Spec management
