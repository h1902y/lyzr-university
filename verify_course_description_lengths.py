desc1 = "Master the fundamentals of the Lyzr Enterprise Agent Platform. Learn how autonomous agents, private RAG knowledge bases, deterministic guardrails, and MCP tool servers interact to deliver production-ready AI workflows across your organization."
desc2 = "Design, govern, and deploy enterprise AI agents visually using Lyzr Agent Studio. Build complex multi-agent SuperFlow orchestrations, attach knowledge bases, and simulate agent behaviors without writing a single line of code."
desc3 = "Build production-grade autonomous agent microservices using the Lyzr ADK Python SDK. Implement multi-provider model switching, custom RAG pipelines, Pydantic structured outputs, and Model Context Protocol (MCP) server integrations."

descs = [
    ("Lyzr Foundations", desc1),
    ("Lyzr for Business Professionals", desc2),
    ("Lyzr for Technical Professionals", desc3)
]

print("==========================================================================")
print(" 📏 VERIFYING COURSE DESCRIPTION CHARACTER LENGTHS (MAX 250 CHARS)")
print("==========================================================================")

for name, text in descs:
    print(f"• Course: {name}")
    print(f"  Length: {len(text)} characters")
    print(f"  Text:   \"{text}\"")
    print("-" * 70)
