import urllib.request
import csv
import os

sheet_id = "1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk"
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid=0"
save_path = "/Users/hkc/Documents/lyzr/university/lyzr_university_live_google_sheet.csv"

print(f"Downloading Google Sheet CSV from: {csv_url}")

req = urllib.request.Request(csv_url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
})

try:
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8')
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Successfully saved Google Sheet CSV to: {save_path}\n")

        # Parse CSV rows
        with open(save_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            print(f"Total Rows in Google Sheet: {len(rows)}")
            if rows:
                print("Header Row:", rows[0])
                print("\nSample Rows:")
                for r in rows[1:10]:
                    print(" -", r)
except Exception as e:
    print(f"❌ Error downloading Google Sheet: {e}")
