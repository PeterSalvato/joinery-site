# Joinery Marketing Site — Session Governance

**Read `NORTHSTAR.md` for positioning and messaging rules.**

This file defines session-level governance for the marketing site.

## Purpose

Static HTML marketing site for Joinery school. Public-facing enrollment funnel. No backend, no authentication, no student-facing course content.

## Tech Stack

- Static HTML (no SSG, no build step)
- GitHub Pages (push to main → live in ~30 seconds via CNAME)
- CSS only (no framework)
- No JavaScript dependencies beyond scroll detection

## Deployment

```
git push to main → automatic GitHub Pages deploy
```

DNS CNAME points to GitHub Pages. Verify with `dig joineryschool.com`.

## Publishing Rules

- Push to `main` = live immediately
- No staging branch. No preview builds.
- Content is public-facing. Every change is live.
- Redirect HTTP to HTTPS (GitHub Pages default)

## Key Files and Purposes

**Public pages:**
- `index.html` — Homepage. The market signal.
- `about.html` — Founder story and credentials
- `courses.html` — Course listing and certification tiers
- `research.html` — Published research (links to DOIs)

**Course detail pages (in `/courses/`):**
- `foundations.html` — Course 01: The entry point
- `input-inversion.html` — Course 02
- `voice-governance.html` — Course 03
- `lens-extraction.html` — Course 04
- `semantic-hierarchy.html` — Course 05
- `coordinator-building.html` — Course 06

**Essays and content:**
- `copyright-submission/essay-the-wrong-question.html` — Foundational essay (no paywall, public)
- Other essays as needed

**Assets:**
- `assets/` — Logo, favicon, CSS
- `assets/diagrams/` — Mermaid diagram renders (placeholder for now)

## Content Governance

**What belongs on joinery-site:**
- Public positioning and messaging (NORTHSTAR.md)
- Course descriptions and metadata
- Founder story and credentials
- Links to published research (DOIs)
- Enrollment CTAs (email capture, Stripe links)

**What does NOT belong here:**
- Student-facing curriculum content (that's in joinery-course/)
- Internal strategy docs or planning (those go to joinery-course/docs/ or joinery/)
- Admin code or instructor tools (those go to joinery-course/platform/)
- Diagrams (removed; will be added when ready, see CLAUDE.md in joinery-course)

## NORTHSTAR.md Alignment

Every page must build the same room as the homepage:

- The founder is a practitioner-educator with 25 years of hands-on experience
- Joinery is a school, not a product
- The thesis is "preserve your voice, don't disappear into defaults"
- The audience is analog-leaning creatives who care about being themselves

Pages should:
- Lead with specificity, not abstraction
- Use real examples from practice
- Show evidence of depth (papers, credentials, teaching background)
- Avoid hype language and marketing jargon

## Key Decisions

- No marketing analytics (no Google Analytics, no pixel tracking)
- No third-party scripts except fonts (Google Fonts)
- Form submission goes to Kit (email capture tool)
- Course enrollment links point to joinery-course/platform (Stripe payments)

## Relationship to Other Repos

| Repo | Purpose | Link? |
|---|---|---|
| `joinery-course/` | Course platform + lessons | Yes (enrollment CTA) |
| `joinery/` | Skills, voice, infrastructure | No (internal only) |
| `petersalvato.com` | Personal site | Yes (founder footer) |

## Misplaced Content Notes

- `/course/` directory removed (that's curriculum, belongs in joinery-course/)
- `/prep/` directory removed (working notes, not deployment content)
- `/tools/` kept (design aids like type-pairing-playground.html are useful for content decisions)

## Session Rules

- Never add backend code or API endpoints
- Never add student authentication or enrollment logic (that's platform/)
- Never move course content or curriculum to this repo
- Never link from courses/ to merch sites or creative projects (Layer 2 boundary rule)
- Always verify links work before pushing
- Always test responsive layout (375px, 768px, 1440px viewports)

## Quick Checks Before Push

- [ ] Links to /research.html work
- [ ] Links to /about.html work
- [ ] Course pages have correct course numbers and descriptions
- [ ] Founder attribution at footer points to petersalvato.com
- [ ] Signup form action points to Kit
- [ ] Enrollment CTAs point to joinery-course
- [ ] No diagram placeholders remain
- [ ] Responsive design verified on mobile/tablet/desktop
