
# Browser Automation for Job Applications — Lessons Learned

## Claude in Chrome: General

- **Tiny viewport (~627x284):** The Chrome tab inside the Claude sidebar is very small. Coordinate-based clicks are unreliable — always prefer `ref`-based clicks from `read_page` or `find`.
- **Screenshot timeouts are common** on heavy React apps (TELUS Digital especially). Use `get_page_text` and `read_page` as primary inspection tools; only screenshot when you need visual layout info.
- **Always batch actions** with `browser_batch` — clicking, waiting, then reading in one call saves 2+ round trips per interaction.
- **`find` is the fastest way to locate buttons** — use natural language queries like "Submit & Continue" rather than parsing the full accessibility tree.
- **Wait 5-8 seconds after navigation/submission** before reading page text — React SPAs need time to render new content.

## React Form Gotchas (TELUS Digital)

- **`form_input` and DOM `.click()` don't update React state** for checkboxes. React uses synthetic events and internal state — the DOM `checked` property changes but React doesn't know about it, so submit buttons stay disabled.
- **Fix:** Find the element's `__reactProps$*` key via `Object.keys(el).find(k => k.startsWith('__reactProps'))`, then call `el[propsKey].onChange({target: {checked: true, type: 'checkbox'}})`. This triggers React's state update properly.
- **Signature canvas pads use PointerEvents, not MouseEvents.** Standard `left_click_drag` and dispatched MouseEvents don't register.
- **Fix:** Dispatch `pointerdown`, `pointermove` (multiple points), `pointerup` with `pointerId: 1`, `pointerType: 'mouse'`, `pressure: 0.5`, and `isPrimary: true`. Use `new PointerEvent(type, {bubbles: true, ...props})`.

## Exit/Navigation Dialogs

- TELUS Digital fires an "Exit Application" modal on focus/blur events in the small viewport. It blocks all interaction until dismissed. Always look for and click "Cancel" (not "Exit") when this appears unexpectedly.

## Platform-Specific Notes

### TELUS Digital (app.telusinternational.ai)
- 6-step application: Profile → Pre-screening → T&C → Document Collection → Exam → Exam
- Job list uses infinite scroll — need to scroll repeatedly to load all jobs (84/131 loaded in one session)
- Language filter search box is dangerous — typing there can accidentally trigger navigation
- Document Collection may ask for both Resume (docx/pdf/jpeg) and Certification (pdf only) — have both ready
- Exams (Steps 5-6) must be handed to the user — they test the candidate's own ability
- DOB field: use `form_input` tool, not `type` action

### Alignerr (app.alignerr.com)
- Simple Apply button click — much easier than TELUS
- Jobs are listed on /home with individual cards
- After applying, status shows "Applied" on the card
- Multiple roles available but each needs separate user approval before applying

### Appen (connect.appen.com)
- Jobs listed at /qrp/core/vendors/job_available
- Most roles are geo-restricted — check "All Countries" vs specific country lists
- Vietnam eligibility is limited

### Clickworker (workplace.clickworker.com)
- Requires complete onboarding (profile, payment method, assessments) before accessing jobs
- Can't automate the onboarding — needs user to complete it manually

### Mindrift (app.mindrift.ai)
- Mostly low-paying microtasks
- No substantial AI Trainer or prompt writer roles found

## File Upload

- **Never click file input elements** — this opens a native dialog that can't be automated. Use `file_upload` tool with the `ref` of the file input and `paths` array pointing to local files.
- TELUS accepts docx/jpeg/jpg/pdf for resume, pdf-only for certification.

## Airtable Integration

- Always `search_records` by title before creating to prevent duplicates
- Source field may not have all platforms as options — use `typecast: true` to auto-create new select options
- Use `get_table_schema` to check select field choices before writing

## Fit Scoring Framework (for consistent evaluation)
- Skill match: 30pts — how well candidate's skills align
- Experience: 20pts — relevant work history
- Vietnam eligibility: 15pts — whether the role is available in Vietnam
- Language: 15pts — English proficiency requirements met
- Qualification: 10pts — degree/certification requirements
- Compensation: 10pts — rate alignment with expectations

**Why:** These lessons came from extensive trial-and-error during a 2+ hour automation session. React internal state management and PointerEvent requirements were the biggest time sinks.

**How to apply:** Reference before any browser-based job application task. Prioritize `find` + `ref` clicks over coordinates, always batch, and use JavaScript for React form state when `form_input` fails.
