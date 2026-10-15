# Upwork application draft — n8n Developer, Long-Term Role

Job URL: https://www.upwork.com/jobs/~022104455237122207096

## Bid decision

- **Recommendation:** Do not spend Connects at the current auction state. Revisit only if competition changes materially or the client invites Dennis.
- **Fit: 8/10.** Direct overlap with n8n, ecommerce operations, APIs, Python, LLM-assisted content, and independent workflow design. The portfolio describes two relevant systems but contains no shareable n8n JSON exports, screenshots, or production uptime evidence. JavaScript depth and long-term maintenance record are not documented.
- **Connects:** 20 required, 32 available. Applying would consume 62.5% of the current balance and leave 12. This falls in the skill's 20–40 Connect medium-risk band, which calls for fit above 9/10.
- **Competition:** 50+ proposals after about one hour; no interviews or invites in the user-provided snapshot. Bid range $10–$70, average $34.69. No boost.
- **Client:** Norway; payment verified; five 5-star reviews. Caution: 28% hire rate, $990 lifetime spend across 12 hires, $11.17 average hourly paid, and 6 open jobs. The advertised $30–$60 expert range is substantially higher than the client's payment history.
- **Rate if applying:** $36/hour, 20% above the $30 floor and near the $34.69 bid average. Agree on a paid test environment and a small initial scope before a long-term commitment.

## Relevant examples and evidence

1. **Magento 2 / Shopify product ingestion** — Portfolio describes an n8n pipeline using HTTP requests and parsers for supplier specs, LLM-assisted brand-voice descriptions, image generation, and REST API publishing to Shopify and Magento 2. This is the closest ecommerce example.
2. **ArtiMind AI content engine** — Portfolio describes an n8n pipeline for trend/concept input, AI image and video production, and publishing hooks through Blotato. This shows orchestration and AI integration, though it is less directly relevant than the catalog workflow.

Source: `Portfolio_AI_Specialist.md` and `Gem_Knowledge/GEM_03_Portfolio_Case_Studies.md`. Before submission, confirm that both systems were personally built and whether a redacted workflow export, architecture diagram, or screen recording can be shared. Do not imply JavaScript expertise or production metrics that cannot be shown.

## Proposal draft

Hi,

Your test-environment approach makes sense for an ecommerce automation role. The first thing I would establish is how your current systems exchange product, order, and content data, then build one measurable workflow in the test environment before touching production.

Two relevant workflows from my portfolio:

1. **Shopify/Magento product ingestion:** I designed an n8n workflow that collects structured supplier data through HTTP requests and parsing, uses an LLM to draft brand-aligned product content, and publishes approved product data and images through the Shopify and Magento APIs. The useful part for your business is the connection between messy source data, reviewable content, and store publishing.
2. **AI content publishing:** I built an n8n-based creative pipeline that connects research and content generation with publishing hooks. It coordinates multiple services while keeping a review step before content goes live.

I work with n8n, REST APIs, webhooks, Python, and AI integrations, and I use coding assistants to speed up debugging while checking the actual workflow output myself. For your first test, I would document inputs, authentication, expected outputs, failure paths, and handoff steps so the workflow is maintainable after launch.

I can commit up to 40 hours per week and would propose **$36/hour**. If you share the first automation you want to test, I can outline a small paid milestone in your separate environment and show the relevant workflow architecture during an Upwork call.

Best regards,  
Dennis Bui

## Before submission

- Confirm the two portfolio systems are real, personally built, and suitable to discuss or demonstrate.
- Attach a redacted n8n workflow export or diagram only if it exists and disclosure is permitted. The workspace currently has no verified export.
- Confirm JavaScript capability before answering any specific screening question about it.
- Verify the live proposal cost, client activity, and status; do not boost.
