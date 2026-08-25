"""Shared page chrome for the Pinnacle Precision Defence site.

The site ships as plain static HTML with no runtime dependencies. This module is
the single source of truth for the <head>, masthead/navigation and footer; run
``python3 tools/generate.py`` to write those into every page (including
index.html, which is patched in place between its HEADER/FOOTER markers).

Paths are emitted relative to each page's depth via {P}, so the site works when
served from a subdirectory (GitHub Pages project sites) and from file://.
"""

NAV_CAPABILITIES = [
    ("strategy-and-policy",      "Defence Strategy &amp; Policy",        "Doctrine, white papers, force posture"),
    ("capability-development",   "Capability Development",               "Requirements, force design, DLOD analysis"),
    ("procurement-advisory",     "Procurement &amp; Acquisition",        "BPP-compliant sourcing and lifecycle costing"),
    ("training-and-doctrine",    "Training, Doctrine &amp; Simulation",  "Curriculum design, exercise design, OPFOR"),
    ("isr-and-c4i",              "ISR &amp; C4I Advisory",               "Sensor-to-shooter architecture, interoperability"),
    ("sustainment-and-mro",      "Sustainment &amp; MRO",                "Availability engineering, spares, obsolescence"),
    ("cyber-and-information",    "Cyber &amp; Information Defence",      "Assurance, SOC design, information operations"),
    ("border-and-maritime",      "Border &amp; Maritime Security",       "Domain awareness, Gulf of Guinea operations"),
]

NAV_SECTORS = [
    ("defence-headquarters", "Ministry of Defence &amp; DHQ",  "Policy, joint planning, programme governance"),
    ("nigerian-army",        "Nigerian Army",                  "Land capability, counter-insurgency, training"),
    ("nigerian-navy",        "Nigerian Navy",                  "Maritime domain awareness, fleet sustainment"),
    ("nigerian-air-force",   "Nigerian Air Force",             "Air power, ISR, availability engineering"),
    ("internal-security",    "Internal Security Agencies",     "Police, NSCDC, Customs, Immigration, NDLEA"),
    ("defence-industry",     "Defence Industrial Base",        "DICON, local content, offset and OEM entry"),
]

SITE_NAME = "Pinnacle Precision Defence"
SITE_URL = "https://www.pinnacleprecisiondefence.ng"

ARROW = ('<svg class="btn__arrow" viewBox="0 0 14 14" aria-hidden="true">'
         '<path d="M1 7h11M8 3l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>')
ARROW_SM = ('<svg viewBox="0 0 14 14" aria-hidden="true">'
            '<path d="M1 7h11M8 3l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>')

MARK = ('<svg class="brand__mark" viewBox="0 0 32 32" aria-hidden="true">'
        '<path d="M16 1.5 29 7v10.5C29 24 23.2 29 16 30.5 8.8 29 3 24 3 17.5V7L16 1.5Z" '
        'fill="none" stroke="#00843D" stroke-width="1.6"/>'
        '<path d="M16 7.5 22.5 21h-4.1L16 15.6 13.6 21H9.5L16 7.5Z" fill="#C9A227"/></svg>')

BRAND = f'''<a class="brand" href="{{P}}index.html" aria-label="{SITE_NAME} — home">
      {MARK}
      <span class="brand__text">
        <span class="brand__name">Pinnacle Precision</span>
        <span class="brand__sub">Defence</span>
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
        {_panel("panel-cap", "Service lines", "capabilities", NAV_CAPABILITIES)}
      </div>

      <div class="nav__item">
        <button class="nav__link" data-nav-trigger aria-expanded="false" aria-controls="panel-sec">
          Sectors
          {CARET}
        </button>
        {_panel("panel-sec", "Who we support", "sectors", NAV_SECTORS)}
      </div>

      <div class="nav__item"><a class="nav__link" href="{{P}}insights/index.html">Insights</a></div>
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
        {BRAND.replace(' aria-label="' + SITE_NAME + ' — home"', '')}
        <p>
          Independent defence and security advisory to the Nigerian Armed Forces, the Ministry
          of Defence and national security agencies.
        </p>
        <p style="margin-top:14px">
          <span class="todo">TODO: registered address</span><br>
          <span class="todo">TODO: phone</span><br>
          <a href="mailto:enquiries@example.com"><span class="todo">TODO: enquiries email</span></a>
        </p>
      </div>

      {_footer_col("Capabilities", [(f"capabilities/{s}.html", l) for s, l, _ in NAV_CAPABILITIES])}

      {_footer_col("Sectors", [(f"sectors/{s}.html", l) for s, l, _ in NAV_SECTORS])}

      {_footer_col("Company", [
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
        © <span data-year>2026</span> Pinnacle Precision Defence Limited.
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
<title>{title} — Pinnacle Precision Defence</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#080B0F">
<link rel="canonical" href="{site}/{path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title} — Pinnacle Precision Defence">
<meta property="og:description" content="{desc}">
<meta property="og:site_name" content="Pinnacle Precision Defence">
<link rel="icon" href="{P}assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{P}assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<!-- ====== HEADER (generated by tools/generate.py — do not edit by hand) ====== -->
{header}
<!-- ====== /HEADER ====== -->

<main id="main">
{body}
</main>

<!-- ====== FOOTER (generated by tools/generate.py — do not edit by hand) ====== -->
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


def cta_band(heading="Start with a scoping conversation",
             body="Tell us the capability problem. We will tell you honestly whether it is one "
                  "we are qualified to help with."):
    return f'''  <section class="cta-band">
    <div class="shell cta-band__inner">
      <div>
        <p class="eyebrow">Next step</p>
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


def render(path, title, desc, body):
    depth = path.count("/")
    prefix = "../" * depth
    html = PAGE.format(title=title, desc=desc, site=SITE_URL, path=path,
                       header=HEADER, footer=FOOTER, body=body, P="{P}")
    return html.replace("{P}", prefix)
