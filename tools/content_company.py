"""Company pages: about, leadership, integrity, insights, careers, contact, legal, 404.

Company facts come from pinnacle_precision_defense_profile.pptx. Anything still
unverified is a visible placeholder, tracked in CONTENT-TODO.md.

Copy is deliberately tight. Short sentences, one idea per line.
"""

from layout import (ARROW, ARROW_SM, page_hero, cta_band, link_arrow, ruled,
                    accordion, cards, DISCLAIMER, LEGAL_NAME, HQ, EMAIL_INFO,
                    EMAIL_ENQUIRIES, PHONE)

TODO = '<span class="todo">TODO: {}</span>'


def about_index():
    body = page_hero(
        "About us",
        "Fifteen years of engineering, construction and supply chain work",
        "A Nigerian engineering and construction firm. For defence that means five "
        "capabilities: engineering design, military construction, supply chain, modernization "
        "consulting, and sovereign cloud and AI.",
        trail=[("About", None)],
    )

    body += f'''
  <section class="section">
    <div class="shell">
      <div class="split">
        <div class="prose">
          <p class="eyebrow">Overview</p>
          <p>
            {LEGAL_NAME} is a Nigerian engineering and construction firm, founded by a team with
            more than fifteen years of combined industry experience and headquartered in {HQ}
            ({TODO.format("CAC number and date of incorporation")}).
          </p>
          <p>
            Our four disciplines, design, build, procure and sustain, map onto what defence
            infrastructure and readiness programmes need. This site sets out that mapping.
          </p>

          <h2>Positioning</h2>
          <p>
            Mission-critical engineering and project delivery that improves readiness, hardens
            infrastructure and strengthens defence logistics, without compromising safety,
            quality, integrity or sustainability.
          </p>

          <h2>Where we focus</h2>
          <p>
            Equipment and supply chain work covers <strong>non-weaponized</strong> categories:
            radios, protective equipment, uniforms, vehicles, surveillance tools and field gear.
            That focus is commercial as much as ethical. It cuts procurement complexity and
            delivers readiness faster.
          </p>
          <p>
            On drones, aircraft and detection systems we help define purpose-based requirements
            and specifications, so you can procure with confidence.
          </p>
        </div>

        <div>
          <p class="eyebrow">At a glance</p>
          {ruled([
              ("Legal entity", f"{LEGAL_NAME}. RC {TODO.format('number')}."),
              ("Headquarters", f"{HQ}. {TODO.format('registered office address')}."),
              ("Experience", "15+ years combined founding-team experience."),
              ("Service lines", "Five pillars: engineering design, military construction, supply chain, modernization consulting, sovereign cloud &amp; AI."),
          ])}
          <div class="notice mt-32">
            <p style="margin:0"><strong>Pre-launch:</strong> gold items need verified facts. See
            <code>CONTENT-TODO.md</code>.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="section-head section-head--wide">
        <p class="eyebrow">Value proposition</p>
        <h2 class="d2">Delivery aligned to readiness</h2>
      </div>
      {cards([
          ("National security alignment", "Every engagement scoped around readiness and continuity."),
          ("Operational efficiency", "Workflows that shorten time-to-readiness."),
          ("Digital readiness", "BIM, IoT and analytics brought into analogue infrastructure."),
          ("Long-term partnership", "Built for repeat engagement and lifecycle support."),
      ], cols=4)}
    </div>
  </section>

  <section class="section" id="method">
    <div class="shell">
      <div class="split split--sticky">
        <div>
          <p class="eyebrow">Engagement model</p>
          <h2 class="d2">From needs assessment to lifecycle support</h2>
          <p class="lede mt-16">
            All work runs inside the procurement, governance, security and confidentiality
            requirements you set.
          </p>
          <div class="actions mt-32">
            <a class="btn btn--ghost" href="{{P}}roadmap/index.html">The phased roadmap</a>
          </div>
        </div>
        <div class="steps">
          <div class="step"><div><h3>Assess</h3></div>
            <p>Requirements, site realities, constraints and risk. Nothing starts on a verbal
            brief.</p></div>
          <div class="step"><div><h3>Design</h3></div>
            <p>FEED, BIM/CAD and IFC packages, with cost logic documented so it can be
            interrogated.</p></div>
          <div class="step"><div><h3>Deliver</h3></div>
            <p>Procurement, construction interfaces, quality control and commissioning, with the
            evidence file built as we go.</p></div>
          <div class="step"><div><h3>Sustain</h3></div>
            <p>Handover, training, asset data and maintenance planning, so your unit can run the
            asset unaided.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--ink2 section--line">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Delivery principles</p>
          <h2 class="d2">Secure-by-design, maintainable-by-design, audit-ready</h2>
          <div class="actions mt-32">
            <a class="btn btn--ghost" href="{{P}}about/integrity-and-compliance.html">Integrity &amp; compliance</a>
            <a class="btn btn--ghost" href="{{P}}about/leadership.html">Leadership</a>
          </div>
        </div>
        <div>
          {ruled([
              ("Design for the real maintenance budget",
               "We specify for durability, not lowest capital cost. Whole-life cost is what you pay."),
              ("Build the evidence file during delivery",
               "Quality records and as-built drawings assembled as work proceeds."),
              ("Hand over something operable",
               "Training, asset data and manuals, so you are not dependent on us."),
              ("Bring in a partner when scope needs one",
               "Named in the bid, with one accountable design authority."),
          ])}
        </div>
      </div>
    </div>
  </section>

''' + cta_band()

    return ("about/index.html", "About us",
            "Pinnacle Precision Engineering & Consulting is a Nigerian engineering and "
            "construction firm delivering defence infrastructure, supply chain and modernization "
            "support from Abuja.", body)


def leadership():
    def person(role, note):
        return f'''      <div class="card">
        <div class="card__icon" aria-hidden="true">
          <svg viewBox="0 0 30 30" fill="none" stroke="currentColor" stroke-width="1.3">
            <circle cx="15" cy="10" r="5"/><path d="M4 27c0-6 5-9 11-9s11 3 11 9"/>
          </svg>
        </div>
        <h3>{TODO.format("full name")}</h3>
        <p style="color:var(--brass);font-size:0.82rem;margin-bottom:10px">{role}</p>
        <p>{note}</p>
      </div>'''

    body = page_hero(
        "Leadership",
        "The people accountable for delivery",
        "Engineering is a business built on individual professional judgement. You are entitled "
        "to know who is responsible for the design you rely on.",
        trail=[("About", "about/index.html"), ("Leadership", None)],
    )

    body += f'''
  <section class="section section--tight">
    <div class="shell">
      <div class="notice">
        <p style="margin:0">
          <strong>Structural placeholder.</strong> Named biographies go live only once each
          individual has confirmed appointment in writing, approved their own text, and had every
          qualification and professional registration verified. For an engineering firm that
          includes COREN registration, which a defence client will check.
        </p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Founding team</p>
        <h2 class="d2">Leadership</h2>
      </div>
      <div class="grid grid--3">
{person("Managing Director", "Accountable for the firm, its clients and delivery performance.")}
{person("Director, Engineering", "Design authority and owner of the design review process.")}
{person("Director, Construction", "Delivery, site management, quality control, commissioning.")}
{person("Head of Supply Chain", "Vendor qualification, sourcing, logistics, inventory.")}
{person("Head of Modernization", "BIM, IoT, analytics and asset management.")}
{person("Head of Compliance &amp; QA", "Quality, anti-corruption controls and audit readiness. Reports independently of delivery.")}
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Credentials</p>
          <h2 class="d2">What a defence client asks for first</h2>
          <p class="lede mt-16">
            Publishing these is a competitive advantage. Claiming them without holding them is
            fatal.
          </p>
        </div>
        <div>
          {ruled([
              ("CAC incorporation", f"Certificate and RC number. {TODO.format('publish')}"),
              ("COREN registration", f"Firm and named engineers. {TODO.format('confirm status')}"),
              ("Professional indemnity", f"Cover level and insurer. {TODO.format('confirm')}"),
              ("Quality certification", f"ISO 9001 or equivalent. {TODO.format('status and timeline')}"),
          ])}
        </div>
      </div>
    </div>
  </section>

''' + cta_band(
        heading="Interested in joining?",
        body="We recruit engineers, project managers and supply chain professionals who have "
             "delivered real projects.")

    return ("about/leadership.html", "Leadership",
            "The leadership team of Pinnacle Precision Engineering & Consulting, and the "
            "credentials a defence client should expect to see.", body)


def integrity():
    body = page_hero(
        "Integrity &amp; compliance",
        "How we work",
        "Defence infrastructure spend attracts scrutiny, and should. Our controls are published "
        "so a client, partner or auditor can hold us to them.",
        trail=[("About", "about/index.html"), ("Integrity &amp; compliance", None)],
    )

    body += f'''
  <section class="section section--paper">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Framework</p>
        <h2 class="d2">Six commitments</h2>
        <p class="lede mt-16">
          Construction and procurement carry elevated corruption risk, and defence adds
          confidentiality. That argues for stricter controls.
        </p>
      </div>
      {accordion("integrity", [
          ("01. Non-weaponized scope",
           "<p>Equipment and supply chain work covers non-sensitive categories: communications, "
           "protection, uniforms, vehicles, surveillance tools, field gear, plus construction "
           "materials and plant.</p>"
           "<p>On drones, aircraft and detection systems we define purpose-based requirements. A "
           "commercial position as much as an ethical one: less complexity, faster delivery.</p>"),
          ("02. Anti-bribery and anti-corruption",
           "<p>Zero tolerance, including facilitation payments, written to satisfy Nigerian law "
           "and the standards our suppliers and partners are subject to.</p><ul>"
           "<li>No facilitation payments, any amount, any purpose</li>"
           "<li>Gifts registered above a low threshold, prohibited during a live procurement</li>"
           "<li>Third parties subject to due diligence before appointment</li>"
           "<li>A confidential reporting route, with published non-retaliation</li></ul>"),
          ("03. Procurement transparency",
           "<p>Buying on a client's behalf creates obvious risk. We manage it with "
           "documentation.</p><ul>"
           "<li>Prequalification criteria set and recorded before sourcing</li>"
           "<li>Competitive quotations retained, including unsuccessful ones</li>"
           "<li>Any supplier interest declared in writing beforehand</li>"
           "<li>The full procurement file handed to the client</li></ul>"),
          ("04. Safety, quality and sustainability",
           "<p>Readiness improves without compromising safety, quality, integrity or "
           "sustainability. In practice:</p><ul>"
           "<li>Multi-discipline design review with recorded close-out</li>"
           "<li>Inspection and test records assembled during construction</li>"
           "<li>Site safety as a delivery requirement, not a report</li></ul>"),
          ("05. Confidentiality and site security",
           "<p>Defence sites and drawings are sensitive. We handle information at the "
           "classification you set.</p><ul>"
           "<li>Personnel vetting before access, to the standard required</li>"
           "<li>Need-to-know handling of site information</li>"
           "<li>Defined retention and certified destruction at close</li></ul>"),
          ("06. Scope and focus",
           "<p>Our scope is deliberately defined, which is what lets us commit to it.</p><ul>"
           "<li>Advisory work stays within engineering, programme and procurement "
           "disciplines</li>"
           "<li>On any one facility we hold either the design and build role or the assurance "
           "role, and disclose any supplier interest in writing</li>"
           "<li>Where a client needs capability beyond our five pillars, we introduce a named "
           "partner and say so in the bid</li></ul>"),
      ])}
    </div>
  </section>

  <section class="section">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Raising a concern</p>
          <h2 class="d2">If we fall short</h2>
          <p class="lede mt-16">
            Anyone can report a concern about this firm or its personnel: a client officer, a
            supplier, our own staff, a member of the public. Reports may be anonymous.
          </p>
          <p class="mt-24">
            Confidential reporting: <a href="mailto:{EMAIL_ENQUIRIES}">{EMAIL_ENQUIRIES}</a><br>
            {TODO.format("dedicated reporting address, separate from general enquiries")}
          </p>
          <p class="mt-24">
            Concerns reach the Head of Compliance &amp; QA, who reports independently of delivery.
            No retaliation for anyone raising a concern in good faith.
          </p>
        </div>
        <div class="prose">
          <h2 class="mt-0">Documents</h2>
          <p>Each requires review by Nigerian counsel before publication.</p>
          <ul>
            <li><a href="{{P}}legal/anti-corruption-policy.html">Anti-bribery and anti-corruption</a></li>
            <li><a href="{{P}}legal/privacy-policy.html">Privacy and data protection</a></li>
            <li><a href="{{P}}legal/terms-of-use.html">Website terms of use</a></li>
            <li>Quality, health and safety, conflict of interest and whistleblowing policies,
                {TODO.format("to be drafted")}</li>
          </ul>
          <h2>Independent verification</h2>
          <p>
            External assessment beats self-certification.
            {TODO.format("confirm which certifications are held or being pursued, with timelines, or remove")}
          </p>
        </div>
      </div>
    </div>
  </section>

''' + cta_band(
        heading="Ask the hard question first",
        body="Raise the conflict, confidentiality or scope question at the outset. Cheaper now "
             "than later.")

    return ("about/integrity-and-compliance.html", "Integrity &amp; compliance",
            "The published integrity framework of Pinnacle Precision Engineering & Consulting: "
            "non-weaponized scope, anti-corruption, procurement transparency, safety and "
            "quality, and confidentiality.", body)


def insights():
    planned = [
        ("Modernization", "Why predictive maintenance beats more spares",
         "What condition monitoring changes on a vehicle fleet, and what it does not."),
        ("Construction", "Designing barracks for the real maintenance budget",
         "Whole-life specification choices that decide what a building costs to keep."),
        ("Supply chain", "Inventory visibility as a readiness intervention",
         "Stock you cannot see is stock you do not have."),
        ("Engineering", "Carrying BIM data past handover",
         "Where digital models lose their value, and how to stop it."),
        ("Industrialisation", "MRO first: the realistic route to Nigerian defence industry",
         "Why maintenance localisation precedes assembly, and assembly precedes design."),
    ]

    rows = "\n".join(
        f'''      <div class="list__item">
        <p class="list__meta">{cat}</p>
        <div><h3>{title}</h3><p>{blurb}</p></div>
        <p class="list__meta">{TODO.format("date")}</p>
      </div>''' for cat, title, blurb in planned
    )

    body = page_hero(
        "Insights",
        "Written analysis, published openly",
        "We publish our thinking on defence infrastructure because the arguments benefit from "
        "being tested, and because you should see how we reason before hiring us.",
        trail=[("Insights", None)],
    )

    body += f'''
  <section class="section section--tight">
    <div class="shell">
      <div class="notice">
        <p style="margin:0">
          <strong>Pipeline, not published work.</strong> These are in preparation. Nothing goes
          out until written, reviewed for confidentiality and factual accuracy, and cleared.
        </p>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">In preparation</p>
        <h2 class="d2">Forthcoming briefings</h2>
      </div>
      <div class="list">
{rows}
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Editorial standards</p>
          <h2 class="d2">What we publish</h2>
        </div>
        <div>
          {ruled([
              ("Nothing confidential",
               "No client information, site detail, security provision or drawing. Cleared before release."),
              ("Clients named only with consent",
               "Case studies are anonymised by default."),
              ("Analysis, not marketing",
               "If a piece has no falsifiable claim or usable method, it does not go out."),
              ("Illustrative figures labelled",
               "Where a number is a target rather than a measured result, we say so."),
          ])}
        </div>
      </div>
    </div>
  </section>

''' + cta_band()

    return ("insights/index.html", "Insights",
            "Analysis from Pinnacle Precision Engineering & Consulting on defence "
            "infrastructure, construction, supply chain and modernization.", body)


def careers():
    roles = [
        ("Senior Design Engineer, Structures", "Full time",
         "Structural design across defence facility projects, FEED through IFC.",
         ["Delivered structural packages through to construction",
          "Fluent in current codes, able to defend a calculation"]),
        ("MEP Engineer", "Full time",
         "Mechanical, electrical and plumbing design, including backup generation and protected "
         "distribution.",
         ["Building services design across mechanical and electrical",
          "Backup power and water system design"]),
        ("Construction / Project Manager", "Full time",
         "Site delivery, quality control, subcontractor management and commissioning.",
         ["Delivered on operational or access-controlled sites",
          "Rigorous on quality records and documentation"]),
        ("Supply Chain &amp; Procurement Lead", "Full time",
         "Vendor qualification, sourcing, logistics and inventory control.",
         ["Procurement with documented, auditable process",
          "Vendor qualification and performance management"]),
        ("BIM / Digital Engineering Specialist", "Full time",
         "BIM standards and model management, plus IoT and analytics for predictive maintenance.",
         ["BIM authoring and coordination at project scale",
          "Interested in carrying model data into operations"]),
    ]

    cards_html = []
    for i, (title, kind, blurb, reqs) in enumerate(roles, 1):
        req_html = "".join(f"<li>{r}</li>" for r in reqs)
        cards_html.append(f'''      <div class="acc__item">
        <h3><button class="acc__btn" aria-expanded="false" aria-controls="role-{i}">
          <span>{title}</span><span class="acc__sign" aria-hidden="true"></span>
        </button></h3>
        <div class="acc__body" id="role-{i}">
          <p style="font-family:var(--ff-mono);font-size:0.76rem;color:var(--brass)">{HQ} · {kind} · {TODO.format("closing date")}</p>
          <p>{blurb}</p>
          <p><strong>What we look for</strong></p>
          <ul>{req_html}</ul>
          <p style="margin-top:1em">Apply to <a href="mailto:{EMAIL_INFO}">{EMAIL_INFO}</a> with a
          CV and one page on a project you delivered and what you would do differently now.</p>
        </div>
      </div>''')

    body = page_hero(
        "Careers",
        "We hire people who have delivered real projects",
        "Engineering credibility comes from completed work. We would rather hire someone who "
        "finished a difficult project than someone who studied many.",
        trail=[("Careers", None)],
    )

    body += f'''
  <section class="section">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Working here</p>
          <h2 class="d2">What to expect</h2>
          <p class="lede mt-16">
            Defence work brings constraints commercial projects do not: vetting, controlled site
            access, confidentiality obligations, and documentation standards that are enforced.
          </p>
          <div class="notice mt-32">
            <p style="margin:0"><strong>Before publishing:</strong> confirm each role is open and
            funded, and set real closing dates.</p>
          </div>
        </div>
        <div>
          {ruled([
              ("Security vetting", f"Vetting appropriate to the sites you work on. {TODO.format('standard and process')}."),
              ("Professional registration", f"We support COREN registration and CPD. {TODO.format('confirm support')}."),
              ("Documentation", "Quality records, design comments and as-built accuracy are part of the job."),
              ("Site work", "Most roles involve time on site, including controlled locations."),
          ])}
        </div>
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Openings</p>
        <h2 class="d2">Current and planned roles</h2>
      </div>
      <div class="acc" data-acc>
{chr(10).join(cards_html)}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Recruitment integrity</p>
          <h2 class="d3">Applying is free</h2>
        </div>
        <div class="prose">
          <p>
            Recruitment with {LEGAL_NAME} is free at every stage: application, processing,
            vetting and placement. Any agent acting for us is paid by us.
          </p>
          <p>
            If anyone requests money in our name, it is a fraud. Report it to
            <a href="mailto:{EMAIL_ENQUIRIES}">{EMAIL_ENQUIRIES}</a>.
          </p>
        </div>
      </div>
    </div>
  </section>

''' + cta_band(
        heading="Nothing here fits?",
        body="Send a speculative application. We would rather know who is out there.")

    return ("careers/index.html", "Careers",
            "Engineering, construction, supply chain and digital engineering careers at "
            "Pinnacle Precision Engineering & Consulting in Abuja.", body)


def contact():
    body = page_hero(
        "Contact",
        "Ready to support defence readiness?",
        "Request a capability briefing, proposal discussion, partnership meeting or site "
        "assessment.",
        trail=[("Contact", None)],
    )

    body += f'''
  <section class="section">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Enquiry</p>
          <h2 class="d3">Send us an outline</h2>
          <p class="lede mt-16">
            Keep this form to unclassified information. Describe the requirement in general terms
            and we will arrange a secure channel before any detail is exchanged.
          </p>

          <form class="form mt-40" data-enquiry-form data-fallback-email="{EMAIL_ENQUIRIES}"
                method="post" novalidate>
            <div class="field--row">
              <div class="field">
                <label for="f-name">Full name</label>
                <input id="f-name" name="name" type="text" autocomplete="name" required>
              </div>
              <div class="field">
                <label for="f-org">Organisation</label>
                <input id="f-org" name="organisation" type="text" autocomplete="organization" required>
              </div>
            </div>
            <div class="field--row">
              <div class="field">
                <label for="f-email">Email</label>
                <input id="f-email" name="email" type="email" autocomplete="email" required>
              </div>
              <div class="field">
                <label for="f-phone">Phone</label>
                <input id="f-phone" name="phone" type="tel" autocomplete="tel">
              </div>
            </div>
            <div class="field">
              <label for="f-topic">Nature of enquiry</label>
              <select id="f-topic" name="topic" required>
                <option value="">Please select</option>
                <option>Capability briefing</option>
                <option>Proposal discussion</option>
                <option>Partnership meeting</option>
                <option>Site assessment</option>
                <option>Engineering design</option>
                <option>Military construction</option>
                <option>Defence supply chain</option>
                <option>Modernization consulting</option>
                <option>Sovereign cloud &amp; AI</option>
                <option>Supplier or subcontractor</option>
                <option>Careers</option>
                <option>Media</option>
                <option>Reporting a concern</option>
                <option>Other</option>
              </select>
            </div>
            <div class="field">
              <label for="f-msg">Outline of the requirement</label>
              <textarea id="f-msg" name="message" required></textarea>
              <p class="hint">Unclassified only. Two or three paragraphs is plenty.</p>
            </div>
            <label class="check">
              <input type="checkbox" name="consent" required>
              <span>This message contains no classified information, and I consent to my details
              being held per the <a href="{{P}}legal/privacy-policy.html">privacy policy</a>.</span>
            </label>
            <div>
              <button class="btn btn--primary" type="submit">Send enquiry {ARROW}</button>
            </div>
            <p class="notice" data-form-status tabindex="-1" hidden></p>
          </form>
        </div>

        <div>
          <p class="eyebrow">Direct</p>
          {ruled([
              ("Headquarters", f"{HQ}<br>{TODO.format('street address')}"),
              ("Enquiries", f'<a href="mailto:{EMAIL_ENQUIRIES}">{EMAIL_ENQUIRIES}</a>'),
              ("Information", f'<a href="mailto:{EMAIL_INFO}">{EMAIL_INFO}</a>'),
              ("Phone", f'<a href="tel:+16624979481">{PHONE}</a><br>{TODO.format("a Nigerian line is recommended")}'),
          ])}

          <div class="notice mt-32">
            <p style="margin:0">
              <strong>Sensitive material:</strong> keep this form and email to unclassified
              information. Classified handling is agreed with your security authority first.
            </p>
          </div>

          <div class="mt-40">
            <p class="eyebrow">Response times</p>
            <p class="lede">
              Acknowledgement within two working days, a substantive response within five.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">What happens next</p>
        <h2 class="d2">From enquiry to engagement</h2>
      </div>
      <div class="steps">
        <div class="step"><div><h3>Acknowledgement</h3></div>
          <p>We confirm receipt and name the senior person handling it.</p></div>
        <div class="step"><div><h3>Capability briefing</h3></div>
          <p>An unclassified discussion at no cost, so both sides can judge fit.</p></div>
        <div class="step"><div><h3>Site assessment</h3></div>
          <p>Where relevant and authorised, a visit to confirm site realities and risk.</p></div>
        <div class="step"><div><h3>Written proposal</h3></div>
          <p>Scope, deliverables, named personnel, programme, assumptions and fee basis, inside
          your procurement requirements.</p></div>
      </div>
    </div>
  </section>
'''

    return ("contact/index.html", "Contact",
            f"Contact Pinnacle Precision Engineering & Consulting in {HQ}: capability briefings, "
            "proposals, partnerships and site assessments.", body)


def _legal_page(slug, title, desc, intro, sections):
    body = page_hero("Legal", title, intro, trail=[(title, None)])
    parts = []
    for h, paras in sections:
        parts.append(f"<h2>{h}</h2>")
        parts.extend(paras)
    body += f'''
  <section class="section section--tight">
    <div class="shell shell--narrow">
      <div class="notice">
        <p style="margin:0">
          <strong>Draft requiring legal review.</strong> A structured starting point, not legal
          advice. Nigerian counsel must approve it, and check it against the Nigeria Data
          Protection Act where personal data is involved, before publication.
        </p>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="shell shell--narrow">
      <div class="prose">
        <p><strong>Updated:</strong> {TODO.format("date")} · <strong>Version:</strong> {TODO.format("version")}</p>
        {"".join(parts)}
        <h2>Contact</h2>
        <p>
          Questions to <a href="mailto:{EMAIL_ENQUIRIES}">{EMAIL_ENQUIRIES}</a>, {LEGAL_NAME},
          {TODO.format("registered office address")}.
        </p>
      </div>
    </div>
  </section>
'''
    return (f"legal/{slug}.html", title, desc, body)


def legal_pages():
    return [
        _legal_page(
            "privacy-policy", "Privacy policy",
            "How Pinnacle Precision Engineering & Consulting handles personal data.",
            "How we handle personal data, from this website and during engagements.",
            [
                ("Who we are", [
                    f"<p>{LEGAL_NAME} (RC {TODO.format('number')}), "
                    f"{TODO.format('registered office address')}, is the data controller. Data "
                    f"protection contact: {TODO.format('name and email')}.</p>"]),
                ("What we collect", [
                    "<p>Name, organisation, job title, email, telephone, the content of enquiries, "
                    "and technical information about your visit. On projects we may process data "
                    "on client personnel, subcontractors and site visitors, governed by the "
                    "engagement contract.</p>",
                    f"<p>{TODO.format('confirm exactly what the live site collects')}</p>"]),
                ("Why we process it", [
                    "<p>To answer enquiries, perform contracts, consider job applications, meet "
                    "legal and anti-corruption due diligence obligations, and send briefings to "
                    "people who ask for them.</p>",
                    f"<p>{TODO.format('state the lawful basis for each purpose under the NDPA')}</p>"]),
                ("Cookies and analytics", [
                    "<p>This site functions without non-essential cookies. If analytics are added, "
                    "a consent banner must be added with them.</p>",
                    f"<p>{TODO.format('list every cookie and analytics tool deployed')}</p>"]),
                ("Sharing", [
                    "<p>We share personal data only with service providers under contract, "
                    "professional advisers, and where required by law. It is never sold or "
                    "rented.</p>",
                    f"<p>{TODO.format('list processor categories once selected')}</p>"]),
                ("Retention and security", [
                    f"<p>{TODO.format('retention periods per data category')} Security measures "
                    "match the sensitivity of what we hold, including need-to-know access control "
                    "and vetting of personnel with access to site information.</p>"]),
                ("Your rights", [
                    "<p>Subject to law you may request access, correction, deletion, restriction, "
                    "objection and portability, and may withdraw consent where processing relies "
                    "on it.</p>",
                    f"<p>Contact {TODO.format('data protection contact')}. You may also complain "
                    "to the Nigeria Data Protection Commission.</p>"]),
                ("International transfers and changes", [
                    f"<p>{TODO.format('state whether data leaves Nigeria and the safeguards')}</p>",
                    "<p>Any change to this policy is posted here with a revised date.</p>"]),
            ]),

        _legal_page(
            "terms-of-use", "Terms of use",
            "Terms governing use of the Pinnacle Precision Engineering & Consulting website.",
            "The terms on which this website is made available.",
            [
                ("Acceptance", [
                    "<p>By using this website you accept these terms. Please read them before "
                    "continuing.</p>"]),
                ("Information is general", [
                    "<p>Content here describes our capabilities in general terms. It is not "
                    "engineering advice and not an offer. Advice is given only under a written "
                    "engagement contract, to the client named in it, on the facts stated in "
                    "it.</p>"]),
                ("Proposed applications", [
                    "<p>Applications and illustrative examples on this site are proposed for "
                    "discussion, not claims of completed contracts. Illustrative targets are "
                    "labelled as such, and results depend on scope and baseline conditions.</p>"]),
                ("No client relationship", [
                    "<p>An enquiry does not create a client relationship. That arises on execution "
                    "of a written engagement agreement.</p>"]),
                ("Sensitive information", [
                    "<p>Please keep submissions to this website and to email unclassified. We "
                    "accept no responsibility for material submitted contrary to this notice.</p>"]),
                ("Intellectual property", [
                    f"<p>Content is owned by {LEGAL_NAME} or its licensors. You may read, download "
                    "and quote published briefings with attribution. Republication in substantial "
                    "part, or commercial use, requires written permission.</p>"]),
                ("Third-party references", [
                    "<p>References to organisations, including government institutions and armed "
                    "services, describe the sectors we are equipped to work in. They assert no "
                    "contractual relationship, endorsement or affiliation unless stated.</p>"]),
                ("Limitation of liability", [
                    f"<p>{TODO.format('to be drafted by Nigerian counsel')}</p>"]),
                ("Governing law", [
                    "<p>These terms are governed by the laws of the Federal Republic of Nigeria. "
                    f"{TODO.format('confirm jurisdiction and dispute resolution with counsel')}</p>"]),
            ]),

        _legal_page(
            "anti-corruption-policy", "Anti-bribery &amp; anti-corruption policy",
            "The anti-bribery and anti-corruption policy of Pinnacle Precision Engineering & "
            "Consulting Limited.",
            "Our zero-tolerance policy, published in full because a firm bidding for public "
            "defence infrastructure should be held to it.",
            [
                ("Statement", [
                    f"<p>{LEGAL_NAME} prohibits bribery and corruption in every form, in every "
                    "jurisdiction, without exception. It applies to every director, employee, "
                    "contractor, agent and subcontractor acting for the firm.</p>",
                    "<p>Construction and procurement carry elevated corruption risk, and defence "
                    "adds confidentiality. That argues for stricter controls.</p>"]),
                ("Scope and standards", [
                    "<p>Written to comply with Nigerian anti-corruption law, including the Corrupt "
                    "Practices and Other Related Offences Act and the EFCC Act, and with the "
                    "extraterritorial standards our partners are subject to, including the UK "
                    "Bribery Act 2010 and the US FCPA.</p>",
                    f"<p>{TODO.format('confirm the full list of applicable statutes with counsel')}</p>"]),
                ("Prohibited conduct", [
                    "<p>Absolutely prohibited:</p>"
                    "<ul>"
                    "<li>Offering, giving, requesting or accepting any advantage to influence the "
                    "improper performance of a function</li>"
                    "<li>Facilitation payments, any amount, any purpose</li>"
                    "<li>Kickbacks, in cash, in kind, or as an inflated subcontract</li>"
                    "<li>Collusive tendering, bid rigging or cover pricing</li>"
                    "<li>Political contributions on behalf of the firm</li>"
                    "<li>Using an intermediary to do anything this policy prohibits</li>"
                    "</ul>"]),
                ("Procurement integrity, gifts and hospitality", [
                    "<p>Prequalification criteria set before sourcing. Competitive quotations "
                    "retained, including unsuccessful ones. Any supplier interest declared in "
                    "writing beforehand. The complete procurement file handed to the client.</p>",
                    "<p>Gifts and hospitality: modest, infrequent, recorded above a threshold of "
                    f"{TODO.format('amount')}, and prohibited entirely with any party connected to "
                    "a live procurement. Cash never.</p>"]),
                ("Third-party due diligence", [
                    "<p>Every agent, supplier, subcontractor and joint venture partner is subject "
                    "to risk-based due diligence before appointment: ownership, sanctions and "
                    "debarment screening, adverse media and integrity history. Anti-corruption "
                    "obligations and audit rights go into every contract we issue.</p>"]),
                ("Books, controls and training", [
                    "<p>All payments recorded with a stated business purpose. No undisclosed "
                    f"account, fund or asset. {TODO.format('name approval thresholds and controls')}</p>",
                    f"<p>All personnel trained on joining and {TODO.format('frequency')} "
                    "thereafter, with extra training for procurement roles.</p>"]),
                ("Reporting and non-retaliation", [
                    f"<p>Report concerns to the Head of Compliance &amp; QA at "
                    f'<a href="mailto:{EMAIL_ENQUIRIES}">{EMAIL_ENQUIRIES}</a> '
                    f"({TODO.format('dedicated channel to be established')}). Anonymous reports "
                    "accepted, from anyone.</p>",
                    "<p>No retaliation for a concern raised in good faith. A good-faith report "
                    "that turns out mistaken carries no consequence.</p>"]),
                ("Consequences and governance", [
                    "<p>Breach is grounds for dismissal or termination, reported to the authorities "
                    "where the law requires. We withdraw from a tender rather than participate in "
                    "prohibited conduct.</p>",
                    f"<p>Owned by the Head of Compliance &amp; QA, reviewed "
                    f"{TODO.format('frequency')} by the board.</p>"]),
            ]),
    ]


def not_found():
    body = f'''  <section class="hero hero--page">
    <div class="hero__bg"></div>
    <div class="shell">
      <div class="hero__body">
        <p class="eyebrow">Error 404</p>
        <h1 class="d1">That page is not here</h1>
        <p class="lede">
          The address may be mistyped, or the page may have moved.
        </p>
        <div class="hero__actions">
          <a class="btn btn--primary" href="{{P}}index.html">Return to home {ARROW}</a>
          <a class="btn btn--ghost" href="{{P}}contact/index.html">Contact us</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="shell">
      <div class="grid grid--4">
        <a class="card" href="{{P}}capabilities/index.html"><h3>Capabilities</h3>
          <p>Five defence-aligned pillars.</p></a>
        <a class="card" href="{{P}}sectors/index.html"><h3>Sectors</h3>
          <p>The institutions we support.</p></a>
        <a class="card" href="{{P}}roadmap/index.html"><h3>Roadmap</h3>
          <p>Our three-phase model.</p></a>
        <a class="card" href="{{P}}about/index.html"><h3>About</h3>
          <p>Who we are and how we work.</p></a>
      </div>
    </div>
  </section>
'''
    return ("404.html", "Page not found", "The page you requested could not be found.", body)


def all_company_pages():
    return [about_index(), leadership(), integrity(), insights(), careers(), contact(),
            not_found()] + legal_pages()
