# HR Directory — Northstar Dynamics

## Document Metadata

- **Document type:** HR Directory
- **Scope:** Organizational structure, department register, employee master list, and detailed employee profiles for Northstar Dynamics.
- **Topics:** departments, employees, roles, skills, locations, reporting hierarchy, inter-department collaboration
- **Entity types:** Employee, Department
- **ID prefixes:** E- (employees), D- (departments)
- **Key sections:** Company Overview, Department Directory, Employee Directory, Detailed Employee Profiles
- **Cross-references:** Links to projects (P-), risks (R-), and vendors (V-) by ID in employee profiles
- **Relationship hints:** reports_to, heads_department, member_of, collaborates_with

---

## 1. Company Overview

Northstar Dynamics is a mid-sized B2B technology company headquartered in Mumbai, India. The company builds enterprise software for financial services, logistics, and healthcare clients across Asia-Pacific, Europe, and North America. The organization currently employs 18 full-time staff across 6 departments and engages 5 active contractors through vendor partnerships.

---

## 2. Department Directory

| Department ID | Department Name         | Parent Department   | Primary Location | Head Employee ID | Budget Owner ID | Function                             |
|---------------|-------------------------|---------------------|------------------|------------------|-----------------|--------------------------------------|
| D-100         | Executive Office        | None                | Mumbai           | E-001            | E-001           | Corporate leadership and governance  |
| D-110         | Human Resources         | Executive Office    | Pune             | E-004            | E-002           | Hiring, payroll, policy, onboarding  |
| D-120         | Engineering Platform    | Executive Office    | Bengaluru        | E-007            | E-003           | Core platform, infrastructure, tools |
| D-130         | Product Management      | Executive Office    | Hyderabad        | E-010            | E-002           | Product strategy, roadmap, delivery  |
| D-140         | Procurement & Vendor Ops| Executive Office    | Chennai          | E-013            | E-002           | Vendor sourcing, contracts, SLAs     |
| D-150         | Risk & Compliance       | Executive Office    | Delhi            | E-018            | E-002           | Governance, audit, risk controls     |

### Department Notes
- D-120 (Engineering Platform) and D-130 (Product Management) operate as a joint delivery unit for all product releases. Engineers from D-120 are embedded in product squads led by D-130 PMs.
- D-140 (Procurement & Vendor Ops) is the mandatory approval gateway for all new vendor engagements. No vendor may be onboarded without D-140 sign-off.
- D-150 (Risk & Compliance) has cross-cutting authority. The Head of Risk & Compliance (E-018) has an escalation path directly to E-001, bypassing the CFO (E-002) for issues with regulatory severity.
- D-110 (HR) partners with D-140 for contractor onboarding — all contractor employment terms are reviewed jointly.

---

## 3. Employee Directory

| Employee ID | Employee Name   | Role                        | Department ID | Manager ID | Location   | Employment Type | Join Date  | Skills                                      |
|-------------|-----------------|------------------------------|---------------|------------|------------|-----------------|------------|---------------------------------------------|
| E-001       | Asha Menon      | Chief Executive Officer      | D-100         | None       | Mumbai     | Full-time       | 2018-04-01 | Strategy, leadership, investor relations    |
| E-002       | Rohan Kulkarni  | Chief Financial Officer      | D-100         | E-001      | Mumbai     | Full-time       | 2018-07-15 | Finance, FP&A, vendor contracts, planning   |
| E-003       | Meera Iyer      | Chief Technology Officer     | D-100         | E-001      | Bengaluru  | Full-time       | 2019-01-10 | Architecture, platform strategy, cloud ops  |
| E-004       | Nisha Verma     | Head of People Operations    | D-110         | E-001      | Pune       | Full-time       | 2019-06-01 | HR policy, talent ops, compliance liaison   |
| E-005       | Karan Shah      | HR Business Partner          | D-110         | E-004      | Pune       | Full-time       | 2020-03-15 | Hiring, employee relations, onboarding      |
| E-006       | Priya Nair      | Talent Acquisition Lead      | D-110         | E-004      | Hyderabad  | Full-time       | 2020-08-01 | Recruiting, sourcing, vendor coordination   |
| E-007       | Arjun Rao       | Director, Engineering Platform| D-120        | E-003      | Bengaluru  | Full-time       | 2019-03-01 | Kubernetes, distributed systems, SRE        |
| E-008       | Sana Ahmed      | Staff Software Engineer      | D-120         | E-007      | Bengaluru  | Full-time       | 2020-11-15 | API design, observability, Go, Python       |
| E-009       | Vikram Sethi    | Security Engineer            | D-120         | E-007      | Bengaluru  | Full-time       | 2021-02-01 | IAM, cloud security, penetration testing    |
| E-010       | Anita Bose      | VP Product                   | D-130         | E-001      | Hyderabad  | Full-time       | 2019-09-01 | Product strategy, roadmap, OKR frameworks   |
| E-011       | Dev Patel       | Product Manager              | D-130         | E-010      | Hyderabad  | Full-time       | 2021-05-10 | Requirements, stakeholder mgmt, analytics   |
| E-012       | Ritu Das        | UX Researcher                | D-130         | E-010      | Hyderabad  | Full-time       | 2021-10-01 | User research, usability testing, Figma     |
| E-013       | Imran Khan      | Head of Procurement          | D-140         | E-002      | Chennai    | Full-time       | 2020-01-15 | Supplier management, negotiation, contracts |
| E-014       | Leena Thomas    | Vendor Manager               | D-140         | E-013      | Chennai    | Full-time       | 2020-06-01 | Contracting, SLA tracking, e-procurement    |
| E-015       | Kabir Jha       | Procurement Analyst          | D-140         | E-013      | Chennai    | Full-time       | 2022-02-01 | Spend analysis, reporting, invoice ops      |
| E-016       | Farah Ali       | Compliance Officer           | D-150         | E-018      | Delhi      | Full-time       | 2020-09-01 | Audit, regulatory tracking, policy review   |
| E-017       | Gaurav Menon    | Enterprise Risk Manager      | D-150         | E-016      | Delhi      | Full-time       | 2021-07-01 | Risk registers, controls, vendor scoring    |
| E-018       | Neha Kapoor     | Head of Risk & Compliance    | D-150         | E-001      | Delhi      | Full-time       | 2019-11-01 | Governance, oversight, executive reporting  |

---

## 4. Detailed Employee Profiles

### E-001 — Asha Menon (CEO)
- **Reports to:** Board of Directors (external)
- **Direct Reports:** E-002 (CFO), E-003 (CTO), E-004 (Head of People), E-010 (VP Product), E-018 (Head of Risk)
- **Key Responsibilities:** Sets company strategy, manages investor relations, approves all major vendor contracts above ₹50L, sponsors enterprise-wide transformation programmes.
- **Cross-department touchpoints:** Sponsors P-200, P-250. Final escalation for all risk events with Critical severity.
- **Linked Projects:** P-200 (executive sponsor via CTO), P-210, P-240
- **Linked Risks:** R-500, R-520 (receives escalation)

### E-002 — Rohan Kulkarni (CFO)
- **Reports to:** E-001
- **Direct Reports:** E-013 (Head of Procurement), E-016 (Compliance Officer, dotted line)
- **Key Responsibilities:** Manages all financial planning and budget allocation. Approves vendor payments and procurement requests above threshold. Signs off on SLA-linked contracts.
- **Linked Projects:** P-230 (financial process sponsor), P-240 (budget owner)
- **Linked Vendors:** V-340 (InvoiceLoop Solutions — invoice validation), V-330 (ComplyGrid — regulatory compliance)
- **Linked Risks:** R-530 (Approval routing failure — direct impact on finance ops)

### E-003 — Meera Iyer (CTO)
- **Reports to:** E-001
- **Direct Reports:** E-007 (Director, Engineering Platform)
- **Key Responsibilities:** Owns technology strategy and platform architecture. Approves all infrastructure vendor engagements. Sponsors all Engineering Platform projects.
- **Linked Projects:** P-200 (sponsor), P-250 (sponsor)
- **Linked Vendors:** V-300 (CloudNova — cloud infra), V-310 (SecureMesh — IAM tooling)
- **Linked Risks:** R-500 (Platform outage), R-540 (Access misconfiguration)

### E-004 — Nisha Verma (Head of People Operations)
- **Reports to:** E-001
- **Direct Reports:** E-005 (HRBP), E-006 (Talent Acquisition Lead)
- **Key Responsibilities:** Owns HR policy lifecycle, manages payroll operations, oversees contractor onboarding with D-140. Policy sign-off required for all HR-facing product features.
- **Linked Projects:** P-210 (sponsor — HR portal)
- **Linked Risks:** R-510 (Outdated HR policy content — direct owner)
- **Collaboration:** Partners with E-013 (Procurement) for contractor agreements. Partners with E-018 (Risk) for HR policy compliance.

### E-005 — Karan Shah (HR Business Partner)
- **Reports to:** E-004
- **Key Responsibilities:** Acts as HR liaison for D-120 and D-130. Handles employee relations, internal grievance management, and supports hiring for technical roles.
- **Collaboration:** Regular sync with E-007 (Engineering Director) and E-010 (VP Product) for headcount planning.

### E-006 — Priya Nair (Talent Acquisition Lead)
- **Reports to:** E-004
- **Key Responsibilities:** Leads all external hiring. Manages relationship with TalentBridge (V-350) for sourcing support. Drives employer brand initiatives.
- **Linked Projects:** P-210 (project lead — HR portal)
- **Linked Vendors:** V-350 (TalentBridge Outsourcing — primary recruiting partner)
- **Contractor Oversight:** Manages contractor C-420 (Fatima Khan from DocuFlow Services)

### E-007 — Arjun Rao (Director, Engineering Platform)
- **Reports to:** E-003
- **Direct Reports:** E-008 (Staff SWE), E-009 (Security Engineer)
- **Key Responsibilities:** Owns the internal engineering platform — infrastructure, CI/CD, observability, and service reliability. All other projects that need platform APIs route through E-007's team.
- **Linked Projects:** P-200 (project lead — Atlas Core Platform Upgrade)
- **Linked Vendors:** V-300 (CloudNova — primary cloud infrastructure vendor)
- **Linked Risks:** R-500 (Platform outage — primary owner), R-520 (vendor concentration risk — impacted)
- **Contractor Oversight:** Manages contractor C-400 (Elena Rossi from CloudNova)

### E-008 — Sana Ahmed (Staff Software Engineer)
- **Reports to:** E-007
- **Key Responsibilities:** Designs and maintains internal APIs. Owns the observability stack (metrics, tracing, logging). Contributes to P-200 CI/CD hardening deliverable.
- **Linked Projects:** P-200 (contributor — observability dashboard)
- **Skills depth:** Go, Python, OpenTelemetry, Prometheus, Grafana, gRPC

### E-009 — Vikram Sethi (Security Engineer)
- **Reports to:** E-007
- **Key Responsibilities:** Owns identity and access management implementation. Leads penetration testing cycles. Partners with SecureMesh (V-310) for IAM tooling deployment.
- **Linked Projects:** P-250 (project lead — Identity and Access Modernization)
- **Linked Vendors:** V-310 (SecureMesh Identity — IAM tooling)
- **Linked Risks:** R-540 (Access misconfiguration — primary owner), R-570 (Contractor access overreach — monitoring responsibility)
- **Contractor Oversight:** Manages contractor C-410 (Daniel Moore from SecureMesh)

### E-010 — Anita Bose (VP Product)
- **Reports to:** E-001
- **Direct Reports:** E-011 (PM), E-012 (UX Researcher)
- **Key Responsibilities:** Defines and owns the product roadmap. Sets OKR frameworks for all product initiatives. Approves external research partners. Coordinates between D-130 and D-120 for delivery.
- **Linked Projects:** P-240 (sponsor — Product Analytics Migration)
- **Linked Vendors:** V-360 (OrbitData Partners — analytics consulting, currently under review)
- **Collaboration:** Frequent sync with E-007 for sprint planning. Works with E-018 for product risk review.

### E-011 — Dev Patel (Product Manager)
- **Reports to:** E-010
- **Key Responsibilities:** Manages P-240 day-to-day. Owns product requirements and stakeholder communication for analytics migration. Interfaces with OrbitData consultants.
- **Linked Projects:** P-240 (project lead)
- **Linked Vendors:** V-360 (OrbitData Partners — consulting engagement)
- **Linked Risks:** R-550 (Analytics data mismatch — primary owner)
- **Contractor Oversight:** Manages contractor C-440 (Mia Chen from OrbitData Partners)

### E-012 — Ritu Das (UX Researcher)
- **Reports to:** E-010
- **Key Responsibilities:** Leads user research for HR portal (P-210) and product analytics (P-240). Conducts usability testing and synthesizes findings for PM and design teams.
- **Linked Projects:** P-210 (research contributor), P-240 (research contributor)
- **Collaboration:** Works with E-006 (Talent Acquisition) for user interview sourcing. Coordinates with E-014 for DocuFlow usability testing.

### E-013 — Imran Khan (Head of Procurement)
- **Reports to:** E-002
- **Direct Reports:** E-014 (Vendor Manager), E-015 (Procurement Analyst)
- **Key Responsibilities:** Owns the full vendor lifecycle — from onboarding to contract renewals to off-boarding. All new vendor requests above ₹5L annual value require E-013 sign-off. Leads contract negotiation for high-criticality vendors.
- **Linked Projects:** P-230 (sponsor — Procurement Workflow Automation)
- **Linked Vendors:** V-320 (DocuFlow), V-340 (InvoiceLoop)
- **Linked Risks:** R-530 (Approval routing failure — direct impact on team)

### E-014 — Leena Thomas (Vendor Manager)
- **Reports to:** E-013
- **Key Responsibilities:** Day-to-day contract management for V-320 and V-340. Tracks SLA performance, manages renewal timelines, coordinates e-signature workflows with DocuFlow.
- **Linked Projects:** P-230 (project lead — Procurement Workflow Automation)
- **Linked Vendors:** V-320 (DocuFlow Services — primary), V-340 (InvoiceLoop Solutions)
- **Contractor Oversight:** Manages contractor C-420 (Fatima Khan from DocuFlow Services)

### E-015 — Kabir Jha (Procurement Analyst)
- **Reports to:** E-013
- **Key Responsibilities:** Produces spend analysis reports, tracks purchase orders, monitors invoice reconciliation. Flags anomalies to E-013 and E-002. Manages operational relationship with InvoiceLoop (V-340).
- **Linked Vendors:** V-340 (InvoiceLoop Solutions — primary contact)
- **Linked Risks:** R-530 (contributes to reconciliation data quality)

### E-016 — Farah Ali (Compliance Officer)
- **Reports to:** E-018
- **Direct Reports:** E-017 (Enterprise Risk Manager)
- **Key Responsibilities:** Owns audit readiness, manages regulatory change tracking, reviews policy documents for compliance gaps. Primary owner of ComplyGrid (V-330) relationship.
- **Linked Projects:** P-220 (compliance feed contributor)
- **Linked Vendors:** V-330 (ComplyGrid Intelligence — regulatory feeds)
- **Linked Risks:** R-560 (Regulatory feed delay — owner), R-570 (Contractor access overreach — audit responsibility)
- **Contractor Oversight:** Manages contractor C-430 (Arjun Bhat from ComplyGrid)

### E-017 — Gaurav Menon (Enterprise Risk Manager)
- **Reports to:** E-016
- **Key Responsibilities:** Maintains the risk register. Builds and maintains vendor risk scoring models. Produces risk dashboards for executive review. Leads the Vendor Risk Monitoring Revamp (P-220).
- **Linked Projects:** P-220 (project lead)
- **Linked Risks:** R-520 (Vendor concentration risk — primary owner), R-500 (contributes to risk register)
- **Linked Vendors:** V-300 (CloudNova — risk concentration monitoring), V-330 (ComplyGrid — data source)

### E-018 — Neha Kapoor (Head of Risk & Compliance)
- **Reports to:** E-001
- **Direct Reports:** E-016 (Compliance Officer)
- **Key Responsibilities:** Owns governance framework. Reports directly to CEO on critical risk events. Approves all vendor risk assessments. Reviews project risk profiles before major launches.
- **Linked Projects:** P-220 (sponsor), P-250 (policy review approver)
- **Linked Risks:** R-520 (receives escalation), R-570 (Contractor access overreach — ultimate owner)
- **Collaboration:** Works with E-004 (HR) on contractor compliance. Works with E-003 (CTO) on technology risk approvals.

---

## 5. Reporting Chain Summary

```
E-001 (CEO — Asha Menon)
├── E-002 (CFO — Rohan Kulkarni)
│   ├── E-013 (Head of Procurement — Imran Khan)
│   │   ├── E-014 (Vendor Manager — Leena Thomas)
│   │   └── E-015 (Procurement Analyst — Kabir Jha)
│   └── E-016 (Compliance Officer — Farah Ali) [dotted line to E-018]
│       └── E-017 (Enterprise Risk Manager — Gaurav Menon)
├── E-003 (CTO — Meera Iyer)
│   └── E-007 (Director, Engineering — Arjun Rao)
│       ├── E-008 (Staff SWE — Sana Ahmed)
│       └── E-009 (Security Engineer — Vikram Sethi)
├── E-004 (Head of People — Nisha Verma)
│   ├── E-005 (HRBP — Karan Shah)
│   └── E-006 (Talent Acquisition — Priya Nair)
├── E-010 (VP Product — Anita Bose)
│   ├── E-011 (PM — Dev Patel)
│   └── E-012 (UX Researcher — Ritu Das)
└── E-018 (Head of Risk — Neha Kapoor)
    └── E-016 (Compliance Officer — Farah Ali)
        └── E-017 (Enterprise Risk Manager — Gaurav Menon)
```

---

## 6. Cross-Department Collaboration Map

| From Department | To Department           | Collaboration Type                          | Key Contacts           |
|-----------------|-------------------------|---------------------------------------------|------------------------|
| D-120           | D-130                   | Joint product delivery, embedded engineers  | E-007 ↔ E-010          |
| D-110           | D-140                   | Contractor onboarding agreements            | E-004 ↔ E-013          |
| D-140           | D-150                   | Vendor risk assessments, scoring reviews    | E-014 ↔ E-017          |
| D-150           | D-120                   | Policy review for P-250 access controls     | E-016 ↔ E-009          |
| D-130           | D-150                   | Product risk review before launch           | E-010 ↔ E-018          |
| D-110           | D-150                   | HR policy compliance sign-off               | E-004 ↔ E-016          |
| D-140           | D-130                   | Vendor capability evaluation for products  | E-013 ↔ E-011          |

---

## 7. Skills Inventory

| Skill Domain       | Employees                         | Relevant Vendors         |
|--------------------|-----------------------------------|--------------------------|
| Cloud infrastructure| E-007, E-008                     | V-300 (CloudNova)        |
| IAM / Security     | E-009                             | V-310 (SecureMesh)       |
| HR Policy & Ops    | E-004, E-005, E-006               | V-350 (TalentBridge)     |
| Vendor & Contracts | E-013, E-014, E-015               | V-320 (DocuFlow), V-340  |
| Risk & Compliance  | E-016, E-017, E-018               | V-330 (ComplyGrid)       |
| Product & Analytics| E-010, E-011, E-012               | V-360 (OrbitData)        |
| Finance & FP&A     | E-002                             | V-340 (InvoiceLoop)      |

---

## 8. Entity Relationship Summary (for Graph Extraction)

```
# Reporting relationships
E-001 -[reports_to]-> Board
E-002 -[reports_to]-> E-001
E-003 -[reports_to]-> E-001
E-004 -[reports_to]-> E-001
E-010 -[reports_to]-> E-001
E-018 -[reports_to]-> E-001
E-007 -[reports_to]-> E-003
E-008 -[reports_to]-> E-007
E-009 -[reports_to]-> E-007
E-005 -[reports_to]-> E-004
E-006 -[reports_to]-> E-004
E-013 -[reports_to]-> E-002
E-014 -[reports_to]-> E-013
E-015 -[reports_to]-> E-013
E-016 -[reports_to]-> E-018
E-017 -[reports_to]-> E-016
E-011 -[reports_to]-> E-010
E-012 -[reports_to]-> E-010

# Department membership
E-001, E-002, E-003 -[member_of]-> D-100
E-004, E-005, E-006 -[member_of]-> D-110
E-007, E-008, E-009 -[member_of]-> D-120
E-010, E-011, E-012 -[member_of]-> D-130
E-013, E-014, E-015 -[member_of]-> D-140
E-016, E-017, E-018 -[member_of]-> D-150

# Project ownership (see project_reports.md for full details)
E-007 -[leads]-> P-200
E-006 -[leads]-> P-210
E-017 -[leads]-> P-220
E-014 -[leads]-> P-230
E-011 -[leads]-> P-240
E-009 -[leads]-> P-250

# Vendor account ownership (see vendor_contractor.md for full details)
E-007 -[owns_vendor]-> V-300
E-009 -[owns_vendor]-> V-310
E-014 -[owns_vendor]-> V-320
E-016 -[owns_vendor]-> V-330
E-015 -[owns_vendor]-> V-340
E-006 -[owns_vendor]-> V-350
E-011 -[owns_vendor]-> V-360
```

---

## 9. Entity and Relationship Summary

Northstar Dynamics has 18 full-time employees across 6 departments, all reporting ultimately to CEO Asha Menon (E-001). The Executive Office (D-100) holds the three C-suite leaders: Asha Menon (CEO), Rohan Kulkarni (CFO, E-002), and Meera Iyer (CTO, E-003). The CEO's five direct reports are Rohan Kulkarni (E-002), Meera Iyer (E-003), Nisha Verma (E-004), Anita Bose (E-010), and Neha Kapoor (E-018).

Engineering Platform (D-120) is led by Arjun Rao (E-007), who reports to CTO Meera Iyer (E-003). The team covers Kubernetes, distributed systems, SRE, API design, observability (Go, Python, OpenTelemetry), IAM, and cloud security. Sana Ahmed (E-008) owns the observability stack and internal APIs; Vikram Sethi (E-009) owns identity, access management, and contractor access reviews, including the SecureMesh (V-310) relationship.

Risk & Compliance (D-150) is based in Delhi and led by Neha Kapoor (E-018), who reports directly to the CEO. Farah Ali (E-016) serves as Compliance Officer under E-018, and Gaurav Menon (E-017) reports to E-016 as Enterprise Risk Manager. All three Delhi-based employees — Farah Ali, Gaurav Menon, and Neha Kapoor — belong to D-150.

Procurement & Vendor Ops (D-140) is the mandatory approval gateway for all vendor onboarding — no vendor may be contracted without D-140 sign-off. It is led by Imran Khan (E-013), reporting to CFO Rohan Kulkarni (E-002), with Leena Thomas (E-014) as Vendor Manager and Kabir Jha (E-015) as Procurement Analyst.

Risk ownership is distributed by domain: E-007 owns R-500, E-004 owns R-510, E-017 owns R-520, E-014 owns R-530, E-009 owns R-540, E-011 owns R-550, E-016 owns R-560, and E-018 owns R-570. Neha Kapoor (E-018) also sits on the escalation path for R-520, R-540, and R-560. Meera Iyer (E-003) is the escalation point for both R-500 and R-540.
