# Northstar Dynamics — Corporate Knowledge Base

## About

Internal corporate documents for **Northstar Dynamics**, a mid-sized B2B technology company based in Mumbai. The company builds enterprise software for financial services, logistics, and healthcare clients.

These files power the **Corporate Intelligence System (CIS)** — staff ask natural-language questions about employees, projects, vendors, contractors, and operational risks. Records use stable IDs (`E-007`, `P-200`, `V-300`, `R-520`, etc.) and cross-reference each other across files.

Synthetic research dataset, version 2.0.

---

## How CIS Ingests This Folder

CIS does not require pipeline settings in this README. During ingest it combines:

1. **This README** — domain context, file inventory, and example questions
2. **Per-file metadata** — optional `## Document Metadata` block at the top of each `.md` file (see any data file for the convention)
3. **Automatic sampling** — heading outline and content excerpts extracted from each file to infer structure and chunking strategy

---

## Documents

| File | Description |
|------|-------------|
| `hr_directory.md` | Org structure, departments, employee register, and employee profiles |
| `project_reports.md` | Project portfolio, budgets, deliverables, dependencies, and team assignments |
| `risk_analyses.md` | Risk register, severity ratings, controls, mitigations, and escalation paths |
| `vendor_contractor.md` | Vendor contracts, contractor assignments, SLAs, and project links |

All files are Markdown (`.md`), English.

---

## Domain

**Industry:** B2B enterprise software  
**Scale:** ~18 employees, 6 departments, 6 projects, 7 vendors, 5 contractors, 8 tracked risks  
**Areas:** HR, engineering, product, procurement, risk & compliance  

The same person or project often appears in multiple files (e.g. an employee as a profile in HR, a project lead in project reports, and a vendor owner in vendor files).

---

## Example Questions

- Who leads the Engineering Platform department?
- What is the budget and status of project P-240?
- Which employees are based in Delhi?
- When does the CloudNova contract expire, and who owns that vendor?
- What risks are rated Critical, and who owns them?
- Which projects depend on other projects, and what vendors do they use?
- Which contractors have admin-level access, and who manages them?
- Which employees work on projects with Critical risks?
- Summarize the risks linked to P-200 and their mitigation status.
- Which vendor renewals are due in the next six months?

---

## Usage Notes

- **Audience:** HR, engineering leadership, procurement, risk/compliance, executives
- **Scope:** Internal operations data — not customer-facing product docs
- **Answer style:** Professional and factual; cite source documents; use entity IDs alongside names when helpful
- **Optional metadata:** Add or update the `## Document Metadata` section when creating new files in this folder
