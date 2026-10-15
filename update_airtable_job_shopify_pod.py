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
        "Title": "Build a Simple Shopify Store from Scratch (POD)",
        "Status": "Applied",
        "Job Description": """Fixed Budget: $100
Build a Simple Shopify Store from Scratch
Posted 1 hour ago
Worldwide

Summary
Description:
I need a freelance Shopify developer to build a brand-new, simple e-commerce store from scratch for selling small print-on-demand goods (e.g., mugs, coasters, tote bags, small home/kitchen items). This is a small, clearly scoped project — no complex features, just a clean, functional store ready to launch.
Scope of work:
Set up a new Shopify store, choose and install a free Shopify theme, basic branding, connect Printful or Printify, build essential pages, add up to 10 products, configure payments/shipping, test checkout, 15-20 min handoff call.
Fixed price: $100""",
        "Client Info": "Worldwide, posted 1 hour ago",
        "Current Status": "Cover letter drafted and logged.",
        "Following Plan": "1. Pitch clean, automated POD workflow.\n2. Propose 5 days turnaround.\n3. Log to Airtable tracker.",
        "ID": "JOB-SHOPIFY-003"
    }
}

response = requests.post(url, headers=headers, json=job_data)

if response.status_code == 200:
    print("Successfully added job to Airtable.")
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
