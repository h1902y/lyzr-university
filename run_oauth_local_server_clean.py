import os
import sys
import json
import urllib.parse
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    'https://www.googleapis.com/auth/youtube.upload',
    'https://www.googleapis.com/auth/youtube',
    'https://www.googleapis.com/auth/youtube.force-ssl',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

CREDENTIALS_PATH = '/Users/hkc/.gemini/antigravity-ide/google_credentials.json'

# Initialize flow
flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, scopes=SCOPES)
# Standard local server redirect URI
flow.redirect_uri = 'http://localhost:8080/'

auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')

print("==========================================================================")
print(" 🔑 CLEAN YOUTUBE OAUTH URL (WITH REDIRECT URI)")
print("==========================================================================")
print(f"\n👉 {auth_url}\n")
