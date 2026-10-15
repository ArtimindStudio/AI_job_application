"""Create or find the CB2026_047 draft in the Upwork Airtable tracker.

Run from the workspace root. Credentials are read from .env and never printed.
"""

from pathlib import Path
import os
import requests


ROOT = Path(__file__).resolve().parent
JOB_URL = "https://www.upwork.com/jobs/~022100895671110876438"
JOB_TITLE = "CB2026_047 - Image Data Collection – Malay, Vietnamese, Indonesian, Japanese, Hindi, Chinese & Thai"
JOB_ID = "JOB-DATA-047"


def load_env():
    for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


def main():
    load_env()
    draft = (ROOT / "application_draft_cb2026_047_image_data_collection.md").read_text(encoding="utf-8")
    proposal = draft.split("## Proposal\n", 1)[1].split("\n## Portfolio", 1)[0].strip()
    token = os.environ["AIRTABLE_PAT"]
    base = os.environ.get("AIRTABLE_BASE_ID", "appSTxBDPzcjMcIvu")
    table = os.environ.get("AIRTABLE_TABLE_ID", "tbl05fiEfgfTzt36b")
    endpoint = f"https://api.airtable.com/v0/{base}/{table}"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    # Compare both title and URL, and also protect the stable local ID.
    params = {
        "filterByFormula": (
            'OR({Job URL}="' + JOB_URL + '",'
            '{Title}="' + JOB_TITLE + '",'
            '{ID}="' + JOB_ID + '")'
        ),
        "maxRecords": 10,
    }
    response = requests.get(endpoint, headers=headers, params=params, timeout=30)
    response.raise_for_status()
    existing = response.json().get("records", [])
    if existing:
        if len(existing) != 1:
            raise RuntimeError("Multiple matching records found; review duplicates before updating")
        record_id = existing[0]["id"]
        patch = {"fields": {
            "Cover Letter": proposal,
            "Current Status": (
                "2026-10-14: Public job remains active with 69 hires of 99 targeted, 50+ proposals, "
                "328 interviews and 2,508 invitations. Candidate confirms iPhone 13 and "
                "immediate availability. Invitation status remains to be confirmed. "
                "Proposal unsubmitted; Connects spent: 0."
            ),
            "Following Plan": (
                "Check whether the direct invitation "
                "is still active and verify the proposal form's Connects cost. Clarify accepted-photo count, "
                "categories, travel area, deadline, and rejection criteria before agreeing to the $50 scope."
            ),
        }}
        response = requests.patch(f"{endpoint}/{record_id}", headers=headers, json=patch, timeout=30)
        response.raise_for_status()
        print("Updated existing Airtable draft record:", record_id)
        return

    fields = {
        "ID": JOB_ID,
        "Title": JOB_TITLE,
        "Source": "Upwork",
        "Job URL": JOB_URL,
        "Status": "Drafting",
        "Cover Letter": proposal,
        "Client Info": "Akshita Singh; India; payment verified; 4.59/5; 89% hire rate; invitation received",
        "Job Description": (
            "Budget: $50 fixed. Invitation response: 0 Connects; no Connects spent. "
            "Vietnamese field data collection in Vietnam. Must reside in a listed country, "
            "have an iPhone 12 or newer, personally photograph real items in public places, "
            "meet focus/text/variety requirements, and avoid PII, stock images, screenshots, "
            "mock-ups, duplicates, and AI-generated imagery."
        ),
        "Current Status": (
            "2026-09-23: Proposal drafted. iPhone model and availability awaiting candidate confirmation. "
            "Invitation has not been answered; no proposal submitted."
        ),
        "Following Plan": (
            "Confirm iPhone model and availability. Clarify photo count, categories, travel area, "
            "deadline, acceptance criteria, and $50 milestone scope. Submit factual proposal through invitation."
        ),
        "Fit Score": 70,
        "Connects": 0,
    }
    response = requests.post(endpoint, headers=headers, json={"fields": fields, "typecast": True}, timeout=30)
    response.raise_for_status()
    print("Created Airtable draft record:", response.json()["id"])


if __name__ == "__main__":
    main()
