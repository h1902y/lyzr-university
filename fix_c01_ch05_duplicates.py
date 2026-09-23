import urllib.request
import re
import pathlib
import subprocess
import csv

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
csv_path = university_dir / "master_courses_content_all_crafted_notes.csv"
branded_dir = university_dir / "revamp_branded"
unbranded_dir = university_dir / "revamp"
intro_bumper = university_dir / "remotion-branding/public/intro_bumper.mp4"
outro_bumper = university_dir / "remotion-branding/public/outro_bumper.mp4"

print("==========================================================================")
print(" 🔄 REPAIRING C01_CH05_L01 AND C01_CH05_L02 FROM DESCRIPT SOURCES")
print("==========================================================================")

# Lookup Descript URLs from CSV
descript_urls = {}
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 4:
            # row format: ..., descript_url, filename, transcript
            for col in row:
                if col.endswith(".mp4"):
                    for c in row:
                        if c.startswith("https://share.descript.com/view/"):
                            descript_urls[col.strip()] = c.strip()

targets = ["C01_CH05_L01_introduction_to_tools_and_mcp.mp4", "C01_CH05_L02_configuring_tavily_mcp_server.mp4"]

for fname in targets:
    url = descript_urls.get(fname)
    print(f"\n🎬 Target: {fname}")
    print(f"   Descript Link: {url}")
    
    if not url:
        print(f"   ❌ Descript URL not found for {fname}")
        continue
        
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    mp4_matches = re.findall(r'https://[^\s"\'<>]+\.mp4[^\s"\'<>]*', html)
    
    if not mp4_matches:
        print(f"   ❌ GCS MP4 URL not found on Descript page {url}")
        continue
        
    gcs_url = mp4_matches[0].replace("&amp;", "&")
    u_path = unbranded_dir / fname
    b_path = branded_dir / fname
    
    print(f"   📥 Downloading raw file to {u_path}...")
    urllib.request.urlretrieve(gcs_url, u_path)
    u_size_mb = u_path.stat().st_size / (1024 * 1024)
    print(f"   ✅ Raw file downloaded: {u_size_mb:.2f} MB")
    
    # Re-stitch Remotion bumpers
    concat_list = university_dir / f"concat_{fname}.txt"
    with open(concat_list, 'w') as f:
        f.write(f"file '{intro_bumper}'\n")
        f.write(f"file '{u_path}'\n")
        f.write(f"file '{outro_bumper}'\n")
        
    stitch_cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list),
        "-c:v", "libx264", "-preset", "fast", "-crf", "22",
        "-c:a", "aac", "-b:a", "192k",
        str(b_path)
    ]
    subprocess.run(stitch_cmd, capture_output=True, text=True)
    b_size_mb = b_path.stat().st_size / (1024 * 1024)
    print(f"   🎉 Rebranded file created: {b_size_mb:.2f} MB")

print("\n==========================================================================")
print(" 🎉 REPAIR COMPLETED FOR ALL FLAGGED DUPLICATES!")
print("==========================================================================")
