import os
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
theme_dir = university_dir / "thinkific-theme"

print("==========================================================================")
print(" 🔄 UPDATING THINKIFIC THEME REDIRECT URLS & NAVIGATION LINKS")
print("==========================================================================")

# 1. Update header_links.liquid
header_file = theme_dir / "snippets" / "header_links.liquid"
if header_file.exists():
    t = open(header_file, 'r', encoding='utf-8').read()
    t = t.replace('href="/courses/foundations">Foundation</a>', 'href="/courses/foundations">Foundations</a>')
    t = t.replace('href="/courses/business">Business</a>', 'href="/courses/platform-studio">Platform Studio</a>')
    t = t.replace('href="/courses/technical">Technical</a>', 'href="/courses/code-libraries">Code Libraries</a>')
    with open(header_file, 'w', encoding='utf-8') as f:
        f.write(t)
    print("  ✓ Updated header_links.liquid")

# 2. Update footer.liquid
footer_file = theme_dir / "sections" / "footer.liquid"
if footer_file.exists():
    t = open(footer_file, 'r', encoding='utf-8').read()
    t = t.replace('href="/courses/foundations">Foundation</a>', 'href="/courses/foundations">Lyzr Foundations</a>')
    t = t.replace('href="/courses/business">Business</a>', 'href="/courses/platform-studio">Lyzr Platform Studio</a>')
    t = t.replace('href="/courses/technical">Technical</a>', 'href="/courses/code-libraries">Lyzr Code Libraries</a>')
    with open(footer_file, 'w', encoding='utf-8') as f:
        f.write(t)
    print("  ✓ Updated footer.liquid")

# 3. Update home_landing_page.liquid
home_file = theme_dir / "pages" / "home_landing_page.liquid"
if home_file.exists():
    t = open(home_file, 'r', encoding='utf-8').read()
    t = t.replace('href="/courses/business"', 'href="/courses/platform-studio"')
    t = t.replace('href="/courses/technical"', 'href="/courses/code-libraries"')
    with open(home_file, 'w', encoding='utf-8') as f:
        f.write(t)
    print("  ✓ Updated home_landing_page.liquid")

# 4. Check category snippets
for s_name in ["category_card.liquid", "products_category_list.liquid"]:
    s_file = theme_dir / "snippets" / s_name
    if s_file.exists():
        t = open(s_file, 'r', encoding='utf-8').read()
        t = t.replace('/courses/business', '/courses/platform-studio')
        t = t.replace('/courses/technical', '/courses/code-libraries')
        with open(s_file, 'w', encoding='utf-8') as f:
            f.write(t)
        print(f"  ✓ Updated {s_name}")

print("\n==========================================================================")
print(" 🎉 THINKIFIC THEME REDIRECT URLS & NAV LINKS UPDATED SUCCESSFULLY!")
print("==========================================================================")
