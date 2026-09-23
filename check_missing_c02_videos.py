import os
import csv
import urllib.request
import re
import html

university_dir = "/Users/hkc/Documents/lyzr/university"
revamp_dir = os.path.join(university_dir, "revamp")
csv_in_path = os.path.join(university_dir, "master_courses_content_markdown_reverted.csv")

print("==========================================================================")
print(" 🔍 CHECKING LOCAL VIDEO ASSETS & DOWNLOADING MISSING DESCRIPT MP4 FILES")
print("==========================================================================")

missing_files = []

with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    
    for row in reader:
        c_name = row[0]
        l_title = row[2]
        d_link = row[4]
        v_name = row[5]

        v_path = os.path.join(revamp_dir, v_name)
        if not os.path.exists(v_path):
            missing_files.append((c_name, l_title, v_name, d_link))

print(f"Total Missing Video Files in 'revamp/': {len(missing_files)}\n")

def extract_descript_mp4_url(share_url):
    try:
        req = urllib.request.Request(share_url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            page_html = resp.read().decode('utf-8', errors='ignore')
            # Regex match signed mp4 URL
            matches = re.findall(r'https://[^"\'\s]+\.mp4\?[^"\'\s]+', page_html)
            if matches:
                clean_url = html.unescape(matches[0])
                return clean_url
    except Exception as e:
        print(f"   ❌ Error fetching HTML for {share_url}: {e}")
    return None

for c_name, l_title, v_name, d_link in missing_files:
    print(f" ⚠️ Missing: [{c_name}] {l_title}")
    print(f"    Expected: {v_name}")
    print(f"    Descript: {d_link}")

    mp4_url = extract_descript_mp4_url(d_link)
    if mp4_url:
        target_file = os.path.join(revamp_dir, v_name)
        print(f"    ⬇️ Downloading MP4 from Descript GCS...")
        try:
            dl_req = urllib.request.Request(mp4_url, headers={"User-Agent": "Lyzr-University/1.0"})
            with urllib.request.urlopen(dl_req) as resp, open(target_file, 'wb') as out_f:
                out_f.write(resp.read())
            file_size_mb = os.path.getsize(target_file) / (1024 * 1024)
            print(f"    ✅ Downloaded successfully! ({file_size_mb:.2f} MB) -> {target_file}\n")
        except Exception as e:
            print(f"    ❌ Download failed: {e}\n")
    else:
        print(f"    ❌ Could not extract MP4 download URL from Descript page.\n")
