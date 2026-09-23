import sqlite3
import os

db_path = "/Users/hkc/Documents/lyzr/personal-desk.db"

print("==========================================================================")
print(" 📊 PARTNER PIPELINE STAGE AUDIT (LOCAL SQLITE DATABASE)")
print("==========================================================================")

if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # Check tables schema
    cur.execute("PRAGMA table_info(partners);")
    cols = cur.fetchall()
    print("Partners Columns:", [c[1] for c in cols])
    
    cur.execute("SELECT id, name, stage, owner, status, updated_at FROM partners ORDER BY stage, name;")
    rows = cur.fetchall()
    print(f"\nTotal Partners in DB: {len(rows)}\n")
    
    current_stage = None
    for r in rows:
        pid, name, stage, owner, status, updated_at = r
        if stage != current_stage:
            current_stage = stage
            print(f"\n--- STAGE: {current_stage or 'UNASSIGNED'} ---")
        print(f"  • {name:<35} | Owner: {owner or 'N/A':<15} | Status: {status or 'N/A':<10} | Updated: {updated_at}")
        
    conn.close()

print("==========================================================================")
