import os, glob

base_dir = '/Users/hkc/Documents/lyzr/university'
output_path = '/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/master_courses_lesson_notes.md'

sections = [
    ('Course 1: Lyzr Foundations', os.path.join(base_dir, 'SDK-track/notes/overview/*.md')),
    ('Course 2: Lyzr for Business Professionals', os.path.join(base_dir, 'Studio-track/notes/**/*.md')),
    ('Course 3: Lyzr for Developers', os.path.join(base_dir, 'SDK-track/notes/*.md'))
]

out = []
out.append('# Lyzr University — Complete Master Courses Lesson Notes\n\n')
out.append('> [!NOTE]\n> Comprehensive text lesson content, learning objectives, key concepts, hands-on instructions, and video transcripts across all 3 Master Courses.\n\n')

for course_title, pattern in sections:
    out.append(f'\n\n# ==========================================================================\n# 🎓 {course_title}\n# ==========================================================================\n\n')
    files = sorted(glob.glob(pattern, recursive=True))
    for fpath in files:
        if 'README' in fpath:
            continue
        fname = os.path.basename(fpath)
        out.append(f'\n\n---\n\n## 📄 File: `{fname}`\n\n')
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            out.append(content)

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(''.join(out))

print(f'Successfully consolidated {len(out)} entries to {output_path}')
