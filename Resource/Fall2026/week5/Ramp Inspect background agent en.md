# Why We Built Our Own Background Agent (Ramp Inspect)

> 来源：<https://engineering.ramp.com/post/why-we-built-our-background-agent>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。
> Static HTML extract was thin; body reconstructed from a readable fetch of the public post.
We built our own background coding agent: Inspect. Inspect writes the code like any other coding agent, but closes the loop on verifying its work by having all the context and tools needed to prove it, as a Ramp engineer would.

For backend work, it can run tests, review telemetry, and query feature flags. For frontend, it visually verifies its work and gives users screenshots and live previews. Agents should have agency, and so we made sure Inspect is never limited by missing context or tools, but only by model intelligence itself.

Each session runs in a sandboxed VM on Modal with everything an engineer would have locally: Vite, Postgres, Temporal, the works. It’s wired into Sentry, Datadog, LaunchDarkly, Braintrust, GitHub, Slack, and Buildkite. It supports all frontier models, MCPs, custom tools, and skills that encode how we ship at Ramp. This also lets builders of all backgrounds, contribute with the tooling and setup an engineer would.

Because Inspect sessions are fast to start and effectively free to run, you can use them without rationing local checkouts or worktrees. A builder can kick off multiple versions of the same prompt, and just see which one lands. They can try different approaches or swap models without thinking twice. There’s no limit to how many sessions you can have running concurrently, and your laptop doesn’t need to be involved at all.

This also means you can capture ideas the moment you have them. Notice a bug while winding down for the night? Kick off a session, talk to it if you want (we added voice), and check the PR in the morning.

The interface understands that people rely on a rich variety of workflows. You can chat with Inspect in Slack and send it screenshots, use the Chrome extension to highlight specific changes to elements, prompt it on the web interface, discuss on the Pull Request, and even drop into a web-based VS Code editor to make manual changes. All changes are synced to the session, so you never lose your work while switching around. Plus, every session is multiplayer. Send your session to any colleague, and they can help take it home.

We want Inspect sessions to be fast, and session speed should only be limited by model-provider time-to-first-token. Everything else, like cloning and installing, is done before you start your session. When background agents are fast, they’re strictly better than local: same intelligence, more power, and unlimited concurrency. You can go home and let Inspect cook (and if you’re so inclined, resume after dinner from your couch and mobile phone).

Internal adoption charts have been vertical: ~30% of all pull requests merged to our frontend and backend repos are written by Inspect. It only took a couple months for us to reach this level of usage, and it continues to grow. We didn’t force anyone to use Inspect over their own tools. We built to people’s needs, created virality loops through letting it work in public spaces, and let the product do the talking.

We think anyone should be able to build this. Owning the tooling lets you build something significantly more powerful than an off-the-shelf tool will ever be. After all, it only has to work on your code. To make this easy to replicate, we’ve written a spec of what we’ve built so far. Paste the link to this post into a coding agent and let it begin building.

## Sandbox

At the core of a hosted coding agent is the execution environment. Whenever you start a new coding session, you want to spin up a new sandbox that has a full development environment. Modal sandboxes start near instantly; file system snapshots freeze and restore state. Approach: image registry per repo; rebuild every 30 minutes (clone, install, setup); snapshot; start sessions from snapshot (≤30 min stale); snapshot again after changes.

Recommend OpenCode as the agent runtime (server-first, typed SDK, plugins). Optimizations: warm sandbox as user types; allow reads before sync completes but block edits until sync done; move as much as possible into image build; queue follow-up prompts; allow spawning child sessions.

## API

API should support many clients with synchronized state and multiplayer. Cloudflare Durable Objects (per-session SQLite) + Agents SDK for streaming. Auth via GitHub so PRs open as the user. Sandbox pushes; API opens PR with user token. GitHub webhooks keep PR state.

## Clients

Slack (classifier for repo, Block Kit, custom emoji), polished web client (hosted VS Code in sandbox, streamed desktop view, stats), Chrome extension for visual React edits (DOM/React tree rather than raw screenshots).
