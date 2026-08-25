"""Sector pages: the /sectors index plus six client-group pages."""

from layout import NAV_SECTORS, ARROW, ARROW_SM, page_hero, cta_band, link_arrow


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


def sector_page(slug, title, eyebrow, lede, context, priorities, services, engagements, desc):
    svc = "\n        ".join(
        f'<a class="card" href="{{P}}capabilities/{href}.html"><h3>{label}</h3><p>{blurb}</p>'
        f'<div class="card__foot"><span class="link-arrow">Read more {ARROW_SM}</span></div></a>'
        for label, href, blurb in services
    )

    body = page_hero(
        eyebrow, title, lede,
        trail=[("Sectors", "sectors/index.html"), (title, None)],
        actions=f'<div class="hero__actions"><a class="btn btn--primary" '
                f'href="{{P}}contact/index.html">Request a briefing {ARROW}</a></div>',
    )

    body += f'''
  <section class="section">
    <div class="shell">
      <div class="split">
        <div class="prose">
          <p class="eyebrow">Context</p>
{context}
        </div>
        <div>
          <p class="eyebrow">Priorities we are asked about</p>
          {_ruled(priorities)}
          <div class="notice mt-32">
            <p style="margin:0"><strong>Note:</strong> this page describes the areas in which we
            are equipped to work. It does not assert an existing contractual relationship with
            any organisation named. Client references are provided confidentially on request.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Service lines</p>
        <h2 class="d2">Where we are most often useful here</h2>
      </div>
      <div class="grid grid--3">
        {svc}
      </div>
    </div>
  </section>

  <section class="section section--ink2 section--line">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Engagement shapes</p>
        <h2 class="d2">Typical work in this sector</h2>
      </div>
      {_acc("sec-" + slug, engagements)}
    </div>
  </section>

''' + cta_band()

    return (f"sectors/{slug}.html", title, desc, body)


_SUMMARIES = {
    "defence-headquarters": "Defence policy, joint capability planning, programme governance and "
                            "the alignment of budget to declared capability priorities.",
    "nigerian-army": "Land capability development, counter-insurgency and stabilisation support, "
                     "training establishment reform and equipment sustainment.",
    "nigerian-navy": "Maritime domain awareness in the Gulf of Guinea, fleet availability, "
                     "riverine operations and offshore infrastructure protection.",
    "nigerian-air-force": "Air power employment concepts, ISR integration, availability "
                          "engineering and aircrew and technician training pipelines.",
    "internal-security": "Capability, training and interoperability across the Nigeria Police "
                         "Force, NSCDC, Customs, Immigration and NDLEA.",
    "defence-industry": "Local content and offset structuring, technology transfer, and "
                        "compliant market entry for foreign OEMs.",
}


def sectors_index():
    cards = []
    for i, (slug, label, blurb) in enumerate(NAV_SECTORS, 1):
        cards.append(f'''      <a class="card" href="{{P}}sectors/{slug}.html" data-reveal="{(i % 3) * 60}">
        <p class="card__num">{i:02d}</p>
        <h3>{label}</h3>
        <p>{_SUMMARIES[slug]}</p>
        <div class="card__foot"><span class="link-arrow">Read more {ARROW_SM}</span></div>
      </a>''')

    body = page_hero(
        "Sectors",
        "Who we support",
        "Our clients are the institutions responsible for Nigeria's defence and internal "
        "security, and the industrial base that equips them. Each has a different mandate, "
        "a different threat picture and a different procurement route.",
        trail=[("Sectors", None)],
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
          <p class="eyebrow">Working across boundaries</p>
          <h2 class="d2">The hardest problems are joint</h2>
          <p class="lede mt-16">
            Border security is not one agency's problem. Maritime domain awareness spans the
            Navy, Customs, Immigration, NIMASA and commercial operators. Counter-insurgency in
            the North East involves the Army, the Air Force, the Police and civil authorities
            simultaneously.
          </p>
        </div>
        <div class="prose">
          <p>
            A great deal of capability is lost in the space between organisations — in unclear
            response authorities, incompatible communications, information that is held rather
            than shared, and duplicated procurement of systems that cannot interoperate.
          </p>
          <p>
            We work those seams explicitly. Where an engagement's real constraint sits inside
            another organisation, we say so, and where we are authorised to do so, we help
            convene the parties who need to be in the room.
          </p>
          <p>{link_arrow("Read about our approach", "about/index.html")}</p>
        </div>
      </div>
    </div>
  </section>

''' + cta_band()

    return ("sectors/index.html", "Sectors",
            "Defence advisory for the Nigerian Ministry of Defence, Army, Navy, Air Force, "
            "internal security agencies and the domestic defence industrial base.",
            body)


def all_sector_pages():
    return [
        sectors_index(),

        sector_page(
            "defence-headquarters",
            "Ministry of Defence &amp; Defence Headquarters",
            "Sector · 01",
            "Policy, joint planning and programme governance support at the centre — where "
            "priorities are set and where they most often fail to survive the budget cycle.",
            desc="Advisory support to Nigeria's Ministry of Defence and Defence Headquarters: "
                 "defence policy, joint capability planning, programme governance and "
                 "budget-to-capability alignment.",
            context='''          <p>
            The centre carries a task no service headquarters can perform: deciding between
            competing service priorities inside a single fiscal envelope, and holding programmes
            to account for delivering what was approved. Doing that well requires a small amount
            of very specific analytical capacity — costed options, credible programme reporting,
            and the ability to challenge a service's own business case.
          </p>
          <p>
            That capacity is chronically scarce everywhere, not only in Nigeria. Ministries are
            staffed to administer, and the analytical burden of a major capability decision
            arrives in bursts. We provide surge analytical capacity that works to the client's
            direction and leaves the method behind.
          </p>
          <p>
            We also support the governance machinery itself: programme board design, gate
            criteria, reporting formats that show slip early rather than at the point of failure,
            and the evidence discipline that makes a programme defensible to the National
            Assembly and the Auditor-General.
          </p>''',
            priorities=[
                ("Aligning budget to declared priority",
                 "Tracing appropriations through to the capability outcomes they fund, and "
                 "exposing where funded activity no longer matches stated policy."),
                ("Challenging service business cases",
                 "Independent cost and requirement assurance so the centre can interrogate a "
                 "submission on its merits."),
                ("Joint capability planning",
                 "Deciding what should be held jointly rather than duplicated across three "
                 "services, and what the joint enablers actually cost."),
                ("Programme governance and reporting",
                 "Board structures, gate criteria and reporting that surfaces problems in time "
                 "to act on them."),
                ("Oversight and audit readiness",
                 "Evidence packs and decision trails built during the programme, not "
                 "reconstructed after a query."),
                ("Defence reform implementation",
                 "Turning policy reform intent into a sequenced, resourced implementation plan "
                 "with named owners."),
            ],
            services=[
                ("Defence Strategy &amp; Policy", "strategy-and-policy",
                 "Strategic review, doctrine and force posture analysis."),
                ("Procurement &amp; Acquisition", "procurement-advisory",
                 "Business cases, cost assurance and tender support."),
                ("Capability Development", "capability-development",
                 "Requirement assurance across the lines of development."),
            ],
            engagements=[
                ("Independent cost and requirement assurance",
                 "<p>A separate analytical opinion on a service submission before it reaches the "
                 "approving authority: whether the requirement is sound, whether the cost is "
                 "credible, and what the sustainment liability will be. Reports to the centre, "
                 "not to the sponsoring service.</p>"),
                ("Programme governance establishment",
                 "<p>Designing and standing up the governance for a major programme: board terms "
                 "of reference, decision gates and criteria, reporting cadence and format, risk "
                 "management and the evidence retention policy.</p>"),
                ("Joint capability study",
                 "<p>Analysis of a capability area held across services — strategic lift, ISR, "
                 "medical, communications — to establish what should be joint, what the joint "
                 "option costs and what the transition would involve.</p>"),
                ("Defence reform implementation support",
                 "<p>Converting a reform policy into an implementation plan: workstreams, "
                 "sequencing, resourcing, named owners and measurable milestones, with "
                 "programme management support through delivery.</p>"),
            ],
        ),

        sector_page(
            "nigerian-army",
            "Nigerian Army",
            "Sector · 02",
            "Land capability development, training reform and equipment sustainment for a force "
            "carrying a sustained internal security commitment across multiple theatres.",
            desc="Advisory support to the Nigerian Army: land capability development, "
                 "counter-insurgency and stabilisation, training establishment reform, and "
                 "vehicle and equipment sustainment.",
            context='''          <p>
            The Nigerian Army has been continuously committed to internal security operations
            across several theatres for well over a decade, at a scale that leaves little
            institutional slack for the training, maintenance and force generation cycle that
            sustains long-term capability. The characteristic pressures follow from that:
            equipment used far beyond planned rates, training compressed or deferred, and
            formations rotating without a proper reconstitution period.
          </p>
          <p>
            Our work with land forces concentrates on the areas where limited investment
            produces disproportionate operational return. Vehicle and weapon availability is
            usually first — a workshop and spares problem far more often than a procurement
            problem. Training design is next, particularly for the small-unit skills that
            determine outcomes in counter-insurgency and the protection measures that reduce
            casualties.
          </p>
          <p>
            We also work the force generation cycle itself: how a formation is prepared,
            deployed, recovered and reconstituted, and what has to be true for that cycle to
            be sustainable at the current commitment level.
          </p>''',
            priorities=[
                ("Vehicle and equipment availability",
                 "Workshop capacity, spares pipelines and maintenance discipline — the fastest "
                 "route to more combat power from the fleet already owned."),
                ("Counter-insurgency and stabilisation capability",
                 "Small-unit tactics, force protection, intelligence-led operations and "
                 "civil-military interaction, designed against the current threat."),
                ("Training establishment reform",
                 "Course relevance, instructor currency, assessment integrity and throughput "
                 "against the force's real requirement."),
                ("Force generation cycle",
                 "A sustainable prepare-deploy-recover-reconstitute rhythm, and what it demands "
                 "in manning and equipment."),
                ("Soldier equipment and protection",
                 "Personal protection, night capability, communications and medical provision at "
                 "section and platoon level."),
                ("Combat service support",
                 "Logistics, transport, medical evacuation and field sustainment in dispersed "
                 "operations."),
            ],
            services=[
                ("Training, Doctrine &amp; Simulation", "training-and-doctrine",
                 "Curriculum, exercise and instructor development."),
                ("Sustainment &amp; MRO", "sustainment-and-mro",
                 "Vehicle and equipment availability engineering."),
                ("Capability Development", "capability-development",
                 "Requirements and force design for land capability."),
            ],
            engagements=[
                ("Fleet availability diagnostic",
                 "<p>Establishing why a vehicle or weapon fleet's availability is where it is, and "
                 "what it would cost to raise it. Ranked constraints — spares, workshop capacity, "
                 "technician skills, funding — with lead times against each.</p>"),
                ("Training establishment review",
                 "<p>Review of a school or training centre against the operational requirement: "
                 "what is taught, by whom, to what standard, and whether graduates arrive at "
                 "units able to do the job.</p>"),
                ("Pre-deployment training design",
                 "<p>Designing the mission-specific training package for a deploying formation "
                 "against the current threat picture in the intended theatre, including the "
                 "validation exercise.</p>"),
                ("Force protection review",
                 "<p>Assessment of protection measures — tactical, technical and procedural — "
                 "against the threat actually being encountered, with prioritised, affordable "
                 "recommendations.</p>"),
                ("Lessons capture and doctrine feedback",
                 "<p>Establishing a functioning route from operational experience into doctrine "
                 "and training, and validating that it works after handover.</p>"),
            ],
        ),

        sector_page(
            "nigerian-navy",
            "Nigerian Navy",
            "Sector · 03",
            "Maritime domain awareness, fleet availability and riverine capability for a navy "
            "responsible for the security of Nigeria's principal export corridor.",
            desc="Advisory support to the Nigerian Navy: Gulf of Guinea maritime domain "
                 "awareness, fleet availability and dockyard capacity, riverine operations and "
                 "offshore infrastructure protection.",
            context='''          <p>
            The Nigerian Navy's operating area contains the country's petroleum export
            infrastructure, one of the world's more contested piracy and armed robbery at sea
            environments, an extensive network of creeks and inland waterways used for crude
            theft and smuggling, and a set of regional obligations under the Yaoundé
            architecture. That is a genuinely demanding portfolio for any navy's fleet size.
          </p>
          <p>
            Two constraints dominate. The first is availability: hulls alongside for want of
            spares, dockyard capacity or planned maintenance discipline produce no sea days,
            and sea days are the currency of maritime security. The second is fusion and
            response — a maritime picture assembled from coastal radar, AIS, satellite and
            patrol reporting is only useful if it reaches a decision maker with the authority
            and the asset to act on it.
          </p>
          <p>
            We work both, and we work the interagency dimension that maritime security
            inescapably involves: Customs, Immigration, NIMASA, marine police, and the
            commercial operators whose assets are being protected.
          </p>''',
            priorities=[
                ("Fleet availability and dockyard capacity",
                 "Converting hulls owned into sea days delivered — maintenance planning, spares "
                 "and repair yard throughput."),
                ("Maritime domain awareness",
                 "Sensor mix, fusion architecture and picture sharing, including regional "
                 "information-exchange obligations."),
                ("Riverine and creek capability",
                 "Small-craft requirements, basing, sustainment and tactics for the Delta "
                 "waterway environment."),
                ("Offshore infrastructure protection",
                 "Layered protection for platforms, terminals and pipelines, with commercial "
                 "and legal interfaces defined."),
                ("Response chain and prosecution",
                 "Turning detection into interdiction and interdiction into conviction, "
                 "including evidence handling."),
                ("Regional and coalition interoperability",
                 "Working with regional partners and visiting navies, including standards and "
                 "communications compatibility."),
            ],
            services=[
                ("Border &amp; Maritime Security", "border-and-maritime",
                 "Domain awareness and interagency response design."),
                ("Sustainment &amp; MRO", "sustainment-and-mro",
                 "Fleet availability and dockyard capability."),
                ("ISR &amp; C4I Advisory", "isr-and-c4i",
                 "Fusion architecture and picture dissemination."),
            ],
            engagements=[
                ("Fleet availability and dockyard review",
                 "<p>Assessment of the maintenance system and repair yard capacity against the "
                 "sea-day requirement, with an investment and process plan to close the gap.</p>"),
                ("Maritime domain awareness architecture",
                 "<p>Designing the sensing, fusion and dissemination architecture for the "
                 "maritime domain, phased by affordability, with a candid statement of the "
                 "coverage each phase buys.</p>"),
                ("Riverine capability study",
                 "<p>Requirement definition for creek and inland waterway operations: craft "
                 "characteristics, basing, sustainment in austere conditions and the manning "
                 "and training implications.</p>"),
                ("Offshore protection concept",
                 "<p>A protection concept for offshore energy infrastructure developed with naval, "
                 "agency and commercial stakeholders, including command arrangements and "
                 "cost-sharing.</p>"),
                ("Interagency maritime coordination",
                 "<p>Designing the joint operating arrangements between the Navy and the civil "
                 "agencies with maritime responsibilities, including information sharing and "
                 "response authorities.</p>"),
            ],
        ),

        sector_page(
            "nigerian-air-force",
            "Nigerian Air Force",
            "Sector · 04",
            "Air power employment, ISR exploitation and the availability engineering that "
            "determines how many airframes are mission-capable on the day.",
            desc="Advisory support to the Nigerian Air Force: air power employment concepts, ISR "
                 "integration and exploitation, airframe availability engineering and aircrew "
                 "and technician training pipelines.",
            context='''          <p>
            Air power is the capability where the gap between platforms owned and effect
            delivered is widest, because that gap is set almost entirely by sustainment. An
            airframe requires spares, qualified technicians, serviceable test equipment,
            deep maintenance capacity and a supply chain that frequently runs through foreign
            OEMs and export licensing. Any weak link in that chain grounds aircraft regardless
            of the size of the fleet.
          </p>
          <p>
            The second recurring theme is exploitation. ISR aircraft and unmanned systems
            generate collection at a rate that overwhelms the analytical establishment
            resourced to exploit it. The result is imagery and video that is collected,
            stored and never turned into a decision. That is an organisational and training
            problem more than a technology problem.
          </p>
          <p>
            We work availability, exploitation, and the training pipelines — aircrew and,
            critically, technician — that underpin both. The technician pipeline is
            consistently the more neglected and the more binding of the two.
          </p>''',
            priorities=[
                ("Airframe availability",
                 "Spares provisioning, maintenance planning, deep maintenance capacity and "
                 "technician establishment against the flying rate required."),
                ("ISR exploitation",
                 "Processing, exploitation and dissemination capacity — the analysts and process "
                 "that turn collection into decisions."),
                ("Air power employment concepts",
                 "How air is best applied in the current internal security context, including "
                 "targeting process and civilian harm mitigation."),
                ("Aircrew training pipeline",
                 "Throughput, currency, simulator strategy and instructor capacity."),
                ("Technician training and retention",
                 "The pipeline that most directly constrains availability, and is most often "
                 "under-resourced."),
                ("Unmanned systems integration",
                 "Airspace integration, tasking, exploitation and sustainment of unmanned "
                 "capability alongside crewed aircraft."),
            ],
            services=[
                ("Sustainment &amp; MRO", "sustainment-and-mro",
                 "Availability engineering and deep maintenance capacity."),
                ("ISR &amp; C4I Advisory", "isr-and-c4i",
                 "Collection management and exploitation architecture."),
                ("Training, Doctrine &amp; Simulation", "training-and-doctrine",
                 "Aircrew and technician training pipeline design."),
            ],
            engagements=[
                ("Airframe availability diagnostic",
                 "<p>Establishing the binding constraint on mission-capable rate for a fleet or "
                 "type — spares, technicians, test equipment, deep maintenance slots or "
                 "funding — and the cost and lead time to relieve each.</p>"),
                ("ISR exploitation capacity review",
                 "<p>Assessment of the processing, exploitation and dissemination chain against "
                 "collection volume, with an establishment and training plan to close the "
                 "exploitation gap.</p>"),
                ("Targeting process assurance",
                 "<p>Review of the targeting process against applicable legal obligations and "
                 "good practice, including collateral damage estimation, approval authorities, "
                 "record keeping and post-strike assessment.</p>"),
                ("Technician pipeline design",
                 "<p>Designing the recruitment, training, qualification and retention pipeline "
                 "for aircraft technicians, sized to the maintenance workload the fleet "
                 "generates.</p>"),
                ("Unmanned systems integration study",
                 "<p>How unmanned capability should be tasked, exploited, sustained and integrated "
                 "into controlled airspace alongside crewed operations.</p>"),
            ],
        ),

        sector_page(
            "internal-security",
            "Internal Security Agencies",
            "Sector · 05",
            "Capability, training and interoperability support across the Nigeria Police Force, "
            "NSCDC, Customs, Immigration and NDLEA.",
            desc="Advisory support to Nigerian internal security agencies: the Nigeria Police "
                 "Force, NSCDC, Nigeria Customs Service, Immigration Service and NDLEA — "
                 "capability development, training and interagency interoperability.",
            context='''          <p>
            Nigeria's internal security architecture involves many organisations with overlapping
            geography, distinct legal mandates and separate procurement routes. The Nigeria
            Police Force, the Nigeria Security and Civil Defence Corps, the Nigeria Customs
            Service, the Nigeria Immigration Service and the NDLEA each hold part of the
            picture and part of the response.
          </p>
          <p>
            The recurring finding is that interoperability, not equipment, is the constraint.
            Radios that cannot cross agencies, watchlists held in separate databases, unclear
            primacy at an incident, and evidence chains that break at the handover to a
            prosecuting authority. Each of those is fixable at modest cost, and each is
            harder to fix than buying a system, because it requires agreement between
            organisations.
          </p>
          <p>
            Our work with these agencies is deliberately framed around lawful, accountable
            capability: training that includes use-of-force and human rights standards as a
            competence rather than an add-on, and evidence and custody practices that hold up
            in court.
          </p>''',
            priorities=[
                ("Interagency interoperability",
                 "Communications, data sharing, incident primacy and joint operating centres "
                 "across agency boundaries."),
                ("Training and professional standards",
                 "Curriculum design including use of force, human rights and evidence handling "
                 "as assessed competencies."),
                ("Investigation and evidence capability",
                 "Case building, forensic access, custody discipline and coordination with "
                 "prosecuting authorities."),
                ("Border and port capability",
                 "Detection, screening, risk-based targeting and trade facilitation at ports "
                 "and land crossings."),
                ("Command and control",
                 "Control room design, dispatch, incident management and resource allocation."),
                ("Accountability mechanisms",
                 "Complaints handling, oversight, use-of-force reporting and internal "
                 "discipline processes."),
            ],
            services=[
                ("Training, Doctrine &amp; Simulation", "training-and-doctrine",
                 "Curriculum design and instructor development."),
                ("Border &amp; Maritime Security", "border-and-maritime",
                 "Border, port and waterway capability."),
                ("Cyber &amp; Information Defence", "cyber-and-information",
                 "Agency network and data protection."),
            ],
            engagements=[
                ("Interoperability assessment",
                 "<p>Establishing where two or more agencies cannot work together — radios, data, "
                 "authorities, procedures — and specifying the fixes in priority order, "
                 "distinguishing what needs procurement from what needs agreement.</p>"),
                ("Training curriculum review",
                 "<p>Review and redesign of agency training against the operational task, with "
                 "use of force, human rights and evidence handling built in as assessed "
                 "competencies rather than briefings.</p>"),
                ("Control room and dispatch design",
                 "<p>Design of a control room capability: call handling, incident management, "
                 "dispatch, resource visibility and the escalation and recording discipline "
                 "that supports later accountability.</p>"),
                ("Evidence and prosecution chain review",
                 "<p>Tracing cases from apprehension to court outcome to find where they fail, "
                 "and remediating the evidence, custody and handover process with the "
                 "prosecuting authority involved.</p>"),
                ("Accountability framework support",
                 "<p>Design of complaints handling, use-of-force reporting and internal oversight "
                 "mechanisms, including the data collection that makes them meaningful.</p>"),
            ],
        ),

        sector_page(
            "defence-industry",
            "Defence Industrial Base",
            "Sector · 06",
            "Local content, offset and technology transfer advisory — for Nigerian "
            "manufacturers building capability at home, and for foreign OEMs seeking a "
            "compliant route into the market.",
            desc="Defence industrial advisory: local content and offset structuring, technology "
                 "transfer, DICON and domestic supplier development, and compliant market entry "
                 "support for foreign OEMs in Nigeria.",
            context='''          <p>
            Every naira of defence equipment imported is a naira of industrial capability not
            built domestically, and a dependency on foreign spares and export licensing that
            constrains operational freedom. The strategic argument for a domestic defence
            industrial base is straightforward. Realising it is not.
          </p>
          <p>
            Genuine industrial capability requires sustained order books, technology transfer
            that includes design authority rather than assembly rights, quality systems that
            meet military standards, and a skills base built over years. Offset arrangements
            that deliver a screwdriver plant and a press release do not move the country
            forward.
          </p>
          <p>
            We work both sides of this. For Nigerian institutions — including the Defence
            Industries Corporation of Nigeria and domestic suppliers — we advise on capability
            strategy, partner selection and how to structure transfer terms that actually
            transfer something. For foreign OEMs, we advise on lawful, compliant market entry
            and realistic local content obligations.
          </p>''',
            priorities=[
                ("Local content strategy",
                 "What Nigeria should realistically build, buy or co-produce, sequenced by "
                 "industrial feasibility rather than ambition."),
                ("Offset structuring",
                 "Offset terms that transfer capability rather than assembly work, with "
                 "measurable, enforceable obligations."),
                ("Technology transfer terms",
                 "Design authority, technical data rights, licensing and the right to modify "
                 "and sustain independently."),
                ("Supplier development",
                 "Quality systems, military standards compliance and production capability for "
                 "domestic manufacturers."),
                ("Compliant market entry",
                 "For foreign OEMs: regulatory route, procurement process, agent risk and "
                 "anti-corruption compliance."),
                ("MRO localisation",
                 "Moving maintenance, repair and overhaul work in-country as the most "
                 "achievable first industrial step."),
            ],
            services=[
                ("Procurement &amp; Acquisition", "procurement-advisory",
                 "Contracting, offset terms and due diligence."),
                ("Sustainment &amp; MRO", "sustainment-and-mro",
                 "MRO localisation and depot capability."),
                ("Capability Development", "capability-development",
                 "Requirements that domestic industry can credibly meet."),
            ],
            engagements=[
                ("Local content strategy study",
                 "<p>An evidence-based assessment of which capability areas Nigeria can "
                 "realistically build domestically over a stated horizon, what investment each "
                 "requires, and the sequencing that gives the best industrial return.</p>"),
                ("Offset design and negotiation support",
                 "<p>Structuring offset obligations attached to a major acquisition so that the "
                 "obligation is measurable, enforceable and delivers transferable capability. "
                 "Includes the compliance monitoring regime.</p>"),
                ("Technology transfer assessment",
                 "<p>Assessing what a proposed transfer actually conveys: design authority, data "
                 "rights, the right to modify, and the ability to sustain independently of the "
                 "originating OEM.</p>"),
                ("Supplier capability development",
                 "<p>Working with a domestic manufacturer on quality systems, standards "
                 "compliance and production capability to reach the level required to supply "
                 "defence customers.</p>"),
                ("Market entry advisory for OEMs",
                 "<p>For foreign manufacturers: the regulatory and procurement landscape, "
                 "realistic local content expectations, agent and intermediary risk, and the "
                 "anti-corruption compliance requirements of operating in this market.</p>"
                 "<ul><li>We advise on process and compliance</li>"
                 "<li>We do not act as an agent, broker or reseller for any OEM</li>"
                 "<li>We do not accept success fees or commission on any sale</li></ul>"),
            ],
        ),
    ]
