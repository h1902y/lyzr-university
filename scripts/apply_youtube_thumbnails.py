import os
import json
import pathlib
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

TOKEN_PATH = '/Users/hkc/.gemini/antigravity-ide/google_token.json'
UNI = pathlib.Path("/Users/hkc/Documents/lyzr/university")
PLAN_PATH = UNI / "youtube_backfill_plan.json"
THUMB_DIR = UNI / "thumbnails"

def main():
    print("==========================================================================")
    print(" APPLYING BRANDED CUSTOM THUMBNAILS TO LIVE YOUTUBE VIDEOS")
    print("==========================================================================")

    if not os.path.exists(TOKEN_PATH):
        print(f"Error: Token path {TOKEN_PATH} not found!")
        return

    with open(TOKEN_PATH, 'r') as f:
        tok_data = json.load(f)

    creds = Credentials.from_authorized_user_info(tok_data)
    youtube = build('youtube', 'v3', credentials=creds)

    if not PLAN_PATH.exists():
        print("Plan file missing.")
        return

    with open(PLAN_PATH, "r") as f:
        plan = json.load(f)

    success_count = 0
    fail_count = 0

    for item in plan.get("items", []):
        yt_id = item.get("youtube_id")
        item_id = item.get("id")

        if not yt_id:
            continue

        # Look for thumbnail in THUMB_DIR
        thumb_path = item.get("thumbnail_path")
        if not thumb_path or not os.path.exists(thumb_path):
            candidate = THUMB_DIR / f"thumb_{item_id}.png"
            if candidate.exists():
                thumb_path = str(candidate)

        if yt_id and thumb_path and os.path.exists(thumb_path):
            try:
                print(f"Uploading thumbnail to YouTube Video ID '{yt_id}' ({item.get('title')[:45]}...)...")
                media = MediaFileUpload(thumb_path, mimetype='image/png')
                youtube.thumbnails().set(videoId=yt_id, media_body=media).execute()
                print(f"  ✓ Applied Successfully to {yt_id}!")
                success_count += 1
            except Exception as e:
                print(f"  ⚠️ Error setting thumbnail for {yt_id}: {e}")
                fail_count += 1
        else:
            print(f"  ⚠️ No matching thumbnail image for Video ID {yt_id} (Item ID: {item_id})")

    print("\n==========================================================================")
    print(f" 🎉 THUMBNAIL PUBLISHING FINISHED! Applied: {success_count} | Errors: {fail_count}")
    print("==========================================================================")

if __name__ == "__main__":
    main()
