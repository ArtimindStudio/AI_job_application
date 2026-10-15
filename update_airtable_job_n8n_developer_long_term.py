"""Idempotently add the n8n Developer opportunity to the Airtable tracker."""

from pathlib import Path
import os
import requests


ROOT = Path(__file__).resolve().parent
TITLE = "n8n Developer - Long-Term Role"
URL = "https://www.upwork.com/jobs/~022104455237122207096"
JOB_ID = "JOB-AUTO-002"


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
    params = {
        "filterByFormula": f'OR({{Job URL}}="{URL}",{{Title}}="{TITLE}",{{ID}}="{JOB_ID}")',
        "maxRecords": 10,
    }
    response = requests.get(endpoint, headers=headers, params=params, timeout=30)
    response.raise_for_status()
    records = response.json().get("records", [])
    if records:
        print("Existing matching Airtable record(s):", ", ".join(record["id"] for record in records))
        print("No new record created; review existing entry before any update.")
        return

    fields = {
        "ID": JOB_ID,
        "Title": TITLE,
        "Source": "Upwork",
        "Job URL": URL,
        "Status": "Drafting",
        "Client Info": "Norway; payment verified; 5.0/5 (5 reviews); 28% hire rate; $990 spent; 12 hires",
        "Job Description": (
            "Budget: $30–$60/hour; 20 Connects required (32 available at review); "
            "30+ hours/week, 6+ months, contract-to-hire. Build and maintain n8n ecommerce "
            "automations using APIs, webhooks, JavaScript, AI/LLM integrations, and AI coding tools. "
            "Initial work in separate test environment. Applicant must give examples of n8n workflows. "
            "50+ proposals in user-provided snapshot."
        ),
        "Current Status": (
            "2026-09-28: Draft prepared, not submitted. Recommendation is to skip current 20-Connect "
            "auction because fit is 8/10, competition is 50+, and client hiring/spend history is weak. "
            "Connects spent: 0."
        ),
        "Following Plan": (
            "If invited or competition improves, verify two n8n portfolio examples and available work samples; "
            "check live Connect cost; propose $36/hour and a paid test-environment milestone."
        ),
        "Fit Score": 80,
        "Connects": 0,
    }
    response = requests.post(endpoint, headers=headers, json={"fields": fields, "typecast": True}, timeout=30)
    response.raise_for_status()
    print("Created Airtable draft record:", response.json()["id"])


if __name__ == "__main__":
    main()
