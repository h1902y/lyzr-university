import sqlite3
import os

db_path = "/Users/hkc/Documents/lyzr/personal-desk.db"

print("==========================================================================")
print(" 🤝 INSPECTING PARTNER PIPELINE STAGES IN SQLITE DATABASE")
print("==========================================================================")

if not os.path.exists(db_path):
    print(f"❌ Database not found at {db_path}")
else:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # List tables
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    print(f"Tables in DB: {[t[0] for t in tables]}\n")
    
    for t in tables:
        tname = t[0]
        cur.execute(f"SELECT COUNT(*) FROM {tname};")
        cnt = cur.fetchone()[0]
        print(f" Table '{tname}': {cnt} rows")
        
    conn.close()

print("==========================================================================")
