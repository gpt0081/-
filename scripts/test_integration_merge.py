#!/usr/bin/env python3
"""Focused regression tests for conservative integration merges."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from integration_merge import safe_merge_variants, existing_status_is_more_mature, extract_additional_registry_collections


def alt(data, path):
    return {"data": data, "provenance": [{"path": path, "pointer": "/"}]}


def test_politician_additive_and_conservative():
    rows = [
        alt({"id": "pol-test", "name": "홍길동", "hanja": "洪吉童",
             "lifespan": {"born": "1900", "died": "1970", "verification": "연도 확인"},
             "roles": ["국회의원"], "researchStatus": "VERIFIED",
             "openLead": "원관보 확인"}, "data/politicians/a.json"),
        alt({"id": "pol-test", "name": "홍길동", "hanja": "洪吉童",
             "lifespan": {"born": "1900-03-02", "died": "1970-04-01", "verification": "일자 확인"},
             "roles": ["내무부 장관"], "researchStatus": "IDENTIFIED",
             "openLeads": ["임명 원문"]}, "data/politicians/b.json")
    ]
    merged, reason = safe_merge_variants("politicians", "pol-test", rows)
    assert reason is None and merged
    data = merged["data"]
    assert data["name"] == "홍길동"
    assert data["lifespan"]["born"] == "1900-03-02"
    assert data["lifespan"]["died"] == "1970-04-01"
    assert data["researchStatus"] == "IDENTIFIED"
    assert set(data["roles"]) == {"국회의원", "내무부 장관"}
    assert merged["fieldVariantCount"] >= 2
    assert len(merged["provenance"]) == 2


def test_birth_conflict_is_blocked():
    rows = [
        alt({"id": "pol-test", "name": "홍길동", "lifespan": {"born": "1898"}}, "a.json"),
        alt({"id": "pol-test", "name": "홍길동", "lifespan": {"born": "1899"}}, "b.json")
    ]
    merged, reason = safe_merge_variants("politicians", "pol-test", rows)
    assert merged is None and reason == "CONFLICTING_BIRTH_DATES"


def test_hanja_conflict_is_blocked():
    rows = [
        alt({"id": "pol-test", "name": "홍길동", "hanja": "洪吉童"}, "a.json"),
        alt({"id": "pol-test", "name": "홍길동", "hanja": "洪吉東"}, "b.json")
    ]
    merged, reason = safe_merge_variants("politicians", "pol-test", rows)
    assert merged is None and reason == "CONFLICTING_HANJA_VARIANTS"


def test_document_shared_number_and_url():
    rows = [
        alt({"documentNumber": "법률 제388호", "title": "관보 1591호 법률388 지방자치법",
             "url": "https://example.org/law/388"}, "a.json"),
        alt({"document_number": "법률388", "title": "법률388 지방자치법 개정",
             "url": "https://example.org/law/388"}, "b.json")
    ]
    merged, reason = safe_merge_variants("documents", "DOC-388", rows)
    assert reason is None and merged
    assert merged["data"]["id"] == "DOC-388"
    assert merged["data"]["url"] == "https://example.org/law/388"


def test_document_number_conflict_is_blocked():
    rows = [
        alt({"documentNumber": "법률 제388호", "title": "지방자치법"}, "a.json"),
        alt({"documentNumber": "법률 제389호", "title": "지방자치법"}, "b.json")
    ]
    merged, reason = safe_merge_variants("documents", "DOC-X", rows)
    assert merged is None and reason == "CONFLICTING_DOCUMENT_NUMBERS"


def test_claim_requires_shared_statement():
    rows = [
        alt({"statement": "국회에서 법률안이 가결됐다."}, "a.json"),
        alt({"statement": "국회에서 법률안이 부결됐다."}, "b.json")
    ]
    merged, reason = safe_merge_variants("claims", "CLM-X", rows)
    assert merged is None and reason == "NO_COMMON_CLAIM_STATEMENT"


def test_event_date_identity_and_variant_preservation():
    rows = [
        alt({"date": "1949-06-06", "description": "특별위원회 경찰 진입"}, "a.json"),
        alt({"date": "1949-06-06", "description": "경찰의 특별위원회 급습"}, "b.json")
    ]
    merged, reason = safe_merge_variants("events", "evt-1949-06-06-test", rows)
    assert reason is None and merged
    assert "description" not in merged["data"]
    assert any(row["fieldPath"] == "description" for row in merged["fieldVariants"])


def test_event_date_conflict_is_blocked():
    rows = [
        alt({"date": "1953-06", "description": "로버트슨 사절단"}, "a.json"),
        alt({"date": "1953-07", "description": "로버트슨 사절단"}, "b.json")
    ]
    merged, reason = safe_merge_variants("events", "evt-robertson-mission", rows)
    assert merged is None and reason == "CONFLICTING_EVENT_DATES"


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items())
             if name.startswith("test_") and callable(value)]
    for test_case in tests:
        test_case()
    print({"tests": len(tests), "status": "PASS"})

def test_existing_higher_status_is_preserved_without_auto_promotion():
    assert existing_status_is_more_mature("ANNALS_ACTIVE", "DISCOVERED")
    assert existing_status_is_more_mature("VERIFIED", "IDENTIFIED")
    assert not existing_status_is_more_mature("DISCOVERED", "ANNALS_ACTIVE")
    assert not existing_status_is_more_mature("VERIFIED", "VERIFIED")


def test_extract_legacy_document_sources_metadata_and_nested_event():
    obj = {
        "sources": [
            {"id": "d150-test-source", "url": "https://example.invalid/source"},
            {"id": "not-a-document", "note": "no title, URL, or location"},
        ],
        "metadataOnly": [
            {"id": "d152-test-law", "number": 436, "date": "1957-02-14", "title": "농업협동조합법"},
        ],
        "additionalEvent": {
            "id": "evt-r150-test-election",
            "date": "1956-08-13",
            "name": "1956 시·도의회 의원 선거",
        },
    }
    extracted = extract_additional_registry_collections(obj, {"documents", "events"})
    by_field = {field: rows for kind, field, rows in extracted}
    assert by_field["sources"][0]["id"] == "d150-test-source"
    assert len(by_field["sources"]) == 1
    assert by_field["metadataOnly"][0]["id"] == "d152-test-law"
    assert by_field["additionalEvent"][0]["id"] == "evt-r150-test-election"
    assert extract_additional_registry_collections(obj, {"events"}) == [
        ("events", "additionalEvent", [obj["additionalEvent"]])
    ]
