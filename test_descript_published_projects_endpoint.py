import urllib.request
import json
import os

bearer_token = os.environ.get("DESCRIPT_BEARER_TOKEN", "")

slugs = ["M7ktDjS5XE4", "JYCOaor01EZ", "xYNw4wPwzjT", "QSwoPpR6hKL", "l0epSX3Joov"]

print("==========================================================================")
print(" 🚀 TESTING GET /v1/published_projects/{slug} ENDPOINT")
print("==========================================================================")

for slug in slugs:
    url = f"https://descriptapi.com/v1/published_projects/{slug}"
    try:
        req = urllib.request.Request(url, headers={
            "Authorization": f"Bearer {bearer_token}",
            "User-Agent": "Lyzr-University/1.0"
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f" ✅ SUCCESS for slug '{slug}':")
            print(f"    • Title:        {data.get('metadata', {}).get('title')}")
            print(f"    • Duration:     {data.get('metadata', {}).get('duration_formatted')}")
            print(f"    • Download URL: {data.get('download_url')[:80]}...")
            print(f"    • Subtitles:    {data.get('subtitles')[:100]}...\n")
    except urllib.error.HTTPError as e:
        print(f" ❌ HTTP Error {e.code} for slug '{slug}': {e.reason}")
    except Exception as e:
        print(f" ❌ Error for slug '{slug}': {e}")
