import os, glob

base_dir = '/Users/hkc/Documents/lyzr'

mp4s = glob.glob(os.path.join(base_dir, '**/*.mp4'), recursive=True)
non_node_mp4s = [m for m in mp4s if 'node_modules' not in m]

print(f"==========================================================================")
print(f" 🎬 TOTAL LOCAL VIDEO MP4 FILES ON DISK: {len(non_node_mp4s)}")
print(f"==========================================================================")

total_bytes = 0
for m in sorted(non_node_mp4s):
    size_mb = os.path.getsize(m) / (1024 * 1024)
    total_bytes += os.path.getsize(m)
    rel_path = m.replace(base_dir, '')
    print(f"  [{size_mb:.1f} MB] {rel_path}")

print(f"\n==========================================================================")
print(f" 📦 TOTAL VIDEO STORAGE SIZE ON DISK: {total_bytes / (1024*1024*1024):.2f} GB")
print(f"==========================================================================")
