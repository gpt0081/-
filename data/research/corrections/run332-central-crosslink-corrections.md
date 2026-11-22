# Run332 central cross-link corrections (2026-11-22)

## Run149 cabinet records: research grouping is not a historical event

Fourteen records in `data/politicians/run149-cabinet-candidates.json` pointed to `evt-r149-cabinet-signature-comparison`. No corresponding dated event record exists in the event registry, and the identifier described a research comparison across three Gazette/legal records rather than a historical action. The invalid `eventIds` relation was removed. Existing `evidenceDocumentIds` were retained and mirrored into `documentIds`:

- `d149-law-384`, Government Organization Act amendment, 1956-02-01
- `d149-law-385`, Local Autonomy Act amendment, 1956-02-13
- `d149-law-388`, Local Autonomy Act amendment, 1956-07-08

No ministerial tenure, appointment date, party affiliation or biography was newly inferred.

## Run218 Korea-Japan preliminary talks: person versus organization

- The 1951-10-20 event's legacy `president-choi-kyuhah` actor reference was crosswalked to the existing stable person node `pol-choi-kyu-hah`. The old presidential overlay ID is preserved in `legacyIds`; the separate presidential chronology remains unchanged.
- The 1951-12-12 "ROK legal-status subcommittee" was removed from `politicianIds` and represented as `org-rok-japan-legal-status-subcommittee-1951`. Its roster, chair, formal mandate and individual authorship remain open. The six-article draft is not treated as an adopted agreement.

## Run136 July 4, 1952 teller designation

The original National Assembly transcript `d129-cons-0170` names Seo Yi-hwan, Jeong Mun-heum, Jang Geon-sang and Kim Yang-su as designated tellers. Three missing candidate IDs are now represented as `DISCOVERED` nodes and linked to the transcript and `evt-r136-tellers`. The Jang Geon-sang and Kim Yang-su candidates carry `possibleSameAs` references to existing 1951 candidates; they are not merged without Hanja/biographical identity evidence. The source event continues to state that actual teller execution requires further confirmation.

## Integration-engine corrections

- Legacy `sources` and `metadataOnly` document arrays are now eligible for canonical document extraction only when a stable document ID and identifying metadata are present.
- Nested `additionalEvent` objects are extracted only when they have a stable event ID and date/title/name.
- Existing stronger politician research status is preserved against a weaker incoming source status, with the weaker variant and provenance retained. No automatic promotion occurs.
- Reference audit coverage now includes evidence-document IDs, linked IDs and snake_case organization fields. President overlay IDs are accepted as legacy person references, not duplicate politician records.
- Operational sidecar linking recognizes lower-case `dNNN-...` document IDs and valid president-overlay aliases.

Floot was not modified or built. Final central-sync status is determined only by the regenerated GitHub Actions audit.
