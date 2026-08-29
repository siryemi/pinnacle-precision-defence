"""Capability pages: the /capabilities index plus the five pillars.

Content source: pinnacle_precision_defense_profile.pptx (slides 2, 4, 5, 6, 7, 8).
Pillar 05 is founder-directed; see the note in layout.py.

Copy is deliberately tight. Keep it that way: short sentences, no throat-clearing,
one idea per line. The reference-architecture diagram lives in
diagram-sovereign.svg so copy edits cannot disturb it.
"""

import pathlib

from layout import (NAV_CAPABILITIES, ARROW, ARROW_SM, page_hero, cta_band,
                    link_arrow, ruled, accordion, cards, DISCLAIMER)

DIAGRAM_SVG = pathlib.Path(__file__).with_name("diagram-sovereign.svg").read_text()

_SUMMARIES = {
    "engineering-design": "Secure facilities, C2 spaces, blast-aware structures, MEP and "
                          "CAD/BIM from FEED through IFC.",
    "military-construction": "Bases, barracks, training grounds, logistics hubs, perimeters "
                             "and secure storage.",
    "defence-supply-chain": "Vendor qualification, sourcing, logistics and inventory control "
                            "for non-sensitive equipment.",
    "modernization-consulting": "Asset management, lifecycle cost, IoT condition monitoring "
                                "and predictive maintenance.",
    "sovereign-cloud-and-ai": "Data classification, sovereign landing zones, air-gapped "
                              "enclaves and in-country AI.",
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
        <h2 class="d2">How this work arrives</h2>
      </div>
      {accordion("eng-" + slug, engagements)}
      <div class="mt-40">{DISCLAIMER}</div>
    </div>
  </section>

  <section class="section section--ink2 section--line">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Deliverables</p>
        <h2 class="d2">What you are left holding</h2>
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
    items = [(label, _SUMMARIES[slug], f"capabilities/{slug}.html")
             for slug, label, _ in NAV_CAPABILITIES]

    body = page_hero(
        "Capabilities",
        "Five pillars, one delivery chain",
        "Design, build, procure, sustain, and the sovereign infrastructure on top. Secure, "
        "maintainable and auditable at every stage.",
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
        <h2 class="d2">Four readiness outcomes</h2>
        <p class="lede mt-16">
          Every scope we propose moves at least one. If it moves none, it is the wrong scope.
        </p>
      </div>
      <div class="grid grid--4">
        <div class="card"><p class="card__num">01</p><h3>Reduce mission risk</h3>
          <p>Design review, quality control and lifecycle thinking.</p></div>
        <div class="card"><p class="card__num">02</p><h3>Accelerate delivery</h3>
          <p>Engineering, procurement and construction in one workflow.</p></div>
        <div class="card"><p class="card__num">03</p><h3>Improve asset uptime</h3>
          <p>Sensors and analytics on vehicles, generators and facilities.</p></div>
        <div class="card"><p class="card__num">04</p><h3>Strengthen accountability</h3>
          <p>Vendor qualification and handover discipline you can audit.</p></div>
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
            The same four stages, whether the scope is one facility or a multi-site programme.
          </p>
          <div class="actions mt-32">
            <a class="btn btn--ghost" href="{{P}}roadmap/index.html">See the phased roadmap</a>
          </div>
        </div>
        <div class="steps">
          <div class="step"><div><h3>Assess</h3></div>
            <p>Requirements, site realities, constraints, risk.</p></div>
          <div class="step"><div><h3>Design</h3></div>
            <p>FEED, BIM/CAD and IFC packages, with cost logic.</p></div>
          <div class="step"><div><h3>Deliver</h3></div>
            <p>Procurement, construction, quality control, commissioning.</p></div>
          <div class="step"><div><h3>Sustain</h3></div>
            <p>Handover, training, asset data, maintenance planning.</p></div>
        </div>
      </div>
    </div>
  </section>

''' + cta_band()

    return ("capabilities/index.html", "Capabilities",
            "Five defence-aligned pillars: engineering design, military construction, defence "
            "supply chain, modernization consulting, and sovereign cloud and AI.",
            body)


def all_capability_pages():
    return [
        capabilities_index(),

        capability_page(
            "engineering-design",
            "Defence Engineering Design",
            "Capability · Pillar 01",
            "Secure-by-design engineering for facilities where downtime is not acceptable.",
            desc="Defence engineering design: secure facilities, command-and-control spaces, "
                 "blast-aware structures, MEP systems and CAD/BIM from FEED through IFC.",
            intro='''          <p>
            Defence infrastructure carries requirements commercial design does not. A command
            space has to hold power, cooling and comms through a utility failure. A secure store
            has to survive an attempt to force it. Blast and ballistic loads belong in the frame,
            not bolted on later.
          </p>
          <p>
            We carry those requirements from front-end design through to
            issued-for-construction. BIM models are structured so facility data survives into
            operations, which is where most of a model's value is normally lost.
          </p>''',
            workstreams=[
                ("Secure facility design",
                 "Access control, compartmentalisation, hardened envelopes, continuity of operations."),
                ("Command and control spaces",
                 "Comms rooms, operations floors, resilient power and cooling, serviceable cable routes."),
                ("Blast-aware structures",
                 "Structural design for the blast and ballistic threat at that location."),
                ("MEP systems",
                 "Mechanical, electrical and plumbing, including backup generation and protected distribution."),
            ],
            engagements=[
                ("Secure command centre design",
                 "<p>Resilient envelope, protected MEP, backup utilities and comms-room readiness, "
                 "with continuity of operations as the governing requirement.</p>"),
                ("FEED study",
                 "<p>Scope, technical basis, cost logic and execution strategy, taken to the point "
                 "where a construction tender can run with confidence. Options compared before the "
                 "design is fixed.</p>"),
                ("Design assurance on an existing package",
                 "<p>Independent review of a design already produced: buildability, "
                 "maintainability, security requirements, MEP coordination. Delivered as a "
                 "prioritised comment register.</p>"),
            ],
            deliverables=[
                ("FEED package", "Technical basis, options, cost logic, execution strategy."),
                ("Coordinated BIM model", "Multi-discipline, structured for handover."),
                ("IFC drawing set", "Drawings a contractor can build from."),
                ("MEP design and calculations", "Sizing, loads and resilience provisions."),
            ],
            related=[
                ("Military Construction", "capabilities/military-construction.html",
                 "Building what the design specifies."),
                ("Modernization Consulting", "capabilities/modernization-consulting.html",
                 "Carrying model data into operations."),
                ("Naval &amp; Air Installations", "sectors/naval-and-air-installations.html",
                 "Hangars, workshops and secure storage."),
            ],
        ),

        capability_page(
            "military-construction",
            "Military Construction",
            "Capability · Pillar 02",
            "Secure-by-design, maintainable-by-design, audit-ready from day one.",
            desc="Military construction: bases, barracks, training grounds, logistics hubs, "
                 "perimeter infrastructure, secure storage and civil works.",
            intro='''          <p>
            Military construction is judged on different criteria. A barracks block is assessed
            after ten years of hard occupation on a constrained maintenance budget. A logistics
            hub is judged on whether stock moves through it under pressure. A perimeter is judged
            on whether it holds.
          </p>
          <p>
            So we specify for durability, sequence work so an operational site keeps running, and
            document the build so your engineers can maintain it without reverse-engineering what
            was done.
          </p>''',
            workstreams=[
                ("Command and control centres",
                 "Operations and comms facilities with resilient utilities and controlled access."),
                ("Barracks and personnel facilities",
                 "Accommodation, messing and welfare, specified for durability and efficient utilities."),
                ("Training grounds",
                 "Ranges, classrooms, workshops, simulation rooms and supporting civil works."),
                ("Logistics hubs and secure storage",
                 "Warehousing, materials handling, controlled-access stores, circulation under load."),
            ],
            engagements=[
                ("Barracks and accommodation",
                 "<p>Durable, maintainable accommodation with efficient utilities, specified so "
                 "whole-life cost drives the material choices rather than capital cost alone.</p>"),
                ("Training facilities",
                 "<p>Ranges, classrooms, workshops and simulation rooms, sequenced so existing "
                 "training continues through construction.</p>"),
                ("Logistics hub and secure storage",
                 "<p>Storage and distribution designed around how stock actually moves, with "
                 "controlled access and inventory-visible layouts.</p>"),
            ],
            deliverables=[
                ("Commissioned facility", "Built to the issued design, tested, accepted."),
                ("Quality records", "Inspection and test records assembled during construction."),
                ("As-built documentation", "Drawings and models reflecting what was built."),
                ("O&amp;M manuals", "What your maintenance organisation needs."),
            ],
            related=[
                ("Defence Engineering Design", "capabilities/engineering-design.html",
                 "The design we build from."),
                ("Defence Supply Chain", "capabilities/defence-supply-chain.html",
                 "Materials, vendors and logistics."),
                ("Nigerian Army", "sectors/nigerian-army.html",
                 "Barracks, training grounds and vehicle facilities."),
            ],
        ),

        capability_page(
            "defence-supply-chain",
            "Defence Supply Chain",
            "Capability · Pillar 03",
            "Procurement discipline and inventory visibility, with accountability at every handoff.",
            desc="Defence supply chain: vendor qualification, strategic sourcing, inventory "
                 "control, logistics and lifecycle support for non-sensitive equipment.",
            intro='''          <p>
            Readiness fails in the supply chain more than anywhere else. A vehicle is grounded for
            a part nobody reordered. A project stalls on a vendor nobody qualified. Stock exists
            on the base but nobody can see it, so it is bought twice.
          </p>
          <p>
            We build the discipline that removes those failures: qualified vendors, negotiated
            supply routes, inventory dashboards with reorder planning, and documented logistics at
            each handoff. Scope covers non-weaponized equipment, materials, spares and services.
          </p>''',
            workstreams=[
                ("Vendor qualification",
                 "Screening, prequalification, compliance checks, ongoing performance monitoring."),
                ("Strategic sourcing",
                 "Alternative routes and negotiated agreements. Trusted OEMs and regional suppliers."),
                ("Inventory control",
                 "Dashboards, categorisation, reorder planning, warehousing discipline."),
                ("Transport and logistics",
                 "Importation, warehousing and distribution, documented at each stage."),
            ],
            engagements=[
                ("Hardware selection and specification",
                 "<p>Guidance on mission-appropriate equipment across non-weaponized categories: "
                 "radios, body armour, tactical uniforms, vehicles, surveillance tools. Delivered "
                 "as comparison matrices, specifications and suitability assessments.</p>"),
                ("Procurement pipeline",
                 "<p>A repeatable route to market for vetted equipment: OEM and regional supplier "
                 "qualification, importation and warehousing logistics, traceability and QA.</p>"),
                ("Vendor governance",
                 "<p>Prequalification criteria, compliance checking and performance monitoring "
                 "across a supplier base, documented to support audit.</p>"),
            ],
            deliverables=[
                ("Qualified vendor register", "Screened suppliers with compliance and performance history."),
                ("Sourcing strategy", "Routes to supply and alternatives per category."),
                ("Comparison matrices", "The options analysis behind each recommendation."),
                ("Inventory dashboard", "Live holdings, categories and reorder status."),
            ],
            related=[
                ("Engagement roadmap", "roadmap/index.html",
                 "How supply chain support phases into manufacturing."),
                ("Modernization Consulting", "capabilities/modernization-consulting.html",
                 "Turning inventory data into maintenance decisions."),
                ("Military Construction", "capabilities/military-construction.html",
                 "Materials and vendor management on projects."),
            ],
            extra='''
  <section class="section section--ink2 section--line">
    <div class="shell">
      <div class="notice">
        <p style="margin:0"><strong>Illustrative target:</strong> disciplined vendor
        qualification and inventory practice are designed to shorten lead times and reduce
        stock-outs. Results depend on scope and baseline conditions.</p>
      </div>
    </div>
  </section>
''',
        ),

        capability_page(
            "modernization-consulting",
            "Modernization Consulting",
            "Capability · Pillar 04",
            "Condition data turned into maintenance decisions, and teams trained to use it.",
            desc="Modernization consulting: risk assessment, asset management, lifecycle cost, "
                 "IoT condition monitoring and predictive maintenance for defence assets.",
            intro='''          <p>
            Most defence infrastructure is maintained reactively: fixed when it fails. That is the
            most expensive strategy available, and on operational assets it turns a maintenance
            problem into a readiness problem.
          </p>
          <p>
            Condition monitoring produces data. Analytics turn failure patterns into maintenance
            decisions. BIM carries facility information into operations. The part that decides
            whether any of it works is adoption, so training is in scope from the start.
          </p>''',
            workstreams=[
                ("IoT condition monitoring",
                 "Sensors on vehicles, generators and critical facility systems."),
                ("Analytics",
                 "Failure-pattern insight turned into specific maintenance intervals."),
                ("BIM for operations",
                 "Facility data carried from design into day-to-day maintenance."),
                ("Asset management",
                 "Registers, criticality ranking and lifecycle cost for repair-or-replace calls."),
            ],
            engagements=[
                ("Predictive maintenance pilot",
                 "<p>A bounded pilot on one asset class: instrumentation, baseline data, analytics "
                 "and a decision workflow, sized so you can judge the return before a wider "
                 "rollout.</p><p><em>Illustrative example:</em> analytics can flag bearing "
                 "degradation before failure, avoiding unplanned downtime.</p>"),
                ("Armoured vehicle maintenance hub",
                 "<p>Diagnostics, workflow, inventory visibility and predictive maintenance built "
                 "around a fleet, aimed at raising the proportion that is available.</p>"),
                ("Asset management system",
                 "<p>Register, criticality ranking, maintenance regimes and lifecycle cost model, "
                 "with the training for your team to run it.</p>"),
            ],
            deliverables=[
                ("Asset register", "What exists, its condition, what matters most."),
                ("Condition monitoring", "Instrumented assets with a live data feed."),
                ("Analytics workflow", "Failure-pattern analysis linked to maintenance action."),
                ("Lifecycle cost model", "Repair, refurbish or replace on documented economics."),
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
            "Sovereign environments built to Nigeria's classification rules, and the AI that "
            "runs inside them.",
            desc="Sovereign cloud and AI: data classification and workload placement under "
                 "Nigeria's cloud instruments, landing zone design, air-gapped enclaves, "
                 "continuous compliance and in-country AI.",
            intro='''          <p>
            Nigeria has written the rules but not the reference architectures. Two NITDA
            instruments, mandatory from 1 January 2027, classify government data Level 1 to 4.
            Level 4 includes military intelligence and never leaves Nigeria. Level 2 and above
            needs primary and secondary sites in different geopolitical zones.
          </p>
          <p>
            We classify the workloads, design the landing zone and the guardrails that enforce
            classification in code, specify key custody, and engineer the facility. That last
            part is why this sits with us: the instruments require power, cooling and physical
            security.
          </p>
          <p>
            <strong>We are provider agnostic.</strong> We design to the requirement, then fit the
            platform to it. You own the environment and hold its keys.
          </p>''',
            workstreams=[
                ("Data classification and placement",
                 "Systems mapped to Levels 1 to 4, and the matrix deciding what sits where."),
                ("Sovereign landing zone",
                 "Accounts, segregation, identity, logging, and residency guardrails enforced in code."),
                ("Access architecture",
                 "Authorised ingress and egress, identity-centric rather than perimeter-based."),
                ("Key custody",
                 "Customer-managed keys held in Nigeria, with hierarchy and rotation documented."),
            ],
            engagements=[
                ("Data classification and placement study",
                 "<p>We inventory systems and data, classify them against Levels 1 to 4, and "
                 "produce the placement matrix: what can use a global region, what stays in "
                 "Nigeria, what is air-gapped, and the migration sequence.</p>"),
                ("Sovereign landing zone design",
                 "<p>Account structure, segregation, identity, logging and the guardrails that make "
                 "classification enforceable. Delivered as a design plus reusable infrastructure "
                 "definitions you own.</p><p>Across many agencies this becomes a baseline each one "
                 "inherits. Far cheaper than every programme designing its own.</p>"),
                ("Air-gapped enclave design",
                 "<p>A disconnected environment for Level 4: platform selection, patch pathway "
                 "without external connectivity, backup and recovery, and the facility "
                 "requirements.</p>"),
            ],
            deliverables=[
                ("Classification register", "Every system mapped to a level, reasoning recorded."),
                ("Placement matrix", "What sits where, and the migration sequence."),
                ("Landing zone design", "Design plus reusable definitions you own."),
                ("Access and key design", "Ingress, egress, identity and key custody."),
            ],
            related=[
                ("Defence Engineering Design", "capabilities/engineering-design.html",
                 "The facility the platform sits in."),
                ("Modernization Consulting", "capabilities/modernization-consulting.html",
                 "Asset data and analytics that feed it."),
                ("Ministry of Defence &amp; DHQ", "sectors/defence-headquarters.html",
                 "Estate-wide and joint programme adoption."),
            ],
            extra=f'''
  <section class="section section--ink2 section--line">
    <div class="shell">
      <div class="section-head section-head--wide">
        <p class="eyebrow">Reference architecture</p>
        <h2 class="d2">A generic sovereign environment, layer by layer</h2>
        <p class="lede mt-16">
          Our own vendor-neutral model, adapted to Nigeria's classification levels. Each
          engagement produces a specific architecture; this is the shape.
        </p>
      </div>

      <div class="diagram">
        {DIAGRAM_SVG}
        <p class="diagram__caption">
          Layers 01 to 05 are the cloud practice. Layer 06 is the engineering business we already
          run. The compliance band spans every layer.
        </p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Artificial intelligence</p>
          <h2 class="d2">AI is a data-governance problem first</h2>
          <p class="lede mt-16">
            The constraint is not model availability. It is which data a model may lawfully train
            on, and where that training happens. Both come back to classification and residency.
          </p>
          <p class="mt-24">
            Nigeria's instruments already regulate AI infrastructure and sovereign compute
            providers. Adopt AI without a classification position first and you will unwind it.
          </p>
        </div>
        <div>
          {ruled([
              ("In-country AI infrastructure",
               "Training and inference resident in Nigeria, plus the power and cooling accelerated compute demands."),
              ("Permitted-data determination",
               "Which datasets a model may lawfully train on, by level, recorded before development starts."),
              ("Applied use cases",
               "Predictive maintenance on vehicles and generators, facility condition monitoring, spares forecasting, document processing."),
              ("Governance and oversight",
               "Model inventory, evaluation, drift monitoring, a named accountable human, review cadence."),
          ])}
        </div>
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">How we work</p>
          <h2 class="d2">Design and assurance, with you in control</h2>
          <p class="lede mt-16">
            We classify, design, assure and engineer. You own the design, the data and the keys.
          </p>
        </div>
        <div class="prose">
          <p>
            Provider agnostic by choice. It keeps the platform decision open until the requirement
            is written, which is the right order and usually cheaper.
          </p>
          <p>
            On larger programmes we work in joint venture, named in the bid, so you get one
            accountable design authority.
          </p>
          <p>
            Cloud partner standing and certified headcount for this pillar:
            <span class="todo">TODO: state cloud partner tier and number of certified
            architects</span>.
          </p>
        </div>
      </div>
    </div>
  </section>
''',
        ),
    ]
