# Politician Network Pass 99 — execution ledger

Date: 2026-09-23
Focus: 1951 어업보호정책 선행문서 계보와 제98회 국무회의 원안통과 검증.

## Material progress
- Directly opened meaningful source pages/documents: **8** (including distinct primary-document records/metadata and institutional research pages; repeated index views not double-counted).
- Official/public/primary or institutional sources: **6**.
- Independent research lines materially advanced: **15**.
- Governance domains strengthened: **7**: cabinet decision process, foreign affairs, commerce/fisheries administration, international-law precedent, Japan treaty/fisheries negotiation, presidential submission workflow, maritime-resource policy.
- Non-president actor nodes newly/deeper structured: **4**: 변영태, 지철근, 김동조, 김훈. President node also gained a recipient/intended-declarant edge.
- Event/sub-event chain structured or materially strengthened: **8**.
- Adversarial checks: **10**.
- Cross-check bundles: **3**: 9/8 primary draft vs later chronology; 1951 document-chain index vs 1952 gazette; memoir attribution vs contemporaneous office-level evidence.
- Existing/open lines materially narrowed: **6**: 98th cabinet meeting existence, proposal content, original passage, next-day presidential submission, 1951 policy lineage, name-change uncertainty.
- Concrete next leads generated: **40**.

## Key findings
1. A contemporaneous 1951-09-08 Foreign Ministry draft, `외정 제958호`, directly states that the 98th Cabinet meeting on 1951-09-07 at the Gyeongnam Provincial Government temporary cabinet room considered a proposal for the President to proclaim a fisheries-protection zone excluding foreign fishing and passed it **as originally proposed**.
2. The same document is a Foreign Minister → President submission and contains reasons, policy logic, and boundary coordinates. It invokes Truman's 1945 fisheries declaration and Latin-American precedents, preserves MacArthur-line claims, and explicitly treats early proclamation as leverage for a future Japan fisheries agreement.
3. The official diplomatic-document series shows a precursor chain beginning no later than 1951-05-04, with a report titled `아국영해선 외의 어업보호관할권문제`, followed by approval/routing documents in May-June, an interagency fisheries meeting on 1951-08-25, and September cabinet/submission records.
4. This narrows the Pass-98 upstream lead substantially. However, it does **not** prove the later claim that the name changed from `어업관할수역` to `어업보호수역` during the 98th meeting. The opened 9/8 document says the protection-zone proposal passed unchanged; the 9/4, 9/6 drafts and actual cabinet minutes remain necessary.
5. Office-level Foreign Ministry authorship does not yet identify the individual drafter. Ji Cheol-geun and Kim Dong-jo remain attribution leads rather than confirmed drafted_by/proposed_by actors.

## Files changed
- `data/research/rhee-pass-99-peace-line-1951-document-chain-2026-09-23.md`
- `data/research/candidates/pass-99-peace-line-1951-chain.json`
- `data/research/runs/2026-09-23-politician-network-pass-99.md`

## Commits
- `638fb931460f33b4f609e77a2806c563dbb4052f` — 1951 primary-text recovery, precursor chain, adversarial audit, 40-lead queue.
- `c2d8c52e8ddc091d99a6177158d9e5fa0702ba6b` — document/actor/claim/event structure.
- This commit records the execution ledger.

## Minimum-target shortfalls
This pass did **not** reach 20 independent research lines, 10 non-president actors, 40 directly opened documents, 20 official/primary documents, or 8 history-debt/open-lead traces. Actual counts are preserved. Several high-value NAHF individual-document URLs returned HTTP 502 when opened even though their indexed metadata remained available, so the run pivoted to new document IDs and the fully exposed `외정 제958호` rather than burning calls on repeated retries.

## Next priority
Open the 1951-09-04 and 09-06 `외정 제958호` versions and `총의 제174호`, then recover the actual 98th Cabinet minutes. In parallel, extract authors/recipients from the 1951-05-04, 05-10, 05-16, 06-18, and 08-25 documents. This should reveal whether the chain is best modeled as Fisheries Bureau technical drafting → Commerce Ministry routing → Foreign Ministry legal/diplomatic revision → Cabinet decision → presidential submission, or whether that apparent sequence is misleading.

**역사부채 주간 전수조사 미실시.**