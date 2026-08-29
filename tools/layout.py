"""Shared page chrome for the Pinnacle Precision Engineering & Consulting site.

Source of truth for the <head>, masthead/navigation and footer. Run
``python3 tools/generate.py`` to write these into every page (including
index.html, patched in place between its HEADER/FOOTER markers).

Content derives from two client documents held in "Context from Lekan/":
  - pinnacle_precision_defense_profile.pptx  (pillars 01-04, mission,
    engagement model, use cases, contact details)
  - Pitch on 3 phases.pdf                    (the short/mid/long-term roadmap)
Do not invent capabilities that are not in those documents.

EXCEPTION, recorded deliberately: pillar 05 (Sovereign Cloud & AI Infrastructure)
is NOT in either source document. It was directed by the founder and is grounded
in Nigeria's NITDA cloud instruments plus publicly released defence cloud
reference architectures, see research/military-cloud-architectures.md. A signed
capability statement for it should be added to "Context from Lekan/" so the
no-invented-capabilities rule holds for pillar 05 as it does for 01-04.

Paths are emitted relative to each page's depth via {P}, so the site works when
served from a subdirectory (GitHub Pages project sites) and from file://.
"""

# --- Company facts (from the profile deck) --------------------------------- #
LEGAL_NAME = "Pinnacle Precision Engineering &amp; Consulting Limited"
SHORT_NAME = "Pinnacle Precision"
BRAND_SUB = "Engineering &amp; Consulting"
TAGLINE = "Engineering Readiness for Secure Operations"
SITE_URL = "https://www.pinnaclepec.com"
HQ = "Abuja, Nigeria"
EMAIL_INFO = "info@pinnaclepec.com"
EMAIL_ENQUIRIES = "enquiries@pinnaclepec.com"
PHONE = "+1 (662) 497-9481"

NAV_CAPABILITIES = [
    ("engineering-design",       "Defence Engineering Design",  "Secure facilities, MEP, CAD/BIM"),
    ("military-construction",    "Military Construction",       "Bases, barracks, logistics hubs"),
    ("defence-supply-chain",     "Defence Supply Chain",        "Vendor qualification, sourcing, inventory"),
    ("modernization-consulting", "Modernization Consulting",    "Asset management, IoT, maintenance"),
    ("sovereign-cloud-and-ai",   "Sovereign Cloud &amp; AI Infrastructure",
     "Classification, landing zones, sovereign AI"),
]

NAV_SECTORS = [
    ("nigerian-army",             "Nigerian Army",                 "Barracks, training, vehicle hubs"),
    ("defence-headquarters",      "Ministry of Defence &amp; DHQ", "Joint programmes and governance"),
    ("naval-and-air-installations", "Naval &amp; Air Installations", "Base infrastructure, hangars, storage"),
    ("internal-security",         "Internal Security Agencies",    "Police and paramilitary facilities"),
    ("defence-industrialisation", "Defence Industrialisation",     "Local assembly, maintenance hubs"),
]

ARROW = ('<svg class="btn__arrow" viewBox="0 0 14 14" aria-hidden="true">'
         '<path d="M1 7h11M8 3l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>')
ARROW_SM = ('<svg viewBox="0 0 14 14" aria-hidden="true">'
            '<path d="M1 7h11M8 3l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>')

MARK = ('<svg class="brand__mark" viewBox="0 0 32 32" aria-hidden="true">'
        '<path d="M16 1.5 29 7v10.5C29 24 23.2 29 16 30.5 8.8 29 3 24 3 17.5V7L16 1.5Z" '
        'fill="none" stroke="#00843D" stroke-width="1.6"/>'
        '<path d="M16 7.5 22.5 21h-4.1L16 15.6 13.6 21H9.5L16 7.5Z" fill="#C9A227"/></svg>')

BRAND = f'''<a class="brand" href="{{P}}index.html" aria-label="{SHORT_NAME} Engineering and Consulting, home">
      {MARK}
      <span class="brand__text">
        <span class="brand__name">Pinnacle Precision</span>
        <span class="brand__sub">{BRAND_SUB}</span>
      </span>
    </a>'''


def _panel(panel_id, heading, folder, items):
    rows = "\n          ".join(
        f'<a href="{{P}}{folder}/{slug}.html">{label}<span>{blurb}</span></a>'
        for slug, label, blurb in items
    )
    return f'''<div class="nav__panel" id="{panel_id}">
          <p class="nav__panel-head">{heading}</p>
          {rows}
        </div>'''


def _drawer_links(folder, items):
    return "\n        ".join(
        f'<a href="{{P}}{folder}/{slug}.html">{label}</a>' for slug, label, _ in items
    )


CARET = ('<svg class="nav__caret" viewBox="0 0 10 10" aria-hidden="true">'
         '<path d="M1 3l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>')

HEADER = f'''<header class="masthead">
  <div class="shell masthead__inner">
    {BRAND}

    <nav class="nav" aria-label="Primary">
      <div class="nav__item">
        <button class="nav__link" data-nav-trigger aria-expanded="false" aria-controls="panel-cap">
          Capabilities
          {CARET}
        </button>
        {_panel("panel-cap", "Five capability pillars", "capabilities", NAV_CAPABILITIES)}
      </div>

      <div class="nav__item">
        <button class="nav__link" data-nav-trigger aria-expanded="false" aria-controls="panel-sec">
          Sectors
          {CARET}
        </button>
        {_panel("panel-sec", "Who we support", "sectors", NAV_SECTORS)}
      </div>

      <div class="nav__item"><a class="nav__link" href="{{P}}roadmap/index.html">Roadmap</a></div>
      <div class="nav__item"><a class="nav__link" href="{{P}}about/index.html">About</a></div>
      <div class="nav__item"><a class="nav__link" href="{{P}}careers/index.html">Careers</a></div>
    </nav>

    <div class="masthead__cta">
      <a class="btn btn--primary btn--sm" href="{{P}}contact/index.html">
        Request a briefing
        {ARROW}
      </a>
      <button class="burger" data-burger aria-expanded="false" aria-controls="site-drawer" aria-label="Open menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>

  <div class="drawer" id="site-drawer">
    <div class="shell">
      <div class="drawer__group">
        <p class="drawer__title">Capabilities</p>
        <a href="{{P}}capabilities/index.html">All capabilities</a>
        {_drawer_links("capabilities", NAV_CAPABILITIES)}
      </div>
      <div class="drawer__group">
        <p class="drawer__title">Sectors</p>
        <a href="{{P}}sectors/index.html">All sectors</a>
        {_drawer_links("sectors", NAV_SECTORS)}
      </div>
      <div class="drawer__group">
        <p class="drawer__title">Company</p>
        <a href="{{P}}roadmap/index.html">Engagement roadmap</a>
        <a href="{{P}}about/index.html">About us</a>
        <a href="{{P}}about/leadership.html">Leadership</a>
        <a href="{{P}}about/integrity-and-compliance.html">Integrity &amp; compliance</a>
        <a href="{{P}}insights/index.html">Insights</a>
        <a href="{{P}}careers/index.html">Careers</a>
      </div>
      <div class="drawer__foot">
        <a class="btn btn--primary" href="{{P}}contact/index.html">Request a briefing</a>
      </div>
    </div>
  </div>
</header>'''


def _footer_col(heading, links):
    rows = "\n        ".join(f'<a href="{{P}}{href}">{label}</a>' for href, label in links)
    return f'''<div class="footer__col">
        <h3>{heading}</h3>
        {rows}
      </div>'''


FOOTER = f'''<footer class="footer">
  <div class="shell">
    <div class="footer__top">
      <div class="footer__brandblock">
        {BRAND.replace(' aria-label="' + SHORT_NAME + ' Engineering and Consulting, home"', '')}
        <p>
          Nigerian engineering and construction for defence.
        </p>
        <p style="margin-top:14px">
          {HQ}<br>
          <a href="mailto:{EMAIL_ENQUIRIES}">{EMAIL_ENQUIRIES}</a><br>
          <a href="mailto:{EMAIL_INFO}">{EMAIL_INFO}</a><br>
          <a href="tel:+16624979481">{PHONE}</a>
        </p>
      </div>

      {_footer_col("Capabilities", [(f"capabilities/{s}.html", l) for s, l, _ in NAV_CAPABILITIES])}

      {_footer_col("Sectors", [(f"sectors/{s}.html", l) for s, l, _ in NAV_SECTORS])}

      {_footer_col("Company", [
          ("roadmap/index.html", "Engagement roadmap"),
          ("about/index.html", "About us"),
          ("about/leadership.html", "Leadership"),
          ("about/integrity-and-compliance.html", "Integrity &amp; compliance"),
          ("insights/index.html", "Insights"),
          ("careers/index.html", "Careers"),
          ("contact/index.html", "Contact"),
      ])}

      {_footer_col("Legal", [
          ("legal/privacy-policy.html", "Privacy policy"),
          ("legal/terms-of-use.html", "Terms of use"),
          ("legal/anti-corruption-policy.html", "Anti-corruption policy"),
          ("contact/index.html", "Report a concern"),
      ])}
    </div>

    <div class="footer__bottom">
      <p style="margin:0">
        © <span data-year>2026</span> {LEGAL_NAME}.
        RC <span class="todo">TODO: CAC number</span>. Registered in Nigeria.
      </p>
      <div class="footer__legal">
        <a href="{{P}}legal/privacy-policy.html">Privacy</a>
        <a href="{{P}}legal/terms-of-use.html">Terms</a>
        <a href="{{P}}legal/anti-corruption-policy.html">Anti-corruption</a>
      </div>
    </div>
  </div>
</footer>'''


PAGE = '''<!DOCTYPE html>
<html lang="en-NG">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Pinnacle Precision Engineering &amp; Consulting</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#080B0F">
<link rel="canonical" href="{site}/{path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title} | Pinnacle Precision Engineering &amp; Consulting">
<meta property="og:description" content="{desc}">
<meta property="og:site_name" content="Pinnacle Precision Engineering &amp; Consulting Limited">
<link rel="icon" href="{P}assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{P}assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<!-- ====== HEADER (generated by tools/generate.py, do not edit by hand) ====== -->
{header}
<!-- ====== /HEADER ====== -->

<main id="main">
{body}
</main>

<!-- ====== FOOTER (generated by tools/generate.py, do not edit by hand) ====== -->
{footer}
<!-- ====== /FOOTER ====== -->

<script src="{P}assets/js/site.js" defer></script>
</body>
</html>
'''


def breadcrumb(trail):
    """trail: list of (label, href_or_None); last item is the current page."""
    parts = ['<a href="{P}index.html">Home</a>']
    for label, href in trail:
        parts.append('<span aria-hidden="true">/</span>')
        parts.append(f'<a href="{{P}}{href}">{label}</a>' if href else f"<span>{label}</span>")
    return '<nav class="breadcrumb" aria-label="Breadcrumb">' + "".join(parts) + "</nav>"


def page_hero(eyebrow, title, lede, trail=(), actions=""):
    return f'''  <section class="hero hero--page">
    <div class="hero__bg"></div>
    <div class="shell">
      {breadcrumb(list(trail))}
      <div class="hero__body">
        <p class="eyebrow">{eyebrow}</p>
        <h1 class="d1">{title}</h1>
        <p class="lede">{lede}</p>
        {actions}
      </div>
    </div>
  </section>
'''


def cta_band(heading="Ready to support defence readiness?",
             body="Request a capability briefing, proposal, partnership meeting or site "
                  "assessment."):
    return f'''  <section class="cta-band">
    <div class="shell cta-band__inner">
      <div>
        <p class="eyebrow">Get in touch</p>
        <h2 class="d2">{heading}</h2>
        <p>{body}</p>
      </div>
      <div class="actions">
        <a class="btn btn--primary" href="{{P}}contact/index.html">Request a briefing {ARROW}</a>
        <a class="btn btn--ghost" href="{{P}}capabilities/index.html">All capabilities</a>
      </div>
    </div>
  </section>
'''


def link_arrow(label, href):
    return f'<a class="link-arrow" href="{{P}}{href}">{label} {ARROW_SM}</a>'


def ruled(rows):
    out = ['<div class="ruled">']
    for h, p in rows:
        out.append(f'      <div class="ruled__row"><h3>{h}</h3><p>{p}</p></div>')
    out.append("    </div>")
    return "\n".join(out)


def accordion(acc_id, items):
    out = [f'<div class="acc" data-acc id="{acc_id}">']
    for i, (q, body) in enumerate(items, 1):
        bid = f"{acc_id}-b{i}"
        out.append(f'''      <div class="acc__item">
        <h3><button class="acc__btn" aria-expanded="false" aria-controls="{bid}">
          <span>{q}</span><span class="acc__sign" aria-hidden="true"></span>
        </button></h3>
        <div class="acc__body" id="{bid}">{body}</div>
      </div>''')
    out.append("    </div>")
    return "\n".join(out)


def cards(items, numbered=True, cols=3):
    """items: list of (title, blurb) or (title, blurb, href)."""
    out = [f'<div class="grid grid--{cols}">']
    for i, item in enumerate(items, 1):
        title, blurb = item[0], item[1]
        href = item[2] if len(item) > 2 else None
        num = f'<p class="card__num">{i:02d}</p>' if numbered else ""
        foot = (f'<div class="card__foot"><span class="link-arrow">Read more {ARROW_SM}</span></div>'
                if href else "")
        tag = f'<a class="card" href="{{P}}{href}"' if href else '<div class="card"'
        end = "</a>" if href else "</div>"
        out.append(f'      {tag}>{num}<h3>{title}</h3><p>{blurb}</p>{foot}{end}')
    out.append("    </div>")
    return "\n".join(out)


DISCLAIMER = (
    '<div class="notice"><p style="margin:0"><strong>Note:</strong> applications shown here are '
    'proposed for discussion.</p></div>'
)


def render(path, title, desc, body):
    depth = path.count("/")
    prefix = "../" * depth
    html = PAGE.format(title=title, desc=desc, site=SITE_URL, path=path,
                       header=HEADER, footer=FOOTER, body=body, P="{P}")
    return html.replace("{P}", prefix)
