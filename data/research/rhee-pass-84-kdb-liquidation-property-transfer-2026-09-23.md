# Rhee research pass 84 — KDB predecessor liquidation and property-transfer chain

Date: 2026-09-23
Scope: Korea Industrial Bank liquidation, transfer to Korea Savings Bank/KDB, property disposal, actor discovery.

## Why this line matters
Pass 83 established that KDB creation was not a simple rename of Korea Industrial Bank. This pass follows the asset/branch/property implementation layer, where liquidation records expose actors and administrative decisions that the enabling statutes alone cannot name.

## Directly inspected sources
1. National Archives of Korea, `기록으로 만나는 대한민국 > 산업은행`: official institutional narrative. Confirms 1951 drafting, Oct. 1951 Assembly submission, Nov. 1953 passage, Dec. 1953 promulgation, 54-article enacted structure, government capital payment of 10 million won, and April 1954 launch.
2. National Legal Information Center recent-law index for 1954: confirms Supreme Court Rule No.20 `한국산업은행등기처리규칙` (1954-02-24), Decrees 858-860 (1954-01-18), and Law 302 (1953-12-30).
3. Bank of Korea official biography of Gu Yong-seo: confirms 1950 BOK establishment-committee vice-chair, BOK governor, 1953 Korea Coal Corporation president, 1954 KDB first/second governor, 1958-60 Commerce Minister.
4. National Archives of Korea, `중요 공개기록물 해설집 V - 국세청·성업공사 편`: directly indexed text describes a 1954-04-01 transaction involving KDB governor Gu [redacted], Korea Industrial Bank head Hong [redacted], a representative liquidator Choi [redacted], Korea Savings Bank, and its president Yu [redacted]. It also records 1954-04-23 demand for 50 million won unpaid real-estate purchase money to be deposited into the KIB liquidation-committee account; 1954-07-07 lease-renewal/rent-revision action; and 1954-07-22 requests for appraisals of former KIB properties in Bupyeong, Chungju, Suncheon and Samcheonpo.
5. National Archives of Korea, Chapter III / Japanese-property claims guide: identifies record series `대일재산관계 자료철 (한국식산은행 청산사무국)`, `대일민간청구권 신고서철 (한국식산은행 청산위원회)`, and `대일청구권 자료표 (한국식산은행 청산사무국)`.
6. National Archives record series DA0422839, `식산채권 및 애국채권, 복표 (한국식산은행청산위원회)`: 1963 permanent record series, 24 items, demonstrating liquidation-committee continuity into later bond settlement work.
7. National Archives DA0422839 item listing pages 1-3: identifies specific bond-redemption and interest-payment records, including `조선식산 채권 원리금 상환에 관한 건(제46차 정기위원회 부의)`.
8. SC First Bank official history: records 1954-01-25 succession of Korea Industrial Bank business, branches and staff by Korea Savings Bank. This is independent institutional evidence that the predecessor's commercial-bank functions were split before KDB launch rather than all passing wholesale to KDB.
9. Academy of Korean Studies Encyclopedia entry on KDB: secondary institutional cross-check of the 1951 draft/1953 passage/1954 launch and 10 million won government contribution.

## Findings
### F84-1 — predecessor succession was functionally split
The SC First Bank official history states that Korea Savings Bank succeeded KIB business, branches and employees on 1954-01-25. The National Archives liquidation narrative separately shows KDB, Korea Savings Bank and the KIB liquidation committee interacting over property in April-July 1954. Therefore the predecessor-to-KDB transition should be modeled as a multi-destination succession/liquidation process, not a single whole-bank transfer.

### F84-2 — liquidation remained an active administrative process after KDB launch
The 1954-04-23, 07-07 and 07-22 actions show a liquidation committee continuing to collect unpaid sale proceeds, revise leases and request property appraisals after KDB's April establishment. This strengthens the distinction between statutory dissolution, operational transfer and liquidation completion.

### F84-3 — new actor group exposed, but names remain partially redacted
The official Archives guide exposes four role slots in the 1954-04-01 transaction: KDB governor Gu, KIB head Hong, representative liquidator Choi, Korea Savings Bank president Yu. Gu is independently identifiable as Gu Yong-seo. The other three must not be guessed from surname alone. They become candidate-role nodes pending original contract/record recovery.

### F84-4 — a new non-president politician lead: Yu Wan-chang
A secondary locator identifies Yu Wan-chang (兪莞昌, Ryu/Yu Wan-chang), former Property Administration chief and later first Reconstruction Minister, as a Korea Industrial Bank liquidation-committee chair. This is historically plausible and highly connected, but the inspected official Archives text redacts the representative liquidator as Choi, so the chairmanship date/phase must be established from primary records before formal registry promotion. Status remains IDENTIFIED-CANDIDATE, not VERIFIED for the liquidation role.

## Event decomposition
- `evt-1954-0125-kib-commercial-function-transfer`: Korea Savings Bank succeeds KIB business, branches and employees. Evidence: SC First Bank official history. Legal instrument still open.
- `evt-1954-0401-kib-property-transaction`: KDB/KIB/Korea Savings Bank/liquidator property transaction described in NAK guide; original contract needed.
- `evt-1954-0423-kib-unpaid-property-payment-demand`: demand to KDB governor for 50 million won unpaid property-sale balance to liquidation account.
- `evt-1954-0707-kib-lease-renewal-rent-revision`: liquidation committee directs renewal/repricing of leases on former KIB properties.
- `evt-1954-0722-kib-property-appraisal-request`: liquidation chair asks Property Administration and KDB to appraise former KIB properties before disposal.
- `evt-1963-kib-bond-settlement`: DA0422839 documents continuing liquidation/bond-redemption administration.

## Adversarial checks
1. Against `simple rename`: split commercial-function transfer plus continuing liquidation contradicts it.
2. Against `all KIB assets went immediately to KDB`: official liquidation/property records show residual assets and third-party transfer activity.
3. Against `liquidation ended on KDB establishment`: April-July 1954 and 1963 record series contradict this.
4. Against naming redacted Hong/Choi/Yu by surname inference: no promotion without original instrument.
5. Against assuming Gu chaired the establishment committee because he became governor: no new evidence; claim remains open.
6. Against treating 4/1 as merely ceremonial: NAK still links launch to completed government capital payment; exact voucher remains open.
7. Against treating SC First Bank history as proof of legal title for every transferred asset: it proves institutional succession claim, not parcel-level title.
8. Against using a later liquidation committee composition for 1954: roster dates must be recovered.
9. Against assuming Yu Wan-chang was the `Choi` representative liquidator: incompatible surname signal means roles/phases may differ; preserve conflict/open state.
10. Against conflating dissolution with liquidation completion: later official record series requires separate event states.

## Cross-check bundles
A. NAK KDB narrative + Law index: statutory creation and administrative launch.
B. SC First Bank official history + NAK liquidation narrative: split transfer to Korea Savings Bank plus continuing liquidation.
C. NAK guide + DA0422839: 1954 property liquidation actions plus long-tail bond settlement continuity.

## Open leads / next queue
1. NAK: recover original 1954-04-01 KIB/KDB/Korea Savings Bank property contract and unredacted names.
2. NAK: identify archival management number for the 1954-04-23 50 million won payment-demand document.
3. NAK: recover 1954-07-07 liquidation-committee lease-renewal decision and minutes.
4. NAK: recover 1954-07-22 appraisal request and identify the chair `Choi` in signature block.
5. NAK: retrieve appraisal reports due 1954-08-10 for Bupyeong/Chungju/Suncheon/Samcheonpo.
6. NAK: locate 1954-09-04 appraisal-fee calculation table source file and signatories.
7. National Legal Information Center: retrieve full original text of Supreme Court Rule No.20.
8. Court registry/NAK: recover first KDB corporate registration application and attached articles.
9. Ministry of Finance records: recover Decree 860 Article 11 establishment-progress report.
10. Ministry of Finance records: recover nine KDB establishment commissioner appointment/commission documents.
11. Treasury records: recover 10 million won government capital payment voucher/provisional receipt and exact date.
12. KDB archive: recover first articles of incorporation and Finance Minister approval instrument.
13. National Assembly: recover 1953-07-13 KDB bill record and speakers.
14. National Assembly: recover 1953-11-21 KDB bill deliberation and amendment actors.
15. National Assembly: recover 1953-11-28 final passage record and vote/attendance.
16. National Assembly: resolve draft article count 68→62→54 with committee reports.
17. SC First Bank archive: recover legal instrument underlying 1954-01-25 business/branch/staff succession.
18. NAK: locate KIB branch-transfer inventory to Korea Savings Bank.
19. NAK: locate KIB employee transfer roster and destination institutions.
20. NAK: locate KIB asset/liability partition schedule between KDB, Korea Savings Bank and liquidation estate.
21. NAK: identify `홍ㅇㅇ` KIB head from original 1954-04-01 instrument.
22. NAK: identify `최ㅇㅇ` representative liquidator from original instrument.
23. SC First Bank archive: identify `유ㅇㅇ` Korea Savings Bank president on 1954-04-01.
24. NAK/government personnel gazette: establish Yu Wan-chang's exact KIB liquidation-chair term.
25. Government gazette: verify Yu Wan-chang's Property Administration chief term and appointment instrument.
26. Government gazette: verify Yu Wan-chang's first Reconstruction Minister appointment and term.
27. NAK: map KIB liquidation committee composition changes 1954-1963.
28. NAK DA0422839: recover `제46차 정기위원회` minutes/date and attendee roster.
29. NAK: recover Japanese-property-claim files produced by KIB liquidation office and identify responsible officials.
30. NAK: determine when KIB liquidation administration transferred to Seong-eop Corporation and by what authority.
31. KDB history archive: recover 1954 first annual/business report and opening balance sheet.
32. KDB history archive: identify first board members and appointment instruments.
33. Finance Ministry: recover KDB governor Gu Yong-seo appointment instrument/date.
34. NAK: trace KIB real estate in Incheon Bupyeong from appraisal through sale.
35. NAK: trace Chungju former-KIB property from appraisal through sale.
36. NAK: trace Suncheon former-KIB property from appraisal through sale.
37. NAK: trace Samcheonpo former-KIB property from appraisal through sale.
38. NAK: compare liquidation lease rates before/after July 1954 revision.
39. NAK: identify whether unpaid KDB property purchase balance was fully paid and when.
40. NAK: determine whether liquidation committee reports were submitted to Finance Ministry and recover them.

## History debt impact
No existing Rhee HD item is resolved by this pass. Create a research-level open debt: exact KIB asset/function partition, liquidation roster and 1954 representative liquidator remain unresolved. Do not merge this into a presidential direct-command debt.

**역사부채 주간 전수조사 미실시.** Wednesday; last full review remains 2026-09-20.