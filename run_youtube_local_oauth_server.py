import os
import sys
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

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
print(" 🚀 STARTING OAUTH LOCAL SERVER FOR YOUTUBE PERMISSIONS")
print("==========================================================================")

flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')

print(f"\n👉 GOOGLE OAUTH URL FOR YOUTUBE:\n{auth_url}\n")
print("Listening on http://localhost:8080/ for OAuth callback...")

creds = flow.run_local_server(port=8080)

with open(TOKEN_PATH, 'w', encoding='utf-8') as tf:
    tf.write(creds.to_json())

print(f"\n✅ YouTube OAuth Token saved successfully to: {TOKEN_PATH}")
