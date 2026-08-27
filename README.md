# Pinnacle Precision Engineering & Consulting — website

Defence-aligned capability profile for **Pinnacle Precision Engineering & Consulting Limited**,
a Nigerian engineering and construction firm based in Abuja.

Structure and interaction patterns are modelled on [axon.com](https://www.axon.com) — a
mission-led homepage with a rotating capability carousel, a products-style `capabilities/` tree,
an industries-style `sectors/` tree, plus company, roadmap, insights, careers, contact and legal
sections.

> **Not ready to publish.** Placeholders are marked in gold throughout and must be replaced with
> verified facts first. See [`CONTENT-TODO.md`](CONTENT-TODO.md).

## Content source of truth

Everything on this site derives from two client documents in `Context from Lekan/`:

| Document | Supplies |
|---|---|
| `pinnacle_precision_defense_profile.pptx` | The four capability pillars, mission and positioning statement, value proposition, readiness outcomes, Assess→Design→Deliver→Sustain engagement model, illustrative use cases, contact details |
| `Pitch on 3 phases.pdf` | The phased roadmap — short-term hardware selection and supply chain, mid-term operational gap analysis, long-term indigenous design and manufacturing |

**Do not add capabilities that are not in those documents.** An earlier draft of this site
invented eight defence-advisory service lines and missed engineering and construction entirely;
the four pillars below are the real business.

## The four pillars

1. **Defence Engineering Design** — secure facilities, C2 spaces, blast-aware structural design, MEP, 3D CAD/BIM, FEED→IFC
2. **Military Construction** — bases, barracks, training grounds, logistics hubs, perimeter infrastructure, secure storage
3. **Defence Supply Chain** — vendor qualification, strategic sourcing, logistics, inventory dashboards, lifecycle support
4. **Modernization Consulting** — risk assessment, asset management, lifecycle cost, IoT, analytics, predictive maintenance

## Stack

Plain HTML, one CSS file, one JS file. No framework, no dependencies, no build step on the host —
serve it from GitHub Pages, S3, Netlify, Nginx or anything else that serves files.

- No web fonts, no images, no third-party scripts. Page weight is dominated by the single stylesheet.
- JavaScript is progressive enhancement only; navigation, content and the form work without it.
- Illustrations are inline SVG, so there are no missing-image placeholders.
- Accessibility: skip link, semantic landmarks, ARIA on nav/rotator/accordions, keyboard support
  on the rotator, visible focus rings, `prefers-reduced-motion` respected.

## Layout

```
index.html                 Homepage (hand-authored body; chrome is generated)
capabilities/              Index + 4 pillar pages
sectors/                   Index + 5 customer-group pages
roadmap/                   The three-phase engagement roadmap
about/                     About, leadership, integrity & compliance
insights/  careers/  contact/
legal/                     Privacy, terms of use, anti-corruption policy
404.html  robots.txt  sitemap.xml
assets/css/site.css        Whole design system
assets/js/site.js          Nav, rotator, accordions, reveal, form guard
tools/                     Generator (dev-time only, never served)
Context from Lekan/        Client source documents
```

## Editing

The header, navigation and footer appear on 23 pages. They live in **one** place —
`tools/layout.py` — and are written into every page by the generator, including `index.html`
(patched in place between its `HEADER` / `FOOTER` marker comments).

```bash
python3 tools/generate.py     # no dependencies, Python 3.8+
```

The generator prints every file it wrote, then runs an internal link check that fails the build
on any `href` that does not resolve to a file on disk. It is idempotent — running it repeatedly
produces identical output.

| To change | Edit |
|---|---|
| Company facts (name, contacts, domain), nav, footer, page shell | `tools/layout.py` |
| Any capability pillar page | `tools/content_capabilities.py` |
| Any sector page | `tools/content_sectors.py` |
| The phased roadmap page | `tools/content_roadmap.py` |
| About / leadership / integrity / insights / careers / contact / legal / 404 | `tools/content_company.py` |
| Homepage body | `index.html` directly — between `<main>` and `</main>` |
| Design system | `assets/css/site.css` |

Do not hand-edit the generated pages: the next run overwrites them. The homepage `<main>` is the
one place you edit HTML directly.

Adding a page means one entry in `NAV_CAPABILITIES` / `NAV_SECTORS` in `tools/layout.py` plus one
content block in the matching module — nav, drawer, footer, index cards and sitemap all follow.

## Local preview

```bash
python3 -m http.server 8000
# http://localhost:8000
```

Links are relative, so the site also works from `file://` and from a subdirectory.

## Deployment

Any static host. For **GitHub Pages**, deploy from the repository root on the default branch;
`.nojekyll` is present. Relative links mean it works from a custom domain or from
`username.github.io/repo-name/` unchanged.

`SITE_URL` in `tools/layout.py` is set to `https://www.pinnaclepec.com` — matching the email
domain in the profile deck. Re-run the generator after changing it so `sitemap.xml` and every
canonical URL match.

## Editorial rules baked into the site

Deliberate decisions, not oversights — preserve them through future edits:

1. **No client is named**, and every sector and capability page carries the deck's own
   disclaimer that applications are proposed for discussion and do not represent claims of
   completed Nigerian Army contracts.
2. **No invented credentials.** No certifications, project counts, award claims or biographies.
   Where a real fact is needed there is a visible placeholder.
3. **Illustrative figures are labelled as illustrative**, carrying the deck's own wording
   including "actual results depend on scope and baseline conditions."
4. **Non-weaponized scope is stated plainly** — taken from both source documents, which treat it
   as a value proposition because it reduces procurement complexity. The site says what the firm
   supplies, what it advises on, and what it does not do.
5. **The contact form warns against sending sensitive material** and has no active endpoint.

## Licence

© Pinnacle Precision Engineering & Consulting Limited. All rights reserved. Not for redistribution.
