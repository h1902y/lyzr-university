import os
import sys
import json
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from google_auth_oauthlib.flow import InstalledAppFlow
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
TOKEN_PATH = '/Users/hkc/.gemini/antigravity-ide/youtube_token.json'

auth_code_container = {}

class OAuthCallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        if 'code' in params:
            auth_code_container['code'] = params['code'][0]
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<h1>OAuth Authorization Successful!</h1><p>You can close this tab and return to terminal.</p>")
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"OAuth code missing.")

print("==========================================================================")
print(" 🚀 STARTING STATE-SAFE OAUTH RECEIVER ON PORT 8080")
print("==========================================================================")

flow = InstalledAppFlow.from_client_secrets_file(
    CREDENTIALS_PATH,
    scopes=SCOPES,
    redirect_uri='http://localhost:8080/'
)

auth_url, state = flow.authorization_url(prompt='consent', access_type='offline')

print(f"\n👉 AUTHORIZATION URL:\n{auth_url}\n")
print("Listening on http://localhost:8080/ ...")

server = HTTPServer(('localhost', 8080), OAuthCallbackHandler)
while 'code' not in auth_code_container:
    server.handle_request()

code = auth_code_container['code']
print(f" ✅ Received Authorization Code: {code[:15]}...")

flow.fetch_token(code=code)
creds = flow.credentials

with open(TOKEN_PATH, 'w', encoding='utf-8') as tf:
    tf.write(creds.to_json())

print(f" ✅ Saved YouTube OAuth Token to: {TOKEN_PATH}")

service = build('youtube', 'v3', credentials=creds)
channels_res = service.channels().list(mine=True, part='snippet,statistics').execute()
items = channels_res.get('items', [])
if items:
    print(f" 🎉 CONNECTED TO YOUTUBE CHANNEL: {items[0]['snippet']['title']} ({items[0]['id']})")
