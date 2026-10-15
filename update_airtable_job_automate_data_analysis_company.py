"""Create the scoped data-analysis automation opportunity in Airtable once."""

from pathlib import Path
import os
import requests


ROOT = Path(__file__).resolve().parent
TITLE = "Automate Data Analysis for Company"
URL = "https://www.upwork.com/jobs/~022103567401517800431"
JOB_ID = "JOB-AUTO-003"


def load_env():
    for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


def main():
    load_env()
    draft = (ROOT / "application_draft_automate_data_analysis_company.md").read_text(encoding="utf-8")
    cover_letter = draft.split("## Cover letter\n", 1)[1].split("\n## Screening answer", 1)[0].strip()
    base = os.environ.get("AIRTABLE_BASE_ID", "appSTxBDPzcjMcIvu")
    table = os.environ.get("AIRTABLE_TABLE_ID", "tbl05fiEfgfTzt36b")
    endpoint = f"https://api.airtable.com/v0/{base}/{table}"
    headers = {"Authorization": f"Bearer {os.environ['AIRTABLE_PAT']}", "Content-Type": "application/json"}
    params = {
        "filterByFormula": f'OR({{Job URL}}="{URL}",{{Title}}="{TITLE}",{{ID}}="{JOB_ID}")',
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
            "Cover Letter": cover_letter,
            "Current Status": "2026-09-28: Revised proposal drafted with n8n schedule, verified totals, Claude narrative, Google Sheets run log, Gmail report and failure alert. Not submitted; Connects spent: 0.",
            "Following Plan": "Verify live job and Connect cost. Ask client for first platform, account, 3–5 KPIs, and sample report. Confirm Composio read actions or approved API/export, then submit the $150 one-platform pilot proposal.",
        }}
        response = requests.patch(f"{endpoint}/{record_id}", headers=headers, json=patch, timeout=30)
        response.raise_for_status()
        print("Updated existing Airtable draft record:", record_id)
        return

    fields = {
        "ID": JOB_ID,
        "Title": TITLE,
        "Source": "Upwork",
        "Job URL": URL,
        "Status": "Drafting",
        "Cover Letter": cover_letter,
        "Client Info": "India, Gurugram; small education company; payment/phone verified; 2 jobs, 1 hire, $150 spent; no reviews",
        "Job Description": (
            "Budget: $150 fixed; 13 Connects required, 32 available at review. "
            "Automate data pulls, analysis, and reporting across content platforms within one month. "
            "Skills: data analysis, Google Sheets, n8n, Make.com. Client requests recent relevant "
            "experience and certifications. 10–15 proposals and 1 hire in user-provided snapshot."
        ),
        "Current Status": (
            "2026-09-28: Proposal and screening answers drafted, not submitted. "
            "Recommend a $150 one-platform pilot; Connects spent: 0."
        ),
        "Following Plan": (
            "Verify live job and 13-Connect cost. Submit $150 scoped pilot proposal with truthful "
            "experience and no unsupported certification. Clarify platforms, metrics, access, "
            "refresh frequency, reporting format, and additional-platform pricing."
        ),
        "Fit Score": 75,
        "Connects": 0,
    }
    response = requests.post(endpoint, headers=headers, json={"fields": fields, "typecast": True}, timeout=30)
    response.raise_for_status()
    print("Created Airtable draft record:", response.json()["id"])


if __name__ == "__main__":
    main()
