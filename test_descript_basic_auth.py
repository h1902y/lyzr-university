import urllib.request
import base64
import os

bearer = os.environ.get("DESCRIPT_BEARER_TOKEN", "")
secret = os.environ.get("DESCRIPT_SECRET", "")

auth_str = f"{bearer}:{secret}"
b64_auth = base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')

endpoints = [
    "https://api.descript.com/v1/user",
    "https://api.descript.com/v1/drive",
    "https://api.descript.com/v1/projects",
    "https://api.descript.com/v2/projects"
]

print("Testing Basic Auth (dx_bearer:dx_secret):")
for ep in endpoints:
    try:
        req = urllib.request.Request(ep, headers={
            "Authorization": f"Basic {b64_auth}",
            "User-Agent": "Lyzr-University/1.0"
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f" SUCCESS: {ep} -> HTTP {resp.status}")
            print(resp.read().decode('utf-8')[:200])
    except urllib.error.HTTPError as e:
        print(f" HTTP {e.code}: {ep} ({e.reason})")
    except Exception as e:
        print(f" Error: {ep} -> {e}")

print("\nTesting Bearer Authorization: Bearer dx_secret...:")
try:
    req = urllib.request.Request("https://api.descript.com/v1/user", headers={
        "Authorization": f"Bearer {secret}",
        "User-Agent": "Lyzr-University/1.0"
    })
    with urllib.request.urlopen(req, timeout=10) as resp:
        print(f" SUCCESS Bearer secret -> HTTP {resp.status}")
        print(resp.read().decode('utf-8')[:200])
except Exception as e:
    print(f" Bearer secret Error: {e}")
