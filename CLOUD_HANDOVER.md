# Claude Code Cloud — Handover: Autonomous AI Job Application Workflow

## 1. Cloud environment settings (claude.ai/code → New environment)

| Setting | Value |
|---|---|
| Repository | `ArtimindStudio/AI_job_application` (install the Claude GitHub App on it) |
| Branch | `main` (Claude works on `claude/*` branches and opens PRs) |
| Network access | **Custom** — allow: `api.airtable.com`, `*.airtable.com`, `weworkremotely.com`, `remoteok.com`, `remotive.com`, `workingnomads.com`, `wellfound.com`, `app.outlier.ai`, `app.alignerr.com`, `dataannotation.tech`, `connect.appen.com`, `app.telusinternational.ai`, `mercor.com`, `pypi.org`, `files.pythonhosted.org` (or pick **Full** for simplicity) |
| Environment variables | `AIRTABLE_PAT=<new rotated token>`<br>`AIRTABLE_BASE_ID=appSTxBDPzcjMcIvu`<br>`AIRTABLE_TABLE_ID=tbl05fiEfgfTzt36b` |
| Setup script | `pip install -r requirements.txt && playwright install --with-deps chromium` |
| Connectors (optional) | Airtable, Gmail, Google Drive |
| Model | Opus 5.5 |

Never commit `.env`. Add `.env`, `__pycache__/`, `*.docx`, `*.pdf` (personal docs) to `.gitignore`.

## 2. Files the repo should contain

- `CLAUDE.md` — workspace rules (copy from local `D:\Projects\Upwork\CLAUDE.md`)
- `CV_AI_Specialist.md`, `Portfolio_AI_Specialist.md`, `workflow_preferences.md`, `ai_creative_stack.md`
- `find_and_track_jobs.py`, `update_airtable_job.py`, `get_airtable_schema.py`, `requirements.txt`
- `skills/` (upwork-job-automation, ai-creative-producer, ad-strategy-analyzer) → place under `.claude/skills/`
- `docs/browser_automation_lessons.md` — copy of the memory notes below
- `.env.example` with empty keys

## 3. Hand-over prompt (paste as the first message)

```
You are continuing my autonomous AI/remote job application workflow. Read CLAUDE.md,
CV_AI_Specialist.md, workflow_preferences.md and docs/browser_automation_lessons.md first.

WHO I AM: Bui Quang Dung (Dennis), Hanoi, Vietnam, remote worldwide. AI Creative Specialist:
generative image/video (Nano Banana, VEO, Kling, Midjourney, Flux), Python + n8n + Airtable
automation, Shopify/WordPress e-commerce, ex-Samsung procurement, MBA Foreign Trade University.
English fluent, Vietnamese native. Contact: hello.artimind@gmail.com.

TARGET ROLES: AI training / RLHF / AI evaluator, prompt writer / prompt engineering,
data annotation (image, video, audio), e-commerce data analyst, AI creative producer,
AI video/image generation, automation (n8n/Python) freelance and remote roles.

SOURCES:
- Public boards (scrape/API): RemoteOK, We Work Remotely, Remotive, Working Nomads, Wellfound.
- AI-training platforms where I already have accounts (need my login — flag, don't try
  to sign in): Outlier, DataAnnotation.tech, Alignerr, TELUS Digital, Appen, Mindrift, Mercor.
  Status: Outlier — AI Training Specialist & Prompt Writer applied, Audio Transcription completed;
  E-commerce Data Analyst, Image Description, Video Annotation not yet applied.

AIRTABLE: base appSTxBDPzcjMcIvu, table "AI Job" (tbl05fiEfgfTzt36b). Creds in env vars
AIRTABLE_PAT / AIRTABLE_BASE_ID / AIRTABLE_TABLE_ID. Fields: ID (JOB-CATEGORY-00X), Title,
Client Info, Cover Letter, Status, Source (use typecast:true for new options), Job URL,
Job Description, Current Status, Following Plan, Fit Score, Applied Date.
Search by title before creating to avoid duplicates.

FIT SCORE (100): skill match 30, experience 20, Vietnam eligibility 15, English 15,
qualification 10, compensation 10. Only draft applications for score >= 65.
Skip roles restricted to US/EU residents, senior backend engineering, or NSFW content.

EACH RUN:
1. Pull new postings from public sources (last 7 days) matching target roles.
2. Score each; write to Airtable with Status=Discovery and the score.
3. For >= 65: write a tailored cover letter (name specific AI tools, no generic filler)
   into the record and application_drafts/<slug>.md.
4. Commit script/draft changes on a branch and open a PR summarizing top 5 jobs.
5. Never submit an application, accept terms, or sign in on my behalf from the cloud —
   list the ready-to-submit jobs with URLs so I can approve and submit them.

First task: audit the repo, make sure find_and_track_jobs.py runs in this environment
(headless Playwright, env-var creds), fix what's broken, then do one full run.
```

## 4. What cloud can't do (keep local)

- Logged-in platform actions (Outlier, DataAnnotation, TELUS, Alignerr) need your browser session
  — run those from the desktop app with Claude in Chrome, or link your computer to the cloud session.
- Exams/assessments must be done by you.
- Final "Submit" on any application needs your explicit approval.
