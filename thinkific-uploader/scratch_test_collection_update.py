import json
import urllib.request
import pathlib

ENV = pathlib.Path("/Users/hkc/Documents/lyzr/university/.env")
BASE = "https://api.thinkific.com/api/public/v1/"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"

def _token():
    for l in ENV.read_text().splitlines():
        if l.startswith("TOKEN="):
            return l.split("=", 1)[1].strip().strip('"').strip("'")
    return ""

def api_all(path, token):
    items, page = [], 1
    sep = "&" if "?" in path else "?"
    while True:
        url = f"{BASE}{path}{sep}page={page}&limit=250"
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}", "User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.loads(r.read().decode())
            items += d["items"]
            nxt = d["meta"]["pagination"].get("next_page")
            if not nxt:
                return items
            page = nxt

def main():
    token = _token()
    if not token:
        print("No token found")
        return
        
    print("Fetching courses and collections from Thinkific API...")
    courses = api_all("courses", token)
    collections = api_all("collections", token)
    
    # We will map each course name to its product ID
    # Note: Course details endpoint or list endpoint provides product_id
    print(f"Fetched {len(courses)} courses.")
    
    # Map of collection ID -> list of product IDs
    # Let's initialize with empty lists
    collection_updates = {
        1456222: [], # Foundations (legacy)
        1445649: [], # Studio Track (business)
        1445650: []  # ADK Track (developer)
    }
    
    for c in courses:
        name = c.get("name", "")
        pid = c.get("product_id")
        status = c.get("status", "")
        
        if not pid:
            continue
            
        # Classify course
        if "[Legacy]" in name or "Lyzr Agent Building" in name or "Lyzr Agent Engineering" in name or "Value Enablement" in name:
            collection_updates[1456222].append(pid)
            print(f"FOUNDATIONS: {name} (Product ID: {pid})")
        elif name.startswith("ADK:"):
            collection_updates[1445650].append(pid)
            print(f"ADK TRACK: {name} (Product ID: {pid})")
        elif name.startswith("Studio:"):
            collection_updates[1445649].append(pid)
            print(f"STUDIO TRACK: {name} (Product ID: {pid})")
            
    # Now let's try updating a collection (e.g. Studio Track 1445649) to see if PUT collections works!
    studio_col_id = 1445649
    pids = list(set(collection_updates[studio_col_id]))
    print(f"\nAttempting to update Studio Track collection {studio_col_id} with product IDs: {pids}")
    
    payload = json.dumps({"product_ids": pids}).encode("utf-8")
    req = urllib.request.Request(
        f"{BASE}collections/{studio_col_id}",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "User-Agent": UA,
            "Content-Type": "application/json"
        },
        method="PUT"
    )
    
    try:
        with urllib.request.urlopen(req) as r:
            res = json.loads(r.read().decode())
            print("Successfully updated collection! Response:")
            print(json.dumps(res, indent=2))
    except Exception as e:
        print("Failed to update collection via API:", e)

if __name__ == "__main__":
    main()
