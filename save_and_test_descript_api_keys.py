import os
import urllib.request
import urllib.parse
import json

bearer_token = os.environ.get("DESCRIPT_BEARER_TOKEN", "")
secret_key = os.environ.get("DESCRIPT_SECRET", "")

env_paths = [
    "/Users/hkc/Documents/lyzr/.env",
    "/Users/hkc/Documents/lyzr/university/.env",
    "/Users/hkc/Documents/lyzr/university/thinkific-uploader/.env"
]

print("==========================================================================")
print(" 🔐 SAVING DESCRIPT API CREDENTIALS DEEPLY & TESTING ENDPOINTS")
print("==========================================================================")

# 1. Save in .env files
env_vars_to_add = {
    "DESCRIPT_BEARER_TOKEN": bearer_token,
    "DESCRIPT_SECRET": secret_key
}

for env_path in env_paths:
    lines = []
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    
    # Remove existing DESCRIPT keys
    lines = [l for l in lines if not l.startswith("DESCRIPT_")]
    
    for k, v in env_vars_to_add.items():
        lines.append(f"{k}={v}\n")
    
    with open(env_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print(f"✅ Saved Descript credentials to: {env_path}")

# 2. Test Descript API Endpoints
test_endpoints = [
    "https://api.descript.com/v1/user",
    "https://api.descript.com/v1/drives",
    "https://api.descript.com/v1/projects",
    "https://api.descript.com/v1/drive/projects"
]

print("\nTesting Descript API Endpoints...")

for ep in test_endpoints:
    try:
        req = urllib.request.Request(ep, headers={
            "Authorization": f"Bearer {bearer_token}",
            "X-Descript-Secret": secret_key,
            "Content-Type": "application/json",
            "User-Agent": "Lyzr-University-Assistant/1.0"
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            status = resp.status
            body = resp.read().decode('utf-8', errors='ignore')
            print(f" • GET {ep} -> HTTP {status}")
            print(f"   Response Preview: {body[:200]}\n")
    except urllib.error.HTTPError as e:
        print(f" • GET {ep} -> HTTP Error {e.code}: {e.reason}")
    except Exception as e:
        print(f" • GET {ep} -> Exception: {e}")

