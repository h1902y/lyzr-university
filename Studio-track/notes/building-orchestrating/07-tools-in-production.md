# Tools in production

*Lesson 02 · Equip & Connect — Studio: Tools, Models & MCP*

## What you'll learn

- Securely authenticate custom tools using static API keys or dynamic OAuth 2.0 flows.
- Configure the secure ACI (Agent Connector Integration) card built on open-source `aci.dev` to handle refresh tokens automatically.
- Limit agent overhead by trashing unneeded actions from prebuilt integrations (like Slack's 800 actions).
- Balance open-ended agent autonomy against structured paths to optimize speed, context size, and token costs.

## Key concepts

**Most production APIs require secure authentication like static keys or OAuth.** Unlike public testing endpoints, production tools require credentials. Studio allows you to seed API keys directly in the default query parameters, keeping them completely hidden from both the LLM and the end-user.

**OAuth 2.0 is fully managed by Lyzr's integration infrastructure.** For complex user authorization (e.g., Gmail, Salesforce), Lyzr stores client IDs/secrets and automatically handles token refreshes, preventing connection timeouts when tokens expire.

**Trimming unneeded actions is the easiest way to cut agent latency and token cost.** A standard integration like Slack carries hundreds of default actions. Activating all of them inflates the prompt context window and causes reasoning lag. Deselecting unused actions optimizes performance.

**Autonomy is a dial you tune based on the task.** If the agent is doing open-ended task solving, let it carry a wide range of actions. If the agent runs on a fixed, known road, trim it down to only the exact actions required to do the job.

## In Studio

Studio feature: **Build → Custom Tool** and **Connections → Integrations**. Here's how to configure authenticated tools and limit active actions:

1. Go to **Build** and select **Custom Tool**. Choose **OpenAPI** and paste your spec.
2. In the configuration fields, locate **Default Query Parameters** (or headers) and insert your API key once. The key will carry automatically with every request.
3. For OAuth setups, choose the **Custom ACI Tool** card. Input your Client ID, Client Secret, Scope list, Authorize URL, Token URL, and Refresh URL.
4. Attach a prebuilt integration (e.g., Slack) to your agent. Open the integration's settings panel.
5. Review the active list of actions. Uncheck the checkboxes next to actions the agent does not require to do its job.
6. Click **Save** to deploy the authenticated, lightweight tool suite.

## Try this

1. Create a custom tool that uses a public API requiring an API key (e.g., NASA Picture of the Day API using `DEMO_KEY`). Verify that the key is stored in the default query parameters and does not leak in the chat traces.
2. Attach the **Slack** integration to an agent. Go to its action registry and deselect everything except `post_message` and `read_message`. Observe the change in available tool definitions.
3. Contrast a "full-roam" agent with a "trimmed" agent—explain when you would use each.

## Transcript

In the tools video, I turned an API into a tool, but two questions come up the second you take that to production. One, my real API needs keys and OAuth. How does the agent authenticate? And two, a ready-made integration comes with dozens of actions. Do I really want my agent carrying all of them? Both have clean answers. Let me show you. First, authentication. In the tools video, our API was open. No key needed. Most real APIs aren't, so let's build one that needs a key. Same flow as before: new custom tool, OpenAPI, paste the spec. The only new move is here in the default query parameters. I give it the API key once. Now, every call this tool makes carries that key automatically. The agent never sees it, never asks for it, and nobody chatting with the agent ever needs it. I'm using NASA's public demo key here and their Picture of the Day API. I attach it, tell the agent when to reach for it, and ask about today's astronomy picture. And there it is, the red glow of the Cosmic Bat Nebula. Now look at the events panel. Tool called, tool responds. A real authenticated API answered that. Key attached, and the key never appeared in the conversation. That covers API keys, but the heavier case is OAuth. Think Gmail, Salesforce, anything where a user signs in and tokens expire. For that, there's the second card, the custom ACI tool built on aci.dev, which is open source. Look at what it takes. Your client ID and secret, the scopes, the authorize and token URLs, and this one, the refresh token URL. That's the part you never want to build yourself. Lyzr stores the token securely and refreshes them for you so the connection doesn't die when a token expires. Second question, actions. Open any ready-made integration and look at how much it can do. This is Slack, and it's around 800 actions. When you add an integration, Lyzr turns all of them on by default, and that's deliberate. You give the agent a task, and it figures out the route itself the way you'd expect a modern agent to. No wiring individual actions by hand. But all on isn't always what you want. Every action the agent carries is context it has to read on every run. That's tokens, credits, and also latency. So when your agent only ever travels one road, trim it down. When you attach the integration to an agent, you can deselect the actions it doesn't need and keep just the ones it does. Same integration, a fraction of the overhead. Let the agent roam when the task is open-ended and pin it down when the road is known. So that's tools production grade: keys and OAuth handled by the platform, refresh tokens included, and you decide exactly which actions your agent carries. Give it everything when it needs to figure things out, trim it down when it doesn't. That's the difference between a demo and something you ship. I am Felipe.
