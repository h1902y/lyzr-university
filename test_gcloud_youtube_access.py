import subprocess
import urllib.request
import urllib.parse
import json

print("==========================================================================")
print(" 🚀 TESTING YOUTUBE API ACCESS VIA GCLOUD CLI TOKEN (harshit.choudhary@lyzr.ai)")
print("==========================================================================")

try:
    token = subprocess.check_output(["gcloud", "auth", "print-access-token"]).decode('utf-8').strip()
    print(" ✅ Successfully fetched gcloud access token!")
    
    # 1. Query YouTube Channel info
    ch_url = "https://www.googleapis.com/youtube/v3/channels?mine=true&part=snippet,contentDetails,statistics"
    req = urllib.request.Request(ch_url, headers={
        "Authorization": f"Bearer {token}",
        "User-Agent": "Lyzr-University/1.0"
    })
    
    with urllib.request.urlopen(req) as resp:
        ch_data = json.loads(resp.read().decode('utf-8'))
        items = ch_data.get('items', [])
        if items:
            ch = items[0]
            print(f" ✅ Connected to YouTube Channel for harshit.choudhary@lyzr.ai:")
            print(f"    • Channel Title:       {ch['snippet']['title']}")
            print(f"    • Custom Handle:       {ch['snippet'].get('customUrl', 'N/A')}")
            print(f"    • Channel ID:          {ch['id']}")
            print(f"    • Channel Link:        https://www.youtube.com/channel/{ch['id']}")
            print(f"    • Subscriber Count:    {ch['statistics'].get('subscriberCount', 'N/A')}\n")
        else:
            print(" ⚠️ No channel found under 'mine=true'. Querying channel by handle @LyzrAI...")
            handle_url = "https://www.googleapis.com/youtube/v3/channels?forHandle=LyzrAI&part=snippet,contentDetails,statistics"
            req2 = urllib.request.Request(handle_url, headers={"Authorization": f"Bearer {token}"})
            with urllib.request.urlopen(req2) as resp2:
                h_data = json.loads(resp2.read().decode('utf-8'))
                print("Handle Query Result:", json.dumps(h_data, indent=2)[:500])

except Exception as e:
    print(f" ❌ Error accessing YouTube API via gcloud token: {e}")
