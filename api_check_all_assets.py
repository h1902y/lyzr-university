import urllib.request
import json
import os

token = os.environ.get("THINKIFIC_API_ACCESS_TOKEN", "")
subdomain = os.environ.get("THINKIFIC_SUBDOMAIN", "lyzr")

print("==========================================================================")
print(" 🌐 CHECKING ALL COURSES & ASSETS VIA OFFICIAL THINKIFIC API")
print("==========================================================================")

# Step 1: Fetch all courses
url = "https://api.thinkific.com/api/public/v1/courses?page=1&limit=50"
req = urllib.request.Request(url, headers={
    "Authorization": f"Bearer {token}",
    "X-Auth-Subdomain": subdomain,
    "Content-Type": "application/json",
    "User-Agent": "LyzrAssistant/1.0"
})

try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        courses = data.get('items', [])
        print(f"✅ Retrieved {len(courses)} courses from Thinkific API!\n")

        for idx, course in enumerate(courses):
            cid = course.get('id')
            cname = course.get('name')
            cslug = course.get('slug')
            card_img = course.get('card_image_url', 'None')
            print(f"[{idx + 1}/{len(courses)}] Course ID #{cid}: '{cname}'")
            print(f"    Slug: {cslug}")
            print(f"    Card Image: {card_img[:80]}...")

            # Step 2: Try fetching detailed course info / contents
            detail_url = f"https://api.thinkific.com/api/public/v1/courses/{cid}"
            detail_req = urllib.request.Request(detail_url, headers={
                "Authorization": f"Bearer {token}",
                "X-Auth-Subdomain": subdomain,
                "Content-Type": "application/json",
                "User-Agent": "LyzrAssistant/1.0"
            })
            try:
                with urllib.request.urlopen(detail_req) as dresp:
                    ddata = json.loads(dresp.read().decode('utf-8'))
                    chapters = ddata.get('chapters', [])
                    print(f"    Chapters ({len(chapters)}):")
                    for ch in chapters:
                        print(f"      - Chapter #{ch.get('id')}: {ch.get('title')}")
                        contents = ch.get('contents', [])
                        for cnt in contents:
                            cnt_type = cnt.get('contentable_type', 'Lesson')
                            cnt_name = cnt.get('name')
                            asset_name = cnt.get('asset_name', 'N/A')
                            print(f"         • [{cnt_type}] {cnt_name} (Asset: {asset_name})")
            except Exception as de:
                print(f"    Notice on details: {de}")
            print()

except Exception as e:
    print(f"API Error: {e}")
