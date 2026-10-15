import json
import os

import requests


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
Connects: Not supplied
Duration: More than 6 months
Weekly capacity: Less than 30 hours/week
Experience level: Expert
Project type: Ongoing project
Posted: 3 hours ago
Location: Worldwide

AI Video Creation Expert for Premium Mattress Brand (Long-Term Potential)

Create high-quality social media ads for a premium bedding brand. The first trial is a 15-second AI video closely replicating an Avocado Green reference ad using supplied product images/video, relevant stock footage, and natural-looking people. Deliver Reels and feed ratios with a script focused on certified organic cotton, wool, latex, comfort, support, and healthy sleep.

Mandatory skills: AI Video Generation; Social Media Advertising.
Preferred qualification: 90%+ Job Success Score.
Activity: 10–15 proposals; client viewed today; 0 interviewing; 0 invites.
Reference: https://www.facebook.com/ads/library/?id=2092290121503731"""

cover_letter = """Hi,

I reviewed the Avocado Green reference. Its effectiveness comes from a simple 15-second structure: tactile macro shots of the mattress materials, natural hand interaction, a soft lifestyle moment with a real-looking person, and a clean certification-led end card. I can recreate that pacing and premium-natural tone using your existing product images and footage, then generate only the human or transitional shots needed to complete the story.

My closest relevant project is a 15-second AI UGC Home Care Product Ad created with MiniMax H3. I directed a realistic on-camera creator in a warm domestic setting, maintained believable product interaction, and built the piece specifically for an organic paid-social feel. I have also created a premium fashion eyewear commercial with two consistent, realistic models from supplied product and wardrobe references.

For your trial, I would map the voiceover into a compact sequence: premium product/material hook; clean construction contrast; tactile cotton, wool, and latex macros; a natural person-in-bed lifestyle payoff; then the brand promise and website CTA.

I use the model best suited to each shot—MiniMax H3, Kling, Seedance, or Higgsfield—then combine the generated shots with supplied product assets and stock footage into a cohesive master. I can deliver both 9:16 Reels and 4:5 feed versions.

Relevant work:
- AI UGC Home Care Product Ad | MiniMax H3: [INSERT DIRECT VIDEO URL]
- AI Fashion Eyewear Commercial | MiniMax H3: [INSERT DIRECT VIDEO URL]

My proposed rate is $25/hour, with an initial 8–10 hour cap for the 15-second trial after reviewing the asset library and confirming revision expectations. I am available for an ongoing engagement under 30 hours per week if the trial is a strong fit.

Best,
Dennis Bui
https://aiartimind.com"""

job_data = {
    "fields": {
        "Title": "AI Video Creation Expert for Premium Mattress Brand",
        "Status": "Drafting",
        "Source": "Upwork",
        "Job Description": job_description,
        "Cover Letter": cover_letter,
        "Client Info": (
            "Worldwide. Expert-level hourly project, <30 hrs/week, >6 months, ongoing. "
            "Posted 3 hours ago; 10–15 proposals; 0 interviewing; client viewed today. "
            "Payment verification, hire rate, spend, location, hourly range, and proposal Connects not supplied."
        ),
        "Current Status": (
            "Strong 9.1/10 fit. Reference ad reviewed: tactile natural-material macros, "
            "soft person-in-bed lifestyle shot, premium neutral styling, and certification-led end card. "
            "Application drafted; direct portfolio URLs and profile JSS still require verification."
        ),
        "Following Plan": (
            "1. Insert direct MiniMax H3 UGC Home Care and Fashion Eyewear video URLs.\n"
            "2. Verify JSS, Connects, client payment/history, and hidden hourly range.\n"
            "3. Bid $25/hour with an 8–10 hour trial cap; do not boost.\n"
            "4. Attach UGC Home Care video first and submit while timing remains favorable."
        ),
        "ID": "JOB-VIDEO-001",
    }
}

response = requests.post(url, headers=headers, json=job_data, timeout=30)

if response.ok:
    print("Successfully added JOB-VIDEO-001 to Airtable.")
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
    response.raise_for_status()
