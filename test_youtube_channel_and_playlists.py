import os
import sys
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = [
    'https://www.googleapis.com/auth/youtube.upload',
    'https://www.googleapis.com/auth/youtube',
    'https://www.googleapis.com/auth/youtube.force-ssl'
]

TOKEN_PATH = '/Users/hkc/.gemini/antigravity-ide/google_token.json'
CREDENTIALS_PATH = '/Users/hkc/.gemini/antigravity-ide/google_credentials.json'

print("==========================================================================")
print(" 🚀 TESTING YOUTUBE API AUTHENTICATION & CHANNEL IDENTIFICATION")
print("==========================================================================")

creds = None
if os.path.exists(TOKEN_PATH):
    try:
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    except Exception as e:
        print(f"Error loading token from {TOKEN_PATH}: {e}")

if creds and creds.expired and creds.refresh_token:
    try:
        creds.refresh(Request())
        print("Successfully refreshed YouTube OAuth token!")
    except Exception as e:
        print(f"Token refresh failed: {e}")

if not creds or not creds.valid:
    print(f"Token invalid or missing YouTube scopes. Please authenticate via OAuth.")
    sys.exit(1)

service = build('youtube', 'v3', credentials=creds)

try:
    channels_res = service.channels().list(mine=True, part='snippet,contentDetails,statistics').execute()
    items = channels_res.get('items', [])
    if items:
        ch = items[0]
        title = ch['snippet']['title']
        ch_id = ch['id']
        subs = ch['statistics'].get('subscriberCount', 'N/A')
        print(f" ✅ Connected to YouTube Channel:")
        print(f"    • Channel Title:       {title}")
        print(f"    • Channel ID:          {ch_id}")
        print(f"    • Subscriber Count:    {subs}")
        print(f"    • Channel Link:        https://www.youtube.com/channel/{ch_id}\n")
    else:
        print(" ❌ No YouTube channels found for the authenticated account.")
except Exception as e:
    print(f" ❌ Error fetching YouTube channel info: {e}")

# Target Playlists
playlists_to_create = [
    {
        "title": "Lyzr Foundations — Master Course",
        "description": "Master the fundamentals of the Lyzr Enterprise Agent Platform. Learn how autonomous agents, private RAG knowledge bases, deterministic guardrails, and MCP tool servers interact to deliver production-ready AI workflows across your organization."
    },
    {
        "title": "Lyzr for Business Professionals — Master Course",
        "description": "Design, govern, and deploy enterprise AI agents visually using Lyzr Agent Studio. Build complex multi-agent SuperFlow orchestrations, attach knowledge bases, and simulate agent behaviors without writing a single line of code."
    },
    {
        "title": "Lyzr for Technical Professionals — Master Course",
        "description": "Build production-grade autonomous agent microservices using the Lyzr ADK Python SDK. Implement multi-provider model switching, custom RAG pipelines, Pydantic structured outputs, and Model Context Protocol (MCP) server integrations."
    }
]

def get_or_create_playlist(service, p_title, p_desc):
    try:
        res = service.playlists().list(mine=True, part='snippet', maxResults=50).execute()
        for item in res.get('items', []):
            if item['snippet']['title'].strip().lower() == p_title.strip().lower():
                p_id = item['id']
                print(f"  ✓ Found existing Playlist '{p_title}':")
                print(f"    ID:   {p_id}")
                print(f"    Link: https://www.youtube.com/playlist?list={p_id}\n")
                return p_id

        print(f"  + Creating new Playlist '{p_title}'...")
        body = {
            'snippet': {
                'title': p_title,
                'description': p_desc
            },
            'status': {
                'privacyStatus': 'public'
            }
        }
        playlist = service.playlists().insert(part='snippet,status', body=body).execute()
        p_id = playlist['id']
        print(f"  ✅ Created Playlist '{p_title}':")
        print(f"     ID:   {p_id}")
        print(f"     Link: https://www.youtube.com/playlist?list={p_id}\n")
        return p_id
    except Exception as e:
        print(f"  ❌ Error managing playlist '{p_title}': {e}\n")
        return None

print("==========================================================================")
print(" 📺 CREATING / VERIFYING THE 3 MASTER PLAYLISTS ON YOUTUBE")
print("==========================================================================")

created_playlists = {}
for p in playlists_to_create:
    pid = get_or_create_playlist(service, p['title'], p['description'])
    if pid:
        created_playlists[p['title']] = pid

print("🎉 YouTube Playlist Creation Complete!")
