import os
import sys
import json
import csv
import time
import re

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

csv.field_size_limit(sys.maxsize)

SCOPES = [
    'https://www.googleapis.com/auth/youtube.upload',
    'https://www.googleapis.com/auth/youtube',
    'https://www.googleapis.com/auth/youtube.force-ssl',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

TOKEN_PATH = '/Users/hkc/.gemini/antigravity-ide/youtube_token.json'
university_dir = "/Users/hkc/Documents/lyzr/university"
revamp_dir = os.path.join(university_dir, "revamp")
csv_in_path = os.path.join(university_dir, "master_courses_content_markdown_reverted.csv")

PLAYLIST_MAP = {
    "Lyzr Foundations": "PLNhUOcQ57yRU",
    "Lyzr for Business Professionals": "PLJs-yamjL6bw",
    "Lyzr for Technical Professionals": "PLad3Pu7_rlUI"
}

print("==========================================================================")
print(" 🚀 UPLOADING 49 MASTER VIDEOS WITH CLEAN USER-FACING METADATA (NO CODES/NUMBERS)")
print("==========================================================================")

if not os.path.exists(TOKEN_PATH):
    print(f"Error: Token file not found at {TOKEN_PATH}")
    sys.exit(1)

creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
if creds.expired and creds.refresh_token:
    creds.refresh(Request())

service = build('youtube', 'v3', credentials=creds)

rows_list = []
with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    rows_list = list(reader)

print(f"Total Lessons to Upload: {len(rows_list)}\n")

def clean_name_no_numbers(text):
    if not text:
        return ""
    text = re.sub(r'^\s*Chapter\s*\d+\s*:\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^\s*Lesson\s*\d+\s*:\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^\s*C\d+_CH\d+_L\d+\s*', '', text)
    return text.strip()

def generate_clean_user_facing_metadata(course_name, chapter_name, lesson_title, lesson_content_md):
    clean_course = course_name.strip()
    clean_chapter = clean_name_no_numbers(chapter_name)
    clean_title = clean_name_no_numbers(lesson_title)

    # Title: "Introduction to Lyzr Platform — Lyzr Foundations"
    title = f"{clean_title} — {clean_course}"
    if len(title) > 95:
        title = title[:95]

    # Extract Objectives / Overview bullets from content markdown
    clean_notes = re.sub(r'#+\s*', '', lesson_content_md)
    clean_notes = re.sub(r'\*\*(.*?)\*\*', r'\1', clean_notes)
    lines = [l.strip() for l in clean_notes.split('\n') if l.strip()]
    
    summary_bullets = []
    for l in lines[:8]:
        if l.startswith('-') or l.startswith('•') or l.startswith('1.') or l.startswith('2.'):
            l_clean = re.sub(r'^\d+\.\s*', '', l)
            summary_bullets.append(f"  • {l_clean.lstrip('-• ')}")

    bullets_text = "\n".join(summary_bullets) if summary_bullets else "  • Comprehensive technical & operational walkthrough."

    # Clean User-Facing Description
    description = f"""Course: {clean_course}
Chapter: {clean_chapter}
Lesson: {clean_title}

============================================================
📚 LESSON OVERVIEW & OBJECTIVES
============================================================
{bullets_text}

============================================================
🔗 USEFUL LYZR RESOURCES & LINKS
============================================================
🌐 Lyzr Enterprise Agent Platform: https://lyzr.ai
📖 Official Lyzr Documentation:  https://docs.lyzr.ai
💻 Lyzr ADK Python SDK (GitHub): https://github.com/LyzrCore/lyzr-core
🚀 Lyzr Agent Studio:             https://studio.lyzr.ai

============================================================
🏷️ HASHTAGS
============================================================
#Lyzr #AIAgents #AgentStudio #LyzrADK #EnterpriseAI #AutonomousAgents #LLM #RAG #AI
"""

    tags = [
        "Lyzr", "Lyzr AI", "Lyzr University", "AI Agents", "Autonomous Agents",
        "Enterprise AI", "Agent Studio", "Lyzr ADK", "Python SDK", "RAG",
        "Knowledge Base", "Model Context Protocol", "MCP Server", clean_course,
        clean_chapter, clean_title
    ]

    return title, description, tags

uploaded_count = 0

for idx, r in enumerate(rows_list, 1):
    c_name = r[0]
    ch_name = r[1]
    l_title = r[2]
    content_md = r[3]
    v_name = r[5]

    playlist_id = PLAYLIST_MAP.get(c_name)
    v_path = os.path.join(revamp_dir, v_name)

    if not os.path.exists(v_path):
        print(f" ⚠️ Skipping row {idx}: Video file {v_path} not found.")
        continue

    video_title, video_desc, video_tags = generate_clean_user_facing_metadata(c_name, ch_name, l_title, content_md)

    print(f"[{idx}/49] Uploading: '{video_title}'")
    print(f"        File: {v_name} ({os.path.getsize(v_path) / (1024*1024):.1f} MB)")
    print(f"        Target Playlist: {playlist_id}")

    try:
        media = MediaFileUpload(v_path, mimetype='video/mp4', resumable=True, chunksize=1024*1024*5)
        body = {
            'snippet': {
                'title': video_title,
                'description': video_desc,
                'tags': video_tags,
                'categoryId': '28' # Science & Technology
            },
            'status': {
                'privacyStatus': 'unlisted'
            }
        }

        insert_req = service.videos().insert(part='snippet,status', body=body, media_body=media)
        
        response = None
        while response is None:
            status, response = insert_req.next_chunk()
            if status:
                print(f"        Progress: {int(status.progress() * 100)}%", end="\r")

        video_id = response['id']
        print(f"\n        ✅ Video Uploaded Successfully! Video ID: {video_id}")

        # Add to Playlist
        playlist_item_body = {
            'snippet': {
                'playlistId': playlist_id,
                'resourceId': {
                    'kind': 'youtube#video',
                    'videoId': video_id
                }
            }
        }
        service.playlistItems().insert(part='snippet', body=playlist_item_body).execute()
        print(f"        🎉 Added Video {video_id} to Playlist {playlist_id}!\n")

        uploaded_count += 1
        time.sleep(1)

    except HttpError as e:
        print(f"\n        ❌ YouTube API HttpError: {e}\n")
    except Exception as e:
        print(f"\n        ❌ Upload Error: {e}\n")

print(f"==========================================================================")
print(f" 🎉 YouTube Video Batch Upload Completed! ({uploaded_count}/49 uploaded)")
print(f"==========================================================================")
