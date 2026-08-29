# Walkthrough script

A spoken script for demonstrating the site to someone — an Army stakeholder, a partner, an
investor, or a colleague. Roughly 6–8 minutes at a normal pace.

**Focus:** what the company can do now, and what it will be doing. Not what the website is.

---

## Before you start

The site is live at **https://siryemi.github.io/pinnacle-precision-defence/**

If the room has bad wifi, run it locally instead — it works fully offline:

```bash
cd lekanpinnacle
python3 -m http.server 8000     # then open http://localhost:8000
```

Note that `localhost` only works in a browser on the same machine as the server.

**Skip these three in a live demo** — they are deliberately unfinished and will undercut you:
Leadership (placeholder names), Insights (nothing written yet), and the Legal pages (marked as
drafts). Nothing in the route below touches them.

---

## Step 1 — Land on the home page

**They see:** a dark page, and one line: *"Engineering readiness for secure operations."*

**Say:**
> "We are an Abuja engineering and construction firm. What we do for defence is keep
> infrastructure and equipment working — so that when a unit needs a facility, a vehicle or a
> store, it is available. That is the whole idea: readiness."

Point at the line underneath it.

> "Four things we already do: secure design, reliable construction, disciplined supply
> chains, and data-driven asset management. And a fifth built on top — sovereign cloud and AI."

---

## Step 2 — Scroll down once, to "Defence positioning"

**They see:** a short paragraph on the right.

**Say:**
> "The founding team has over fifteen years of combined experience in engineering,
> construction and supply chain. This is not a new capability — it is existing capability
> pointed at defence."

---

## Step 3 — Scroll to "Five capability pillars" and click through the tabs

This is the core of the pitch. Click each tab, pause on each, and say one sentence. Five tabs.

**Tab 1 — Engineering design.** A diagram appears showing FEED → DETAIL → REVIEW → IFC.
> "We design the facility before anyone builds it. Command centres, secure stores, blast-aware
> structures, the power and water systems inside them. We take it from concept all the way to
> the drawings a contractor builds from."

**Tab 2 — Military construction.** A site plan appears with a controlled perimeter.
> "Then we build it. Barracks, training grounds, logistics hubs, perimeters, secure storage.
> And we specify for the maintenance budget that will actually exist — not the one on paper."

**Tab 3 — Defence supply chain.** A four-stage flow: qualify → source → receive → issue.
> "We also run the procurement. We qualify the vendor, source the equipment, inspect it on
> arrival, and issue it to the unit — with a paper trail at every handoff. Radios, body armour,
> uniforms, vehicles, surveillance equipment."

**Tab 4 — Modernization consulting.** A chart showing wear detected before failure.
> "And this is where it gets interesting. We put sensors on vehicles and generators, and the
> data tells us a part is failing before it fails. You fix it on a Tuesday in the workshop
> instead of on an operation."

---

**Tab 5 — Sovereign cloud & AI.** A diagram of data classification Levels 1 to 4.
> "And this is the newest one. Nigeria's cloud rules classify government data from Level 1 to
> Level 4 — and Level 4, which includes military intelligence, may never leave the country.
> We classify the workloads, design the environment that's allowed to hold them, and engineer
> the building it sits in. Nobody else does both halves."

---

## Step 3b — Sovereign cloud and AI, in depth

Worth its own stop if the person in the room is technical or from an ICT directorate. Click
**Capabilities → Sovereign Cloud & AI Infrastructure**.

**They see:** an overview, then a full-width layered reference architecture diagram.

**Say, pointing at the diagram from the bottom up:**
> "Read this from the bottom. Layer six is the facility — power, cooling, earthing, physical
> security. That's the business we already run.
>
> Layer five is the platform physically inside Nigeria. Four is the control plane — identity,
> policy guardrails, and key custody, with the keys held here, not abroad. Three is AI. Two is
> the workload zones, and notice Level 4 in gold — that one is air-gapped, no connection out.
> One is how people reach it.
>
> And that dashed band down the right spans every layer: compliance evidence is produced
> continuously, not assembled the week before an audit."

Then the key line:
> "A software consultancy can design layers one to five but cannot engineer layer six. An
> engineering firm can build layer six but cannot classify the workloads. The rules require
> both. That's the position."

Scroll to the **AI section**:
> "AI here is a data-governance problem before it's a technology problem. The question isn't
> which model — it's which data we're lawfully allowed to train on, and where that training is
> allowed to physically happen. We answer that first, in writing, before anyone builds
> anything."

And read the last row of the AI list out loud — it matters:
> "We don't build autonomous targeting or weapons systems, and we don't build AI for
> surveillance aimed at civilians. A human stays accountable for every consequential decision."

**Then scroll to "What we are, and what we are not"** and read the *not* list. This page makes
the strongest claims on the site, so the limits do the most work here: not a cloud provider,
not a data centre operator, not a reseller, holds no assurance certification, does not host
data or hold keys.

> **Note for the demo:** this page carries a gold placeholder for cloud partner tier and
> certified architect headcount. Until those are real, do not present this pillar as available
> today — present it as the direction, with the facility layer available now.

---

## Step 4 — Scroll to "Readiness outcomes, not deliverables"

**They see:** four cards — reduce mission risk, accelerate delivery, improve asset uptime,
strengthen accountability.

**Say:**
> "Every job we propose has to move one of these four. If it doesn't move any of them, we will
> tell you it's the wrong job. That is how we want to be measured."

---

## Step 5 — Click "Roadmap" in the top menu

This is the most important page in the pitch, because it answers "what will you be doing."

**They see:** three phases down the page.

**Say, pointing at each:**
> "Phase one — right now. We help you choose equipment and stabilise the supply chain. You
> don't have to reorganise anything for this to start working.
>
> Phase two — once we know each other. We sit down with commanders and map what is actually
> broken: communications, mobility, surveillance blind spots, equipment fatigue, maintenance.
> Then we solve those specific things.
>
> Phase three — the real goal. Building it in Nigeria. Local assembly and maintenance hubs,
> partnerships with Nigerian universities, technology transfer. Tactical vehicles,
> communications, surveillance platforms, protective equipment — made here."

Then scroll to the quote at the bottom and read it out:
> "Support today, growing into full indigenous capability tomorrow."

---

## Step 6 — Go back to the top menu, hover "Capabilities", click "Military Construction"

Pick whichever pillar matters most to the person in the room. This shows depth.

**They see:** an overview, then a list of what the work includes, then expandable applications.

**Say:**
> "Every capability opens up like this. What the work includes, how a typical job arrives, and
> what you are left holding at the end."

Click one of the expandable rows — for example *"Water and power resilience works."*
> "This one is often the fastest win on an established site. Backup generation, boreholes, a
> mini-grid — and the maintenance plan to keep them running."

Scroll to **"What the client is left holding."**
> "Notice this: as-built drawings, maintenance manuals, quality records, and a trained team.
> You are not dependent on us afterwards. That is deliberate."

---

## Step 7 — Hover "Sectors", click "Nigerian Army"

**They see:** an Army-specific page.

**Say:**
> "The Army is our first focus. Same four capabilities, applied to Army problems — vehicle
> availability, barracks, training facilities, power and water, stores discipline."

Point at the note in the gold box.
> "And we are explicit here: these are proposed applications for discussion. We are not
> claiming contracts we haven't done."

**Why this matters:** say that line out loud. Anyone experienced will be checking whether you
are overclaiming. Saying it first earns you credibility for everything else on the page.

---

## Step 8 — Click "About", scroll to "A practical path from needs assessment to lifecycle support"

**They see:** four stages — Assess, Design, Deliver, Sustain.

**Say:**
> "Every job runs the same four stages. We assess the site properly first, we design it, we
> deliver it, and we stay through handover and training. And all of it inside your own
> procurement and security rules."

---

## Step 9 — Scroll to "Non-weaponized by design" on the home page

**Say:**
> "One thing to be clear about. We do not supply weapons or ammunition. Radios, armour,
> uniforms, vehicles, surveillance, field gear — yes. Ordnance — no.
>
> That is a commercial advantage, not a limitation. It keeps procurement simple and gets
> capability delivered faster."

---

## Step 10 — Close on "Contact"

**Say:**
> "Four ways to start: a capability briefing, a proposal discussion, a partnership meeting, or
> a site assessment. The site assessment is usually the honest place to begin — let us come
> and look at the actual site before anyone writes a proposal."

---

## The 30-second version

If you only get one lift's worth of time:

> "We are an Abuja engineering and construction firm doing four things for defence: we design
> secure facilities, we build them, we run the supply chain that equips them, and we use sensor
> data to keep vehicles and generators running. On top of that we classify government data
> against Nigeria's new cloud rules and design the sovereign environment and AI that runs
> inside it — including the building it physically sits in, which nobody else combines. We
> start by helping you buy the right kit. We end up manufacturing it in Nigeria."

---

## What to add next

Ranked by what would most improve the pitch. The first two are worth more than everything else
combined.

### 1. Proof — a "Projects" page

The single biggest gap. Right now the site describes capability with nothing behind it. Every
experienced person in the room will silently ask *"what have you actually built?"*

Add three to five completed projects — civil, commercial, anything — with photographs, scope,
value and duration. They do not need to be defence projects. A well-executed commercial
building proves you can execute; the defence framing is then believable.

### 2. Credentials strip

Add a band showing: CAC/RC number, COREN registration, BPP contractor registration,
professional indemnity insurance, ISO 9001 if held. For public defence work these get asked for
first, and BPP registration is close to a prerequisite for federal contracts.

Put these on the home page as a small strip. It answers the procurement officer's real question
before they have to ask it.

### 3. A downloadable capability statement (PDF)

Procurement officers forward documents, not links. One or two pages: who you are, four pillars,
credentials, contact. Generated from the same content so it never contradicts the site.

### 4. Real leadership profiles

Names, photographs, qualifications, COREN registration numbers. Engineering is sold on the
credibility of named individuals. Publish only what is verified and personally approved.

### 5. Partner and OEM logos

If you have supplier or manufacturer relationships for phase one, name them (with permission).
It shows the supply chain is real rather than aspirational.

### 6. One number on the home page

Something concrete — projects delivered, square metres built, years operating. There is
currently no figure anywhere on the site. One verifiable number is worth several paragraphs.
Do not invent it.

### 7. A Nigerian phone number

The contact number is currently a US line against an Abuja headquarters. It works, but it
invites a question you would rather not answer in a first meeting.

### 8. Two written insight pieces

The Insights section is an empty pipeline. Two properly written pieces — say, "why predictive
maintenance beats more spares" and "designing barracks for the maintenance budget that will
actually exist" — demonstrate thinking that no amount of marketing copy can.
