#!/usr/bin/env python3
"""Conservative field-wise merger for repeated stable IDs.

Original alternatives remain in the lossless registry. This helper only creates a
queryable merged projection when the same stable ID has a shared identity key.
Conflicting scalar values are omitted from the projection and retained with
source provenance in fieldVariants; no last-write-wins selection is used.
"""
import copy
import hashlib
import json
import re

MERGE_POLICY = (
    "SAME_STABLE_ID_AND_SHARED_IDENTITY_KEY; ADDITIVE_ARRAYS; "
    "AMBIGUOUS_SCALARS_OMITTED_WITH_PROVENANCE; CONSERVATIVE_STATUS; "
    "DATE_PRECISION_REFINED_ONLY_WITHIN_SAME_CALENDAR_POINT"
)

NAME_FIELDS = {
    "name", "name_ko", "nameKo", "displayName", "display_name",
    "name_en", "nameEn", "english", "romanization", "romanized",
    "hanja", "name_hanja", "nameHanja"
}
PERSON_NAME_FIELDS = {
    "name", "name_ko", "nameKo", "displayName", "display_name",
    "name_en", "nameEn", "english", "romanization", "romanized"
}
STATUS_FIELDS = {
    "researchStatus", "research_status", "status",
    "researchMaturity", "research_maturity"
}
DATE_FIELDS = {
    "date", "startDate", "start_date", "endDate", "end_date",
    "dateRange", "date_range", "issuedDate", "issued_date",
    "publicationDate", "publication_date", "born", "birth",
    "birthYear", "dateOfBirth", "date_of_birth", "died", "death",
    "deathYear", "dateOfDeath", "date_of_death"
}
LIST_FIELDS = {
    "aliases", "aliasesAdditional", "aliases_additional",
    "roles", "periodRoles", "period_roles", "rolesByPeriod", "roles_by_period",
    "offices", "affiliations", "partyAffiliations", "party_affiliation",
    "events", "eventIds", "event_ids", "linkedEventIds", "linked_event_ids",
    "eventLinks", "event_links", "eventConnections", "event_connections",
    "documentIds", "document_ids", "linkedDocumentIds", "linked_document_ids",
    "evidenceDocumentIds", "evidence_document_ids", "evidenceIds", "evidence_ids",
    "claimIds", "claim_ids", "organizationIds", "organization_ids",
    "roleIds", "role_ids", "politicianIds", "politician_ids",
    "actorIds", "actor_ids", "relatedEventIds", "related_event_ids",
    "relatedDocumentIds", "related_document_ids", "relatedClaimIds", "related_claim_ids",
    "relatedPoliticianIds", "related_politician_ids",
    "relatedOrganizationIds", "related_organization_ids",
    "relatedRoleIds", "related_role_ids",
    "supportingDocumentIds", "supporting_document_ids",
    "contradictingDocumentIds", "contradicting_document_ids",
    "openLeads", "open_leads", "historyDebtIds", "history_debt_ids",
    "researchRefs", "research_refs", "connections", "actions",
    "actionTypes", "action_types", "evidence", "sources",
    "proposedBy", "proposed_by", "decidedBy", "decided_by",
    "executedBy", "executed_by", "opposedBy", "opposed_by",
    "legalAuthority", "legal_authority", "observedBy", "observed_by",
    "laterFinding", "later_finding", "nameVariants", "name_variants",
    "titleVariants", "title_variants", "sourceLocations", "source_locations"
}
FILE_LIST_FIELDS = {
    "evidenceFile": "evidenceFiles",
    "annalsFile": "annalsFiles",
    "coverageFile": "coverageFiles",
    "openLeadsFile": "openLeadsFiles"
}
SINGULAR_LEAD_FIELDS = {"openLead": "openLeads", "open_lead": "open_leads"}
STATUS_RANK = {
    "DISCOVERED": 0,
    "IDENTIFIED": 1,
    "VERIFIED": 2,
    "ANNALS_ACTIVE": 3,
    "MATURE": 4
}
OMIT = object()


def _stable(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _norm(value):
    return "".join(ch.lower() for ch in str(value or "") if ch.isalnum())


def _strings(value):
    if isinstance(value, str):
        return [value] if value.strip() else []
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return [str(value)]
    if isinstance(value, dict):
        result = []
        for key in ("ko", "name_ko", "nameKo", "en", "english", "name_en", "nameEn"):
            item = value.get(key)
            if isinstance(item, str) and item.strip():
                result.append(item)
        if not result:
            result.extend(v for v in value.values() if isinstance(v, str) and v.strip())
        return result
    if isinstance(value, list):
        result = []
        for item in value:
            result.extend(_strings(item))
        return result
    return []


def _unique_strings(values):
    seen = set()
    result = []
    for value in values:
        if not isinstance(value, str) or not value.strip():
            continue
        key = _norm(value)
        if key and key not in seen:
            seen.add(key)
            result.append(value.strip())
    return result


def _common_key(variants, keys, include_aliases=False):
    sets = []
    for row in variants:
        values = []
        for key in keys:
            values.extend(_strings(row.get(key)))
        if include_aliases:
            values.extend(_strings(row.get("aliases")))
            values.extend(_strings(row.get("aliasesAdditional")))
            values.extend(_strings(row.get("aliases_additional")))
        normalized = {_norm(value) for value in values if _norm(value)}
        if normalized:
            sets.append(normalized)
    if not sets:
        return None
    common = set.intersection(*sets)
    if not common:
        return None
    return sorted(common, key=lambda item: (0 if re.search(r"[\uac00-\ud7a3]", item) else 1, -len(item), item))[0]


def _display_for_key(variants, key):
    candidates = []
    for row in variants:
        for field in PERSON_NAME_FIELDS:
            candidates.extend(_strings(row.get(field)))
        candidates.extend(_strings(row.get("aliases")))
    candidates = [value for value in candidates if _norm(value) == key]
    if not candidates:
        return key
    candidates.sort(key=lambda value: (
        0 if re.search(r"[\uac00-\ud7a3]", value) else 1,
        -len(value),
        value.lower()
    ))
    return candidates[0]


def _date_parts(value):
    text = str(value or "").strip()
    match = re.fullmatch(r"(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?", text)
    if not match:
        return None
    year, month, day = match.groups()
    return (year, month, day, 1 + bool(month) + bool(day))


def _merge_dates(values):
    raw = _unique_strings([str(value) for value in values if value is not None and str(value).strip()])
    if not raw:
        return None, True
    if len(raw) == 1:
        return raw[0], True
    parsed = [_date_parts(value) for value in raw]
    if any(item is None for item in parsed):
        if len({_norm(value) for value in raw}) == 1:
            return raw[0], True
        return None, False
    years = {item[0] for item in parsed}
    months = {item[1] for item in parsed if item[1]}
    days = {item[2] for item in parsed if item[2]}
    if len(years) > 1 or len(months) > 1 or len(days) > 1:
        return None, False
    best_precision = max(item[3] for item in parsed)
    best = [raw[index] for index, item in enumerate(parsed) if item[3] == best_precision]
    if len({_norm(value) for value in best}) > 1:
        return None, False
    return sorted(best, key=lambda value: (len(value), value), reverse=True)[0], True


def _collect_dates(variants, top_keys, nested_keys=()):
    values = []
    for row in variants:
        for key in top_keys:
            values.extend(_strings(row.get(key)))
        nested = row.get("lifespan")
        if isinstance(nested, dict):
            for key in nested_keys:
                values.extend(_strings(nested.get(key)))
    return values


def _id_aliases(variants):
    fields = ("id", "candidateId", "candidate_id", "politicianId",
              "politician_id", "stableId", "stable_id")
    return [value for row in variants for key in fields for value in _strings(row.get(key))]


def _document_number_key(value):
    text = str(value or "").strip()
    clean = re.sub(r"\.[A-Za-z0-9]+$", "", text)
    match = re.search(r"(\d+)(?:[-_ ]*([A-Za-z]+))?$", clean)
    if match:
        return match.group(1) + (match.group(2) or "").lower()
    digits = re.findall(r"\d+", text)
    if digits:
        return digits[-1]
    return _norm(text)


def _identity_basis(kind, ident, variants):
    if kind == "politicians":
        common = _common_key(variants, PERSON_NAME_FIELDS, include_aliases=True)
        if not common:
            return None, "NO_COMMON_PERSON_NAME_OR_ALIAS"
        hanja = {_norm(value) for row in variants for key in ("hanja", "name_hanja", "nameHanja")
                 for value in _strings(row.get(key)) if _norm(value)}
        if len(hanja) > 1:
            return None, "CONFLICTING_HANJA_VARIANTS"
        aliases = _id_aliases(variants)
        if any(value != ident for value in aliases):
            return None, "CONFLICTING_STABLE_ID_ALIAS"
        birth = _collect_dates(
            variants,
            ("birth", "birthYear", "born", "dateOfBirth", "date_of_birth"),
            ("born", "birth", "birthYear", "dateOfBirth", "date_of_birth")
        )
        death = _collect_dates(
            variants,
            ("death", "deathYear", "died", "dateOfDeath", "date_of_death"),
            ("died", "death", "deathYear", "dateOfDeath", "date_of_death")
        )
        _, birth_ok = _merge_dates(birth)
        _, death_ok = _merge_dates(death)
        if not birth_ok:
            return None, "CONFLICTING_BIRTH_DATES"
        if not death_ok:
            return None, "CONFLICTING_DEATH_DATES"
        return {
            "basis": "SAME_STABLE_PERSON_ID_AND_SHARED_NAME_OR_ALIAS",
            "identityKey": common,
            "displayName": _display_for_key(variants, common),
            "hanja": sorted(hanja),
        }, None

    if kind == "documents":
        number_values = [
            value for row in variants
            for key in ("documentNumber", "document_number", "docNumber", "doc_number")
            for value in _strings(row.get(key))
        ]
        number_keys = {_document_number_key(value) for value in number_values if _document_number_key(value)}
        if len(number_keys) > 1:
            return None, "CONFLICTING_DOCUMENT_NUMBERS"
        common = _common_key(
            variants,
            ("title", "documentTitle", "document_title", "name",
             "documentNumber", "document_number", "docNumber", "doc_number",
             "originalLocation", "original_location", "url", "sourceUrl", "source_url")
        )
        if not common:
            return None, "NO_COMMON_DOCUMENT_NUMBER_TITLE_OR_ORIGINAL_LOCATION"
        return {"basis": "SAME_STABLE_DOCUMENT_ID_AND_SHARED_DOCUMENT_KEY",
                "identityKey": common}, None

    if kind == "claims":
        common = _common_key(
            variants,
            ("claim", "statement", "proposition", "text", "title", "description")
        )
        if not common:
            return None, "NO_COMMON_CLAIM_STATEMENT"
        return {"basis": "SAME_STABLE_CLAIM_ID_AND_SHARED_STATEMENT",
                "identityKey": common}, None

    if kind == "events":
        common = _common_key(
            variants,
            ("name", "title", "event", "action", "description",
             "eventName", "event_name", "eventTitle", "event_title",
             "actionName", "action_name", "descriptionKo", "description_ko")
        )
        dates = [value for row in variants
                 for key in ("date", "startDate", "start_date", "dateRange", "date_range")
                 for value in _strings(row.get(key))]
        selected_date, date_ok = _merge_dates(dates)
        if dates and not date_ok:
            return None, "CONFLICTING_EVENT_DATES"
        id_date = re.search(r"evt-(\d{4}-\d{2}-\d{2})", ident)
        if not common and not selected_date and not id_date:
            return None, "NO_COMMON_EVENT_NAME_OR_COMPATIBLE_DATE"
        return {"basis": "SAME_STABLE_EVENT_ID_AND_SHARED_NAME_OR_COMPATIBLE_DATE",
                "identityKey": common, "selectedDate": selected_date,
                "eventIdDate": id_date.group(1) if id_date else None}, None

    if kind == "organizations":
        common = _common_key(variants, ("name", "title", "organizationName", "organization_name"))
        if not common:
            return None, "NO_COMMON_ORGANIZATION_NAME"
        return {"basis": "SAME_STABLE_ORGANIZATION_ID_AND_SHARED_NAME",
                "identityKey": common}, None

    if kind == "roles":
        common = _common_key(variants, ("name", "title", "role", "roleName", "role_name"))
        if not common:
            return None, "NO_COMMON_ROLE_NAME_OR_TITLE"
        return {"basis": "SAME_STABLE_ROLE_ID_AND_SHARED_TITLE",
                "identityKey": common}, None

    return None, "UNSUPPORTED_REGISTRY_KIND"


def _provenance_for(alternatives):
    result = []
    seen = set()
    for alternative in alternatives:
        for source in alternative.get("provenance", []):
            key = _stable(source)
            if key not in seen:
                seen.add(key)
                result.append(copy.deepcopy(source))
    return sorted(result, key=lambda row: (str(row.get("path", "")), str(row.get("pointer", ""))))


def _record_field_variant(field_variants, field_path, values, resolution):
    grouped = {}
    for value, provenance in values:
        key = _stable(value)
        if key not in grouped:
            grouped[key] = {"value": copy.deepcopy(value), "provenance": []}
        for source in provenance:
            if source not in grouped[key]["provenance"]:
                grouped[key]["provenance"].append(copy.deepcopy(source))
    if len(grouped) <= 1:
        return
    field_variants.append({
        "fieldPath": field_path,
        "values": sorted(grouped.values(), key=lambda row: _stable(row["value"])),
        "resolution": resolution
    })


def _normalize_status(value):
    text = str(value or "").upper()
    for status in ("MATURE", "ANNALS_ACTIVE", "VERIFIED", "IDENTIFIED", "DISCOVERED"):
        if status in text:
            return status
    return "DISCOVERED"

def existing_status_is_more_mature(existing, incoming):
    """Preserve a stronger existing status; never promote from a weaker source."""
    left = _normalize_status(existing)
    right = _normalize_status(incoming)
    return STATUS_RANK[left] > STATUS_RANK[right]


def extract_additional_registry_collections(obj, allowed_kinds):
    """Extract legacy document arrays and one nested additional event conservatively."""
    if not isinstance(obj, dict):
        return []
    extracted = []
    document_id_fields = ("id", "documentId", "document_id",
                          "candidateDocumentId", "candidate_document_id")
    document_descriptors = ("title", "originalLocation", "original_location", "url",
                            "documentNumber", "document_number")
    if "documents" in allowed_kinds:
        for field in ("sources", "metadataOnly", "metadata_only",
                      "sourceDocuments", "documentSources"):
            items = obj.get(field)
            if not isinstance(items, list):
                continue
            selected = []
            for item in items:
                if not isinstance(item, dict):
                    continue
                ident = next((item.get(key) for key in document_id_fields
                              if isinstance(item.get(key), str) and item.get(key).strip()), None)
                has_descriptor = any(item.get(key) not in (None, "", [], {})
                                     for key in document_descriptors)
                if ident and has_descriptor:
                    selected.append(item)
            if selected:
                extracted.append(("documents", field, selected))
    if "events" in allowed_kinds:
        event = obj.get("additionalEvent")
        if isinstance(event, dict):
            event_id = next((event.get(key) for key in
                             ("id", "eventId", "event_id", "candidateEventId", "candidate_event_id")
                             if isinstance(event.get(key), str) and event.get(key).strip()), None)
            has_descriptor = any(event.get(key) not in (None, "", [], {})
                                 for key in ("date", "title", "name", "description"))
            if event_id and has_descriptor:
                extracted.append(("events", "additionalEvent", [event]))
    return extracted


def _merge_object(objects, provenance_rows, kind, identity, field_variants, prefix=""):
    result = {}
    promoted = {}
    keys = sorted(set().union(*(set(row.keys()) for row in objects if isinstance(row, dict))))
    for key in keys:
        if key in ("id", "_integration"):
            continue
        values = []
        for index, row in enumerate(objects):
            if not isinstance(row, dict) or key not in row:
                continue
            value = row[key]
            if value is None or value == "" or value == [] or value == {}:
                continue
            values.append((value, provenance_rows[index]))
        if not values:
            continue
        field_path = f"{prefix}.{key}" if prefix else key
        merged = _merge_field(key, values, kind, identity, field_variants, field_path)
        if merged is not OMIT:
            result[key] = merged
        elif key in FILE_LIST_FIELDS or key in SINGULAR_LEAD_FIELDS:
            plural = FILE_LIST_FIELDS.get(key) or SINGULAR_LEAD_FIELDS.get(key)
            promoted.setdefault(plural, [])
            for value, _source_provenance in values:
                promoted[plural].extend(_strings(value))
    for plural, values in promoted.items():
        combined = list(result.get(plural, [])) if isinstance(result.get(plural), list) else []
        seen = {_stable(value) for value in combined}
        for value in values:
            if value not in (None, "") and _stable(value) not in seen:
                combined.append(value)
                seen.add(_stable(value))
        if combined:
            result[plural] = combined
    return result


def _merge_field(key, values, kind, identity, field_variants, field_path):
    raw_values = [value for value, _ in values]
    if all(_stable(value) == _stable(raw_values[0]) for value in raw_values[1:]):
        return copy.deepcopy(raw_values[0])

    if key in LIST_FIELDS:
        flattened = []
        seen = set()
        for value in raw_values:
            items = value if isinstance(value, list) else [value]
            for item in items:
                marker = _stable(item)
                if marker not in seen:
                    seen.add(marker)
                    flattened.append(copy.deepcopy(item))
        return flattened

    if key in FILE_LIST_FIELDS:
        plural = FILE_LIST_FIELDS[key]
        flattened = []
        for value in raw_values:
            flattened.extend(_strings(value))
        if flattened:
            _record_field_variant(field_variants, field_path, values,
                                  "MOVED_TO_ADDITIVE_" + plural.upper())
        return OMIT

    if key in SINGULAR_LEAD_FIELDS:
        plural = SINGULAR_LEAD_FIELDS[key]
        flattened = []
        for value in raw_values:
            flattened.extend(_strings(value))
        if flattened:
            _record_field_variant(field_variants, field_path, values,
                                  "MOVED_TO_ADDITIVE_" + plural.upper())
        return OMIT

    if key in NAME_FIELDS:
        strings = _unique_strings([item for value in raw_values for item in _strings(value)])
        if kind == "politicians" and key == "name" and identity.get("displayName"):
            _record_field_variant(field_variants, field_path, values,
                                  "NORMALIZED_TO_SHARED_PERSON_NAME")
            return identity["displayName"]
        if len({_norm(value) for value in strings}) == 1 and strings:
            selected = strings[0]
            _record_field_variant(field_variants, field_path, values,
                                  "NORMALIZED_EQUIVALENT_NAME_VARIANT")
            return selected
        _record_field_variant(field_variants, field_path, values,
                              "PRESERVED_WITHOUT_CANONICAL_NAME_SELECTION")
        return OMIT

    if key in STATUS_FIELDS:
        statuses = [_normalize_status(value) for value in raw_values if isinstance(value, str)]
        if statuses:
            selected = min(statuses, key=lambda value: STATUS_RANK[value])
            _record_field_variant(field_variants, field_path, values,
                                  "CONSERVATIVE_MINIMUM_RESEARCH_STATUS")
            return selected

    if key in DATE_FIELDS:
        date_values = [item for value in raw_values for item in _strings(value)]
        selected, compatible = _merge_dates(date_values)
        if compatible and selected is not None:
            _record_field_variant(field_variants, field_path, values,
                                  "NONCONFLICTING_DATE_PRECISION_REFINEMENT")
            return selected
        _record_field_variant(field_variants, field_path, values,
                              "PRESERVED_WITHOUT_CANONICAL_DATE_SELECTION")
        return OMIT

    if all(isinstance(value, dict) for value in raw_values):
        nested_objects = raw_values
        nested_provenance = [prov for _, prov in values]
        merged = _merge_object(nested_objects, nested_provenance, kind,
                               identity, field_variants, field_path)
        return merged if merged else OMIT

    if all(isinstance(value, list) for value in raw_values):
        flattened = []
        seen = set()
        for value in raw_values:
            for item in value:
                marker = _stable(item)
                if marker not in seen:
                    seen.add(marker)
                    flattened.append(copy.deepcopy(item))
        return flattened

    _record_field_variant(field_variants, field_path, values,
                          "PRESERVED_WITHOUT_CANONICAL_SCALAR_SELECTION")
    return OMIT


def safe_merge_variants(kind, ident, alternatives):
    """Return (safe_merge, blocked_reason); safe_merge is None when review is required."""
    if not isinstance(alternatives, list) or len(alternatives) < 2:
        return None, "NOT_A_MULTI_VARIANT_RECORD"
    variants = [row.get("data", {}) for row in alternatives]
    if not all(isinstance(row, dict) for row in variants):
        return None, "NON_OBJECT_ALTERNATIVE"
    identity, reason = _identity_basis(kind, ident, variants)
    if not identity:
        return None, reason
    provenance_rows = [row.get("provenance", []) for row in alternatives]
    field_variants = []
    merged_data = _merge_object(variants, provenance_rows, kind, identity, field_variants)
    merged_data["id"] = ident
    if kind == "politicians" and not merged_data.get("name"):
        merged_data["name"] = identity["displayName"]
    merged_data = {key: merged_data[key] for key in sorted(merged_data)}
    provenance = _provenance_for(alternatives)
    digest = hashlib.sha256(_stable(merged_data).encode("utf-8")).hexdigest()
    field_variants.sort(key=lambda row: row["fieldPath"])
    return {
        "status": "SAFE_FIELDWISE_MERGE",
        "mergePolicy": MERGE_POLICY,
        "identityBasis": identity,
        "data": merged_data,
        "digest": digest,
        "provenance": provenance,
        "fieldVariantCount": len(field_variants),
        "fieldVariants": field_variants,
        "sourceVariantCount": len(alternatives)
    }, None
