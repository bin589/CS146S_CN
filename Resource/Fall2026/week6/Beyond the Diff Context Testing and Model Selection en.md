# How to build a code review agent

> 课程阅读标题：Beyond the Diff: Context, Testing, and Model Selection
> 作者：Daksh Gupta（Greptile）
> 原文：<https://greptile.com/blog/how-to-build-a-code-review-agent>（2026-10-09）
> 抓取时间：2026-10-29
> 说明：改编自作者 2026 年 10 月在 AIE NYC 的演讲；英文存档来自公开博文 HTML 抽取。版权归原作者所有。

Adapted from a talk I gave at AIE NYC in October 2026

My name is Daksh. I’m one of the cofounders of Greptile. We build agents that review and test pull requests , catching logic and security bugs before merge.

*[Figure omitted: Building an AI code review agent]*

Thousands of companies like Nvidia and Coinbase use Greptile to check their changes before merge. To give you a sense of scale, more than 1% of PRs on GitHub go through Greptile each day.

*[Figure omitted: More than 1% of GitHub PRs]*

There are three main reasons companies choose Greptile.

1. First, codebase context: Greptile is very good at indexing large codebases, so it can catch complex bugs that are not in the diff but second order effects of the diff.
1. Second, Greptile runs your code: most code review agents are really just using frontier models to read the code to find bugs. Greptile actually installs your dependencies and spins up a dev server in a sandbox, clicks around, mocks API inputs, pressure tests endpoints to find things that AI alone could never catch.
1. Third, we’re really good at allocating inference. We use the right-sized model, both frontier and open source, for each subtask of the code review and testing process. We also give agents an array of specialized tools to check code. By doing this, we can get better results than pure Codex or Claude Code review at a tenth of the cost.
*[Figure omitted: Why Greptile]*

Every now and then, however, companies have very specific needs that we’re not well set up to serve yet. In those situations, they decide to build their own internal code review solution.

When they do - we like to help them with it, completely for free. We get to learn a lot from the process about how we can serve customers like them in the future. They get our expertise in building great review agents.

Today, I am going to share some of that expertise with you. This is going to be helpful for two types of people:

1. You work at a large company and want to build your own AI code review tool
1. You are choosing an AI code review tool for your company and want to know how they work so you can make a more educated decision.
*[Figure omitted: Who this is for]*

Alright, let’s dive right in.

## Basic workflow

At the core, you will need some type of sandbox running an agent. It will receive webhooks from GitHub when there are new pull requests ready for review. You can use Codex or Claude Code for this, or something like Pi or OpenCode if you want to be model-agnostic. It will analyze the changes, detect bugs, and post comments back to GitHub.

*[Figure omitted: Basic workflow]*

You can probably build this in a day.

You will notice a couple of things go wrong:

1. It will miss a lot of bugs, and you won’t know what it’s missing (it will be hard to evaluate and improve it)
1. It won’t deeply understand your codebase and product, particularly if it spans multiple repos
1. It will be very expensive (at least $3-5, up to $10-20 per run, and it will be run 2-3 times per PR)
1. It will make a lot of nitpicky comments which will annoy engineers
1. It will keep finding new bugs every time you run it instead of reporting everything at once
*[Figure omitted: Then you run it]*

Let’s address all of these one by one.

## Improvement 1: Optimizing the prompt

*[Figure omitted: The prompt]*

The lowest hanging fruit is to make the prompt better. You can instruct it to look for specific types of bugs, and also specifically tell it not to make nitpicky comments.

You can get quite far with this, but it’s surprisingly hard to evaluate if your improvements are working. Evaluating review agents is very hard because true bugs are very rare.

*[Figure omitted: Bugs are rare]*

No single company has enough PRs moving through to be able to iterate the agent’s performance. Greptile has the advantage of having millions of PRs going through it every month, so we can monitor and detect if our changes are improving the rate of bugs being caught or not. One way you can improve your mileage is by building a dataset of historic PRs with a diversity of bugs and hillclimb those.

*[Figure omitted: A dataset of historical PRs]*

## Improvement 2: Model optimization

If your company uses Claude to code, and you used Claude models for review, they will miss a lot of bugs. This is because the author and reviewer will have similar blind spots. As an example, Claude models are twice as likely as GPT models to introduce n+1 errors, and are also around twice as likely to miss them during review.

You should consider using Codex models to review Claude’s code and vice versa.

This is easy if your company only uses one coding model. If everyone is on Claude, use GPT models in your review agent.

In case you use multiple, you’ll have to develop a router/classifier that can detect the author’s model and flip the review model.

*[Figure omitted: Different author, different reviewer]*

In our research on model inversion , bug catch rates go up ~10% when you do this. That number might seem small, but every additional bug that doesn’t reach your customers is a big deal.

*[Figure omitted: Higher bug catch rate in Greptile’s research]*

Greptile of course does model inversion out of the box.

## Improvement 3: Codebase context

In spite of everything, your review agent will likely not understand your codebase. This will lead it to make false positive comments, or more importantly, entirely miss complex chained bugs. A common example is auth bypasses, which are often introduced by accident and catching them requires a pretty intricate understanding of how auth works in the application.

*[Figure omitted: Codebase context]*

The review agent will also not fully understand intent. Sometimes code is perfectly correct but either does the wrong thing, or an incomplete thing.

*[Figure omitted: Correct code can still do the wrong thing]*

You can resolve this in two steps:

- build an MCP gateway to give it access to your docs and your Jira, Linear, docs etc.
- build a codebase indexer
*[Figure omitted: Two pieces of context]*

Building a codebase indexer is pretty involved. One way to do it is to have agents crawl your codebase periodically and maintain some type of wiki. This is roughly what Greptile does.

You should also track reverts and incidents and store them in your wiki. This way your review agents will know what has gone wrong in the past, and prevent mistakes from being repeated. This involves building some type of integration layer with your telemetry stack.

You can inject this wiki into the agent’s sandbox, allowing it to go in with an understanding of the codebase and the product, leading to more bugs caught and fewer false positives.

*[Figure omitted: A wiki the agent can use]*

## Improvement 4: Autonomous testing

Imagine you wanted to build a system to catch UI bugs in a web application. Maybe you want to make sure certain buttons are not hidden when the site is opened on an iPhone. In theory, you could shove the React diff into a very smart model, let it spin for a bit, and tell you if the code is buggy. A much better way to do this is to spin up a dev server, open a browser, and use computer use to click through every path, ensuring it works.

*[Figure omitted: Does the button work on an iPhone?]*

Fortunately, frontier models are quite good at computer use. The parts you’ll need to build are:

1. Very good dev boxes which can be configured to make it easy to quickly spin up a PR branch to test it
1. A mapping of codebase sections to testable user flows
For the former, we went with large configurable VMs, but even so we usually need FDEs from our team to go in and help customers set up these VMs.

For the latter, we use our knowledge base , where Greptile tracks the flows related to each part of the codebase. You should be able to use AI to produce this.

*[Figure omitted: Two things to build]*

## Improvement 5: Use cheaper models for some things

If you do all of the above, you’ll start to see good results, but each review run will likely cost you anywhere from $2 to $20 in token costs. Since your reviewer is likely to run on every push to a PR branch, this can add up pretty quickly.

*[Figure omitted: Token costs per review run]*

Fortunately, reviewing and testing a PR is made up of a pretty consistent set of subtasks. That means you can pick the perfect model for each subtask and drastically reduce costs and maintain/improve performance vs. using only frontier models.

*[Figure omitted: A model for each subtask]*

As an example, much of the token use in review is file reads. A majority of the files read are clearly not relevant to the change, but the model only discovers this after reading the file. Using a very light and cheap model for this can greatly reduce the cost of file reads, and a narrower, higher signal set of files can then be passed into the frontier model.

*[Figure omitted: Fewer irrelevant file reads]*

A great code review agent combines codebase context, testing, reliable evaluations, and the right model for each task to catch bugs efficiently.
