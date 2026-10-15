"""Create or refresh the invited AI-tools research job in Airtable."""

from pathlib import Path
import os
import requests


ROOT = Path(__file__).resolve().parent
TITLE = "Freelancers & Independent Professionals - Active Users of AI Tools (Crowdsourcing Project)"
JOB_ID = "JOB-RESEARCH-001"


def load_env():
    for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


def main():
    load_env()
    base = os.environ.get("AIRTABLE_BASE_ID", "appSTxBDPzcjMcIvu")
    table = os.environ.get("AIRTABLE_TABLE_ID", "tbl05fiEfgfTzt36b")
    endpoint = f"https://api.airtable.com/v0/{base}/{table}"
    headers = {"Authorization": f"Bearer {os.environ['AIRTABLE_PAT']}", "Content-Type": "application/json"}
    draft = (ROOT / "application_draft_ai_tools_crowdsourcing.md").read_text(encoding="utf-8")
    cover = draft.split("## Cover letter\n", 1)[1].split("\n## Candidate use cases", 1)[0].strip()

    response = requests.get(
        endpoint,
        headers=headers,
        params={"filterByFormula": f'OR({{Title}}="{TITLE}",{{ID}}="{JOB_ID}")', "maxRecords": 10},
        timeout=30,
    )
    response.raise_for_status()
    matches = response.json().get("records", [])
    if len(matches) > 1:
        raise RuntimeError("Multiple matching Airtable records; resolve duplicates manually")

    fields = {
        "ID": JOB_ID,
        "Title": TITLE,
        "Source": "Upwork",
        "Status": "Drafting",
        "Cover Letter": cover,
        "Client Info": "US Enterprise client; payment verified; 4.93/5 (295 reviews); 100% hire rate; $886K spent",
        "Job Description": (
            "Budget: $15 fixed; invited proposal says 0 Connects. Research project for frequent professional "
            "AI-tool users. Submit 2–3 genuine use cases with tool, goal, actual verbatim prompts, and workflow "
            "experience. $3–$5 per accepted use case. Google Form and sample attachment required."
        ),
        "Current Status": (
            "2026-10-14: Proposal drafted. Two real-work use cases documented: screw restoration "
            "with authorized verbatim fal.ai prompt, and Vietnamese AI influencer video test with "
            "prompt still missing. Sample attachment is also missing. No proposal or form submitted. "
            "Connects spent: 0."
        ),
        "Following Plan": (
            "Retrieve an original prompt from the Vietnamese AI influencer test and verify its use and disclosure rights. "
            "Review sample attachment and Google Form. Confirm live Enterprise invitation and submit only "
            "accurate material."
        ),
        "Fit Score": 85,
        "Connects": 0,
    }
    if matches:
        record_id = matches[0]["id"]
        response = requests.patch(f"{endpoint}/{record_id}", headers=headers, json={"fields": fields}, timeout=30)
        response.raise_for_status()
        print("Updated existing Airtable draft record:", record_id)
    else:
        response = requests.post(endpoint, headers=headers, json={"fields": fields, "typecast": True}, timeout=30)
        response.raise_for_status()
        print("Created Airtable draft record:", response.json()["id"])


if __name__ == "__main__":
    main()
