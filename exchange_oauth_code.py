import os
import sys
import json
import urllib.parse
import urllib.request
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

def exchange_code_from_url(redirect_url_or_code):
    raw_input = redirect_url_or_code.strip()
    
    if "code=" in raw_input:
        parsed = urllib.parse.urlparse(raw_input)
        params = urllib.parse.parse_qs(parsed.query)
        auth_code = params.get('code', [raw_input])[0]
    else:
        auth_code = raw_input

    flow = InstalledAppFlow.from_client_secrets_file(
        CREDENTIALS_PATH,
        scopes=SCOPES,
        redirect_uri='http://localhost'
    )
    
    flow.fetch_token(code=auth_code)
    creds = flow.credentials

    with open(TOKEN_PATH, 'w', encoding='utf-8') as tf:
        tf.write(creds.to_json())

    print(f"✅ YouTube OAuth Token generated and saved to: {TOKEN_PATH}")
    return creds

if __name__ == '__main__':
    if len(sys.argv) > 1:
        exchange_code_from_url(sys.argv[1])
    else:
        print("Usage: python3 exchange_oauth_code.py '<PASTED_URL_OR_CODE>'")
