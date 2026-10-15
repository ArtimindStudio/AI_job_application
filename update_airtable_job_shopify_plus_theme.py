import os
import requests
import json

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
        "Title": "Shopify 2.0 / Shopify Plus Developer – Custom Theme & High-Converting Store",
        "Status": "Drafting",
        "Job Description": """Fixed Budget: $500 (Ongoing project)
Shopify 2.0 / Shopify Plus Developer – Custom Theme & High-Converting Store
Posted 3 minutes ago — Worldwide — Expert level

Responsibilities:
- Develop and customize Shopify 2.0 themes using Liquid
- Build custom sections, product pages, landing pages, and features
- Integrate Shopify apps, APIs, and third-party tools
- Work with Metafields and Metaobjects
- Optimize mobile responsiveness, speed, and Core Web Vitals
- Implement conversion-focused UX, upsells, and product functionality
- Support Shopify Plus features and ongoing improvements

Skills: Shopify, JavaScript, Shopify Plus, Shopify 2.0, Shopify Liquid, Shopify Theme Development, Shopify API, Ecommerce Website Development, Website Performance Optimization

Proposals: Less than 5 | Connects: 14""",
        "Connects Spent": 14,
        "Client Info": "Melbourne AUS | 5.0 rating (37 reviews) | 95% hire rate | 39 jobs posted | $1.2K total spent | Member since Jul 2024",
        "Current Status": "Application draft prepared. Low competition (< 5 proposals). Strong apply signal.",
        "Following Plan": "1. Finalize cover letter with store portfolio links.\n2. Submit proposal at $500 fixed.\n3. Emphasize ongoing availability and AI creative edge.",
        "ID": "JOB-SHOPIFY-004"
    }
}

response = requests.post(url, headers=headers, json=job_data)

if response.status_code == 200:
    print("Successfully added job to Airtable.")
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
