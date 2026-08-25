# Pinnacle Precision Defence — website

Static marketing and capability site for Pinnacle Precision Defence Limited, an independent
defence advisory firm serving the Nigerian Armed Forces, the Ministry of Defence and national
security agencies.

The information architecture is modelled on [axon.com](https://www.axon.com): a mission-led
homepage with a rotating capability carousel, a products-style `capabilities/` tree, an
industries-style `sectors/` tree, plus company, insights, careers, contact and legal sections.

> **This site is not ready to publish.** Placeholders are marked in gold throughout and must be
> replaced with verified facts first. See [`CONTENT-TODO.md`](CONTENT-TODO.md).

## Stack

Plain HTML, one CSS file, one JS file. No framework, no dependencies, no build step on the
host — it can be served by GitHub Pages, S3, Netlify, Nginx or anything else that serves files.

- Total page weight is dominated by the single 24 KB stylesheet; there are no web fonts,
  no images and no third-party scripts.
- JavaScript is progressive enhancement only. Navigation, content and the contact form are all
  usable with JS disabled.
- Illustrations are inline SVG, so there are no missing-image placeholders to chase.
- Accessibility: skip link, semantic landmarks, ARIA on the nav/rotator/accordions, keyboard
  support on the rotator, visible focus rings, and `prefers-reduced-motion` respected.

## Layout

```
index.html                 Homepage (hand-authored body; chrome is generated)
capabilities/              Index + 8 service-line pages
sectors/                   Index + 6 client-group pages
about/                     About, leadership, integrity & compliance
insights/  careers/  contact/
legal/                     Privacy, terms of use, anti-corruption policy
404.html  robots.txt  sitemap.xml
assets/css/site.css        Whole design system
assets/js/site.js          Nav, rotator, accordions, reveal, form guard
tools/                     Generator (dev-time only, never served)
```

## Editing

The header, navigation and footer appear on 27 pages. They live in **one** place —
`tools/layout.py` — and are written into every page by the generator, including `index.html`
(patched in place between its `HEADER` / `FOOTER` marker comments).

```bash
python3 tools/generate.py     # no dependencies, Python 3.8+
```

The generator prints every file it wrote and then runs an internal link check, which fails the
build on any `href` that does not resolve to a file on disk.

| To change | Edit |
|---|---|
| Nav, footer, `<head>`, page shell | `tools/layout.py` |
| Any capability page | `tools/content_capabilities.py` |
| Any sector page | `tools/content_sectors.py` |
| About / leadership / integrity / insights / careers / contact / legal / 404 | `tools/content_company.py` |
| Homepage body (hero, rotator, sections) | `index.html` directly — between `<main>` and `</main>` |
| Design system | `assets/css/site.css` |

Do not hand-edit the generated pages: the next generator run overwrites them. The homepage
`<main>` is the one place you edit HTML directly.

Adding a capability or sector page means adding one entry to `NAV_CAPABILITIES` /
`NAV_SECTORS` in `tools/layout.py` and one content block in the matching module — the nav,
drawer, footer, index cards and sitemap all pick it up automatically.

## Local preview

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

Links are relative rather than root-absolute, so the site also works opened directly from disk
(`file://`) and when served from a subdirectory.

## Deployment

Any static host. For **GitHub Pages**, set Pages to deploy from the repository root on the
default branch; `.nojekyll` is present so Jekyll does not interfere. Relative links mean the
site works unchanged whether it is served from a custom domain or from
`username.github.io/repo-name/`.

Before the first real deployment, set the live domain in `tools/layout.py` (`SITE_URL`) and in
the `canonical` tag in `index.html`, then re-run the generator so `sitemap.xml` and every
canonical URL match.

## Editorial rules baked into the site

Worth preserving through future edits — each is a deliberate decision, not an oversight:

1. **No client is named.** Every sector page carries a notice stating that describing a sector
   does not assert an existing contractual relationship.
2. **No invented credentials.** No certifications, client counts, award claims or biographies.
   Where a real fact is needed, there is a visible placeholder instead.
3. **The independence position is stated repeatedly** — no equipment sales, no supplier
   commission, no agency agreements — because it is the firm's core commercial differentiator
   and the basis of trust in its procurement advice.
4. **Scope limits are published**, including the work the firm declines: no arms brokering, no
   armed services, no offensive cyber, no domestic influence operations. See
   `about/integrity-and-compliance.html`.
5. **The contact form warns against sending classified material** and has no active endpoint.

## Licence

© Pinnacle Precision Defence Limited. All rights reserved. Not for redistribution.
