import json
from pathlib import Path

import requests


def load_env(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            env[key.strip()] = value.strip()
    return env


workspace = Path(__file__).resolve().parent
env = load_env(workspace / ".env")
base_url = f"https://api.airtable.com/v0/{env['AIRTABLE_BASE_ID']}/{env['AIRTABLE_TABLE_ID']}"
headers = {
    "Authorization": f"Bearer {env['AIRTABLE_PAT']}",
    "Content-Type": "application/json",
}
job_url = "https://www.upwork.com/jobs/~022097165605765461044"

cover_letter = """Hi,

For a 45–60 episode AI drama, the hard part is not generating attractive shots—it is preventing character, wardrobe, geography, lighting, and emotional continuity from drifting over 90 finished minutes.

My workflow begins with a locked series bible: character turnarounds and expression sheets, wardrobe and prop states, ship/location references, palette and lens rules, and approved hero frames. Every asset receives a stable ID and is tracked by episode, scene, shot, model version, references, and approval status. I then generate anchor frames with Google Nano Banana 2 / Omni, Midjourney, or Flux and animate approved frames through Veo, Kling, or Seedance using image-to-video and first/last-frame controls. Visual cleanup and match grading are handled in Photoshop, with a continuity review before each shot enters the edit.

For vertical storytelling, I would design each 1.5–2 minute episode around an immediate visual conflict, compressed coverage, readable close-ups, and a strong final beat or cliffhanger. The Age of Sail setting also needs a dedicated world bible so ship geometry, weather, period materials, costumes, and props remain coherent across episodes.

Relevant completed work:
- [INSERT CINEMATIC NARRATIVE SAMPLE]
- [INSERT CHARACTER-CONSISTENCY SAMPLE]
- [INSERT VERTICAL EDIT OR REEL]

For the complete 90-minute scope, my preliminary price is $20,000 fixed, or approximately $222 per finished minute—about $333 for a 1.5-minute episode and $444 for a 2-minute episode. I can follow your 15% / 20% / 20% / 25% / 20% milestone structure, provided each stage has defined acceptance criteria and revision limits.

One point to clarify: my working languages are English and Vietnamese. For Chinese dialogue and final-language QA, I would need client-approved Chinese scripts/VO or a native Chinese collaborator. I can own the visual pipeline and coordinate subtitles, music, and SFX against those approved language assets.

Before we proceed, please confirm whether the full project budget is $20,000–$25,000 as stated in the description—the Upwork header currently displays $2,000—and whether one producer owns the full series or the work will be divided among the 10 hires.

Best,
Dennis Bui
https://aiartimind.com"""

job_data = {
    "fields": {
        "Title": "AI Video Producer Needed for Vertical Short Drama Series",
        "Status": "Drafting",
        "Job Description": f"""Connects: 8 | Available Connects: 157
Description budget: $20,000–$25,000 fixed | Upwork header: $2,000 fixed
Posted 1 hour ago | Worldwide | Intermediate | Complex project
Job URL: {job_url}

Produce approximately 90 minutes total across 45–60 vertical 9:16 episodes of 1.5–2 minutes each, set in the Age of Sail. Scope includes full scripts, consistent characters/world, all AI footage, Chinese VO, music, SFX, subtitles, masters, and platform versions. Timeline: 4–6 weeks. Milestones: scripts 15%, assets 20%, pilot 20%, main body 25%, final 20%.

Requirements: proven AI short-drama production at scale using Runway, Sora, Kling, or Jimeng; clear character-consistency workflow; strong editing, color, and sound; vertical storytelling; responsive English/Chinese communication. Application must include 2–3 completed samples/reel, consistency approach, and per-episode/minute cost.

Activity: 5–10 proposals, 0 interviewing, 0 invites. Client last viewed 55 minutes ago. Needs 10 freelancers.

Client: Hong Kong; payment not verified; phone verified; one job posted; 0% hire rate; two open jobs; member since September 4, 2026.""",
        "Client Info": "Hong Kong. Payment method not verified; phone verified. New client: 1 job posted, 0% hire rate, 2 open jobs, member since Sep 4, 2026. Needs 10 freelancers. Budget conflict between $2,000 header and $20,000–$25,000 description.",
        "Current Status": "Conditional draft. Creative-track fit 63/100. Eight Connects and low competition are attractive, but no completed vertical-drama video samples were found locally and Chinese fluency is not documented. Do not submit until genuine sample links are inserted and Chinese VO/language QA coverage is confirmed.",
        "Following Plan": "1. Insert 2–3 genuine completed video/reel URLs; do not use stills as substitutes.\n2. Confirm whether work is divided among 10 hires or one producer owns all 90 minutes.\n3. Confirm the actual funded budget and never start before a verified, funded milestone.\n4. Confirm client-supplied Chinese script/VO or native Chinese collaborator.\n5. Bid $20,000 for full 90-minute ownership ($222/min; $333–$444/episode), no boost.\n6. Lock acceptance criteria and revision limits for every milestone.",
        "Cover Letter": cover_letter,
        "ID": "JOB-DRAMA-001",
    }
}

query = requests.get(
    base_url,
    headers=headers,
    params={
        "pageSize": 10,
        "filterByFormula": f"FIND('{job_url}', {{Job Description}})",
    },
    timeout=30,
)
query.raise_for_status()
records = query.json().get("records", [])

if records:
    record_id = records[0]["id"]
    response = requests.patch(
        f"{base_url}/{record_id}", headers=headers, json=job_data, timeout=30
    )
    action = "updated"
else:
    response = requests.post(base_url, headers=headers, json=job_data, timeout=30)
    action = "added"

if response.ok:
    print(f"Successfully {action} job in Airtable.")
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
    response.raise_for_status()
