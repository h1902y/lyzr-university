import urllib.request
import json
import base64
import os

bearer = os.environ.get("DESCRIPT_BEARER_TOKEN", "")
secret = os.environ.get("DESCRIPT_SECRET", "")

endpoints = [
    "https://descriptapi.com/v1/projects",
    "https://descriptapi.com/v1/user",
    "https://descriptapi.com/v1/drives",
    "https://descriptapi.com/v1/drive/projects"
]

auth_header_options = [
    {"Authorization": f"Bearer {bearer}"},
    {"Authorization": f"Bearer {secret}"},
    {"Authorization": f"Basic {base64.b64encode(f'{bearer}:{secret}'.encode()).decode()}"},
    {"X-Api-Key": bearer, "X-Api-Secret": secret}
]

print("==========================================================================")
print(" 🚀 TESTING OFFICIAL DESCRIPT API (https://descriptapi.com/v1/)")
print("==========================================================================")

for ep in endpoints:
    for headers in auth_header_options:
        try:
            req_headers = {"User-Agent": "Lyzr-University/1.0", "Content-Type": "application/json"}
            req_headers.update(headers)
            req = urllib.request.Request(ep, headers=req_headers)
            with urllib.request.urlopen(req, timeout=5) as resp:
                print(f" SUCCESS: {ep} | Headers: {list(headers.keys())} -> HTTP {resp.status}")
                print(resp.read().decode('utf-8')[:200])
                break
        except urllib.error.HTTPError as e:
            if e.code != 401 and e.code != 404:
                print(f" HTTP {e.code}: {ep} ({e.reason}) | {headers}")
        except Exception as e:
            pass
