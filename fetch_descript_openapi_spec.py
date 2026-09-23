import urllib.request
import re

url = "https://docs.descriptapi.com/"
req = urllib.request.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
})

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        # Search for redoc init or spec url
        matches = re.findall(r'spec-url=[\'"]([^\'"]+)[\'"]', html)
        if not matches:
            matches = re.findall(r'https?://[^\s"\'<>]*(?:openapi|swagger|spec|api)[^\s"\'<>]*\.(?:json|yaml|yml)', html, re.IGNORECASE)
        print("Found spec URL matches:", matches)
        
        # Search for base URL in HTML
        base_urls = re.findall(r'https://[a-zA-Z0-9.-]*descript[a-zA-Z0-9./_-]*', html)
        print("Found Descript API URLs in docs:")
        for u in set(base_urls[:10]):
            print(" •", u)

except Exception as e:
    print("Error:", e)
