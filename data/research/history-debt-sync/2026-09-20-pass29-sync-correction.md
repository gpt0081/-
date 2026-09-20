# HISTORY_DEBT sync correction — 2026-09-20

Status: PENDING-MERGE-INTO-CANONICAL-LEDGER

Pass 29 recorded that the Sunday 2026-09-20 Asia/Seoul weekly full sweep was performed against unresolved HD-RHEE-002 through HD-RHEE-012, while canonical `data/research/HISTORY_DEBT.md` still carries `last_full_review: 2026-09-19`; this is a synchronization defect, not evidence that a second sweep is required.

Canonical merge requirements:
- set `last_full_review: 2026-09-20` after preserving the Pass 29 run report as provenance;
- HD-RHEE-003 remains NARROWED, adding regional execution evidence from Truth and Reconciliation Commission materials while leaving the central first kill-order sender unresolved;
- HD-RHEE-008 should be promoted OPEN → NARROWED because the 1959-04-30 22:15 formal delivery of the publication-permit cancellation and the Public Information Office's five stated grounds are identified, while Blue House approval/directive remains unresolved;
- HD-RHEE-010 remains NARROWED, adding the O Ik-gyeong → Han Dong-seok → Yi Jong-dae/Pak Jong-yeong operational chain reported in contemporaneous prosecution/court material, without inferring prior Defense Ministry/Blue House approval;
- HD-RHEE-011 remains NARROWED, adding the Interior Ministry ↔ Liberal Party planning/execution evidence and keeping presidential prior approval of specific illegal methods unresolved;
- do not reopen HD-RHEE-001 absent new contradictory evidence;
- do not silently overwrite conflicting testimony; preserve source stage (suspect statement, prosecution allegation, judicial finding, contemporaneous foreign observation, later official finding).

This correction file exists because a safe full rewrite of the canonical ledger was not available in the connector response; it prevents the mismatch from being forgotten or falsely treated as a new historical finding.
