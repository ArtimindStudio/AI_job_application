import json
import os

import requests


JOB_ID = "JOB-MUSIC-001"


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

job_description = """Educational AI Song Producer (Suno, AI Art, Lyric-Video Editing)
Posted yesterday; Worldwide
Hourly: $20–$50; Expert; less than 30 hours/week
Duration: 1–3 months; ongoing project
Connects: 17 of 125 (108 after application)
Activity: 15–20 proposals; 0 interviewing; 0 invites

Produce educational vocabulary songs from a topic and three supplied words. Work includes Suno song generation/refinement, a supplied Armie review section through a private client tool, three child-friendly word illustrations/cards, AI lyric-video creation, exact caption and card synchronization, educational QA, Canva thumbnail/cover adaptation, and organized Google Drive delivery.

Client supplies approved brand examples, editable templates, prompt guidance, character/background assets, occasional word illustrations, card templates, Canva templates, and a Google Drive handoff structure.

Reference: https://youtu.be/Z_nhe9FZYnA
Job URL was not included in the supplied posting text."""

cover_letter = """Hi,

I reviewed the Colour Splash reference and the four supplied cover examples—Asteroid Joyride, Take One Breath, Build It Up, and Volleyball Parade. The visual system is clear: an oversized vocabulary-led title, a background tied directly to the word or theme, a recurring character, the yellow lightbulb brand mark, and consistent platform badges. I would preserve that system while making each new song feel distinct and age-appropriate.

My workflow covers brief and educational QA with GPT, Claude, and manual review; Suno prompt development using the supplied genre/instrument/tempo/vocal/mood framework; GPT Image 2 and Google Nano Banana for word illustrations and keyframes; MiniMax H3, Kling, Seedance, or Veo for motion; Premiere Pro for lyric synchronization, captions, sound, and finishing; and Canva/Photoshop for the supplied thumbnail and cover templates.

Relevant adjacent work:
- AI Product Landing Page Motion Design | MiniMax H3 — typography, feature callouts, pacing, transitions, and final edit: [INSERT DIRECT VIDEO URL]
- AI UGC Home Care Product Ad | MiniMax H3 — visual direction, consistent imagery, product storytelling, and social-ready edit: [INSERT DIRECT VIDEO URL]

These are AI advertising examples rather than children’s music videos, so I am sharing them specifically as evidence of AI visual direction, editing, timing, and template discipline. [CONFIRM BEFORE SENDING: add genuine Suno/lyric-video evidence if available.]

I can commit 20–30 hours per week, begin with the funded paid trial, and propose $26/hour.

Best,
Dennis Bui
https://aiartimind.com"""

fields = {
    "Title": "Educational AI Song Producer (Suno, AI Art, Lyric-Video Editing)",
    "Status": "Drafting",
    "Source": "Upwork",
    "Job Description": job_description,
    "Client Info": (
        "United Kingdom, Newbury. Payment and phone verified; 5.0/5 from 14 reviews; "
        "14 jobs posted; 93% hire rate; 3 open jobs; $494K spent; 26 hires and 10 active "
        "contracts; $84.88/hour average paid; 5,387 hours; mid-sized company (10–99); "
        "member since 2025-01-16."
    ),
    "Current Status": (
        "Conditional apply; estimated fit 7.8/10. Low Connects risk: 17 of 125. "
        "Client economics are exceptional and no interviews are reported. Strong fit for AI visuals, "
        "editing, captions, templates, and QA; key gap is verified Suno/music-production evidence."
    ),
    "Following Plan": (
        "1. Confirm genuine hands-on Suno experience and active access.\n"
        "2. Insert direct URLs for Product Landing Page Motion and UGC Home Care.\n"
        "3. Add a genuine Suno or lyric-sync example if available; do not mislabel ad work.\n"
        "4. Bid $26/hour without boosting.\n"
        "5. Keep private-tool credentials inside a funded contract and begin with the paid trial."
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
