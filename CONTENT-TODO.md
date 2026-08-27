# Pre-launch checklist

Every item marked in gold on the site (`<span class="todo">`) is a placeholder that must be
replaced with a **verified** fact before publication. They are styled to be impossible to miss
in a browser, so nothing ships by accident.

```bash
grep -rn 'class="todo"' --include='*.html' .
```

Placeholders live in the generator, not the generated HTML. Edit `tools/layout.py` (company
facts, nav, footer) or the relevant `tools/content_*.py` module, then re-run
`python3 tools/generate.py`.

**Content source of truth:** everything on this site derives from two documents in
`Context from Lekan/` — the profile deck (`pinnacle_precision_defense_profile.pptx`) and the
phased pitch (`Pitch on 3 phases.pdf`). Do not add capabilities that are not in those documents.

---

## 1. Already resolved from the profile deck

These no longer need chasing — they came from slide 10 and are live on the site:

- Legal name: Pinnacle Precision Engineering & Consulting Limited
- Headquarters: Abuja, Nigeria
- `info@pinnaclepec.com`, `enquiries@pinnaclepec.com`
- `+1 (662) 497-9481`
- Site domain set to `pinnaclepec.com` (`SITE_URL` in `tools/layout.py`)

## 2. Corporate identity — still blocking

| Item | Where | Notes |
|---|---|---|
| CAC registration (RC) number | footer (every page), `about/index.html`, legal pages | From the certificate of incorporation. |
| Date of incorporation | `about/index.html` | |
| Registered office street address | footer, `about/index.html`, `contact/index.html`, legal pages | Must match the CAC record. |
| Nigerian phone line | `contact/index.html`, footer | The deck's number is a **US** number against an Abuja HQ. It works, but a Nigerian line reads far better to a Nigerian military buyer and removes an obvious question. |
| Confidential reporting channel | `about/integrity-and-compliance.html`, `legal/anti-corruption-policy.html` | Currently routed to general enquiries. A separate address that does **not** reach delivery staff is the point of the control. |

## 3. Credentials — the highest-value items on this list

For an engineering and construction firm bidding defence work, these get requested first.
Publishing them is a competitive advantage; claiming them without holding them is fatal.
Listed with placeholders on `about/leadership.html`:

- [ ] **COREN registration** — for the firm and each named engineer. Directly checkable.
- [ ] **BPP contractor registration** — Bureau of Public Procurement registration and category.
      Effectively a prerequisite for federal work.
- [ ] **Professional indemnity insurance** — cover level and insurer.
- [ ] **ISO 9001** quality management, or a stated timeline to certification.
- [ ] **Health and safety record** — safety management system and incident history.
- [ ] **Project references** — completed civil/engineering projects, with client permission to cite.

The deck claims "15+ years of combined founding-team experience." That is on the site as written.
Be ready to substantiate it by naming the projects if asked.

## 4. Leadership — blocking

`about/leadership.html` is a **structural placeholder**. Do not publish named biographies until:

- [ ] The individual has confirmed their appointment in writing.
- [ ] They have read and approved their own biography text.
- [ ] Every qualification, professional registration and project claim is verified against
      documentation.

## 5. Claims discipline — keep these

The deck's own disclaimers are good practice and are carried through the site. **Do not remove
them** until the underlying facts change:

- "These are proposed defence applications for discussion purposes and do not represent claims
  of completed Nigerian Army contracts." — homepage, every sector page, every capability page.
- "Illustrative target: disciplined vendor qualification and inventory practices are designed to
  shorten lead times and reduce stock-outs. Actual results depend on scope and baseline
  conditions." — `capabilities/defence-supply-chain.html`.
- "Illustrative example" framing on the predictive-maintenance bearing-degradation example.
- "All work proceeds within the formal procurement, governance, security and confidentiality
  requirements set by the client."

No client is named anywhere, by design. Before any client reference appears: written permission,
confidentiality review, internal sign-off.

## 6. Scope statement — verify it still matches the business

The site states plainly that the firm supplies **non-weaponized** categories only, and does not
supply, broker or finance weapons, ammunition or ordnance. This is taken directly from both
source documents, which describe non-weaponized scope as a deliberate value proposition
("reduces procurement complexity").

It appears on the homepage scope section, `about/index.html`, and commitments 01 and 06 of
`about/integrity-and-compliance.html`.

- [ ] Confirm this is still accurate. **If the business intends to supply weapons or ordnance,
      these sections must be rewritten before launch and the licensing position stated** —
      end-user certification and the relevant Nigerian approvals become the centre of the site's
      credibility at that point.

## 7. Legal documents — require Nigerian counsel

All three carry a "draft requiring legal review" banner. Do not remove it until counsel signs off.

- [ ] `legal/privacy-policy.html` — check against the **Nigeria Data Protection Act**. Needs real
      answers on: what the live site collects, lawful basis per purpose, cookie/analytics
      inventory, processor list, retention periods, international transfer safeguards.
- [ ] `legal/terms-of-use.html` — limitation of liability and jurisdiction clauses deliberately
      left blank rather than filled with generic wording.
- [ ] `legal/anti-corruption-policy.html` — confirm applicable statutes, set the gift/hospitality
      threshold, name the financial approval thresholds, set training frequency and board review
      cycle.

Still to be drafted (referenced from the integrity page):

- [ ] Quality management policy
- [ ] Health and safety policy
- [ ] Conflict of interest policy
- [ ] Whistleblowing policy

## 8. Insights — do not fake it

`insights/index.html` lists five briefings as an **editorial pipeline**, with a visible notice
saying so. Nothing is written yet.

- [ ] Write at least two properly before launch — with no public client list, this is the
      strongest credibility signal available.
- [ ] Confidentiality and factual review before each publication.
- [ ] Remove the pipeline notice only once real, dated pieces exist.

## 9. Careers

- [ ] Confirm each of the five roles is genuinely open and funded. Delete the rest.
- [ ] Real closing dates, and decide whether a dedicated recruitment address is needed.
- [ ] Confirm the vetting standard the firm can actually arrange.
- [ ] Confirm COREN registration support before claiming it.

Keep the recruitment-fraud warning — it is accurate and protects candidates.

## 10. Contact form — currently non-functional

No submission endpoint. `assets/js/site.js` deliberately blocks submission and directs the user
to email rather than silently discarding an enquiry.

To activate, set a real `action` on the `<form data-enquiry-form>` element in
`tools/content_company.py` → `contact()`, then re-run the generator.

- [ ] An endpoint that stores or forwards submissions somewhere monitored.
- [ ] Spam protection.
- [ ] Privacy policy updated to cover what the form collects.
- [ ] **Keep** the warning against submitting classified or security-sensitive information.

## 11. Imagery

No photography — illustrations are inline SVG. See `assets/img/README.md`. For this firm the
highest-value additions are **photographs of completed projects**, which do more for credibility
than any amount of copy. Subject to client permission and site security review.

## 12. Repository name

The repo is still `pinnacle-precision-defence` from the earlier draft, while the site is now
Pinnacle Precision Engineering & Consulting. Renaming it on GitHub also changes the Pages URL.
Cosmetic, but worth doing before the link is circulated widely.

---

## Launch gate

Do not publish while any of the following is true:

- [ ] Any `class="todo"` marker remains in the built HTML.
- [ ] Any named individual has not approved their own biography.
- [ ] The legal pages still carry the "draft requiring legal review" banner.
- [ ] Any credential is claimed that the firm does not currently hold.
- [ ] The non-weaponized scope statement does not match what the business actually does.
