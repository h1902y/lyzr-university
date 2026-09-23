# The Lyzr Stack

*Lesson 03 · Overview — Lyzr Overview & Offerings*

## What you'll learn

- Understand the 5 distinct layers that make up the unified Lyzr stack.
- Learn about deployment options across different cloud providers and on-premise hardware.
- Discover how models, frameworks, and visual builders interface with one another.

## Key concepts

**The Lyzr stack is structured into five cohesive layers.** This architecture guarantees that infrastructure, models, frameworks, SaaS applications, and whiteboard tools work together seamlessly.

**The infrastructure and integration layers form the bottom of the stack.** Lyzr can be deployed on AWS, Azure, GCP, or on-premise virtual machines, and natively integrates with multiple commercial LLMs, pre-trained models, and third-party tools.

**The agent framework, Studio, and Architect layers handle developer and user interaction.** While the framework deals with runtime execution, Studio provides a low-code visual builder, and Architect serves as a whiteboard planning canvas.

## In Studio

- Walk through the visual representation of the 5-layer Lyzr stack architecture.
- Identify where developers write SDK code versus where business teams interact with visual builders.

## Try this

1. List the primary differences between the infrastructure layer (hosting) and the integration layer (model access) in your system.
2. Map your own planned agent deployment to a specific cloud provider (such as GCP or AWS) or on-premise VM.

## Transcript

Now that you already know that it can put together multiple different types of solutions, let us see how the Lyzr stack is put together. At the bottommost layer of the stack is the infrastructure layer.  The infrastructure layer specifies where all Lyzr can be deployed.
It can be deployed on any of the cloud providers, be it Azure, AWS, or GCP. It can also be deployed on on-prem solutions like bare metal, virtual machines. On top of this infrastructure layer is the integration layer with multiple models and third-party tools. As an agent, it needs to have a model that powers the agent as well as it needs to interact with different third-party tools.
All of this integration is taken care of at this layer. Then comes the agent framework, the layer which takes care of how to develop and deploy the agents. And then comes the Lyzr agent studio layer. This is the layer which interacts directly with the client. You as the user of Lyzr will be working on the agent studio in order to develop agents, in order to put together the knowledge base and integrate the tools.
All of this will be done by the client or by the user at this layer. And then the topmost layer is architect. This is the white coding platform on which you can put to- out your thoughts as to what you want to build, and the architect takes care of building that application for you completely. It puts together a very nice front end with an agentic back end, and you get a working application right out of the box So together, the stack has five layers, and we will look at the Architect and the Studio.
