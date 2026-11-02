# Augment Cosmos code review

> 来源：<https://www.augmentcode.com/blog/solving-code-review-with-cosmos>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。
TL;DR. When agents write 100% of your code, the bottleneck moves to review: at one point we had 1,400 open PRs and a 20-hour median time-to-first-comment. We rebuilt the review process on Cosmos as a team of agents that auto-approves low-risk changes, runs line-by-line correctness analysis, and pulls humans in only for the calls that need judgment. Since January, code output is up 3x, median merge time has dropped, and bug rate per output unit is trending down.
Teams that go all-in on AI coding tools hit the same wall. Raw code output grows exponentially, and PRs pile up in the review queue. Someone's whole job could be reviewing PRs and it would still make no dent. Some companies solve this by rubber stamping PRs to keep moving fast, but shipping faster with bugs and uncontrolled tech debt is a one-way road to chaos.
Here is how we solved our code review bottleneck and started merging PRs at the same rapid rate that we were generating them. We did this without compromising on the quality of the software nor our reviewers’ understanding of the PRs they reviewed. This was a fundamental rethink of how code reviews are done. Let's dig in.
How bad it got
We hit the code review wall at Augment in January. With 100% of our code being written by agents, PRs generated shot up, but so did the median merge time (i.e. PR latency). PR merge rate (i.e. PR throughput) went up, but not at the pace at which they were being generated. PRs started piling up in the review queue and there were over 1,400 open PRs at one point. We had a real problem.
Our median time-to-first-human-comment was hovering around 1,200 minutes. That's 20 hours before an engineer even looked at your PR. This wasn't a reviewer problem. They had six PRs ahead of yours, each 400 lines of code they didn't write. Our original AI code review tool ran in 3-5 minutes and caught real bugs, but a human still had to read every line of every PR. A two-line change ended up waiting a day at the bottom of the queue.
Our VP of Engineering called it out: the main bottleneck was confidence: a human reviewer needed to read and reason about every single line of code to gain confidence in the quality of what was being shipped, and develop an understanding of the system being built. This was what we had to solve.
How we solved our code review problem
A couple of months ago, Augment internally rolled out Cosmos, our operating system for agentic software development: agents that run anywhere, work across your SDLC, with humans steering where judgment matters. It is purpose built for automating workflows, with several out-of-the-box feature for teams like shared context and memory, self-improving agent loops, connections to all of your tools, etc. Each Cosmos automation comes in the form of an Expert, which has its own prompt, integrations, environment, secrets, event triggers, subscriptions, worker experts and much more. Code review was naturally the first automation we went after.
The figure below highlights our new code review process: a team of Experts drives the code review process and pulls in the human only when needed. It splits the code review process into four coordinated loops: change execution (PR Author), risk analysis (PR Risk Analyzer), correctness (Bug Reviewer), and system design judgment (Pair Reviewer + human; Pair Reviewer was previously known as Intent Reviewer), all continuously improving via shared memory.
Augment's new code review process on Cosmos
PR Risk Analyzer
Evaluates the risk for every new PR automatically and routes it appropriately.
- Low-risk changes (docs, configs, trivial edits) → automatically approved with justification**
- Higher-risk changes → tagged with specific review dimensions (e.g. architecture, security) that need human input
👉 Removes low-value queue work and ensures humans only see what requires judgment. Initially, we saw 10% of PRs automatically approved, but this number goes up once developers start providing feedback on what type of PRs are low-risk.
**talk to us to understand how to maintain SOC-II compliance with agent approved PRs.
Pair Reviewer (Interactive)
Owns the review process end-to-end and engages the human only when needed.
- Breaks the review into structured phases (design, risk, correctness, etc.)
- Guides the human through decisions instead of requiring full code diff review
- Posts finalized comments back to GitHub
- This is the only part of the code review process requiring human input
👉 Shifts humans from line-by-line reviewers to decision-makers.
Deep Code Review
- Performs deep, line-by-line correctness analysis focused purely on objective bugs
- This is the component most similar to a standalone AI code review tool (Akshay wrote a separate post on the engineering behind the review agent.)
👉 Catches the vast majority of high and medium severity issues with very high recall.
PR Author
Owns the execution loop of the PR lifecycle.
- Given a feature request in a ticket or specification, it implements the feature and opens a PR
- Automatically responds to review comments, fixes CI failures, resolves merge conflicts, and puts up subsequent commits
- After providing a ticket link or specification, the human developer only needs to come in to give the final merge decision
👉 Removes the author-side bottleneck and keeps PRs moving without manual intervention.
Memory Manager
Learns from every PR to continuously improve the system.
- Captures human feedback from merged PRs - human comments, replies to bot comments, thumbs up/down emojis and sessions with the Pair Reviewer - and distills it into a structured, per-repo knowledge base that all experts ingest before starting their work
- A deep-dive into the memory system will be discussed in an subsequent blog
👉 Ensures the system gets better to match your company’s specific practices or preferences so that over time less and less human intervention is needed.
Did it work?
Our Weave charts tell the story: while code output at Augment has gone up over 3x since January, median merge time has actually decreased.
Weekly code output more than tripled from November to April while median PR merge time fell by roughly two-thirds.
Bugs introduced have been steady over time even though we've been pushing significantly more code. The raw count didn't spike which many would expect. Bugs per output unit is tapering down. Quality is maintained.
Bug-introducing commits per output unit dropped from a mid-January peak of 0.097 to 0.006 by April 6.
Weekly revert rate is healthy - we aim for it to be 1.5%, and we hover around +/- 0.5%.
The revert rate stayed below the 1.5 threshold in 20 of 25 weeks, with no exceptions after late January.
Finally there are two effects that we can’t capture in numbers; in spite of shorter review times:
- Humans are still driving high-level system design because they have better organizational and business context.
- Reviewers continue to get the knowledge transfer benefit of code review.
How you can do this too
If AI has spiked the volume of code generated, the goal isn’t just “faster reviews.” It’s building a review system that scales: automate low-level correctness, reserve humans for judgment calls, and eliminate low-risk queue work. You can do all of this using Augment’s Cosmos Platform, which is in public preview. Just prompt the platform’s Cosmos Advisor Expert saying “Set up the code review automation fleet for me” and it will build up this suite of code review experts for you and help you customize them to your unique requirements and setup.
After solving the code review bottleneck at Augment, we’ve moved on to automating our subsequent SDLC bottlenecks internally, including end-to-end testing, incident response, feedback triage, and ticket management, all deployed on the Augment Cosmos Platform. Stay tuned for upcoming blogs about those.
Written by
Akshay Utture
Akshay Utture builds intelligent agents that make software development faster, safer, and more reliable. At Augment Code, he leads the engineering behind the company’s AI Code Review agent, bringing research-grade program analysis and modern GenAI techniques together to automate one of the most time-consuming parts of the SDLC. Before Augment, Akshay spent several years at Uber advancing automated code review and repair systems, and conducted research across AWS’s Automated Reasoning Group, Google’s Android Static Analysis team, and UCLA. His work sits at the intersection of AI, software engineering, and programming-language theory.
Will Colbert
Member of Technical Staff
Will Colbert is a Member of Technical Staff at Augment Code, where he works on Cosmos and Code Review. Previously, he spent three years at Quicken developing consumer fintech products, most recently as a Senior Software Engineer. Before that, while at UC Davis, he co-founded MTools and Profits IO, platforms that helped drive over $1.8M in StockX affiliate sales.
