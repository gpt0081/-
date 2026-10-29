# Pass257O5 correction/review history (2026-10-29T11:28:25.582Z)

- Original Pass257O4 documents shard repeated two existing document registry IDs (DOC-P239K-UN-A2711 and DOC-P239K-NEC-1954-ELECTION) despite existing_registry_reuse markers. Removed duplicate objects; retained existing_document_ids_reused references and all claim/event edges. No source deleted from original pass239k registry.
- Original new Choi Soon-joo candidate included unverified hanja alias while explicitly saying unverified. Removed that alias rather than asserting it.
- Corrected pass257O4 run report actor count to 17 distinct nonpresident IDs (13 previous + 4 new).
- This correction is explicitly logged; no silent overwrite of historical claim evidence or debt status. All previous commits remain in Git history.
