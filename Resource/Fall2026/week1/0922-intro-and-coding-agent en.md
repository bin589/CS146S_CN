# 0922-intro-and-coding-agent — slide transcript

> Unofficial English text extraction from the source `.pptx`, one section per slide, in presentation order.

> Source: [`0922-intro-and-coding-agent en.pptx`](./0922-intro-and-coding-agent%20en.pptx) · extracted 2026-10-22 · images in `images/0922/`

## Slide 1

- The Modern Software Developer
- CS146S
- Stanford University, Fall 2026
- Mihail Eric
- themodernsoftware.dev

## Slide 2

- State of the World: 2026
- themodernsoftware.dev

![Slide 2 image 1](images/0922/slide02-01.png)
![Slide 2 image 2](images/0922/slide02-02.png)
![Slide 2 image 3](images/0922/slide02-03.png)
![Slide 2 image 4](images/0922/slide02-04.png)

**Speaker notes:**

- With release of Claude Opus 4.5 in early December of 2025, the power of coding agents skyrocketed
- They predicted it in 2025 and they have pretty much closed the gap
- Coding assistant → true agentic work
- Using AI in the workforce is a non-negotiable
- Agents are getting too good which introduces new challenges
- Hacky sack as a trend is back

## Slide 3

- What That Means For You
- Broader industry-wide AI adoption means companies need you
   - Becoming “AI-native” is now the new goal
- But…the floor is higher
- Software developers are more productive than they have ever been in history and so expectations have grown
- Focus on holistic systems-level thinking, architectures, and abstractions
   - When combined with AI-first development practices you will be irreplaceable
- themodernsoftware.dev

**Speaker notes:**

- While trend last year was removing of entry level roles because “AI will replace those roles”, now teams want to upskill and transform themselves to be more AI-native
- You guys were forged in this generation. Many of you started your CS journeys when ChatGPT just came out
- Many employers have adopted blanket policies like no hiring of L3/L4s. Or at the very least you must be L5 and above quality
- Students learning CS today can be an order of magnitude better than I was when I was learning. With AI coding an engineer can pick up tech stacks and tools at an unprecedented pace. What a time to be alive!
- If you think in terms of systems, understand business context, think through resilient architectures and abstractions, AI will strap a rocket to your back in terms of productivity

## Slide 4

- The Modern Software Developer
- themodernsoftware.dev

**Speaker notes:**

- Which brings us to this course…

## Slide 5

- This class is about principles not tools
- themodernsoftware.dev

**Speaker notes:**

- This is a class for fairly experienced engineers to truly become 10x engineers

## Slide 6

- 10 weeks in 1 slide
- themodernsoftware.dev

## Slide 7

- The Takeaway
- Human-agent engineering
   - Focus on the skills that are not yet replaced by AI systems
   - Business and product understanding
   - Become the tech architect  – develop good taste for software systems
   - Communication is crucial
- LLMs are only as good as you are
   - Good context leads to good code
   - If you can’t understand your codebase, neither will an LLM
   - Prevent AI slop
- Experiment aggressively
- themodernsoftware.dev

## Slide 8

- Course Logistics
- themodernsoftware.dev
- Instructor (Hi!)
   - Stanford undergrad/grad
   - Head of AI at Monaco, an SF-based startup in the sales space
   - AI Advisor for dozens of companies from seed-stage startups to public enterprises
   - Built first LLMs at Amazon Alexa
   - Founded and sold an ML education startup
   - Founded a YC-backed AI coding company
- 2 awesome CAs
   - Isaac Kan
   - Vijay Daita

![Slide 8 image 1](images/0922/slide08-01.png)
![Slide 8 image 2](images/0922/slide08-02.png)
![Slide 8 image 3](images/0922/slide08-03.png)
![Slide 8 image 4](images/0922/slide08-04.png)
![Slide 8 image 5](images/0922/slide08-05.png)
![Slide 8 image 6](images/0922/slide08-06.png)
![Slide 8 image 7](images/0922/slide08-07.png)
![Slide 8 image 8](images/0922/slide08-08.png)
![Slide 8 image 9](images/0922/slide08-09.png)
![Slide 8 image 10](images/0922/slide08-10.png)

## Slide 9

- Course Logistics
- https://themodernsoftware.dev
- Lectures
   - Tue/Thur 5:30-6:20 pm
- Deliverables
   - 6 assignments (1x/week) focusing on lecture material practice
      - https://github.com/mihail911/modern-software-dev-assignments
   - 3-4 contributions to OSS repositories
   - 1 final open-ended project in which you will exercise AI coding principles we cover
- Grading
   - 50/15/30/5 breakdown for project/assignments/OSS/participation
- themodernsoftware.dev

**Speaker notes:**

- All lecture materials on official course page
- Additional reading will be there
- Links to assignments
- This class is going to be hard

## Slide 10

- Course Logistics
- OSS Partners
   - 15 of the top AI-native open-source projects including Vercel, Warp, Marimo, Milvus, Pi, CrewAI, Browserbase, HeyGen, CopilotKit, Semgrep, OpenHands, Cmux, Arize, Sloth, Anyscale
- Guest Lectures
   - Founders and engineering execs leading top AI developer teams today (creators of Claude Code, Devin, Replit, Factory, and more)
   - Billions of dollars raised, tens of billions in valuation
   - Don’t miss these talks!
- themodernsoftware.dev

**Speaker notes:**

- The OSS partner assignments are designed to give you hands on experience working in and contributing to complex codebases

## Slide 11

- How to Build Claude Code in 200 Lines of Code
- themodernsoftware.dev

**Speaker notes:**

- In order to understand how to best develop with coding agents, we need to understand how agents are built. That will be the focus this week.

## Slide 12

- themodernsoftware.dev

![Slide 12 image 1](images/0922/slide12-01.png)
![Slide 12 image 2](images/0922/slide12-02.png)
![Slide 12 image 3](images/0922/slide12-03.png)
![Slide 12 image 4](images/0922/slide12-04.png)
![Slide 12 image 5](images/0922/slide12-05.png)
![Slide 12 image 6](images/0922/slide12-06.png)
- It’s that simple

**Speaker notes:**

- User interacts with coding agent client (windsurf, cursor, claude code) and runs a loop with an underlying llm. Sometimes the llm issues tool calls which the client executes (off-LLM)

## Slide 13

- Steps
- Read in terminal and keep appending to conversation
- Tell LLM what tools are available
   - It asks for tool use at appropriate time
   - You execute tool offline and return response
   - Tools
      - “Read_file”
      - “List_dir”
      - “Edit_file”
- themodernsoftware.dev

## Slide 14

- Let’s build a coding agent from scratch!
- themodernsoftware.dev

![Slide 14 image 1](images/0922/slide14-01.png)

## Slide 15

- themodernsoftware.dev
- Questions?
