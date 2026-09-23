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

flow = InstalledAppFlow.from_client_secrets_file(
    CREDENTIALS_PATH,
    scopes=SCOPES,
    redirect_uri='http://localhost:8080/',
    autogenerate_code_verifier=False
)

# prompt='select_account consent' forces Google to show Account & Channel Picker
auth_url, _ = flow.authorization_url(prompt='select_account consent', access_type='offline')

print("==========================================================================")
print(" 🔑 BRAND ACCOUNT YOUTUBE OAUTH URL (PROMPT ACCOUNT & CHANNEL SELECTOR)")
print("==========================================================================")
print(f"\n👉 {auth_url}\n")
