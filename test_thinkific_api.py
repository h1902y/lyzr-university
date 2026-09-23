import urllib.request
import json
import os

token = os.environ.get("THINKIFIC_API_ACCESS_TOKEN", "")
subdomain = os.environ.get("THINKIFIC_SUBDOMAIN", "lyzr")

url = "https://api.thinkific.com/api/public/v1/courses"

req = urllib.request.Request(url, headers={
    "Authorization": f"Bearer {token}",
    "X-Auth-Subdomain": subdomain,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
})

try:
    with urllib.request.urlopen(req) as resp:
        print(f"🎉 SUCCESS! Status Code: {resp.getcode()}")
        data = json.loads(resp.read().decode('utf-8'))
        print(json.dumps(data, indent=2)[:600])
except Exception as e:
    print(f"❌ Failed: {e}")
