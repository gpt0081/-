# 2026-11-12 08:18 KST | Central politician identity reconciliation (read-only audit)

## Method and scope
Read complete `data/politicians.json` (336 politician entries), `data/research/graphs/2026-11-12-0520-cabinet-geneva-actions.json`, README, history debt, prior reconciliation ledger, and open PR #72–74 descriptions. This is a **registry identity audit**, not new historical primary-source research. Root `data/events.json` connector content was empty and therefore not rewritten. No PR was merged.

## Concrete findings
1. `candidate-1952-chang-myon` (overlay) is already represented by `cand-1952-nov-chang-myon` (central), name 장면, 張勉, Chang Myon, status ANNALS_ACTIVE. **Candidate alias mapping proposed, not automatically applied**. Central role history presently includes 1952-11 former prime minister and 1960 acts; 1952-06 cabinet testimony requires item-level linkage, not a new politician ID.
2. `candidate-1954-pyun-yung-tai` (overlay) corresponds in name/Hanja/office to `pol-pyun-yong-tae` (central), status ANNALS_ACTIVE. **Candidate alias mapping proposed**. The 1954 Geneva action still requires Korean foreign-ministry original for authorization.
3. `candidate-1952-yi-pom-sok` (overlay) **cannot safely be mapped to a unique central ID**: both `pol-lee-beom-seok` and `pol-lee-beom-seok-1900` exist with the same name 李範奭 and overlapping high-office roles, but distinct central IDs. This is an explicit identity collision requiring provenance and record-history review. Do not choose by name or blindly merge. The 1952 June Home Affairs office is listed under the second ID, while the first lists initial prime minister and defense minister; these roles could refer to one historical person, but that inference alone does not justify destroying separate records.

## Safe integration plan
- Preserve the overlay IDs as immutable historical aliases until source-linked migration.
- Resolve `pol-lee-beom-seok` vs `pol-lee-beom-seok-1900` using birth/death dates, term-of-office original records, existing evidence references, and PR #72–74 branch content. If same identity, designate canonical ID and `legacyIds` / `sameAs` with correction history; if distinct, record explicit `differentFrom`.
- Check whether the 1952 June 3 action already appears in PR #73/#74 before creating root event IDs; compare date, telegram 1259, role and action, not only labels.
- Compare 1954 May 15 14-point draft and June 15 declaration to independent Korean Foreign Ministry and UN records before marking adoption or direct responsibility.
- Never mark HD-RHEE-006 resolved based on FRUS secondhand cabinet testimony; individual arrest orders remain unverified.

## Targeted next records
1. National Archives of Korea, 1952-06-03 cabinet minutes, Home Affairs attendance/appointment register, Yi's actual office.
2. Official appointment gazette for Yi Pom-sok in 1948 and 1952, plus personal archival birth/death entry, to decide whether two central IDs are duplicates.
3. Korean National Assembly June 1952 amendment introduction register, Chang's compromise bill sponsorship.
4. PR #73 and #74 changed-file inventories and actor ID maps, especially the 1952-07-04 Cabinet/Assembly timing conflict.
5. ROK Foreign Ministry May 1954 Geneva delegation instruction and 14-point original; UN June 15 declaration original.

## Execution ledger
New original historical documents opened: 0; official primary historical documents: 0; independent historical research lines: 0; adversarial historical searches: 0; completed independent cross-family verifications: 0; new politicians: 0; formal promotions: 0; new event integrations: 0; registry entries audited: 336; overlay candidate identities checked: 3; exact-name central records found: 4; collision cases: 1; actionable follow-up record targets: 5; files changed: this audit only. Weekly comprehensive historical-debt review not performed (Thursday). Floot untouched. No claim of one-hour elapsed.
