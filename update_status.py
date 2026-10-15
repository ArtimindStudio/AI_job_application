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

# We'll update the record ID returned: recYPleShAwbUEdQf
record_id = "recYPleShAwbUEdQf"
url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_ID}/{record_id}"
headers = {
    "Authorization": f"Bearer {AIRTABLE_PAT}",
    "Content-Type": "application/json"
}

payload = {
    "fields": {
        "Status": "Applied"
    }
}

response = requests.patch(url, headers=headers, json=payload)

if response.status_code == 200:
    print("Successfully updated job status in Airtable.")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
