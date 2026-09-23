import urllib.request
import urllib.parse
import json
import os

client_id = os.environ.get("GOOGLE_SHEET_CLIENT_ID", "")
client_secret = os.environ.get("GOOGLE_SHEET_CLIENT_SECRET", "")
refresh_token = os.environ.get("GOOGLE_SHEET_REFRESH_TOKEN", "")
sheet_id = os.environ.get("GOOGLE_SHEET_ID", "1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk")

token_url = "https://oauth2.googleapis.com/token"
token_data = urllib.parse.urlencode({
    "client_id": client_id,
    "client_secret": client_secret,
    "refresh_token": refresh_token,
    "grant_type": "refresh_token"
}).encode('utf-8')

token_req = urllib.request.Request(token_url, data=token_data, headers={
    "Content-Type": "application/x-www-form-urlencoded"
})

try:
    with urllib.request.urlopen(token_req) as resp:
        print(resp.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("HTTPError Status:", e.code)
    print("HTTPError Body:", e.read().decode('utf-8'))
except Exception as e:
    print("Error:", e)
