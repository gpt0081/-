# 2026-11-12 11:20 KST | Critical actor misidentification: Chang Taek-sang ≠ Chang Myon

## Primary source reinspection
Directly reopened US Department of State FRUS 1952–1954 vol XV/1 document 163, telegram 1259, Lightner, Pusan, 1952-06-03 midnight: https://history.state.gov/historicaldocuments/frus1952-54v15p1/d163 (access 2026-11-12). Its *Persons* index explicitly identifies **Chang Taek-Sang**, and paragraph 1 calls him Prime Minister Chang. This is **장택상 (張澤相)**, **not 장면 (張勉 / Chang Myon)**.

## Correction, no silent overwrite
Prior main research overlay `data/research/graphs/2026-11-12-0520-cabinet-geneva-actions.json` incorrectly uses `candidate-1952-chang-myon` for the June 3 prime-minister interview and compromise draft, and `identityReconciliation.mappings` proposes alias to `cand-1952-nov-chang-myon`. These mappings are **RETRACTED / INVALID** for the June 3, 1952 document and must not be imported. Prior narrative asserting 장면 authored the June 3 compromise draft is also retracted. The FRUS telegram identifies 장택상 as the prime minister who reported cabinet discussion and drafted the compromise proposal. The PR #74 actor graph already uses `pol-r139-jang-taek-sang` for these actions. Do not treat that PR as merged.

The same telegram describes Yi Pom-Sok's mass arrest suggestion as *Chang Taek-sang's report to US embassy officers*, not an adopted order. No `decided_by` or `executed_by` can be inferred. The telegram also records the prime minister explicitly declining to sponsor the proposed amendment; proposal to Rhee ≠ Assembly bill submission.

## Crosswalk and affected IDs
- INVALID: `candidate-1952-chang-myon` -> `cand-1952-nov-chang-myon` for FRUS d163.
- CORRECT ACTOR CANDIDATE: `pol-r139-jang-taek-sang` as used in PR #74 (verify against main registry before canonical migration).
- AFFECTED overlay actions: `evt-overlay-1952-cabinet-dissolution-discussion`, `evt-overlay-1952-chang-compromise-draft`; `evt-overlay-1952-yi-mass-arrest-suggestion` must identify the reporting prime minister as 장택상 rather than 장면.
- AFFECTED claim: `claim-overlay-1952-chang-bill-submission` should be reworded with 장택상; source is evidence against **his** formal sponsorship, not a claim about 장면.
- 1954 Pyun actor remains separate and unchanged. Yi duplicate identity remains unresolved.

## Follow-up and audit
1. Inspect main registry `pol-r139-jang-taek-sang` and birth/office sources before canonicalizing.
2. Apply an additive, reversible correction in the overlay and update all affected action references/claim text; preserve this correction ledger and previous ID as a deprecated alias only, never as sameAs.
3. Search main evidence/annals and prior 2026-11-12 reports for all assertions of 장면 as June 3 PM; annotate correction, avoid silently rewriting historical reports.
4. Reconcile PR #72–74 and run224 identity guardrail without name-only matching.
5. Seek 1952-06-03 ROK cabinet original minutes to independently verify the reported discussion.

## Execution ledger
One original archival document directly reopened; one critical historical identity error corrected at audit level; one independent primary provenance family (US State FRUS); one adversarial source check against existing overlay; zero new primary Korean originals, zero formal registry promotions, zero central events integrated, zero cross-family confirmations. Historical debt weekly full review not performed (Thursday). Floot untouched. No claim of one-hour runtime.
