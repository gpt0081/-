# 2026-11-12 05:20 KST | Actor/action/document overlay integration

Status: PARTIALLY_INTEGRATED_SHARDED. Prior run 04:20 source audit and lead queue reviewed; no claim of new discovery of those documents. Root `data/events.json` and `data/politicians.json` deliberately not overwritten because full registry identity reconciliation and large-file migration are pending. This overlay is machine-readable and deliberately preserves candidate identifiers rather than creating unsafe duplicate stable IDs.

## Directly rechecked original texts
- FRUS XV/1 d163 (telegram 1259, June 3, 1952): Chang's report of cabinet dissolution dispute, Yi Pom-Sok mass-arrest suggestion, Chang compromise draft and explicit refusal to sponsor it. Nested hearsay: Chang -> embassy officers -> Lightner. https://history.state.gov/historicaldocuments/frus1952-54v15p1/d163
- FRUS XVI d167 (telegram 84, May 17, 1954): Pyun's 14-point May 15 DRAFT; South Korean election conditional on majority wishes; ROK constitution to remain until amended. https://history.state.gov/historicaldocuments/frus1952-54v16/d167
- FRUS XVI d237 (Declaration June 15, 1954): separate multinational final declaration, Pyun listed as ROK signatory; signed original transmitted June 25 Secto 4. https://history.state.gov/historicaldocuments/frus1952-54v16/d237

## Structured work
Five event/action nodes, three document objects, three actor candidate records, three explicit adversarial claims. Claim relations distinguish contradicts from insufficient. Direct presidential arrest order is NOT inferred. Cross-provenance independent three-family verification: 0. All three reviewed items belong to FRUS publication family, even where they reproduce documents of different origin.

## Handoff / unresolved
1. National Archives Korean cabinet minutes 1952-06-03 to test Chang's reported discussion.
2. National Assembly June 1952 bill introduction ledger to test whether compromise draft was formally sponsored.
3. Korean Interior Ministry/police arrest warrants and dispatches to separate Yi suggestion from execution.
4. ROK Foreign Ministry 1954-05-15 original Pyun text and delegation authorization.
5. UN Geneva proceedings May 17–June 15 and June 25 signed declaration facsimile.
6. Reconcile three candidate IDs with existing `data/politicians.json` before promotion.

Execution ledger: 3 distinct previously known substantive originals re-opened; newly discovered original documents 0; official contemporary documents rechecked 3; independent research threads 2; government domains 2; adversarial claims formalized 3; existing leads followed 5; new leads 0 (existing leads made actionable in graph); new event/action overlay 5; candidate politicians 3; formal registry promotions 0; strict cross-family verifications 0. No one-hour elapsed claim. Weekly comprehensive historical debt review not performed (Thursday). Floot untouched.