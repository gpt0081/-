# Politician Network Pass 10 — 2026-09-20

## Scope

Focused continuation of the Rhee Syngman backbone through the 1949 Farmland Reform Act, while generalizing the material into politician-centric and event-centric records. The weekly full HISTORY_DEBT review was not repeated because `last_full_review` is already `2026-09-20`.

## High-priority leads pursued

1. Legal character of the government's 1949-05-16 `소멸통고` and the National Assembly response.
2. Exact June 14–15 constitutional sequence behind the Act's legal finalization.
3. Legislative actors obscured by a president-only account of farmland reform.
4. Non-controversial policy formation: Agriculture Ministry draft → Planning Office revision → cabinet → Assembly Industrial Committee → plenary amendment.

## New findings / narrowing

The National Institute of Korean History constitutional-history DB provides a substantially tighter domestic reconstruction than the shorthand used in FRUS. The bill was transmitted to the government on 1949-05-02 after the second Assembly session had expired. Prime Minister Lee Beom-seok sent a return-reasons document and a 1949-05-16 notice arguing that because the Assembly was out of session, return under Constitution Article 40 could not be performed and the bill should be regarded as naturally lapsed. The Constitution did not expressly provide for this closed-session situation.

The third Assembly then debated the matter on June 14 and 15 (3rd Assembly, sittings 16 and 17) and resolved that the government's lapse notice was unlawful and that the bill had become law under Article 40(4). The government promulgated Act No. 31 on 1949-06-21. This narrows HD-EVT-001: the remaining conflict is not merely a one-day date mismatch, but also whether FRUS's `veto/override` terminology is an analytically acceptable shorthand for an irregular `소멸통고 → 위법 판단 → 법률확정 결의` sequence.

## Politician graph expansion

- `pol-lee-hoon-gu` (이훈구): named lead sponsor of a 1948-11-13 Assembly farmland-reform bill with 31 co-sponsors.
- `pol-seo-yong-gil` (서용길): with 30 other members pressed for the government bill to be placed on the agenda when the Industrial Committee delayed action.
- `pol-seo-sang-il` (서상일): Industrial Committee chair during the committee alternative and agenda conflict; individual statements still require primary-text extraction before personal intent is attributed.
- `pol-yun-jae-geun` (윤재근): March 14 plenary criticism of a land-reform design favoring landlords over farmers is cited to the original stenographic record by the constitutional-history DB.

These actors are stored as legislative candidates, not ranked or normatively scored.

## General policy coverage

The event record now distinguishes institutional stages: Agriculture Ministry draft (1948-09-07 committee; 1949-01-14 draft), Planning Office revision (1949-02-04), cabinet adoption (1949-02-05), Assembly member bill, Industrial Committee alternative, plenary amendment, government lapse notice, Assembly constitutional response, promulgation, and later amendment. This prevents attribution of the whole reform to any single politician.

## Adversarial check

The FRUS characterization remains preserved rather than overwritten. Domestic constitutional-history material points to June 21 promulgation and a non-standard lapse notice rather than a conventional veto/override sequence. HD-EVT-001 remains CONFLICTED pending the actual June 14–15 stenographic text, the May 16 return-reasons/notice original, the June 21 promulgation/approval record, and the underlying U.S. diplomatic dispatch used for the FRUS memorandum.

## Files changed

- `data/events.json`: farmland-reform event generalized from a president-only node to a multi-actor policy/legislative/constitutional network; HD-EVT-001 attached.
- `data/politicians.json`: added Lee Hoon-gu, Seo Yong-gil, Seo Sang-il, Yun Jae-geun as stable candidate nodes.
- this run ledger.

## Sources / provenance

- National Institute of Korean History, Constitutional History DB, farmland reform legislative history and stenographic citations: https://db.history.go.kr/item/cons/level.do?levelId=cons_001_0020_0020_0030_0040_0060&viewType=tab (accessed 2026-09-20).
- Academy of Korean Studies, Encyclopedia of Korean Culture, `농지개혁법`: https://encykorea.aks.ac.kr/Article/E0080662 (accessed 2026-09-20).
- U.S. Department of State, FRUS 1949, Korea memorandum/document 304: https://history.state.gov/historicaldocuments/frus1949v07p2/d304 (retained as conflicting foreign diplomatic characterization; accessed 2026-09-20).

## Next priority

Open and extract the 3rd Assembly sittings 16 and 17 (1949-06-14/15) speaker-by-speaker. Build edges for who argued `재의요구`, `소멸`, `위법`, and `법률확정`; then trace the May 16 return-reasons document and June 21 presidential/cabinet promulgation record. Do not collapse institutional acts into direct presidential orders without documentary evidence.
