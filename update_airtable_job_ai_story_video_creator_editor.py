import json
import os

import requests


JOB_ID = "JOB-VIDEO-003"


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

job_description = """Budget: $10–$20/hour
Recommended bid: $15/hour
Connects required: 6
Available Connects: 77 (71 after application)
Duration: Less than 1 month
Workload: Not sure
Experience level: Intermediate
Project type: One-time; contract-to-hire; potential ongoing work
Posted: 1 hour ago
Location: Worldwide

AI Story Video Creator / Editor

Create short AI-generated story videos for TikTok, Instagram Reels, and YouTube Shorts in a style similar to @logicbend: unique characters, strong visual storytelling, professional cinematography, natural colour, consistent characters/scenes, editing, pacing, sound effects, and music. Output should feel cinematic and not obviously AI-generated.

Application requirements: start cover letter with “Hello world”; explain workflow from story/script through generation and finishing; provide 2–3 relevant projects; explain tools and production method for each.

Mandatory skills: Video Editing; AI Video Generator.
Activity: 5–10 proposals; client viewed 27 minutes ago; 1 interviewing; no invites.
Bid range: $7 low; $12.44 average; $20 high."""

cover_letter = """Hello world

I would approach these as directed short films, not as a collection of attractive AI clips. Before generating anything, I reduce the script to one clear hook, escalation, and payoff; lock the characters and visual world; then design each camera angle around what that moment needs to communicate.

My workflow is:
1. Script and story — Claude Code + Codex: I refine the premise into a strong hook, escalation, and payoff, then break the script into scenes, actions, dialogue/voiceover, shot durations, and production requirements.
2. Character/world development — GPT Image 2 + Google Nano Banana: I create consistent character sheets, expressions, wardrobe, environments, props, and hero keyframes. These become a locked reference bible for faces, proportions, palette, lighting, and visual rules.
3. Storyboard and shot design — Claude Code + Codex: I create a vertical storyboard and structured shot manifest covering framing, lens feel, camera angle, movement, screen direction, performance, transition, audio cue, prompt, and reference assets.
4. Motion generation — MiniMax H3 + Kling + Seedance + Higgsfield + Veo: I choose the model per shot and use image-to-video, reference, and first/last-frame controls where available. Shots stay short and modular for consistency and editorial control.
5. Continuity QA — Codex + Claude Code + manual review: I compare each output with the character/world bible and track face, wardrobe, props, geography, eyelines, hands, lighting, camera direction, and motion. Failed shots are regenerated or repaired before editing.
6. Edit and sound — Adobe Premiere Pro: I assemble selects, shape pacing, synchronize voiceover, and add music, ambience, Foley/SFX, captions, colour matching, and subtle grain. Codex and Claude Code support Premiere Pro by preparing edit lists, shot manifests, subtitle files, asset/version checks, and automation scripts; I retain manual control of the creative edit.
7. Export and delivery — Premiere Pro + automated QA: I export platform-ready 9:16 masters and requested hook variants. Codex/Claude Code help verify duration, resolution, frame rate, filenames, missing media, and caption-safe areas before final manual playback approval.

This workflow uses coding agents for structure, consistency, and production automation while keeping story judgment, shot selection, pacing, and final quality control human-led.

Relevant work:
- AI Fashion Eyewear Commercial | MiniMax H3 — two consistent people across cinematic close-ups, full-body compositions, and product details: [INSERT DIRECT VIDEO URL]
- AI UGC Home Care Product Ad | MiniMax H3 — a realistic creator, believable product interaction, warm domestic light, and natural social-video direction: [INSERT DIRECT VIDEO URL]
- AI Product Landing Page Motion Design | MiniMax H3 — visual hooks, dramatic zooms, feature callouts, and fast transitions from one product reference: [INSERT DIRECT VIDEO URL]

These are commercial shorts rather than character-story films, but together they demonstrate consistent people, natural-looking scenes, and controlled short-form pacing. I would be glad to begin with one paid test story.

My rate is $15/hour.

Best,
Dennis Bui
https://aiartimind.com"""

fields = {
    "Title": "AI Story Video Creator / Editor",
    "Status": "Drafting",
    "Source": "Upwork",
    "Job Description": job_description,
    "Client Info": (
        "Indonesia. Payment method and phone verified. Other client history, spend, "
        "rating, hire rate, and total hours were not supplied."
    ),
    "Current Status": (
        "Apply recommendation; 8.0/10 fit. Low Connects risk: 6 of 77. "
        "Low competition but 1 candidate interviewing. Main gap: no documented completed "
        "character-story short. Proposal drafted with honest adjacent portfolio positioning."
    ),
    "Following Plan": (
        "1. Insert direct URLs for Fashion Eyewear, UGC Home Care, and Landing Page Motion.\n"
        "2. If possible, manually review 2–3 @logicbend posts while logged into Instagram.\n"
        "3. Bid $15/hour and do not boost.\n"
        "4. Preserve exact opening line 'Hello world' and propose one paid test story."
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
