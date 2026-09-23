# Deploy — ship it

*Lesson 06 · Foundations · The Agent Lifecycle*

## What you'll learn

- Find your agent's ready-made API on the Deploy tab — it's been live since creation, with nothing to spin up
- Choose between two ways to put an agent in front of people: an API embed for developers, or a published App Store app you ship straight from Studio
- Publish your support agent to the Lyzr App Store under the right category and get a shareable app
- Recognise the build-govern-test-deploy loop as complete, with only monitoring left to close it

## Key concepts

**Your agent was live behind an API the moment you created it — there is no deploy step.** This is the surprise of the lesson. Building the agent in Studio already exposed it as a callable endpoint; the Deploy tab just shows you it's "deployed and ready to use." Shipping isn't an action you perform on the agent, it's a decision about how you put it in front of people.

**There are two distribution paths, and you pick based on your audience.** If you have developers, the Deploy tab hands you a ready-made API you drop straight into a website or app. If you'd rather not touch code, you publish the agent to the Lyzr App Store right from Studio, where it becomes its own shareable app. Same agent, two front doors.

**Publishing to the App Store means picking a category, not writing config.** In the launch configuration you choose the category that fits the agent — for a support agent, customer experience is the right home — then hit Publish. That single choice in the Studio UI is what makes it discoverable and shareable as an app.

**Five lessons in, the lifecycle loop is almost closed.** You went from a blank page to a governed, tested, and published agent in a few minutes: build, equip, govern, test, deploy. The only open question is how the agent behaves once real people start using it — which is exactly what monitoring and traces answer next.

## In Studio

Studio feature: **Deploy · Lyzr App Store**.

1. Open the **Deploy** tab for your support agent. It already reads as deployed and ready to use — confirmation the agent has been live behind an API since creation.
2. Note the **ready-made API** shown here. This is the endpoint a developer would drop into a website or app; no extra deploy step is needed to make it work.
3. To ship it as a standalone app instead, click **Publish**.
4. In the **launch configuration**, choose a **category**. Since this is a support agent, pick **Customer Experience**.
5. Hit **Publish**. The agent is now published — live and shareable as its own app in the Lyzr App Store, all from the Studio UI.

## Try this

1. Open the Deploy tab on your support agent and *locate the ready-made API* before you publish anything — confirm for yourself that the agent was already live, with nothing for you to start.
2. Publish the agent to the Lyzr App Store under the **Customer Experience** category, then open the resulting app and send it one in-doc question (e.g. *the return window for an unopened laptop*) to confirm the published app behaves the same as the Playground did.
3. *Optional:* publish a second throwaway agent under a different category and notice how the category choice changes where it lands in the App Store — this is the only knob that controls discoverability.

## Transcript

We've built, equipped, governed, and tested our agent. Now we ship it. And here's the nice surprise with Lizr. There's no big deploy step at the end. The moment you created this agent, it was already live behind an API. So deploying is really about choosing how you put it in front of people. On the Deploy tab, you can see it. Your agent is deployed and ready to use. There are two ways to take it live. If you have developers, there is a ready-made API you drop straight into a website or app. But you don't need code at all. You can publish the agent right to the Lizr app store and share it as its own app. That's what I'll do here. I'll click Publish, and in the launch configuration, I'll choose a category. Since this is a support agent, customer experience is the right fit. Then I hit Publish. And that's it. Agent published. A support agent is now live and shareable with no code required So in just a few minutes, we went from a blank page to a governed, tested, and published agent. The only question left is how it's doing once real people start using it. That's the final video: monitoring and traces. I'm Filippo with Lyserv. See you there
