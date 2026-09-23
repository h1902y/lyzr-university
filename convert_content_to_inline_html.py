import urllib.request
import urllib.parse
import json
import os
import csv
import sys
import re

csv.field_size_limit(sys.maxsize)

token_file = "/Users/hkc/.gemini/antigravity-ide/google_token.json"
sheet_id = "1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk"
university_dir = "/Users/hkc/Documents/lyzr/university"
csv_in_path = os.path.join(university_dir, "master_courses_content_final_clean.csv")

print("==========================================================================")
print(" 🎨 CONVERTING MARKDOWN LEXICONS TO CLEAN INLINE HTML RICH TEXT")
print("==========================================================================")

def markdown_to_clean_html(md):
    if not md:
        return ""
    
    # 1. Code blocks ```python ... ```
    def code_block_sub(m):
        code = m.group(1).strip()
        code_escaped = html_escape(code)
        return f'<pre style="background-color:#1e1e2e; color:#f8f8f2; padding:14px; border-radius:6px; font-family:monospace; overflow-x:auto; line-height:1.4;"><code>{code_escaped}</code></pre>'
    
    md = re.sub(r'```(?:python|bash|json)?\s*\n?(.*?)```', code_block_sub, md, flags=re.DOTALL)

    # 2. Inline code `code`
    md = re.sub(r'`([^`]+)`', r'<code style="background-color:#f3f4f6; color:#d97706; padding:2px 6px; border-radius:4px; font-family:monospace; font-weight:600;">\1</code>', md)

    # 3. Headings # -> <h1>, ## -> <h2>
    md = re.sub(r'^# (.*?)$', r'<h1 style="color:#651a39; font-weight:700; font-size:24px; margin-top:0; margin-bottom:12px;">\1</h1>', md, flags=re.MULTILINE)
    md = re.sub(r'^## (.*?)$', r'<h2 style="color:#111827; font-weight:700; font-size:18px; margin-top:20px; margin-bottom:8px; border-bottom:2px solid #e5e7eb; padding-bottom:4px;">\1</h2>', md, flags=re.MULTILINE)

    # 4. Bold text **text** -> <b>text</b>
    md = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', md)

    # 5. Bullet list items - item -> <li>item</li>
    lines = md.split('\n')
    in_list = False
    new_lines = []
    
    for line in lines:
        line_s = line.strip()
        if line_s.startswith('- ') or line_s.startswith('* '):
            item_text = line_s[2:].strip()
            if not in_list:
                new_lines.append('<ul style="margin-top:6px; margin-bottom:12px; padding-left:24px;">')
                in_list = True
            new_lines.append(f'  <li style="margin-bottom:4px; color:#374151;">{item_text}</li>')
        else:
            if in_list:
                new_lines.append('</ul>')
                in_list = False
            
            if line_s and not line_s.startswith('<h1') and not line_s.startswith('<h2') and not line_s.startswith('<pre') and not line_s.startswith('<ul') and not line_s.startswith('</ul'):
                new_lines.append(f'<p style="color:#374151; line-height:1.6; margin-top:6px; margin-bottom:10px;">{line_s}</p>')
            else:
                new_lines.append(line)
    
    if in_list:
        new_lines.append('</ul>')

    final_html = '\n'.join(new_lines)
    return final_html

def html_escape(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

updated_rows = []

with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    updated_rows.append(header)

    converted_count = 0
    for row in reader:
        content_md = row[3] if len(row) > 3 else ""

        html_content = markdown_to_clean_html(content_md)
        row[3] = html_content
        converted_count += 1

        updated_rows.append(row)

print(f"✅ Converted markdown to inline HTML rich text for all {converted_count} lesson notes!\n")

# Refresh OAuth Access Token
with open(token_file, 'r', encoding='utf-8') as f:
    tok_data = json.load(f)

token_payload = urllib.parse.urlencode({
    "client_id": tok_data["client_id"],
    "client_secret": tok_data["client_secret"],
    "refresh_token": tok_data["refresh_token"],
    "grant_type": "refresh_token"
}).encode('utf-8')

token_req = urllib.request.Request("https://oauth2.googleapis.com/token", data=token_payload, headers={
    "Content-Type": "application/x-www-form-urlencoded"
})

with urllib.request.urlopen(token_req) as resp:
    access_token = json.loads(resp.read().decode('utf-8'))["access_token"]

# Push live update to Google Sheet
tab_name = "Master Courses Content"
encoded_tab_name = urllib.parse.quote(tab_name)

update_url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/'{encoded_tab_name}'!A1?valueInputOption=USER_ENTERED"
update_payload = json.dumps({"values": updated_rows}).encode('utf-8')

update_req = urllib.request.Request(update_url, data=update_payload, headers={
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}, method="PUT")

try:
    with urllib.request.urlopen(update_req) as uresp:
        res = json.loads(uresp.read().decode('utf-8'))
        print(f"🎉 GOOGLE SHEET INLINE HTML LIVE UPDATE SUCCESS!")
        print(f"   Updated Range: {res.get('updatedRange')}")
        print(f"   Updated Cells: {res.get('updatedCells')}")
except Exception as e:
    print(f"❌ Sheet update error: {e}")

# Save CSV backup
csv_out_path = os.path.join(university_dir, "master_courses_content_inline_html.csv")
with open(csv_out_path, 'w', newline='', encoding='utf-8') as cf:
    writer = csv.writer(cf)
    writer.writerows(updated_rows)

print(f"💾 Saved inline HTML CSV export to: {csv_out_path}")
