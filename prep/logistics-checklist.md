# Joinery Logistics: Infrastructure & Payments Checklist

**Status:** STAGED / PREP
**Objective:** Finalize the "pipes" to take money and deliver course content.

---

## 1. Custom Email & Domain
**Goal:** Professional sender identity (`peter@joinerysystemworks.com` or similar) to avoid spam filters and build trust.

- [ ] **Secure Email Hosting:** 
    - *Option A (Budget):* Zoho Mail (Free tier for 1 domain).
    - *Option B (Integrated):* Google Workspace ($6/mo).
    - *Option C (Forwarding):* Cloudflare Email Routing (Free) + Gmail (send-as).
- [ ] **DNS Records:** Update SPF, DKIM, and DMARC for the custom domain to ensure Kit emails actually land in inboxes.

---

## 2. Kit (ConvertKit) Fixes
**Goal:** Automate the handoff from payment to "Here is your course."

- [ ] **Welcome Sequence:** 
    - Draft the "Thank You / Welcome" email in `prep/kit-welcome-email.md`.
    - Must include the "Secret URL" to the gated lesson pages.
- [ ] **Subscriber Tagging:** Ensure users are tagged `Foundations-Student` upon purchase.
- [ ] **Opt-in Form:** Simple "Get Updates" form for the homepage to capture the 99% who don't buy immediately.

---

## 3. Stripe Setup
**Goal:** A $299 Payment Link that works globally.

- [ ] **Create Payment Link:**
    - Title: "Joinery: Foundations for Designers"
    - Price: $299 (One-time)
    - Image: Use the Joinery logo or a "Hot Sauce" teaser.
- [ ] **Post-Purchase Redirect:** 
    - Option A: Redirect to a "Success" page on `joinery-site` that tells them to check their email.
    - Option B: Integrate with Kit via Zapier (Free tier) or Kit's native Stripe integration.

---

## 4. Gated Content Delivery (The "Low-Tech" Gate)
**Goal:** Deliver content without a $100/mo LMS (Skool/Teachable).

- [ ] **Obscure URL Path:** Move compiled lessons to `/course/foundations-for-designers-[random-hash]/`.
- [ ] **Index Page:** Create a simple navigation page for students at that URL.
- [ ] **No-Index Tag:** Add `<meta name="robots" content="noindex">` to all gated pages.

---

## 5. Next Actions (The "Hour 1" List)
1. **DNS check:** Who is your domain registrar? I can provide the specific records to add.
2. **Draft Welcome Email:** Focus on the "Secret URL" delivery first.
