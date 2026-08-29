"""Sector pages: who the five capability pillars are applied for.

Same capabilities, different customers. Each page carries the deck's note that
applications shown are proposed for discussion.

Copy is deliberately tight. Short sentences, one idea per line.
"""

from layout import (NAV_SECTORS, ARROW, ARROW_SM, page_hero, cta_band,
                    link_arrow, ruled, accordion, cards, DISCLAIMER)

_SUMMARIES = {
    "nigerian-army": "Barracks, training grounds, vehicle maintenance hubs, logistics and site "
                     "infrastructure.",
    "defence-headquarters": "Joint programmes, design assurance, procurement governance and "
                            "estate asset management.",
    "naval-and-air-installations": "Base infrastructure, hangars, workshops, secure storage, "
                                   "power and water resilience.",
    "internal-security": "Facilities, training infrastructure and logistics discipline for "
                         "police and paramilitary services.",
    "defence-industrialisation": "Local assembly and maintenance hubs, university partnerships "
                                 "and technology transfer.",
}


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
          <p class="eyebrow">Where we are most useful</p>
          {ruled(priorities)}
          <div class="mt-32">{DISCLAIMER}</div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Capability pillars</p>
        <h2 class="d2">What we bring here</h2>
      </div>
      <div class="grid grid--3">
        {svc}
      </div>
    </div>
  </section>

  <section class="section section--ink2 section--line">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Applications</p>
        <h2 class="d2">Proposed for discussion</h2>
      </div>
      {accordion("sec-" + slug, engagements)}
    </div>
  </section>

''' + cta_band()

    return (f"sectors/{slug}.html", title, desc, body)


def sectors_index():
    items = [(label, _SUMMARIES[slug], f"sectors/{slug}.html")
             for slug, label, _ in NAV_SECTORS]

    body = page_hero(
        "Sectors",
        "Who we support",
        "The same five pillars, applied to the institutions responsible for Nigeria's defence "
        "and internal security, and to the industrial base that will equip them.",
        trail=[("Sectors", None)],
    )

    body += f'''
  <section class="section">
    <div class="shell">
      {cards(items, cols=3)}
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Primary focus</p>
          <h2 class="d2">Positioned first for the Nigerian Army</h2>
          <p class="lede mt-16">
            Our profile is written for Army infrastructure resilience, readiness and
            modernization. That is where engagement is directed first.
          </p>
        </div>
        <div class="prose">
          <p>
            The other customers here are the same capabilities on different estates. Barracks,
            secure storage, utility resilience and asset management are needed at a naval base or
            a police college as much as at an Army formation. The engineering does not change,
            only the customer and the governance route.
          </p>
          <p>{link_arrow("See the five capability pillars", "capabilities/index.html")}</p>
        </div>
      </div>
    </div>
  </section>

''' + cta_band()

    return ("sectors/index.html", "Sectors",
            "Defence infrastructure, construction, supply chain and modernization support for "
            "the Nigerian Army, Ministry of Defence, naval and air installations, internal "
            "security agencies and the defence industrial base.",
            body)


def all_sector_pages():
    return [
        sectors_index(),

        sector_page(
            "nigerian-army",
            "Nigerian Army",
            "Sector · 01",
            "Infrastructure resilience, readiness and modernization support. Our primary focus.",
            desc="Engineering, construction, supply chain and modernization support for the "
                 "Nigerian Army: barracks, training grounds, vehicle maintenance hubs and site "
                 "infrastructure.",
            context='''          <p>
            The Army has been committed to internal security operations across several theatres
            for over a decade. That tempo leaves little slack for the work that sustains
            readiness. Accommodation is occupied harder than it was designed for, vehicles run
            beyond planned rates, facility maintenance is deferred.
          </p>
          <p>
            We focus on the unglamorous work with the highest return: keeping power and water on,
            raising vehicle availability through better hubs and spares visibility, and building
            accommodation specified to survive hard use on a tight maintenance budget.
          </p>''',
            priorities=[
                ("Vehicle availability",
                 "Maintenance hub design, diagnostics, workflow and spares visibility."),
                ("Accommodation",
                 "Durable, maintainable barracks with efficient utilities."),
                ("Training infrastructure",
                 "Ranges, classrooms, workshops and simulation rooms."),
                ("Power and water resilience",
                 "Mini-grid, borehole and backup generation, with the maintenance regime."),
            ],
            services=[
                ("Military Construction", "military-construction",
                 "Barracks, training grounds, site infrastructure."),
                ("Modernization Consulting", "modernization-consulting",
                 "Vehicle availability and asset management."),
                ("Defence Supply Chain", "defence-supply-chain",
                 "Equipment selection, sourcing, inventory."),
            ],
            engagements=[
                ("Armoured vehicle maintenance hub",
                 "<p>Diagnostics, workflow design, inventory visibility and predictive maintenance "
                 "around a fleet, aimed at raising the mission-capable proportion.</p>"),
                ("Barracks and accommodation",
                 "<p>Durable accommodation with efficient utilities, with maintenance burden "
                 "designed down rather than discovered.</p>"),
                ("Training facilities",
                 "<p>Ranges, classrooms, workshops and civil works, sequenced so training "
                 "continues during construction.</p>"),
            ],
        ),

        sector_page(
            "defence-headquarters",
            "Ministry of Defence &amp; Defence Headquarters",
            "Sector · 02",
            "Joint programmes, design assurance and procurement governance at the centre.",
            desc="Support to Nigeria's Ministry of Defence and Defence Headquarters: joint "
                 "infrastructure programmes, design assurance, procurement governance and estate "
                 "asset management.",
            context='''          <p>
            The centre makes decisions no single formation can: which investments to fund across
            competing service demands, whether a submitted design and cost are credible, and how
            to show afterwards that public money achieved what was approved.
          </p>
          <p>
            Our contribution is analytical. Independent review lets the centre interrogate a
            submission on evidence. Estate-wide asset registers turn infrastructure budgeting from
            an annual argument into a prioritised programme. Documented delivery produces the audit
            trail that protects the officers who approved the spend.
          </p>''',
            priorities=[
                ("Design and cost assurance",
                 "Independent review of submitted designs and estimates before approval."),
                ("Estate asset management",
                 "Registers, condition assessment and criticality ranking across sites."),
                ("Procurement governance",
                 "Vendor standards, documentation and performance monitoring applied consistently."),
                ("Audit readiness",
                 "Evidence assembled during delivery, not reconstructed after a query."),
            ],
            services=[
                ("Defence Engineering Design", "engineering-design",
                 "Design assurance and technical review."),
                ("Modernization Consulting", "modernization-consulting",
                 "Estate asset management and lifecycle cost."),
                ("Defence Supply Chain", "defence-supply-chain",
                 "Vendor governance across programmes."),
            ],
            engagements=[
                ("Independent design and cost review",
                 "<p>A separate technical and cost opinion before a package reaches the approving "
                 "authority: buildability, maintainability, specification, and whether the estimate "
                 "is credible.</p>"),
                ("Estate condition survey",
                 "<p>Condition assessment across sites producing an asset register, criticality "
                 "ranking and a costed remediation programme.</p>"),
                ("Procurement governance framework",
                 "<p>Prequalification criteria, documentation standards, performance monitoring and "
                 "retention requirements, designed to withstand audit.</p>"),
            ],
        ),

        sector_page(
            "naval-and-air-installations",
            "Naval &amp; Air Installations",
            "Sector · 03",
            "Base infrastructure, hangars, workshops, secure storage and utility resilience.",
            desc="Engineering and construction for Nigerian naval and air installations: base "
                 "infrastructure, hangars, workshops, secure storage, power and water resilience.",
            context='''          <p>
            Naval and air installations concentrate high-value equipment in a few fixed locations,
            which makes their infrastructure disproportionately important. A workshop without
            reliable power cannot complete maintenance. A hangar with a failing roof damages what
            it was built to protect.
          </p>
          <p>
            The engineering is the same as elsewhere in our profile, applied to buildings with
            demanding technical requirements and low tolerance for downtime. Our scope is the
            facilities that support platforms.
          </p>''',
            priorities=[
                ("Workshops and maintenance facilities",
                 "Designed around the workflow, with the power, lifting and services it needs."),
                ("Hangars and covered storage",
                 "Structures protecting high-value equipment, specified for climate and decades of upkeep."),
                ("Secure storage",
                 "Controlled-access stores with structural protection and inventory visibility."),
                ("Power and water resilience",
                 "Backup generation on sites where interruption stops technical work."),
            ],
            services=[
                ("Defence Engineering Design", "engineering-design",
                 "Technical building and MEP design."),
                ("Military Construction", "military-construction",
                 "Construction and commissioning."),
                ("Modernization Consulting", "modernization-consulting",
                 "Condition monitoring and maintenance planning."),
            ],
            engagements=[
                ("Workshop or maintenance facility",
                 "<p>Design and construction built around the workflow: services, lifting "
                 "provision, layout, lighting and the utility resilience to keep work moving.</p>"),
                ("Hangar or covered storage",
                 "<p>Structures protecting high-value equipment, specified for climate and "
                 "long-term maintainability rather than lowest capital cost.</p>"),
                ("Secure storage facility",
                 "<p>Controlled access, structural protection, environmental control where "
                 "required, and layouts that keep inventory visible.</p>"),
            ],
        ),

        sector_page(
            "internal-security",
            "Internal Security Agencies",
            "Sector · 04",
            "Facilities, training infrastructure and logistics discipline for police and "
            "paramilitary services.",
            desc="Engineering, construction and logistics support for Nigerian internal security "
                 "agencies: facilities, training infrastructure, accommodation and supply chain "
                 "discipline.",
            context='''          <p>
            Police and paramilitary services run a far larger and more dispersed estate than the
            military, usually on a smaller per-site maintenance budget. The pattern is familiar:
            station buildings in poor condition, training facilities that cap throughput, and
            stores where nobody can say what is held.
          </p>
          <p>
            Standardisation delivers more here than anywhere else in our profile. Repeatable
            designs and common specifications cut both construction cost and maintenance
            complexity across many sites.
          </p>''',
            priorities=[
                ("Station and office facilities",
                 "Durable, maintainable buildings with efficient utilities across a dispersed estate."),
                ("Training infrastructure",
                 "Classrooms, workshops, ranges and accommodation sized to required throughput."),
                ("Accommodation",
                 "Personnel accommodation specified for intensive use and low upkeep."),
                ("Standardised design",
                 "Repeatable designs to control cost and simplify maintenance across sites."),
            ],
            services=[
                ("Military Construction", "military-construction",
                 "Facilities, accommodation, training infrastructure."),
                ("Defence Supply Chain", "defence-supply-chain",
                 "Vendor governance and inventory visibility."),
                ("Modernization Consulting", "modernization-consulting",
                 "Estate condition assessment and prioritisation."),
            ],
            engagements=[
                ("Training college infrastructure",
                 "<p>Classrooms, workshops, ranges, accommodation and civil works, sized to the "
                 "throughput the agency needs to achieve.</p>"),
                ("Standardised station design",
                 "<p>A repeatable design and specification set for recurring facility types, "
                 "cutting per-project design cost and simplifying spares.</p>"),
                ("Estate condition survey",
                 "<p>Assessment across sites producing a ranked remediation programme, so budget "
                 "allocation follows consequence rather than escalation.</p>"),
            ],
        ),

        sector_page(
            "defence-industrialisation",
            "Defence Industrialisation",
            "Sector · 05",
            "Local assembly and maintenance hubs, university partnerships and technology "
            "transfer. The long-term goal.",
            desc="Supporting Nigerian defence industrialisation: local assembly and maintenance "
                 "hubs, university engineering partnerships, technology transfer and workforce "
                 "development.",
            context='''          <p>
            Every naira of equipment imported is industrial capability not built at home, and a
            dependency on foreign spares and export licensing that limits operational freedom. The
            strategic case is straightforward. Building it is not.
          </p>
          <p>
            Real capability needs sustained order books, transfer that conveys design authority
            rather than assembly rights, quality systems meeting military standards, and a skills
            base built over years. Our route in is the achievable one: maintenance and repair
            localisation first, then assembly, then design.
          </p>''',
            priorities=[
                ("MRO localisation",
                 "Moving maintenance and overhaul in country. The step that most improves availability."),
                ("Local assembly hubs",
                 "Facilities, tooling, quality systems and technician capability."),
                ("University partnerships",
                 "Engineering partnerships with Nigerian universities and research centres."),
                ("Technology transfer",
                 "Transfer conveying design authority and the right to modify and sustain."),
            ],
            services=[
                ("Defence Engineering Design", "engineering-design",
                 "The design capability an industrial base needs."),
                ("Modernization Consulting", "modernization-consulting",
                 "Maintenance capability and asset management."),
                ("Defence Supply Chain", "defence-supply-chain",
                 "Supplier development and quality systems."),
            ],
            engagements=[
                ("Maintenance hub establishment",
                 "<p>Design and delivery of an in-country repair facility: capacity, workflow, "
                 "tooling, test equipment and the technician competence framework.</p>"),
                ("Local assembly feasibility",
                 "<p>Which non-weaponized systems could credibly be assembled in Nigeria, what each "
                 "requires, and the sequencing with the best industrial return.</p>"),
                ("University partnership design",
                 "<p>Research agenda, funding model, student pipeline and intellectual property "
                 "arrangements with Nigerian universities.</p>"),
            ],
        ),
    ]
