"""Company pages: about, leadership, integrity, insights, careers, contact, legal, 404."""

from layout import ARROW, ARROW_SM, page_hero, cta_band, link_arrow, breadcrumb

TODO = '<span class="todo">TODO: {}</span>'


def _ruled(rows):
    out = ['<div class="ruled">']
    for h, p in rows:
        out.append(f'      <div class="ruled__row"><h3>{h}</h3><p>{p}</p></div>')
    out.append("    </div>")
    return "\n".join(out)


def _acc(acc_id, items):
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


# --------------------------------------------------------------------------- #
def about_index():
    body = page_hero(
        "About us",
        "A Nigerian defence advisory firm, built to be needed less over time",
        "Pinnacle Precision Defence exists to strengthen the capability of the institutions "
        "responsible for Nigeria's defence and security — by improving how they define "
        "requirements, buy equipment, train their people and sustain what they own.",
        trail=[("About", None)],
    )

    body += f'''
  <section class="section">
    <div class="shell">
      <div class="split">
        <div class="prose">
          <p class="eyebrow">Who we are</p>
          <p>
            Pinnacle Precision Defence Limited is an independent defence and security advisory
            firm incorporated in Nigeria ({TODO.format("CAC registration number and date")}),
            headquartered in Abuja. We work for the Ministry of Defence, the Defence
            Headquarters, the three services, national security agencies and the domestic
            defence industrial base.
          </p>
          <p>
            We are a consultancy. Our product is analysis, written advice, designed processes
            and trained people. We do not manufacture, broker, source or supply defence
            equipment, we hold no agency or distribution agreement with any manufacturer, and
            we accept no commission or success fee from any supplier. That independence is the
            basis on which a client can act on our recommendation about what to buy.
          </p>

          <h2>Why the firm exists</h2>
          <p>
            Nigeria does not have a defence capability problem that can be solved by buying
            more equipment. It has a capability problem that runs through requirement
            definition, acquisition discipline, training design and — above all —
            sustainment. Equipment arrives without the spares, technicians or doctrine to use
            it properly. Requirements are written as product descriptions. Support costs
            surface years after the purchase decision that committed to them.
          </p>
          <p>
            That analysis is not novel, and it is not unique to Nigeria. What is missing is
            resident, independent analytical capacity that understands both the international
            body of practice in defence capability management and the specific legal,
            institutional and operational reality of Nigeria. That is the gap this firm is
            built to fill.
          </p>

          <h2>How we are different from the alternatives</h2>
          <p>
            <strong>Against a foreign consultancy:</strong> we are resident, we understand the
            Public Procurement Act and the institutions that operate it, our costs are in naira,
            and we are accountable in-country. We are not flying in for a six-week diagnostic.
          </p>
          <p>
            <strong>Against a supplier's advisory arm:</strong> we have no equipment to sell,
            so our options analysis can honestly conclude that the answer is better training,
            more spares, or no purchase at all.
          </p>
          <p>
            <strong>Against a general management consultancy:</strong> our people have worked
            in defence — in operations, in engineering, in acquisition. Defence capability
            management is a specialist discipline and we treat it as one.
          </p>
        </div>

        <div>
          <p class="eyebrow">At a glance</p>
          {_ruled([
              ("Legal entity", f"Pinnacle Precision Defence Limited, incorporated in Nigeria. RC {TODO.format('number')}."),
              ("Headquarters", f"Abuja, Federal Capital Territory. {TODO.format('registered office address')}."),
              ("Founded", TODO.format("year of incorporation")),
              ("People", f"{TODO.format('headcount')} consultants and vetted associates."),
              ("Clients", "Nigerian defence and security institutions and the domestic defence industrial base. References provided confidentially."),
              ("What we do not do", "Manufacture, broker, source or supply equipment. Accept supplier commission. Provide armed or close-protection services."),
          ])}
          <div class="notice mt-32">
            <p style="margin:0"><strong>Pre-launch:</strong> items marked in gold require
            verified company facts before this site is published. See
            <code>CONTENT-TODO.md</code>.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--paper" id="method">
    <div class="shell">
      <div class="section-head section-head--wide">
        <p class="eyebrow">Method</p>
        <h2 class="d2">How an engagement runs</h2>
        <p class="lede mt-16">
          The same five stages apply whether the engagement is a two-week review or a
          multi-year programme. The client owns the output, the evidence and the decision
          at every stage.
        </p>
      </div>
      <div class="steps">
        <div class="step"><div><h3>Scoping and clearance</h3></div>
          <p>We agree the question, the deliverables, the classification handling regime, the
          personnel to be vetted and the access required — in writing, before fieldwork begins.
          If we do not believe we are the right firm for the problem, this is where we say so.</p></div>
        <div class="step"><div><h3>Baseline assessment</h3></div>
          <p>Structured interviews, document review and, where authorised, site and unit visits.
          We produce an evidenced picture of the current state including the parts that are
          uncomfortable, and we distinguish clearly between what we verified and what we were told.</p></div>
        <div class="step"><div><h3>Options and trade-offs</h3></div>
          <p>Costed, comparable options against the requirement — each with its risks, its
          sustainment burden, its dependency on foreign support and its implementation timeline
          stated. Including, where it is the honest answer, the option of doing nothing.</p></div>
        <div class="step"><div><h3>Decision support</h3></div>
          <p>We brief at the level that decides. Recommendations are written to be defensible in
          front of an auditor or a legislative committee, with assumptions exposed and
          dissenting views inside our own team recorded rather than smoothed over.</p></div>
        <div class="step"><div><h3>Implementation and handover</h3></div>
          <p>Programme support through delivery, paired with a knowledge transfer obligation to
          the client's own staff. Every engagement specifies what the client's team will be able
          to do unaided at the end of it.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Principles</p>
          <h2 class="d2">Four things we hold to</h2>
          <div class="actions mt-32">
            <a class="btn btn--ghost" href="{{P}}about/integrity-and-compliance.html">Integrity &amp; compliance</a>
            <a class="btn btn--ghost" href="{{P}}about/leadership.html">Leadership</a>
          </div>
        </div>
        <div>
          {_ruled([
              ("Say the unwelcome thing early",
               "The cost of an uncomfortable finding rises with every month it is deferred. We would rather lose a follow-on contract than sign off analysis we do not believe."),
              ("Independence in writing, not in principle",
               "No supplier commission, no agency agreements, declared conflicts of interest for every named individual on an engagement."),
              ("Transfer the capability",
               "Every engagement carries a knowledge transfer obligation. If the client cannot run the process unaided afterwards, the job is not finished."),
              ("Evidence over assertion",
               "Sources cited, assumptions stated, and a clear line drawn between what we verified and what we were told."),
          ])}
        </div>
      </div>
    </div>
  </section>

''' + cta_band()

    return ("about/index.html", "About us",
            "Pinnacle Precision Defence is an independent Nigerian defence advisory firm based "
            "in Abuja, supporting the Armed Forces and security agencies across capability "
            "management.", body)


# --------------------------------------------------------------------------- #
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
        <div class="card__tags">
          <span class="card__tag">{TODO.format("background")}</span>
        </div>
      </div>'''

    body = page_hero(
        "Leadership",
        "The people accountable for the advice",
        "Defence advisory is a business built on individual judgement and individual "
        "credibility. Clients are entitled to know exactly who is responsible for what "
        "they are being told.",
        trail=[("About", "about/index.html"), ("Leadership", None)],
    )

    body += f'''
  <section class="section section--tight">
    <div class="shell">
      <div class="notice">
        <p style="margin:0">
          <strong>This page is a structural placeholder.</strong> Named biographies must not be
          published until each individual has confirmed their appointment in writing and
          approved their own biography, and until any claimed rank, appointment, qualification
          or professional membership has been verified. Overstating a leadership team's
          credentials is the single most damaging error a new defence advisory firm can make.
          See <code>CONTENT-TODO.md</code>.
        </p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Executive</p>
        <h2 class="d2">Leadership team</h2>
      </div>
      <div class="grid grid--3">
{person("Chief Executive Officer", "Overall accountability for the firm, its client relationships and the quality of its advice.")}
{person("Director, Capability &amp; Acquisition", "Leads requirements, procurement and capability development engagements.")}
{person("Director, Sustainment &amp; Engineering", "Leads availability engineering, MRO and technical assurance work.")}
{person("Director, Training &amp; Doctrine", "Leads curriculum, exercise design and doctrine engagements.")}
{person("Head of Compliance &amp; Risk", "Owns conflict-of-interest screening, due diligence and the engagement acceptance process. Reports independently of fee-earning lines.")}
{person("Head of Operations", "Contracting, security vetting administration, and delivery assurance.")}
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Governance</p>
          <h2 class="d2">Advisory board</h2>
          <p class="lede mt-16">
            An advisory board provides external challenge on engagement acceptance, ethical
            questions and technical quality. Its members are not employees and hold no
            executive authority.
          </p>
          <p class="mt-24">Composition intended to include: {TODO.format("proposed advisory board composition — e.g. retired senior officer, procurement law practitioner, defence engineer, human rights or civil society figure")}.</p>
        </div>
        <div class="prose">
          <h2 class="mt-0">Why an external board matters here</h2>
          <p>
            A defence consultancy faces decisions its own commercial interest cannot be trusted
            to resolve: whether to accept an engagement with human rights exposure, whether a
            conflict of interest is manageable, whether a client is asking for analysis or for
            cover. Those decisions need someone in the room who does not depend on the fee.
          </p>
          <p>
            The board's terms of reference, once appointed, will be published on this site,
            including its power to require an engagement be declined.
          </p>
          <p>{link_arrow("Read our integrity and compliance framework", "about/integrity-and-compliance.html")}</p>
        </div>
      </div>
    </div>
  </section>

''' + cta_band(
        heading="Interested in joining?",
        body="We recruit people who have done the job — in operations, engineering, "
             "acquisition or training.")

    return ("about/leadership.html", "Leadership",
            "The leadership team and advisory board of Pinnacle Precision Defence.", body)


# --------------------------------------------------------------------------- #
def integrity():
    body = page_hero(
        "Integrity &amp; compliance",
        "The work we will not take, and why we say so publicly",
        "Defence consulting carries specific, well-documented risks: conflicted advice, "
        "facilitation payments, and analysis that ends up enabling conduct a client would "
        "not defend in public. We manage those in writing.",
        trail=[("About", "about/index.html"), ("Integrity &amp; compliance", None)],
    )

    body += f'''
  <section class="section">
    <div class="shell shell--narrow">
      <div class="prose">
        <p class="eyebrow">Position</p>
        <p>
          Defence and security is among the highest corruption-risk sectors in the world, on
          the assessment of every major international index. Nigeria's own institutional
          reforms — the Public Procurement Act, the Bureau of Public Procurement, and active
          legislative and audit oversight — exist because of that risk. A firm that intends to
          advise on defence acquisition in this environment has an obligation to state its own
          controls plainly, and to accept being held to them.
        </p>
        <p>
          What follows is our published position. It is reflected in our engagement letters and
          in our staff terms of employment. Where we fall short of it, we would rather be told.
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
      {_acc("integrity", [
          ("01 — No supplier interest, ever",
           "<p>We accept no commission, agency fee, finder's fee, success fee, retainer or "
           "gift from any manufacturer, supplier, distributor or intermediary whose products "
           "or services we might assess or whose bid we might evaluate. Our entire fee income "
           "comes from clients.</p><ul>"
           "<li>We hold no agency, representation or distribution agreements</li>"
           "<li>We do not broker, source, import or resell equipment of any kind</li>"
           "<li>Staff and associates declare outside interests annually and per engagement</li>"
           "<li>Where a conflict cannot be eliminated, we decline the engagement rather than "
           "manage it with an information barrier</li></ul>"),
          ("02 — Anti-bribery and anti-corruption",
           "<p>Zero tolerance, including facilitation payments. Our policy is written to satisfy "
           "Nigerian law and the standards our international clients and partners are themselves "
           "subject to, including the UK Bribery Act 2010 and the US Foreign Corrupt Practices "
           "Act.</p><ul>"
           "<li>No facilitation payments, in any amount, for any purpose</li>"
           "<li>Gifts and hospitality registered above a low threshold and prohibited entirely "
           "during a live procurement</li>"
           "<li>Third parties, agents and subcontractors subject to due diligence before "
           "appointment</li>"
           "<li>A confidential reporting route available to staff and to client personnel, with "
           "a published non-retaliation commitment</li></ul>"),
          ("03 — Human rights and end-use screening",
           "<p>Every prospective engagement is screened for human rights risk before acceptance. "
           "We assess what our analysis would be used for, by whom, and what it would "
           "foreseeably enable.</p><ul>"
           "<li>We decline work where our output would foreseeably contribute to unlawful use "
           "of force, arbitrary detention, or the targeting of civilians or lawful dissent</li>"
           "<li>Training and doctrine work we design incorporates the law of armed conflict and "
           "applicable human rights standards as assessed competencies</li>"
           "<li>We will state in writing, to the client, where we believe a proposed course of "
           "action carries legal risk</li>"
           "<li>Screening decisions are recorded and reviewed by the compliance function, "
           "independently of the fee-earning team</li></ul>"),
          ("04 — Classification and information security",
           "<p>We handle client information at the classification the client sets, and we "
           "retain nothing beyond the agreed period.</p><ul>"
           "<li>Personnel security vetting to the standard the engagement requires, arranged "
           "before access is granted</li>"
           "<li>Strict need-to-know within our own team</li>"
           "<li>Client data held in client-approved systems and locations; no unapproved cloud "
           "storage or personal devices</li>"
           "<li>Defined retention and certified destruction at engagement close</li>"
           "<li>No client name, logo or engagement detail used in marketing without written "
           "permission</li></ul>"),
          ("05 — Export control and technology transfer",
           "<p>Technical advisory work can itself constitute a controlled transfer of "
           "technology. Engagements involving foreign-origin technical data are screened "
           "against applicable export control regimes before work begins, and structured so "
           "that neither we nor the client is placed in breach.</p>"),
          ("06 — Scope limits we hold to",
           "<p>There is work adjacent to ours that we do not do, and stating it publicly is "
           "part of being trusted with the work we do.</p><ul>"
           "<li>We do not supply, broker, transport or finance weapons, ammunition, platforms "
           "or dual-use equipment</li>"
           "<li>We do not provide armed personnel, close protection or any operational security "
           "service, and we are not a private military company</li>"
           "<li>We do not develop offensive cyber capability, intrusion tooling or "
           "communications interception systems</li>"
           "<li>We do not conduct or advise on influence operations directed at domestic "
           "populations, and we do not undertake political consulting</li>"
           "<li>We do not participate in a procurement as both adviser to the buyer and "
           "adviser to a bidder — in any form, at any remove</li></ul>"),
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
            Confidential reporting address: {TODO.format("dedicated reporting email address")}<br>
            Reporting line: {TODO.format("dedicated reporting phone number")}
          </p>
          <p class="mt-24">
            Concerns are received by the Head of Compliance &amp; Risk, who reports to the
            board independently of any fee-earning line. We commit publicly to no retaliation
            against anyone raising a concern in good faith.
          </p>
        </div>
        <div class="prose">
          <h2 class="mt-0">Documents</h2>
          <p>
            The following policies are published in full. Each requires review by Nigerian
            counsel before this site goes live.
          </p>
          <ul>
            <li><a href="{{P}}legal/anti-corruption-policy.html">Anti-bribery and anti-corruption policy</a></li>
            <li><a href="{{P}}legal/privacy-policy.html">Privacy and data protection policy</a></li>
            <li><a href="{{P}}legal/terms-of-use.html">Website terms of use</a></li>
            <li>Conflict of interest policy — {TODO.format("to be drafted and published")}</li>
            <li>Human rights and engagement acceptance policy — {TODO.format("to be drafted and published")}</li>
            <li>Whistleblowing policy — {TODO.format("to be drafted and published")}</li>
          </ul>
          <h2>Independent verification</h2>
          <p>
            We intend to seek external assessment of our compliance programme rather than rely
            on self-assertion. Target frameworks and certification bodies:
            {TODO.format("e.g. ISO 37001 anti-bribery management systems; Transparency International Defence Companies Index — confirm intent and timeline before publishing")}.
          </p>
        </div>
      </div>
    </div>
  </section>

''' + cta_band(
        heading="Ask us the hard question first",
        body="If you are considering engaging us, raise the conflict, classification or "
             "end-use question at the outset. It is a cheaper conversation now than later.")

    return ("about/integrity-and-compliance.html", "Integrity &amp; compliance",
            "Pinnacle Precision Defence's published integrity framework: no supplier interest, "
            "anti-corruption, human rights and end-use screening, classification handling, "
            "export control, and the work we decline.", body)


# --------------------------------------------------------------------------- #
def insights():
    planned = [
        ("Sustainment", "Why availability, not acquisition, is Nigeria's binding defence constraint",
         "Working through what a mission-capable rate actually depends on, and why the support "
         "budget is the wrong place to economise."),
        ("Procurement", "Writing a defence requirement that a tender can be built on",
         "The difference between a requirement and a product description, and what the "
         "difference costs at contract award."),
        ("Maritime", "Detection is not interdiction: the response gap in Gulf of Guinea security",
         "Why additional sensors rarely improve outcomes without the response and prosecution "
         "chain behind them."),
        ("Industry", "Offsets that transfer capability, and offsets that transfer nothing",
         "Assessing what a technology transfer arrangement actually conveys — design authority, "
         "data rights, or assembly work."),
        ("Training", "Training designed against the threat rather than the syllabus",
         "How training needs analysis changes a curriculum, and what it takes to sustain the "
         "change after the consultants leave."),
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
        "We publish our thinking on Nigerian defence capability because the arguments benefit "
        "from being tested in public — and because a client is entitled to see how we reason "
        "before they hire us.",
        trail=[("Insights", None)],
    )

    body += f'''
  <section class="section section--tight">
    <div class="shell">
      <div class="notice">
        <p style="margin:0">
          <strong>Editorial pipeline, not published work.</strong> The items below are the
          briefings currently in preparation. Nothing should be presented as published until it
          has been written, reviewed for classification and factual accuracy, and cleared by
          the compliance function. Do not publish placeholder analysis under the firm's name.
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
          {_ruled([
              ("Nothing classified, ever",
               "No client information, operational detail or classified material appears in published work. Every piece is cleared against this before release."),
              ("No client named without written consent",
               "Case studies are anonymised by default. A client is named only with explicit written permission."),
              ("Analysis, not marketing",
               "If a piece does not contain a falsifiable claim or a usable method, it does not go out under our name."),
              ("Sources cited",
               "Public sources are referenced. Where an assertion rests on our own engagement experience, we say so and describe its limits."),
              ("Corrections published",
               "Where we get something wrong, the correction is published on the same page as the original."),
          ])}
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="shell shell--narrow center">
      <p class="eyebrow eyebrow--plain">Stay informed</p>
      <h2 class="d3">Briefing distribution list</h2>
      <p class="lede center mt-16">
        New briefings are circulated to a distribution list of defence and security
        professionals. {TODO.format("subscription mechanism — mailing platform and privacy notice required before enabling")}
      </p>
      <div class="actions mt-32" style="justify-content:center">
        <a class="btn btn--primary" href="{{P}}contact/index.html">Ask to be added {ARROW}</a>
      </div>
    </div>
  </section>

''' + cta_band()

    return ("insights/index.html", "Insights",
            "Published analysis from Pinnacle Precision Defence on Nigerian defence capability, "
            "procurement, sustainment and training.", body)


# --------------------------------------------------------------------------- #
def careers():
    roles = [
        ("Principal Consultant — Capability &amp; Acquisition", "Abuja", "Full time",
         "Leads requirement definition and acquisition engagements. Suited to a former "
         "acquisition or programme officer, or a defence procurement practitioner with "
         "experience of the Public Procurement Act.",
         ["Written a requirement or business case that went through formal approval",
          "Understands whole-life costing well enough to defend a model line by line",
          "Able to brief at service headquarters or ministerial level",
          "Will state an unwelcome finding to a client in writing"]),
        ("Senior Consultant — Sustainment &amp; Engineering", "Abuja", "Full time",
         "Availability engineering and MRO work across land, sea and air fleets. Suited to a "
         "former military engineering officer or a defence maintenance and logistics "
         "professional.",
         ["Hands-on background in aircraft, vessel or vehicle maintenance management",
          "Comfortable building and defending an availability model",
          "Understands spares provisioning and levels-of-repair analysis",
          "Willing to spend time in workshops and depots, not only in meetings"]),
        ("Senior Consultant — Training &amp; Doctrine", "Abuja", "Full time",
         "Curriculum, exercise and simulation design for training establishments and "
         "formations. Suited to a former instructor, training development officer or doctrine "
         "writer.",
         ["Has designed a course or exercise that was actually delivered",
          "Fluent in training needs analysis and assessment design",
          "Can develop instructors, not merely deliver lessons",
          "Understands how doctrine, training and operational lessons connect"]),
        ("Analyst — Defence Programmes", "Abuja", "Full time",
         "Analytical support across engagements: data gathering, modelling, document review "
         "and drafting. An entry route for strong analysts without a defence background.",
         ["Rigorous quantitative and written work under time pressure",
          "Able to build a clean, documented model another person can audit",
          "Writes concisely and distinguishes evidence from inference",
          "Discretion — this work involves sensitive client information"]),
        ("Associate network — all disciplines", "Nigeria-wide", "Associate",
         "We maintain a vetted associate network of specialists engaged per project: retired "
         "senior officers, engineers, legal practitioners, cyber specialists and regional "
         "experts.",
         ["Deep specialism with a verifiable record",
          "Available for defined project periods",
          "Willing to complete security vetting and conflict-of-interest declarations",
          "Comfortable with our no-supplier-interest rule, which applies to associates too"]),
    ]

    cards = []
    for i, (title, loc, kind, blurb, reqs) in enumerate(roles, 1):
        req_html = "".join(f"<li>{r}</li>" for r in reqs)
        cards.append(f'''      <div class="acc__item">
        <h3><button class="acc__btn" aria-expanded="false" aria-controls="role-{i}">
          <span>{title}</span><span class="acc__sign" aria-hidden="true"></span>
        </button></h3>
        <div class="acc__body" id="role-{i}">
          <p style="font-family:var(--ff-mono);font-size:0.76rem;color:var(--brass)">{loc} · {kind} · {TODO.format("closing date")}</p>
          <p>{blurb}</p>
          <p><strong>What we are looking for</strong></p>
          <ul>{req_html}</ul>
          <p style="margin-top:1em">Apply to {TODO.format("recruitment email address")} with a CV and a
          one-page note on a capability problem you have worked on and what you would do
          differently now.</p>
        </div>
      </div>''')

    body = page_hero(
        "Careers",
        "We hire people who have done the job",
        "Operational, engineering, acquisition and training experience counts for more here "
        "than a consulting background. We can teach the analytical method; we cannot teach "
        "twenty years in a workshop or an operations room.",
        trail=[("Careers", None)],
    )

    body += f'''
  <section class="section">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Who we recruit</p>
          <h2 class="d2">Three routes in</h2>
          <p class="lede mt-16">
            Retired and transitioning officers and warrant officers. Defence engineers,
            logisticians and procurement specialists. And strong analysts at the start of
            their careers who want to learn this discipline properly.
          </p>
          <div class="notice mt-32">
            <p style="margin:0"><strong>Before publishing:</strong> confirm each vacancy is
            genuinely open and funded, and set a real closing date and application address.
            Advertising roles that do not exist is a reputational cost this firm cannot
            afford.</p>
          </div>
        </div>
        <div>
          {_ruled([
              ("Security vetting", f"All personnel complete vetting appropriate to the engagements they support. {TODO.format('vetting standard and process')}."),
              ("Conflict of interest", "Every member of staff and every associate declares outside interests on joining, annually, and per engagement."),
              ("Knowledge transfer", "You will be expected to make client staff independent of you. That is the job, not a threat to it."),
              ("Writing", "Everyone here writes. Clear written analysis is a core competence at every level, and it is assessed at interview."),
              ("Development", f"Structured professional development in defence capability management. {TODO.format('training budget and framework')}."),
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
{chr(10).join(cards)}
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
            Pinnacle Precision Defence never charges a fee at any stage of recruitment, and
            never asks a candidate for payment for training, processing, vetting or placement.
            We do not use recruitment agents who charge candidates.
          </p>
          <p>
            If anyone requests money in our name, it is a fraud. Please report it to
            {TODO.format("reporting email address")}.
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
            "Careers at Pinnacle Precision Defence — consulting, engineering, training and "
            "analytical roles in Abuja, plus a vetted associate network.", body)


# --------------------------------------------------------------------------- #
def contact():
    body = page_hero(
        "Contact",
        "Start with a scoping conversation",
        "Tell us the capability problem in outline. We will tell you honestly whether it is "
        "one we are equipped to help with, and what a first phase would involve.",
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
            Please do not include classified or operationally sensitive information in this
            form. Describe the problem in general terms and we will arrange an appropriately
            secure channel before any detail is exchanged.
          </p>

          <form class="form mt-40" data-enquiry-form data-fallback-email="the enquiries address above"
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
                <option>Defence strategy &amp; policy</option>
                <option>Capability development</option>
                <option>Procurement &amp; acquisition</option>
                <option>Training, doctrine &amp; simulation</option>
                <option>ISR &amp; C4I</option>
                <option>Sustainment &amp; MRO</option>
                <option>Cyber &amp; information defence</option>
                <option>Border &amp; maritime security</option>
                <option>Defence industry / OEM market entry</option>
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
              <span>I confirm this message contains no classified or operationally sensitive
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
          {_ruled([
              ("Headquarters", f"Abuja, Federal Capital Territory<br>{TODO.format('registered office address')}"),
              ("General enquiries", f"{TODO.format('enquiries email')}<br>{TODO.format('switchboard number')}"),
              ("New business", TODO.format("business development email")),
              ("Careers", TODO.format("recruitment email")),
              ("Media", f"{TODO.format('press email')} — we respond to media enquiries but do not comment on client engagements."),
              ("Reporting a concern", f"{TODO.format('confidential reporting email')} — received by the Head of Compliance &amp; Risk. Anonymous reports accepted."),
          ])}

          <div class="notice mt-32">
            <p style="margin:0">
              <strong>Handling sensitive material:</strong> we do not accept classified material
              by email or through this website. Where an engagement requires it, handling
              arrangements are agreed with the client's own security authority first.
              {TODO.format("state accepted secure channels once established")}
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
          <p>We confirm receipt and identify the senior person who will handle the enquiry.</p></div>
        <div class="step"><div><h3>Initial conversation</h3></div>
          <p>An unclassified discussion of the problem, at no cost. If we are not the right
          firm, we say so here and, where we can, suggest who might be.</p></div>
        <div class="step"><div><h3>Acceptance screening</h3></div>
          <p>Before we propose, the engagement is screened for conflicts of interest, human
          rights exposure and export control implications by the compliance function.</p></div>
        <div class="step"><div><h3>Written proposal</h3></div>
          <p>Scope, deliverables, named personnel, timeline, assumptions, fee basis and the
          knowledge transfer obligation — in writing, before any work starts.</p></div>
      </div>
    </div>
  </section>
'''

    return ("contact/index.html", "Contact",
            "Contact Pinnacle Precision Defence in Abuja — enquiries, new business, careers, "
            "media and confidential reporting.", body)


# --------------------------------------------------------------------------- #
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
          point, not legal advice, and it must be reviewed and approved by Nigerian counsel —
          and checked against the Nigeria Data Protection Act where personal data is involved —
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
          Questions about this document should be directed to {TODO.format("compliance contact email")},
          Pinnacle Precision Defence Limited, {TODO.format("registered office address")}.
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
            "How Pinnacle Precision Defence collects, uses, stores and protects personal data.",
            "How we handle personal data, including data collected through this website and in "
            "the course of client engagements.",
            [
                ("Who we are", [
                    f"<p>Pinnacle Precision Defence Limited (RC {TODO.format('number')}), "
                    f"{TODO.format('registered office address')}, is the data controller for "
                    "personal data described in this policy. Our data protection contact is "
                    f"{TODO.format('DPO or contact name and email')}.</p>"]),
                ("What we collect", [
                    "<p>Through this website and our business activities we may collect: name, "
                    "organisation, job title, email address, telephone number, the content of "
                    "enquiries you send us, and technical information about your visit.</p>",
                    f"<p>{TODO.format('confirm exactly what the live site collects — analytics, cookies, form data, mailing list — and list only that')}</p>",
                    "<p>In the course of engagements we may process personal data relating to "
                    "client personnel. That processing is governed by the engagement contract "
                    "and by the client's own instructions as controller.</p>"]),
                ("Why we process it", [
                    "<p>To respond to enquiries; to perform contracts; to consider job "
                    "applications; to comply with legal, regulatory and anti-corruption due "
                    "diligence obligations; and to send briefings to people who have asked for "
                    "them.</p>",
                    f"<p>{TODO.format('state the lawful basis for each purpose under the Nigeria Data Protection Act')}</p>"]),
                ("Cookies and analytics", [
                    f"<p>{TODO.format('list every cookie and analytics tool actually deployed, its purpose and retention; add a consent mechanism if any non-essential cookie is used')}</p>",
                    "<p>This site is built to function without non-essential cookies. If "
                    "analytics are added, this section and a consent banner must be added with "
                    "them.</p>"]),
                ("Sharing", [
                    "<p>We do not sell personal data. We share it only with service providers "
                    "under contract, professional advisers, and where required by law or "
                    "lawful request.</p>",
                    f"<p>{TODO.format('list categories of processors once selected — hosting, email, CRM, mailing platform')}</p>"]),
                ("Retention and security", [
                    f"<p>{TODO.format('state retention periods per data category')}</p>",
                    "<p>We apply technical and organisational security measures appropriate to "
                    "the sensitivity of the information we hold, including access control on a "
                    "need-to-know basis and vetting of personnel with access to sensitive "
                    "material.</p>"]),
                ("Your rights", [
                    "<p>Subject to applicable law you may request access to your personal data, "
                    "correction of inaccurate data, deletion, restriction of processing, "
                    "objection to processing, and portability. You may also withdraw consent "
                    "where processing relies on it.</p>",
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
            "Terms governing use of the Pinnacle Precision Defence website.",
            "The terms on which this website is made available.",
            [
                ("Acceptance", [
                    "<p>By using this website you accept these terms. If you do not accept "
                    "them, please do not use the site.</p>"]),
                ("Information is general", [
                    "<p>Content on this site describes our services in general terms. It is "
                    "not advice, it does not constitute an offer, and it should not be relied "
                    "upon in making any decision. Advice is given only under a written "
                    "engagement contract, to the client named in it, on the facts stated in "
                    "it.</p>"]),
                ("No client relationship", [
                    "<p>Sending an enquiry through this site does not create a client "
                    "relationship. A relationship arises only on execution of a written "
                    "engagement agreement.</p>"]),
                ("Do not send sensitive information", [
                    "<p>Do not submit classified, restricted or operationally sensitive "
                    "information through this website or by unencrypted email. We accept no "
                    "responsibility for material submitted contrary to this warning.</p>"]),
                ("Intellectual property", [
                    "<p>All content on this site, including text, graphics, diagrams and "
                    "published briefings, is owned by Pinnacle Precision Defence Limited or "
                    "its licensors. You may read, download and quote briefings with "
                    "attribution. You may not republish content in substantial part, or use it "
                    "commercially, without written permission.</p>"]),
                ("Third-party references", [
                    "<p>References to organisations, including government institutions, are "
                    "descriptive of the sectors in which we are equipped to work. They do not "
                    "assert an existing contractual relationship, endorsement or affiliation "
                    "unless expressly stated.</p>"]),
                ("Limitation of liability", [
                    f"<p>{TODO.format('liability wording to be drafted by Nigerian counsel — do not publish a generic clause')}</p>"]),
                ("Governing law", [
                    "<p>These terms are governed by the laws of the Federal Republic of "
                    f"Nigeria. {TODO.format('confirm jurisdiction and dispute resolution clause with counsel')}</p>"]),
            ]),

        _legal_page(
            "anti-corruption-policy", "Anti-bribery &amp; anti-corruption policy",
            "The anti-bribery and anti-corruption policy of Pinnacle Precision Defence.",
            "Our zero-tolerance policy on bribery and corruption, published in full because a "
            "defence advisory firm should be held to it.",
            [
                ("Statement", [
                    "<p>Pinnacle Precision Defence Limited prohibits bribery and corruption in "
                    "every form, in every jurisdiction, without exception and regardless of "
                    "commercial consequence. This policy applies to every director, employee, "
                    "associate, contractor and agent acting for or on behalf of the firm.</p>",
                    "<p>The defence sector carries elevated corruption risk. We treat that as "
                    "a reason for stricter controls than a general commercial business would "
                    "apply, not as an excuse for market practice.</p>"]),
                ("Scope and standards", [
                    "<p>This policy is written to comply with Nigerian anti-corruption law, "
                    "including the Corrupt Practices and Other Related Offences Act and the "
                    "Economic and Financial Crimes Commission Act, and with the extraterritorial "
                    "standards our international clients and partners are subject to, including "
                    "the UK Bribery Act 2010 and the US Foreign Corrupt Practices Act.</p>",
                    f"<p>{TODO.format('confirm the full list of applicable statutes with Nigerian counsel')}</p>"]),
                ("Prohibited conduct", [
                    "<p>The following are prohibited absolutely:</p>",
                    "<ul>"
                    "<li>Offering, giving, requesting or accepting any financial or other "
                    "advantage to influence the improper performance of a function</li>"
                    "<li>Facilitation payments of any amount, for any purpose, including to "
                    "expedite a routine administrative action</li>"
                    "<li>Kickbacks, whether in cash, in kind, or as an inflated subcontract</li>"
                    "<li>Political contributions made on behalf of the firm</li>"
                    "<li>Charitable donations used as a route to improper influence</li>"
                    "<li>Using an agent, consultant or intermediary to do anything this policy "
                    "prohibits</li></ul>"]),
                ("No supplier commission", [
                    "<p>We accept no commission, agency fee, finder's fee, success fee or other "
                    "payment from any manufacturer, supplier, distributor or intermediary. Our "
                    "fee income comes from clients only. This rule applies equally to "
                    "associates and subcontractors engaged on our work.</p>"]),
                ("Gifts and hospitality", [
                    f"<p>Gifts and hospitality must be modest, infrequent, transparent and "
                    f"recorded in the firm's register above a threshold of "
                    f"{TODO.format('threshold amount')}. Gifts and hospitality to or from any "
                    "party connected to a live procurement in which we are involved are "
                    "prohibited entirely. Cash and cash equivalents may never be given or "
                    "accepted.</p>"]),
                ("Third-party due diligence", [
                    "<p>Every agent, intermediary, associate, subcontractor and joint venture "
                    "partner is subject to risk-based due diligence before appointment, "
                    "covering ownership, sanctions and debarment screening, adverse media and "
                    "integrity history. Anti-corruption obligations and audit rights are "
                    "written into every engagement.</p>"]),
                ("Books, records and controls", [
                    "<p>All payments are accurately recorded with a stated business purpose. No "
                    "undisclosed or unrecorded account, fund or asset may be established for "
                    "any purpose.</p>",
                    f"<p>{TODO.format('name the approval thresholds and the financial controls actually in place')}</p>"]),
                ("Training", [
                    f"<p>All personnel receive anti-corruption training on joining and "
                    f"{TODO.format('frequency')} thereafter, with specific additional training "
                    "for those working on procurement engagements.</p>"]),
                ("Reporting and non-retaliation", [
                    f"<p>Concerns must be reported to the Head of Compliance &amp; Risk at "
                    f"{TODO.format('confidential reporting email')} or "
                    f"{TODO.format('reporting phone number')}. Reports may be made anonymously "
                    "and may be made by anyone, including client personnel, suppliers and "
                    "members of the public.</p>",
                    "<p>The firm will not retaliate against anyone who raises a concern in good "
                    "faith, and will treat any attempt to do so as a disciplinary matter. A "
                    "report made in good faith that turns out to be mistaken carries no "
                    "consequence for the person who made it.</p>"]),
                ("Consequences", [
                    "<p>Breach of this policy is grounds for dismissal or termination of "
                    "engagement, and will be reported to the relevant authorities where the law "
                    "requires or the circumstances warrant. We will terminate a client "
                    "engagement rather than participate in conduct this policy prohibits.</p>"]),
                ("Governance", [
                    f"<p>This policy is owned by the Head of Compliance &amp; Risk, who reports "
                    f"independently of fee-earning lines, and is reviewed "
                    f"{TODO.format('review frequency')} by the board.</p>"]),
            ]),
    ]


# --------------------------------------------------------------------------- #
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
          <p>Eight service lines across the capability lifecycle.</p></a>
        <a class="card" href="{{P}}sectors/index.html"><h3>Sectors</h3>
          <p>The institutions we support.</p></a>
        <a class="card" href="{{P}}about/index.html"><h3>About</h3>
          <p>Who we are and how we work.</p></a>
        <a class="card" href="{{P}}careers/index.html"><h3>Careers</h3>
          <p>Current and planned openings.</p></a>
      </div>
    </div>
  </section>
'''
    return ("404.html", "Page not found", "The page you requested could not be found.", body)


def all_company_pages():
    return [about_index(), leadership(), integrity(), insights(), careers(), contact(),
            not_found()] + legal_pages()
