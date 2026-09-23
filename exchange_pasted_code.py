import os
import sys
import json
import urllib.parse
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

SCOPES = [
    'https://www.googleapis.com/auth/youtube.upload',
    'https://www.googleapis.com/auth/youtube',
    'https://www.googleapis.com/auth/youtube.force-ssl',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

CREDENTIALS_PATH = '/Users/hkc/.gemini/antigravity-ide/google_credentials.json'
TOKEN_PATH = '/Users/hkc/.gemini/antigravity-ide/youtube_lyzrai_token.json'

auth_url_or_code = "http://localhost:8080/?iss=https://accounts.google.com&code=4/0AXEQxICJe0tvgDZSkO8HoBaassu5ViRKsojn3Y8fBuKzx_l7i-aJdsT1qZfiOxlqN58MnA&scope=https://www.googleapis.com/auth/youtube.upload%20https://www.googleapis.com/auth/youtube%20https://www.googleapis.com/auth/youtube.force-ssl%20https://www.googleapis.com/auth/spreadsheets%20https://www.googleapis.com/auth/drive"

if "code=" in auth_url_or_code:
    parsed = urllib.parse.urlparse(auth_url_or_code)
    params = urllib.parse.parse_qs(parsed.query)
    code = params['code'][0]
else:
    code = auth_url_or_code

print("==========================================================================")
print(" 🚀 EXCHANGING AUTHORIZATION CODE FOR YOUTUBE OAUTH TOKEN")
print("==========================================================================")
print(f"Code: {code[:15]}...")

flow = InstalledAppFlow.from_client_secrets_file(
    CREDENTIALS_PATH,
    scopes=SCOPES,
    redirect_uri='http://localhost:8080/',
    autogenerate_code_verifier=False
)

flow.fetch_token(code=code)
creds = flow.credentials

with open(TOKEN_PATH, 'w', encoding='utf-8') as tf:
    tf.write(creds.to_json())

print(f" ✅ Saved YouTube Token to: {TOKEN_PATH}")

service = build('youtube', 'v3', credentials=creds)

ch_res = service.channels().list(mine=True, part='snippet,statistics').execute()
items = ch_res.get('items', [])
if items:
    ch = items[0]
    print(f" 🎉 CONNECTED TO YOUTUBE CHANNEL:")
    print(f"    • Title:  {ch['snippet']['title']}")
    print(f"    • Handle: {ch['snippet'].get('customUrl')}")
    print(f"    • ID:     {ch['id']}")
    print(f"    • Link:   https://www.youtube.com/channel/{ch['id']}\n")
