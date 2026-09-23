import os
import shutil

university_dir = "/Users/hkc/Documents/lyzr/university"
upload_dir = os.path.join(university_dir, "thinkific-upload")
bulk_dir = os.path.join(university_dir, "bulk-video-upload")
os.makedirs(bulk_dir, exist_ok=True)

# Exact Mapping of Target Standardized Filename -> Relative Path under thinkific-upload
exact_video_map = {
    # C01: Lyzr Foundations
    "C01_CH01_L01_introduction_to_lyzr_platform.mp4": "01 Lyzr Foundations/Chapter 01 Lyzr Platform Overview/01a Introduction to Lyzr.mp4",
    "C01_CH01_L02_client_success_stories.mp4": "01 Lyzr Foundations/Chapter 01 Lyzr Platform Overview/02a Client Success Stories.mp4",
    "C01_CH01_L03_the_lyzr_stack_and_architecture.mp4": "01 Lyzr Foundations/Chapter 01 Lyzr Platform Overview/03a The Lyzr Stack.mp4",
    "C01_CH02_L01_architect_overview.mp4": "01 Lyzr Foundations/Chapter 01 Lyzr Platform Overview/04a Architect.mp4",
    "C01_CH02_L02_studio_overview.mp4": "01 Lyzr Foundations/Chapter 01 Lyzr Platform Overview/05a Studio.mp4",
    "C01_CH02_L03_lyzr_capabilities.mp4": "01 Lyzr Foundations/Chapter 01 Lyzr Platform Overview/06a Lyzr Capabilities.mp4",
    "C01_CH03_L01_computer_agent.mp4": "01 Lyzr Foundations/Chapter 01 Lyzr Platform Overview/07a Computer Agent.mp4",
    "C01_CH03_L02_git_agent.mp4": "01 Lyzr Foundations/Chapter 01 Lyzr Platform Overview/08a Git Agent.mp4",
    "C01_CH04_L01_designing_knowledge_bases.mp4": "01 Lyzr Foundations/Chapter 02 Enterprise Knowledge Base Masterclass/02a Designing Knowledge Bases & Source Selection.mp4",
    "C01_CH04_L02_pdf_parsing_strategies.mp4": "01 Lyzr Foundations/Chapter 02 Enterprise Knowledge Base Masterclass/03a PDF Parsing Strategies & Tabular Data Extraction.mp4",
    "C01_CH04_L03_retrieval_algorithms.mp4": "01 Lyzr Foundations/Chapter 02 Enterprise Knowledge Base Masterclass/04a Retrieval Algorithms — Basic, MMR, and HYDE.mp4",
    "C01_CH04_L04_wiring_kb_to_agent.mp4": "01 Lyzr Foundations/Chapter 02 Enterprise Knowledge Base Masterclass/05a Wiring KB to Agent & Debugging Execution Traces.mp4",
    "C01_CH05_L01_introduction_to_tools_and_mcp.mp4": "01 Lyzr Foundations/Chapter 03 Connecting Agents with MCP Servers and Tools/01a Introduction to Tools & MCP Servers for Agents.mp4",
    "C01_CH05_L02_configuring_tavily_mcp_server.mp4": "01 Lyzr Foundations/Chapter 03 Connecting Agents with MCP Servers and Tools/02a Configuring Tavily MCP Server for Live Web Search.mp4",
    "C01_CH05_L03_integrating_gmail_email_tools.mp4": "01 Lyzr Foundations/Chapter 03 Connecting Agents with MCP Servers and Tools/03a Integrating Gmail & Email Action Tools.mp4",

    # C02: Lyzr for Business Professionals
    "C02_CH01_L01_welcome_to_agent_studio_lifecycle.mp4": "1 - Tracks/Studio/06 Studio The Agent Lifecycle/01a Welcome to Agent Studio and Lifecycle.mp4",
    "C02_CH01_L02_build_choose_type_and_create_agent.mp4": "1 - Tracks/Studio/06 Studio The Agent Lifecycle/02a Build Choose Type and Create Agent.mp4",
    "C02_CH01_L03_equip_model_tool_memory_knowledge.mp4": "1 - Tracks/Studio/06 Studio The Agent Lifecycle/03a Equip Model Tool Memory Knowledge.mp4",
    "C02_CH01_L04_what_agent_type_should_i_build.mp4": "1 - Tracks/Studio/07 Studio Design and Create/01a What Agent Type Should I Build.mp4",
    "C02_CH02_L01_lyzr_manager_orchestration.mp4": "1 - Tracks/Studio/07 Studio Design and Create/02a Lyzr Manager Orchestration.mp4",
    "C02_CH02_L02_superflow_basic_dynamic_flows.mp4": "1 - Tracks/Studio/07 Studio Design and Create/04a SuperFlow Invoice Reconciliation.mp4",
    "C02_CH02_L03_superflow_advanced_routing_loops.mp4": "1 - Tracks/Studio/07 Studio Design and Create/05a SuperFlow Loops.mp4",
    "C02_CH03_L01_rag_in_studio.mp4": "02 Lyzr for Business Teams/Chapter 03 Grounding Agents in Knowledge/01a RAG in Studio.mp4",
    "C02_CH03_L02_build_a_knowledge_base.mp4": "02 Lyzr for Business Teams/Chapter 03 Grounding Agents in Knowledge/02a Build a Knowledge Base.mp4",
    "C02_CH03_L03_document_parsing_ingestion.mp4": "02 Lyzr for Business Teams/Chapter 03 Grounding Agents in Knowledge/03a Document parsing & ingestion.mp4",
    "C02_CH03_L04_data_connectors_as_live_sources.mp4": "02 Lyzr for Business Teams/Chapter 03 Grounding Agents in Knowledge/04a Data Connectors as live sources.mp4",
    "C02_CH04_L01_agent_memory_in_depth.mp4": "02 Lyzr for Business Teams/Chapter 03 Grounding Agents in Knowledge/05a Agent memory in depth.mp4",
    "C02_CH04_L02_beyond_vectors_structured_knowledge.mp4": "02 Lyzr for Business Teams/Chapter 03 Grounding Agents in Knowledge/06a Beyond vectors — structured knowledge.mp4",
    "C02_CH04_L03_build_a_knowledge_graph.mp4": "02 Lyzr for Business Teams/Chapter 03 Grounding Agents in Knowledge/07a Build a Knowledge Graph.mp4",
    "C02_CH04_L04_the_semantic_model_global_context.mp4": "02 Lyzr for Business Teams/Chapter 03 Grounding Agents in Knowledge/08a The Semantic Model.mp4",
    "C02_CH05_L01_responsible_ai_guardrails.mp4": "02 Lyzr for Business Teams/Chapter 04 Governing and Testing Enterprise Agents/01a Responsible AI in Studio.mp4",
    "C02_CH05_L02_agent_simulation_observability.mp4": "02 Lyzr for Business Teams/Chapter 04 Governing and Testing Enterprise Agents/02a The Simulation Engine.mp4",

    # C03: Lyzr for Technical Professionals
    "C03_CH01_L01_what_is_a_lyzr_agent.mp4": "03 Lyzr for Developers/Chapter 01 ADK Python SDK Getting Started/01a What is a Lyzr Agent.mp4",
    "C03_CH01_L02_building_your_first_agent.mp4": "03 Lyzr for Developers/Chapter 01 ADK Python SDK Getting Started/02a Your first Agent.mp4",
    "C03_CH01_L03_swapping_llm_providers.mp4": "03 Lyzr for Developers/Chapter 01 ADK Python SDK Getting Started/03a Swapping LLM Providers.mp4",
    "C03_CH01_L04_streaming_responses.mp4": "03 Lyzr for Developers/Chapter 01 ADK Python SDK Getting Started/04a Streaming Responses.mp4",
    "C03_CH01_L05_structured_outputs.mp4": "03 Lyzr for Developers/Chapter 01 ADK Python SDK Getting Started/05a Structured Outputs.mp4",
    "C03_CH01_L06_project_multi_provider_chatbot.mp4": "03 Lyzr for Developers/Chapter 01 ADK Python SDK Getting Started/06a Project — Multi-provider chatbot.mp4",
    "C03_CH02_L01_image_generation_agents.mp4": "03 Lyzr for Developers/Chapter 02 Multimodal Agents/07a Image generation.mp4",
    "C03_CH02_L02_file_generation_agents.mp4": "03 Lyzr for Developers/Chapter 02 Multimodal Agents/08a File generation.mp4",
    "C03_CH02_L03_project_creative_assistant.mp4": "03 Lyzr for Developers/Chapter 02 Multimodal Agents/09a Project — Creative assistant.mp4",
    "C03_CH03_L01_technical_rag_fundamentals.mp4": "03 Lyzr for Developers/Chapter 03 Knowledge Vector Stores and Agent Memory/10a What is RAG.mp4",
    "C03_CH03_L02_document_ingestion_pipelines.mp4": "03 Lyzr for Developers/Chapter 03 Knowledge Vector Stores and Agent Memory/11a Document ingestion.mp4",
    "C03_CH03_L03_vector_stores_custom_retrievers.mp4": "03 Lyzr for Developers/Chapter 03 Knowledge Vector Stores and Agent Memory/12a Vector stores and retrieval.mp4",
    "C03_CH03_L04_agent_memory_basics.mp4": "03 Lyzr for Developers/Chapter 03 Knowledge Vector Stores and Agent Memory/13a Agent memory basics.mp4",
    "C03_CH03_L05_conversation_memory_persistence.mp4": "03 Lyzr for Developers/Chapter 03 Knowledge Vector Stores and Agent Memory/14a Conversation memory.mp4",
    "C03_CH03_L06_project_document_qa_bot.mp4": "03 Lyzr for Developers/Chapter 03 Knowledge Vector Stores and Agent Memory/15a Project — Document Q&A bot.mp4",
    "C03_CH04_L01_why_tools_matter.mp4": "03 Lyzr for Developers/Chapter 04 Custom Tools and Workflows/16a Why tools matter.mp4",
    "C03_CH04_L02_writing_custom_local_tools.mp4": "1 - Tracks/ADK/04 ADK Tools and Workflows/17a Writing local tools.mp4"
}

copied_count = 0
for target_name, rel_src in exact_video_map.items():
    src_full = os.path.join(upload_dir, rel_src)
    dest_full = os.path.join(bulk_dir, target_name)
    
    if os.path.exists(src_full):
        shutil.copy(src_full, dest_full)
        copied_count += 1
        print(f" [{copied_count:2d}/49] Copied '{target_name}'")
    else:
        # Fallback search by basename
        base_src = os.path.basename(rel_src)
        found = False
        for root, dirs, files in os.walk(upload_dir):
            if base_src in files:
                shutil.copy(os.path.join(root, base_src), dest_full)
                copied_count += 1
                found = True
                print(f" [{copied_count:2d}/49] Copied (Fallback) '{target_name}'")
                break
        if not found:
            print(f" ⚠️ Missing file: {rel_src}")

print(f"\n🎉 100% SUCCESS! Prepared {copied_count} / {len(exact_video_map)} standardized video files in: {bulk_dir}")
