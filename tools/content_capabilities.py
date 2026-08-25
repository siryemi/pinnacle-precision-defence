"""Capability pages: the /capabilities index plus eight service-line pages."""

from layout import (NAV_CAPABILITIES, ARROW, ARROW_SM, page_hero, cta_band,
                    link_arrow, breadcrumb)


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


def _deliverables(items):
    cards = []
    for i, (title, blurb) in enumerate(items, 1):
        cards.append(f'''      <div class="card">
        <p class="card__num">{i:02d}</p>
        <h3>{title}</h3>
        <p>{blurb}</p>
      </div>''')
    return '<div class="grid grid--3">\n' + "\n".join(cards) + "\n    </div>"


def capability_page(slug, title, eyebrow, lede, intro, workstreams, engagements,
                    deliverables, related, desc):
    """Assemble one service-line page."""
    rel = "\n        ".join(
        f'<a class="card" href="{{P}}{href}"><h3>{label}</h3><p>{blurb}</p>'
        f'<div class="card__foot"><span class="link-arrow">Read more {ARROW_SM}</span></div></a>'
        for label, href, blurb in related
    )

    body = page_hero(
        eyebrow, title, lede,
        trail=[("Capabilities", "capabilities/index.html"), (title, None)],
        actions=f'<div class="hero__actions"><a class="btn btn--primary" '
                f'href="{{P}}contact/index.html">Discuss this capability {ARROW}</a></div>',
    )

    body += f'''
  <section class="section">
    <div class="shell">
      <div class="split">
        <div class="prose">
          <p class="eyebrow">Overview</p>
{intro}
        </div>
        <div>
          <p class="eyebrow">Workstreams</p>
          {_ruled(workstreams)}
        </div>
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Engagements</p>
        <h2 class="d2">How this work typically arrives</h2>
        <p class="lede mt-16">Representative engagement shapes. Each is scoped to the client's
          classification handling requirements before any work begins.</p>
      </div>
      {_acc("eng-" + slug, engagements)}
    </div>
  </section>

  <section class="section section--ink2 section--line">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Deliverables</p>
        <h2 class="d2">What the client is left holding</h2>
      </div>
      {_deliverables(deliverables)}
    </div>
  </section>

  <section class="section">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Related</p>
        <h2 class="d3">Often paired with</h2>
      </div>
      <div class="grid grid--3">
        {rel}
      </div>
    </div>
  </section>

''' + cta_band()

    return (f"capabilities/{slug}.html", title, desc, body)


# --------------------------------------------------------------------------- #
# Index page
# --------------------------------------------------------------------------- #

_CAP_SUMMARIES = {
    "strategy-and-policy": "Defence policy, doctrine and force posture analysis for ministerial and "
                           "service-headquarters decision makers.",
    "capability-development": "Turning operational intent into a written, testable requirement "
                              "assessed across every line of development.",
    "procurement-advisory": "Acquisition strategy, whole-life costing, vendor due diligence and "
                            "tender support under the Public Procurement Act.",
    "training-and-doctrine": "Curriculum, exercise and simulation design for training "
                             "establishments and operational formations.",
    "isr-and-c4i": "Independent architecture advice on intelligence, surveillance, "
                   "reconnaissance and command-and-control systems.",
    "sustainment-and-mro": "Availability engineering, spares provisioning, maintenance planning "
                           "and obsolescence management.",
    "cyber-and-information": "Cyber defence assurance, security operations centre design and "
                             "information environment analysis.",
    "border-and-maritime": "Land border and maritime domain awareness, including Gulf of Guinea "
                           "and inland waterway security.",
}


def capabilities_index():
    cards = []
    for i, (slug, label, blurb) in enumerate(NAV_CAPABILITIES, 1):
        cards.append(f'''      <a class="card" href="{{P}}capabilities/{slug}.html" data-reveal="{(i % 3) * 60}">
        <p class="card__num">{i:02d}</p>
        <h3>{label}</h3>
        <p>{_CAP_SUMMARIES[slug]}</p>
        <div class="card__tags"><span class="card__tag">{blurb}</span></div>
        <div class="card__foot"><span class="link-arrow">Read more {ARROW_SM}</span></div>
      </a>''')

    body = page_hero(
        "Capabilities",
        "Eight service lines across the capability lifecycle",
        "We are organised around the sequence a capability actually travels — from policy "
        "and requirement, through acquisition, into training and sustainment. Most clients "
        "engage us on one line and find the problem sits in another.",
        trail=[("Capabilities", None)],
    )

    body += f'''
  <section class="section">
    <div class="shell">
      <div class="grid grid--3">
{chr(10).join(cards)}
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Why the sequence matters</p>
          <h2 class="d2">Capability fails at the joins</h2>
          <p class="lede mt-16">
            Equipment arrives without the doctrine to employ it. Doctrine is written for a
            platform the maintenance budget cannot keep flying. Training is built around a
            syllabus rather than the threat. The failures cluster at the handover points
            between organisations — which is precisely where a single-discipline consultancy
            cannot help.
          </p>
        </div>
        <div class="prose">
          <p>
            We are deliberately structured to work across those joins. A requirements review
            will say so if the honest answer is that no purchase is needed — that the gap is
            in training, in spares availability, or in how two existing systems fail to share
            data. An acquisition review will state the sustainment bill for twenty years, not
            the sticker price for one.
          </p>
          <p>
            That occasionally makes for an unwelcome briefing. We would rather deliver it at
            the requirement stage than have a client discover it after contract award.
          </p>
          <p>{link_arrow("How an engagement runs", "about/index.html#method")}</p>
        </div>
      </div>
    </div>
  </section>

''' + cta_band(
        heading="Not sure which line you need?",
        body="Describe the symptom. Part of our scoping work is establishing where the problem "
             "actually sits before you commit budget to solving the wrong one.")

    return ("capabilities/index.html", "Capabilities",
            "Eight defence advisory service lines spanning strategy, capability development, "
            "procurement, training, ISR and C4I, sustainment, cyber and border security.",
            body)


# --------------------------------------------------------------------------- #
# Detail pages
# --------------------------------------------------------------------------- #

def all_capability_pages():
    return [
        capabilities_index(),

        capability_page(
            "strategy-and-policy",
            "Defence Strategy &amp; Policy",
            "Capability · Service line 01",
            "Policy, doctrine and force posture work for the people who have to sign it — "
            "written to be argued in a ministerial meeting, not filed.",
            desc="Defence policy, doctrine development, force posture and strategic review "
                 "support for the Nigerian Ministry of Defence and service headquarters.",
            intro='''          <p>
            Nigeria's defence policy has to reconcile a set of demands that pull in different
            directions: a protracted internal security commitment in the North East and North
            West, maritime and energy infrastructure protection in the Gulf of Guinea, regional
            obligations under ECOWAS and the Multinational Joint Task Force, and a fiscal
            envelope that will not stretch to all of them at once.
          </p>
          <p>
            Our strategy work starts from that constraint rather than around it. We help
            clients state what the force is <strong>for</strong>, in priority order, and then
            test whether the current structure, doctrine and investment plan actually deliver
            it. Where they do not, we say which of the demands is going unmet — because a
            strategy that claims to cover everything at the current budget is not a strategy.
          </p>
          <p>
            The output is intended to survive contact with a hostile reviewer: assumptions
            written down, evidence referenced, and the trade-offs made explicit rather than
            buried in an annex.
          </p>''',
            workstreams=[
                ("Strategic defence review support",
                 "Structured review of missions, force structure and investment against the "
                 "threat and fiscal picture, in the pattern of a defence white paper process."),
                ("Doctrine development",
                 "Drafting and editorial support for joint and single-service doctrine, "
                 "including doctrine hierarchy design and currency review of existing publications."),
                ("Force posture and basing analysis",
                 "Where formations, air assets and naval units should be held to meet response "
                 "time requirements, and what the sustainment implications are."),
                ("Threat and operating environment assessment",
                 "Open-source and client-provided assessment of the actors, capabilities and "
                 "trends the force must plan against over a stated horizon."),
                ("Defence budget-to-capability alignment",
                 "Tracing budget lines to the capability outcomes they fund, and identifying "
                 "where funded activity no longer matches stated priority."),
                ("Programme governance design",
                 "Board structures, decision gates, terms of reference and reporting lines for "
                 "major capability programmes."),
            ],
            engagements=[
                ("Strategic review secretariat",
                 "<p>Providing the analytical secretariat for a service-level or joint strategic "
                 "review: managing the evidence base, running the workshop programme, drafting "
                 "sections to the review board's direction and maintaining the audit trail of "
                 "decisions.</p><ul><li>Typical duration: six to twelve months</li>"
                 "<li>Client retains authorship; we provide analysis and drafting capacity</li>"
                 "<li>Cleared personnel only, working on client premises where required</li></ul>"),
                ("Doctrine currency audit",
                 "<p>A rapid assessment of an existing doctrine set: what is out of date, what "
                 "contradicts other publications, what has no corresponding training, and what "
                 "is missing entirely. Delivered as a prioritised remediation plan.</p>"),
                ("Independent challenge on a strategy already drafted",
                 "<p>Red-team review of a policy or strategy document before it goes forward. We "
                 "argue the opposing case in writing — the assumptions we think will not hold, "
                 "the resource implications we think are understated, and the questions a "
                 "sceptical legislator will ask.</p>"),
                ("Standing policy advisory retainer",
                 "<p>A named senior adviser available to a principal for short-turnaround "
                 "analysis, briefing preparation and second opinions, under a fixed monthly "
                 "commitment rather than per-task pricing.</p>"),
            ],
            deliverables=[
                ("Evidenced strategy or policy text",
                 "Publication-ready drafting with a referenced evidence base and stated assumptions."),
                ("Trade-off register",
                 "The choices the strategy makes, what each one costs and what it gives up."),
                ("Doctrine remediation plan",
                 "Prioritised list of publications to write, revise, merge or withdraw."),
                ("Force posture options",
                 "Comparable basing and structure options with response-time and cost implications."),
                ("Governance handbook",
                 "Board terms of reference, gate criteria and reporting templates the client owns."),
                ("Briefing pack",
                 "Decision-grade slides and speaking notes for ministerial or board presentation."),
            ],
            related=[
                ("Capability Development", "capabilities/capability-development.html",
                 "Turning the strategy into testable requirements."),
                ("Ministry of Defence &amp; DHQ", "sectors/defence-headquarters.html",
                 "How we support the policy and joint planning centre."),
                ("Procurement &amp; Acquisition", "capabilities/procurement-advisory.html",
                 "Funding the priorities the strategy sets."),
            ],
        ),

        capability_page(
            "capability-development",
            "Capability Development",
            "Capability · Service line 02",
            "Requirements engineering and force design — establishing what capability is "
            "actually needed before anyone is asked to quote a price for it.",
            desc="Requirements engineering, force design and lines-of-development analysis for "
                 "Nigerian defence capability programmes.",
            intro='''          <p>
            The most expensive mistakes in defence are made early and cheaply. A requirement
            written as a product description — a particular airframe, a named vehicle, a
            specific radar — has already foreclosed the analysis that would have told the
            client whether the capability gap was even an equipment gap.
          </p>
          <p>
            We work the requirement properly. Starting from the operational task, we
            decompose it into measurable capability statements and then assess each against
            all the lines of development that have to move together: doctrine, organisation,
            training, equipment, personnel, infrastructure, information and logistics. The
            frequent finding is that the equipment line is not the binding constraint.
          </p>
          <p>
            The result is a requirement document that a tender can be built on, that vendors
            can be compared against on equal terms, and that will still make sense to a
            successor three years later.
          </p>''',
            workstreams=[
                ("Operational analysis",
                 "Quantifying the task: how many, how far, how often, in what conditions, "
                 "against what threat, at what readiness."),
                ("Requirements decomposition",
                 "From user requirement to system requirement, with each statement testable and "
                 "traceable back to an operational need."),
                ("Lines of development assessment",
                 "Structured review across doctrine, organisation, training, equipment, "
                 "personnel, infrastructure, information and logistics."),
                ("Options analysis",
                 "Comparable costed options — including the option of changing training or "
                 "process rather than buying anything."),
                ("Force design and structure",
                 "Establishment tables, sub-unit design and manning implications of a proposed "
                 "capability."),
                ("Benefits and measurement framework",
                 "How the client will know, in two years, whether the capability delivered what "
                 "was claimed for it."),
            ],
            engagements=[
                ("Capability gap analysis",
                 "<p>An assessment of a stated gap against the current force: whether the gap is "
                 "real as described, what is actually driving it, and which lines of development "
                 "would have to move to close it. Frequently reframes the client's question.</p>"),
                ("User requirement document authoring",
                 "<p>Drafting the user and system requirement documents for a programme entering "
                 "acquisition, with a full traceability matrix from operational task to "
                 "individual requirement line.</p><ul><li>Written for tender use</li>"
                 "<li>Vendor-neutral by construction — no OEM-specific language</li></ul>"),
                ("Pre-tender requirement assurance",
                 "<p>Independent review of a requirement set already drafted, checking for "
                 "unstated assumptions, untestable statements, requirements only one supplier "
                 "can meet, and gaps that will surface as change requests after award.</p>"),
                ("Force design study",
                 "<p>Structure, establishment and manning design for a new or reorganised "
                 "formation, including the training and infrastructure consequences.</p>"),
            ],
            deliverables=[
                ("User requirement document", "Operational need stated in testable terms, vendor-neutral."),
                ("System requirement document", "Technical requirements traceable to each user requirement."),
                ("Traceability matrix", "Every requirement line linked back to the operational task it serves."),
                ("Lines-of-development report", "Where the real constraint sits across all eight lines."),
                ("Costed options analysis", "Comparable options with whole-life cost and risk stated."),
                ("Benefits framework", "Measurable success criteria agreed before contract award."),
            ],
            related=[
                ("Procurement &amp; Acquisition", "capabilities/procurement-advisory.html",
                 "Taking a sound requirement to market."),
                ("Sustainment &amp; MRO", "capabilities/sustainment-and-mro.html",
                 "The support bill a requirement commits you to."),
                ("Training, Doctrine &amp; Simulation", "capabilities/training-and-doctrine.html",
                 "The training line of development, in detail."),
            ],
        ),

        capability_page(
            "procurement-advisory",
            "Procurement &amp; Acquisition Advisory",
            "Capability · Service line 03",
            "Acquisition strategy, whole-life costing, due diligence and tender support — "
            "built to comply with the Public Procurement Act and to withstand audit.",
            desc="Defence procurement and acquisition advisory: acquisition strategy, whole-life "
                 "cost modelling, vendor due diligence and tender support under Nigeria's Public "
                 "Procurement Act.",
            intro='''          <p>
            Defence acquisition in Nigeria sits inside a specific legal and institutional
            frame: the Public Procurement Act and Bureau of Public Procurement guidance,
            Ministry of Defence and service procurement processes, National Assembly
            appropriation and oversight, and the Office of the Auditor-General for the
            Federation. Work that ignores any of them creates exposure for the officers who
            signed it.
          </p>
          <p>
            We provide the analytical and process support that keeps an acquisition defensible:
            a documented acquisition strategy, whole-life cost models that include the twenty-year
            support bill, structured due diligence on suppliers and their beneficial ownership,
            transparent evaluation criteria fixed before bids are opened, and a retained evidence
            pack that reconstructs why each decision was made.
          </p>
          <p>
            <strong>What we do not do:</strong> we do not sell, broker, source or supply
            equipment, and we accept no commission, agency fee, finder's fee or success fee
            from any supplier. Our fee comes from the client and nowhere else.
          </p>''',
            workstreams=[
                ("Acquisition strategy",
                 "Route to market, contracting approach, competition strategy and risk allocation, "
                 "documented and approved before engagement with industry."),
                ("Whole-life cost modelling",
                 "Acquisition, support, personnel, infrastructure, mid-life update and disposal "
                 "costs over the stated service life, with sensitivity analysis."),
                ("Market and supplier analysis",
                 "Who can actually supply the capability, on what lead times, with what support "
                 "footprint and what dependency on export licensing."),
                ("Due diligence",
                 "Corporate, financial, beneficial ownership, sanctions and integrity screening "
                 "of prospective suppliers and their intermediaries."),
                ("Tender and evaluation support",
                 "Specification packaging, evaluation model design, evaluator briefing and "
                 "moderation support, with criteria fixed before bid opening."),
                ("Contract and negotiation support",
                 "Commercial terms, performance regimes, intellectual property, technical data "
                 "rights, offset and local content provisions."),
            ],
            engagements=[
                ("Business case and approval support",
                 "<p>Preparing the investment case for an acquisition: requirement, options, "
                 "whole-life cost, affordability against the medium-term expenditure framework, "
                 "risk and delivery plan — in the format the approving authority requires.</p>"),
                ("Independent cost assurance",
                 "<p>A separate cost estimate developed independently of the programme team, used "
                 "to test whether the programme's own figure is credible. Commonly commissioned "
                 "by a board that suspects an estimate is optimistic.</p>"),
                ("Tender process support",
                 "<p>Process and analytical support through a competitive tender, from "
                 "specification issue to award recommendation, with all evaluation records "
                 "retained in an audit-ready pack.</p><ul>"
                 "<li>Strict separation between our team and any bidder</li>"
                 "<li>Conflict-of-interest declarations for every named individual</li>"
                 "<li>Evaluation criteria and weightings locked before bids are opened</li></ul>"),
                ("Supplier integrity due diligence",
                 "<p>Standalone due diligence on a prospective supplier, agent or joint venture "
                 "partner: corporate structure, ultimate beneficial ownership, sanctions and "
                 "debarment screening, litigation history and adverse media, with sources cited.</p>"),
                ("Post-award contract assurance",
                 "<p>Reviewing delivery against contract: milestone verification, performance "
                 "regime operation, change control discipline and early warning on schedule slip.</p>"),
            ],
            deliverables=[
                ("Acquisition strategy paper", "Approved route to market with risk allocation stated."),
                ("Whole-life cost model", "Client-owned, documented model with assumptions exposed."),
                ("Due diligence reports", "Sourced integrity and financial findings on each supplier."),
                ("Evaluation framework", "Criteria, weightings and scoring guidance fixed pre-tender."),
                ("Award recommendation", "Reasoned recommendation with dissenting views recorded."),
                ("Audit evidence pack", "Complete decision trail retained for the client's records."),
            ],
            related=[
                ("Capability Development", "capabilities/capability-development.html",
                 "The requirement a tender should be built on."),
                ("Integrity &amp; compliance", "about/integrity-and-compliance.html",
                 "Our conflict-of-interest and anti-corruption position."),
                ("Defence Industrial Base", "sectors/defence-industry.html",
                 "Local content, offset and technology transfer."),
            ],
        ),

        capability_page(
            "training-and-doctrine",
            "Training, Doctrine &amp; Simulation",
            "Capability · Service line 04",
            "Curriculum, exercise and simulation design benchmarked against the threat the "
            "force is facing — not the syllabus it inherited.",
            desc="Military training design, curriculum development, exercise design and "
                 "simulation strategy for Nigerian training establishments and formations.",
            intro='''          <p>
            Training is the line of development that most reliably produces capability per naira
            spent, and the one most often left as it was found. Syllabi drift out of step with
            the operating environment; instructors teach what they were taught; exercises
            rehearse a scenario that no longer resembles the threat.
          </p>
          <p>
            We design training backwards from the task. What must a soldier, sailor, airman or
            officer be able to do, to what standard, under what conditions? From there we build
            the curriculum, the assessment regime that proves the standard has been reached,
            the exercise programme that tests it collectively, and the simulation strategy that
            makes repetition affordable.
          </p>
          <p>
            We also build the instructor cadre. Training design that depends on our people
            remaining in post has failed on its own terms.
          </p>''',
            workstreams=[
                ("Training needs analysis",
                 "From operational task to individual and collective training requirement, with "
                 "performance standards and conditions stated."),
                ("Curriculum and course design",
                 "Course architecture, lesson specifications, assessment design and progression "
                 "criteria for training establishments."),
                ("Instructor development",
                 "Train-the-trainer programmes, instructional technique, assessment moderation "
                 "and instructor quality assurance."),
                ("Collective training and exercise design",
                 "Field training exercise and command post exercise design, scenario writing, "
                 "opposing force construction and exercise control."),
                ("Simulation and synthetic training strategy",
                 "Where simulation earns its cost, what fidelity is actually required, and how "
                 "synthetic and live training should be blended."),
                ("Lessons and evaluation systems",
                 "Structures for capturing operational lessons and feeding them back into "
                 "doctrine and training within a useful timeframe."),
            ],
            engagements=[
                ("Training establishment review",
                 "<p>End-to-end review of a training school or academy: course relevance, "
                 "instructor capacity and currency, facilities and equipment state, assessment "
                 "integrity and throughput against the force's actual requirement.</p>"),
                ("Course design and accreditation",
                 "<p>Designing or rebuilding a specific course to a defined standard, including "
                 "lesson materials, assessment instruments and an instructor handbook the "
                 "establishment retains and maintains.</p>"),
                ("Exercise design and control",
                 "<p>Designing a collective training event against a realistic threat scenario, "
                 "including a credible opposing force, exercise control structure, injects and "
                 "an evaluation framework that produces usable findings.</p>"),
                ("Simulation investment appraisal",
                 "<p>Independent assessment of a proposed simulator or synthetic training "
                 "purchase: whether the training need justifies the fidelity being bought, what "
                 "the through-life cost is, and what proportion of the live training bill it can "
                 "credibly displace.</p>"),
                ("Lessons-learned system design",
                 "<p>Establishing the process, roles and repository through which operational "
                 "experience reaches doctrine writers and training staff — and verifying it "
                 "functions after handover.</p>"),
            ],
            deliverables=[
                ("Training needs analysis report", "Task-to-standard mapping with conditions specified."),
                ("Curriculum and lesson materials", "Complete, client-owned course documentation."),
                ("Assessment instruments", "Tests and practical assessments tied to stated standards."),
                ("Instructor handbook", "Delivery guidance so the course survives staff rotation."),
                ("Exercise design pack", "Scenario, OPFOR, control plan and evaluation framework."),
                ("Simulation strategy", "Fidelity requirements, blend ratio and cost justification."),
            ],
            related=[
                ("Capability Development", "capabilities/capability-development.html",
                 "Training as a line of development."),
                ("Nigerian Army", "sectors/nigerian-army.html",
                 "Land force training establishment support."),
                ("Defence Strategy &amp; Policy", "capabilities/strategy-and-policy.html",
                 "Doctrine that training must reflect."),
            ],
        ),

        capability_page(
            "isr-and-c4i",
            "ISR &amp; C4I Advisory",
            "Capability · Service line 05",
            "Independent architecture advice on sensors, command systems and the networks "
            "between them — including where a proposed system will fail to talk to the one "
            "already in service.",
            desc="Independent ISR and C4I architecture advisory: sensor-to-decision "
                 "architecture, interoperability, data standards and system integration "
                 "assurance for Nigerian defence.",
            intro='''          <p>
            Sensors are easy to buy and hard to exploit. A great deal of defence ISR investment
            produces a feed that reaches one screen, in one headquarters, in a format nothing
            else can consume — with the analytical manpower to exploit it never having been
            resourced.
          </p>
          <p>
            Our work is architectural and vendor-neutral. We map how information should move
            from sensor to analyst to commander to effector, specify the interfaces and data
            standards that make that possible across services, and test proposed systems
            against the ones already in service. Where a procurement will produce another
            isolated stovepipe, we say so before contract award.
          </p>
          <p>
            We advise on architecture, standards, integration and exploitation. We are not a
            systems integrator and do not bid for the implementation work we specify.
          </p>''',
            workstreams=[
                ("Sensor-to-decision architecture",
                 "End-to-end design of how collection, processing, exploitation and dissemination "
                 "fit together, including the human analytical capacity required."),
                ("Interoperability and standards",
                 "Data formats, message standards and interface specifications enabling joint and "
                 "coalition operation, including MNJTF and regional partner interoperability."),
                ("Collection management",
                 "Processes and tooling for tasking scarce collection assets against prioritised "
                 "intelligence requirements."),
                ("C4I system assessment",
                 "Independent technical and operational assessment of command, control, "
                 "communications and intelligence systems, in service or proposed."),
                ("Communications and bearer planning",
                 "Bearer strategy across satellite, terrestrial and tactical radio, with "
                 "resilience and spectrum considerations."),
                ("Data exploitation and analytics",
                 "Realistic assessment of what automation and analytics can do for a given "
                 "collection posture — and what still requires trained analysts."),
            ],
            engagements=[
                ("ISR architecture study",
                 "<p>A reference architecture for a service or joint ISR enterprise: sensors, "
                 "processing, dissemination, standards and the analytical establishment needed to "
                 "exploit it. Includes a migration path from the current state.</p>"),
                ("Interoperability assessment",
                 "<p>Testing whether specified systems can actually exchange information: "
                 "protocol and format analysis, gap identification and a remediation "
                 "specification. Frequently commissioned after two procurements have already "
                 "been made independently.</p>"),
                ("Pre-award technical assurance",
                 "<p>Independent technical evaluation of an ISR or C4I bid: whether claimed "
                 "performance is credible, what integration work the client will inherit, and "
                 "what technical data rights are needed to avoid vendor lock-in.</p>"),
                ("Collection management review",
                 "<p>Assessment of how collection assets are tasked against intelligence "
                 "requirements, and redesign of the tasking cycle where prioritisation is "
                 "informal or contested.</p>"),
                ("Real-time operations centre design",
                 "<p>Design of a fusion or operations centre: information flows, watchkeeping "
                 "structure, decision authorities, physical layout and system integration "
                 "requirements.</p>"),
            ],
            deliverables=[
                ("Reference architecture", "Documented target architecture with a staged migration path."),
                ("Interface and standards specification", "The interoperability requirements to write into contracts."),
                ("Integration risk register", "Where systems will not connect, and what it costs to fix."),
                ("Technical assurance report", "Independent verdict on bid credibility and lock-in risk."),
                ("Collection management process", "Tasking cycle, prioritisation model and roles."),
                ("Operations centre design", "Layout, watch structure, information flows and system list."),
            ],
            related=[
                ("Border &amp; Maritime Security", "capabilities/border-and-maritime.html",
                 "Domain awareness as an ISR problem."),
                ("Cyber &amp; Information Defence", "capabilities/cyber-and-information.html",
                 "Securing the networks the architecture depends on."),
                ("Nigerian Air Force", "sectors/nigerian-air-force.html",
                 "Air ISR integration and exploitation."),
            ],
        ),

        capability_page(
            "sustainment-and-mro",
            "Sustainment &amp; MRO Advisory",
            "Capability · Service line 06",
            "Availability engineering, spares provisioning, maintenance planning and "
            "obsolescence management — the work that decides what is mission-capable on the day.",
            desc="Defence sustainment and MRO advisory: availability engineering, spares "
                 "provisioning, maintenance planning, obsolescence management and depot design.",
            intro='''          <p>
            A fleet's headline number tells you almost nothing. What matters to a commander is
            how many aircraft, hulls or vehicles are mission-capable this morning — and that
            figure is set by spares availability, maintenance capacity, technician skills and
            the supply chain, not by the size of the original purchase.
          </p>
          <p>
            Sustainment is where Nigerian defence capability is most often lost, and it is
            structurally under-resourced because it is invisible at the point of purchase.
            We work the whole support system: reliability and availability modelling, spares
            range and scaling, maintenance policy and depot capacity, technician training,
            obsolescence and diminishing-sources management, and the contracting model that
            underpins it.
          </p>
          <p>
            The uncomfortable version of this analysis — that a fleet cannot be sustained at
            the funded support level and a decision on reduction or reinvestment is required —
            is one we will put in writing.
          </p>''',
            workstreams=[
                ("Availability and reliability analysis",
                 "Modelling mission-capable rates against maintenance policy, spares holdings, "
                 "manpower and infrastructure to find the binding constraint."),
                ("Spares provisioning",
                 "Range and scaling of spares, repair pipelines, stock policy and the working "
                 "capital implication of each."),
                ("Maintenance policy and planning",
                 "Preventive and corrective maintenance regimes, inspection intervals, and "
                 "levels-of-repair analysis across unit, intermediate and depot levels."),
                ("Depot and facility design",
                 "Capacity planning, workflow, tooling, test equipment and facility "
                 "specification for maintenance and overhaul organisations."),
                ("Obsolescence management",
                 "Diminishing manufacturing sources, component lifecycle monitoring and "
                 "planned technology refresh."),
                ("Support contracting",
                 "Contractor logistic support, availability-based contracting and performance "
                 "regimes, with the technical data rights needed to avoid captivity."),
            ],
            engagements=[
                ("Fleet availability diagnostic",
                 "<p>A structured diagnostic of why a fleet's mission-capable rate is where it is: "
                 "supply, maintenance capacity, skills, infrastructure or funding. Delivered as a "
                 "ranked constraint list with the cost and lead time to relieve each.</p>"),
                ("Support solution design",
                 "<p>Designing the support system for a capability entering service — spares, "
                 "maintenance levels, facilities, technician establishment and contracting "
                 "model — ideally before the platform contract is signed.</p>"),
                ("Sustainment cost review",
                 "<p>Independent assessment of what an in-service or proposed fleet actually costs "
                 "to sustain per year at a stated availability, against what is currently "
                 "budgeted. Often the basis of a difficult but necessary board paper.</p>"),
                ("Depot capability assessment",
                 "<p>Assessment of an MRO facility against the workload it is expected to carry: "
                 "capacity, tooling, technician competence, quality system and turnaround "
                 "performance, with an investment plan.</p>"),
                ("Obsolescence and technology refresh planning",
                 "<p>Identifying components and subsystems approaching end of support, with a "
                 "phased refresh plan and the procurement lead times each requires.</p>"),
            ],
            deliverables=[
                ("Availability model", "Client-owned model linking support inputs to mission-capable rate."),
                ("Constraint register", "Ranked list of what limits availability, with cost to relieve."),
                ("Spares provisioning plan", "Range, scaling and stock policy with working capital stated."),
                ("Maintenance policy", "Levels of repair, intervals and depot workflow."),
                ("Sustainment cost baseline", "Annual cost to hold a stated availability, defensibly derived."),
                ("Obsolescence roadmap", "Phased refresh plan with decision dates."),
            ],
            related=[
                ("Procurement &amp; Acquisition", "capabilities/procurement-advisory.html",
                 "Whole-life cost at the point of purchase."),
                ("Nigerian Air Force", "sectors/nigerian-air-force.html",
                 "Airframe availability engineering."),
                ("Nigerian Navy", "sectors/nigerian-navy.html",
                 "Fleet availability and dockyard capacity."),
            ],
        ),

        capability_page(
            "cyber-and-information",
            "Cyber &amp; Information Defence",
            "Capability · Service line 07",
            "Defensive cyber assurance, security operations design and information "
            "environment analysis for military networks and national security institutions.",
            desc="Defensive cyber advisory for defence: network security assurance, security "
                 "operations centre design, incident response readiness and information "
                 "environment analysis.",
            intro='''          <p>
            Military networks in Nigeria carry operational traffic across infrastructure that was
            frequently procured piecemeal, is partly commercial, and is administered by people
            without dedicated security training. Meanwhile the information environment — the
            contest over narrative around operations in the North East and elsewhere — has
            direct operational consequences.
          </p>
          <p>
            Our work here is <strong>defensive and analytical</strong>. We assess and harden
            networks, design security operations and incident response capability, build the
            skills of the client's own security staff, and analyse the information environment
            so a client understands how their operations are being represented.
          </p>
          <p>
            We do not develop offensive cyber capability, intrusion tooling or surveillance
            systems, and we do not conduct or advise on influence operations directed at
            domestic populations. Those boundaries are contractual, not aspirational.
          </p>''',
            workstreams=[
                ("Security architecture review",
                 "Assessment of network segmentation, boundary protection, identity management "
                 "and cryptographic provision against the classification of traffic carried."),
                ("Security operations centre design",
                 "SOC design and build-out: monitoring coverage, tooling, staffing model, "
                 "escalation paths and the training pipeline to sustain it."),
                ("Incident response readiness",
                 "Response plans, playbooks, roles, exercises and forensic readiness — tested "
                 "rather than written and shelved."),
                ("Supply chain and third-party assurance",
                 "Security assessment of vendors, contractors and hosted services with access to "
                 "defence networks or data."),
                ("Personnel and insider risk",
                 "Vetting process design, privileged access management and insider risk "
                 "controls proportionate to the environment."),
                ("Information environment assessment",
                 "Analytical assessment of how an operation or institution is being represented "
                 "across media and social platforms, and where factual correction is warranted."),
            ],
            engagements=[
                ("Network security assessment",
                 "<p>A structured assessment of a defence or agency network against a recognised "
                 "control framework, producing a prioritised remediation plan costed and "
                 "sequenced by risk reduction per naira.</p><ul>"
                 "<li>Conducted under written authorisation with agreed scope and rules of engagement</li>"
                 "<li>Findings delivered to the client only, under classification handling</li></ul>"),
                ("SOC establishment programme",
                 "<p>Standing up a security operations capability from design through to operating "
                 "handover: use cases, tooling specification, staffing, procedures and analyst "
                 "training, with a defined competence handover point.</p>"),
                ("Incident response exercise",
                 "<p>Tabletop or technical exercise of a realistic incident scenario against the "
                 "client's actual plans and staff, with findings written up as a remediation "
                 "plan.</p>"),
                ("Cyber workforce development",
                 "<p>Designing the training and career pipeline for a defence cyber workforce — "
                 "which is usually the constraint, rather than tooling.</p>"),
                ("Information environment briefing",
                 "<p>Periodic analytical assessment of the information environment surrounding an "
                 "operation or institution: principal narratives, their sources and reach, and "
                 "the factual record where it is being misstated.</p>"),
            ],
            deliverables=[
                ("Security assessment report", "Findings against a control framework, evidence included."),
                ("Prioritised remediation plan", "Sequenced by risk reduction, with costs and lead times."),
                ("SOC design pack", "Use cases, tooling specification, staffing and procedures."),
                ("Incident response playbooks", "Tested plans with named roles and escalation paths."),
                ("Workforce development plan", "Training pipeline and competence framework."),
                ("Information environment assessment", "Sourced analysis of narratives and reach."),
            ],
            related=[
                ("ISR &amp; C4I Advisory", "capabilities/isr-and-c4i.html",
                 "The networks that carry the architecture."),
                ("Internal Security Agencies", "sectors/internal-security.html",
                 "Agency network and data protection."),
                ("Integrity &amp; compliance", "about/integrity-and-compliance.html",
                 "The work we decline, and why."),
            ],
        ),

        capability_page(
            "border-and-maritime",
            "Border &amp; Maritime Security",
            "Capability · Service line 08",
            "Domain awareness and interagency response design across Nigeria's land borders, "
            "inland waterways and the Gulf of Guinea.",
            desc="Border and maritime security advisory: domain awareness architecture, "
                 "interagency coordination, Gulf of Guinea operations and inland waterway "
                 "security for Nigerian agencies.",
            intro='''          <p>
            Nigeria's security perimeter is long, porous and shared between many organisations.
            Land borders across the north and along the Cameroon frontier, the Lake Chad basin,
            the creeks and waterways of the Niger Delta, and an exclusive economic zone in the
            Gulf of Guinea that carries the country's petroleum exports — each with a different
            threat profile and a different lead agency.
          </p>
          <p>
            The consistent finding in this domain is that the constraint is coordination rather
            than sensors. Multiple agencies hold partial pictures, on incompatible systems, with
            unclear response authorities. Detection without a functioning response chain
            produces reports, not interdictions.
          </p>
          <p>
            We design the whole chain — detect, identify, decide, respond, prosecute — and we
            work the interagency mechanics that make it function across organisational
            boundaries.
          </p>''',
            workstreams=[
                ("Maritime domain awareness",
                 "Architecture for building and sharing a maritime picture: coastal radar, AIS, "
                 "satellite, patrol assets and fusion, with the Gulf of Guinea regional "
                 "information-sharing framework in view."),
                ("Land border surveillance",
                 "Proportionate surveillance design for extended land borders, including the "
                 "trade-off between fixed infrastructure, mobile patrols and human networks."),
                ("Inland waterway and creek operations",
                 "Capability design for riverine and creek environments, including small-craft "
                 "requirements, basing and sustainment in austere conditions."),
                ("Interagency coordination",
                 "Joint operating centres, information-sharing agreements, response authorities "
                 "and de-confliction between military, police and civil agencies."),
                ("Offshore infrastructure protection",
                 "Protection concepts for platforms, terminals, pipelines and shipping, including "
                 "the commercial and legal interfaces with operators."),
                ("Evidence and prosecution chain",
                 "Ensuring interdictions convert into prosecutions: evidence handling, custody, "
                 "documentation and coordination with prosecuting authorities."),
            ],
            engagements=[
                ("Domain awareness architecture study",
                 "<p>Designing the sensing, fusion and dissemination architecture for a maritime "
                 "or land domain, with a phased investment plan and a candid statement of what "
                 "coverage each phase actually buys.</p>"),
                ("Interagency operating model design",
                 "<p>Designing the joint operating centre, information-sharing arrangements and "
                 "response authorities across the agencies with a stake in a domain — including "
                 "the memoranda of understanding needed to make it stand up.</p>"),
                ("Response capability review",
                 "<p>Assessment of whether detection can be converted into interdiction: asset "
                 "readiness, response times from realistic basing, sustainment in the operating "
                 "environment and the legal basis for action.</p>"),
                ("Offshore protection concept",
                 "<p>A protection concept for offshore energy infrastructure, developed with the "
                 "relevant naval, agency and commercial stakeholders, including cost-sharing "
                 "and command arrangements.</p>"),
                ("Prosecution chain review",
                 "<p>Tracing recent interdictions from apprehension to court outcome to find "
                 "where cases are failing, and fixing the evidence and handover process.</p>"),
            ],
            deliverables=[
                ("Domain awareness architecture", "Sensing and fusion design with phased investment plan."),
                ("Coverage assessment", "Honest statement of what is and is not detectable, by phase."),
                ("Interagency operating model", "Centre design, authorities and draft MOUs."),
                ("Response readiness report", "Detection-to-interdiction timeline against realistic basing."),
                ("Protection concept", "Layered protection design for fixed and offshore infrastructure."),
                ("Prosecution chain remediation", "Evidence handling and handover fixes, agency by agency."),
            ],
            related=[
                ("Nigerian Navy", "sectors/nigerian-navy.html",
                 "Maritime capability and fleet employment."),
                ("Internal Security Agencies", "sectors/internal-security.html",
                 "Customs, Immigration, NSCDC and marine police."),
                ("ISR &amp; C4I Advisory", "capabilities/isr-and-c4i.html",
                 "Sensor and fusion architecture."),
            ],
        ),
    ]
