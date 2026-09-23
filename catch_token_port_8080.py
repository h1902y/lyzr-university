import os
import sys
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/youtube.upload',
    'https://www.googleapis.com/auth/youtube',
    'https://www.googleapis.com/auth/youtube.force-ssl',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

CREDENTIALS_PATH = '/Users/hkc/.gemini/antigravity-ide/google_credentials.json'
TOKEN_PATH = '/Users/hkc/.gemini/antigravity-ide/youtube_token.json'

print("==========================================================================")
print(" 🚀 STARTING OAUTH LOCAL SERVER ON PORT 8080")
print("==========================================================================")

flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
flow.redirect_uri = 'http://localhost:8080/'

auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')

print(f"\n👉 GOOGLE OAUTH URL FOR YOUTUBE:\n{auth_url}\n")

creds = flow.run_local_server(port=8080, open_browser=False)

with open(TOKEN_PATH, 'w', encoding='utf-8') as tf:
    tf.write(creds.to_json())

print(f"\n✅ YouTube OAuth Token saved successfully to: {TOKEN_PATH}")

service = build('youtube', 'v3', credentials=creds)
channels_res = service.channels().list(mine=True, part='snippet,statistics').execute()
items = channels_res.get('items', [])
if items:
    print(f" ✅ Connected to YouTube Channel: {items[0]['snippet']['title']} ({items[0]['id']})")
