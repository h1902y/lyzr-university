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
print(" 🚀 CREATING MASTER COURSE PLAYLISTS ON LYZR YOUTUBE ACCOUNT")
print("==========================================================================")

creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
if creds.expired and creds.refresh_token:
    creds.refresh(Request())

service = build('youtube', 'v3', credentials=creds)

ch_res = service.channels().list(mine=True, part='snippet,statistics').execute()
items = ch_res.get('items', [])
if items:
    ch = items[0]
    print(f" ✅ Connected Channel: {ch['snippet']['title']} (Handle: {ch['snippet'].get('customUrl')}) (ID: {ch['id']})\n")

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

created_results = []

for p in playlists_to_create:
    title = p['title']
    desc = p['description']
    print(f"Checking Playlist: '{title}'...")
    
    res = service.playlists().list(mine=True, part='snippet', maxResults=50).execute()
    existing_id = None
    for item in res.get('items', []):
        if item['snippet']['title'].strip().lower() == title.strip().lower():
            existing_id = item['id']
            break

    if existing_id:
        print(f"  ✓ Found existing Playlist ID: {existing_id}")
        playlist_url = f"https://www.youtube.com/playlist?list={existing_id}"
        created_results.append((title, existing_id, playlist_url))
    else:
        print(f"  + Creating new Playlist on YouTube...")
        body = {
            'snippet': {
                'title': title,
                'description': desc
            },
            'status': {
                'privacyStatus': 'public'
            }
        }
        playlist = service.playlists().insert(part='snippet,status', body=body).execute()
        pid = playlist['id']
        playlist_url = f"https://www.youtube.com/playlist?list={pid}"
        print(f"  🎉 Successfully Created Playlist: {pid}")
        print(f"     Link: {playlist_url}\n")
        created_results.append((title, pid, playlist_url))

print("==========================================================================")
print(" 📋 SUMMARY OF YOUTUBE MASTER COURSE PLAYLISTS")
print("==========================================================================")
for title, pid, url in created_results:
    print(f" • {title}")
    print(f"   ID:   {pid}")
    print(f"   Link: {url}\n")
