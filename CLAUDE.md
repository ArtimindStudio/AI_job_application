# Upwork Job Application Workspace

## Overview
This workspace manages Upwork & AI job applications, including job tracking via Airtable, application drafting, and portfolio management.

## Key Workflow
When processing a new Upwork job, use the `/upwork-job-automation` skill. It will:
1. Analyze the bid economics (connects, competition, rate strategy)
2. Generate an Airtable update script (`update_airtable_job_<slug>.py`)
3. Draft tailored application materials (`application_draft_<slug>.md`)

## Airtable Integration
- Credentials in `.env` (PAT, base ID, table ID)
- Base: `appSTxBDPzcjMcIvu`, Table: `tbl05fiEfgfTzt36b`
- Template script: `update_airtable_job.py`

## AI Workflow (for cover letters)
1. **System & Automation:** Antigravity & n8n
2. **Generative Content:** Google Nano Banana, Google VEO, KlingAI
3. **Editing & Polish:** Canva & Adobe Photoshop

## Available Skills
- `upwork-job-automation` — Full job processing pipeline
- `ai-creative-producer` — Generate ad assets (scripts, prompts, copy)
- `ad-strategy-analyzer` — Reverse-engineer ad mechanics

## Important Files
- `workflow_preferences.md` — AI workflow description & availability
- `ai_creative_stack.md` — Full tool list
- `Portfolio_Assets/` — Curated portfolio images
- `find_and_track_jobs.py` — Automated job search via Playwright + Airtable
- `CV_AI_Specialist.md` / `.html` — Current CV
- `Portfolio_AI_Specialist.md` / `.html` — Portfolio page

## Conventions
- Job IDs follow `JOB-CATEGORY-00X` pattern
- Application drafts: `application_draft_<slug>.md`
- Airtable scripts: `update_airtable_job_<slug>.py`
- Skip implementation plans for job processing — execute immediately
