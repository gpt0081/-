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

## 2026-11-22 Run330 current snapshot

- Source snapshot commit: `e2d528b73bed55037ffbb525a623c11ffc98049b`; source tree: `58ea5d18e1b142a631127a25d7d59cf93e5750d8`.
- Per-group inventories refreshed: 2,274 data files across annals 145, claims 154, documents 190, events 143, evidence 65, organizations 15, politician shards 109, research 1,450, plus the three operational/backbone roots.
- `data/integration/generated/source-triage.json` is the current per-file status authority: 341 BLOCKED_ID_CONFLICT, 597 INDEXED_NOT_CANONICAL_VERIFIED, 777 NON_JSON_PRESERVED, 556 UNMAPPED_AUXILIARY_OR_PARTIAL, 2 operational roots, 1 presidential backbone.
- Canonical source audit: 584 conflicted IDs, 11 exact duplicate IDs, 677 auxiliary records, 563 unintegrated sources, 11 partial sources, 0 parse errors.
- Root sync: 2,808 events with 2,681 canonical rows merged, 0 missing IDs, 0 duplicate IDs, 16 field variants; 975 politicians with 764 canonical rows merged, 0 missing IDs, 0 duplicate IDs, 110 field variants, 92 policy exclusions.
- Operational links: 202 linked / 310 unlinked. Structural audit: 0 integrity issues, 0 reference issues, 0 crosswalk gaps.
- PR #73/#74 changed paths: 34/34 present on main. PR #72 remains open; 29/29 changed paths are present. Path presence does not establish semantic integration.
- Final state remains **FULL_INTEGRATION_INCOMPLETE / CENTRAL_SYNC_PARTIAL**. No conflict was silently resolved. Floot untouched.
- Workflow: [Run 88](https://github.com/gpt0081/-/actions/runs/44951206183) completed its integration steps and failed only at the explicit completeness gate because unresolved conflicts/references remain.
- Weekly history-debt full review was not run; `last_full_review` was not changed.


## 2026-11-22 role-slot registry migration

- The integration extractor now routes explicit `candidateRoleId`, `candidateGroupId`, `roleId`, and `actorSlotId` records from actor collections into a separate `roles` registry, using a `role-` namespace. They are not politician promotions.
- The lossless `data/integration/generated/roles.json` and queryable `data/integration/canonical/roles.json` are audited alongside documents, claims, events, politicians and organizations. `eventLinks` on role records are reference-checked against the event registry.
- This specifically preserves the 1954 Korean Industrial Bank establishment-commissioner group and redacted Hong/Choi/Yu office-holder slots without inventing personal identities. Source records remain unchanged.
- This migration does not resolve the existing 584 source ID conflicts, the 110 politician and 16 event root-field variants, or the 310 unlinked operational-layer files. The completeness state must remain `FULL_INTEGRATION_INCOMPLETE` unless the regenerated audit proves otherwise.
- Floot was not modified or built.


## 2026-11-22 post-role-registry and PR74 additive backfill snapshot

- Source inventory: 2,274 files. Canonical materialized registries: documents 4,585; claims 2,115; events 2,681; politicians 852; organizations 83; roles 57.
- Source-level conflicts: 584 IDs. Auxiliary records: 666. Partial source files: 9. Unintegrated/auxiliary sources: 555.
- Operational roots: events 2,808; politicians 976. Root field variants: events 16; politicians 107. Missing canonical event/politician IDs after sync: 0.
- Structural audit: 0 integrity issues, 0 dangling reference issues, 0 crosswalk gaps. Operational layer links: 202 linked / 310 unlinked.
- PR #74 branch backfill: 199 history-debt sections, 29 coverage domains, 4 next-priority entries and 125 open leads added additively. Weekly debt review remains INCOMPLETE; last successful full review remains 2026-09-27.
- PR #73 content comparison: 11/18 identical, 7 shared-file variants. PR #74: 12/16 identical, 4 shared-root variants. All changed paths are present on main. PR #72 remains open; no whole-branch merge.
- Status remains `CENTRAL_SYNC_PARTIAL` / `FULL_INTEGRATION_INCOMPLETE`. The politician-root comparison against the PR #74 branch snapshot is pending. Floot was not modified or built.
