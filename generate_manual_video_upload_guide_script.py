import pathlib

artifact_path = pathlib.Path("/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/MANUAL_VIDEO_UPLOAD_GUIDE.md")

md = []
md.append("# 📤 Manual Video Upload Guide — Corrected Master Videos\n")
md.append("This guide contains the exact local file paths, Thinkific course locations, and YouTube playlist details for manually uploading the 3 corrected/re-stitched videos.\n")

md.append("## 📍 Local File Paths for Updated Videos\n")
md.append("1. **`C02_CH01_L02_build_choose_type_and_create_agent.mp4`** (118.12 MB)")
md.append("   - **Path:** [`/Users/hkc/Documents/lyzr/university/revamp_branded/C02_CH01_L02_build_choose_type_and_create_agent.mp4`](file:///Users/hkc/Documents/lyzr/university/revamp_branded/C02_CH01_L02_build_choose_type_and_create_agent.mp4)")
md.append("   - **Thumbnail:** [`/Users/hkc/Documents/lyzr/university/revamp/thumbnails/C02_CH01_L02_build_choose_type_and_create_agent.png`](file:///Users/hkc/Documents/lyzr/university/revamp/thumbnails/C02_CH01_L02_build_choose_type_and_create_agent.png)\n")

md.append("2. **`C01_CH05_L01_introduction_to_tools_and_mcp.mp4`** (8.88 MB)")
md.append("   - **Path:** [`/Users/hkc/Documents/lyzr/university/revamp_branded/C01_CH05_L01_introduction_to_tools_and_mcp.mp4`](file:///Users/hkc/Documents/lyzr/university/revamp_branded/C01_CH01_L05_L01_introduction_to_tools_and_mcp.mp4)")
md.append("   - **Thumbnail:** [`/Users/hkc/Documents/lyzr/university/revamp/thumbnails/C01_CH05_L01_introduction_to_tools_and_mcp.png`](file:///Users/hkc/Documents/lyzr/university/revamp/thumbnails/C01_CH05_L01_introduction_to_tools_and_mcp.png)\n")

md.append("3. **`C01_CH05_L02_configuring_tavily_mcp_server.mp4`** (8.66 MB)")
md.append("   - **Path:** [`/Users/hkc/Documents/lyzr/university/revamp_branded/C01_CH05_L02_configuring_tavily_mcp_server.mp4`](file:///Users/hkc/Documents/lyzr/university/revamp_branded/C01_CH05_L02_configuring_tavily_mcp_server.mp4)")
md.append("   - **Thumbnail:** [`/Users/hkc/Documents/lyzr/university/revamp/thumbnails/C01_CH05_L02_configuring_tavily_mcp_server.png`](file:///Users/hkc/Documents/lyzr/university/revamp/thumbnails/C01_CH01_L05_L02_configuring_tavily_mcp_server.png)\n")

md.append("## 🏫 Thinkific LMS Upload Instructions\n")
md.append("### **Video 1: Build: Choose Type and Create Agent**")
md.append("- **Thinkific URL:** Open [Thinkific Course Builder](https://lyzr.thinkific.com/manage/courses)")
md.append("- **Target Course:** `Lyzr Platform Studio` (Course #3489969)")
md.append("- **Chapter:** `Chapter 1: Agent Studio Lifecycle`")
md.append("- **Lesson:** `Build: Choose Type and Create Agent`")
md.append("- **Action:** Click on lesson $\\rightarrow$ Select Video Block $\\rightarrow$ Upload [`C02_CH01_L02_build_choose_type_and_create_agent.mp4`](file:///Users/hkc/Documents/lyzr/university/revamp_branded/C02_CH01_L02_build_choose_type_and_create_agent.mp4) $\\rightarrow$ Click **Save**.\n")

md.append("### **Video 2: Introduction to Tools & MCP**")
md.append("- **Target Course:** `Lyzr Foundations` (Course #3489968)")
md.append("- **Chapter:** `Chapter 5: Tools & MCP`")
md.append("- **Lesson:** `Introduction to Tools & MCP`")
md.append("- **Action:** Click on lesson $\\rightarrow$ Select Video Block $\\rightarrow$ Upload [`C01_CH05_L01_introduction_to_tools_and_mcp.mp4`](file:///Users/hkc/Documents/lyzr/university/revamp_branded/C01_CH05_L01_introduction_to_tools_and_mcp.mp4) $\\rightarrow$ Click **Save**.\n")

md.append("### **Video 3: Configuring Tavily MCP Server**")
md.append("- **Target Course:** `Lyzr Foundations` (Course #3489968)")
md.append("- **Chapter:** `Chapter 5: Tools & MCP`")
md.append("- **Lesson:** `Configuring Tavily MCP Server`")
md.append("- **Action:** Click on lesson $\\rightarrow$ Select Video Block $\\rightarrow$ Upload [`C01_CH05_L02_configuring_tavily_mcp_server.mp4`](file:///Users/hkc/Documents/lyzr/university/revamp_branded/C01_CH05_L02_configuring_tavily_mcp_server.mp4) $\\rightarrow$ Click **Save**.\n")

md.append("## 🔴 YouTube Studio Upload Instructions\n")
md.append("- **Channel:** [@LyzrAI Studio](https://studio.youtube.com)")
md.append("- **Visibility:** Unlisted")
md.append("- **Playlists:**")
md.append("  - `Lyzr Platform Studio — Master Course` for Video 1")
md.append("  - `Lyzr Foundations — Master Course` for Video 2 & Video 3")

with open(artifact_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(md))

print("  ✓ Created MANUAL_VIDEO_UPLOAD_GUIDE.md")
