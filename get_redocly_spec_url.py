import urllib.request
import re

url = "https://docs.descriptapi.com/"
req = urllib.request.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
})

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        # Search for redoc spec or json URL
        matches = re.findall(r'spec-url=["\']([^"\']+)["\']', html)
        print("Spec-url attribute:", matches)
        
        # Search for script src
        scripts = re.findall(r'src=["\']([^"\']+)["\']', html)
        print("Scripts found:", scripts)
        
        # Check dark-mode-init or inline scripts
        inlines = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
        print(f"Found {len(inlines)} inline scripts.")
        for idx, s in enumerate(inlines):
            if "redoc" in s.lower() or "spec" in s.lower() or "json" in s.lower():
                print(f"Inline script {idx}:", s[:300])

except Exception as e:
    print("Error:", e)
