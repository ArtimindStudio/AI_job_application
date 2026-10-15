---
name: Upwork Job Automation
description: Process a new Upwork job posting — analyze the bid economics, update the Airtable tracker, draft a tailored application with portfolio selection and cover letter.
user_invocable: true
---

# Upwork Job Automation Skill

Process and apply to Upwork jobs by updating the tracking database and preparing tailored application materials.

## Trigger
User pastes a job description or says "new job", "apply to this", etc.

## Steps

### 1. Parse the Job
Extract from the posting:
- Title, budget/rate range, connects required
- Key requirements and nice-to-haves
- Client info (location, history, spend)

### 2. Bid Decision — Connects & Competition Analysis
Fixed budget: **100 Connects/month**. Every application is a strategic bet.

**Decision Matrix:**
- **Low Risk (< 20 total connects):** Prioritize.
- **Medium Risk (20–40 connects):** Apply only if Fit Score > 9/10.
- **High Risk (> 40 connects):** Skip unless dream job or perfect long-term retainer.

**Competition Insights (Top 4 Bids):**
- 1st place bid > 80 Connects → likely agency magnet, avoid unless unique advantage.
- Large gap between 1st and 2nd → 2nd-4th slots still viable.

### 3. Rate Strategy
- If profile rate ($15) < client's floor → bid the client's floor minimum.
- **Confidence Play:** Bid Client Floor + 20-30% to signal proprietary tools & efficiency.
- **Value Anchor:** Always mention AI-Native workflow (30-50+ images/day) = 10x value per hour vs manual.

### 4. Update Airtable
Create a Python script (based on `update_airtable_job.py` template) that POSTs to Airtable REST API using credentials from `.env`:
- `AIRTABLE_PAT`, `AIRTABLE_BASE_ID` (`appSTxBDPzcjMcIvu`), `AIRTABLE_TABLE_ID` (`tbl05fiEfgfTzt36b`)

**Schema:**
- **Title**: String
- **Status**: "Active" | "Applied" | "Drafting" | "Failed"
- **Job Description**: Long Text (include budget & connects at top)
- **Connects Spent**: Number
- **Client Info**: String
- **Current Status**: Long Text (tracking notes)
- **Following Plan**: Long Text (next steps)
- **ID**: `JOB-CATEGORY-00X`

### 5. Draft Application Materials

**Portfolio Curation** (from `Portfolio_Assets/`):
- DTC/Ecommerce → hero shots, lifestyle images
- Health/Wellness → "Oasis", ingredients, splash, natural keywords
- SaaS/Tech → `Elite_Minimalist_Series/` assets

**AI Workflow Explanation** (from `workflow_preferences.md`):
1. **System & Automation Setup:** Antigravity & n8n
2. **Generative Content:** Google Nano Banana, Google VEO, KlingAI
3. **Editing & Polish:** Canva & Adobe Photoshop

**Cover Letter:** Tailored to the specific job, highlighting relevant experience and the AI-native workflow advantage.

### 6. Output
Produce:
1. `application_draft_<slug>.md` — cover letter and notes
2. `update_airtable_job_<slug>.py` — ready-to-run Airtable update script
3. Bid recommendation with connects analysis

## Key Files
- `.env` — Airtable credentials
- `workflow_preferences.md` — AI workflow and availability
- `ai_creative_stack.md` — Tool list
- `Portfolio_Assets/` — Curated portfolio images
- `update_airtable_job.py` — Template script
