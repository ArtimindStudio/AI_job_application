# Upwork scan & Connects playbook

Last updated: 2026-10-15. Used by the scheduled "Upwork fresh-job scan" task and by any session that applies to Upwork jobs.

## Why
- Upwork reports a 90% rise in generative-AI contract starts while earnings per contract fell 13%. Simple AI work ("make images") fell 28%; complex AI work rose 45%.
- On 2026-10-15, AI image/video jobs had fewer than 5 to 10 proposals when 1-2 hours old, and 20-50 a day later. Speed beats boosting.
- Dennis's sample: of 14 closed proposals, 11 were boosted (13-63 Connects) and only 3 were opened. Both recent hires came within about a day of posting.

## Scan routine
1. `get_freelancer_dashboard check` for invitations (0 Connects), offers and messages that need a reply.
2. `find_jobs smart_search` with `mode=most_recent`, `days_posted=1`, plus `find_jobs search` on these titles with `sort=recency`: "AI video", "AI image", "AI product", "AI UGC", "product photography", "AI ads", "jewelry", "n8n content".
3. Drop jobs with `applied=true` and jobs already in Airtable (match on Job URL).
4. Run the gates, then score. Call `find_jobs get` only on survivors, to get connects_cost, client_record and jobActivity.

## Hard gates (fail one = skip)
| Gate | Rule |
|---|---|
| Freshness | Posted 3 hours ago or less, OR proposals tier "Fewer than 5" / "5 to 10" |
| Saturation | Skip "20 to 50" and "50+". Skip if totalInvitedToInterview >= 3 or totalHired >= 1 |
| Client | Payment verified. If they have hired before: hire rate >= 50% and feedback >= 4.5. New clients: only with a clear paid test and a defined scope |
| Pay | >= $8/hr, or a fixed price that works out to >= $8/hr for the real scope (changed 2026-10-17 at Dennis's request; was $15). Still skip "$3 per task" micro-gigs and anything under $8/hr |
| Fit | Product-accurate imagery or video (jewellery, fashion, accessories, cosmetics, home goods), AI UGC/ad video, or an AI content pipeline (n8n + generation). Skip engineering builds (Next.js, RAG, full-stack), on-camera "real person" UGC, Chinese/Italian/Dutch/French language roles, in-person roles and NSFW |
| Location | No country restriction that excludes Vietnam |
| Safety | No fees, no off-platform payment, no ID requested before a contract |

## Score (0-10) for jobs that pass every gate
- Fit with portfolio evidence: 0-3 (3 = jewellery/fashion/product accuracy, with a matching portfolio project)
- Freshness/competition: 0-2 (2 = fewer than 5 proposals)
- Client quality: 0-2 (spend >= $10k and hire rate >= 70% = 2)
- Pay: 0-2 (>= $20/hr or a long-term retainer = 2; $12-19/hr = 1; $8-11/hr = 0)
- Repeat potential: 0-1 ("ongoing", "long-term", "30+ hrs/week")

8+ = apply now. 7 = apply if Connects allow. Below 7 = list only.

## Connects strategy (about 5 bids a week, about 80 Connects)
- Budget: buy 100 Connects ($15) at a time. Keep a reserve of 20.
- Invitations cost 0 Connects. Always evaluate them first.
- Never boost by default. Boost only when the score is 9+, the job is under 2 hours old, and the 4th paid slot costs 15 Connects or less. Bid the minimum that takes a slot.
- Skip any job whose connects_cost is above 20 unless it scores 9+.
- Cost per bid target: 15 Connects or less (about $2.25).
- Under-$15/hr jobs: apply only if they are long-term (more than 1 month), and quote at least $12/hr. Use them to build reviews, not as the main pipeline.
- Review every 30 days: Connects spent, proposals opened by the client, interviews, hires, revenue. Continue if there is at least 1 hire per 100 Connects; otherwise pause and shift time to Mercor or AI-training platforms.

## Output of each scan
- An email to Dennis (only if something passes the gates, or if an invitation, offer or message needs him):
  - for each job: title, link, age, proposal tier, client stats, pay, Connects cost, score, why it fits, which portfolio projects to attach, and a 120-180 word cover-letter draft;
  - the Connects balance;
  - the invitations, offers and messages waiting for him.
- For jobs scoring 7+: an Airtable record (Status Drafting, Source Upwork, the Connects field set to the cost, ID JOB-<CATEGORY>-<YYMM>-<NN>, duplicate check on Job URL first).
- Never submit a proposal, spend Connects or send a client message without Dennis's approval in chat.
