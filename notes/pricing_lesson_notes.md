# 💰 Lyzr Platform Pricing & Token Economics

Understanding how Lyzr is priced, how Agent Processing Credits (APCs) work, and how to estimate deployment costs across SaaS and Virtual Private Cloud (VPC).

---

## 🎯 Executive Summary & Core Philosophy

The traditional way to price AI platforms is **per-agent** or with arbitrary **complexity tiers**. This approach creates friction because enterprise teams cannot accurately predict how many agents or tiers they will need prior to deployment.

Lyzr solves this by pricing on **tokens**—the exact same unit used by foundation model providers (OpenAI, Anthropic, Google). 

### Key Principles of Lyzr Pricing:
* **Parity with Model Pricing:** Cost is directly tied to token usage.
* **Zero Feature Gating:** Every customer receives access to the complete enterprise platform (RAG, Knowledge Graphs, SuperFlows, Guardrails, Memory).
* **Parity Across Deployments:** The exact same APC unit applies whether running on Lyzr SaaS or On-Premise VPC.
* **No Hidden Fees:** Zero markup on inference model costs.

---

## 🧠 What is an Agent Processing Credit (APC)?

An **Agent Processing Credit (APC)** is Lyzr's standardized billing unit. 

$$\text{1 APC} = \text{1 Token} \approx \text{4 Characters} \approx \text{0.75 Words}$$

### How a Single Execution Consumes APCs:
$$\text{Total APCs} = \text{Input Tokens} + \text{Output Tokens}$$

1. **Input Tokens:** Includes user query, agent instructions/system prompt, conversation history, retrieved Knowledge Base context, and tool definitions.
2. **Output Tokens:** The agent's generated response, reasoning steps, and tool arguments.
3. **Symmetric Rate:** Input and output tokens are billed at the **exact same 1:1 APC rate**, making cost forecasting straightforward.

---

## ☁️ Deployment Models: SaaS vs. On-Premise VPC

| Metric / Dimension | Lyzr SaaS (Shared Cloud) | Lyzr VPC (Private Cloud / On-Prem) |
| :--- | :--- | :--- |
| **Data Perimeter** | Hosted on Lyzr multi-tenant infrastructure | 100% inside your private cloud / data center |
| **Setup Fee** | **$0** (Instant Onboarding) | One-time upfront deployment fee |
| **Annual Subscription Base** | $100,000 / year (5 Billion APCs) | $250,000 / year (50 Billion APCs) |
| **Volume Efficiency** | ~50 Billion APCs per $1M | ~200 Billion APCs per $1M (4x Capacity per $) |
| **Best For** | Fast quarterly deployment & experimentation | Regulated enterprise & strict data residency |

---

## 🔑 Model Cost & Billing Transparency (BYOK vs. Pass-Through)

Lyzr never marks up foundation model inference costs. You choose how model execution is handled:

### Option A: Bring Your Own Keys (BYOK)
* You configure your own OpenAI, Anthropic, or Google API keys inside Lyzr.
* You pay Lyzr only for APC platform credits.
* Model providers bill your enterprise directly under your negotiated rates.

### Option B: Pass-Through Provisioning
* Lyzr provisions foundation models on your behalf.
* Model costs pass through at **exact list price with zero markup** as an itemized line item.

---

## 🔄 Carry-Forward & Rollover Protection

To eliminate the risk of under-utilization, **unused APC subscription credits carry forward** into subsequent years. Enterprise teams can commit to long-term capacity without fearing lost budget during ramp-up phases.
