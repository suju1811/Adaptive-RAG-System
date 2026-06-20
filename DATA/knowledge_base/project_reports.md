# Project Reports — Northstar Dynamics

## Document Metadata

- **Document type:** Project Reports
- **Scope:** Active project portfolio with budgets, timelines, deliverables, dependencies, team rosters, and links to vendors and risks.
- **Topics:** projects, milestones, deliverables, budgets, dependencies, project health, team assignments
- **Entity types:** Project, Employee, Vendor, Contractor, Risk
- **ID prefixes:** P- (projects); references E-, V-, C-, R-, D- from other domains
- **Key sections:** Portfolio Overview, Project Summaries
- **Cross-references:** Each project profile links to leads/sponsors (E-), dependencies (P-, V-), team members (E-, C-), and risks (R-)
- **Relationship hints:** leads, sponsors, depends_on, uses_vendor, has_risk, member_of team

---

## 1. Portfolio Overview

| Project ID | Project Name                        | Business Unit            | Lead ID | Sponsor ID | Start Date | Target Date | Status      | Priority | Budget (₹L) |
|------------|-------------------------------------|--------------------------|---------|------------|------------|-------------|-------------|----------|-------------|
| P-200      | Atlas Core Platform Upgrade         | Engineering Platform     | E-007   | E-003      | 2025-01-08 | 2025-09-30  | In Progress | High     | 120         |
| P-210      | Northstar Self-Service HR Portal    | Human Resources          | E-006   | E-004      | 2025-02-14 | 2025-08-15  | In Progress | High     | 65          |
| P-220      | Vendor Risk Monitoring Revamp       | Risk & Compliance        | E-017   | E-018      | 2025-03-01 | 2025-10-20  | Planned     | High     | 80          |
| P-230      | Procurement Workflow Automation     | Procurement & Vendor Ops | E-014   | E-013      | 2025-01-22 | 2025-07-31  | In Progress | Medium   | 55          |
| P-240      | Product Analytics Migration         | Product Management       | E-011   | E-010      | 2025-02-05 | 2025-11-15  | In Progress | High     | 75          |
| P-250      | Identity and Access Modernization   | Engineering Platform     | E-009   | E-003      | 2025-04-01 | 2025-12-31  | Planned     | High     | 90          |

---

## 2. Project Summaries

### P-200 — Atlas Core Platform Upgrade
**Owner Department:** Engineering Platform (D-120)
**Project Lead:** Arjun Rao (E-007)
**Sponsor:** Meera Iyer (E-003)
**Status:** In Progress
**Health:** Amber (minor timeline risk on CI/CD stream)

**Objective:**
Modernize internal platform services, improve deployment reliability, reduce operational incidents, and establish a stable API surface for downstream projects.

**Scope:**
This is the foundational platform project. Three other projects (P-210, P-230, P-240) directly depend on platform APIs that P-200 is modernizing. Delays in P-200 create a cascade risk across the portfolio.

**Key Deliverables:**
| Deliverable                      | Owner  | Status      | Target     |
|----------------------------------|--------|-------------|------------|
| Service mesh upgrade (Istio 1.20)| E-007  | In Progress | 2025-06-15 |
| Observability dashboard rollout  | E-008  | In Progress | 2025-07-01 |
| CI/CD pipeline hardening         | E-008  | Not Started | 2025-08-01 |
| Legacy service deprecation plan  | E-007  | In Progress | 2025-07-15 |
| API gateway migration            | E-008  | Not Started | 2025-09-01 |
| Rollback test suite              | E-007  | In Progress | 2025-06-30 |

**Milestones:**
- M1: Service mesh pilot (2 services) — Completed 2025-03-20
- M2: Full service mesh rollout — Target 2025-06-15
- M3: Observability v1 live — Target 2025-07-01
- M4: CI/CD hardening complete — Target 2025-08-01
- M5: Legacy deprecation signed off — Target 2025-09-15
- M6: Final release and handoff — Target 2025-09-30

**Dependencies:**
| Depends On   | Type      | Reason                                         | Status     |
|--------------|-----------|------------------------------------------------|------------|
| P-250        | Hard      | Identity integration required for API gateway  | Blocked    |
| V-300        | Hard      | Cloud monitoring and disaster recovery support  | Active     |
| V-310        | Soft      | Migration tooling and access control review    | Pending    |

**Team:**
- Arjun Rao (E-007) — Lead, architecture decisions
- Sana Ahmed (E-008) — Implementation, observability
- Elena Rossi (C-400) — Staff augmentation from CloudNova (V-300)

**Budget:**
- Approved: ₹120L
- Spent to date: ₹42L
- Forecast to complete: ₹110L (within budget)

**Key Risks:**
- R-500: Platform outage during migration (High severity, owned by E-007)
- Secondary: P-250 blocker delays API gateway stream

---

### P-210 — Northstar Self-Service HR Portal
**Owner Department:** Human Resources (D-110)
**Project Lead:** Priya Nair (E-006)
**Sponsor:** Nisha Verma (E-004)
**Status:** In Progress
**Health:** Green

**Objective:**
Provide employees with a unified self-service portal for onboarding, leave management, policy access, and manager workflows — reducing HR team handling time by 60%.

**Scope:**
Portal will replace 3 legacy internal tools currently hosted on intranet. Policy knowledge base will use DocuFlow's search indexing (V-320). HR approvals will be integrated with P-200's API layer.

**Key Deliverables:**
| Deliverable                        | Owner  | Status      | Target     |
|------------------------------------|--------|-------------|------------|
| Employee profile module            | E-006  | Completed   | 2025-04-01 |
| Policy knowledge search (DocuFlow) | E-014  | In Progress | 2025-06-01 |
| Leave request + approval workflow  | E-006  | In Progress | 2025-07-01 |
| Manager dashboard                  | E-005  | Not Started | 2025-07-15 |
| Onboarding checklist module        | E-005  | Not Started | 2025-08-01 |

**Milestones:**
- M1: Employee profile module live — Completed 2025-04-01
- M2: DocuFlow search integration — Target 2025-06-01
- M3: Leave workflow UAT — Target 2025-07-01
- M4: Policy sign-off from D-150 — Target 2025-07-10
- M5: Full portal launch — Target 2025-08-15

**Dependencies:**
| Depends On   | Type  | Reason                                                        | Status     |
|--------------|-------|---------------------------------------------------------------|------------|
| P-200        | Hard  | Platform APIs for authentication and profile management       | In Progress|
| V-320        | Hard  | DocuFlow document search and indexing for policy knowledge base| Active    |
| D-150        | Hard  | Policy content approval from Risk & Compliance before launch  | Not Started|

**Team:**
- Priya Nair (E-006) — Lead
- Karan Shah (E-005) — Manager workflows
- Ritu Das (E-012) — UX research
- Fatima Khan (C-420) — DocuFlow implementation contractor

**Budget:**
- Approved: ₹65L
- Spent to date: ₹28L
- Forecast to complete: ₹60L (within budget)

**Key Risks:**
- R-510: Outdated HR policy content (Medium severity, owned by E-004)
- Secondary: Approval bottlenecks in manager workflow if manager counts are underestimated

---

### P-220 — Vendor Risk Monitoring Revamp
**Owner Department:** Risk & Compliance (D-150)
**Project Lead:** Gaurav Menon (E-017)
**Sponsor:** Neha Kapoor (E-018)
**Status:** Planned
**Health:** Not yet started (awaiting P-230 data readiness)

**Objective:**
Build a centralized, real-time view of vendor health, contract exposure, and risk signals — enabling proactive escalation instead of reactive incident response.

**Scope:**
The project consumes vendor master data from P-230 (Procurement automation) and risk signal feeds from ComplyGrid (V-330) and CloudNova (V-300). Output is a live risk dashboard used by D-150 and reported to the board quarterly.

**Key Deliverables:**
| Deliverable                        | Owner  | Status      | Target     |
|------------------------------------|--------|-------------|------------|
| Vendor scoring model v1            | E-017  | Not Started | 2025-07-01 |
| Contract expiration alert engine   | E-016  | Not Started | 2025-08-01 |
| Risk taxonomy dashboard            | E-017  | Not Started | 2025-09-01 |
| Exception and escalation workflow  | E-018  | Not Started | 2025-10-01 |
| Board reporting pack (automated)   | E-016  | Not Started | 2025-10-20 |

**Milestones:**
- M1: Data readiness sign-off from P-230 — Target 2025-06-30
- M2: Vendor scoring model complete — Target 2025-07-30
- M3: Dashboard v1 live — Target 2025-09-15
- M4: Full system launch — Target 2025-10-20

**Dependencies:**
| Depends On   | Type  | Reason                                               | Status     |
|--------------|-------|------------------------------------------------------|------------|
| P-230        | Hard  | Vendor master data feeds required for scoring model  | In Progress|
| V-300        | Soft  | Risk signal ingestion from CloudNova monitoring APIs | Active     |
| V-330        | Hard  | External compliance and regulatory feeds             | Active     |

**Team:**
- Gaurav Menon (E-017) — Lead, risk modeling
- Farah Ali (E-016) — Compliance requirements, regulatory feeds
- Arjun Bhat (C-430) — ComplyGrid support contractor

**Budget:**
- Approved: ₹80L
- Spent to date: ₹0L (not yet started)
- Forecast to complete: ₹75L

**Key Risks:**
- R-520: Vendor concentration risk (Critical severity, owned by E-017)
- R-560: Regulatory feed delay from V-330 (Medium severity, owned by E-016)

---

### P-230 — Procurement Workflow Automation
**Owner Department:** Procurement & Vendor Ops (D-140)
**Project Lead:** Leena Thomas (E-014)
**Sponsor:** Imran Khan (E-013)
**Status:** In Progress
**Health:** Amber (integration delay with InvoiceLoop)

**Objective:**
Eliminate manual procurement steps — purchase request routing, approval escalation, contract versioning, and invoice matching — reducing end-to-end procurement cycle time by 50%.

**Scope:**
Automates 4 core procurement workflows. Integrates DocuFlow (V-320) for e-signature and InvoiceLoop (V-340) for invoice validation. Serves as the upstream data provider for P-220 (Vendor Risk Monitoring).

**Key Deliverables:**
| Deliverable                        | Owner  | Status      | Target     |
|------------------------------------|--------|-------------|------------|
| Purchase request intake module     | E-014  | Completed   | 2025-03-15 |
| Approval matrix automation         | E-013  | In Progress | 2025-05-30 |
| Contract version tracking          | E-014  | In Progress | 2025-06-15 |
| E-signature integration (DocuFlow) | C-420  | In Progress | 2025-06-15 |
| Invoice validation API (InvoiceLoop)| E-015 | Not Started | 2025-07-01 |
| SLA reminder engine                | E-014  | Not Started | 2025-07-15 |

**Milestones:**
- M1: Purchase request module live — Completed 2025-03-15
- M2: Approval matrix UAT — Target 2025-05-30
- M3: E-signature integration complete — Target 2025-06-15
- M4: InvoiceLoop API integration — Target 2025-07-01
- M5: Full system launch — Target 2025-07-31

**Dependencies:**
| Depends On   | Type  | Reason                                               | Status     |
|--------------|-------|------------------------------------------------------|------------|
| P-200        | Hard  | Authentication services required for approval routing| In Progress|
| V-320        | Hard  | E-signature integration for contract routing         | Active     |
| V-340        | Hard  | Invoice validation API integration                   | Delayed    |

**Team:**
- Leena Thomas (E-014) — Lead
- Kabir Jha (E-015) — Invoice ops, spend analysis
- Imran Khan (E-013) — Sponsor and approval matrix sign-off
- Fatima Khan (C-420) — DocuFlow implementation

**Budget:**
- Approved: ₹55L
- Spent to date: ₹24L
- Forecast to complete: ₹52L (within budget)

**Key Risks:**
- R-530: Approval routing failure (Medium severity, owned by E-014)
- Secondary: InvoiceLoop API delays pushing M4 milestone

---

### P-240 — Product Analytics Migration
**Owner Department:** Product Management (D-130)
**Project Lead:** Dev Patel (E-011)
**Sponsor:** Anita Bose (E-010)
**Status:** In Progress
**Health:** Red (data mapping issues identified in QA)

**Objective:**
Migrate all product analytics from 3 legacy dashboard tools to a unified metrics layer — enabling consistent KPI tracking, executive reporting, and product decision-making.

**Scope:**
Covers 14 dashboards, 8 data sources, and approximately 200 KPI definitions. OrbitData Partners (V-360) provides consulting support. The project has a hard dependency on P-200 platform availability and P-250 access management.

**Key Deliverables:**
| Deliverable                        | Owner  | Status      | Target     |
|------------------------------------|--------|-------------|------------|
| Event taxonomy standardization     | E-011  | Completed   | 2025-04-01 |
| Source system mapping doc          | C-440  | In Progress | 2025-05-15 |
| Dashboard migration (14 dashboards)| E-011  | In Progress | 2025-08-01 |
| Data quality validation suite      | C-440  | In Progress | 2025-07-01 |
| Stakeholder training programme     | E-012  | Not Started | 2025-09-01 |
| Executive reporting cutover        | E-011  | Not Started | 2025-11-01 |

**Milestones:**
- M1: Event taxonomy signed off — Completed 2025-04-01
- M2: Source mapping validated — Target 2025-05-15 (currently delayed)
- M3: Dashboard migration wave 1 (6 dashboards) — Target 2025-07-01
- M4: Data quality validation complete — Target 2025-08-15
- M5: Full cutover — Target 2025-11-15

**Dependencies:**
| Depends On   | Type  | Reason                                               | Status     |
|--------------|-------|------------------------------------------------------|------------|
| P-200        | Hard  | Platform availability for analytics infrastructure   | In Progress|
| V-300        | Soft  | Analytics infrastructure support from CloudNova      | Active     |
| P-250        | Hard  | Access management for dashboard permissions          | Not Started|
| V-360        | Hard  | Consulting engagement for migration advisory         | Under Review|

**Team:**
- Dev Patel (E-011) — Lead
- Ritu Das (E-012) — Stakeholder research
- Anita Bose (E-010) — Sponsor, executive sign-off
- Mia Chen (C-440) — OrbitData analytics contractor

**Budget:**
- Approved: ₹75L
- Spent to date: ₹31L
- Forecast to complete: ₹78L (over budget by ₹3L due to scope additions)

**Key Risks:**
- R-550: Analytics data mismatch (High severity, owned by E-011)
- Secondary: V-360 (OrbitData) under review — consultant engagement at risk

---

### P-250 — Identity and Access Modernization
**Owner Department:** Engineering Platform (D-120)
**Project Lead:** Vikram Sethi (E-009)
**Sponsor:** Meera Iyer (E-003)
**Status:** Planned
**Health:** Not yet started (pending policy review from D-150)

**Objective:**
Strengthen identity, access, and permission controls across all internal systems — replacing ad-hoc access grants with policy-driven, auditable role-based controls.

**Scope:**
Covers all 18 internal employees, 5 contractors, and 7 vendor access grants. Policy review from D-150 is a mandatory pre-condition. SecureMesh (V-310) provides the IAM tooling.

**Key Deliverables:**
| Deliverable                          | Owner  | Status      | Target     |
|--------------------------------------|--------|-------------|------------|
| Access inventory and gap analysis    | E-009  | In Progress | 2025-05-15 |
| Single sign-on (SSO) upgrade         | E-009  | Not Started | 2025-07-01 |
| Role-based access policy document    | E-016  | Not Started | 2025-07-15 |
| Privileged access monitoring setup   | C-410  | Not Started | 2025-09-01 |
| Access certification workflow        | E-009  | Not Started | 2025-10-01 |
| Contractor access review and cleanup | E-009  | Not Started | 2025-11-01 |

**Milestones:**
- M1: Access inventory complete — Target 2025-05-15
- M2: Policy review from D-150 signed off — Target 2025-06-30
- M3: SSO upgrade complete — Target 2025-07-31
- M4: RBAC rollout — Target 2025-10-01
- M5: Full certification workflow live — Target 2025-12-31

**Dependencies:**
| Depends On   | Type  | Reason                                                   | Status     |
|--------------|-------|----------------------------------------------------------|------------|
| D-150        | Hard  | Policy review and approval required before RBAC rollout  | Not Started|
| V-310        | Hard  | Identity tooling (SSO, PAM) from SecureMesh              | Active     |
| P-220        | Soft  | Vendor risk approval gates should align with access certs| Planned    |

**Team:**
- Vikram Sethi (E-009) — Lead
- Farah Ali (E-016) — Policy review (D-150 representative)
- Arjun Rao (E-007) — Architecture sign-off
- Daniel Moore (C-410) — SecureMesh advisory contractor

**Budget:**
- Approved: ₹90L
- Spent to date: ₹8L (access inventory work only)
- Forecast to complete: ₹85L

**Key Risks:**
- R-540: Access misconfiguration (High severity, owned by E-009)
- R-570: Contractor access overreach (Medium severity, monitored by E-009 and E-018)

---

## 3. Cross-Project Dependency Matrix

| Project | Depends On       | Blocks                    | Description                                                          |
|---------|------------------|---------------------------|----------------------------------------------------------------------|
| P-200   | P-250 (hard)     | P-210, P-230, P-240       | Platform APIs required by 3 downstream projects                     |
| P-210   | P-200, V-320     | None                      | HR portal needs platform APIs and DocuFlow search                   |
| P-220   | P-230, V-330     | P-250 (soft)              | Vendor master data from P-230 feeds risk scoring                    |
| P-230   | P-200, V-320, V-340 | P-220                  | Procurement automation feeds vendor master data to risk             |
| P-240   | P-200, P-250     | None                      | Analytics migration needs platform + access management              |
| P-250   | D-150, V-310     | P-200 (API gateway), P-240| IAM modernization unblocks API gateway and analytics access         |

**Critical Path:**
P-250 → P-200 (API gateway) → P-240 (dashboard access)
P-230 → P-220 (vendor data)

**Cascade Risk:**
If P-200 slips beyond August 2025, both P-210 (August 15 target) and P-230 (July 31 target) will miss their deadlines.

---

## 4. Portfolio Budget Summary

| Project | Budget (₹L) | Spent (₹L) | Forecast (₹L) | Variance  |
|---------|------------|-----------|--------------|-----------|
| P-200   | 120        | 42        | 110          | -10L      |
| P-210   | 65         | 28        | 60           | -5L       |
| P-220   | 80         | 0         | 75           | -5L       |
| P-230   | 55         | 24        | 52           | -3L       |
| P-240   | 75         | 31        | 78           | +3L       |
| P-250   | 90         | 8         | 85           | -5L       |
| **Total** | **485** | **133**  | **460**      | **-25L**  |

P-240 is the only project currently over forecast. All others are within budget.

---

## 5. Project-to-Entity Cross-Reference

### Projects by Employee (Lead)
- E-007 → P-200
- E-006 → P-210
- E-017 → P-220
- E-014 → P-230
- E-011 → P-240
- E-009 → P-250

### Projects by Vendor
- V-300 (CloudNova) → P-200, P-220, P-240
- V-310 (SecureMesh) → P-250, P-240 (access)
- V-320 (DocuFlow) → P-210, P-230
- V-330 (ComplyGrid) → P-220
- V-340 (InvoiceLoop) → P-230
- V-360 (OrbitData) → P-240

### Projects by Risk
- R-500 → P-200
- R-510 → P-210
- R-520 → P-220
- R-530 → P-230
- R-540 → P-250
- R-550 → P-240
- R-560 → P-220
- R-570 → None (structural — contractor access policy)

---

## 7. Entity and Relationship Summary

The Northstar Dynamics project portfolio contains six active initiatives with a combined budget of ₹485L. Four projects are currently In Progress — P-200 (Atlas Core Platform Upgrade), P-210 (Northstar Self-Service HR Portal), P-230 (Procurement Workflow Automation), and P-240 (Product Analytics Migration) — while P-220 (Vendor Risk Monitoring Revamp) and P-250 (Identity and Access Modernization) are in Planned status.

P-200 is the most critical dependency in the portfolio. P-210, P-230, and P-240 all have hard dependencies on the platform APIs being modernised by P-200. A slip in P-200 cascades directly to three downstream projects. P-200 is led by Arjun Rao (E-007) and sponsored by CTO Meera Iyer (E-003). P-250 is also a hard dependency of P-200's API gateway stream, creating a circular dependency risk that must be managed actively.

P-240 (Product Analytics Migration) is the only project currently forecast to exceed its budget, with a ₹3L overrun projected. It also carries Red health status due to data mapping issues discovered in QA — the source mapping document from OrbitData (V-360) was delayed and contained errors, and the V-360 consulting engagement is now formally under review. All other projects are within or under their approved budgets.

V-300 (CloudNova Systems) is the vendor with the highest portfolio exposure, supporting P-200, P-220, and P-240 simultaneously. This direct exposure underpins the Critical-severity vendor concentration risk (R-520). Meera Iyer (E-003) sponsors both P-200 and P-250, giving the CTO the broadest project sponsorship footprint in the portfolio.

The critical delivery path that carries the most portfolio risk runs: P-250 must unblock P-200's API gateway stream, which in turn unblocks P-240's access management and P-210's authentication. Separately, P-230 must reach data readiness before P-220 can begin its vendor scoring model.
