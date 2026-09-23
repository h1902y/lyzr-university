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

TOKEN_PATH = '/Users/hkc/.gemini/antigravity-ide/youtube_token.json'

print("==========================================================================")
print(" 🧹 CLEANING UP DUPLICATE/CODE TITLES FROM PLAYLIST 1 (PLNhUOcQ57yRU)")
print("==========================================================================")

creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
if creds.expired and creds.refresh_token:
    creds.refresh(Request())

service = build('youtube', 'v3', credentials=creds)

p_id = "PLNhUOcQ57yRU"
res = service.playlistItems().list(playlistId=p_id, part='snippet', maxResults=50).execute()
items = res.get('items', [])

removed_count = 0

for item in items:
    v_title = item['snippet']['title']
    playlist_item_id = item['id']
    
    # Check if title starts with C01_CH
    if v_title.startswith("C01_CH") or "C01_" in v_title:
        print(f" Removing old title item: '{v_title}' (Item ID: {playlist_item_id})")
        try:
            service.playlistItems().delete(id=playlist_item_id).execute()
            removed_count += 1
            print("  ✓ Removed.")
        except Exception as e:
            print(f"  ❌ Error removing item: {e}")

print(f"\n✅ Cleaned {removed_count} old items from Playlist 1!")
