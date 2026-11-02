# Atlassian Remote MCP Server

> 来源：<https://www.atlassian.com/blog/announcements/remote-mcp-server>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。
It’s our calling to help all kinds of teams plan, track, and align their work to goals to get the most out of enterprise knowledge. Over the past year, we’ve invested heavily in enabling AI-powered Rovo Search, Chat, and Agents to help our customers do just that. Our secret sauce? Teamwork Graph — a powerful data intelligence layer that connects and makes sense of all your Atlassian and third-party data, from your work to your knowledge, teams, and goals.
Now, we’re further extending that value by connecting your enterprise knowledge to more places where you already work, whether that’s an LLM, an IDE, or another agent platform. We know tons and tons of you have been clamoring for it, so we’re pretty jazzed to introduce our new Remote MCP Server in beta, which will serve as the bridge into that future.
Connect your enterprise knowledge to more AI tools
That’s right! We’re bringing Atlassian’s structured knowledge into more AI tools thanks to MCP, which provides a universal, open standard for connecting AI systems with data sources. With our Remote MCP Server, you can summarize work, create issues or pages, and perform multi-step actions, all while keeping data secure and within permissioned boundaries.
We’re building our Remote MCP server with industry leaders who share our commitment to security and innovation. Starting with Anthropic as our first official partner and hosted on Cloudflare infrastructure, Jira and Confluence Cloud customers can now interact with their data directly from Claude, Anthropic’s AI assistant.
At Atlassian, it’s in our DNA to be open by design, play as a team, and contribute to healthy software ecosystems that give our customers more choices. MCP hits every one of these notes—it is a powerful open standard with a fast-growing and diverse community that has key implications for human-AI collaboration, extensibility, and meeting teams where they work. We’re excited to be a part of this ecosystem and play a role in expanding what’s possible with MCP. We can’t wait to see what our customers do with it.”
— Rajeev Rajan, Atlassian Chief Technology Officer
Jira and Confluence get the MCP treatment… with more to come!
Starting today, you can access information from Jira and Confluence wherever you use Claude to do all sorts of things like:
- Summarize Jira work items or Confluence pages
- Create Jira work items or Confluence pages directly from Claude
- Get the model to take multiple actions in one go, like creating issues or pages in bulk
- Enrich Jira work items with context from many different sources that Claude has access to
- And so much more!
The best part? We’re just getting started… Keep your eyes peeled for more connected Atlassian apps coming soon.
Enterprise knowledge shouldn’t be trapped in silos – it should flow naturally through the tools teams already use. With Atlassian’s Remote MCP Server, teams can access their Jira tickets and Confluence documentation conveniently within Claude. This means less context switching, faster decision-making, and ultimately, more time spent on meaningful work. Together with Atlassian, Anthropic is helping to make enterprise data work harder for the people who rely on it.”
— Scott White, Anthropic product lead
Securely access Atlassian data in external AI tools
Unlike locally hosted MCP servers, our Remote MCP Server is run by Atlassian to ensure a secure, supported experience. As always, we’ve embraced privacy by design in building it, so you can rest easy knowing it features OAuth authentication and respects all your existing permission controls.
To further ensure your enterprise data stays secure while enabling powerful integrations, our server will soon integrate with additional trusted and thoughtfully curated AI partners that support remote MCP. Stay tuned for more.
Open innovation is the name of the game
Atlassians are nothing if not team-oriented, and we know that the future we are building with AI is impossible alone. So you can imagine how much we’ve enjoyed joining other industry leaders in rallying around MCP from Anthropic. We also aren’t prone to hyperbole, so when we tell you that this open framework has had a meteoric rise, we mean it. MCP has quickly become the gold standard for how LLMs interact with tools, and the ecosystem it’s forming has some really cool implications for agents, scaling interoperability, and building in the AI era. We’re pumped to play a role in expanding what’s possible with MCP.
In addition to teaming up with Anthropic, we’re using Cloudflare’s Agents SDK to build our Remote MCP Server. Cloudflare provided everything from OAuth to out-of-the-box remote MCP support so we could quickly build, secure, and scale a fully operational setup.
Try it today!
Ready to get started? You can try the Atlassian Remote MCP Server today in beta with Claude in Jira and Confluence. Learn more about our server here, and let us know what other providers you’d love to use it with—this is only the beginning.
