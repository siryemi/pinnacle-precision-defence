"""Capability pages: the /capabilities index plus the four pillars.

Content source: pinnacle_precision_defense_profile.pptx (slides 2, 4, 5, 6, 7, 8).
Nothing here should assert a capability absent from that deck.
"""

from layout import (NAV_CAPABILITIES, ARROW, ARROW_SM, page_hero, cta_band,
                    link_arrow, ruled, accordion, cards, DISCLAIMER)

_SUMMARIES = {
    "engineering-design": "Secure facilities, command-and-control spaces, blast-aware "
                          "structural design, MEP systems and 3D CAD/BIM documentation "
                          "from FEED through IFC.",
    "military-construction": "Bases, barracks, training grounds, logistics hubs, perimeter "
                             "infrastructure, secure storage and civil/structural works.",
    "defence-supply-chain": "Vendor qualification, strategic sourcing, logistics coordination, "
                            "inventory dashboards and lifecycle support for non-sensitive "
                            "equipment and services.",
    "modernization-consulting": "Risk assessments, asset management, lifecycle cost analysis, "
                                "digital transformation, IoT pilots and predictive maintenance.",
}


def capability_page(slug, title, eyebrow, lede, intro, workstreams, engagements,
                    deliverables, related, desc, extra=""):
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
          <p class="eyebrow">What the work includes</p>
          {ruled(workstreams)}
        </div>
      </div>
    </div>
  </section>
{extra}
  <section class="section section--paper">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Applications</p>
        <h2 class="d2">How this work typically arrives</h2>
        <p class="lede mt-16">Representative engagement shapes. All work proceeds within the
          formal procurement, governance, security and confidentiality requirements set by the
          client.</p>
      </div>
      {accordion("eng-" + slug, engagements)}
      <div class="mt-40">{DISCLAIMER}</div>
    </div>
  </section>

  <section class="section section--ink2 section--line">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Deliverables</p>
        <h2 class="d2">What the client is left holding</h2>
      </div>
      {cards(deliverables)}
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


def capabilities_index():
    items = [
        (label, _SUMMARIES[slug], f"capabilities/{slug}.html")
        for slug, label, _ in NAV_CAPABILITIES
    ]

    body = page_hero(
        "Capabilities",
        "Four capability pillars for defence infrastructure and modernization",
        "Secure engineering design, reliable construction, disciplined supply chain management "
        "and modernization consulting — framed for defence stakeholders as secure, "
        "maintainable, auditable and readiness-oriented delivery at every stage.",
        trail=[("Capabilities", None)],
    )

    body += f'''
  <section class="section">
    <div class="shell">
      {cards(items, cols=2)}
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Why it matters</p>
        <h2 class="d2">Three readiness outcomes we design for</h2>
        <p class="lede mt-16">
          Each pillar exists to move one of these. If a proposed scope does not move any of
          them, it is the wrong scope.
        </p>
      </div>
      <div class="grid grid--4">
        <div class="card"><p class="card__num">01</p><h3>Reduce mission risk</h3>
          <p>Structured design reviews, quality controls and lifecycle thinking reduce
          infrastructure and delivery risk.</p></div>
        <div class="card"><p class="card__num">02</p><h3>Accelerate delivery</h3>
          <p>Integrated engineering, procurement and construction workflows improve
          time-to-readiness.</p></div>
        <div class="card"><p class="card__num">03</p><h3>Improve asset uptime</h3>
          <p>IoT sensors, analytics and predictive maintenance support vehicle, generator and
          facility uptime.</p></div>
        <div class="card"><p class="card__num">04</p><h3>Strengthen accountability</h3>
          <p>Transparent vendor qualification, documentation and handover discipline support
          full auditability.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Engagement model</p>
          <h2 class="d2">Assess, design, deliver, sustain</h2>
          <p class="lede mt-16">
            A practical path from needs assessment to lifecycle support. The same four stages
            apply whether the scope is a single facility or a multi-site programme.
          </p>
          <div class="actions mt-32">
            <a class="btn btn--ghost" href="{{P}}roadmap/index.html">See the phased roadmap</a>
          </div>
        </div>
        <div class="steps">
          <div class="step"><div><h3>Assess</h3></div>
            <p>Confirm requirements, site realities, operational constraints and risk profile.</p></div>
          <div class="step"><div><h3>Design</h3></div>
            <p>Develop FEED, BIM/CAD and IFC packages, alongside cost logic and execution
            strategy.</p></div>
          <div class="step"><div><h3>Deliver</h3></div>
            <p>Manage procurement, construction interfaces, quality controls and
            commissioning.</p></div>
          <div class="step"><div><h3>Sustain</h3></div>
            <p>Support handover, training, asset data capture and maintenance-readiness
            planning.</p></div>
        </div>
      </div>
    </div>
  </section>

''' + cta_band()

    return ("capabilities/index.html", "Capabilities",
            "Four defence-aligned capability pillars: engineering design, military "
            "construction, defence supply chain and modernization consulting.",
            body)


def all_capability_pages():
    return [
        capabilities_index(),

        capability_page(
            "engineering-design",
            "Defence Engineering Design",
            "Capability · Pillar 01",
            "Secure-by-design engineering for facilities where reliability, access control and "
            "continuity of operations are non-negotiable.",
            desc="Defence engineering design: secure facilities, command-and-control spaces, "
                 "blast-aware structural design, MEP systems and 3D CAD/BIM documentation from "
                 "FEED through IFC.",
            intro='''          <p>
            Defence infrastructure carries requirements that ordinary commercial design does not
            address. A command-and-control space has to hold power, cooling and communications
            through a utility failure. A secure store has to control access and survive an
            attempt to force it. A structure in an exposed location has to be designed with
            blast and ballistic considerations built into the frame, not added afterwards.
          </p>
          <p>
            We take those requirements into the design from the outset and carry them through
            documented, reviewable stages — front-end engineering design, through detailed
            design, to issued-for-construction packages. The deliverable is a coordinated set
            of drawings and models that a construction team can build from and that the client's
            own engineers can maintain against for the life of the asset.
          </p>
          <p>
            Design continuity matters as much as the design itself. BIM models are structured so
            facility data survives into operations rather than being abandoned at handover,
            which is where most of the long-term value of a digital model is normally lost.
          </p>''',
            workstreams=[
                ("Secure facility design",
                 "Access control, compartmentalisation, hardened envelopes and continuity of "
                 "operations designed in from concept stage."),
                ("Command-and-control spaces",
                 "Communication rooms, operations floors, resilient power and cooling, and the "
                 "cable management that keeps them serviceable."),
                ("Blast-aware structural design",
                 "Structural design accounting for blast and ballistic considerations "
                 "appropriate to the threat and location."),
                ("MEP systems",
                 "Mechanical, electrical and plumbing design including backup generation, "
                 "water systems and protected distribution."),
                ("3D CAD and BIM documentation",
                 "Coordinated models and drawing sets carried from FEED through to "
                 "issued-for-construction, structured for use in operations."),
                ("Design review and assurance",
                 "Structured multi-discipline reviews with recorded comments and close-out, so "
                 "design decisions are traceable."),
            ],
            engagements=[
                ("Secure command centre design",
                 "<p>Design of a command or operations facility: resilient building envelope, "
                 "protected MEP systems, backup utilities and communication-room readiness, with "
                 "continuity of operations as the governing requirement.</p>"),
                ("FEED study for a new facility",
                 "<p>Front-end engineering design establishing scope, technical basis, cost logic "
                 "and execution strategy to the point where a construction procurement can be "
                 "run with confidence.</p><ul>"
                 "<li>Options studied and compared before a design is fixed</li>"
                 "<li>Cost logic documented so the estimate can be interrogated</li></ul>"),
                ("Design assurance on an existing package",
                 "<p>Independent multi-discipline review of a design already produced — "
                 "buildability, maintainability, security requirements, MEP coordination and "
                 "compliance — delivered as a prioritised comment register.</p>"),
                ("BIM implementation for an estate",
                 "<p>Establishing a BIM standard and model structure for a facility or estate so "
                 "that asset data captured during design remains usable by the maintenance "
                 "organisation afterwards.</p>"),
            ],
            deliverables=[
                ("FEED package", "Technical basis, options assessment, cost logic and execution strategy."),
                ("Coordinated 3D/BIM model", "Multi-discipline model structured for handover into operations."),
                ("IFC drawing set", "Issued-for-construction drawings a contractor can build from."),
                ("MEP design and calculations", "Documented sizing, loads and resilience provisions."),
                ("Design review register", "Recorded comments, dispositions and close-out evidence."),
                ("Asset data schema", "The facility data structure the maintenance team will inherit."),
            ],
            related=[
                ("Military Construction", "capabilities/military-construction.html",
                 "Building what the design specifies."),
                ("Modernization Consulting", "capabilities/modernization-consulting.html",
                 "Carrying model data into operations and maintenance."),
                ("Naval &amp; Air Installations", "sectors/naval-and-air-installations.html",
                 "Hangars, secure storage and base infrastructure."),
            ],
        ),

        capability_page(
            "military-construction",
            "Military Construction",
            "Capability · Pillar 02",
            "Planning, design and delivery support for facilities where downtime is not an "
            "option — built secure-by-design, maintainable-by-design and audit-ready from day one.",
            desc="Military construction: bases, barracks, training grounds, logistics hubs, "
                 "perimeter infrastructure, secure storage and civil and structural works.",
            intro='''          <p>
            Military construction is judged on different criteria from commercial work. A barracks
            block is assessed on how it performs after ten years of intensive occupation with a
            constrained maintenance budget. A logistics hub is judged on whether stock can be
            moved through it under pressure. A perimeter is judged on whether it holds.
          </p>
          <p>
            We plan and deliver to those criteria. That means specifying for durability and
            maintainability rather than lowest capital cost, sequencing work so an operational
            site keeps functioning during construction, and documenting the build so the
            client's engineers can maintain it without reverse-engineering what was done.
          </p>
          <p>
            Our delivery principle is secure-by-design, maintainable-by-design, and audit-ready
            from day one. Audit readiness is not paperwork for its own sake: on public
            infrastructure spend it is what protects the officers who approved the project.
          </p>''',
            workstreams=[
                ("Command and control centres",
                 "Construction of operations and communications facilities with resilient "
                 "utilities and controlled access."),
                ("Barracks and personnel facilities",
                 "Accommodation, messing and welfare facilities specified for durability, "
                 "sustainability and efficient utilities."),
                ("Training grounds and support buildings",
                 "Ranges, classrooms, workshops, simulation rooms and the civil works that "
                 "support them."),
                ("Logistics hubs and secure storage",
                 "Warehousing, materials handling layout, controlled-access stores and the "
                 "circulation that makes them work under load."),
                ("Perimeter and civil infrastructure",
                 "Perimeter works, roads, drainage, hardstanding, water and power distribution "
                 "across a site."),
                ("Construction management",
                 "Procurement interfaces, quality control, site supervision, commissioning and "
                 "documented handover."),
            ],
            engagements=[
                ("Barracks and accommodation programme",
                 "<p>Delivery of durable, sustainable and maintainable accommodation with "
                 "efficient utilities — specified so that whole-life cost, not capital cost "
                 "alone, drives the material and system choices.</p>"),
                ("Training facility construction",
                 "<p>Ranges, classrooms, workshops and simulation rooms with the supporting "
                 "civil works, sequenced so existing training activity continues during "
                 "construction.</p>"),
                ("Logistics hub and secure storage",
                 "<p>Construction of storage and distribution facilities designed around the "
                 "actual movement of stock, with controlled access and inventory-visible "
                 "layouts.</p>"),
                ("Water and power resilience works",
                 "<p>Mini-grid support, borehole and water systems, backup generation and the "
                 "lifecycle maintenance regime to keep them running — frequently the highest "
                 "readiness return per naira on an established site.</p>"),
                ("Perimeter and site infrastructure upgrade",
                 "<p>Perimeter works, roads, drainage and utility distribution on an operational "
                 "site, phased to avoid interrupting activity.</p>"),
            ],
            deliverables=[
                ("Constructed and commissioned facility", "Built to the issued design, tested and formally accepted."),
                ("Quality records", "Inspection and test records assembled through construction, not after."),
                ("As-built documentation", "Drawings and models reflecting what was actually built."),
                ("Operation and maintenance manuals", "What the maintenance organisation needs to keep it working."),
                ("Handover and training pack", "Briefed handover so the receiving unit can operate the asset."),
                ("Audit evidence file", "Procurement and delivery trail retained for the client's records."),
            ],
            related=[
                ("Defence Engineering Design", "capabilities/engineering-design.html",
                 "The design the construction is built from."),
                ("Defence Supply Chain", "capabilities/defence-supply-chain.html",
                 "Materials, vendors and logistics behind delivery."),
                ("Nigerian Army", "sectors/nigerian-army.html",
                 "Barracks, training grounds and vehicle facilities."),
            ],
        ),

        capability_page(
            "defence-supply-chain",
            "Defence Supply Chain",
            "Capability · Pillar 03",
            "Procurement discipline and inventory visibility — readiness-focused support built "
            "around accountability at every handoff.",
            desc="Defence supply chain services: vendor qualification, strategic sourcing, "
                 "inventory control, transport and logistics, and lifecycle support for "
                 "non-sensitive equipment and services.",
            intro='''          <p>
            Readiness fails in the supply chain more often than anywhere else. A vehicle is
            grounded for a part that was never reordered. A project stalls on a vendor who was
            never properly qualified. Stock exists somewhere on the base but nobody can see it,
            so it is bought again.
          </p>
          <p>
            We build the procurement and inventory discipline that removes those failures:
            structured vendor qualification and performance monitoring, alternative sourcing
            routes and negotiated supply agreements, inventory dashboards with categorisation
            and reorder planning, and controlled logistics flows with documentation at each
            handoff.
          </p>
          <p>
            <strong>Scope:</strong> this work covers non-sensitive equipment, materials, spares
            and services — including the categories set out in our phased roadmap, such as
            radios, protective equipment, tactical uniforms, vehicles and surveillance tools. We
            supply and coordinate; we hold ourselves to documented traceability and
            quality-assurance systems on everything that moves through the pipeline.
          </p>''',
            workstreams=[
                ("Vendor qualification",
                 "Structured screening, prequalification, compliance checks and ongoing "
                 "performance monitoring of suppliers."),
                ("Strategic sourcing",
                 "Alternative sourcing routes and negotiated supply agreements for approved "
                 "items and services, including identification of trusted OEMs and regional "
                 "suppliers."),
                ("Inventory control",
                 "Dashboards, categorisation, reorder planning and warehousing process "
                 "discipline so stock is visible and replenished before it runs out."),
                ("Transport and logistics",
                 "Planning, documentation and controlled logistics flows for project materials "
                 "and spares, including importation, warehousing and distribution."),
                ("Traceability and quality assurance",
                 "Documented provenance and inspection regimes so what arrives is what was "
                 "specified."),
                ("Hardware selection support",
                 "Comparison matrices, technical specifications and suitability assessments to "
                 "support equipment selection decisions."),
            ],
            engagements=[
                ("Hardware selection and specification",
                 "<p>Expert guidance on choosing reliable, mission-appropriate equipment across "
                 "non-weaponized, high-impact categories — radios, body armour, tactical "
                 "uniforms, vehicles and surveillance tools — delivered as comparison matrices, "
                 "technical specifications and suitability assessments.</p>"),
                ("Procurement pipeline establishment",
                 "<p>Building a streamlined procurement pipeline for vetted equipment: trusted "
                 "OEM and regional supplier identification, logistics support for importation, "
                 "warehousing and distribution, and traceability and quality-assurance "
                 "systems.</p>"),
                ("Vendor governance programme",
                 "<p>Establishing prequalification criteria, compliance checking and performance "
                 "monitoring across a supplier base, with the documentation to support "
                 "auditability.</p>"),
                ("Inventory visibility implementation",
                 "<p>Categorisation, dashboards, reorder points and warehousing process design so "
                 "stock levels are known and stock-outs become predictable rather than "
                 "surprising.</p>"),
                ("Defence logistics optimisation",
                 "<p>Vendor governance, stock control, warehousing discipline and delivery "
                 "reliability reviewed end to end, with remediation sequenced by readiness "
                 "impact.</p>"),
            ],
            deliverables=[
                ("Qualified vendor register", "Screened suppliers with compliance status and performance history."),
                ("Sourcing strategy", "Routes to supply, negotiated agreements and alternatives per category."),
                ("Comparison matrices", "Documented options analysis behind each equipment recommendation."),
                ("Inventory dashboard", "Live visibility of holdings, categories and reorder status."),
                ("Logistics documentation", "Importation, warehousing and distribution records at each handoff."),
                ("Quality assurance regime", "Inspection and traceability procedures the client retains."),
            ],
            related=[
                ("Engagement roadmap", "roadmap/index.html",
                 "How supply chain support phases into manufacturing."),
                ("Modernization Consulting", "capabilities/modernization-consulting.html",
                 "Turning inventory data into maintenance decisions."),
                ("Military Construction", "capabilities/military-construction.html",
                 "Materials and vendor management on projects."),
            ],
            extra=f'''
  <section class="section section--ink2 section--line">
    <div class="shell">
      <div class="notice">
        <p style="margin:0"><strong>Illustrative target:</strong> disciplined vendor
        qualification and inventory practices are designed to shorten lead times and reduce
        stock-outs. Actual results depend on scope and baseline conditions.</p>
      </div>
    </div>
  </section>
''',
        ),

        capability_page(
            "modernization-consulting",
            "Modernization Consulting",
            "Capability · Pillar 04",
            "Transforming existing engineering and asset management practice with data-driven "
            "tools — and making sure the maintenance team actually uses them.",
            desc="Modernization consulting: risk assessment, asset management, lifecycle cost "
                 "analysis, digital transformation, IoT condition monitoring and predictive "
                 "maintenance for defence assets.",
            intro='''          <p>
            A great deal of defence infrastructure and equipment is maintained reactively: it is
            fixed when it fails. That is the most expensive maintenance strategy available, and
            on operational assets it converts a maintenance problem into a readiness problem.
          </p>
          <p>
            Modernization consulting closes that gap with instrumentation and analysis. Condition
            monitoring across vehicles, generators and critical facility systems produces data;
            analytics turn failure patterns in that data into maintenance decisions; BIM carries
            facility information from design into day-to-day operations so the people maintaining
            an asset know what they are maintaining.
          </p>
          <p>
            The part that determines whether any of it works is adoption. We include hands-on
            training and workflow support, because a dashboard nobody opens has changed nothing.
          </p>''',
            workstreams=[
                ("IoT condition monitoring",
                 "Sensor deployment for condition monitoring across vehicles, generators and "
                 "critical facility systems."),
                ("Analytics",
                 "Failure-pattern insights that turn raw sensor data into specific maintenance "
                 "decisions and intervals."),
                ("BIM for operations",
                 "Facility data continuity carried from design through to day-to-day operations "
                 "and maintenance."),
                ("Asset management and lifecycle cost",
                 "Asset registers, criticality assessment and lifecycle cost analysis to support "
                 "repair, refurbish or replace decisions."),
                ("Risk assessment",
                 "Structured assessment of infrastructure and asset risk, prioritised by "
                 "consequence to operations."),
                ("Training and adoption",
                 "Hands-on adoption support so maintenance teams actually use the new workflow "
                 "after handover."),
            ],
            engagements=[
                ("Predictive maintenance pilot",
                 "<p>A bounded pilot on a defined asset class — instrumentation, baseline data "
                 "capture, analytics and a decision workflow — sized so the client can judge the "
                 "return before committing to a wider rollout.</p>"
                 "<p><em>Illustrative example:</em> predictive maintenance analytics can flag "
                 "early signs of component wear, such as bearing degradation, before failure, "
                 "helping avoid unplanned downtime.</p>"),
                ("Armoured vehicle maintenance hub",
                 "<p>Diagnostics capability, workflow design, inventory visibility and predictive "
                 "maintenance built around a vehicle fleet, aimed directly at raising the "
                 "proportion of the fleet that is available.</p>"),
                ("Asset management system implementation",
                 "<p>Asset register, criticality ranking, maintenance regimes and lifecycle cost "
                 "model, with the data structure and training needed for the client's team to "
                 "run it.</p>"),
                ("Infrastructure risk assessment",
                 "<p>Assessment of an estate's infrastructure risk — power, water, structural "
                 "condition, fire, access — prioritised by operational consequence and costed "
                 "for remediation.</p>"),
                ("Digital readiness review",
                 "<p>Where BIM, IoT and analytics would genuinely help, and where they would add "
                 "cost without changing a decision. Deliberately includes the case for not "
                 "digitising something.</p>"),
            ],
            deliverables=[
                ("Asset register and criticality ranking", "What exists, its condition, and what matters most."),
                ("Condition monitoring deployment", "Instrumented assets with a live data feed."),
                ("Analytics and reporting workflow", "Failure-pattern analysis linked to maintenance action."),
                ("Lifecycle cost model", "Repair, refurbish or replace decisions on documented economics."),
                ("Risk register", "Prioritised infrastructure and asset risks with remediation costs."),
                ("Trained maintenance team", "Adoption support and handover so the workflow survives us."),
            ],
            related=[
                ("Defence Supply Chain", "capabilities/defence-supply-chain.html",
                 "Spares availability behind every maintenance plan."),
                ("Defence Engineering Design", "capabilities/engineering-design.html",
                 "BIM data originating in design."),
                ("Defence Industrialisation", "sectors/defence-industrialisation.html",
                 "Local maintenance hubs and capability transfer."),
            ],
        ),
    ]
