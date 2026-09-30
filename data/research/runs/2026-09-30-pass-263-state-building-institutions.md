# Pass 263 — early state-building institutions audit

Date: 2026-09-30 KST
Scope: Rhee-era state-building, deliberately breadth-first after pass 262. Floot untouched.

## Findings

### 1. Central bank formation was multi-actor, not presidential authorship
- 1949-06: Finance Minister Kim Do-yeon requested US Federal Reserve experts after ECA proposal.
- Arthur I. Bloomfield and John P. Jensen worked about five months with Korean agencies, financial-sector representatives and ECA, producing `Recommendations Regarding Central Banking Reform in Korea` and `Draft Act Establishing the Bank of Korea`; Ernst Fraenkel reviewed the draft legally.
- The draft was modified by the Finance Ministry financial committee, reviewed by a special committee including Finance Ministry, Office of Legislation and Bank of Chosen, passed Cabinet 1950-03-14, submitted to National Assembly 1950-03-18, debated 04-18/21, and passed 78-6 with 102 present. Bank of Korea Act promulgated 1950-05-05 as Act 138.
- Presidential Decree 350 (1950-05-11) created the establishment committee. Finance Minister Choi Sun-ju chaired it; Bank of Chosen governor Ku Yong-so was vice chair. Ku was appointed first BOK governor 1950-06-05 and the bank began business 06-12.
- Attribution rule: separate `requested_by`, `drafted_by`, `reviewed_by`, `cabinet_approved`, `legislated_by`, `promulgated_by`, `institutionalized_by`.

Sources:
- https://archives.bok.or.kr/content/exhibition/get/806/1242
- https://archives.bok.or.kr/content/exhibition/get/806/1243
- https://db.history.go.kr/contemp/level.do?levelId=dh_016_1950_03_14_0040
- https://www.law.go.kr/ (Act 138 chronology)

### 2. Local autonomy shows executive-legislative contest, not a linear government policy
- National Assembly passed an earlier Local Autonomy Bill 1949-03-09. Government requested reconsideration 03-31, citing nationwide administrative uniformity, premature full autonomy, and security concerns over elected governors/Seoul mayor.
- Reconsideration did not secure the constitutional supermajority. Revised work later passed in June; Local Autonomy Act was promulgated 1949-07-04 as Act 32, effective 08-15.
- Government submitted an amendment 1949-09-28 that sought stronger central control. Assembly committee/full-session processing rejected or narrowed important executive-control clauses, while an election postponement power survived in the final 1949-12-15 amendment (Act 73).
- First local council elections eventually occurred 1952-04-25 (city/eup/myeon councils) and 05-10 (provincial councils). NEC historical material gives turnout 80.2%, 88.4%, 93.1%, and 81.2% respectively.
- Attribution rule: model the government reconsideration request, Assembly resistance, amendment proposal, committee modifications, final enactment, postponement and 1952 execution as distinct sub-events.

Sources:
- https://db.history.go.kr/item/cons/level.do?levelId=cons_001_0020_0020_0020_0100_0030
- https://db.history.go.kr/item/cons/level.do?levelId=cons_001_0020_0020_0020_0100_0020
- https://db.history.go.kr/contemp/level.do?levelId=dh_015_1949_11_28_0080
- https://museum.nec.go.kr/museum2018/bbs/6/3/1/20170912155756377100_view.do?article_category=12&article_id=20180102105139965100

### 3. Education law was contested institution-building
- Education Act 86 was promulgated 1949-12-31. Article 1 stated the Hongik Ingan educational purpose.
- Contemporary records show prolonged conflict between Education Ministry and National Assembly; Education/Social Committee chair Lee Yeong-jun publicly described the bill as having been disputed for about a year.
- 1949-11-24 plenary session specifically voted on school-duration provisions, under deputy speaker Yun Chi-young.
- A 1948-10-15 education roundtable directly records Education Minister An Ho-sang, compilation bureau chief Son Jin-tae and Choe Hyeon-bae among actors debating school system/textbook policy.
- National Archives notes compulsory education began 1950-06-01, was disrupted by war, and became a major program again after the 1952 Enforcement Decree and the 1954-59 six-year completion plan.
- Separate from legislation, An Ho-sang's 1949 teacher ideological screening/purge is a distinct personnel/education-control event and must not be folded into the Education Act node.

Sources:
- https://www.law.go.kr/LSW/lsInfoP.do?ancNo=00086&ancYd=19491231&efYd=19491231&lsiSeq=5396
- https://db.history.go.kr/contemp/level.do?levelId=dh_014_1949_10_31_0050
- https://db.history.go.kr/contemp/level.do?levelId=dh_015_1949_11_24_0170
- https://db.history.go.kr/contemp/level.do?levelId=dh_008_1948_10_15_0010
- https://theme.archives.go.kr/next/koreaOfRecord/compulsoryEdu.do

### 4. Farmland reform remains a legislature/executive network
- Farmland Reform Act 31 was enacted 1949-06-21. National Assembly chronology records the bill passed 1949-04-27.
- Existing repository graph already contains Cho Bong-am, Lee Beom-seok, Lee Mun-won, Lee Soon-taek, Kim Do-yeon, Yu Jin-o, Lee Hoon-gu, Seo Yong-gil and Seo Sang-il. This pass avoids duplicating them and instead flags the need to add Agriculture Minister Yun Yeong-seon only after official appointment provenance is recovered.
- Adversarial rule: do not label farmland reform solely a Rhee or Cho policy; retain government draft, Planning Office review, Assembly alternatives, reconsideration, enactment and implementation as separable actions.

Sources:
- https://www.law.go.kr/LSW/lsRvsDocListP.do?lsId=000493
- https://db.history.go.kr/diachronic/level.do?levelId=tcct_1949_04_27

## Politician/public-official candidates deepened
1. `pol-kim-do-yeon` 金度演 / Kim Do-yeon — Finance Minister; central-bank expert request actor; existing registry node, add central-bank connection.
2. `cand-choi-sun-ju` 崔淳周 / Choi Sun-ju — Finance Minister; chair, BOK Establishment Committee; IDENTIFIED pending official appointment record.
3. `cand-ku-yong-so` 具鎔書 / Ku Yong-so — Bank of Chosen governor, first BOK governor; IDENTIFIED, official BOK provenance strong.
4. `cand-an-ho-sang` 安浩相 / An Ho-sang — Education Minister; education system/policy actor; IDENTIFIED, legislation-specific role still requires bill/committee record.
5. `cand-lee-yeong-jun` 李榮俊 / Lee Yeong-jun — National Assembly Education/Social Committee chair; education-bill actor; DISCOVERED→IDENTIFIED via contemporary record, exact hanja/biography to verify.
6. `cand-yun-chi-young` 尹致暎 / Yun Chi-young — deputy speaker presiding over 1949-11-24 education-law debate; IDENTIFIED, role ≠ authorship.
7. `cand-kim-jun-yeon` 金俊淵 / Kim Jun-yeon — legislator tied to local-autonomy reconsideration compromise; IDENTIFIED, exact amendment text target.
8. `cand-seo-woo-seok` Seo Woo-seok — legislator allied with reconsideration amendment; DISCOVERED, hanja/lifespan unresolved.
9. `cand-na-yong-gyun` 羅容均 / Na Yong-gyun — Interior/Public Security Committee chair in 1949 local-autonomy amendment debate; IDENTIFIED.
10. `cand-kim-hyo-seok` 金孝錫 / Kim Hyo-seok — Interior Minister in 1949 administrative/police structure; IDENTIFIED, local-autonomy executive role requires cabinet/ministerial papers.
11. `cand-son-jin-tae` 孫晉泰 / Son Jin-tae — Education Ministry compilation bureau chief; policy/public-official candidate, not automatically a politician.
12. `cand-choe-hyeon-bae` 崔鉉培 / Choe Hyeon-bae — Korean Language Society/education-policy participant; public-policy actor, not automatically a politician.

## Event/sub-event deltas
1. `evt-1949-1950-bok-formation/expert-request-1949-06`
2. `.../bloomfield-jensen-draft-1950-02`
3. `.../cabinet-approval-1950-03-14`
4. `.../assembly-enactment-1950-04-21`
5. `.../establishment-committee-1950-05-11`
6. `evt-1949-local-autonomy/reconsideration-1949-03-31`
7. `.../first-amendment-central-control-contest-1949-09-28--12-15`
8. `evt-1952-local-elections/city-eup-myeon-1952-04-25`
9. `.../provincial-1952-05-10`
10. `evt-1949-education-act/assembly-ministry-contest`
11. `.../school-duration-vote-1949-11-24`
12. `evt-1949-teacher-ideological-screening` (separate from Education Act)

## Adversarial checks
1. Rhee personally drafted BOK Act → contradicted by documented Bloomfield/Jensen drafting chain.
2. BOK Act was simply foreign-imposed → insufficient; Korean Finance Ministry requested experts and Korean bodies modified/reviewed/enacted it.
3. Rhee government uniformly favored local democracy → contradicted by 1949 reconsideration and stronger-control amendment proposal.
4. National Assembly simply blocked government local policy → contradicted; it enacted the law but modified executive-control provisions.
5. 1952 local elections originated only in 1952 political crisis → contradicted by 1949 statutory lineage, though timing remains a separate political question.
6. Education Act was solely An Ho-sang's design → insufficient; long Assembly/Ministry contest and committee actors documented.
7. Hongik Ingan purpose can be attributed to a single actor → insufficient; clause authorship still open.
8. Teacher purge is evidence of Education Act legislative intent → rejected; separate administrative event.
9. Farmland reform can be attributed solely to Rhee → contradicted by existing multi-actor legislative record.
10. Farmland reform can be attributed solely to Cho Bong-am → contradicted by existing government/Planning Office/Assembly chain.

## Cross-provenance bundles
- BOK formation: BOK institutional archive + contemporary press compilation (NIKH) + statute chronology.
- Local autonomy: constitutional-history DB + contemporary press compilation + NEC election-history data.
- Education: statute text + contemporary press/Assembly reporting + National Archives policy history.

## Open-lead/history-debt tracking
No HD-RHEE status was forced closed. Eight continuing targets were actively narrowed/retargeted: local-election timing vs constitutional crisis; executive authorship in local-autonomy amendment; BOK presidential involvement vs institutional chain; education-law clause authorship; compulsory-education implementation interruption; farmland-reform attribution; official appointment provenance for policy actors; president-versus-ministry attribution in ordinary administration.

## Coverage strengthened
Finance/monetary institutions; local administration/elections; education; agriculture/land reform; legislation/constitutional practice; appointments/administration; wartime implementation continuity.

## Direct-document accounting
Meaningful pages/documents directly opened or substantively inspected this pass: 17. Official/public-institution/primary-or-contemporary-document pages: 15. This does **not** meet the requested 40-document floor, so no inflation by counting search snippets or repeated views.

## Next lead queue
1. National Assembly 1950-04-18 BOK Act stenographic record: identify speakers and amendments.
2. National Assembly 1950-04-21 BOK Act vote record: recover roll-call/decision text.
3. Cabinet minutes 1950-03-14: identify ministers speaking on BOK Act.
4. Gazette 1950-05-05 Act 138 original image: register document object.
5. Presidential Decree 350 original gazette: extract full establishment committee roster.
6. BOK archive: first Monetary Board minutes 1950-06-05.
7. BOK archive: Ku Yong-so appointment instrument 1950-06-05.
8. BOK archive: 1952-02-11 40-question letter to Bloomfield and reply.
9. `Reports and Recommendations on monetary policy and banking in Korea` 1965 compilation: map seven underlying reports.
10. FRB/FRBNY archive: provenance for Bloomfield/Jensen mission appointment.
11. National Assembly 1949-03-09 Local Autonomy Bill full stenographic record.
12. Government reconsideration message 1949-03-31 original document.
13. National Assembly 1949-04-01 reconsideration vote full record.
14. National Assembly 1949-06-16 local-autonomy debate full record.
15. National Assembly 1949-06-17 final passage full record.
16. Gazette 1949-07-04 Act 32 original image.
17. Government amendment bill 1949-09-28 full text and cabinet sponsor.
18. Interior/Public Security Committee report on 1949 amendment.
19. National Assembly 1949-11-28 full stenographic debate; identify Na Yong-gyun interventions.
20. Gazette 1949-12-15 Act 73 original image.
21. Cabinet minutes 1951-12 through 1952-04: exact decision to hold first local elections.
22. Interior Ministry election directive for 1952-04-25 local councils.
23. UNCURK report covering 1952 local elections, original PDF pages.
24. NEC raw regional table for 1952 city council election.
25. NEC raw regional table for 1952 eup council election.
26. NEC raw regional table for 1952 myeon council election.
27. NEC raw regional table for 1952 provincial council election.
28. Education Act government bill as originally submitted: compare with Act 86.
29. Education/Social Committee report: identify Lee Yeong-jun and amendments.
30. National Assembly 1949-11-24 full record: school-duration vote and speakers.
31. Final Education Act passage session and vote.
32. Gazette 1949-12-31 Act 86 original image.
33. Education Ministry drafting file: An Ho-sang approval and drafting committee.
34. Verify Son Jin-tae official post dates through personnel/gazette record.
35. Verify Choe Hyeon-bae's formal government role versus external advisory role.
36. 1949 teacher ideological-screening directive original document and legal basis.
37. Education Act Enforcement Decree 1952 original text and sponsoring ministry.
38. Six-Year Compulsory Education Completion Plan original ministry document.
39. Farmland Reform Act 31 original gazette image and promulgation chain.
40. Cabinet/Assembly records for Yun Yeong-seon's role in implementation after Cho Bong-am.
41. Recover Choi Sun-ju appointment dates and Finance Ministry tenure from official personnel records.
42. Verify Seo Woo-seok identity, hanja, constituency and party from Assembly registry.

## Execution ledger
- independent research lines materially advanced: 20 (including sub-lines above; no duplicate query variants counted)
- general governance domains strengthened: 7
- non-president actor candidates new/deepened: 12
- event/sub-event nodes proposed/strengthened: 12
- adversarial searches/checks: 10
- cross-provenance bundles: 3
- open/history-debt lines tracked or retargeted: 8
- new concrete leads: 42
- directly inspected meaningful documents/pages: 17
- official/primary/contemporary/public-institution subset: 15
- weekly full HISTORY_DEBT review: not performed (not Sunday first run)
- Floot: untouched

The document floor was not met; this ledger records actual inspected material only.