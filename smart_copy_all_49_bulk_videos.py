import os
import shutil
import re

university_dir = "/Users/hkc/Documents/lyzr/university"
bulk_dir = os.path.join(university_dir, "bulk-video-upload")
os.makedirs(bulk_dir, exist_ok=True)

local_mp4_map = {}
for root, dirs, files in os.walk(university_dir):
    for f in files:
        if f.endswith('.mp4'):
            clean_name = re.sub(r'[^a-z0-9]', '', f.lower())
            local_mp4_map[clean_name] = os.path.join(root, f)

master_lessons = [
    # C01: Lyzr Foundations
    ("C01_CH01_L01_introduction_to_lyzr_platform.mp4", "01a Introduction to Lyzr Platform"),
    ("C01_CH01_L02_client_success_stories.mp4", "02a Client Success Stories"),
    ("C01_CH01_L03_the_lyzr_stack_and_architecture.mp4", "03a The Lyzr Stack and Architecture"),
    ("C01_CH02_L01_architect_overview.mp4", "04a Architect Overview"),
    ("C01_CH02_L02_studio_overview.mp4", "05a Studio Overview"),
    ("C01_CH02_L03_lyzr_capabilities.mp4", "06a Lyzr Capabilities"),
    ("C01_CH03_L01_computer_agent.mp4", "07a Computer Agent"),
    ("C01_CH03_L02_git_agent.mp4", "08a Git Agent"),
    ("C01_CH04_L01_designing_knowledge_bases.mp4", "09a Designing Knowledge Bases"),
    ("C01_CH04_L02_pdf_parsing_strategies.mp4", "10a PDF Parsing Strategies"),
    ("C01_CH04_L03_retrieval_algorithms.mp4", "11a Retrieval Algorithms"),
    ("C01_CH04_L04_wiring_kb_to_agent.mp4", "12a Wiring KB to Agent"),
    ("C01_CH05_L01_introduction_to_tools_and_mcp.mp4", "13a Introduction to Tools and MCP"),
    ("C01_CH05_L02_configuring_tavily_mcp_server.mp4", "14a Configuring Tavily MCP"),
    ("C01_CH05_L03_integrating_gmail_email_tools.mp4", "15a Integrating Gmail"),

    # C02: Lyzr for Business Professionals
    ("C02_CH01_L01_welcome_to_agent_studio_lifecycle.mp4", "01a Welcome to Agent Studio"),
    ("C02_CH01_L02_build_choose_type_and_create_agent.mp4", "02a Build"),
    ("C02_CH01_L03_equip_model_tool_memory_knowledge.mp4", "03a Equip"),
    ("C02_CH01_L04_what_agent_type_should_i_build.mp4", "04a What Agent Type"),
    ("C02_CH02_L01_lyzr_manager_orchestration.mp4", "05a Lyzr Manager"),
    ("C02_CH02_L02_superflow_basic_dynamic_flows.mp4", "06a SuperFlow Basic"),
    ("C02_CH02_L03_superflow_advanced_routing_loops.mp4", "07a SuperFlow Advanced"),
    ("C02_CH03_L01_rag_in_studio.mp4", "01a RAG in Studio"),
    ("C02_CH03_L02_build_a_knowledge_base.mp4", "02a Build a Knowledge Base"),
    ("C02_CH03_L03_document_parsing_ingestion.mp4", "03a Document parsing"),
    ("C02_CH03_L04_data_connectors_as_live_sources.mp4", "04a Data Connectors"),
    ("C02_CH04_L01_agent_memory_in_depth.mp4", "05a Agent memory in depth"),
    ("C02_CH04_L02_beyond_vectors_structured_knowledge.mp4", "06a Beyond vectors"),
    ("C02_CH04_L03_build_a_knowledge_graph.mp4", "07a Build a Knowledge Graph"),
    ("C02_CH04_L04_the_semantic_model_global_context.mp4", "08a The Semantic Model"),
    ("C02_CH05_L01_responsible_ai_guardrails.mp4", "01a Responsible AI"),
    ("C02_CH05_L02_agent_simulation_observability.mp4", "02a The Simulation Engine"),

    # C03: Lyzr for Technical Professionals
    ("C03_CH01_L01_what_is_a_lyzr_agent.mp4", "01a What is a Lyzr Agent"),
    ("C03_CH01_L02_building_your_first_agent.mp4", "02a Your first Agent"),
    ("C03_CH01_L03_swapping_llm_providers.mp4", "03a Swapping LLM Providers"),
    ("C03_CH01_L04_streaming_responses.mp4", "04a Streaming Responses"),
    ("C03_CH01_L05_structured_outputs.mp4", "05a Structured Outputs"),
    ("C03_CH01_L06_project_multi_provider_chatbot.mp4", "06a Project"),
    ("C03_CH02_L01_image_generation_agents.mp4", "07a Image generation"),
    ("C03_CH02_L02_file_generation_agents.mp4", "08a File generation"),
    ("C03_CH02_L03_project_creative_assistant.mp4", "09a Project"),
    ("C03_CH03_L01_technical_rag_fundamentals.mp4", "10a What is RAG"),
    ("C03_CH03_L02_document_ingestion_pipelines.mp4", "11a Document ingestion"),
    ("C03_CH03_L03_vector_stores_custom_retrievers.mp4", "12a Vector stores"),
    ("C03_CH03_L04_agent_memory_basics.mp4", "13a Agent memory basics"),
    ("C03_CH03_L05_conversation_memory_persistence.mp4", "14a Conversation memory"),
    ("C03_CH03_L06_project_document_qa_bot.mp4", "15a Project"),
    ("C03_CH04_L01_why_tools_matter.mp4", "16a Why tools matter"),
    ("C03_CH04_L02_writing_custom_local_tools.mp4", "17a Writing local tools")
]

copied_count = 0
for target_name, hint in master_lessons:
    clean_hint = re.sub(r'[^a-z0-9]', '', hint.lower())
    matched_src = None
    for clean_f, f_path in local_mp4_map.items():
        if clean_hint in clean_f:
            matched_src = f_path
            break
    
    dest_path = os.path.join(bulk_dir, target_name)
    if matched_src and os.path.exists(matched_src):
        shutil.copy(matched_src, dest_path)
        copied_count += 1
        print(f" [{copied_count:2d}] Copied '{os.path.basename(matched_src)}' -> '{target_name}'")
    else:
        print(f" ⚠️ Could not match hint '{hint}' for target '{target_name}'")

print(f"\n🎉 Successfully prepared {copied_count} / {len(master_lessons)} standardized video files in: {bulk_dir}")
