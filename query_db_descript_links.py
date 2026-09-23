import sqlite3
import re

db_path = "/Users/hkc/Documents/lyzr/personal-desk.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

descript_db_links = []

for (tbl,) in tables:
    try:
        cursor.execute(f"SELECT * FROM {tbl}")
        rows = cursor.fetchall()
        for r in rows:
            txt = str(r)
            matches = re.findall(r'https?://[^\s]*descript[^\s]*', txt, re.IGNORECASE)
            for m in matches:
                descript_db_links.append({"table": tbl, "link": m.rstrip(")'\"`*,;")})
    except Exception as e:
        pass

conn.close()

print(f"Total Descript Links Found in personal-desk.db: {len(descript_db_links)}")
for i, d in enumerate(descript_db_links):
    print(f" {i+1}. [{d['table']}] {d['link']}")
