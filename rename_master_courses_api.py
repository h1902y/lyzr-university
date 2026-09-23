import urllib.request
import json
import os

token = os.environ.get("THINKIFIC_API_ACCESS_TOKEN", "")
subdomain = os.environ.get("THINKIFIC_SUBDOMAIN", "lyzr")

renames = [
    {"id": 3489968, "name": "Lyzr Foundations"},
    {"id": 3489969, "name": "Lyzr for Business Professionals"},
    {"id": 3490173, "name": "Lyzr for Business Professionals"},
    {"id": 3489970, "name": "Lyzr for Technical Professionals"}
]

print("==========================================================================")
print(" ✏️ RENAMING MASTER COURSES VIA THINKIFIC API")
print("==========================================================================")

for item in renames:
    cid = item["id"]
    new_name = item["name"]
    url = f"https://api.thinkific.com/api/public/v1/courses/{cid}"
    
    payload = json.dumps({"name": new_name}).encode('utf-8')
    req = urllib.request.Request(url, data=payload, headers={
        "Authorization": f"Bearer {token}",
        "X-Auth-Subdomain": subdomain,
        "Content-Type": "application/json",
        "User-Agent": "LyzrAssistant/1.0"
    }, method="PUT")

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"✅ Course #{cid} successfully renamed to: '{data.get('name')}' (HTTP {resp.getcode()})")
    except Exception as e:
        print(f"❌ Failed renaming course #{cid}: {e}")
