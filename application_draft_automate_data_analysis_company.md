# Upwork application draft — Automate Data Analysis for Company

Job URL: https://www.upwork.com/jobs/~022103567401517800431

## Bid decision

- **Recommendation:** Apply with a tightly scoped $150 pilot; do not promise a complete multi-platform analytics system for that price.
- **Fit: 7.5/10.** Good overlap with n8n, APIs, content-platform workflows, data organization, and practical reporting. The workspace shows adjacent automation projects, but not a documented end-to-end cross-platform analytics dashboard or certification.
- **Connects:** 13 required, 32 available. Cost is 40.6% of the current balance and 13% of the 100-Connect monthly budget; 19 would remain. Below the skill's 20-Connect low-risk threshold. Do not boost.
- **Competition:** 10–15 proposals, no interviews, one hire on the job; bid range $140–$150, average $149.23 in the user-provided snapshot.
- **Client:** Payment and phone verified; new small education company in India. Two jobs posted, one hire, $150 spent, no reviews yet. Limited history, though the first hire is a positive sign.
- **Bid:** $150 fixed for a first platform plus a Google Sheets reporting template, data refresh workflow, and handoff. Additional platforms, API setup costs, and deeper analysis should be priced after the platform list and metric definitions are known.

## Proposed pilot workflow

At a fixed weekly time, n8n reads one authorized platform account through a verified Composio read action or the platform's approved API/export. It normalizes and checks the records, removes duplicates, and writes raw rows and a run log to Google Sheets. n8n calculates weekly totals and changes. Claude drafts a short explanation using those verified figures; n8n checks every figure before Gmail sends the report. A source failure triggers a clear alert. If Claude is unavailable, the system sends a figures-only report and flags the missing narrative.

Before promising a connector, verify the named platform's available analytics actions, metric definitions, reporting grain, history, and pagination. Notion is optional for a readable handoff, not required for the $150 pilot.

## Cover letter

Hi,

You need a weekly view of content performance that runs reliably and makes missed data obvious. I would start with one platform and a few agreed metrics, then expand only after the first report reconciles with the source.

I have built related n8n workflows for ecommerce data ingestion and content publishing. For your pilot, n8n would run at a fixed time, pull data from one approved source, validate and deduplicate it, and record both the data and each run in Google Sheets. It would calculate the weekly totals; Claude would turn those verified numbers into a short, readable summary. A final check would match every reported figure to the sheet before Gmail sends it. If a source fails, you would receive an alert rather than a misleading report.

For **$150**, I propose one platform, one account, a few confirmed KPIs, one weekly email, and a concise handoff within your one-month timeline. I can use Composio if its authorized connection exposes the needed analytics; otherwise I would check the platform's approved API or export before committing to the integration.

Which platform should we pilot, what three to five metrics matter most, and can you share the YouTube example you liked?

Best regards,  
Dennis Bui

## Screening answer — recent similar experience

My recent automation work includes an n8n-based ecommerce workflow that collects and structures supplier product data, prepares brand-aligned content with an LLM, and sends approved records to Shopify and Magento through their APIs. I have also built a content workflow that coordinates AI production and publishing across social platforms. Those projects involved connecting sources, transforming data, and checking outputs—skills directly relevant to your reporting system. For your project, I would start with one platform, validate its metrics against the source, then schedule a Google Sheets report with a run log and failure alert. I can show the related workflow architecture during an Upwork call.

## Screening answer — certifications

I do not currently list a certification specifically for n8n, Make.com, Google Sheets, or data analytics. My relevant qualification is hands-on work building n8n, API, and Python workflows, which I can explain and demonstrate.

## Portfolio selection and checks

- Use the **Magento 2 & Shopify Product Ingestion Workflow** and **AI Video Automation Engine** sections of `Portfolio_AI_Specialist.md` as related workflow examples. Neither is an analytics dashboard; describe them accurately.
- Do not attach product imagery; it does not demonstrate data analysis.
- Confirm the target platforms, API/export availability, account access, refresh frequency, KPI definitions, and expected charts before committing to the full scope.
- Verify the first platform's Composio read actions, reporting grain, history, and pagination before selecting that connector. Keep Claude's narrative separate from n8n's calculations.
- Verify that the job is still open and the live Connect cost before submission. No proposal has been sent from this draft.
