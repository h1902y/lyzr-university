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
print(" 🔍 LISTING ALL ACCESSIBLE YOUTUBE CHANNELS FOR AUTHENTICATED ACCOUNT")
print("==========================================================================")

creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
if creds.expired and creds.refresh_token:
    creds.refresh(Request())

service = build('youtube', 'v3', credentials=creds)

# 1. Query mine=True
print("📌 Channels under mine=True:")
try:
    res1 = service.channels().list(mine=True, part='snippet,statistics,contentDetails').execute()
    for item in res1.get('items', []):
        print(f"  • Title:  {item['snippet']['title']}")
        print(f"    Handle: {item['snippet'].get('customUrl')}")
        print(f"    ID:     {item['id']}\n")
except Exception as e:
    print(f"  Error: {e}\n")

# 2. Query managedByMe=True
print("📌 Channels under managedByMe=True:")
try:
    res2 = service.channels().list(managedByMe=True, part='snippet,statistics,contentDetails').execute()
    for item in res2.get('items', []):
        print(f"  • Title:  {item['snippet']['title']}")
        print(f"    Handle: {item['snippet'].get('customUrl')}")
        print(f"    ID:     {item['id']}\n")
except Exception as e:
    print(f"  Error: {e}\n")

# 3. Query handle @LyzrAI directly
print("📌 Channel details for forHandle='LyzrAI':")
try:
    res3 = service.channels().list(forHandle='LyzrAI', part='snippet,statistics,contentDetails').execute()
    for item in res3.get('items', []):
        print(f"  • Title:  {item['snippet']['title']}")
        print(f"    Handle: {item['snippet'].get('customUrl')}")
        print(f"    ID:     {item['id']}\n")
except Exception as e:
    print(f"  Error: {e}\n")
