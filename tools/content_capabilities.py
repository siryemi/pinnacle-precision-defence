"""Capability pages: the /capabilities index plus the five pillars.

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
    "sovereign-cloud-and-ai": "Data classification and workload placement, sovereign landing "
                              "zone design, air-gapped enclaves for classified workloads, "
                              "continuous compliance evidence and in-country AI infrastructure.",
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
        "Five capability pillars for defence infrastructure and modernization",
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

        capability_page(
            "sovereign-cloud-and-ai",
            "Sovereign Cloud &amp; AI Infrastructure",
            "Capability · Pillar 05",
            "We do not host government data. We engineer and assure the environment that is "
            "permitted to — and design the AI capability that runs inside it.",
            desc="Sovereign cloud and AI infrastructure advisory: data classification and "
                 "workload placement under Nigeria's cloud instruments, landing zone design, "
                 "air-gapped enclaves, continuous compliance evidence and in-country AI.",
            intro='''          <p>
            Nigeria has written the rules but not the reference architectures. The National
            Cloud Technical Guideline 2026 and the National Guideline for Cloud Computing in
            Nigeria 2026 — both mandatory, both effective 1 January 2027 — establish a data
            classification model from Level 1 to Level 4. Level 4 includes military
            intelligence, must remain within Nigeria's territorial boundary under all
            circumstances, and must sit on-premises or in a certified private cloud. For Level 2
            and above, primary and secondary sites must both be in Nigeria and in different
            geopolitical zones.
          </p>
          <p>
            Those requirements do not prevent a Nigerian institution from using global cloud
            capability. They determine <em>where the data rests</em> and <em>who can reach
            it</em> — which is an architecture problem, not a prohibition. Dedicated in-country
            infrastructure, vendor hardware installed in a Nigerian facility, and ruggedised
            edge compute for forward sites all keep data resident while the platform and its
            services remain the same.
          </p>
          <p>
            Our contribution is the design and assurance work in between: classifying the
            workloads, designing the landing zone and the residency guardrails that enforce
            classification technically rather than by policy, specifying key custody so keys
            stay in Nigerian hands, and engineering the facility the whole thing sits in. That
            last part is why this sits with us rather than with a software consultancy — a
            cloud practice cannot design the power train, the cooling plant or the physical
            security envelope, and the instruments require all three.
          </p>
          <p>
            <strong>Our position is vendor-neutral.</strong> We hold no reseller relationship
            and we are not a cloud service provider, a data centre operator or a hosting
            provider. We do not host, process or store client data, and we do not hold or
            manage client encryption keys. We advise, design, assure and integrate.
          </p>''',
            workstreams=[
                ("Data classification and workload placement",
                 "Mapping an institution's systems onto Levels 1–4 and producing the placement "
                 "matrix that decides what may sit where. The first engagement, and the document "
                 "every later decision depends on."),
                ("Sovereign landing zone design",
                 "Account and organisation structure, network segregation, identity, logging and "
                 "residency guardrails enforced technically — so a workload cannot be deployed "
                 "to a non-compliant location even by mistake."),
                ("Access architecture",
                 "Authorised ingress and authorised egress as named, designed capabilities, with "
                 "identity-centric access replacing perimeter assumptions."),
                ("Key custody and encryption design",
                 "Customer-managed keys held in Nigeria, with a documented key hierarchy and "
                 "rotation regime. The control that actually answers the extraterritorial-access "
                 "question rather than deflecting it."),
                ("Continuous compliance and audit evidence",
                 "Change control through version-controlled infrastructure definitions, and "
                 "automated control evidence, so compliance is a continuous state rather than a "
                 "point-in-time audit scramble."),
                ("Air-gapped and edge deployment design",
                 "Disconnected enclaves for Level 4 workloads and ruggedised compute for forward "
                 "operating bases, designed to run without a link to any external region."),
                ("Hardened baseline and supply chain provenance",
                 "A hardened, minimal software baseline and provenance regime for government "
                 "workloads, so what runs in production is traceable to what was reviewed."),
                ("AI infrastructure and governance",
                 "In-country model hosting, training and inference, with the data-governance and "
                 "human-oversight framework around it. See the AI section below."),
            ],
            engagements=[
                ("Data classification and placement study",
                 "<p>We inventory an institution's systems and data holdings, classify them "
                 "against Levels 1–4, and produce a placement matrix: what may use a global "
                 "region, what must stay in Nigeria, what must be air-gapped, and what the "
                 "migration sequence should be.</p><ul>"
                 "<li>Deliverable is a decision document, not a procurement recommendation</li>"
                 "<li>No warranty of regulatory outcome — the institution and its counsel own "
                 "any submission to the regulator</li></ul>"),
                ("Sovereign landing zone design",
                 "<p>Design of the account structure, network segregation, identity model, "
                 "logging and audit trail, and the residency guardrails that make "
                 "classification enforceable in code. Delivered as a documented design plus "
                 "reusable infrastructure definitions the institution owns.</p>"
                 "<p>Where an institution runs many agencies, this becomes a reusable baseline "
                 "each one inherits — which is materially cheaper than every programme "
                 "designing its own.</p>"),
                ("Air-gapped enclave design for classified workloads",
                 "<p>Design of a disconnected environment for Level 4 data: platform selection, "
                 "update and patch pathway without external connectivity, backup and recovery, "
                 "and the facility requirements that go with it.</p>"),
                ("Continuous compliance implementation",
                 "<p>Establishing version-controlled change management and automated control "
                 "evidence collection, so the institution can demonstrate compliance on demand "
                 "instead of reconstructing it annually.</p>"),
                ("AI readiness and sovereign AI design",
                 "<p>Assessment of where AI can be applied against data the institution is "
                 "permitted to use, what infrastructure that requires in country, and the "
                 "governance framework needed before a model influences any decision.</p>"),
                ("Edge compute for forward operating bases",
                 "<p>Design of ruggedised, low-bandwidth-tolerant compute for dispersed sites — "
                 "local processing, deferred synchronisation, and physical and environmental "
                 "protection appropriate to the location.</p>"),
            ],
            deliverables=[
                ("Data classification register", "Every system mapped to a level, with the reasoning recorded."),
                ("Workload placement matrix", "What may sit where, and the migration sequence."),
                ("Landing zone design and baseline", "Documented design plus reusable definitions the client owns."),
                ("Access and key management design", "Ingress, egress, identity and key custody specified."),
                ("Compliance evidence pipeline", "Automated control evidence and a change audit trail."),
                ("AI governance framework", "Permitted data, human oversight, evaluation and review cadence."),
            ],
            related=[
                ("Defence Engineering Design", "capabilities/engineering-design.html",
                 "The facility the platform sits in."),
                ("Modernization Consulting", "capabilities/modernization-consulting.html",
                 "Asset data and analytics that feed it."),
                ("Ministry of Defence &amp; DHQ", "sectors/defence-headquarters.html",
                 "Estate-wide and joint programme adoption."),
            ],
            extra='''
  <section class="section section--ink2 section--line">
    <div class="shell">
      <div class="section-head section-head--wide">
        <p class="eyebrow">Reference architecture</p>
        <h2 class="d2">A generic sovereign environment, layer by layer</h2>
        <p class="lede mt-16">
          This is our own generic reference model, drawn deliberately vendor-neutral. It is
          informed by publicly released defence cloud reference architectures and adapted to
          Nigeria's classification levels. Each engagement produces a specific architecture;
          this shows the shape.
        </p>
      </div>

      <div class="diagram">
        <svg viewBox="0 0 900 560" role="img"
             aria-label="Layered sovereign cloud reference architecture. From top: an access layer with authorised ingress and authorised egress; a workload zone layer split into Level 1 to 2 general, Level 3 restricted, and Level 4 classified air-gapped; an AI and analytics layer with model hosting, training and edge inference; a control plane with identity, policy guardrails, key custody and logging; an in-country platform layer with dedicated infrastructure, on-premises nodes and tactical edge; and at the base a facility layer covering power, cooling, earthing and physical security. A continuous compliance evidence band spans every layer.">
          <g stroke="#1E2831" stroke-width="1" fill="none">
            <path d="M22 44v476"/>
          </g>

          <!-- 01 ACCESS -->
          <text x="34" y="36" fill="#C9A227" font-family="monospace" font-size="9">01 · ACCESS</text>
          <g fill="none" stroke="#14A356" stroke-width="1.3">
            <rect x="34" y="44" width="320" height="46" rx="2"/>
            <rect x="370" y="44" width="320" height="46" rx="2"/>
          </g>
          <g fill="#EDF0EE" font-family="monospace" font-size="10" text-anchor="middle">
            <text x="194" y="73">AUTHORISED INGRESS</text>
            <text x="530" y="73">AUTHORISED EGRESS</text>
          </g>

          <!-- 02 WORKLOAD ZONES -->
          <text x="34" y="122" fill="#C9A227" font-family="monospace" font-size="9">02 · WORKLOAD ZONES</text>
          <g fill="none" stroke="#14A356" stroke-width="1.3">
            <rect x="34" y="130" width="205" height="58" rx="2"/>
            <rect x="252" y="130" width="205" height="58" rx="2"/>
          </g>
          <rect x="470" y="130" width="220" height="58" rx="2" fill="none" stroke="#C9A227" stroke-width="1.6" stroke-dasharray="6 4"/>
          <g fill="#A7B0AC" font-family="monospace" font-size="9" text-anchor="middle">
            <text x="136" y="155">LEVEL 1–2</text><text x="136" y="170">GENERAL</text>
            <text x="354" y="155">LEVEL 3</text><text x="354" y="170">RESTRICTED</text>
            <text x="580" y="155" fill="#C9A227">LEVEL 4 · CLASSIFIED</text>
            <text x="580" y="170" fill="#C9A227">AIR-GAPPED</text>
          </g>

          <!-- 03 AI -->
          <text x="34" y="220" fill="#C9A227" font-family="monospace" font-size="9">03 · AI &amp; ANALYTICS</text>
          <rect x="34" y="228" width="656" height="54" rx="2" fill="none" stroke="#14A356" stroke-width="1.3"/>
          <g stroke="#1E2831" stroke-width="1">
            <path d="M252 228v54M470 228v54"/>
          </g>
          <g fill="#A7B0AC" font-family="monospace" font-size="9" text-anchor="middle">
            <text x="143" y="252">MODEL</text><text x="143" y="266">HOSTING</text>
            <text x="361" y="252">TRAINING &amp;</text><text x="361" y="266">FINE-TUNING</text>
            <text x="580" y="252">INFERENCE</text><text x="580" y="266">AT THE EDGE</text>
          </g>

          <!-- 04 CONTROL PLANE -->
          <text x="34" y="314" fill="#C9A227" font-family="monospace" font-size="9">04 · CONTROL PLANE</text>
          <g fill="none" stroke="#14A356" stroke-width="1.3">
            <rect x="34" y="322" width="158" height="50" rx="2"/>
            <rect x="200" y="322" width="158" height="50" rx="2"/>
            <rect x="366" y="322" width="158" height="50" rx="2"/>
            <rect x="532" y="322" width="158" height="50" rx="2"/>
          </g>
          <g fill="#A7B0AC" font-family="monospace" font-size="8.5" text-anchor="middle">
            <text x="113" y="344">IDENTITY &amp;</text><text x="113" y="357">ACCESS</text>
            <text x="279" y="344">POLICY</text><text x="279" y="357">GUARDRAILS</text>
            <text x="445" y="344">KEY CUSTODY</text><text x="445" y="357">(IN NIGERIA)</text>
            <text x="611" y="344">LOGGING &amp;</text><text x="611" y="357">AUDIT TRAIL</text>
          </g>

          <!-- 05 PLATFORM -->
          <text x="34" y="404" fill="#C9A227" font-family="monospace" font-size="9">05 · IN-COUNTRY PLATFORM</text>
          <g fill="none" stroke="#14A356" stroke-width="1.3">
            <rect x="34" y="412" width="212" height="50" rx="2"/>
            <rect x="256" y="412" width="212" height="50" rx="2"/>
            <rect x="478" y="412" width="212" height="50" rx="2"/>
          </g>
          <g fill="#A7B0AC" font-family="monospace" font-size="8.5" text-anchor="middle">
            <text x="140" y="434">DEDICATED</text><text x="140" y="447">INFRASTRUCTURE</text>
            <text x="362" y="434">ON-PREMISES</text><text x="362" y="447">NODES</text>
            <text x="584" y="434">TACTICAL</text><text x="584" y="447">EDGE</text>
          </g>

          <!-- 06 FACILITY -->
          <text x="34" y="494" fill="#C9A227" font-family="monospace" font-size="9">06 · FACILITY — OUR ENGINEERING CORE</text>
          <rect x="34" y="502" width="656" height="46" rx="2" fill="rgba(201,162,39,0.10)" stroke="#C9A227" stroke-width="1.6"/>
          <text x="362" y="530" fill="#C9A227" font-family="monospace" font-size="9.5" text-anchor="middle">POWER · COOLING · EARTHING &amp; LPS · PHYSICAL SECURITY · RESILIENCE</text>

          <!-- continuous compliance band -->
          <rect x="716" y="44" width="154" height="504" rx="2" fill="none" stroke="#14A356" stroke-width="1.2" stroke-dasharray="6 5"/>
          <text transform="translate(802,296) rotate(-90)" fill="#14A356" font-family="monospace" font-size="10" text-anchor="middle">CONTINUOUS COMPLIANCE EVIDENCE</text>
          <text transform="translate(820,296) rotate(-90)" fill="#6E767C" font-family="monospace" font-size="8" text-anchor="middle">CHANGE CONTROL · CONTROL TESTING · REPORTING</text>
        </svg>
        <p class="diagram__caption">
          Our own generic model, drawn vendor-neutral. Layers 01 to 05 are the cloud practice;
          layer 06 is the engineering business we already run. The compliance band spans every
          layer because evidence is produced continuously, not assembled for an audit.
        </p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Artificial intelligence</p>
          <h2 class="d2">AI is a data-governance problem before it is a technology problem</h2>
          <p class="lede mt-16">
            The constraint on defence AI in Nigeria is not model availability. It is which data
            a model may lawfully be trained on and where that training may physically happen —
            which returns directly to classification and residency.
          </p>
          <p class="mt-24">
            Nigeria's own cloud instruments already name AI infrastructure providers and
            sovereign compute providers among the parties they regulate. The obligations are
            arriving alongside the capability, and an institution that adopts AI without a
            classification and governance position first will have to unwind it.
          </p>
        </div>
        <div>
          <div class="ruled">
            <div class="ruled__row">
              <h3>In-country AI infrastructure</h3>
              <p>Training and inference on infrastructure physically resident in Nigeria, so
              classified and restricted data never has to leave to be useful. Includes the
              power and cooling design that accelerated compute actually demands — which is a
              materially different thermal problem from general-purpose servers.</p>
            </div>
            <div class="ruled__row">
              <h3>Permitted-data determination</h3>
              <p>Which datasets a model may lawfully be trained or fine-tuned on, by
              classification level, recorded as a decision document before any development
              starts.</p>
            </div>
            <div class="ruled__row">
              <h3>Applied use cases within our scope</h3>
              <p>Predictive maintenance on vehicle and generator fleets, condition monitoring
              across facilities, demand forecasting for spares and inventory, and document and
              language processing for administrative load. All non-weaponized, all extending
              work we already do.</p>
            </div>
            <div class="ruled__row">
              <h3>Governance and human oversight</h3>
              <p>Model inventory, evaluation before deployment, monitoring for drift, a named
              accountable human for every model that informs a decision, and a review cadence.
              Written to be auditable.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Honest position</p>
          <h2 class="d2">What we are, and what we are not</h2>
          <p class="lede mt-16">
            This pillar is newer than the four it sits on. Stating its limits plainly is what
            makes the rest of the page worth reading.
          </p>
        </div>
        <div class="prose">
          <p><strong>We are:</strong> an engineering and consulting firm that classifies
          workloads, designs sovereign environments and the facilities that host them, and
          designs the governance around AI.</p>
          <p><strong>We are not:</strong> a cloud service provider, a data centre operator, a
          hosting provider, a reseller, or a certification body. We hold no assurance
          certification for operating national digital infrastructure, and we do not claim a
          path to one.</p>
          <p><strong>We do not:</strong> host, process or store client data; hold or manage
          client encryption keys; or perform audit or attestation functions on our own work.</p>
          <p>
            Partner standing and certified engineering headcount for this pillar:
            <span class="todo">TODO: state cloud partner tier and number of certified
            architects, or remove this pillar from the site until it can be stated</span>.
          </p>
          <p>
            Where a requirement needs capability we do not hold, we say so and propose a named
            joint venture rather than stretching to cover it.
          </p>
        </div>
      </div>
    </div>
  </section>
''',
        ),
    ]
