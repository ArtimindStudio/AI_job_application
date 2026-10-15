import os
import requests
import json

def load_env(path='d:/Projects/Upwork/.env'):
    env = {}
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                if '=' in line:
                    key, val = line.split('=', 1)
                    env[key.strip()] = val.strip()
    return env

env = load_env()
AIRTABLE_PAT = env.get('AIRTABLE_PAT')
AIRTABLE_BASE_ID = env.get('AIRTABLE_BASE_ID')
AIRTABLE_TABLE_ID = env.get('AIRTABLE_TABLE_ID')

url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_ID}"
headers = {
    "Authorization": f"Bearer {AIRTABLE_PAT}",
    "Content-Type": "application/json"
}

job_data = {
    "fields": {
        "Title": "AI Video Generation — DTC eCommerce Agency (10 Brands, 4 vids/day)",
        "Status": "Drafting",
        "Job Description": """Connects: 20 | Fixed: $1,200/mo | $10/video
4 videos/day (3 hooks + 1 body each) = ~120 videos/month

DTC eCommerce agency managing 10 brands needs AI video editor/generator.
Pay per video: $10 (3 hooks + 1 body).
Start ASAP. Only DTC ecom videos. Proficiency in AI video generator tools required.
Portfolio required.

Fixed-price $1,200/mo. Expert level. Contract-to-hire opportunity.
Skills: Video Editing, Premiere Pro, After Effects, Video Production, Video Post-Editing.""",
        "Connects Spent": 20,
        "Client Info": "Montenegro (Budva) | 5.0★ (6 reviews) | 37% hire rate | $1.4K spent | 22 hires, 13 active | Agency owner",
        "Current Status": "Drafting application. Medium-fit — strong AI video alignment but low per-unit rate ($10/video). Contract-to-hire upside.",
        "Following Plan": "1. Submit application with AI video portfolio samples.\n2. Offer paid test day (4 videos) to prove speed.\n3. Build per-brand asset libraries to compound efficiency.\n4. Renegotiate rate after first month based on performance.",
        "ID": "JOB-VIDEO-001"
    }
}

response = requests.post(url, headers=headers, json=job_data)

if response.status_code == 200:
    print("Successfully added job to Airtable.")
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
