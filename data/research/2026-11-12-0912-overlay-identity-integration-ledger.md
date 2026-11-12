# 2026-11-12 09:12 KST | Actor identity reconciliation in research overlay

## Scope and provenance
Reviewed README, HOURLY_ANNALS_LOOP, HISTORY_DEBT, presidents, politicians registry, root events fetch attempt (empty content), Rhee evidence/coverage/open leads, methodology, latest commits, open PR list, prior 06:16 and 08:18 reconciliation reports, and 05:20 cabinet/Geneva overlay. The identity comparisons originate in the 08:18 audit of 336 central politician entries, not newly examined historical originals. No Floot changes.

## Change
Added `identityReconciliation` to `data/research/graphs/2026-11-12-0520-cabinet-geneva-actions.json`. Two proposed aliases: `candidate-1952-chang-myon` -> `cand-1952-nov-chang-myon`; `candidate-1954-pyun-yung-tai` -> `pol-pyun-yong-tae`. One explicit unresolved identity collision: `candidate-1952-yi-pom-sok` vs `pol-lee-beom-seok` and `pol-lee-beom-seok-1900`. These are reconciliation annotations, not source-verified promotions, and event/action nodes retain their original references.

## Non-integration gates
Root `data/events.json` fetch returned empty content; no central event writes were attempted. PR #72–74 may contain overlapping action IDs and contradictory chronology; their full diffs and source chains remain to be checked. Do not infer cabinet adoption or arrests from FRUS secondhand testimony. Do not merge Yi's two registry entries until original appointments, birth/death and all incoming references are audited. HISTORY_DEBT states unchanged, especially HD-RHEE-006.

## Active primary-record queue
1. National Archives of Korea, 1952-06-03 cabinet minutes and attendance register, to distinguish Chang's reported account from recorded decisions.
2. National Archives of Korea, 1948 first prime-minister appointment gazette and 1952 interior-minister appointment gazette, to verify Yi's identity and offices.
3. Korean National Assembly, June 1952 bill-introduction ledger, to test whether Chang sponsored the compromise amendment.
4. Korean National Assembly, 1952-07-04 plenary minutes and cabinet minutes, to resolve morning/night chronology against PR #74.
5. National Archives of Korea, 1952 May-July arrest warrants and martial-law command chain, to test HD-RHEE-006.
6. ROK Foreign Ministry, May 1954 Geneva delegation instructions and 14-point draft, to distinguish draft delivery from authorization.
7. United Nations, June 1954 Geneva conference proceedings and June 15 signed declaration, to compare with FRUS XVI d237.
8. GitHub PR #72/#73/#74 changed-file inventories, document IDs and event IDs, to avoid duplicate central events.

## Execution ledger
Independent new historical research lines: 0; historical originals newly opened: 0; official/primary originals newly opened: 0; adversarial historical searches: 0; new independent cross-provenance bundles: 0; new politician profiles: 0; formal promotions: 0; new event nodes: 0; identity mappings annotated: 2; collision cases preserved: 1; new leads: 0 (8 existing targets carried forward); historical-debt entries materially narrowed: 0; files changed: overlay and this ledger; coherent commits: 210521527edce293f88885750edb4f865af020bd plus this file's commit. Status: PARTIAL_INTEGRATION, not INTEGRATED. The available tool window was not one hour and no one-hour claim is made. 역사부채 주간 전수조사 미실시 (Thursday).
