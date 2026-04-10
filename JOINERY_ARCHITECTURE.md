# Joinery — Three-Repo Architecture

**Date:** 2026-04-10

This document describes how the three Joinery repositories work together to form a complete school system.

---

## The Three Repos

### 1. joinery-site (Public Marketing)

**URL:** joineryschool.com  
**Repo:** https://github.com/PeterSalvato/joinery-site  
**Directory:** `projects/active/joinery-site/`

**Tech:** Static HTML, GitHub Pages, no build step

**Purpose:** Public-facing enrollment funnel. Copy, course descriptions, founder story, signup CTAs.

**Key Pages:**
- `index.html` — Homepage (market positioning)
- `about.html` — Founder credentials and story
- `courses.html` — Course listing and certification tiers
- `research.html` — Links to published research (6 papers with DOIs)
- `courses/*.html` — Individual course detail pages (Foundations, Input Inversion, Voice Governance, etc.)

**Deployment:**
- Push to `main` → GitHub Pages live in ~30 seconds
- DNS CNAME points to GitHub Pages
- No staging, no preview builds

**Governance:**
- Purely public. Every change is immediately live.
- Read `NORTHSTAR.md` for positioning and messaging
- Read `CLAUDE.md` for session rules

**Content:**
- Who: Analog-leaning creatives (illustrators, designers, authors, copywriters, CDs)
- What: A school for creatives using AI who don't want to disappear into defaults
- Why: Attunement (apply your existing skill to a new receiving system) + Accommodation Design (structure for AI tools)

---

### 2. joinery-course (Private Delivery)

**Repo:** https://github.com/PeterSalvato/joinery-course  
**Directory:** `projects/active/joinery-course/`

**Tech (dual-layer):**
- **Lessons:** Static HTML (compiled from markdown)
- **Platform:** Flask 2.3.3, SQLAlchemy, Stripe, Docker

**Purpose:** Private student-facing course delivery. Two separate functions in one repo.

#### Layer 1: lessons/

- 3 modules (Task Decomposition, Input Inversion, Voice Governance)
- 18 lesson files (HTML, compiled from markdown via `build-lessons.py`)
- Watermarked, `noindex` meta tag, read-only for students
- Static assets (CSS, logo, favicon, JavaScript for scroll detection)
- Lessons are curriculum content, not interactive

#### Layer 2: platform/

- Flask application managing enrollment, progress, forums, capstones, certificates
- 8 SQLAlchemy models: User, Course, Lesson, Enrollment, Purchase, ForumPost, Capstone, LessonCompleted
- Stripe payment webhook integration
- Admin dashboard for instructor management
- Student dashboard showing enrolled courses, lesson progress, capstone status
- Forum for office hours discussion
- Capstone submission and evaluation
- Auto-issued digital certificates (PDF generation)
- Comprehensive test suite (100+ test cases, pytest)
- Production-ready Docker setup (Gunicorn + PostgreSQL)

**Enrollment Flow:**

```
Prospect → joinery-site/index.html
   ↓
Read about Joinery (courses, founder, research)
   ↓
Click "Enroll" → Stripe Checkout
   ↓
Pay $299 (Foundations) or $2,499 (full ladder)
   ↓
Stripe webhook → platform/stripe_handler.py
   ↓
Platform creates User + Enrollment records
   ↓
Redirect to platform/signup.html (password setup)
   ↓
Student logs in → Dashboard
   ↓
Can now access lessons/ (watermarked HTML)
   ↓
Complete modules → Submit capstone → Get certificate
```

**Development:**

```bash
cd joinery-course/platform
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
make dev        # Runs Flask on localhost:5000
make test       # Runs pytest
```

**Production:**

```bash
docker-compose -f docker-compose.prod.yml up -d
# Runs Gunicorn + PostgreSQL
# Port 8000 (behind reverse proxy)
```

**Governance:**
- Read `ARCHITECTURE.md` for dual-layer rationale
- Read `CLAUDE.md` for session rules
- Read `platform/docs/BUILD_COMPLETE.md` for complete platform documentation

---

### 3. joinery (Central Infrastructure)

**Repo:** https://github.com/PeterSalvato/joinery  
**Directory:** `projects/active/joinery/`

**Tech:** Claude Code skills, voice protocols, agent configurations, automation

**Purpose:** Reusable infrastructure shared across the constellation projects.

**What's Inside:**

- **90+ Claude Code skills** — Audit, copy, design, brand analysis, texture, press tools, etc.
- **Voice protocols** — Master voice protocol (enforced globally), role-specific profiles
- **Agent configurations** — Two-tier system (consultation agents, execution agents)
- **Automation tools** — Workflow scripts, session continuity hooks
- **Templates** — Skill templates, agent templates, session handoff templates
- **Workflow transcripts** — Ideation history, research outputs, session logs

**Skill Families:**

- **Audit suite** — Capture, baseline, lens, synthesize (complete audit coordinator)
- **Brand reading** — Structural brand analysis using 8-lens framework
- **EI skills** — Author/artist/philosopher extraction from essays (Victore, Bukowski, Pirsig, Sennett, Fowler, Millman, Chimero, Bierut)
- **Design tools** — Copy, design-pass, texture system, pressure, front-end-design
- **Support skills** — Voice-sample, baseline, service-health, repo-hygiene, sensitivity-check
- **Homelab skills** — Service health checks, backup verification, storage management, VPN, container monitoring

**Governance:**
- Central source of truth for voice protocols (master version enforced globally)
- All skills committed to git with clear versioning
- Symlinked to `~/.claude/skills/` for system access
- Read `CLAUDE.md` for repo purpose and structure
- Read `MANIFEST.md` for skill dependency map

---

## How They Work Together

```
┌──────────────────────────────────────────────────────────────┐
│                    joinery-site (Public)                      │
│                  Static HTML Marketing                        │
│  index.html | about.html | courses/*.html | research.html   │
│                                                                │
│         ↓ Enrollment CTA links to joinery-course ↓           │
└────────────────────┬─────────────────────────────────────────┘
                     │
        Stripe Payment (webhook)
                     │
                     ↓
┌──────────────────────────────────────────────────────────────┐
│                 joinery-course (Private)                      │
│              LAYER 1: Static Lessons                         │
│        (module-1, module-2, module-3 HTML files)             │
│       Watermarked, noindex, read-only for students           │
│                                                                │
│              LAYER 2: Flask Platform                         │
│    (User, Enrollment, Forum, Capstone, Certificates)         │
│     Stripe integration, admin dashboard, tests               │
│                                                                │
│  ↓ Uses voice/protocols from joinery ↓                       │
└────────────┬──────────────────────────┬──────────────────────┘
             │                          │
             └──────────┬───────────────┘
                        │
                        ↓
        ┌──────────────────────────────┐
        │   joinery (Infrastructure)   │
        │  Skills | Voice | Agents     │
        │   Symlinked to ~/.claude/    │
        └──────────────────────────────┘
```

---

## Key Decisions

### Why joinery-site is separate
- Public content changes frequently (enrollment dates, course descriptions, marketing messaging)
- No backend code
- Deploys instantly (GitHub Pages)
- Can be managed independently of course platform

### Why joinery-course is dual-layer (not lessons + separate platform)
- Lessons and platform serve the same purpose: private student delivery
- Single source of truth for enrollment and course relationships
- Reduces deployment complexity (two components, one repo)
- Student payload is small (18 lessons, ~50KB total)
- Backup and versioning are unified

### Why joinery is separate
- Skills and voice protocols are used across other projects (petersalvato.com, consulting sites, etc.)
- Central place to maintain voice consistency across the constellation
- Easier to symlink and manage from `~/.claude/skills/`
- Clear governance separation between infrastructure and product

---

## Technology Stack Summary

| Layer | Purpose | Tech | Location |
|---|---|---|---|
| joinery-site | Public enrollment funnel | Static HTML, GitHub Pages | `joinery-site/` |
| joinery-course/lessons | Curriculum delivery | Static HTML, Markdown source | `joinery-course/lessons/` |
| joinery-course/platform | LMS & enrollment mgmt | Flask, SQLAlchemy, Stripe | `joinery-course/platform/` |
| joinery | Infrastructure (shared) | Skills, voice, agents | `joinery/` |

---

## Database & State

- **joinery-site:** No database. Static files only.
- **joinery-course/lessons:** No database. Static HTML files.
- **joinery-course/platform:** SQLite (dev) / PostgreSQL (prod). 8 models.
- **joinery:** No database. File-based (skills, voice definitions, agent configs).

---

## Deployment Checklist

### joinery-site
- [ ] Push to main → live in 30 seconds
- [ ] CNAME points to GitHub Pages
- [ ] All links work (no 404s)
- [ ] Responsive design verified

### joinery-course
- [ ] Platform tests pass (`make test`)
- [ ] Stripe webhook configured for production domain
- [ ] Database migrations applied
- [ ] Lessons compiled and assets correct
- [ ] Admin dashboard loads
- [ ] Full enrollment flow tested (signup → lesson access → capstone → cert)

### joinery
- [ ] All skills committed to git
- [ ] Skills symlinked to `~/.claude/skills/`
- [ ] Voice protocol updated in global CLAUDE.md if changed
- [ ] No uncommitted changes

---

## References

- **joinery-site/NORTHSTAR.md** — Positioning and messaging rules
- **joinery-site/CLAUDE.md** — Marketing site session governance
- **joinery-course/ARCHITECTURE.md** — Dual-layer rationale
- **joinery-course/CLAUDE.md** — Platform session governance
- **joinery-course/platform/BUILD_COMPLETE.md** — 950 lines of platform documentation
- **joinery-course/platform/docs/DEPLOYMENT.md** — Production setup
- **joinery/CLAUDE.md** — Infrastructure repo governance
- **joinery/MANIFEST.md** — Skill dependency map

---

## Contact

All three repos are maintained by Peter Salvato. Questions? See individual CLAUDE.md files for session-specific governance.
