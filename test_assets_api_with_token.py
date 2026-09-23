import urllib.request
import json
import os

token = os.environ.get("THINKIFIC_API_ACCESS_TOKEN", "")
subdomain = os.environ.get("THINKIFIC_SUBDOMAIN", "lyzr")

print("==========================================================================")
print(" 🚀 TESTING THINKIFIC ASSET & CONTENTS API ENDPOINTS WITH BEARER TOKEN")
print("==========================================================================")

endpoints = [
  "https://api.thinkific.com/api/public/v1/contents",
  "https://api.thinkific.com/api/public/v1/chapters",
  "https://api.thinkific.com/api/public/v1/courses/3489970"
]

for url in endpoints:
    print(f"\nTesting: {url}")
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "X-Auth-Subdomain": subdomain,
        "Content-Type": "application/json",
        "User-Agent": "LyzrAssistant/1.0"
    })
    try:
        with urllib.request.urlopen(req) as resp:
            status = resp.getcode()
            data = json.loads(resp.read().decode('utf-8'))
            print(f"  ✅ SUCCESS HTTP {status}!")
            print(f"  Response: {json.dumps(data, indent=2)[:300]}")
    except Exception as e:
        print(f"  ❌ Error: {e}")

# Test GraphQL Stable endpoint with Authorization Bearer
print("\nTesting GraphQL Stable Endpoint (https://api.thinkific.com/stable/graphql)...")
gql_url = "https://api.thinkific.com/stable/graphql"

gql_body = json.dumps({
    "query": "query GetCourses { courses(first: 5) { nodes { id name } } }"
}).encode('utf-8')

gql_req = urllib.request.Request(gql_url, data=gql_body, headers={
    "Authorization": f"Bearer {token}",
    "X-Auth-Subdomain": subdomain,
    "Content-Type": "application/json",
    "User-Agent": "LyzrAssistant/1.0"
})

try:
    with urllib.request.urlopen(gql_req) as resp:
        print(f"  ✅ GraphQL SUCCESS HTTP {resp.getcode()}!")
        data = json.loads(resp.read().decode('utf-8'))
        print(f"  GraphQL Response: {json.dumps(data, indent=2)[:500]}")
except Exception as e:
    print(f"  ❌ GraphQL Error: {e}")
