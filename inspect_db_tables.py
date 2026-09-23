import sqlite3
import os

db_path = "/Users/hkc/Documents/lyzr/personal-desk.db"

print("==========================================================================")
print(" 🔍 INSPECTING TABLES & SCHEMA IN PERSONAL-DESK.DB")
print("==========================================================================")

if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [t[0] for t in cur.fetchall()]
    print(f"Tables in {db_path}: {tables}\n")
    
    for tname in tables:
        cur.execute(f"PRAGMA table_info({tname});")
        cols = [c[1] for c in cur.fetchall()]
        cur.execute(f"SELECT COUNT(*) FROM {tname};")
        cnt = cur.fetchone()[0]
        print(f" Table '{tname}' ({cnt} rows): {cols}")
        
    conn.close()

print("==========================================================================")
