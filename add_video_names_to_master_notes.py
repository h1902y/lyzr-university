import re

master_path = '/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/master_courses_lesson_notes.md'

video_map = {
    # Course 1
    '01-introduction-to-lyzr.md': '01a Introduction to Lyzr Platform.mp4',
    '02-client-success-stories.md': '02a Client Success Stories.mp4',
    '03-the-lyzr-stack.md': '03a The Lyzr Stack and Architecture.mp4',
    '04-architect.md': '04a Architect Overview.mp4',
    '05-studio.md': '05a Studio Overview.mp4',
    '06-lyzr-capabilities.md': '06a Lyzr Capabilities.mp4',
    '07-computer-agent.md': '07a Computer Agent.mp4',
    '08-git-agent.md': '08a Git Agent.mp4',
    '09-designing-knowledge-bases-and-source-selection.md': '09a Designing Knowledge Bases and Source Selection.mp4',
    '10-pdf-parsing-strategies-and-tabular-extraction.md': '10a PDF Parsing Strategies and Tabular Extraction.mp4',
    '11-retrieval-algorithms-basic-mmr-and-hyde.md': '11a Retrieval Algorithms Basic MMR and HYDE.mp4',
    '12-wiring-kb-to-agent-and-execution-traces.md': '12a Wiring KB to Agent and Execution Traces.mp4',
    '13-introduction-to-tools-and-mcp-servers.md': '13a Introduction to Tools and MCP Servers.mp4',
    '14-configuring-tavily-mcp-server.md': '14a Configuring Tavily MCP Server.mp4',
    '15-integrating-gmail-and-email-action-tools.md': '15a Integrating Gmail and Email Action Tools.mp4',

    # Course 2
    '01-welcome-agent-studio-lifecycle.md': '01a Welcome to Agent Studio and Lifecycle.mp4',
    '02-build-choose-type-create-agent.md': '02a Build Choose Type and Create Agent.mp4',
    '03-equip-model-tool-knowledge.md': '03a Equip Model Tool Memory Knowledge.mp4',
    '04-govern-add-guardrails.md': '04a Responsible AI and Guardrails.mp4',
    '05-test-simulation-engine.md': '05a Agent Simulation and Observability.mp4',
    '06-deploy-ship-it.md': '06a Deploying Enterprise Agents.mp4',
    '07-project-one-agent-full-lifecycle.md': '07a Project One Agent Full Lifecycle.mp4',
    '01-what-agent-type-to-build.md': '04a What Agent Type Should I Build.mp4',
    '02-lyzr-manager.md': '05a Lyzr Manager Orchestration.mp4',
    '03-managers-agent-page-editing.md': '05b Managers Agent Page Editing.mp4',
    '04-superflow-invoice-reconciliation.md': '06a SuperFlow Basic and Dynamic Flows.mp4',
    '05-superflow-loops.md': '07a SuperFlow Advanced Routing and Loops.mp4',
    '06-models-in-depth.md': '06b Models in Depth.mp4',
    '07-tools-in-production.md': '07b Tools in Production.mp4',
    '01-rag-in-studio.md': '08a RAG in Studio.mp4',
    '02-build-a-knowledge-base.md': '09a Build a Knowledge Base.mp4',
    '03-document-parsing-and-ingestion.md': '10a Document Parsing and Ingestion.mp4',
    '04-data-connectors-as-live-sources.md': '11a Data Connectors as Live Sources.mp4',
    '05-agent-memory-in-depth.md': '12a Agent Memory in Depth.mp4',
    '06-beyond-vectors-structured-knowledge.md': '13a Beyond Vectors Structured Knowledge.mp4',
    '07-build-a-knowledge-graph.md': '14a Build a Knowledge Graph.mp4',
    '08-the-semantic-model-and-global-context.md': '15a The Semantic Model and Global Context.mp4',
    '09-project-document-qa-agent-with-memory.md': '15b Project Document QA Agent with Memory.mp4',
    '01-responsible-ai-in-studio.md': '16a Responsible AI and Guardrails.mp4',
    '02-the-simulation-engine.md': '17a Agent Simulation and Observability.mp4',

    # Course 3
    '01-what-is-a-lyzr-agent.md': '01a What is a Lyzr Agent.mp4',
    '02-your-first-agent.md': '02a Your first Agent.mp4',
    '03-swapping-llm-providers.md': '03a Swapping LLM Providers.mp4',
    '04-streaming-responses.md': '04a Streaming Responses.mp4',
    '05-structured-outputs.md': '05a Structured Outputs.mp4',
    '06-project-multi-provider-chatbot.md': '06a Project Multi provider chatbot.mp4',
    '07-image-generation.md': '07a Image generation.mp4',
    '08-file-generation.md': '08a File generation.mp4',
    '09-project-creative-assistant.md': '09a Project Creative Assistant.mp4',
    '10-what-is-rag.md': '10a What is RAG.mp4',
    '11-document-ingestion.md': '11a Document ingestion.mp4',
    '12-vector-stores-and-retrieval.md': '12a Vector stores and retrieval.mp4',
    '13-agent-memory-basics.md': '13a Agent memory basics.mp4',
    '14-conversation-memory.md': '14a Conversation memory.mp4',
    '15-document-qa-bot.md': '15a Project — Document Q&A bot.mp4',
    '16-why-tools-matter.md': '16a Why tools matter.mp4',
    '17-writing-local-tools.md': '17a Writing local tools.mp4',
    '18-agent-context.md': '18a Agent context.mp4',
    '19-multi-step-workflows.md': '19a Multi step workflows.mp4'
}

with open(master_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    new_lines.append(line)
    if line.startswith('## 📄 File:'):
        m = re.search(r'`([^`]+)`', line)
        if m:
            fname = m.group(1)
            video_name = video_map.get(fname, f"{fname.replace('.md', '')}.mp4")
            new_lines.append(f"\n> **🎥 Thinkific Video Asset:** `{video_name}`\n\n")

with open(master_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Successfully injected Thinkific video file names into master_courses_lesson_notes.md!")
