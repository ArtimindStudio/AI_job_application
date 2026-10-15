import os
import requests
import json

# Minimalistic load_env logic
def load_env(path=os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')):
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
        "Title": "Consistent Room AI Image Specialist / Interior Viewpoints Artist",
        "Status": "Drafting",
        "Job Description": """AI image (applying same design from different angles/perspectives to consistent room layout)
Posted 55 minutes ago
Worldwide

Summary
We have original images of the room, and we have also created several reference design images. Now we need to create/adjust those design images and apply the same room design from different angles and perspectives.

As an example, I uploaded three images. The first two are original photos of the room, and the third one is a reference design image. We want the second original photo to be generated in the same design as the third image.

When we try to do this normally, the AI often gets confused and creates a different design instead of keeping exact same room. That is why we need a professional AI image artist who can carefully adjust our images and keep the design consistent across different viewpoints.

Less than 30 hrs/week
Hourly
Less than 1 month
Duration
Intermediate
I am looking for a mix of experience and value
Attachments: ChatGPT Image Jun 16, 2026, 01_26_22 AM.png, 01_26_27 AM.png, 05_30_52 PM.png""",
        "Client Info": "Worldwide, posted 55 minutes ago",
        "Current Status": "Cover Letter drafted. Ready to submit proposal.",
        "Following Plan": "1. Leverage ControlNet (Canny, Depth, Segment) to lock room geometry of secondary angles.\n2. Apply IP-Adapter, Style Reference (SRef), and ControlNet-Tile to transfer reference design.\n3. Detail-enhance via SDXL/Flux inpainting & Photoshop compositing.",
        "ID": "JOB-ROOM-001"
    }
}

response = requests.post(url, headers=headers, json=job_data)

if response.status_code == 200:
    print("Successfully added job to Airtable.")
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
