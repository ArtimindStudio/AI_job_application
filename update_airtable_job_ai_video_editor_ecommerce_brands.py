import json
import os

import requests


JOB_ID = "JOB-VIDEO-004"


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

job_description = """Budget: $1,000 fixed-price; scope not defined
Client stated rate: $20 per 1.5 minutes of editing
Recommended full-production rate: $60–$90 per 1.5-minute video
Connects required: 16
Available Connects: 74 (58 after application)
Experience level: Expert
Project type: Ongoing; contract-to-hire; paid trial
Posted: 1 hour ago
Location: Worldwide
Canonical URL: https://www.upwork.com/jobs/~022097975435650841189

AI Video Editor for E-commerce Brands

Create AI UGC, Pixar/3D-style videos, claymation, and AI interviews for ecommerce brands. Client supplies scripts, AI tools if hired, voiceover in most cases, brand details, and briefs. Requires AI generation/editing, short-form advertising knowledge, brand-reference execution, speed, communication, and reliability.

Quality reference: https://adityagautam.my.canva.site/

Activity: 10–15 proposals; client viewed 22 minutes ago; 1 interviewing; 5 invites; 1 unanswered invite.
Bid range: $130 low; $940 average; $1,400 high."""

cover_letter = """Hi,

I reviewed the quality reference. The range is broader than AI generation alone: 4:5 direct-response edits with bold hooks and talking heads, caption-led 9:16 Pixar-style stories, ecommerce verticals, AI presenters, and 16:9 VSL content. The common requirement is strong ad structure—an immediate hook, readable message hierarchy, frequent visual change, clean sound, and consistent brand execution.

My closest work includes:
- AI UGC Home Care Product Ad | MiniMax H3 — realistic creator, believable product interaction, and paid-social pacing: [INSERT DIRECT VIDEO URL]
- AI Fashion Eyewear Commercial | MiniMax H3 — two consistent models across cinematic product compositions: [INSERT DIRECT VIDEO URL]
- AI Product Landing Page Motion Design | MiniMax H3 — hook-driven typography, feature callouts, zooms, and transitions: [INSERT DIRECT VIDEO URL]

My workflow:
1. Brief/script breakdown — Claude Code + Codex: map the script, VO, brand kit, and reference into hooks, scenes, shot durations, captions, product moments, and formats.
2. Keyframes and consistency — GPT Image 2 + Google Nano Banana: build approved character/product sheets, environments, wardrobe, expressions, and style frames.
3. AI motion — MiniMax H3, Kling, Seedance, Higgsfield, Veo, or Runway: choose the model per shot and use reference, camera, motion, and first/last-frame controls where available.
4. QA: check faces, product geometry, hands, wardrobe, lip-sync, eyelines, lighting, screen direction, captions, and brand details; regenerate or repair weak shots.
5. Edit and delivery — Adobe Premiere Pro: assemble takes, tighten pacing, add captions, B-roll, music, ambience, SFX, colour matching, and platform reframing. Codex/Claude Code support edit lists, subtitles, asset/version checks, and Premiere automation scripts.

I am available for 20–30 hours per week and can start with the paid trial. I can match $20 per 1.5-minute edit when you provide approved video assets/generated clips, script, VO, brand kit, and a clear edit brief, with one consolidated revision. Full AI keyframe/video generation, consistency work, artifact repair, sound design, and finishing would be $60–$90 per 1.5-minute video depending on shot count and style.

My strongest current examples are realistic AI UGC and premium product videos. Pixar/3D, claymation, and AI-interview formats are capabilities I would demonstrate through your paid trial rather than mislabeling unrelated portfolio work.

Best,
Dennis Bui
https://aiartimind.com"""

fields = {
    "Title": "AI Video Editor for E-commerce Brands",
    "Status": "Drafting",
    "Source": "Upwork",
    "Job Description": job_description,
    "Client Info": (
        "India, Ghaziabad. Media & Entertainment company, 10–99 people. Payment verified; "
        "4.81/5 from 17 reviews; 171 jobs posted; 19% hire rate; 1 open job; $4.8K spent; "
        "38 hires and 19 active contracts; member since 2022-05-08."
    ),
    "Current Status": (
        "Conditional apply recommendation; 8.7/10 AI-video fit. Low Connects risk: 16 of 74. "
        "Main risks are 19% client hire rate, undefined $1,000 scope, and unsustainable $20 rate "
        "if full AI generation is included. Portfolio URLs still required."
    ),
    "Following Plan": (
        "1. Insert direct URLs for UGC Home Care, Fashion Eyewear, and Landing Page Motion.\n"
        "2. Confirm whether $20/1.5 minutes is editing-only or end-to-end AI production.\n"
        "3. Quote $20 for tightly scoped supplied-asset editing; $60–$90 for full production.\n"
        "4. Confirm $1,000 batch scope, weekly volume, revisions, and client-funded tool access.\n"
        "5. Apply without boosting if the scope distinction can be stated clearly."
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
