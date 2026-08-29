"""The phased engagement roadmap.

Content source: "Pitch on 3 phases.pdf", short-term support, mid-term
collaboration, long-term indigenous capability, plus the value proposition.
"""

from layout import ARROW, page_hero, cta_band, ruled, accordion, cards, DISCLAIMER


def roadmap_page():
    body = page_hero(
        "Engagement roadmap",
        "Support today, problem-solving tomorrow, indigenous capability after that",
        "Our goal is to support the Nigerian military with practical, scalable solutions that "
        "strengthen readiness today while building long-term national capability. The path has "
        "three phases, and each one earns the next.",
        trail=[("Roadmap", None)],
        actions=f'<div class="hero__actions"><a class="btn btn--primary" '
                f'href="{{P}}contact/index.html">Discuss the roadmap {ARROW}</a></div>',
    )

    body += f'''
  <section class="section section--tight section--ink2">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Purpose of engagement</p>
          <h2 class="d3">Practical, scalable, modernization-aligned support.</h2>
        </div>
        <div class="prose">
          <p>
            To provide the Nigerian Armed Forces with practical, scalable and
            modernization-aligned support across communications, protection, surveillance,
            mobility and long-term defence industrialisation.
          </p>
          <p>
            The phasing is deliberate. Phase one requires no structural change from the client
            and delivers immediate operational value. Phase two goes deeper only once we have
            earned access and understand the terrain. Phase three is a multi-year national
            capability commitment that would be premature to propose on day one.
          </p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Phase one · short term</p>
        <h2 class="d2">Immediate support, minimal structural change</h2>
        <p class="lede mt-16">
          Practical assistance that strengthens operations without requiring the client to
          reorganise anything first.
        </p>
      </div>
      <div class="split">
        <div>
          <h3 class="d4">A · Hardware selection consultation</h3>
          <p class="lede mt-16">
            Expert guidance on choosing reliable, mission-appropriate equipment, focused on
            non-weaponized, high-impact categories.
          </p>
          {ruled([
              ("Radios", "Tactical and base communications equipment selection."),
              ("Body armour", "Protection levels matched to the threat and the task."),
              ("Tactical uniforms", "Durability, climate suitability and sustained-use performance."),
              ("Vehicles", "Mobility requirements, terrain suitability and maintainability."),
              ("Surveillance tools", "Sensor selection against the actual observation requirement."),
          ])}
          <p class="mt-24"><strong>Delivered as:</strong> comparison matrices, technical
          specifications and suitability assessments.</p>
        </div>
        <div>
          <h3 class="d4">B · Supply chain solutions</h3>
          <p class="lede mt-16">
            A streamlined procurement pipeline for vetted equipment, with accountability at
            every handoff.
          </p>
          {ruled([
              ("Vetted procurement pipeline", "A repeatable route to market for approved equipment categories."),
              ("Trusted OEMs and regional suppliers", "Identification and qualification of credible sources of supply."),
              ("Logistics support", "Importation, warehousing and distribution coordination."),
              ("Traceability and quality assurance", "Documented provenance and inspection on everything supplied."),
          ])}
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Phase two · mid term</p>
        <h2 class="d2">Joint problem-solving with commanders</h2>
        <p class="lede mt-16">
          Identify operational gaps and co-develop tailored solutions, addressing deeper
          challenges and beginning capability expansion.
        </p>
      </div>
      {accordion("phase2", [
          ("A. Operational gap analysis",
           "<p>Structured listening sessions with unit commanders to uncover the challenges "
           "that do not appear in formal reporting, then mapping them into addressable "
           "operational domains.</p>"
           "<p>Pain points we map:</p><ul>"
           "<li>Communication gaps</li>"
           "<li>Mobility limitations</li>"
           "<li>Surveillance blind spots</li>"
           "<li>Equipment fatigue</li>"
           "<li>Maintenance challenges</li></ul>"
           "<p>Output is a tailored solution set for each operational domain, prioritised by "
           "readiness impact.</p>"),
          ("B. High-level capability requirements",
           "<p>Safe, non-operational discussions on capability needs, helping the military "
           "define purpose-based requirements without crossing into restricted operational "
           "guidance.</p>"
           "<p>Topics in scope:</p><ul>"
           "<li>What drones are needed for ISR, logistics or surveillance</li>"
           "<li>What aircraft range, endurance and payload missions require</li>"
           "<li>What non-weaponized missile-defence detection systems are needed</li>"
           "<li>What technical specifications matter for procurement decisions</li></ul>"
           "<p>This is requirements definition, not operational advice and not the supply of "
           "weapons systems.</p>"),
      ])}
    </div>
  </section>

  <section class="section section--ink2 section--line">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Phase three · long term</p>
        <h2 class="d2">A Nigerian defence-industry ecosystem</h2>
        <p class="lede mt-16">
          Built on engineering, design and manufacturing, positioning the firm as a strategic
          partner in Nigeria's modernization journey rather than a supplier of imports.
        </p>
      </div>
      <div class="split">
        <div>
          <h3 class="d4">A · Design, engineering and manufacturing</h3>
          <p class="lede mt-16">
            Developing local production capacity for non-weaponized systems.
          </p>
          {ruled([
              ("Tactical vehicles", "Local assembly and eventual design capability."),
              ("Communication systems", "Domestic production and integration capacity."),
              ("Surveillance platforms", "Indigenous capability for observation systems."),
              ("Protective equipment", "Body armour and personal protection manufacture."),
              ("Field gear", "Sustained-use equipment produced in country."),
          ])}
          <p class="mt-24">Supported by engineering partnerships with universities and research
          centres, and local assembly and maintenance hubs.</p>
        </div>
        <div>
          <h3 class="d4">B · Strategic partnership model</h3>
          <p class="lede mt-16">
            Multi-year modernization collaboration rather than transactional supply.
          </p>
          {ruled([
              ("Multi-year collaboration", "Sustained engagement with Nigerian Army leadership."),
              ("Joint R&amp;D programmes", "Co-developed research with domestic institutions."),
              ("Local workforce development", "Building the engineering and technician base."),
              ("Technology transfer agreements", "Structured transfer that conveys real capability."),
          ])}
        </div>
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Value proposition</p>
        <h2 class="d2">Why this sequence works</h2>
      </div>
      {cards([
          ("Rapid deployment",
           "Solutions deliver immediate operational impact rather than requiring a "
           "reorganisation before any benefit appears."),
          ("Cost-effective modernization",
           "A non-weaponized focus reduces procurement complexity, shortening the path from "
           "requirement to delivered capability."),
          ("Local capability building",
           "Directly supports Nigeria's long-term defence industrialisation goals rather than "
           "deepening import dependency."),
          ("Interoperability",
           "Designed to integrate with existing Nigerian Army platforms instead of creating "
           "another isolated system."),
      ], cols=4)}
      <div class="mt-56">
        <div class="quote">
          <p>
            We want to be a dependable partner in Nigeria's modernization journey, starting
            with support today and growing into full indigenous capability tomorrow.
          </p>
          <cite>Pinnacle Precision Engineering &amp; Consulting Limited</cite>
        </div>
      </div>
      <div class="mt-40">{DISCLAIMER}</div>
    </div>
  </section>

''' + cta_band()

    return ("roadmap/index.html", "Engagement roadmap",
            "A three-phase roadmap for supporting the Nigerian Armed Forces: short-term "
            "hardware selection and supply chain support, mid-term operational gap analysis, "
            "and long-term indigenous design and manufacturing capability.",
            body)


def all_roadmap_pages():
    return [roadmap_page()]
