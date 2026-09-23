import os, glob

base_dir = '/Users/hkc/Documents/lyzr/university'

print("=== ALL MD FILES UNDER UNIVERSITY ===")
all_md = sorted(glob.glob(os.path.join(base_dir, '**/*.md'), recursive=True))
for f in all_md:
    print(f.replace(base_dir, ''))
