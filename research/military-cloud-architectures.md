# Publicly documented military cloud architectures

Source material for a sovereign-cloud capability. Everything here is **publicly released**
and citable. Verified by direct retrieval on 28 August 2026 unless marked otherwise.

> Companion to `sovereign-infrastructure-capability.md`, which covers the facility layer.
> This document covers the **cloud architecture** layer the founder actually asked about.

---

## 1. What is publicly available

The US Department of Defense publishes its cloud reference architectures openly. This is the
single richest public source of defence cloud design, and it is free to study and cite.

Index: **https://dodcio.defense.gov/Library/**

### The documents that matter most

| Document | Why it matters |
|---|---|
| **DoD Enterprise DevSecOps Reference Design — AWS Managed Services** (draft, cleared 19 Oct 2021) | A public, named-service reference design for building defence workloads **on AWS**. See §2 below. |
| **DoD Enterprise DevSecOps Reference Design — CNCF Kubernetes** | The vendor-neutral equivalent. Also a Multi-Cluster Kubernetes variant. |
| **Cloud Native Access Point (CNAP) Reference Design v1.0** | How to reach cloud-hosted defence workloads **without a traditional network perimeter**. See §3. |
| **DoD Zero Trust Reference Architecture v2.0** (Sep 2022) | The zero trust model defence is actually building to. |
| **DoD Zero Trust Strategy**, Capabilities and Activities, Capability Execution Roadmap | The implementation sequencing behind the RA. |
| **DoD Cloud Security Playbook** — Overview, Vol 1, Vol 2 | Operational cloud security guidance. |
| **DoD Enterprise ICAM Reference Design** | Identity, credential and access management across the enterprise. |
| **DoD Cybersecurity Reference Architecture** | The overarching security architecture. |
| **DoD OCONUS Cloud Strategy** | Cloud outside the continental US — the closest public analogue to a *sovereign//overseas* deployment problem. |
| **DoD Cloud FinOps Strategy** | Cost governance, which government buyers always ask about. |
| **DoD Software Modernization Strategy** + FY25–26 Implementation Plan | The programme context. |
| **Memo: FedRAMP Equivalency for Cloud Service Providers** | How accreditation reciprocity is handled. |
| **DoD Data Strategy**, AI Strategy, Cyber Strategy (summaries) | Policy framing. |
| Also on the index | DoD Architecture Framework (DoDAF), Private 5G Deployment Strategy, Post Quantum Cryptography Strategy, ICT-SCRM Strategy, DevSecOps Fundamentals, Activities & Tools Guidebook, DevSecOps Playbook |

Some CIO/CISO memo pages require CAC access and are not openly downloadable. Everything
listed above was retrievable without authentication.

---

## 2. DoD Enterprise DevSecOps Reference Design — AWS Managed Services

Recovered structure and named services (verified by text extraction from the published PDF):

**Architecture layers**
1. Assumptions and Principles — including the stated benefits of adopting **DoD Cloud
   Infrastructure as Code (IaC)** baselines
2. Software Factory Interconnects
   - **Cloud Native Access Points** (ties directly to the CNAP design in §3)
   - **CNCF Certified Kubernetes: AWS Elastic Kubernetes Service (EKS)**
   - **Locally Centralized Artifact Repository: AWS Elastic Container Registry (ECR)**
   - **Incorporate Zero Trust Principles: AWS App Mesh**
3. Software Factory K8s Reference Design — accessing the DoD Cloud IaC baselines; the
   containerised software factory
4. Hosting Environment — container orchestration
5. Additional Tools and Activities — continuous monitoring in Kubernetes, including
   **CSP-managed services for continuous monitoring**
6. Appendix — accessing the DoD Cloud IaC code repository

**The reusable idea:** the government publishes *infrastructure-as-code baselines* that
mission owners inherit, rather than every programme designing its own landing zone. That is
the single most transferable pattern in the whole document set, and it is directly
applicable to a Nigerian MDA context.

> **Currency warning.** This is a 2021 draft. Service choices have moved on — AWS App Mesh
> in particular has been superseded for new work. Cite the document for its *architecture
> and governance model*, never for its specific service list, or a competent reviewer will
> date you immediately.

---

## 3. Cloud Native Access Point (CNAP) Reference Design v1.0

The problem CNAP solves: how does a soldier or contractor reach a cloud-hosted application
when there is no longer a network perimeter to sit inside? It is expressed in **DoDAF**
notation (a CV-2 capability taxonomy), which is itself worth knowing.

**Four core capabilities**
- **C.1 — Authenticated and Authorized Entities**
- **C.2 — Authorized Ingress**
- **C.3 — Authorized Egress**
- **C.4 — Security Monitoring and Compliance Enforcement**, comprising:
  - Monitoring and Remediation
  - Compliance Auditing and Enforcement
  - Integrated Visibility with CSSP/DCO (cyber service provider / defensive cyber ops)
  - **Continuous Authorization to Operate (cATO)**

**Logical design patterns:** access to a Mission Owner cloud enclave; access to SaaS services.

**Data flows documented:** CSP portal access; SaaS access; authorised ingress; authorised
egress; security monitoring and compliance enforcement.

**Responsibility split** — this is the part worth copying: DoD Enterprise / Mission Owner /
Mission Partners / Cloud Service Provider each have separately enumerated obligations.

**The reusable ideas:**
- **cATO** — continuous authorisation instead of a periodic accreditation event. This is the
  most valuable concept in the corpus for a country writing new cloud rules.
- Explicit **authorised ingress and egress** as named architectural capabilities.
- A written four-way responsibility matrix, so no control is assumed to be someone else's.

---

## 4. Platform One / Big Bang — a working, public implementation

Where the documents above are designs, **Big Bang** is the running code, publicly documented
at **https://docs-bigbang.dso.mil/**.

- **Model:** a Helm umbrella chart deploying a curated DevSecOps stack onto Kubernetes,
  reconciled by **Flux** from Git (GitOps). Shared library charts (`bb-common`, `gluon`)
  standardise service mesh, network policy and route resources across packages.
- **Service mesh / ingress:** Istio (`istiod`, `istio-cni`, `istio-crds`, `istio-gateway`,
  `ztunnel`), Gateway API, Kiali. Sidecar and Ambient modes, Ambient in beta.
- **Observability:** Fluent Bit and Grafana Alloy, Loki, Elasticsearch/Kibana via ECK;
  Prometheus Operator, Alertmanager, Grafana, Tempo for traces, Thanos or Mimir for
  long-term metrics.
- **Policy and runtime security:** Kyverno (+ policies, reporter), OPA Gatekeeper, NeuVector,
  Twistlock.
- **Scanning:** Anchore Enterprise, SonarQube, Fortify.
- **Identity:** Keycloak plus Authservice for per-application OIDC/SSO enforcement.
- **Platform services:** GitLab + Runner, Harbor, MinIO, Vault, External Secrets Operator,
  cert-manager, Velero for backup/restore.
- **Secrets:** SOPS-encrypted values committed to Git; External Secrets Operator and Vault
  at runtime.
- **Hardened images:** consumes **Iron Bank** hardened, non-root container images from
  Repo1; upstream charts are modified to run on them.
- **Deployment profiles that matter for defence:** standard, **airgap**, resource-constrained
  ("appliance mode"), and an SSO quickstart.

**The reusable ideas:**
- **Airgap and appliance-mode installs** — directly relevant to forward operating bases and
  to a Level 4 environment that must never touch a foreign region.
- **Hardened base images from an accredited registry** as a supply-chain control.
- **GitOps as the audit trail** — every change is a reviewable commit, which is exactly what
  a continuous-authorisation regime needs.

---

## 5. Sovereignty precedents worth knowing

- **Estonia's data embassy** — state data replicated to servers in Luxembourg under
  diplomatic-premises status, so the data remains under Estonian jurisdiction while sitting
  physically abroad. The sharpest existing answer to "what if the country itself is
  unavailable." *(General knowledge — verify at e-estonia.com before citing.)*
- **Dedicated in-country hyperscaler infrastructure** operated to customer-specified controls
  with screened local staff. Singapore's government is the usual public reference.
  *(Verify current product naming and the Singapore reference before citing.)*
- **On-premises hyperscaler hardware** in the customer's own facility, so data at rest never
  leaves the country while the platform APIs remain identical.
- **Edge / ruggedised compute** for disconnected and tactical sites.

---

## 6. How this maps to Nigeria

Nigeria's instruments (verified: National Cloud Technical Guideline 2026 and National
Guideline for Cloud Computing in Nigeria 2026, both NITDA, approved 4 August 2026, effective
1 January 2027, enforcement status **Mandatory**; target audience Federal Public
Institutions, State Governments, Cloud Service Providers, Data Centre Operators) create a
**data classification model — Levels 1 to 4 — that plays the same structural role as the DoD
Impact Levels.** Level 4 includes military intelligence and may never leave Nigeria.

That correspondence is the intellectual core of the offer:

| DoD concept | Nigerian equivalent | What it lets you do |
|---|---|---|
| Impact Levels IL2–IL6 | NITDA Levels 1–4 | Build a **placement matrix**: which workload may sit where |
| Cloud IaC baselines inherited by mission owners | *does not exist yet in Nigeria* | Offer to author reusable, compliant landing-zone baselines for MDAs |
| CNAP authorised ingress/egress | *not yet specified* | Design the access architecture against a published model |
| cATO — continuous authorisation | NITDA/ONSA audit regime | Propose continuous compliance evidence instead of point-in-time audit |
| Iron Bank hardened images | *does not exist* | Propose a hardened image baseline for government workloads |
| Airgap / appliance mode | Level 4 on-premises requirement | The technical answer to strict residency |

**The gap is the opportunity.** Nigeria has published the *rules* but not the *reference
architectures*. The DoD has published reference architectures for exactly this problem
shape. Adapting the second to the first is legitimate, citable, high-value advisory work
that nobody in the Nigerian market appears to have packaged.

---

## 7. Services this supports

Assuming certified staff and partner standing are in place:

1. **Data classification and workload placement** — map an MDA's systems onto Levels 1–4 and
   produce the placement matrix. First engagement; needs judgement and the instruments, not
   certifications.
2. **Sovereign landing zone design** — account structure, network segregation, identity,
   logging, and residency guardrails **enforced technically** so a workload cannot deploy to
   a non-compliant location. Modelled on the published IaC-baseline pattern.
3. **Access architecture** — authorised ingress/egress and identity-centric access to cloud
   workloads, modelled on CNAP rather than invented.
4. **Key custody and encryption design** — customer-managed keys held in Nigeria. The control
   that answers the extraterritorial-access objection.
5. **Continuous compliance and evidence** — GitOps-based change control and automated control
   evidence, adapting the cATO concept to the NITDA/ONSA audit regime.
6. **Air-gapped and edge deployment design** — Level 4 on-premises environments and
   disconnected forward sites, modelled on published airgap/appliance patterns.
7. **Hardened baseline and supply chain** — an Iron Bank-equivalent hardened image and
   provenance regime for government workloads.
8. **The facility that hosts it** — siting, power, cooling, physical security. Covered in the
   companion document; this is the part a software consultancy cannot do.

Items 1–7 are the cloud practice. Item 8 is the existing business. **The combination is the
differentiated position**: no pure cloud consultancy can engineer the data hall, and no
engineering firm can classify the workloads.

---

## 8. Honest caveats

- The AWS reference design is a **2021 draft**. Use it for architecture and governance
  patterns, never for its service list.
- These are **US** documents. Cite them as *international good practice being adapted*, never
  as standards Nigeria is subject to. Applying US doctrine to a threat picture set by
  Nigerian intelligence reads badly to a Nigerian Army audience.
- I did **not** retrieve: the Zero Trust RA body text, the Cloud Security Playbook volumes,
  the ICAM Reference Design, or the CNCF Kubernetes reference design. Only their existence
  and titles are confirmed. Read them before relying on their contents.
- Estonia and the dedicated-infrastructure precedents in §5 are from general knowledge and
  need verification before appearing in client material.
- No public source shows a Nigerian firm holding this scope. That is either an opening or a
  sign the buyer does not exist yet; this research cannot tell you which.
