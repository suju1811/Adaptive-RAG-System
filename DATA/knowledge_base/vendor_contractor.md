# Vendor and Contractor Register — Northstar Dynamics

## Document Metadata

- **Document type:** Vendor and Contractor Register
- **Scope:** Vendor master list, contract details, SLA notes, contractor assignments, and links to projects, employees, and risks.
- **Topics:** vendors, contractors, contracts, SLAs, access levels, renewal dates, criticality
- **Entity types:** Vendor, Contractor, Employee, Project
- **ID prefixes:** V- (vendors), C- (contractors); references E-, P-, R-
- **Key sections:** Vendor Master, Contractor Register, Vendor Profiles, Contractor Profiles
- **Cross-references:** Vendors link to account owners (E-), supported projects (P-), and exposed risks (R-); contractors link to manager (E-), employer vendor (V-), and assigned projects (P-)
- **Relationship hints:** owns_vendor, works_for, managed_by, works_on, uses_vendor, exposes_risk

---

## 1. Vendor Master

| Vendor ID | Vendor Name              | Category    | Service Type                     | Account Owner ID | Contract Status | Region         | Criticality | Annual Value (₹L) | Contract Expiry |
|-----------|--------------------------|-------------|----------------------------------|------------------|-----------------|----------------|-------------|-------------------|-----------------|
| V-300     | CloudNova Systems        | Technology  | Cloud infrastructure + monitoring| E-007            | Active          | Global         | High        | 85                | 2026-03-31      |
| V-310     | SecureMesh Identity      | Technology  | IAM tooling + PAM                | E-009            | Active          | North America  | High        | 42                | 2025-12-31      |
| V-320     | DocuFlow Services        | Technology  | Document workflow + search       | E-014            | Active          | Europe         | Medium      | 28                | 2026-01-31      |
| V-330     | ComplyGrid Intelligence  | Technology  | Regulatory and compliance feeds  | E-016            | Active          | Global         | High        | 36                | 2026-06-30      |
| V-340     | InvoiceLoop Solutions    | Operations  | Invoice validation + PO matching | E-015            | Active          | Asia-Pacific   | Medium      | 18                | 2025-10-31      |
| V-350     | TalentBridge Outsourcing | Services    | Recruiting support               | E-006            | Active          | India          | Medium      | 22                | 2025-09-30      |
| V-360     | OrbitData Partners       | Services    | Analytics consulting             | E-011            | Under Review    | Global         | Medium      | 30                | 2025-10-10      |

**Total active vendor spend:** ₹261L/year (7 vendors)
**Under review:** V-360 (OrbitData Partners) — review triggered by deliverable quality concerns in P-240.

---

## 2. Contractor Register

| Contractor ID | Contractor Name | Working For              | Account Manager ID | Engagement Type        | Start Date | End Date   | Access Level    | Status | Daily Rate (₹) |
|---------------|-----------------|--------------------------|---------------------|------------------------|------------|------------|-----------------|--------|----------------|
| C-400         | Elena Rossi     | CloudNova Systems (V-300)| E-007               | Staff augmentation     | 2025-02-01 | 2025-08-31 | Platform admin  | Active | 12,000         |
| C-410         | Daniel Moore    | SecureMesh Identity (V-310)| E-009             | Advisory               | 2025-03-15 | 2025-09-15 | Read-only       | Active | 18,000         |
| C-420         | Fatima Khan     | DocuFlow Services (V-320) | E-014              | Implementation         | 2025-01-20 | 2025-07-20 | Workflow admin  | Active | 10,000         |
| C-430         | Arjun Bhat      | ComplyGrid Intelligence (V-330)| E-016         | Support                | 2025-04-01 | 2025-12-31 | Compliance analyst| Active| 8,500         |
| C-440         | Mia Chen        | OrbitData Partners (V-360)| E-011              | Consulting             | 2025-02-10 | 2025-10-10 | Analytics contrib.| Active| 15,000        |

**Total contractor headcount:** 5 active
**Contractor cost (estimated, FY2025):** ₹63L (across all engagements)

---

## 3. Vendor Detailed Profiles

### V-300 — CloudNova Systems
**Account Owner:** Arjun Rao (E-007)
**Category:** Technology — Cloud Infrastructure
**Contract Status:** Active
**Contract Expiry:** 2026-03-31
**Annual Value:** ₹85L
**Region:** Global
**Criticality:** High

**Services Provided:**
- Cloud hosting (multi-region: Mumbai, Singapore, Frankfurt)
- Real-time monitoring and alerting (used by P-200 observability stack)
- Disaster recovery and backup services
- Infra-as-code tooling (Terraform modules)
- Technical support SLA: P1 response within 2 hours

**Connected Projects:**
| Project ID | Project Name                    | Nature of Dependency                                      |
|------------|---------------------------------|-----------------------------------------------------------|
| P-200      | Atlas Core Platform Upgrade     | Cloud hosting + monitoring; DR support during migration   |
| P-220      | Vendor Risk Monitoring Revamp   | Risk signal ingestion from CloudNova monitoring APIs      |
| P-240      | Product Analytics Migration     | Analytics infrastructure hosting and scaling              |

**Active Contractors:**
- C-400 Elena Rossi — staff augmentation for P-200 infrastructure work

**Associated Risks:**
| Risk ID | Risk Title                    | Severity | Relationship                                        |
|---------|-------------------------------|----------|-----------------------------------------------------|
| R-500   | Platform outage during migration| High   | CloudNova infra failure triggers outage risk         |
| R-520   | Vendor concentration risk     | Critical | 3 critical projects concentrated on single vendor   |

**Contract Notes:**
- Renewal due 2026-03-31. E-007 and E-013 must initiate renewal negotiation by 2025-12-31.
- Current contract includes a 90-day data portability window on termination — legal review pending (flagged by E-016 under R-520 mitigations).
- V-300 is the subject of a secondary vendor qualification initiative to reduce concentration risk.

**SLA Performance (last 6 months):**
| Month    | P1 Incidents | Avg Resolution | SLA Met |
|----------|-------------|----------------|---------|
| Nov 2024 | 1           | 1.8h           | Yes     |
| Dec 2024 | 0           | —              | Yes     |
| Jan 2025 | 2           | 3.1h           | No      |
| Feb 2025 | 1           | 1.5h           | Yes     |
| Mar 2025 | 0           | —              | Yes     |
| Apr 2025 | 1           | 2.2h           | No      |

---

### V-310 — SecureMesh Identity
**Account Owner:** Vikram Sethi (E-009)
**Category:** Technology — IAM and Security
**Contract Status:** Active
**Contract Expiry:** 2025-12-31
**Annual Value:** ₹42L
**Region:** North America
**Criticality:** High

**Services Provided:**
- Identity and Access Management (IAM) platform
- Privileged Access Management (PAM) tooling
- Single Sign-On (SSO) policy enforcement and federation
- Role-based access control (RBAC) templates and audit trails
- Security advisory — contractor Daniel Moore (C-410) embedded

**Connected Projects:**
| Project ID | Project Name                          | Nature of Dependency                              |
|------------|---------------------------------------|---------------------------------------------------|
| P-250      | Identity and Access Modernization     | Core tooling provider for SSO, RBAC, and PAM      |
| P-240      | Product Analytics Migration           | Access management for dashboard permissions       |

**Active Contractors:**
- C-410 Daniel Moore — SecureMesh advisory, embedded in P-250 team

**Associated Risks:**
| Risk ID | Risk Title                    | Severity | Relationship                                          |
|---------|-------------------------------|----------|-------------------------------------------------------|
| R-540   | Access misconfiguration       | High     | RBAC policy gaps introduced during SecureMesh rollout |
| R-570   | Contractor access overreach   | Medium   | SecureMesh PAM tooling used to monitor contractor access|

**Contract Notes:**
- Contract expires 2025-12-31 — renewal decision required by September 2025.
- Vendor lock-in concern: SecureMesh SSO federation makes migration to alternative provider a 6-month effort.
- E-009 has flagged vendor lock-in risk to E-003 (CTO) — alternative evaluation deferred to post-P-250 launch.

**SLA Performance (last 6 months):**
All SLAs met. No P1 incidents. One P2 ticket (SSO federation delay, Jan 2025) resolved within 4 hours.

---

### V-320 — DocuFlow Services
**Account Owner:** Leena Thomas (E-014)
**Category:** Technology — Document Management
**Contract Status:** Active
**Contract Expiry:** 2026-01-31
**Annual Value:** ₹28L
**Region:** Europe (GDPR compliant)
**Criticality:** Medium

**Services Provided:**
- Document workflow automation (intake, routing, approval)
- Search indexing and retrieval for document repositories
- E-signature integration (DocuSign-compatible API)
- Template management and version control

**Connected Projects:**
| Project ID | Project Name                    | Nature of Dependency                                    |
|------------|---------------------------------|---------------------------------------------------------|
| P-210      | Northstar Self-Service HR Portal| Policy knowledge search and document indexing           |
| P-230      | Procurement Workflow Automation | E-signature integration for contract routing            |

**Active Contractors:**
- C-420 Fatima Khan — implementation contractor for P-210 and P-230 integrations

**Associated Risks:**
| Risk ID | Risk Title                     | Severity | Relationship                                    |
|---------|--------------------------------|----------|-------------------------------------------------|
| R-510   | Outdated HR policy content     | Medium   | DocuFlow re-indexing failure may expose stale policies |

**Contract Notes:**
- Renewal due 2026-01-31. E-014 to initiate by 2025-10-01.
- Contract covers GDPR data residency in EU. No India data residency clause — flagged by E-016 under DPDP Act review.

---

### V-330 — ComplyGrid Intelligence
**Account Owner:** Farah Ali (E-016)
**Category:** Technology — Regulatory Compliance
**Contract Status:** Active
**Contract Expiry:** 2026-06-30
**Annual Value:** ₹36L
**Region:** Global
**Criticality:** High

**Services Provided:**
- Real-time regulatory and compliance feed APIs
- Jurisdiction-specific rule change notifications
- Alert enrichment with risk scoring weights
- Custom taxonomy mapping for vendor classification

**Connected Projects:**
| Project ID | Project Name                    | Nature of Dependency                                    |
|------------|---------------------------------|---------------------------------------------------------|
| P-220      | Vendor Risk Monitoring Revamp   | Primary data source for regulatory alerts and scoring  |

**Active Contractors:**
- C-430 Arjun Bhat — ComplyGrid support contractor for P-220 integration

**Associated Risks:**
| Risk ID | Risk Title               | Severity | Relationship                                    |
|---------|--------------------------|----------|-------------------------------------------------|
| R-560   | Regulatory feed delay    | Medium   | V-330 latency directly impacts P-220 alert quality |

**Contract Notes:**
- Coverage includes EU, North America, and major APAC jurisdictions. India-specific DPDP coverage is limited — E-016 has requested an expansion proposal from ComplyGrid.
- Renewal not due until June 2026 — low urgency.

---

### V-340 — InvoiceLoop Solutions
**Account Owner:** Kabir Jha (E-015)
**Category:** Operations — Finance Automation
**Contract Status:** Active
**Contract Expiry:** 2025-10-31
**Annual Value:** ₹18L
**Region:** Asia-Pacific
**Criticality:** Medium

**Services Provided:**
- Invoice validation and 3-way PO matching
- Payment exception handling
- Duplicate invoice detection
- API integration with procurement systems

**Connected Projects:**
| Project ID | Project Name                    | Nature of Dependency                              |
|------------|---------------------------------|---------------------------------------------------|
| P-230      | Procurement Workflow Automation | Invoice validation API for month-end processing   |

**Associated Risks:**
| Risk ID | Risk Title               | Severity | Relationship                                    |
|---------|--------------------------|----------|-------------------------------------------------|
| R-530   | Approval routing failure | Medium   | InvoiceLoop API failures disrupt invoice matching|

**Contract Notes:**
- Contract expires 2025-10-31. Renewal decision required by August 2025.
- P-230 integration is currently delayed (see project risk log) — InvoiceLoop API documentation was incomplete, requiring additional development effort.
- E-015 has flagged a potential switch to a competitor (InvoTrack) if integration issues are not resolved by June 2025.

**SLA Performance (last 3 months):**
| Month    | API Uptime | Incidents | Notes                         |
|----------|-----------|-----------|-------------------------------|
| Feb 2025 | 98.4%     | 1         | Month-end batch delay (4h)    |
| Mar 2025 | 99.8%     | 0         | —                             |
| Apr 2025 | 97.1%     | 2         | Duplicate detection miss x2   |

---

### V-350 — TalentBridge Outsourcing
**Account Owner:** Priya Nair (E-006)
**Category:** Services — Talent Acquisition
**Contract Status:** Active
**Contract Expiry:** 2025-09-30
**Annual Value:** ₹22L
**Region:** India
**Criticality:** Medium

**Services Provided:**
- Candidate sourcing support for technical and non-technical roles
- Interview coordination and scheduling
- Candidate outreach campaigns
- Employer brand content (job descriptions, social posts)

**Connected Projects:**
| Project ID | Project Name                    | Nature of Dependency                                    |
|------------|---------------------------------|---------------------------------------------------------|
| P-210      | Northstar Self-Service HR Portal| Talent data scope — sourcing pipeline feeds into HR portal|

**Associated Risks:**
- No formal risk register entry, but E-006 has flagged informally:
  - Candidate pipeline inconsistency during peak hiring (Q2 and Q4)
  - Data privacy concerns — TalentBridge handles PII for candidates not yet employees (DPDP Act implications)
  - SLA misses during high-volume hiring — requires escalation to E-013 for penalty enforcement

**Contract Notes:**
- Renewal due 2025-09-30. E-006 and E-013 reviewing whether to renew or bring sourcing in-house.
- Data Processing Agreement (DPA) with TalentBridge under review for DPDP Act compliance — flagged by E-016.

---

### V-360 — OrbitData Partners
**Account Owner:** Dev Patel (E-011)
**Category:** Services — Analytics Consulting
**Contract Status:** Under Review
**Contract Expiry:** 2025-10-10
**Annual Value:** ₹30L
**Region:** Global
**Criticality:** Medium

**Services Provided:**
- Analytics consulting and data modeling advisory
- Dashboard migration support (legacy → unified metrics layer)
- Event taxonomy design
- Data quality framework design

**Connected Projects:**
| Project ID | Project Name                    | Nature of Dependency                              |
|------------|---------------------------------|---------------------------------------------------|
| P-240      | Product Analytics Migration     | Core consulting partner for migration advisory    |

**Active Contractors:**
- C-440 Mia Chen — analytics contributor embedded in P-240 team

**Under Review Reason:**
E-011 has flagged deliverable quality concerns — source mapping document was submitted 3 weeks late and contained mapping errors that contributed to P-240's Red health status. E-010 (VP Product) has initiated a formal contract performance review. Options being considered:
1. Continue with remediation plan and enhanced quality gates
2. Partially offboard (retain Mia Chen, terminate broader engagement)
3. Full termination and transfer of knowledge to internal team

**Associated Risks:**
| Risk ID | Risk Title               | Severity | Relationship                                    |
|---------|--------------------------|----------|-------------------------------------------------|
| R-550   | Analytics data mismatch  | High     | Mapping errors from OrbitData triggered P-240 Red status|

**Contract Notes:**
- OrbitData holds a 30-day notice clause. If full termination is selected, knowledge transfer must begin immediately to avoid P-240 delay.
- Mia Chen (C-440) engagement can be extended independently of the V-360 contract — E-011 is exploring this option.

---

## 4. Contract Renewal Tracker

| Vendor ID | Vendor Name              | Expiry Date  | Renewal Start  | Owner  | Status       | Risk if Not Renewed                              |
|-----------|--------------------------|--------------|----------------|--------|--------------|--------------------------------------------------|
| V-350     | TalentBridge Outsourcing | 2025-09-30   | 2025-07-01     | E-006  | Not Started  | Hiring pipeline disruption                       |
| V-340     | InvoiceLoop Solutions    | 2025-10-31   | 2025-08-01     | E-015  | Not Started  | P-230 invoice module at risk                     |
| V-360     | OrbitData Partners       | 2025-10-10   | Under review   | E-011  | Under Review | P-240 consulting dependency                      |
| V-310     | SecureMesh Identity      | 2025-12-31   | 2025-09-01     | E-009  | Not Started  | P-250 IAM tooling — 6-month migration lock-in    |
| V-320     | DocuFlow Services        | 2026-01-31   | 2025-10-01     | E-014  | Not Started  | P-210 and P-230 document workflows at risk       |
| V-300     | CloudNova Systems        | 2026-03-31   | 2025-12-31     | E-007  | Not Started  | Platform outage risk — highest renewal priority  |
| V-330     | ComplyGrid Intelligence  | 2026-06-30   | 2026-03-01     | E-016  | Not Started  | Regulatory feed for P-220 risk monitoring        |

**Most urgent renewal:** V-340 (InvoiceLoop) — integration delays make this a priority for Q3 2025 decision.
**Highest risk renewal:** V-300 (CloudNova) — concentration risk (R-520) means renewal negotiation must include secondary vendor qualification conversation.

---

## 5. Contractor Access Review Summary

| Contractor ID | Name          | Access Level        | Manager | End Date   | Access Review Due | Risk Level |
|---------------|---------------|---------------------|---------|------------|-------------------|------------|
| C-400         | Elena Rossi   | Platform admin      | E-007   | 2025-08-31 | Overdue           | High       |
| C-410         | Daniel Moore  | Read-only           | E-009   | 2025-09-15 | 2025-06-15        | Low        |
| C-420         | Fatima Khan   | Workflow admin      | E-014   | 2025-07-20 | 2025-05-20        | Medium     |
| C-430         | Arjun Bhat    | Compliance analyst  | E-016   | 2025-12-31 | 2025-06-01        | Low        |
| C-440         | Mia Chen      | Analytics contrib.  | E-011   | 2025-10-10 | 2025-07-10        | Low        |

**Overdue review:** C-400 (Elena Rossi) — Platform admin access has not been reviewed since engagement start. E-007 notified. Risk escalated to E-018 per R-570 mitigation plan.

---

## 6. Vendor-to-Entity Cross-Reference

### By Project Involvement
| Vendor | Projects Supported              | Count |
|--------|---------------------------------|-------|
| V-300  | P-200, P-220, P-240             | 3     |
| V-310  | P-250, P-240                    | 2     |
| V-320  | P-210, P-230                    | 2     |
| V-330  | P-220                           | 1     |
| V-340  | P-230                           | 1     |
| V-350  | P-210                           | 1     |
| V-360  | P-240                           | 1     |

### By Risk Exposure
| Vendor | Risks Linked    | Highest Severity |
|--------|-----------------|------------------|
| V-300  | R-500, R-520    | Critical         |
| V-310  | R-540, R-570    | High             |
| V-320  | R-510           | Medium           |
| V-330  | R-560           | Medium           |
| V-340  | R-530           | Medium           |
| V-350  | (informal only) | Low              |
| V-360  | R-550           | High             |

---

## 7. Suggested Graph Relations

```
Vendor -[owned_by]-> Employee
Vendor -[supports]-> Project
Vendor -[exposes_risk]-> Risk
Vendor -[has_contract_expiry]-> Date
Contractor -[works_for]-> Vendor
Contractor -[assigned_to]-> Employee (manager)
Contractor -[has_access]-> AccessLevel
Contractor -[works_on]-> Project
Department -[manages_vendor]-> Vendor
```

---

## 9. Entity and Relationship Summary

Northstar Dynamics maintains seven vendor relationships with a combined annual spend of ₹261L. V-300 (CloudNova Systems) is the largest at ₹85L per year and the most critically exposed vendor, supporting three projects simultaneously (P-200, P-220, P-240). V-310 (SecureMesh Identity) follows at ₹42L and is the sole IAM tooling provider for P-250. V-360 (OrbitData Partners) is currently Under Review following deliverable quality concerns on P-240.

Four vendor contracts expire before the end of 2025: V-350 (TalentBridge Outsourcing, September 2025), V-340 (InvoiceLoop Solutions, October 2025), V-360 (OrbitData Partners, October 2025 — under review), and V-310 (SecureMesh Identity, December 2025). The most urgent renewal decision is V-340 — InvoiceLoop's API integration with P-230 is already delayed, making the October 2025 expiry a near-term risk to the Procurement Automation project.

Arjun Rao (E-007) owns the CloudNova (V-300) relationship and must initiate renewal negotiation by December 2025. The V-300 contract includes a 90-day data portability window on termination — a clause under legal review given the concentration risk (R-520). Elena Rossi (C-400), a CloudNova staff augmentation contractor with Platform admin access, is currently embedded on P-200. Her access review is overdue and has been escalated to Neha Kapoor (E-018) per the R-570 mitigation plan.

Two vendors specifically support procurement operations: V-320 (DocuFlow Services) for e-signature and document workflow, and V-340 (InvoiceLoop Solutions) for invoice validation and PO matching — both integrated into P-230. OrbitData Partners (V-360) came under formal contract performance review after the source mapping document for P-240 was submitted three weeks late and contained mapping errors that directly caused P-240's Red health rating. VP Product Anita Bose (E-010) initiated the review.
