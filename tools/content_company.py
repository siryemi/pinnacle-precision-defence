"""Company pages: about, leadership, integrity, insights, careers, contact, legal, 404.

Company facts come from pinnacle_precision_defense_profile.pptx. Anything still
unverified is a visible placeholder, tracked in CONTENT-TODO.md.
"""

from layout import (ARROW, ARROW_SM, page_hero, cta_band, link_arrow, ruled,
                    accordion, cards, DISCLAIMER, LEGAL_NAME, HQ, EMAIL_INFO,
                    EMAIL_ENQUIRIES, PHONE)

TODO = '<span class="todo">TODO: {}</span>'


def about_index():
    body = page_hero(
        "About us",
        "Fifteen years of engineering, construction and supply chain expertise",
        "Pinnacle Precision Engineering &amp; Consulting Limited is a Nigerian private "
        "engineering and construction firm. For defence stakeholders that experience "
        "translates into four focused capabilities — secure engineering design, reliable "
        "construction, disciplined supply chain management and modernization consulting — "
        "and a fifth built on top of them: sovereign cloud and AI infrastructure.",
        trail=[("About", None)],
    )

    body += f'''
  <section class="section">
    <div class="shell">
      <div class="split">
        <div class="prose">
          <p class="eyebrow">Company overview</p>
          <p>
            {LEGAL_NAME} is a Nigerian private engineering and construction firm founded by a
            team carrying more than fifteen years of combined industry experience, headquartered
            in {HQ} ({TODO.format("CAC registration number and date of incorporation")}).
          </p>
          <p>
            We are not a defence prime and we do not present ourselves as one. We are an
            engineering and construction business whose existing disciplines — design,
            build, procure, sustain — map directly onto what defence infrastructure and
            readiness programmes require. This site sets out that mapping.
          </p>

          <h2>Defence positioning statement</h2>
          <p>
            Mission-critical engineering and project-delivery support designed to improve
            readiness, harden infrastructure and strengthen defence logistics — without
            compromising safety, quality, integrity or sustainability.
          </p>

          <h2>Mission</h2>
          <p>
            To strengthen defence infrastructure and operational readiness by delivering secure
            engineering solutions, reliable construction, disciplined supply chains and
            strategic modernization consulting tailored to Nigeria's defence sector.
          </p>

          <h2>What we are careful about</h2>
          <p>
            Our supply chain and equipment work is deliberately scoped to
            <strong>non-weaponized</strong> categories — radios, protective equipment, tactical
            uniforms, vehicles, surveillance tools and similar. That is a commercial choice as
            much as an ethical one: it reduces procurement complexity, shortens approval paths
            and lets us deliver measurable readiness improvement quickly.
          </p>
          <p>
            Where we contribute to discussions about drones, aircraft or detection systems, our
            role is helping define purpose-based capability requirements — not providing
            operational guidance and not supplying weapons systems.
          </p>
        </div>

        <div>
          <p class="eyebrow">At a glance</p>
          {ruled([
              ("Legal entity", f"{LEGAL_NAME}. RC {TODO.format('number')}."),
              ("Headquarters", f"{HQ}. {TODO.format('registered office address')}."),
              ("Experience", "15+ years of combined founding-team industry experience."),
              ("Service lines", "Five defence-aligned pillars: engineering design, military construction, defence supply chain, modernization consulting, and sovereign cloud &amp; AI infrastructure."),
              ("Primary focus", "Nigerian Army infrastructure resilience, operational readiness and modernization."),
              ("Equipment scope", "Non-weaponized categories only. We do not supply weapons or ordnance."),
          ])}
          <div class="notice mt-32">
            <p style="margin:0"><strong>Pre-launch:</strong> items marked in gold require
            verified company facts before publication. See <code>CONTENT-TODO.md</code>.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="section-head section-head--wide">
        <p class="eyebrow">Value proposition</p>
        <h2 class="d2">Aligning project delivery with operational readiness</h2>
      </div>
      {cards([
          ("National security alignment",
           "Every engagement is scoped around readiness, resilience and operational continuity."),
          ("Operational efficiency",
           "Streamlined workflows that shorten time-to-readiness without cutting corners."),
          ("Innovation and digital readiness",
           "BIM, IoT and analytics brought into traditionally analogue defence infrastructure."),
          ("Partnership for long-term capability",
           "Built for repeat engagement and lifecycle support, not one-off delivery."),
      ], cols=4)}
    </div>
  </section>

  <section class="section" id="method">
    <div class="shell">
      <div class="split split--sticky">
        <div>
          <p class="eyebrow">Engagement model</p>
          <h2 class="d2">A practical path from needs assessment to lifecycle support</h2>
          <p class="lede mt-16">
            All work proceeds within the formal procurement, governance, security and
            confidentiality requirements set by the client.
          </p>
          <div class="actions mt-32">
            <a class="btn btn--ghost" href="{{P}}roadmap/index.html">The phased roadmap</a>
          </div>
        </div>
        <div class="steps">
          <div class="step"><div><h3>Assess</h3></div>
            <p>Confirm requirements, site realities, operational constraints and risk profile.
            Nothing starts on a verbal brief.</p></div>
          <div class="step"><div><h3>Design</h3></div>
            <p>Develop FEED, BIM/CAD and IFC packages, alongside cost logic and execution
            strategy — with the cost logic documented so it can be interrogated.</p></div>
          <div class="step"><div><h3>Deliver</h3></div>
            <p>Manage procurement, construction interfaces, quality controls and commissioning,
            assembling the evidence file as we go rather than afterwards.</p></div>
          <div class="step"><div><h3>Sustain</h3></div>
            <p>Support handover, training, asset data capture and maintenance-readiness planning,
            so the receiving unit can operate and maintain the asset unaided.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--ink2 section--line">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Delivery principles</p>
          <h2 class="d2">Secure-by-design, maintainable-by-design, audit-ready from day one</h2>
          <div class="actions mt-32">
            <a class="btn btn--ghost" href="{{P}}about/integrity-and-compliance.html">Integrity &amp; compliance</a>
            <a class="btn btn--ghost" href="{{P}}about/leadership.html">Leadership</a>
          </div>
        </div>
        <div>
          {ruled([
              ("Design for the maintenance budget that exists",
               "Specifying for durability and maintainability rather than lowest capital cost, because whole-life cost is what the client actually pays."),
              ("Build the evidence file during delivery",
               "Quality records, procurement trail and as-built documentation assembled as work proceeds, not reconstructed when someone asks."),
              ("Hand over something operable",
               "Training, asset data and manuals so the receiving organisation is not dependent on us to run what we built."),
              ("Say what is outside our scope",
               "Where a requirement falls outside the five pillars, we say so rather than stretching to cover it."),
          ])}
        </div>
      </div>
    </div>
  </section>

''' + cta_band()

    return ("about/index.html", "About us",
            "Pinnacle Precision Engineering & Consulting Limited is a Nigerian engineering and "
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
        "Engineering and construction is a business built on individual professional "
        "judgement. Clients are entitled to know exactly who is responsible for the design "
        "they are relying on and the project they are funding.",
        trail=[("About", "about/index.html"), ("Leadership", None)],
    )

    body += f'''
  <section class="section section--tight">
    <div class="shell">
      <div class="notice">
        <p style="margin:0">
          <strong>This page is a structural placeholder.</strong> Do not publish named
          biographies until each individual has confirmed their appointment in writing,
          approved their own biography, and had every claimed qualification, professional
          registration and project record independently verified. For an engineering firm this
          includes COREN registration and any professional body membership — these are checkable,
          and a defence client will check them.
        </p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Founding team</p>
        <h2 class="d2">Leadership team</h2>
        <p class="lede mt-16">
          The firm was founded by a team carrying more than fifteen years of combined industry
          experience across engineering, construction and supply chain management.
        </p>
      </div>
      <div class="grid grid--3">
{person("Managing Director", "Overall accountability for the firm, its client relationships and delivery performance.")}
{person("Director, Engineering", "Design authority across engineering packages, and owner of the design review process.")}
{person("Director, Construction", "Delivery, site management, quality control and commissioning.")}
{person("Head of Supply Chain", "Vendor qualification, sourcing, logistics and inventory discipline.")}
{person("Head of Modernization &amp; Digital", "BIM, IoT, analytics and asset management workstreams.")}
{person("Head of Compliance &amp; QA", "Quality management, anti-corruption controls and audit readiness. Reports independently of delivery lines.")}
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Credentials to publish</p>
          <h2 class="d2">What a defence client will ask for</h2>
          <p class="lede mt-16">
            For an engineering and construction firm bidding into defence work, these are the
            documents that get requested first. Publishing them is a competitive advantage;
            claiming them without holding them is fatal.
          </p>
        </div>
        <div>
          {ruled([
              ("CAC incorporation", f"Certificate and RC number. {TODO.format('obtain and publish')}"),
              ("COREN registration", f"Council for the Regulation of Engineering in Nigeria registration for the firm and named engineers. {TODO.format('confirm status')}"),
              ("Professional indemnity insurance", f"Cover level and insurer. {TODO.format('confirm cover')}"),
              ("Quality management certification", f"ISO 9001 or equivalent, if held or being pursued. {TODO.format('confirm status and timeline')}"),
              ("Health and safety record", f"Safety management system and incident record. {TODO.format('confirm')}"),
              ("BPP contractor registration", f"Bureau of Public Procurement registration and category. {TODO.format('confirm registration')}"),
              ("Project references", f"Completed civil and engineering projects with client permission to cite. {TODO.format('assemble reference list')}"),
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
            "The leadership team of Pinnacle Precision Engineering & Consulting Limited, and "
            "the credentials a defence client should expect to see.", body)


def integrity():
    body = page_hero(
        "Integrity &amp; compliance",
        "How we work, and the limits we hold to",
        "Defence infrastructure spend attracts scrutiny, and it should. We set out our "
        "controls publicly so a client, a partner or an auditor can hold us to them.",
        trail=[("About", "about/index.html"), ("Integrity &amp; compliance", None)],
    )

    body += f'''
  <section class="section">
    <div class="shell shell--narrow">
      <div class="prose">
        <p class="eyebrow">Position</p>
        <p>
          Construction and procurement are among the highest corruption-risk activities in any
          economy, and defence spending compounds that risk with confidentiality. Nigeria's own
          institutional reforms — the Public Procurement Act, the Bureau of Public Procurement,
          and active legislative and audit oversight — exist because of it.
        </p>
        <p>
          A firm that intends to build defence infrastructure and run defence supply chains has
          an obligation to state its controls plainly. What follows is reflected in our
          engagement letters and staff terms. Where we fall short of it, we would rather be told.
        </p>
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Framework</p>
        <h2 class="d2">Six commitments</h2>
      </div>
      {accordion("integrity", [
          ("01 — Non-weaponized scope",
           "<p>Our equipment and supply chain work covers non-sensitive, non-weaponized "
           "categories: radios and communications equipment, body armour and protective "
           "equipment, tactical uniforms, vehicles, surveillance tools, field gear, and "
           "construction materials, plant and services.</p>"
           "<p>We do not supply, broker, transport or finance weapons, ammunition or ordnance. "
           "Where we support capability requirement discussions involving drones, aircraft or "
           "detection systems, our role is defining purpose-based requirements and technical "
           "specifications — not supplying weapons systems and not providing operational "
           "guidance.</p>"
           "<p>This is a deliberate commercial position as well as an ethical one: it reduces "
           "procurement complexity and shortens the path from requirement to delivered "
           "capability.</p>"),
          ("02 — Anti-bribery and anti-corruption",
           "<p>Zero tolerance, including facilitation payments. Our policy is written to satisfy "
           "Nigerian law and the standards our international suppliers and partners are "
           "themselves subject to.</p><ul>"
           "<li>No facilitation payments, in any amount, for any purpose</li>"
           "<li>Gifts and hospitality registered above a low threshold and prohibited entirely "
           "during a live procurement</li>"
           "<li>Agents, subcontractors and suppliers subject to due diligence before "
           "appointment</li>"
           "<li>A confidential reporting route open to staff, client personnel, suppliers and "
           "the public, with a published non-retaliation commitment</li></ul>"),
          ("03 — Procurement transparency",
           "<p>Our defence supply chain work makes us a buyer on our clients' behalf, which "
           "creates an obvious risk. We manage it with documentation rather than assurance.</p>"
           "<ul>"
           "<li>Vendor prequalification criteria set and recorded before sourcing begins</li>"
           "<li>Competitive quotations retained, including unsuccessful ones</li>"
           "<li>Any interest in a supplier declared in writing before that supplier is "
           "considered</li>"
           "<li>Traceability and quality-assurance records on everything supplied</li>"
           "<li>Full procurement file handed to the client, not retained as leverage</li></ul>"),
          ("04 — Safety, quality and sustainability",
           "<p>Our positioning statement commits to improving readiness without compromising "
           "safety, quality, integrity or sustainability. In practice:</p><ul>"
           "<li>Structured multi-discipline design review with recorded comments and close-out</li>"
           "<li>Inspection and test records assembled during construction, not compiled "
           "afterwards</li>"
           "<li>Site safety management as a delivery requirement, not a reporting exercise</li>"
           "<li>Specification for durability and maintainability against the client's real "
           "maintenance budget</li></ul>"),
          ("05 — Confidentiality and site security",
           "<p>Defence sites and drawings are sensitive. We handle client information at the "
           "classification the client sets.</p><ul>"
           "<li>Personnel vetting to the standard the engagement requires, arranged before "
           "access</li>"
           "<li>Need-to-know handling of site information, drawings and security provisions</li>"
           "<li>No site photography, drawings or client identification used in marketing without "
           "written permission</li>"
           "<li>Defined retention and certified destruction at engagement close</li></ul>"),
          ("06 — Scope limits we hold to",
           "<p>Stating what we do not do is part of being trusted with what we do.</p><ul>"
           "<li>We do not supply, broker or finance weapons, ammunition or ordnance</li>"
           "<li>We do not provide armed personnel, guarding or close protection, and we are not "
           "a private military or security company</li>"
           "<li>We do not provide operational or tactical advice to commanders</li>"
           "<li>We do not develop surveillance or interception systems for use against "
           "civilians</li>"
           "<li>We do not act as both adviser to a buyer and interested supplier in the same "
           "procurement without written disclosure and the client's express agreement</li></ul>"),
      ])}
    </div>
  </section>

  <section class="section">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Raising a concern</p>
          <h2 class="d2">If you believe we have fallen short</h2>
          <p class="lede mt-16">
            Anyone — a client officer, a supplier, a member of our staff or a member of the
            public — can report a concern about the conduct of this firm or its personnel.
            Reports may be made anonymously.
          </p>
          <p class="mt-24">
            Confidential reporting: <a href="mailto:{EMAIL_ENQUIRIES}">{EMAIL_ENQUIRIES}</a><br>
            {TODO.format("dedicated confidential reporting address, separate from general enquiries")}
          </p>
          <p class="mt-24">
            Concerns are received by the Head of Compliance &amp; QA, who reports independently
            of delivery lines. We commit publicly to no retaliation against anyone raising a
            concern in good faith.
          </p>
        </div>
        <div class="prose">
          <h2 class="mt-0">Documents</h2>
          <p>Each requires review by Nigerian counsel before this site goes live.</p>
          <ul>
            <li><a href="{{P}}legal/anti-corruption-policy.html">Anti-bribery and anti-corruption policy</a></li>
            <li><a href="{{P}}legal/privacy-policy.html">Privacy and data protection policy</a></li>
            <li><a href="{{P}}legal/terms-of-use.html">Website terms of use</a></li>
            <li>Quality management policy — {TODO.format("to be drafted and published")}</li>
            <li>Health and safety policy — {TODO.format("to be drafted and published")}</li>
            <li>Conflict of interest policy — {TODO.format("to be drafted and published")}</li>
            <li>Whistleblowing policy — {TODO.format("to be drafted and published")}</li>
          </ul>
          <h2>Independent verification</h2>
          <p>
            We would rather be externally assessed than self-certify.
            {TODO.format("confirm which certifications are held or being pursued — e.g. ISO 9001 quality, ISO 45001 safety, ISO 37001 anti-bribery — with real timelines, or remove this section")}
          </p>
        </div>
      </div>
    </div>
  </section>

''' + cta_band(
        heading="Ask us the hard question first",
        body="If you are considering engaging us, raise the conflict, confidentiality or scope "
             "question at the outset. It is a cheaper conversation now than later.")

    return ("about/integrity-and-compliance.html", "Integrity &amp; compliance",
            "The published integrity framework of Pinnacle Precision Engineering & Consulting: "
            "non-weaponized scope, anti-corruption, procurement transparency, safety and "
            "quality, confidentiality, and the work we decline.", body)


def insights():
    planned = [
        ("Modernization", "Why predictive maintenance beats more spares for vehicle availability",
         "What condition monitoring actually changes on a vehicle fleet, and what it does not."),
        ("Construction", "Designing barracks for the maintenance budget that will actually exist",
         "Whole-life specification decisions that determine what a building costs to keep."),
        ("Supply chain", "Inventory visibility as a readiness intervention",
         "Why stock you cannot see is functionally stock you do not have."),
        ("Engineering", "Carrying BIM data past handover",
         "Where digital models lose their value, and how to structure them so they do not."),
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
        "We publish our thinking on defence infrastructure and readiness because the arguments "
        "benefit from being tested in public — and because a client is entitled to see how we "
        "reason before they hire us.",
        trail=[("Insights", None)],
    )

    body += f'''
  <section class="section section--tight">
    <div class="shell">
      <div class="notice">
        <p style="margin:0">
          <strong>Editorial pipeline, not published work.</strong> These are the briefings in
          preparation. Nothing should be presented as published until it has been written,
          reviewed for client confidentiality and factual accuracy, and cleared internally.
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
          <h2 class="d2">What we will and will not publish</h2>
        </div>
        <div>
          {ruled([
              ("Nothing confidential, ever",
               "No client information, site detail, security provision or drawing appears in published work. Every piece is cleared against this before release."),
              ("No client named without written consent",
               "Case studies are anonymised by default. A client is named only with explicit written permission."),
              ("Analysis, not marketing",
               "If a piece contains no falsifiable claim or usable method, it does not go out under our name."),
              ("Illustrative figures labelled as such",
               "Where a number is a target or an illustration rather than a measured result, we say so on the page."),
              ("Corrections published",
               "Where we get something wrong, the correction appears on the same page as the original."),
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
        ("Senior Design Engineer — Structures", HQ, "Full time",
         "Structural design across defence facility projects, from FEED through IFC. Suited to "
         "an experienced structural engineer with building and civil works background.",
         ["Delivered structural packages through to construction",
          "Fluent in current design codes and able to defend a calculation",
          "COREN registered or eligible for registration",
          "Comfortable designing for maintainability, not just compliance"]),
        ("MEP Engineer", HQ, "Full time",
         "Mechanical, electrical and plumbing design including backup generation, water systems "
         "and protected distribution for facilities where downtime is not acceptable.",
         ["Building services design experience across mechanical and electrical",
          "Backup power and water system design",
          "Able to coordinate MEP within a multi-discipline BIM model",
          "Understands resilience as a design requirement"]),
        ("Construction / Project Manager", HQ, "Full time",
         "Site delivery, quality control, subcontractor management and commissioning on "
         "defence and civil projects.",
         ["Delivered projects on operational or access-controlled sites",
          "Rigorous on quality records and documentation discipline",
          "Strong safety management record",
          "Able to sequence work so a live site keeps functioning"]),
        ("Supply Chain & Procurement Lead", HQ, "Full time",
         "Vendor qualification, sourcing, logistics coordination and inventory control across "
         "projects and equipment categories.",
         ["Procurement experience with documented, auditable process",
          "Vendor qualification and performance management",
          "Import, warehousing and distribution logistics",
          "Uncompromising on procurement transparency"]),
        ("BIM / Digital Engineering Specialist", HQ, "Full time",
         "BIM standards and model management, plus IoT and analytics workstreams supporting "
         "predictive maintenance.",
         ["BIM authoring and coordination at project scale",
          "Interest in carrying model data into operations",
          "Data analysis skills for condition monitoring",
          "Able to train non-specialists to use what you build"]),
    ]

    cards_html = []
    for i, (title, loc, kind, blurb, reqs) in enumerate(roles, 1):
        req_html = "".join(f"<li>{r}</li>" for r in reqs)
        cards_html.append(f'''      <div class="acc__item">
        <h3><button class="acc__btn" aria-expanded="false" aria-controls="role-{i}">
          <span>{title}</span><span class="acc__sign" aria-hidden="true"></span>
        </button></h3>
        <div class="acc__body" id="role-{i}">
          <p style="font-family:var(--ff-mono);font-size:0.76rem;color:var(--brass)">{loc} · {kind} · {TODO.format("closing date")}</p>
          <p>{blurb}</p>
          <p><strong>What we are looking for</strong></p>
          <ul>{req_html}</ul>
          <p style="margin-top:1em">Apply to <a href="mailto:{EMAIL_INFO}">{EMAIL_INFO}</a> with a
          CV and a one-page note on a project you delivered and what you would do differently
          now. {TODO.format("confirm whether a dedicated recruitment address should be used instead")}</p>
        </div>
      </div>''')

    body = page_hero(
        "Careers",
        "We hire people who have delivered real projects",
        "Engineering and construction credibility comes from completed work. We would rather "
        "hire someone who has finished a difficult project than someone who has studied many.",
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
            Defence work brings constraints most commercial projects do not: vetting, controlled
            site access, confidentiality obligations and documentation standards that are
            genuinely enforced.
          </p>
          <div class="notice mt-32">
            <p style="margin:0"><strong>Before publishing:</strong> confirm each role is
            genuinely open and funded, and set real closing dates. Advertising roles that do not
            exist is a reputational cost a young firm cannot afford.</p>
          </div>
        </div>
        <div>
          {ruled([
              ("Security vetting", f"Personnel complete vetting appropriate to the sites they work on. {TODO.format('confirm standard and process')}."),
              ("Professional registration", f"We support COREN registration and continuing professional development. {TODO.format('confirm support offered')}."),
              ("Documentation discipline", "Quality records, design review comments and as-built accuracy are part of the job, not an afterthought."),
              ("Site work", "Most roles involve time on site, including operational and access-controlled locations."),
              ("Knowledge transfer", "You will be expected to make client teams independent of you. That is the job."),
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
          <h2 class="d3">We charge nothing to apply</h2>
        </div>
        <div class="prose">
          <p>
            {LEGAL_NAME} never charges a fee at any stage of recruitment, and never asks a
            candidate for payment for training, processing, vetting or placement. We do not use
            recruitment agents who charge candidates.
          </p>
          <p>
            If anyone requests money in our name, it is a fraud. Please report it to
            <a href="mailto:{EMAIL_ENQUIRIES}">{EMAIL_ENQUIRIES}</a>.
          </p>
        </div>
      </div>
    </div>
  </section>

''' + cta_band(
        heading="Nothing here fits, but you think we should talk?",
        body="Send a speculative application. We would rather know who is out there than fill "
             "a role badly.")

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
            Please do not include classified, security-sensitive or site-specific protective
            detail in this form. Describe the requirement in general terms and we will arrange
            an appropriately secure channel before any detail is exchanged.
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
                <option>Defence engineering design</option>
                <option>Military construction</option>
                <option>Defence supply chain</option>
                <option>Modernization consulting</option>
                <option>Supplier or subcontractor enquiry</option>
                <option>Careers</option>
                <option>Media enquiry</option>
                <option>Reporting a concern</option>
                <option>Other</option>
              </select>
            </div>
            <div class="field">
              <label for="f-msg">Outline of the requirement</label>
              <textarea id="f-msg" name="message" required></textarea>
              <p class="hint">Unclassified information only. Two or three paragraphs is plenty.</p>
            </div>
            <label class="check">
              <input type="checkbox" name="consent" required>
              <span>I confirm this message contains no classified or security-sensitive
              information, and I consent to my details being held in accordance with the
              <a href="{{P}}legal/privacy-policy.html">privacy policy</a>.</span>
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
              ("Headquarters", f"{HQ}<br>{TODO.format('registered office street address')}"),
              ("General enquiries", f'<a href="mailto:{EMAIL_ENQUIRIES}">{EMAIL_ENQUIRIES}</a>'),
              ("Information", f'<a href="mailto:{EMAIL_INFO}">{EMAIL_INFO}</a>'),
              ("Phone", f'<a href="tel:+16624979481">{PHONE}</a><br>{TODO.format("a Nigerian line is recommended for Nigerian defence clients")}'),
              ("Media", f'{EMAIL_INFO} — we respond to media enquiries but do not comment on client engagements.'),
              ("Reporting a concern", "Received by the Head of Compliance &amp; QA. Anonymous reports accepted."),
          ])}

          <div class="notice mt-32">
            <p style="margin:0">
              <strong>Handling sensitive material:</strong> we do not accept classified or
              security-sensitive material by email or through this website. Where an engagement
              requires it, handling arrangements are agreed with the client's own security
              authority first.
            </p>
          </div>

          <div class="mt-40">
            <p class="eyebrow">Response times</p>
            <p class="lede">
              We aim to acknowledge every enquiry within two working days and to give a
              substantive response — including a straight no where appropriate — within five.
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
          <p>We confirm receipt and identify the senior person handling the enquiry.</p></div>
        <div class="step"><div><h3>Capability briefing</h3></div>
          <p>An unclassified discussion of the requirement, at no cost. If we are not the right
          firm, we say so here.</p></div>
        <div class="step"><div><h3>Site assessment</h3></div>
          <p>Where relevant and authorised, a visit to confirm site realities, constraints and
          risk profile before anything is proposed.</p></div>
        <div class="step"><div><h3>Written proposal</h3></div>
          <p>Scope, deliverables, named personnel, programme, assumptions and fee basis — in
          writing, within the client's procurement requirements, before work starts.</p></div>
      </div>
    </div>
  </section>
'''

    return ("contact/index.html", "Contact",
            f"Contact Pinnacle Precision Engineering & Consulting in {HQ} — capability "
            "briefings, proposals, partnerships and site assessments.", body)


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
          <strong>Draft requiring legal review.</strong> This document is a structured starting
          point, not legal advice. It must be reviewed and approved by Nigerian counsel — and
          checked against the Nigeria Data Protection Act where personal data is involved —
          before publication. Do not publish as-is.
        </p>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="shell shell--narrow">
      <div class="prose">
        <p><strong>Last updated:</strong> {TODO.format("date")} · <strong>Version:</strong> {TODO.format("version")}</p>
        {"".join(parts)}
        <h2>Contact</h2>
        <p>
          Questions about this document should be directed to
          <a href="mailto:{EMAIL_ENQUIRIES}">{EMAIL_ENQUIRIES}</a>, {LEGAL_NAME},
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
            "How Pinnacle Precision Engineering & Consulting collects, uses and protects "
            "personal data.",
            "How we handle personal data, including data collected through this website and in "
            "the course of client engagements.",
            [
                ("Who we are", [
                    f"<p>{LEGAL_NAME} (RC {TODO.format('number')}), "
                    f"{TODO.format('registered office address')}, is the data controller for "
                    "personal data described in this policy. Our data protection contact is "
                    f"{TODO.format('name and email')}.</p>"]),
                ("What we collect", [
                    "<p>Through this website and our business activities we may collect: name, "
                    "organisation, job title, email address, telephone number, the content of "
                    "enquiries you send us, and technical information about your visit.</p>",
                    f"<p>{TODO.format('confirm exactly what the live site collects — analytics, cookies, form data — and list only that')}</p>",
                    "<p>On projects we may process personal data relating to client personnel, "
                    "subcontractors and site visitors. That processing is governed by the "
                    "engagement contract and the client's instructions as controller.</p>"]),
                ("Why we process it", [
                    "<p>To respond to enquiries; to perform contracts; to consider job "
                    "applications; to meet legal, regulatory, procurement and anti-corruption "
                    "due diligence obligations; and to send briefings to people who have asked "
                    "for them.</p>",
                    f"<p>{TODO.format('state the lawful basis for each purpose under the Nigeria Data Protection Act')}</p>"]),
                ("Cookies and analytics", [
                    f"<p>{TODO.format('list every cookie and analytics tool actually deployed, its purpose and retention; add a consent mechanism if any non-essential cookie is used')}</p>",
                    "<p>This site is built to function without non-essential cookies. If "
                    "analytics are added, this section and a consent banner must be added with "
                    "them.</p>"]),
                ("Sharing", [
                    "<p>We do not sell personal data. We share it only with service providers "
                    "under contract, professional advisers, and where required by law or lawful "
                    "request.</p>",
                    f"<p>{TODO.format('list categories of processors once selected — hosting, email, CRM')}</p>"]),
                ("Retention and security", [
                    f"<p>{TODO.format('state retention periods per data category')}</p>",
                    "<p>We apply technical and organisational security measures appropriate to "
                    "the sensitivity of the information we hold, including access control on a "
                    "need-to-know basis and vetting of personnel with access to sensitive site "
                    "information.</p>"]),
                ("Your rights", [
                    "<p>Subject to applicable law you may request access to your personal data, "
                    "correction, deletion, restriction of processing, objection to processing, "
                    "and portability. You may withdraw consent where processing relies on it.</p>",
                    f"<p>To exercise a right, contact {TODO.format('data protection contact')}. "
                    "You may also complain to the Nigeria Data Protection Commission.</p>"]),
                ("International transfers", [
                    f"<p>{TODO.format('state whether data leaves Nigeria — relevant for cloud hosting and email — and the safeguards applied')}</p>"]),
                ("Changes", [
                    "<p>We will post any change to this policy on this page with a revised "
                    "update date.</p>"]),
            ]),

        _legal_page(
            "terms-of-use", "Terms of use",
            "Terms governing use of the Pinnacle Precision Engineering & Consulting website.",
            "The terms on which this website is made available.",
            [
                ("Acceptance", [
                    "<p>By using this website you accept these terms. If you do not accept them, "
                    "please do not use the site.</p>"]),
                ("Information is general", [
                    "<p>Content on this site describes our capabilities in general terms. It is "
                    "not engineering advice, it does not constitute an offer, and it should not "
                    "be relied upon in making any decision. Engineering advice is given only "
                    "under a written engagement contract, to the client named in it, on the "
                    "facts and assumptions stated in it.</p>"]),
                ("Proposed applications", [
                    "<p>Applications, use cases and illustrative examples described on this site "
                    "are proposed defence applications for discussion purposes. They do not "
                    "represent claims of completed contracts with the Nigerian Army or any other "
                    "organisation. Illustrative targets and examples are labelled as such and "
                    "actual results depend on scope and baseline conditions.</p>"]),
                ("No client relationship", [
                    "<p>Sending an enquiry through this site does not create a client "
                    "relationship. A relationship arises only on execution of a written "
                    "engagement agreement.</p>"]),
                ("Do not send sensitive information", [
                    "<p>Do not submit classified, restricted or security-sensitive information "
                    "through this website or by unencrypted email. We accept no responsibility "
                    "for material submitted contrary to this warning.</p>"]),
                ("Intellectual property", [
                    "<p>All content on this site is owned by "
                    f"{LEGAL_NAME} or its licensors. You may read, download and quote published "
                    "briefings with attribution. You may not republish content in substantial "
                    "part, or use it commercially, without written permission.</p>"]),
                ("Third-party references", [
                    "<p>References to organisations, including government institutions and armed "
                    "services, are descriptive of the sectors in which we are equipped to work. "
                    "They do not assert an existing contractual relationship, endorsement or "
                    "affiliation unless expressly stated.</p>"]),
                ("Limitation of liability", [
                    f"<p>{TODO.format('liability wording to be drafted by Nigerian counsel — do not publish a generic clause')}</p>"]),
                ("Governing law", [
                    "<p>These terms are governed by the laws of the Federal Republic of Nigeria. "
                    f"{TODO.format('confirm jurisdiction and dispute resolution clause with counsel')}</p>"]),
            ]),

        _legal_page(
            "anti-corruption-policy", "Anti-bribery &amp; anti-corruption policy",
            "The anti-bribery and anti-corruption policy of Pinnacle Precision Engineering & "
            "Consulting Limited.",
            "Our zero-tolerance policy on bribery and corruption, published in full because a "
            "firm bidding for public defence infrastructure work should be held to it.",
            [
                ("Statement", [
                    f"<p>{LEGAL_NAME} prohibits bribery and corruption in every form, in every "
                    "jurisdiction, without exception and regardless of commercial consequence. "
                    "This policy applies to every director, employee, contractor, agent and "
                    "subcontractor acting for or on behalf of the firm.</p>",
                    "<p>Construction and procurement carry elevated corruption risk, and defence "
                    "spending compounds it with confidentiality. We treat that as a reason for "
                    "stricter controls than a general commercial business would apply, not as an "
                    "excuse for market practice.</p>"]),
                ("Scope and standards", [
                    "<p>This policy is written to comply with Nigerian anti-corruption law, "
                    "including the Corrupt Practices and Other Related Offences Act and the "
                    "Economic and Financial Crimes Commission Act, and with the extraterritorial "
                    "standards our international suppliers and partners are subject to, "
                    "including the UK Bribery Act 2010 and the US Foreign Corrupt Practices "
                    "Act.</p>",
                    f"<p>{TODO.format('confirm the full list of applicable statutes with Nigerian counsel')}</p>"]),
                ("Prohibited conduct", [
                    "<p>The following are prohibited absolutely:</p>",
                    "<ul>"
                    "<li>Offering, giving, requesting or accepting any financial or other "
                    "advantage to influence the improper performance of a function</li>"
                    "<li>Facilitation payments of any amount, for any purpose, including to "
                    "expedite a permit, inspection, clearance or routine administrative "
                    "action</li>"
                    "<li>Kickbacks, whether in cash, in kind, or as an inflated subcontract</li>"
                    "<li>Collusive tendering, bid rigging or cover pricing</li>"
                    "<li>Political contributions made on behalf of the firm</li>"
                    "<li>Charitable donations used as a route to improper influence</li>"
                    "<li>Using an agent, consultant, subcontractor or intermediary to do "
                    "anything this policy prohibits</li></ul>"]),
                ("Procurement integrity", [
                    "<p>Because we procure on our clients' behalf, we apply specific controls: "
                    "prequalification criteria set before sourcing; competitive quotations "
                    "retained including unsuccessful ones; written declaration of any interest "
                    "in a supplier before that supplier is considered; and the complete "
                    "procurement file handed to the client.</p>"]),
                ("Gifts and hospitality", [
                    "<p>Gifts and hospitality must be modest, infrequent, transparent and "
                    f"recorded in the firm's register above a threshold of "
                    f"{TODO.format('threshold amount')}. Gifts and hospitality to or from any "
                    "party connected to a live procurement or tender in which we are involved "
                    "are prohibited entirely. Cash and cash equivalents may never be given or "
                    "accepted.</p>"]),
                ("Third-party due diligence", [
                    "<p>Every agent, intermediary, supplier, subcontractor and joint venture "
                    "partner is subject to risk-based due diligence before appointment, covering "
                    "ownership, sanctions and debarment screening, adverse media and integrity "
                    "history. Anti-corruption obligations and audit rights are written into "
                    "every contract we issue.</p>"]),
                ("Books, records and controls", [
                    "<p>All payments are accurately recorded with a stated business purpose. No "
                    "undisclosed or unrecorded account, fund or asset may be established for any "
                    "purpose.</p>",
                    f"<p>{TODO.format('name the approval thresholds and financial controls actually in place')}</p>"]),
                ("Training", [
                    f"<p>All personnel receive anti-corruption training on joining and "
                    f"{TODO.format('frequency')} thereafter, with additional training for those "
                    "working on procurement and tendering.</p>"]),
                ("Reporting and non-retaliation", [
                    f"<p>Concerns must be reported to the Head of Compliance &amp; QA at "
                    f"<a href=\"mailto:{EMAIL_ENQUIRIES}\">{EMAIL_ENQUIRIES}</a> "
                    f"({TODO.format('dedicated confidential reporting channel to be established')}). "
                    "Reports may be made anonymously and may be made by anyone, including client "
                    "personnel, suppliers and members of the public.</p>",
                    "<p>The firm will not retaliate against anyone who raises a concern in good "
                    "faith, and will treat any attempt to do so as a disciplinary matter. A "
                    "report made in good faith that turns out to be mistaken carries no "
                    "consequence for the person who made it.</p>"]),
                ("Consequences", [
                    "<p>Breach of this policy is grounds for dismissal or termination of "
                    "contract, and will be reported to the relevant authorities where the law "
                    "requires or the circumstances warrant. We will withdraw from a tender or "
                    "terminate an engagement rather than participate in conduct this policy "
                    "prohibits.</p>"]),
                ("Governance", [
                    f"<p>This policy is owned by the Head of Compliance &amp; QA, who reports "
                    f"independently of delivery lines, and is reviewed "
                    f"{TODO.format('review frequency')} by the board.</p>"]),
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
          The address may be mistyped, or the page may have moved. The main sections of the
          site are below.
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
          <p>Four defence-aligned capability pillars.</p></a>
        <a class="card" href="{{P}}sectors/index.html"><h3>Sectors</h3>
          <p>The institutions we support.</p></a>
        <a class="card" href="{{P}}roadmap/index.html"><h3>Roadmap</h3>
          <p>Our three-phase engagement model.</p></a>
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
