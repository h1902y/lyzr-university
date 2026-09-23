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
print(" 🔍 AUDITING LIVE YOUTUBE PLAYLISTS & UPLOADED VIDEOS")
print("==========================================================================")

if not os.path.exists(TOKEN_PATH):
    print(f"Error: Token file not found at {TOKEN_PATH}")
    sys.exit(1)

creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
if creds.expired and creds.refresh_token:
    creds.refresh(Request())

service = build('youtube', 'v3', credentials=creds)

playlists = [
    ("Lyzr Foundations — Master Course", "PLNhUOcQ57yRU"),
    ("Lyzr for Business Professionals — Master Course", "PLJs-yamjL6bw"),
    ("Lyzr for Technical Professionals — Master Course", "PLad3Pu7_rlUI")
]

total_uploaded_videos = 0

for p_title, p_id in playlists:
    print(f"📌 Playlist: '{p_title}' (ID: {p_id})")
    print(f"   Link: https://www.youtube.com/playlist?list={p_id}")

    res = service.playlistItems().list(playlistId=p_id, part='snippet', maxResults=50).execute()
    items = res.get('items', [])
    print(f"   Total Videos in Playlist: {len(items)}")

    for idx, item in enumerate(items, 1):
        v_title = item['snippet']['title']
        v_id = item['snippet']['resourceId']['videoId']
        print(f"     {idx:2d}. [{v_id}] {v_title}")

    total_uploaded_videos += len(items)
    print("-" * 70)

print(f"🎉 Total Successfully Uploaded & Assigned Videos: {total_uploaded_videos} / 49")
