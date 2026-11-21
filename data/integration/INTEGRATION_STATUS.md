# Integration migration status

Date: 2026-11-22

## Scope and safety

The current migration inventories every file under data/ outside data/integration/. It does not delete or rewrite research source files. data/events.json and data/politicians.json are mutable operational roots, not competing research-source variants. Their pre-reconciliation snapshots remain inventoried; their post-reconciliation hashes are recorded separately in root-sync-report.json. data/presidents.json remains a separate chronological overlay.

## Parser corrections

The source extractor now recognizes snake_case and legacy candidate IDs, including candidate_id, proposedPoliticianId, event_id, claim_id, document_id, candidate_document_id, and candidateOrganizationId. It also recognizes standalone one-record politician candidate files and explicit politician update collections. Document-like provenance entries are indexed only when they contain a stable document ID and a title, original location, or URL.

## Central-root policy

Only named pol-, cand-, and candidate- person records are eligible for the domestic politician root. Foreign/external actors, organizations, collective discovery classes, legacy president IDs, unresolved name slots, and unnamed candidate records remain preserved in source/canonical layers with explicit exclusion reasons. They are not silently promoted or merged.

## Audit corrections

Canonical rows may receive a normalized id field when the source used a legacy ID field. The audit now compares the canonical payload against the original source payload without treating that generated compatibility field as source mutation. Operational root hashes are validated against the post-sync snapshot.

## Remaining gate

This migration is not declared complete merely because the source inventory or canonical overlays exist. Conflicting source variants remain alternatives, auxiliary and specialized layers remain individually triaged, and operational evidence/annals/coverage/open-lead links must be checked. The generated report and integrity audit remain authoritative. Expected final status for this commit is FULL_INTEGRATION_INCOMPLETE until those backlogs are resolved.

Floot was not modified or built.
