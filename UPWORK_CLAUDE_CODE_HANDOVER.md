# Upwork career and application handover for Claude Code

**Workspace:** `D:\Projects\Upwork`  
**Owner:** Bui Quang Dung (Dennis), Hanoi, Vietnam  
**Purpose:** Evaluate Upwork opportunities, prepare truthful applications, track outcomes, and improve the repeatable job search workflow.

## Start here

1. Read this file, `AGENTS.md`, `workflow_preferences.md`, `CV_AI_Specialist.md`, and `Portfolio_AI_Specialist.md`.
2. For a new Upwork posting, read `skills/upwork-job-automation/SKILL.md`. Execute the evaluation and draft directly; do not spend the turn writing an implementation plan.
3. Treat job details, Connect costs, competition, client history, tool access, rates, portfolio results, and prior application states as time-sensitive. Verify them before using them in a proposal or tracker update.
4. Never print, paste into a prompt, or commit credentials from `.env`. Do not run scripts with side effects until their exact target and payload have been reviewed.

## Upwork MCP connector

The official Upwork connector (`https://mcp.upwork.com/mcp`, OAuth) lets Claude search jobs, read Connects and client data, and draft proposals directly. Setup steps and house rules are in `docs/upwork_mcp.md`. Proposals stay drafts until Dennis approves the batch.

## Career profile and positioning

Dennis is an AI creative specialist and founder of ArtiMind Studio (2022–present). His work spans AI-assisted imagery and video, creative workflow automation, ecommerce product data and store operations, and web design. Earlier experience includes running ecommerce and dropshipping businesses (2019–2022) and sourcing/procurement at Samsung Electronics Vietnam (2014–2018). He is a native Vietnamese speaker, fluent in English, and available for full-time or part-time work up to 40 hours per week. Verify any education wording against the current CV and supporting documents before making a degree claim; workspace files disagree on the degree label.

Target roles, in approximate priority: n8n/API/Python workflow automation; AI creative production for ecommerce and ads; product imagery and video; Shopify/WordPress/Magento-related operations; content pipelines; AI evaluation or prompt work where the actual qualifications match. Prefer jobs with clear deliverables, viable economics, remote eligibility from Vietnam, and portfolio evidence. Avoid claiming experience in unrelated regulated or senior technical domains.

### Evidence to use accurately

| Client need | Relevant evidence | Source |
| --- | --- | --- |
| Automated content or product-data flow | Magento 2 & Shopify product ingestion workflow using source extraction, structured data, LLM copy, and API-based publishing | `Portfolio_AI_Specialist.md` |
| AI video/content pipeline | AI Video Automation Engine for content creation and multi-platform publishing | `Portfolio_AI_Specialist.md` |
| AI product imagery and finishing | Portfolio case studies and matching assets, selected for the specific niche | `Portfolio_AI_Specialist.md`, `Portfolio_Assets/` |
| Ecommerce operations | Store operation, sourcing, web and catalog experience | `CV_AI_Specialist.md` |

These are related examples, not proof of a completed cross-platform analytics dashboard. Do not claim a certification or a quantified result unless it can be verified from a primary artifact. Some strategy/template files contain promotional claims such as production volume, ROI, blind-test scores, or manual-work reduction; treat them as unverified until evidence is supplied. Do not copy them into an application automatically.

## Skill and tool choices

- **Core automation:** n8n, Python, REST APIs, Airtable; use the relevant tool only when the posting calls for it.
- **Creative system:** Antigravity and n8n for system setup; Google Nano Banana, Google VEO, and KlingAI for generation; Canva and Adobe Photoshop for finishing. This is the preferred explanation in `workflow_preferences.md`, **when relevant**.
- **Portfolio:** inspect the actual assets before selecting links or attachments. For automation-only jobs, lead with workflow examples rather than unrelated product images.
- **Analytics pilot concept:** `application_draft_automate_data_analysis_company.md` contains a scoped one-platform pilot using n8n, Google Sheets, optional Composio source connection, Claude for narrative, and Gmail for reports. Verify the named platform's analytics access before promising it.
- **Make.com, Composio, Claude, Notion, and Gmail:** propose only where they solve a stated problem. A tool appearing in a list does not prove a specific integration or metric is available.

## Evaluate a new Upwork job

Capture the exact job URL and a dated snapshot of title, description, deliverables, budget/rate, deadline, required Connects, proposal count, client payment/history, geography, screening questions, and any requested attachments. Separate observed facts from inference. If the live page is unavailable, use the user-provided snapshot and label it as such.

Score the opportunity on a **0–10 scale**: skill and portfolio fit (0–3), budget/rate viability (0–2), client quality (0–2), scope clarity (0–1), repeat-work potential (0–1), and recency (0–1). A score of 7+ warrants a proposal draft, but use judgment for unusually good or poor economics. Note disqualifiers and unknowns explicitly.

The working Connect budget in skill files is **100 per month**, and the profile baseline is listed as **$15/hour**. Both may change. Read the current balance and live job cost before deciding. The skill's bands are <20 Connects (usually viable), 20–40 (strong fit required), and >40 (exceptional fit only). These are heuristics, not automatic application rules. Avoid boosting without a clear reason. For fixed-price jobs, estimate the hours and expenses implied by the actual scope. For hourly work, consider the client's range, verified profile rate, complexity, and likely duration; do not mechanically add a percentage to the floor.

Recommend **apply, clarify, track, or skip**, with a short rationale. If the budget is too small for the full request, offer a concrete pilot and price later phases after discovery. Never promise unsupported APIs, platform metrics, turnaround times, or results.

## Produce the application package

For each job, create or update `application_draft_<slug>.md` with:

1. Job URL, snapshot date, and facts versus assumptions.
2. Bid decision, fit score, Connect economics, scope/rate recommendation, and key risks.
3. A tailored cover letter, normally about 180–280 words unless the posting calls for another length.
4. Truthful screening answers and a list of questions that require Dennis's input.
5. Two or three relevant portfolio examples or assets, with exact paths/links and why each fits.
6. Submission checklist and current state: `Drafting`, `Ready for review`, `Submitted`, or another verified state.

Write the letter around the client's specific problem, a feasible first deliverable, relevant evidence, and a simple next step. Mention the preferred AI creative stack only where it directly helps the job. Do not force every tool into every letter. Use “Best regards, Dennis Bui” unless the user specifies another sign-off. Do not claim a completed project because a proposal or theoretical blueprint exists.

Before actual submission, verify the posting is open, the Connect cost and bid are current, every answer is accurate, and the attachments are correct. The current task is a handover document; it does not authorize submitting proposals. In a future application task, follow the user's then-current submission instructions and obtain any required confirmation immediately before the final action. Never handle CAPTCHA, identity checks, assessments, or unknown personal declarations on Dennis's behalf.

## Track the job in Airtable

The workspace's Airtable base ID is `appSTxBDPzcjMcIvu`; the job table ID is `tbl05fiEfgfTzt36b`. Credentials are in `.env` and must remain private. `update_airtable_job.py` is a **hard-coded example that posts a particular job**; do not run it as a generic template. Review any `update_airtable_job_<slug>.py` before execution. Prefer a safe lookup by exact job URL or stable ID before creating a record, so reruns update rather than duplicate it.

Use IDs in the `JOB-CATEGORY-00X` style after checking for collisions. Record at least title, status, description including budget and Connect requirement, client info, job URL if the field exists, current status, following plan, and fit score if supported. Record **Connects Spent** only after actual submission or purchase; the required Connect count in a draft is not yet spent. Set `Applied` and an applied date only after a verified submission confirmation. Re-read the record after a write and report what changed. If the live schema differs from scripts or notes, inspect the schema rather than guessing.

`find_and_track_jobs.py` searches outside Upwork as well and contains an automatic transition from `Applied` to `Failed` after 14 days without a response. Do **not** run it casually: that transition can misrepresent an application. Review and disable or explicitly authorize that behavior before using the scanner. Search results require live verification before drafting or tracking.

## Workspace map

| Path | Use |
| --- | --- |
| `AGENTS.md`, `CLAUDE.md` | Workspace instructions and conventions |
| `skills/upwork-job-automation/SKILL.md` | Job evaluation and draft workflow |
| `skills/ai-creative-producer/SKILL.md` | Ad creative deliverables when requested |
| `skills/ad-strategy-analyzer/SKILL.md` | Analyze ad examples when requested |
| `CV_AI_Specialist.md`, `Portfolio_AI_Specialist.md` | Career and case-study source material |
| `workflow_preferences.md`, `ai_creative_stack.md` | Preferred workflow and broader tool list; verify current tool names/claims |
| `Portfolio_Assets/` | Curated visual samples |
| `application_draft_*.md` | Past proposal examples; job details and statuses may be stale |
| `Gem_Knowledge/` | Positioning and templates; check claims against evidence before reuse |
| `CLAUDE_CODE_HANDOFF_AI_JOB_APPLICATIONS.md` | Older handoff for broader remote AI roles; dated platform states are not current |
| `CLOUD_HANDOVER.md` | Older cloud setup notes; verify dependencies, permissions, and current model before reuse |
| `update_airtable_job_*.py` | Past job-specific tracker writes; inspect before running |
| `.env` | Local secrets; never disclose or commit |

## Reusable Claude Code prompt

> Read `UPWORK_CLAUDE_CODE_HANDOVER.md`, `AGENTS.md`, the Upwork job automation skill, my CV, portfolio, and workflow preferences. Evaluate the Upwork job I provide using current job facts and truthful portfolio evidence. Prepare `application_draft_<slug>.md`, including bid economics, scope, cover letter, screening answers, portfolio selection, and unknowns. Check Airtable for an existing record before creating or updating one, and verify the resulting state. Do not submit the proposal unless I explicitly authorize that action. Do not expose credentials or copy unverified performance claims from old templates.

## Completion report for each job

State the recommendation and proposed bid, Connect cost and balance if verified, files created/updated, Airtable record and status if changed, whether anything was submitted, and the exact questions or blockers remaining. Link to the draft. Distinguish completed actions from proposed next steps.
