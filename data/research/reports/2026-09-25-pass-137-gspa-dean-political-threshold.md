# Pass 137 — GSPA governance actors cross the state-actor threshold

## Why this pass

Pass 136 left the first GSPA deans as an institutional leadership spine but explicitly required independent career reconstruction before politician-registry promotion. This pass tested that threshold rather than assuming that a dean was a political actor.

## Shin Tae-hwan (申泰煥)

The Academy of Korean Studies' *Encyclopedia of Korean Culture* identifies Shin Tae-hwan (1912–1993) as an economist and educator who served at SNU Law College, later became SNU president, and also held national executive/policy offices including **Minister of Reconstruction in 1961** and **the first Minister of National Unification**. It additionally records service on the Bank of Korea monetary-policy body and several economic-policy advisory bodies.

This is enough to change his graph status. He should no longer remain merely an `IDENTIFIED` GSPA dean with an open politician threshold. He qualifies as a verified senior-state/cabinet actor and should eventually receive an independent politician registry node and annals thread.

The finding does **not** prove that Shin authored the January 1959 Presidential Decree establishing GSPA, designed admissions, or wrote the curriculum. His first-dean office and later cabinet offices are distinct evidence claims.

## Lee Byeong-do (李丙燾)

The same encyclopedia series records Lee Byeong-do (1896–1989) as an SNU historian who served for four years as chair of the Ministry of National Defense war-history compilation committee and, after the April Revolution, entered the transitional cabinet as **Minister of Education in 1960**. This independently clears the cabinet-actor threshold for the person who Pass 136 identified as acting GSPA dean from 1960-09-20 to 1961-03-31.

A Korea Democracy Foundation chronology supplies a concrete ministerial-action lead: on **1960-06-23**, Lee publicly argued that the teachers union should be dissolved; union representatives responded that their organization was lawful and issued a recommendation that he resign. The chronology points onward to contemporary *Chosun Ilbo* and *Dong-A Ilbo* pages. Those underlying newspapers and the ministry's directive/legal opinion remain the next evidentiary targets.

This creates a useful person-centered cross-link: the same individual appears in academic governance, cabinet education policy, and an earlier Defense Ministry historical-record role. These must remain separate role/event edges rather than being collapsed into one political label.

## Adversarial result

The actor-threshold question is now narrower, but authorship and legal-authority questions remain open. A ministerial biography does not prove responsibility for every act of a ministry, and a deanship does not prove authorship of a university decree. Exact appointment instruments, cabinet minutes, ministry circulars, GSPA minutes and the 1959/1961 legal instruments are still required for fine-grained attribution.

The June 1960 teachers-union conflict also should **not** be modeled as a GSPA event. It belongs to Lee Byeong-do's independent person node and education-policy event graph, with a cross-link to his later/parallel university governance role.

## Immediate graph consequences

- Shin Tae-hwan: `IDENTIFIED / politician threshold OPEN` → `VERIFIED / QUALIFIES_SENIOR_STATE_ACTOR`.
- Lee Byeong-do: `IDENTIFIED / politician threshold OPEN` → `VERIFIED / QUALIFIES_CABINET_ACTOR`.
- New event candidate: `evt-1960-teachers-union-dispute`, pending recovery of ministry and contemporary primary records.
- GSPA founding decree authorship remains OPEN.
- GSPA March 1961 separation/independence authority remains OPEN.

## Sources directly inspected

1. Academy of Korean Studies, *Encyclopedia of Korean Culture*, “신태환”.
2. Academy of Korean Studies, *Encyclopedia of Korean Culture*, “이병도”.
3. Korea Democracy Foundation chronology, 1960-06-23, “이병도 문교부장관 ‘교원노동조합 해체해야’”.
4. Academy of Korean Studies, “한국경제학회”, used to cross-check Shin's early economics-network role.
5. National Institute of Korean History modern-source index result used as a name-collision warning: an 1873-born 申泰煥 exists in the person DB and must not be conflated with the 1912-born economist.

The fifth item is a useful negative control. Name-only historical-database searches can return a different 申泰煥, so future automated ingestion must bind birth year/career context before linking records.

## Execution note

This was a focused continuation pass, not a claim that the full hourly lower bounds were met. Five meaningful source pages/records were inspected in this pass, with four high-value actor/network findings and more than thirty concrete next-document targets recorded in the candidate ledger. The lower bound of 40 directly opened documents was **not** reached in this execution window. No number is inflated to compensate.

History-debt weekly full review not performed; this is Friday in Asia/Seoul, so the Sunday-first-run rule does not trigger.

Floot was not modified or built.