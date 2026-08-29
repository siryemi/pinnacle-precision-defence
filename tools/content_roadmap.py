"""The phased engagement roadmap.

Content source: "Pitch on 3 phases.pdf". Copy is deliberately tight.
"""

from layout import ARROW, page_hero, cta_band, ruled, accordion, cards, DISCLAIMER


def roadmap_page():
    body = page_hero(
        "Engagement roadmap",
        "Support today, indigenous capability later",
        "Practical, scalable solutions that strengthen readiness now while building national "
        "capability. Three phases, and each one earns the next.",
        trail=[("Roadmap", None)],
        actions=f'<div class="hero__actions"><a class="btn btn--primary" '
                f'href="{{P}}contact/index.html">Discuss the roadmap {ARROW}</a></div>',
    )

    body += f'''
  <section class="section section--tight section--ink2">
    <div class="shell">
      <div class="split">
        <div>
          <p class="eyebrow">Purpose</p>
          <h2 class="d3">Practical, scalable, modernization-aligned.</h2>
        </div>
        <div class="prose">
          <p>
            Support for the Nigerian Armed Forces across communications, protection,
            surveillance, mobility and long-term defence industrialisation.
          </p>
          <p>
            Phase one needs no structural change and delivers value immediately. Phase two goes
            deeper once we know the terrain. Phase three is a multi-year national commitment.
          </p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--paper">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Phase one · short term</p>
        <h2 class="d2">Immediate support, no reorganisation</h2>
      </div>
      <div class="split">
        <div>
          <h3 class="d4">A · Hardware selection</h3>
          <p class="lede mt-16">
            Guidance on reliable, mission-appropriate equipment in non-weaponized categories.
          </p>
          {ruled([
              ("Radios", "Tactical and base communications."),
              ("Body armour", "Protection matched to threat and task."),
              ("Tactical uniforms", "Durability and climate suitability."),
              ("Vehicles", "Terrain suitability and maintainability."),
          ])}
          <p class="mt-24"><strong>Delivered as:</strong> comparison matrices, specifications
          and suitability assessments.</p>
        </div>
        <div>
          <h3 class="d4">B · Supply chain</h3>
          <p class="lede mt-16">
            A procurement pipeline for vetted equipment, accountable at every handoff.
          </p>
          {ruled([
              ("Vetted pipeline", "A repeatable route to market for approved categories."),
              ("Trusted suppliers", "OEM and regional supplier qualification."),
              ("Logistics", "Importation, warehousing and distribution."),
              ("Traceability and QA", "Documented provenance and inspection."),
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
      </div>
      {accordion("phase2", [
          ("A. Operational gap analysis",
           "<p>Structured listening sessions with unit commanders to surface the challenges that "
           "do not appear in formal reporting.</p><p>Pain points we map:</p><ul>"
           "<li>Communication gaps</li><li>Mobility limits</li>"
           "<li>Surveillance blind spots</li><li>Equipment fatigue and maintenance</li></ul>"
           "<p>Output is a solution set per domain, prioritised by readiness impact.</p>"),
          ("B. High-level capability requirements",
           "<p>Non-operational discussions that help define purpose-based requirements.</p>"
           "<p>Topics in scope:</p><ul>"
           "<li>Drones for ISR, logistics or surveillance</li>"
           "<li>Aircraft range, endurance and payload</li>"
           "<li>Non-weaponized detection systems</li>"
           "<li>Specifications that matter for procurement</li></ul>"
           "<p>This is requirements definition, and it stays clear of restricted operational "
           "guidance.</p>"),
      ])}
    </div>
  </section>

  <section class="section section--ink2 section--line">
    <div class="shell">
      <div class="section-head">
        <p class="eyebrow">Phase three · long term</p>
        <h2 class="d2">A Nigerian defence-industry ecosystem</h2>
        <p class="lede mt-16">
          Built on engineering, design and manufacturing, as a strategic partner rather than a
          supplier of imports.
        </p>
      </div>
      <div class="split">
        <div>
          <h3 class="d4">A · Design and manufacturing</h3>
          <p class="lede mt-16">Local production capacity for non-weaponized systems.</p>
          {ruled([
              ("Tactical vehicles", "Local assembly, then design capability."),
              ("Communication systems", "Domestic production and integration."),
              ("Surveillance platforms", "Indigenous observation systems."),
              ("Protective equipment", "Body armour and personal protection."),
          ])}
          <p class="mt-24">Supported by university engineering partnerships and local assembly
          and maintenance hubs.</p>
        </div>
        <div>
          <h3 class="d4">B · Strategic partnership</h3>
          <p class="lede mt-16">Multi-year collaboration rather than transactional supply.</p>
          {ruled([
              ("Multi-year collaboration", "Sustained engagement with Army leadership."),
              ("Joint R&amp;D", "Co-developed research with domestic institutions."),
              ("Workforce development", "Building the engineering and technician base."),
              ("Technology transfer", "Structured transfer that conveys real capability."),
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
          ("Rapid deployment", "Immediate operational impact, no reorganisation first."),
          ("Cost-effective", "A non-weaponized focus cuts procurement complexity."),
          ("Local capability", "Supports Nigeria's defence industrialisation goals."),
          ("Interoperability", "Designed to integrate with existing Army platforms."),
      ], cols=4)}
      <div class="mt-56">
        <div class="quote">
          <p>
            A dependable partner in Nigeria's modernization: support today, growing into full
            indigenous capability tomorrow.
          </p>
          <cite>Pinnacle Precision Engineering &amp; Consulting Limited</cite>
        </div>
      </div>
      <div class="mt-40">{DISCLAIMER}</div>
    </div>
  </section>

''' + cta_band()

    return ("roadmap/index.html", "Engagement roadmap",
            "A three-phase roadmap: short-term hardware selection and supply chain support, "
            "mid-term operational gap analysis, and long-term indigenous design and "
            "manufacturing.",
            body)


def all_roadmap_pages():
    return [roadmap_page()]
