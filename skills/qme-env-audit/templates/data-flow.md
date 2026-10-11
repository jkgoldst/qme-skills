# Current-State Data Flow

Use this template after the interview. Replace placeholders with actual systems and evidence labels. Draw each current-state edge only when an evidence ID establishes both endpoints and the action; label the edge VERIFIED or REPORTED with that ID. Record hypothetical or UNKNOWN paths separately from the diagram. Retain the granularity actually supplied: a notification renderer does not establish a worker architecture, and a finalization requirement does not establish a completed finalization path. A physician using one service may need only a device, service, and export path. Record the audit host and report storage as a separate path. When a destination is supplied but its source is unstated, record the destination and unknown source in prose or the inventory. Keep hypothetical credential reachability out of the current-state diagram; describe it as an unresolved risk question.

Build a path table from evidence before drawing a diagram:

| Evidence ID | Established source | Action/data | Established destination |
|---|---|---|---|

Include an edge only from a complete row. A reported laptop download with no named source belongs in the inventory and unknowns, not an edge from a guessed store or app. A diagram is optional; a short path table is enough for a limited review.

## Trust boundaries

Document at least:

- customer device ↔ application
- production ↔ non-production
- operator ↔ subprocessors
- case/tenant ↔ other case/tenant
- PHI boundary ↔ PHI-blind external services

## Data inventory

Record established account/control owners with their evidence IDs, or UNKNOWN. Put recommended action owners in the action plan instead. Components and subprocessors are different inventories. List a component as an external vendor only when evidence establishes that relationship; otherwise keep its vendor/owner UNKNOWN.

| Component | Vendor / owner | Data handled | PHI? | Region | Contract/BAA status | Evidence level |
|---|---|---|---|---|---|---|
| Web app |  |  |  |  |  |  |
| Source storage |  |  |  |  |  |  |
| Database |  |  |  |  |  |  |
| Model runtime |  |  |  |  |  |  |
| Email |  |  |  |  |  |  |
| Analytics |  |  |  |  |  |  |

## Notes

- Distinguish persistent storage from transient processing.
- Include derived PHI, not only original PDFs.
- Include URLs, logs, analytics, and email when identifiers can leak there.
- If a system is unverified, label it UNKNOWN rather than assuming the intended architecture is real.
