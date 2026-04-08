# Joinery Launch Workplan
**Updated:** 2026-04-07
**Budget:** $2,500 (tonight) + $2,000 (post-Lionfish)

---

## Budget Breakdown

| Item | Cost | Priority | Notes |
|---|---|---|---|
| Florida LLC (Sunbiz) | $125 | Day 1 | Required for Stripe business account |
| Trademark: Joinery | $250 | Day 2 | Class 41 (Education), TEAS Plus |
| Trademark: Accommodation Design | $250 | Day 2 | Class 41 |
| Trademark: Attunement | $250 | Day 2 | Class 41 |
| Trademark: Input Inversion | $250 | Day 2 | Class 41 |
| Trademark: Voice Governance | $250 | Day 2 | Class 41 |
| Trademark: Lens Extraction | $250 | Day 2 | Class 41 |
| Trademark: Directorial Scaffold | $250 | Day 2 | Publish essay first — see below |
| Copyright (GRUW batch 1) | $85 | Day 3 | Course materials + whitepapers |
| Google Workspace | $6/mo | Day 3 | peter@, hello@, help@ joinerysystemworks.com |
| Stripe (free) | $0 | Day 3 | 2.9% + 30¢ per transaction |
| Kit (ConvertKit) | $0 | Day 3 | Free up to 1,000 subscribers |
| **Total (initial)** | **$1,966** | | Leaves ~$534 operational runway |

---

## Phase 1: Legal Permanence (Tonight + Tomorrow)

### Tonight
- [ ] File Florida LLC at sunbiz.org
  - Entity type: Florida LLC
  - Cost: $125
  - Time: ~20 minutes
  - URL: https://dos.fl.gov/sunbiz/manage-business/efile/florida-limited-liability-company/
- [ ] Run USPTO TESS search for all 7 marks
  - URL: https://tess.uspto.gov
  - Search each term. Note any conflicts.

### Tomorrow — Day 2
- [ ] File 7 trademarks via USPTO TEAS Plus
  - URL: https://www.uspto.gov/trademarks/apply
  - Class 41: Education and training services
  - $250 per mark = $1,750 total
  - **Before filing Directorial Scaffold:** publish a short essay or whitepaper stub with a DOI (Zenodo is free). Timestamp matters.
- [ ] File copyright via USCO
  - URL: https://www.copyright.gov/registration/
  - "Group Registration of Unpublished Works" — up to 10 works, $85
  - Include: all 6 whitepapers + Foundations course syllabus + course compiled markdown files

---

## Phase 2: Operational Infrastructure (Days 3-4)

### Business Banking (after LLC confirms, 1-2 days)
- [ ] Apply for EIN (free, instant)
  - URL: https://www.irs.gov/businesses/small-businesses-self-employed/apply-for-an-employer-identification-number-ein-online
  - Have LLC name and Sunbiz confirmation number ready
- [ ] Open Mercury business bank account
  - URL: https://mercury.com
  - Requires: EIN + LLC docs (Articles of Organization from Sunbiz)
  - Free, no minimums, online only

### Email
- [ ] Set up Google Workspace ($6/mo)
  - Create: peter@joinerysystemworks.com, hello@joinerysystemworks.com, help@joinerysystemworks.com
  - Set DNS records: MX, SPF, DKIM, DMARC (Google provides exact records)
  - Forward hello@ to peter@ for now

### Stripe
- [ ] Create Stripe account at stripe.com
  - Use LLC name and EIN (from Sunbiz filing)
  - Create Payment Link:
    - Title: "Joinery: Foundations for Designers"
    - Price: $299 one-time
    - Image: Joinery logo
    - Success redirect: joinerysystemworks.com/enrolled.html (create this page)
- [ ] Create enrolled.html on the site
  - Simple page: "You're in. Check your email for access."
  - noindex meta tag

### Kit (ConvertKit)
- [ ] Update sender email to peter@joinerysystemworks.com
- [ ] Set DNS records for Kit (SPF/DKIM) so emails land in inbox
- [ ] Create welcome sequence (3 emails):
  - Email 1 (immediate): Welcome + what's coming
  - Email 2 (day 3): Link to "The Wrong Question" essay
  - Email 3 (day 7): Prompt Deconstructor PDF
- [ ] Tag: Founding-Cohort-List vs. Foundations-Student (post-purchase)
- [ ] Connect Stripe → Kit via native integration or Zapier free tier

### Prompt Deconstructor PDF
- [ ] Build as single-page PDF
  - Source material: prep/prompt-deconstructor.md
  - One page, Joinery visual language, downloadable
  - Gate it behind the Kit form on the homepage

---

## Phase 3: Outreach (Days 3-5, after infrastructure is live)

**Do not reach out until Stripe is live and email is on custom domain.**

### Victore
- [ ] Send: "James — still want to connect whenever works for you."
- Short. No pitch. Stay warm.

### Adam Wahler
- [ ] Send: "I've been building something for three years that connects directly to what you taught me about craft and production rigor. Would you look at it before I launch?"
- If he engages: send the site + the one-paragraph description

### SVA Alumni Affairs
- [ ] Call: 212.592.2300
- Script: "I'm an SVA alum, I studied under James Victore, I've spent three years publishing peer-reviewed research on AI methodology for designers and just launched a school based on it. I wanted to see if this is something SVANow covers."
- Follow up with email to alumni@sva.edu if they ask

### Design Press
- [ ] Find editorial contact at Eye on Design (AIGA)
- [ ] Find editorial contact at It's Nice That
- [ ] Send one-paragraph pitch to both:
  - "SVA-trained designer spends three years publishing peer-reviewed research on why AI makes everything look the same, launches school to fix it. Six whitepapers with DOIs. First research-backed methodology for creative AI methodology. Happy to send more."

---

## Phase 4: Content (This Week, Parallel to Above)

### Directorial Scaffold — Whitepaper 7 (Thursday, tokens reset)
- [ ] Step-through extraction session with Claude (same process as other 6 papers)
- [ ] Concept: coordination layer that interviews the human to extract judgment, bridges decomposition outputs into synthesis, keeps the CD in the room at the decision point
- [ ] Publish to Zenodo for DOI
- [ ] Add to research page on site
- [ ] Trademark already filed Day 2 — DOI is supporting evidence

### 90-second video
- [ ] Record screen walkthrough of Roughing It comparison
  - Compound prompt → output
  - Decomposed specialists → outputs
  - Your synthesis → the difference
- [ ] Post to LinkedIn, embed on Foundations page

### The Wrong Question essay
- [ ] Pitch to design newsletters as a guest post / syndication
- [ ] Share on LinkedIn as a post (pull one striking passage, link to full essay)

---

## One-Paragraph Outreach Description (Ready to Send)

"I spent three years figuring out why AI makes everything look the same. The problem turned out to be structural — the way most people use AI forces the model toward consensus, and consensus is the death of distinctiveness in creative work. I documented the fix across six peer-reviewed whitepapers and just launched a school to teach it. The methodology comes from special education pedagogy — the same framework that makes accommodating a student's processing reality federal law. Applied to AI, it keeps your judgment in the room and your voice in the work. It's called Joinery. joinerysystemworks.com"

---

## Phase 5: Thursday (Tokens Reset)

### Directorial Scaffold — Whitepaper 7
- [ ] Step-through extraction session with Claude (same process as other 6 papers)
- [ ] Concept: the coordination layer that interviews the human to extract judgment, bridges decomposition outputs into synthesis, keeps the CD in the room at the decision point
- [ ] Publish to Zenodo for DOI
- [ ] Add to research page on site
- [ ] File trademark immediately after DOI confirmed

---

## Success Metrics (End of Week 1)
- [ ] LLC filed and confirmed
- [ ] 7 trademarks filed
- [ ] Copyright filed
- [ ] Stripe live with $299 payment link
- [ ] Email on custom domain
- [ ] Kit welcome sequence active
- [ ] Victore, Wahler, SVA contacted
- [ ] Design press pitched
- [ ] Directorial Scaffold essay published with DOI
