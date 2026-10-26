# Rhee research pass 72 — UN resolution lineage audit

Access date: 2026-09-22

## Purpose

Continue pass 71 without repeating the India-vote search. This pass tests the document lineage around A/2450 → A/RES/711(VII)[A-C], the legal/documentary bridge from the Korean Armistice to the political conference, and the distinction between committee drafts, plenary amendments, and final resolution components.

## Findings

1. The UN Digital Library independently identifies final A/RES/711(VII)[A] as **Implementation of paragraph 60 of the Korean Armistice Agreement**, adopted 1953-08-28 at the 430th plenary meeting by 43-5-10. Its metadata explicitly records A/L.158 as an amendment and A/2450 as the committee report.
2. Final A/RES/711(VII)[B] was adopted 55-1-1 at the same plenary meeting and likewise derives through A/2450.
3. Final A/RES/711(VII)[C] was adopted 54-3-1 at the same meeting. This further confirms pass 71's warning that the final component labels cannot be mapped mechanically onto the committee report's A/B/C/D labels.
4. The UN Dag Hammarskjöld Library's official seventh-session resolution table independently gives the same 711 A/B/C vote counts and records A/L.158 as amending the 711 package. This is a second UN publication surface, not a new provenance family, but it is useful metadata corroboration.
5. FRUS d752 explains the transformation: committee resolution C (India participation) was withdrawn from plenary disposition after Krishna Menon's intervention, while committee D (communication to Beijing/Pyongyang) was adopted. The surviving committee A, B and D became the three final components of Resolution 711. This is the missing semantic explanation behind the label shift.
6. A/2431 and S/3079 are UN document symbols reproducing the Korean Armistice Agreement. A contemporaneous 1953 American Journal of International Law publication states that the agreement was reproduced in those UN documents. These should be registered as document objects linking the armistice's paragraph 60 to the later 711A implementation event.
7. FRUS d748 records the procedural trigger: Resolution 705(VII), adopted 1953-04-18, called for reconvening the General Assembly and resuming the Korean question once the armistice was signed; the Assembly reconvened on 1953-08-17 after notification of signature. Thus the August conference-composition debate belongs to a pre-existing procedural chain, not an ad hoc post-armistice invention.

## Adversarial checks

- `final 711C = committee India resolution C` — contradicted.
- `A/L.158 created an entirely new resolution independent of A/2450` — contradicted by UN metadata: it amended the A/2450-derived final package.
- `all three final 711 components had the same vote` — contradicted: 43-5-10 / 55-1-1 / 54-3-1.
- `political-conference machinery began only after the armistice` — narrowed/contradicted by Resolution 705(VII)'s April reconvening trigger.
- `paragraph 60 can be modeled only as FRUS narrative` — contradicted; A/2431/S/3079 and 711A create a UN documentary chain.
- `India proposal was defeated in plenary` — contradicted again; withdrawal/non-vote remains the correct disposition.
- `final resolution component letters preserve committee-report semantic identity` — contradicted.
- `A/2450 alone is enough to reconstruct final disposition` — contradicted; A/PV.430 and final component metadata are needed.
- `A/RES/711(VII) is a single indivisible vote` — contradicted by separate A/B/C vote metadata.
- `ROK policy can be inferred from UN final votes alone` — unsupported; Korean mission/cabinet/Foreign Ministry records remain required.

## Data-model consequence

Document registry needs explicit relations: `derived_from`, `amended_by`, `withdrawn_before_plenary`, `plenary_successor`, `reproduces_document`, and `implements_clause_of`. Event graph should distinguish committee adoption, withdrawal request, plenary adoption, and communication/execution.

## Open leads

Highest value remains A/PV.430 full text and A/L.158 original. Also retrieve A/PV.427 / A/2386 for Resolution 705(VII), A/2431 and S/3079 exact UN copies of the armistice, and Korean Foreign Ministry / ROK Observer Mission records showing how Seoul instructed its UN representation.

## Sources directly checked this pass

- UN Digital Library: A/RES/711(VII)[A], metadata/vote/amendment lineage.
- UN Digital Library: A/RES/711(VII)[B], metadata/vote.
- UN Digital Library: A/RES/711(VII)[C], metadata/vote.
- UN Dag Hammarskjöld Library official 7th-session resolution table.
- FRUS XV/2 d752 editorial note.
- FRUS XV/2 d748 editorial note.
- AJIL 47 supplement reproduction note for A/2431 and S/3079 (contemporaneous secondary publication pointing to UN originals).

No blocked source is counted as directly opened. Floot untouched.