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
        "Title": "AI Product Image Creator / AI Creative Designer — Petite Skin Co (Skincare)",
        "Status": "Drafting",
        "Job Description": """Connects: 17 | Bid: $30/hr | Avg Bid: $27.89 | Range: $15-$55
Hourly, 30+ hrs/week, 1-3 months, Ongoing potential

Australian children's/teen skincare brand (www.petiteskinco.com) needs AI image creator for product & lifestyle imagery across Meta, Google, Pinterest, Instagram, website, email.

Key requirements:
- AI product photography maintaining EXACT product accuracy (shape, colours, labels, logos, text)
- Studio-style, flat lays, bathroom/bedroom settings, ingredient-led, campaign concepts
- Lifestyle imagery with age-appropriate models (14 and under)
- Ad creative with space for headlines/CTAs
- Multi-format: 1080x1080, 1080x1440, 1080x1920
- Strong Photoshop finishing to correct AI artefacts
- Tools: Gemini, Nano Banana, Midjourney, Firefly, Photoshop, ChatGPT image gen

Client: Australia, Kunda Park. 5.0 rating (24 reviews), 78% hire rate, $5.5K spent, 43 hires. Fashion & Beauty, small company (2-9). Already hired 1 on this job.""",
        "Connects Spent": 17,
        "Client Info": "Australia (Kunda Park) | 5.0★ (24 reviews) | 78% hire rate | $5.5K spent | 43 hires | Fashion & Beauty | Small (2-9)",
        "Current Status": "Drafting application. High-fit skincare job with ongoing retainer potential. Bidding $30/hr.",
        "Following Plan": "1. Submit application with AURORA skincare portfolio samples.\n2. Offer small test batch to demonstrate product accuracy.\n3. If hired, build product reference library from their existing photography.\n4. Establish weekly creative delivery cadence.",
        "ID": "JOB-SKINCARE-001"
    }
}

response = requests.post(url, headers=headers, json=job_data)

if response.status_code == 200:
    print("Successfully added job to Airtable.")
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
