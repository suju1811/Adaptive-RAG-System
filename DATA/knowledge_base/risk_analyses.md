# Risk Analyses — Northstar Dynamics

## Document Metadata

- **Document type:** Risk Analysis Register
- **Scope:** Corporate risk register with severity ratings, owners, control status, mitigations, and escalation paths.
- **Topics:** risks, likelihood/impact ratings, controls, mitigations, escalation chains, impacted projects and vendors
- **Entity types:** Risk, Employee, Project, Vendor, Department
- **ID prefixes:** R- (risks); references E-, P-, V-, D-
- **Key sections:** Risk Register, Detailed Risk Profiles
- **Cross-references:** Each risk profile links to owner (E-), impacted projects (P-), linked vendors (V-), and escalation contacts (E-)
- **Relationship hints:** owns_risk, impacts, exposes_risk, escalates_to, mitigated_by

---

## 1. Risk Register

| Risk ID | Risk Title                          | Category      | Owner ID | Linked Project | Linked Vendor | Likelihood | Impact | Severity | Control Status | Last Reviewed |
|---------|-------------------------------------|---------------|----------|----------------|---------------|------------|--------|----------|----------------|---------------|
| R-500   | Platform outage during migration    | Operational   | E-007    | P-200          | V-300         | Medium     | High   | High     | Partial        | 2025-04-10    |
| R-510   | Outdated HR policy content          | Compliance    | E-004    | P-210          | V-320         | Medium     | Medium | Medium   | Partial        | 2025-04-01    |
| R-520   | Vendor concentration risk           | Third-party   | E-017    | P-220          | V-300         | High       | High   | Critical | Weak           | 2025-04-15    |
| R-530   | Approval routing failure            | Process       | E-014    | P-230          | V-340         | Medium     | Medium | Medium   | Partial        | 2025-04-05    |
| R-540   | Access misconfiguration             | Security      | E-009    | P-250          | V-310         | Medium     | High   | High     | Strong         | 2025-04-12    |
| R-550   | Analytics data mismatch             | Data quality  | E-011    | P-240          | V-360         | Medium     | High   | High     | Partial        | 2025-04-08    |
| R-560   | Regulatory feed delay               | Compliance    | E-016    | P-220          | V-330         | Low        | High   | Medium   | Partial        | 2025-04-03    |
| R-570   | Contractor access overreach         | Security      | E-018    | None           | V-310         | Low        | High   | Medium   | Weak           | 2025-04-15    |

---

## 2. Severity Rating Scale

| Severity | Likelihood | Impact | Description                                                              |
|----------|------------|--------|--------------------------------------------------------------------------|
| Critical | High       | High   | Requires immediate executive escalation and remediation plan              |
| High     | Medium     | High   | Requires owner-led mitigation within 30 days and monthly review          |
| Medium   | Low-Medium | Medium | Tracked in register, owner review quarterly or on trigger event           |
| Low      | Low        | Low    | Monitored passively, no active remediation required                       |

---

## 3. Detailed Risk Narratives

### R-500 — Platform Outage During Migration
**Owner:** Arjun Rao (E-007)
**Severity:** High
**Category:** Operational
**Control Status:** Partial

**Description:**
A critical service disruption during the Atlas Core Platform Upgrade (P-200) would affect all dependent systems including the HR portal (P-210), procurement workflows (P-230), and analytics dashboards (P-240). The risk is highest during the service mesh cutover and CI/CD pipeline changes scheduled between June and August 2025.

**Impacted Departments:**
- Engineering Platform (D-120) — primary owner
- Product Management (D-130) — downstream analytics impact
- Human Resources (D-110) — HR portal access disruption
- Procurement & Vendor Ops (D-140) — procurement workflow downtime

**Impacted Projects:**
- P-200 (direct)
- P-210 (dependent — API outage blocks HR portal)
- P-230 (dependent — procurement authentication failure)
- P-240 (dependent — analytics infrastructure downtime)

**Triggers:**
- Incomplete rollback testing before service mesh cutover
- Deployment conflicts between service mesh upgrade and legacy service deprecation
- Infrastructure drift between staging and production environments
- Unplanned CloudNova (V-300) infrastructure changes during maintenance windows

**Mitigations:**
| Action                          | Owner  | Status      | Target Date |
|---------------------------------|--------|-------------|-------------|
| Dry-run migrations in staging   | E-007  | In Progress | 2025-05-30  |
| Rollback scripts for all services| E-007 | Not Started | 2025-06-10  |
| Change freeze during peak hours | E-008  | Completed   | Standing    |
| V-300 SLA for incident response | E-014  | Active       | Standing    |
| Blue/green deployment setup     | E-007  | Not Started | 2025-06-15  |

**Escalation Path:**
E-007 → E-003 (CTO) → E-001 (CEO) if severity upgrades to Critical
Notification required to E-010 (VP Product) and E-004 (Head of HR) if outage exceeds 2 hours.

**Notes:**
R-500 has the broadest blast radius in the portfolio. A major outage during P-200's critical path window (June–August 2025) would trigger a portfolio-level emergency response.

---

### R-510 — Outdated HR Policy Content
**Owner:** Nisha Verma (E-004)
**Severity:** Medium
**Category:** Compliance
**Control Status:** Partial

**Description:**
The HR Self-Service Portal (P-210) relies on a policy knowledge base built using DocuFlow's search index (V-320). If HR policies are updated in source systems but not reflected in the portal's indexed content, employees may receive stale guidance — creating compliance and legal exposure.

**Impacted Departments:**
- Human Resources (D-110) — primary owner
- Risk & Compliance (D-150) — compliance exposure
- All departments (employees using the portal)

**Impacted Projects:**
- P-210 (direct — policy search is a core feature)

**Triggers:**
- Policy updates in the HR policy repository not synced to DocuFlow index
- DocuFlow re-indexing failures or delays (V-320 dependency)
- Manual approval workflows delaying policy publication
- Rapid regulatory changes (employment law, leave policy) not reflected in time

**Mitigations:**
| Action                               | Owner  | Status      | Target Date |
|--------------------------------------|--------|-------------|-------------|
| DocuFlow auto-sync on policy update  | C-420  | In Progress | 2025-06-01  |
| Policy version control and audit log | E-004  | In Progress | 2025-06-15  |
| Quarterly policy review committee    | E-004  | Active       | Standing    |
| Policy expiry alerts (D-150 review)  | E-016  | Not Started | 2025-07-01  |

**Escalation Path:**
E-004 → E-001 for policies with regulatory implications
E-016 (Compliance Officer) must be notified immediately for any policy lapse in regulated domains (data protection, leave entitlements, POSH).

---

### R-520 — Vendor Concentration Risk
**Owner:** Gaurav Menon (E-017)
**Severity:** Critical
**Category:** Third-party
**Control Status:** Weak

**Description:**
CloudNova Systems (V-300) is the sole provider for cloud infrastructure, monitoring, and disaster recovery services. Three projects (P-200, P-220, P-240) have active dependencies on V-300. A V-300 service failure, commercial dispute, or contract non-renewal would simultaneously impact the platform upgrade, vendor risk monitoring, and analytics migration — causing a portfolio-level outage.

**Impacted Departments:**
- Engineering Platform (D-120)
- Risk & Compliance (D-150) — risk monitoring system dependency
- Product Management (D-130) — analytics infrastructure

**Impacted Projects:**
- P-200 (cloud infrastructure dependency)
- P-220 (risk signal ingestion dependency)
- P-240 (analytics infrastructure dependency)

**Triggers:**
- V-300 contract renewal not completed 90 days before expiry
- V-300 service degradation affecting multiple projects simultaneously
- Alternative cloud provider not qualified and approved
- CloudNova contract terms include restrictive data portability clauses

**Mitigations:**
| Action                                  | Owner  | Status      | Target Date |
|-----------------------------------------|--------|-------------|-------------|
| Secondary vendor qualification (AWS/GCP)| E-007  | Not Started | 2025-07-01  |
| Split scope between V-300 and secondary | E-013  | Not Started | 2025-08-01  |
| Contract renewal tracker in P-220       | E-014  | Not Started | 2025-07-01  |
| V-300 data portability clause review    | E-016  | Not Started | 2025-06-15  |

**Escalation Path:**
E-017 → E-018 (Head of Risk) → E-001 (CEO) for contract failure scenarios
E-002 (CFO) must be looped in for any financial exposure above ₹20L from vendor disruption.

**Notes:**
R-520 is the only Critical severity risk in the current register. It has no strong controls in place. The Vendor Risk Monitoring Revamp (P-220) is specifically designed to address this class of risk, but until P-220 is live, detection and response remain manual.

---

### R-530 — Approval Routing Failure
**Owner:** Leena Thomas (E-014)
**Severity:** Medium
**Category:** Process
**Control Status:** Partial

**Description:**
The procurement approval matrix being built in P-230 maps financial thresholds to approver roles. If the matrix does not accurately reflect current delegated authority policies (which are owned by E-002 and may change), purchase requests may be routed to incorrect approvers — causing delays, duplicate approvals, or bypassed controls.

**Impacted Departments:**
- Procurement & Vendor Ops (D-140)
- Finance (via CFO E-002)

**Impacted Projects:**
- P-230 (direct — approval matrix is a core deliverable)

**Triggers:**
- Delegated authority matrix updated by finance but not reflected in automation
- Edge cases in approval thresholds (multi-currency POs, emergency requests)
- InvoiceLoop (V-340) API failures during month-end processing
- New vendor types or procurement categories not covered in initial rule set

**Mitigations:**
| Action                                    | Owner  | Status      | Target Date |
|-------------------------------------------|--------|-------------|-------------|
| Monthly review of approval matrix vs policy| E-013 | Not Started | 2025-06-01  |
| Edge case exception workflow              | E-014  | In Progress | 2025-06-15  |
| Manual override with dual-approval fallback| E-013 | Not Started | 2025-07-01  |
| V-340 API uptime SLA enforcement          | E-015  | Active       | Standing    |

---

### R-540 — Access Misconfiguration
**Owner:** Vikram Sethi (E-009)
**Severity:** High
**Category:** Security
**Control Status:** Strong

**Description:**
During the Identity and Access Modernization (P-250), migrating from ad-hoc access grants to role-based access controls (RBAC) introduces a window where access policies may be misconfigured — granting excessive privilege or inadvertently revoking necessary access. This risk is amplified by the presence of 5 active contractors with varying access levels.

**Impacted Departments:**
- Engineering Platform (D-120) — platform access
- Procurement & Vendor Ops (D-140) — contract system access
- Risk & Compliance (D-150) — audit system access

**Impacted Projects:**
- P-250 (direct — RBAC rollout)
- P-200 (indirect — API gateway access controls)

**Triggers:**
- RBAC policy gaps identified after go-live
- Manual access exceptions granted outside the certification workflow
- Contractor access not cleaned up after engagement end dates
- SSO misconfiguration granting broad authentication bypass

**Mitigations:**
| Action                                     | Owner  | Status      | Target Date |
|--------------------------------------------|--------|-------------|-------------|
| Automated access review pre-cutover        | E-009  | In Progress | 2025-06-30  |
| Segregation of duties policy               | E-016  | Not Started | 2025-07-15  |
| Quarterly access certification workflow    | E-009  | Not Started | 2025-10-01  |
| Contractor access expiry automation        | E-009  | Not Started | 2025-08-01  |
| SecureMesh (V-310) PAM tooling             | C-410  | Active       | Standing    |

**Notes:**
Despite a Partial control status overall, R-540 has the most mature mitigation plan in the register. V-310 (SecureMesh) is actively providing PAM tooling, and E-009 has strong domain expertise. This risk is expected to downgrade from High to Medium post-P-250 launch.

---

### R-550 — Analytics Data Mismatch
**Owner:** Dev Patel (E-011)
**Severity:** High
**Category:** Data Quality
**Control Status:** Partial

**Description:**
During the Product Analytics Migration (P-240), mapping data from 8 legacy source systems to a new unified metrics layer introduces risk of schema mismatches, definition inconsistencies, and incomplete validation. Incorrect data in executive dashboards could lead to flawed strategic decisions.

**Impacted Departments:**
- Product Management (D-130) — primary
- Executive Office (D-100) — inaccurate executive reporting

**Impacted Projects:**
- P-240 (direct)

**Triggers:**
- Source system schema changes not captured in mapping document
- OrbitData (V-360) consultant Mia Chen (C-440) exits before knowledge transfer
- Dual-run reporting period cut short due to stakeholder pressure
- Legacy dashboard decommission before validation is complete

**Mitigations:**
| Action                                  | Owner  | Status      | Target Date |
|-----------------------------------------|--------|-------------|-------------|
| Data reconciliation rules engine        | C-440  | In Progress | 2025-06-30  |
| Dual-run reporting (legacy + new)       | E-011  | Not Started | 2025-08-01  |
| Dashboard approval gate (per dashboard) | E-010  | Not Started | 2025-08-15  |
| Source system change notification SLA   | E-011  | Not Started | 2025-06-01  |

**Escalation Path:**
E-011 → E-010 (VP Product) → E-001 (CEO) if executive reporting accuracy is compromised.

---

### R-560 — Regulatory Feed Delay
**Owner:** Farah Ali (E-016)
**Severity:** Medium
**Category:** Compliance
**Control Status:** Partial

**Description:**
P-220 (Vendor Risk Monitoring) relies on real-time regulatory feeds from ComplyGrid (V-330). If ComplyGrid feeds are delayed, incomplete, or cover an insufficient range of jurisdictions, the vendor risk scoring model will produce stale alerts — missing regulatory changes that should trigger vendor escalations.

**Impacted Departments:**
- Risk & Compliance (D-150)

**Impacted Projects:**
- P-220 (direct — regulatory alerts are a core feature)

**Triggers:**
- V-330 API latency or downtime
- ComplyGrid coverage gaps in India, Southeast Asia jurisdictions
- New regulatory domains not yet covered (e.g., DPDP Act amendments)

**Mitigations:**
| Action                                   | Owner  | Status      | Target Date |
|------------------------------------------|--------|-------------|-------------|
| SLA with V-330 for feed latency < 4 hours | E-016 | Active       | Standing    |
| Manual fallback review (weekly)          | E-017  | Active       | Standing    |
| Coverage gap audit for India + APAC      | E-016  | Not Started | 2025-06-30  |
| Alternative feed provider evaluation     | E-018  | Not Started | 2025-08-01  |

---

### R-570 — Contractor Access Overreach
**Owner:** Neha Kapoor (E-018)
**Severity:** Medium
**Category:** Security
**Control Status:** Weak

**Description:**
Five active contractors (C-400 through C-440) have been granted access levels commensurate with their project scope. However, as projects evolve, contractor access is rarely reviewed mid-engagement. There is a risk that contractors retain broader access than required, particularly C-400 (Elena Rossi, Platform Admin) and C-420 (Fatima Khan, Workflow Admin).

**Impacted Areas:**
- Platform administration (C-400 — CloudNova staff augmentation)
- Workflow administration (C-420 — DocuFlow implementation)
- Analytics environment (C-440 — OrbitData consulting)

**Triggers:**
- Contractor engagement extended without access review
- Project scope narrows but access level not reduced
- Contractor offboarded without timely access revocation

**Contractor Risk Profiles:**
| Contractor ID | Name            | Access Level        | Risk Level | Review Status |
|---------------|-----------------|---------------------|------------|---------------|
| C-400         | Elena Rossi     | Platform admin      | High       | Not Reviewed  |
| C-410         | Daniel Moore    | Read-only           | Low        | Current       |
| C-420         | Fatima Khan     | Workflow admin      | Medium     | Pending       |
| C-430         | Arjun Bhat      | Compliance analyst  | Low        | Current       |
| C-440         | Mia Chen        | Analytics contrib.  | Low        | Current       |

**Mitigations:**
| Action                                    | Owner  | Status      | Target Date |
|-------------------------------------------|--------|-------------|-------------|
| 60-day access review cycle for all contractors| E-009 | Not Started | 2025-05-30  |
| Contractor offboarding checklist          | E-004  | Not Started | 2025-06-01  |
| Just-in-time (JIT) access for admin tasks | E-009  | Not Started | 2025-08-01  |
| Escalation to E-018 for Platform Admin access| E-007 | Active      | Standing    |

---

## 4. Risk Heat Map Summary

```
IMPACT
High  │  R-560   R-500 R-540  R-520
      │          R-550
Med   │  R-510   R-530
      │
Low   │
      └─────────────────────────────
         Low    Medium    High    ← LIKELIHOOD
```

- **Top-right quadrant (High priority):** R-520, R-500, R-540, R-550
- **Critical (action required now):** R-520 only

---

## 5. Risk-to-Entity Cross-Reference

### By Owner
| Owner ID | Owner Name    | Risks Owned               |
|----------|---------------|---------------------------|
| E-007    | Arjun Rao     | R-500                     |
| E-004    | Nisha Verma   | R-510                     |
| E-017    | Gaurav Menon  | R-520                     |
| E-014    | Leena Thomas  | R-530                     |
| E-009    | Vikram Sethi  | R-540                     |
| E-011    | Dev Patel     | R-550                     |
| E-016    | Farah Ali     | R-560                     |
| E-018    | Neha Kapoor   | R-570                     |

### By Vendor
| Vendor ID | Vendor Name         | Linked Risks      |
|-----------|---------------------|-------------------|
| V-300     | CloudNova Systems   | R-500, R-520      |
| V-310     | SecureMesh Identity | R-540, R-570      |
| V-320     | DocuFlow Services   | R-510             |
| V-330     | ComplyGrid          | R-560             |
| V-340     | InvoiceLoop         | R-530             |
| V-360     | OrbitData Partners  | R-550             |

### By Project
| Project ID | Project Name                  | Linked Risks      |
|------------|-------------------------------|-------------------|
| P-200      | Atlas Core Platform Upgrade   | R-500             |
| P-210      | HR Portal                     | R-510             |
| P-220      | Vendor Risk Monitoring        | R-520, R-560      |
| P-230      | Procurement Automation        | R-530             |
| P-240      | Product Analytics Migration   | R-550             |
| P-250      | Identity & Access Modernization| R-540, R-570     |

---

## 6. Suggested Graph Relations

```
Risk -[owned_by]-> Employee
Risk -[impacts]-> Project
Risk -[linked_to]-> Vendor
Risk -[affects]-> Department
Risk -[mitigated_by]-> MitigationAction
Risk -[escalates_to]-> Employee
Risk -[triggered_by]-> Event
MitigationAction -[assigned_to]-> Employee
```

---

## 8. Entity and Relationship Summary

The risk register contains eight tracked risks across operational, compliance, third-party, process, security, and data quality categories. R-520 (Vendor concentration risk) is the only Critical-severity risk. It is owned by Gaurav Menon (E-017), carries Weak control status, and affects three projects simultaneously — P-200, P-220, and P-240 — through a single-vendor dependency on CloudNova Systems (V-300). The absence of a qualified secondary vendor is the root cause. R-520 has no strong mitigations in place and represents the most urgent risk action item in the register.

Two risks carry Weak control status: R-520 (owned by E-017) and R-570 (Contractor access overreach, owned by E-018). Both require active remediation rather than passive monitoring. R-570 specifically affects contractor Elena Rossi (C-400), whose Platform admin access review is currently overdue.

V-300 (CloudNova Systems) is linked to two risks — R-500 and R-520 — making it the highest-risk vendor in the register. V-310 (SecureMesh Identity) is linked to R-540 and R-570. No other vendor carries more than one direct risk linkage.

Arjun Rao (E-007) owns R-500, which has the broadest blast radius in the portfolio — a platform outage during P-200's migration window would cascade to P-210, P-230, and P-240 due to their API dependencies on P-200.

The escalation structure concentrates oversight at the top of the organisation. Neha Kapoor (E-018) owns R-570 directly and sits on the escalation path for R-520, R-540, and R-560. Meera Iyer (E-003, CTO) is the escalation point for R-500 and R-540. For any risk escalating to Critical severity, the final escalation recipient is CEO Asha Menon (E-001).
