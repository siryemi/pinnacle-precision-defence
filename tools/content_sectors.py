"""Sector pages: who the five capability pillars are applied for.

These pages apply the same capabilities to different customers. Each carries the
deck's own note that applications shown are proposed for discussion.
"""

from layout import (NAV_SECTORS, ARROW, ARROW_SM, page_hero, cta_band,
                    link_arrow, ruled, accordion, cards, DISCLAIMER)

_SUMMARIES = {
    "nigerian-army": "Barracks and accommodation, training grounds, armoured vehicle "
                     "maintenance hubs, logistics facilities and site infrastructure.",
    "defence-headquarters": "Joint infrastructure programmes, design assurance, procurement "
                            "governance and estate-wide asset management.",
    "naval-and-air-installations": "Base infrastructure, hangars and workshops, secure storage, "
                                   "and power and water resilience at naval and air stations.",
    "internal-security": "Facilities, training infrastructure and logistics discipline for "
                         "police and paramilitary services.",
    "defence-industrialisation": "Local assembly and maintenance hubs, university engineering "
                                 "partnerships and technology transfer.",
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
        <h2 class="d2">What we bring to this customer</h2>
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
        <h2 class="d2">Proposed applications for discussion</h2>
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
        "The same five capability pillars, applied to the institutions responsible for "
        "Nigeria's defence and internal security, and to the domestic industrial base that "
        "will eventually equip them.",
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
          <p class="eyebrow">Our primary focus</p>
          <h2 class="d2">Positioned first for the Nigerian Army</h2>
          <p class="lede mt-16">
            Our capability profile is written to support Nigerian Army infrastructure
            resilience, operational readiness and long-term modernization programmes. That is
            where our engagement is directed first.
          </p>
        </div>
        <div class="prose">
          <p>
            The other customers listed here represent the same capabilities applied to
            different estates. Barracks construction, secure storage, power and water
            resilience and asset management are needed at a naval base or a police training
            college as much as at an Army formation, the engineering does not change, only
            the customer and the governance route.
          </p>
          <p>
            Where a scope needs capability beyond the five pillars, we bring in a named partner
            rather than stretch to cover it.
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
            "security agencies and the domestic defence industrial base.",
            body)


def all_sector_pages():
    return [
        sectors_index(),

        sector_page(
            "nigerian-army",
            "Nigerian Army",
            "Sector · 01",
            "Infrastructure resilience, operational readiness and long-term modernization "
            "support for the Nigerian Army, our primary focus.",
            desc="Engineering, construction, supply chain and modernization support for the "
                 "Nigerian Army: barracks, training grounds, armoured vehicle maintenance hubs, "
                 "logistics facilities and site infrastructure.",
            context='''          <p>
            The Nigerian Army has been continuously committed to internal security operations
            across several theatres for well over a decade. That tempo leaves little
            institutional slack for the infrastructure and maintenance work that sustains
            long-term readiness, accommodation is occupied harder than it was designed for,
            vehicles are used beyond planned rates, and facility maintenance is deferred.
          </p>
          <p>
            Our capability profile is positioned specifically to support Army infrastructure
            resilience and readiness. In practice that means the unglamorous work with the
            highest return: keeping power and water on, raising vehicle availability through
            better maintenance hubs and spares visibility, and building accommodation and
            training facilities specified to survive intensive use on a constrained maintenance
            budget.
          </p>
          <p>
            We work to formation-level realities rather than headquarters assumptions. Phase
            two of our roadmap is built around structured listening sessions with unit
            commanders precisely because the binding constraint is usually not the one in the
            formal reporting.
          </p>''',
            priorities=[
                ("Vehicle availability",
                 "Maintenance hub design, diagnostics, workflow and spares visibility, the "
                 "fastest route to more usable vehicles from the fleet already owned."),
                ("Accommodation and barracks",
                 "Durable, maintainable accommodation with efficient utilities, specified on "
                 "whole-life rather than capital cost."),
                ("Training infrastructure",
                 "Ranges, classrooms, workshops and simulation rooms with supporting civil works."),
                ("Power and water resilience",
                 "Mini-grid support, borehole and water systems and backup generation, with the "
                 "maintenance regime to sustain them."),
                ("Logistics and stores discipline",
                 "Warehousing layout, inventory visibility and vendor governance so stock is "
                 "known and replenished."),
                ("Command facilities",
                 "Resilient command and communications spaces with protected utilities."),
            ],
            services=[
                ("Military Construction", "military-construction",
                 "Barracks, training grounds and site infrastructure."),
                ("Modernization Consulting", "modernization-consulting",
                 "Vehicle availability and asset management."),
                ("Defence Supply Chain", "defence-supply-chain",
                 "Equipment selection, sourcing and inventory control."),
            ],
            engagements=[
                ("Armoured vehicle maintenance hub",
                 "<p>Diagnostics capability, workflow design, inventory visibility and predictive "
                 "maintenance built around a vehicle fleet, aimed directly at raising the "
                 "proportion of the fleet that is mission-capable.</p>"),
                ("Military housing and barracks",
                 "<p>Durable, sustainable and maintainable accommodation with efficient "
                 "utilities, delivered so that maintenance burden after handover is designed "
                 "down rather than discovered.</p>"),
                ("Training facilities",
                 "<p>Ranges, classrooms, workshops, simulation rooms and supporting civil works, "
                 "sequenced so existing training continues during construction.</p>"),
                ("Water and power resilience",
                 "<p>Mini-grid support, borehole and water systems, backup generation and "
                 "lifecycle maintenance, frequently the highest readiness return per naira on "
                 "an established site.</p>"),
                ("Operational gap analysis with commanders",
                 "<p>Structured listening sessions mapping communication gaps, mobility "
                 "limitations, surveillance blind spots, equipment fatigue and maintenance "
                 "challenges into an addressable, prioritised solution set.</p>"),
            ],
        ),

        sector_page(
            "defence-headquarters",
            "Ministry of Defence &amp; Defence Headquarters",
            "Sector · 02",
            "Joint infrastructure programmes, design assurance and procurement governance at "
            "the centre, where estate-wide decisions are made and audited.",
            desc="Support to Nigeria's Ministry of Defence and Defence Headquarters: joint "
                 "infrastructure programmes, design assurance, procurement governance and "
                 "estate-wide asset management.",
            context='''          <p>
            The centre carries decisions no single formation can make: which infrastructure
            investments to fund across competing service demands, whether a submitted design and
            cost estimate are credible, and how to demonstrate afterwards that public money
            achieved what was approved.
          </p>
          <p>
            Our contribution there is analytical and assurance-focused. Independent design and
            cost review gives the centre the ability to interrogate a submission on its merits.
            Estate-wide asset registers and condition data turn infrastructure budgeting from an
            annual argument into a prioritised programme. Documented procurement and handover
            discipline produces the audit trail that protects the officers who approved the
            spend.
          </p>
          <p>
            Audit readiness is a recurring theme in our work because on public infrastructure it
            is not administrative overhead, it is the difference between a defensible programme
            and an exposed one.
          </p>''',
            priorities=[
                ("Design and cost assurance",
                 "Independent review of submitted designs and estimates before approval, so the "
                 "centre can challenge on evidence."),
                ("Estate-wide asset management",
                 "Asset registers, condition assessment and criticality ranking across multiple "
                 "sites to support prioritised investment."),
                ("Procurement governance",
                 "Vendor qualification standards, documentation requirements and performance "
                 "monitoring applied consistently across programmes."),
                ("Programme documentation and audit readiness",
                 "Evidence assembled during delivery rather than reconstructed after a query."),
                ("Lifecycle cost analysis",
                 "Whole-life costing so infrastructure decisions account for the maintenance "
                 "liability they create."),
                ("Standardisation",
                 "Repeatable design and specification standards across an estate to reduce cost "
                 "and simplify maintenance."),
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
                 "<p>A separate technical and cost opinion on a submitted infrastructure package "
                 "before it reaches the approving authority, buildability, maintainability, "
                 "specification appropriateness and whether the estimate is credible.</p>"),
                ("Estate condition and asset survey",
                 "<p>Structured condition assessment across multiple sites producing an asset "
                 "register, criticality ranking and prioritised remediation programme with "
                 "costs.</p>"),
                ("Procurement governance framework",
                 "<p>Vendor prequalification criteria, documentation standards, performance "
                 "monitoring and retention requirements, designed to be applied consistently "
                 "and to withstand audit.</p>"),
                ("Design standardisation programme",
                 "<p>Development of repeatable design and specification standards for recurring "
                 "facility types across an estate, reducing per-project design cost and "
                 "simplifying maintenance and spares.</p>"),
            ],
        ),

        sector_page(
            "naval-and-air-installations",
            "Naval &amp; Air Installations",
            "Sector · 03",
            "Base infrastructure, hangars and workshops, secure storage and utility resilience "
            "at naval and air stations.",
            desc="Engineering and construction support for Nigerian naval and air installations: "
                 "base infrastructure, hangars and workshops, secure storage, and power and water "
                 "resilience.",
            context='''          <p>
            Naval and air installations concentrate high-value equipment in a small number of
            fixed locations, which makes their infrastructure disproportionately important. A
            workshop without reliable power cannot complete maintenance. A hangar with a failing
            roof damages what it was built to protect. A dockside or apron surface in poor
            condition constrains everything that moves across it.
          </p>
          <p>
            The engineering here is the same as elsewhere in our profile, secure design,
            durable construction, utility resilience, asset management, applied to buildings
            and infrastructure with demanding technical requirements and low tolerance for
            downtime.
          </p>
          <p>
            We are an engineering and construction firm, not a naval architect or an aviation
            authority. Our scope is the facilities and infrastructure that support platforms,
            not the platforms themselves.
          </p>''',
            priorities=[
                ("Workshops and maintenance facilities",
                 "Facilities designed around the maintenance workflow, with the power, lifting "
                 "and services the work actually requires."),
                ("Hangars and covered storage",
                 "Structures protecting high-value equipment, specified for the local climate "
                 "and maintainable over decades."),
                ("Secure storage",
                 "Controlled-access stores with appropriate structural protection and inventory "
                 "visibility."),
                ("Power and water resilience",
                 "Backup generation, distribution and water systems on sites where interruption "
                 "stops technical work."),
                ("Civil infrastructure",
                 "Roads, hardstanding, drainage and site services supporting movement and "
                 "operations."),
                ("Facility asset management",
                 "Condition monitoring and planned maintenance for technical buildings and "
                 "their systems."),
            ],
            services=[
                ("Defence Engineering Design", "engineering-design",
                 "Technical building and MEP design."),
                ("Military Construction", "military-construction",
                 "Construction and commissioning of facilities."),
                ("Modernization Consulting", "modernization-consulting",
                 "Facility condition monitoring and maintenance planning."),
            ],
            engagements=[
                ("Workshop or maintenance facility delivery",
                 "<p>Design and construction of a technical maintenance facility built around "
                 "the workflow it must support, services, lifting provision, layout, lighting "
                 "and the utility resilience to keep work moving.</p>"),
                ("Hangar or covered storage construction",
                 "<p>Structures protecting high-value equipment, specified for climate, "
                 "durability and long-term maintainability rather than lowest capital cost.</p>"),
                ("Secure storage facility",
                 "<p>Controlled-access stores with appropriate structural protection, "
                 "environmental control where required, and layouts that keep inventory "
                 "visible.</p>"),
                ("Base utility resilience programme",
                 "<p>Assessment and upgrade of power and water systems across an installation, "
                 "prioritised by the operational consequence of each failure mode.</p>"),
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
            Police and paramilitary services operate from a far larger and more dispersed estate
            than the military, usually with a smaller per-site maintenance budget. The result is
            a familiar pattern: accommodation and station buildings in poor condition, training
            facilities that constrain throughput, and stores where nobody can say with confidence
            what is held.
          </p>
          <p>
            The same pillars apply. Durable, maintainable construction; utility resilience;
            vendor qualification and inventory visibility; and asset management that lets a
            central authority prioritise across many sites rather than reacting to whichever one
            escalates loudest.
          </p>
          <p>
            Because this estate is large and dispersed, standardisation delivers more here than
            anywhere else in our profile, repeatable designs and common specifications reduce
            both construction cost and maintenance complexity.
          </p>''',
            priorities=[
                ("Station and office facilities",
                 "Durable, maintainable buildings with efficient utilities across a dispersed "
                 "estate."),
                ("Training infrastructure",
                 "Classrooms, workshops, ranges and accommodation that support required "
                 "throughput."),
                ("Accommodation",
                 "Personnel accommodation specified for intensive use and low maintenance "
                 "burden."),
                ("Standardised design",
                 "Repeatable designs and specifications to control cost and simplify maintenance "
                 "across many sites."),
                ("Stores and inventory discipline",
                 "Vendor qualification, categorisation and inventory visibility across "
                 "distributed holdings."),
                ("Estate condition data",
                 "Condition assessment and prioritisation so central budgets go to the highest "
                 "consequence sites first."),
            ],
            services=[
                ("Military Construction", "military-construction",
                 "Facilities, accommodation and training infrastructure."),
                ("Defence Supply Chain", "defence-supply-chain",
                 "Vendor governance and inventory visibility."),
                ("Modernization Consulting", "modernization-consulting",
                 "Estate condition assessment and prioritisation."),
            ],
            engagements=[
                ("Training college infrastructure",
                 "<p>Classrooms, workshops, ranges, accommodation and supporting civil works "
                 "sized to the training throughput the agency actually needs to achieve.</p>"),
                ("Standardised station design programme",
                 "<p>A repeatable design and specification set for recurring facility types "
                 "across a dispersed estate, cutting per-project design cost and simplifying "
                 "maintenance and spares.</p>"),
                ("Estate condition survey and prioritisation",
                 "<p>Condition assessment across sites producing a ranked remediation programme, "
                 "so central budget allocation is driven by consequence rather than "
                 "escalation.</p>"),
                ("Stores and logistics discipline",
                 "<p>Vendor qualification, categorisation, reorder planning and warehousing "
                 "process design across distributed holdings.</p>"),
            ],
        ),

        sector_page(
            "defence-industrialisation",
            "Defence Industrialisation",
            "Sector · 05",
            "Local assembly and maintenance hubs, university engineering partnerships and "
            "technology transfer, the long-term goal our earlier phases are building toward.",
            desc="Supporting Nigerian defence industrialisation: local assembly and maintenance "
                 "hubs, engineering partnerships with universities and research centres, "
                 "technology transfer and local workforce development.",
            context='''          <p>
            Every naira of defence equipment imported is a naira of industrial capability not
            built at home, and a dependency on foreign spares and export licensing that
            constrains operational freedom. The strategic case for a domestic defence industrial
            base is straightforward. Building one is not.
          </p>
          <p>
            Real industrial capability needs sustained order books, technology transfer that
            conveys design authority rather than assembly rights, quality systems meeting
            military standards, and a skills base built over years. Arrangements that deliver a
            screwdriver plant and a press release do not advance the country.
          </p>
          <p>
            This is the third phase of our roadmap, and we are explicit that it follows the
            first two rather than replacing them. Our route into it is the most achievable one:
            maintenance and repair localisation first, then assembly, then design, for
            non-weaponized systems including tactical vehicles, communication systems,
            surveillance platforms, protective equipment and field gear.
          </p>''',
            priorities=[
                ("MRO localisation",
                 "Moving maintenance, repair and overhaul work in country, the most achievable "
                 "first industrial step and the one that most improves availability."),
                ("Local assembly and maintenance hubs",
                 "Facilities, tooling, quality systems and technician capability for in-country "
                 "assembly and support."),
                ("University and research partnerships",
                 "Engineering partnerships with Nigerian universities and research centres to "
                 "build the design base."),
                ("Technology transfer",
                 "Structured transfer conveying design authority and the right to modify and "
                 "sustain independently."),
                ("Local workforce development",
                 "Engineer and technician pipelines sized to the industrial capability being "
                 "built."),
                ("Joint R&amp;D programmes",
                 "Co-developed research with domestic institutions on non-weaponized systems."),
            ],
            services=[
                ("Defence Engineering Design", "engineering-design",
                 "The design capability an industrial base requires."),
                ("Modernization Consulting", "modernization-consulting",
                 "Maintenance capability and asset management."),
                ("Defence Supply Chain", "defence-supply-chain",
                 "Supplier development and quality systems."),
            ],
            engagements=[
                ("Maintenance hub establishment",
                 "<p>Design and delivery of an in-country maintenance and repair facility, "
                 "capacity planning, workflow, tooling, test equipment and the technician "
                 "competence framework to operate it.</p>"),
                ("Local assembly feasibility study",
                 "<p>Assessment of which non-weaponized systems could credibly be assembled in "
                 "Nigeria over a stated horizon, what investment each requires, and the "
                 "sequencing that gives the best industrial return.</p>"),
                ("University engineering partnership design",
                 "<p>Structuring a working partnership with Nigerian universities and research "
                 "centres, research agenda, funding model, student pipeline and intellectual "
                 "property arrangements.</p>"),
                ("Technology transfer assessment",
                 "<p>Assessing what a proposed transfer actually conveys: design authority, "
                 "technical data rights, the right to modify, and the ability to sustain "
                 "independently of the originating manufacturer.</p>"),
                ("Workforce development programme",
                 "<p>Recruitment, training and qualification pipeline for the engineers and "
                 "technicians an industrial capability depends on.</p>"),
            ],
        ),
    ]
