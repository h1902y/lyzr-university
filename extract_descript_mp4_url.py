import urllib.request
import re
import pathlib

url = "https://share.descript.com/view/r0i0W0qxzAh"

print("==========================================================================")
print(f" 🔍 FETCHING DESCRIPT MP4 DIRECT LINK FROM {url}")
print("==========================================================================")

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    mp4_matches = re.findall(r'https://[^\s"\'<>]+\.mp4[^\s"\'<>]*', html)
    print(f"Found {len(mp4_matches)} MP4 matches:")
    for m in set(mp4_matches):
        print(f" 🔗 {m}")
        
    # Also find title
    title_m = re.search(r'<title>(.*?)</title>', html)
    if title_m:
        print(f" 📌 Title: {title_m.group(1)}")
except Exception as e:
    print(f"❌ Error: {e}")

print("==========================================================================")
