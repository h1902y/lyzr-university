import urllib.request
import json

headers = {
    'X-Auth-API-Key': '2b9fb543fbba4cb0c8702c2e0aa71dbd',
    'X-Auth-Subdomain': 'lyzr',
    'Content-Type': 'application/json'
}

req = urllib.request.Request("https://api.thinkific.com/api/v2/courses", headers=headers)
try:
    res = urllib.request.urlopen(req)
    data = json.loads(res.read().decode('utf-8'))
    print("==========================================================================")
    print(" 🔍 LIVE THINKIFIC COURSES & SLUGS")
    print("==========================================================================")
    for c in data.get('items', []):
        print(f" ID: {c.get('id')} | Name: '{c.get('name')}' | Slug: '{c.get('slug')}' | Landing URL: '{c.get('landing_page_url')}'")
    print("==========================================================================")
except Exception as e:
    print(f"API Error: {e}")
