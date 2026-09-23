import urllib.request
import json
import os

token = os.environ.get("THINKIFIC_API_ACCESS_TOKEN", "")
subdomain = os.environ.get("THINKIFIC_SUBDOMAIN", "lyzr")

print("==========================================================================")
print(" 🚀 TESTING LIVE THINKIFIC API CALLS USING SAVED TOKEN")
print("==========================================================================")

# 1. Fetch public/v1/courses with Authorization header
url = "https://api.thinkific.com/api/public/v1/courses?page=1&limit=5"
req = urllib.request.Request(url, headers={
    "Authorization": f"Bearer {token}",
    "X-Auth-Subdomain": subdomain,
    "Content-Type": "application/json",
    "User-Agent": "LyzrAssistant/1.0"
})

try:
    with urllib.request.urlopen(req) as resp:
        print(f"\n1. GET /api/public/v1/courses — HTTP {resp.getcode()} SUCCESS!")
        data = json.loads(resp.read().decode('utf-8'))
        items = data.get('items', [])
        print(f"   Returned {len(items)} courses:")
        for c in items:
            print(f"    - [{c.get('id')}] {c.get('name')} (Draft: {c.get('draft')})")
except Exception as e:
    print(f"\n1. GET /api/public/v1/courses call result: {e}")

# 2. Fetch public/v1/users
url_users = "https://api.thinkific.com/api/public/v1/users?page=1&limit=5"
req_users = urllib.request.Request(url_users, headers={
    "Authorization": f"Bearer {token}",
    "X-Auth-Subdomain": subdomain,
    "Content-Type": "application/json",
    "User-Agent": "LyzrAssistant/1.0"
})

try:
    with urllib.request.urlopen(req_users) as resp:
        print(f"\n2. GET /api/public/v1/users — HTTP {resp.getcode()} SUCCESS!")
        data = json.loads(resp.read().decode('utf-8'))
        items = data.get('items', [])
        print(f"   Returned {len(items)} user accounts:")
        for u in items:
            print(f"    - [{u.get('id')}] {u.get('email')} ({u.get('first_name')} {u.get('last_name')})")
except Exception as e:
    print(f"\n2. GET /api/public/v1/users call result: {e}")
