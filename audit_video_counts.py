import os, glob

base_dir = '/Users/hkc/Documents/lyzr/university/thinkific-upload'

mp4s = glob.glob(os.path.join(base_dir, '**/*.mp4'), recursive=True)
non_legacy_mp4s = [m for m in mp4s if 'Legacy' not in m and 'node_modules' not in m]

print(f"Total MP4 files under thinkific-upload (excluding legacy): {len(non_legacy_mp4s)}")

courses_map = {}
for m in non_legacy_mp4s:
    rel = m.replace(base_dir, '')
    parts = rel.strip('/').split('/')
    top_folder = parts[0] if len(parts) > 0 else 'root'
    courses_map.setdefault(top_folder, []).append(os.path.basename(m))

for folder, files in courses_map.items():
    print(f"\n📁 Folder: {folder} ({len(files)} video files)")
    for f in sorted(files):
        print(f"   - {f}")
