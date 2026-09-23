import os
import sys
import json
from google_auth_oauthlib.flow import InstalledAppFlow

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
print(" 🔑 INITIATING YOUTUBE OAUTH AUTHENTICATION FLOW")
print("==========================================================================")

flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)

# Generate local server auth url
auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')

print(f"\n👉 AUTHORIZATION URL:\n{auth_url}\n")
print("Please open the above URL in browser to complete OAuth consent for YouTube.")
