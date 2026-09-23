import os
import sys
import json

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/youtube.upload',
    'https://www.googleapis.com/auth/youtube',
    'https://www.googleapis.com/auth/youtube.force-ssl',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

TOKEN_PATH = '/Users/hkc/.gemini/antigravity-ide/youtube_lyzrai_token.json'

print("==========================================================================")
print(" 🧹 DELETING TEST UPLOADS & PLAYLISTS FROM PERSONAL CHANNEL")
print("==========================================================================")

creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
if creds.expired and creds.refresh_token:
    creds.refresh(Request())

service = build('youtube', 'v3', credentials=creds)

playlists = ["PLNhUOcQ57yRU", "PLJs-yamjL6bw", "PLad3Pu7_rlUI"]

deleted_videos = 0
for pid in playlists:
    try:
        res = service.playlistItems().list(playlistId=pid, part='snippet', maxResults=50).execute()
        items = res.get('items', [])
        for item in items:
            v_id = item['snippet']['resourceId']['videoId']
            v_title = item['snippet']['title']
            print(f" Deleting video '{v_title}' ({v_id})...")
            try:
                service.videos().delete(id=v_id).execute()
                deleted_videos += 1
                print("  ✓ Deleted from YouTube.")
            except Exception as e:
                print(f"  ❌ Error deleting video {v_id}: {e}")

        # Delete Playlist
        print(f" Deleting Playlist ID {pid}...")
        service.playlists().delete(id=pid).execute()
        print("  ✓ Playlist Deleted.\n")
    except Exception as e:
        print(f" Error cleaning playlist {pid}: {e}\n")

print(f"🎉 Cleanup Complete! Deleted {deleted_videos} test videos and 3 playlists from personal channel.")
