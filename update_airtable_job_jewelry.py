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
        "Title": "Shopify Store Design for Jewelry",
        "Status": "Applied",
        "Job Description": """Shopify Store Design for Jewelry
Posted yesterday
Worldwide

Summary
We are seeking a skilled freelancer to design and develop a Shopify store for our jewelry brand. The ideal candidate will have experience in creating visually appealing and user-friendly e-commerce platforms. Responsibilities include customizing Shopify templates, integrating payment systems, and ensuring mobile responsiveness. The project requires an intermediate level of proficiency and is expected to be completed in less than a month.""",
        "Client Info": "Worldwide, posted yesterday",
        "Current Status": "Cover letter drafted and logged.",
        "Following Plan": "1. Highlight luxury jewelry staging experience (LUMINA/TIGRÉE).\n2. Pitch a premium visual approach matching high-ticket jewelry catalog standards.\n3. Log to Airtable.",
        "ID": "JOB-JEWELRY-002"
    }
}

response = requests.post(url, headers=headers, json=job_data)

if response.status_code == 200:
    print("Successfully added job to Airtable.")
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
