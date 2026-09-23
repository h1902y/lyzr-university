import urllib.request
import json
import re

url = "https://share.descript.com/view/M7ktDjS5XE4"

req = urllib.request.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
})

try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        
        # Check __NEXT_DATA__
        m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html, re.DOTALL)
        if m:
            data = json.loads(m.group(1))
            props = data.get("props", {}).get("pageProps", {})
            print("Keys in pageProps:", props.keys())
            
            # Print project / transcript details if present
            project = props.get("project") or props.get("share") or props.get("video")
            if project:
                print("Project keys:", project.keys() if isinstance(project, dict) else type(project))
            
            # Extract all transcript words / paragraphs
            text_blocks = []
            def search_text(obj):
                if isinstance(obj, dict):
                    for k, v in obj.items():
                        if k in ["text", "transcript", "content"] and isinstance(v, str) and len(v) > 3:
                            if not v.startswith("http") and not v.startswith("data:"):
                                text_blocks.append(v)
                        else:
                            search_text(v)
                elif isinstance(obj, list):
                    for elem in obj:
                        search_text(elem)

            search_text(props)
            full_txt = " ".join(text_blocks)
            print(f"\nExtracted {len(text_blocks)} text blocks ({len(full_txt)} chars). Sample:")
            print(full_txt[:300])

except Exception as e:
    print(f"Error fetching Descript page: {e}")
