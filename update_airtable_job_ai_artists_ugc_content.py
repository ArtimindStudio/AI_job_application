import json
import os

import requests


JOB_ID = "JOB-VIDEO-002"


def load_env(path=r"D:\Projects\Upwork\.env"):
    env = {}
    if os.path.exists(path):
        with open(path, encoding="utf-8") as env_file:
            for raw_line in env_file:
                line = raw_line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, value = line.split("=", 1)
                env[key.strip()] = value.strip()
    return env


env = load_env()
airtable_pat = env.get("AIRTABLE_PAT")
airtable_base_id = env.get("AIRTABLE_BASE_ID", "appSTxBDPzcjMcIvu")
airtable_table_id = env.get("AIRTABLE_TABLE_ID", "tbl05fiEfgfTzt36b")

if not airtable_pat:
    raise RuntimeError("AIRTABLE_PAT is missing from D:\\Projects\\Upwork\\.env")

url = f"https://api.airtable.com/v0/{airtable_base_id}/{airtable_table_id}"
headers = {
    "Authorization": f"Bearer {airtable_pat}",
    "Content-Type": "application/json",
}

job_description = """Budget: Hourly; range not supplied
Recommended bid: $15/hour
Connects required: 20
Available Connects: 97 (77 after application)
Duration: More than 6 months
Weekly capacity: Less than 30 hours/week
Experience level: Intermediate
Project type: Complex project
Posted: 8 hours ago
Location: Worldwide

AI Artists for UGC Content

Create UGC-style social content from briefs, including short-form videos, images, and text-based posts. Deliver platform-ready assets quickly, collaborate closely, and adapt ideas to audience needs. Arcads experience is a plus.

Mandatory tags: Adobe Illustrator; Illustration.
Nice-to-have: Graphic Design; Adobe Photoshop.
Activity: 5–10 proposals; client viewed today; 1 interviewing; 0 invites.
Bids: $150 high; $33.79 average; $7 low."""

cover_letter = """Hi,

I create UGC-style social assets from brief to final delivery—including realistic AI creators, short-form product videos, supporting images, hooks, captions, and platform-ready variations.

My closest example is a 15-second AI UGC Home Care Product Ad created with MiniMax H3. I developed the creator concept, directed a natural bathroom routine, maintained believable product interaction, and shaped the edit for an organic TikTok/Reels ad feel. I have also produced a fashion eyewear commercial with two consistent realistic models and a product landing-page motion concept built around fast visual hooks and feature callouts.

For ongoing production, I turn each brief into a hook, shot list, visual references, and platform format before generation. I use MiniMax H3, Kling, Seedance, or Higgsfield based on the motion required, with Google Nano Banana for supporting image assets and Photoshop, Illustrator, and Canva for final polish. Claude, Codex, Antigravity, and n8n help organize variations and repeatable QA.

Arcads has not been the centre of my current workflow, but I am comfortable adapting to new AI production platforms. The important part is keeping the creator, product, message, and pacing consistent across each deliverable.

Relevant work:
- AI UGC Home Care Product Ad | MiniMax H3: [INSERT DIRECT VIDEO URL]
- AI Fashion Eyewear Commercial | MiniMax H3: [INSERT DIRECT VIDEO URL]
- AI Product Landing Page Motion Design | MiniMax H3: [INSERT DIRECT VIDEO URL]

I can work part-time at $15/hour and am available for an ongoing collaboration.

Best,
Dennis Bui
https://aiartimind.com"""

fields = {
    "Title": "AI Artists for UGC Content",
    "Status": "Drafting",
    "Source": "Upwork",
    "Job Description": job_description,
    "Client Info": (
        "United States (Bronx). Payment and phone verified; 4.8/5 from 13 reviews; "
        "43 jobs posted; 56% hire rate; 7 open jobs; $9K spent; 36 hires; 21 active; "
        "$12.67/hour average across 554.83 hours. Recent visible hires: $12–$15/hour."
    ),
    "Current Status": (
        "Apply recommendation; 9.2/10 fit. Medium Connects risk: 20 of 97. "
        "Low competition but 1 candidate already interviewing. Proposal drafted; "
        "three direct MiniMax H3 portfolio URLs still required."
    ),
    "Following Plan": (
        "1. Insert direct URLs for UGC Home Care, Fashion Eyewear, and Product Landing Page videos.\n"
        "2. Bid $15/hour and do not boost.\n"
        "3. Attach UGC Home Care video first.\n"
        "4. Clarify video/static/text mix, Arcads requirement, asset volume, and revisions in interview."
    ),
    "Cover Letter": cover_letter,
    "ID": JOB_ID,
}

lookup = requests.get(
    url,
    headers=headers,
    params={"filterByFormula": f"{{ID}}='{JOB_ID}'", "maxRecords": 1},
    timeout=30,
)
lookup.raise_for_status()
existing_records = lookup.json().get("records", [])

if existing_records:
    record_id = existing_records[0]["id"]
    response = requests.patch(
        f"{url}/{record_id}", headers=headers, json={"fields": fields}, timeout=30
    )
    action = "updated"
else:
    response = requests.post(url, headers=headers, json={"fields": fields}, timeout=30)
    action = "added"

if response.ok:
    print(f"Successfully {action} {JOB_ID} in Airtable.")
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
    response.raise_for_status()
