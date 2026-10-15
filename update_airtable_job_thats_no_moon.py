import json
import os
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
url = f"https://api.airtable.com/v0/{env['AIRTABLE_BASE_ID']}/{env['AIRTABLE_TABLE_ID']}"
headers = {
    "Authorization": f"Bearer {env['AIRTABLE_PAT']}",
    "Content-Type": "application/json",
}

job_data = {
    "fields": {
        "Title": "AI Video Artist for Cinematic Sci-Fi / Esoteric Film — That's No Moon",
        "Status": "Drafting",
        "Job Description": """Fixed price: $1,500 USD initial trial month | Connects: not provided
Posted yesterday | Worldwide | Target start: mid-September

AI Video Artist for Cinematic Sci-Fi / Esoteric Film (Month-to-Month)

Project: That's No Moon, a feature-length (90-minute) esoteric AI film about the moon as an engineered construct, a Truman Show-esque control room, and an ancient metallic vault below lunar dust.

Need: Generate tightly controlled images and AI-video footage alongside a spoken transcript; collaborate and iterate sequence by sequence; deliver assets toward 15–20 minutes of approved finished footage per month.

Visual direction: Grounded, gritty optical realism. Blend 1960s retro-futurism, Apollo archival film stock, and sterile mid-century control rooms with a subtle esoteric undercurrent. Buried metallic architecture, faint geometric circuitry, and acoustic chambers must feel atmospheric, eerie, and restrained—not generic fantasy, plastic AI, or CGI spectacle.

Requirements: Veo, Seedance, Kling or similar AI video; Midjourney, Flux or similar image generation; cinematic lighting, film-stock emulation, architectural scale; precise art-direction iteration; ongoing month-to-month availability.

Client supplied teaser: https://drive.google.com/file/d/1QzzGnDNYHAHY4RRWsZ3ay1SsQMtIjEwt/view?usp=sharing""",
        "Client Info": "Worldwide. Client identity, hire history, payment verification, connects, and auction data were not supplied. Posting is a repost because the original was removed for an administrative issue.",
        "Current Status": "Drafting tailored proposal. Fit 8.5/10: strong tooling and cinematic-photorealism fit, with LUMINA low-key lighting/optical-realism assets selected. Teaser could not be previewed from Google Drive during preparation. Fixed $1,500 trial needs a bounded sequence, shot-count, and revision agreement before acceptance.",
        "Following Plan": "1. Submit the no-boost proposal if Connects cost is below 20; reassess at 20–40 Connects against live bids.\n2. Attach/select LUMINA Eclipse Diver on Obsidian Glass and Watch on Wrist, Urban Night.\n3. Confirm trial scope: target final duration, approximate shot count, revision rounds, and delivery responsibilities.\n4. If awarded, create an approved visual bible with archival/film-stock, lens, lighting, scale, texture, and reveal-restraint rules before production.\n5. Establish a sequence-by-sequence review cadence for the month-to-month engagement.",
        "ID": "JOB-FILM-001",
    }
}

response = requests.post(url, headers=headers, json=job_data, timeout=30)
if response.ok:
    print("Successfully added job to Airtable.")
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
    response.raise_for_status()
