# Pre-launch checklist

Every item marked in gold on the site (`<span class="todo">`) is a placeholder that must be
replaced with a **verified** fact before this site is published. They are deliberately styled to
be impossible to miss in a browser, so nothing ships by accident.

To find them all:

```bash
grep -rn 'class="todo"' --include='*.html' .
```

Placeholders live in the generator, not the generated HTML. Edit `tools/layout.py` (footer,
navigation) or the relevant `tools/content_*.py` module, then re-run `python3 tools/generate.py`.

---

## 1. Corporate identity — blocking

| Item | Where | Notes |
|---|---|---|
| CAC registration (RC) number | footer (every page), `about/index.html` | From the CAC certificate of incorporation. |
| Date of incorporation | `about/index.html` | |
| Registered office address | footer, `about/index.html`, `contact/index.html`, legal pages | Must match the CAC record. |
| Switchboard number | footer, `contact/index.html` | |
| Enquiries email | footer, `contact/index.html` | |
| Business development email | `contact/index.html` | |
| Recruitment email | `careers/index.html` | |
| Press email | `contact/index.html` | |
| Confidential reporting email + phone | `about/integrity-and-compliance.html`, `contact/index.html`, `legal/anti-corruption-policy.html` | Must route to the compliance function, **not** to a fee-earning line. |
| Domain name | `tools/layout.py` → `SITE_URL`, and the `canonical` tag in `index.html` | Currently `pinnacleprecisiondefence.ng` — confirm or change before launch, then re-run the generator. |

## 2. Leadership — blocking, and the highest-risk section

`about/leadership.html` is a **structural placeholder only**. Do not publish named biographies until:

- [ ] The individual has confirmed their appointment **in writing**.
- [ ] The individual has read and approved their own biography text.
- [ ] Every claimed rank, appointment, posting, decoration, degree and professional membership
      has been independently verified against documentation.
- [ ] Any reference to prior service is cleared against the individual's terms of retirement —
      some carry restrictions on the commercial use of a former appointment.

Overstating a leadership team's credentials is the fastest way to destroy a new defence
advisory firm's credibility, and it is trivially checkable by exactly the people you are
selling to.

Also required: advisory board composition, and publication of its terms of reference.

## 3. Numbers — remove or substantiate

The homepage stat band (`index.html`) has three placeholder figures: consultant headcount,
combined years of service experience, and engagements delivered.

For a newly incorporated firm, the honest options are:

1. Publish real figures once they exist, however modest.
2. **Delete the stat band entirely** until they do.

Do not publish an aspirational number. Combined-experience figures in particular are easy to
inflate and are treated as a warning sign by informed buyers.

## 4. Clients and case studies

No client is named anywhere on the site, by design. Before any client reference appears:

- [ ] Written permission from the client to be named.
- [ ] Classification review of the engagement description.
- [ ] Sign-off from the compliance function.

The sector pages each carry a visible notice stating that describing a sector does not assert
an existing contractual relationship. **Keep that notice** until real, permissioned references
exist.

## 5. Legal documents — require Nigerian counsel

All three carry a "draft requiring legal review" banner. Do not remove the banner until counsel
has signed off.

- [ ] `legal/privacy-policy.html` — must be checked against the **Nigeria Data Protection Act**.
      Sections needing real answers: what the live site actually collects, lawful basis per
      purpose, cookie/analytics inventory, processor list, retention periods per data category,
      international transfer safeguards (relevant as soon as you use foreign cloud hosting or
      email).
- [ ] `legal/terms-of-use.html` — limitation of liability and jurisdiction clauses are
      deliberately left blank rather than filled with generic wording.
- [ ] `legal/anti-corruption-policy.html` — confirm the applicable Nigerian statutes, set the
      gift/hospitality threshold, name the financial approval thresholds and controls, set the
      training frequency and the board review cycle.

Still to be drafted and published (referenced from `about/integrity-and-compliance.html`):

- [ ] Conflict of interest policy
- [ ] Human rights and engagement acceptance policy
- [ ] Whistleblowing policy

## 6. Insights — do not fake it

`insights/index.html` lists five briefings as an **editorial pipeline**, with a visible notice
saying so. Nothing there is written yet.

- [ ] Write at least two briefings properly before launch — the Insights section is the single
      strongest credibility signal available to a firm with no public client list.
- [ ] Classification and factual review before each publication.
- [ ] Remove the pipeline notice only once real, dated pieces exist.
- [ ] Decide on the mailing list mechanism; a privacy notice is required before collecting a
      single address.

## 7. Careers

- [ ] Confirm each of the five advertised roles is genuinely open and funded. Delete the rest.
- [ ] Real closing dates and a real application address.
- [ ] Confirm the security vetting standard the firm will apply and can actually arrange.
- [ ] Confirm the training budget and development framework, or remove the claim.

The recruitment-fraud warning ("we charge nothing to apply") should stay — it is accurate and
it protects candidates.

## 8. Contact form — currently non-functional

`contact/index.html` has no submission endpoint. `assets/js/site.js` deliberately blocks
submission and tells the user to email instead, rather than silently discarding an enquiry.

To activate, set a real `action` on the `<form data-enquiry-form>` element (in
`tools/content_company.py` → `contact()`), then re-run the generator. The JS hands control back
to the browser as soon as an `action` is present.

Requirements before enabling:

- [ ] An endpoint that stores or forwards submissions somewhere monitored.
- [ ] Spam protection.
- [ ] Confirm the privacy policy covers the data the form collects.
- [ ] **Keep** the on-form warning against submitting classified or operationally sensitive
      information.

## 9. Imagery

The site currently uses generated SVG diagrams and CSS gradients — no photography. See
`assets/img/README.md` for what to add and the licensing/OPSEC constraints that apply to
defence photography specifically.

## 10. Third-party verification

`about/integrity-and-compliance.html` states an intent to seek external assessment of the
compliance programme (e.g. ISO 37001). Either confirm that intent with a real target and
timeline, or remove the paragraph. Do not leave an unspecific promise on the page.

---

## Launch gate

Do not publish while any of the following is true:

- [ ] Any `class="todo"` marker remains in the built HTML.
- [ ] Any named individual has not approved their own biography.
- [ ] The legal pages still carry the "draft requiring legal review" banner.
- [ ] The stat band contains a figure that cannot be substantiated on request.
