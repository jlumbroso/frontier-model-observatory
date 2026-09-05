#!/usr/bin/env python3
"""Generate deterministic, cross-linked JSONL examples from calibration facts."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "tests" / "fixtures" / "schema" / "all-records.jsonl"
STAMP = "2026-09-05T07:00:00Z"
OBS = {"first_observed": {"value": "2026-09-05", "precision": "day", "basis": "retrieval"}}
OPEN_2026 = {"status": "open", "start": {"value": "2026", "precision": "year", "basis": "artifact_body"}}

U = {
    "org": "fmo:org:00000000-0000-4000-8000-000000000001",
    "family": "fmo:family:00000000-0000-4000-8000-000000000002",
    "model": "fmo:model:00000000-0000-4000-8000-000000000003",
    "checkpoint": "fmo:checkpoint:00000000-0000-4000-8000-000000000004",
    "configuration": "fmo:configuration:00000000-0000-4000-8000-000000000005",
    "product": "fmo:product:00000000-0000-4000-8000-000000000006",
    "deployment": "fmo:deployment:00000000-0000-4000-8000-000000000007",
    "endpoint": "fmo:endpoint:00000000-0000-4000-8000-000000000008",
    "alias": "fmo:alias:00000000-0000-4000-8000-000000000009",
    "artifact": "fmo:artifact:00000000-0000-4000-8000-000000000010",
    "version": "fmo:artifact-version:00000000-0000-4000-8000-000000000011",
    "artifact2": "fmo:artifact:00000000-0000-4000-8000-000000000012",
    "version2": "fmo:artifact-version:00000000-0000-4000-8000-000000000013",
    "url1": "fmo:url:00000000-0000-4000-8000-000000000014",
    "url2": "fmo:url:00000000-0000-4000-8000-000000000015",
    "retrieval": "fmo:retrieval:00000000-0000-4000-8000-000000000016",
    "redirect": "fmo:redirect:00000000-0000-4000-8000-000000000017",
    "part": "fmo:part:00000000-0000-4000-8000-000000000018",
    "relationship": "fmo:artifact-relationship:00000000-0000-4000-8000-000000000019",
    "claim1": "fmo:claim:00000000-0000-4000-8000-000000000020",
    "claim2": "fmo:claim:00000000-0000-4000-8000-000000000021",
    "event": "fmo:event:00000000-0000-4000-8000-000000000022",
    "absence": "fmo:absence:00000000-0000-4000-8000-000000000023",
    "coverage": "fmo:coverage:00000000-0000-4000-8000-000000000024"
}

def env(record_type, ident, key):
    return {"schema_version": "1.0.0", "record_type": record_type, "id": ident,
            "canonical_key": key, "recorded_at": STAMP, "record_status": "active"}

def entity(kind, ident, key, name, **extra):
    d = env("entity", ident, key)
    d.update({"kind": kind, "preferred_name": name,
              "names": [{"value": name, "name_type": "provider_preferred"}],
              "observed_time": OBS})
    d.update(extra)
    return d

records = [
    entity("organization", U["org"], "google-deepmind", "Google DeepMind",
           roles=["provider", "publisher"]),
    entity("model_family", U["family"], "gemini-robotics", "Gemini Robotics",
           provider_org_id=U["org"]),
    entity("model", U["model"], "gemini-robotics-1-5", "Gemini Robotics 1.5",
           provider_org_id=U["org"], family_id=U["family"],
           modalities=[{"native": "robot camera images", "normalized": "robotics"}]),
    entity("checkpoint", U["checkpoint"], "gemini-robotics-1-5-ga", "Gemini Robotics 1.5 general availability",
           model_id=U["model"], stage="general_availability"),
    entity("configuration", U["configuration"], "gemini-robotics-1-5-camera-input", "robot camera image input",
           configures_id=U["model"], configuration_class="input_modality"),
    entity("product", U["product"], "vertex-ai", "Vertex AI", provider_org_id=U["org"]),
    entity("deployment", U["deployment"], "vertex-ai/gemini-robotics-1-5", "Gemini Robotics 1.5 on Vertex AI",
           product_id=U["product"], model_id=U["model"], checkpoint_id=U["checkpoint"],
           configuration_ids=[U["configuration"]], valid_time=OPEN_2026),
    entity("endpoint", U["endpoint"], "gemini-api", "Gemini API", provider_org_id=U["org"],
           product_id=U["product"], endpoint_class="api"),
    entity("alias", U["alias"], "alias/gemini-robotics-1-5", "Gemini Robotics 1.5 provider label",
           alias_value="Gemini Robotics 1.5", alias_type="marketing_name",
           target_id=U["model"], valid_time=OPEN_2026),
]

a = env("artifact", U["artifact"], "google/gemini-robotics-1-5-technical-report")
a.update({"preferred_title": "Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots",
          "publisher_org_ids": [U["org"]], "artifact_class": "technical_report",
          "native_artifact_type": {"native": "technical report", "normalized": "technical_report"},
          "subject_refs": [{"subject_id": U["model"], "scope_role": "primary"}],
          "observed_time": OBS, "officiality": "provider_published", "corpus_partition": "main",
          "redistribution_status": "review_required", "current_version_ids": [U["version"]]})
records.append(a)

v = env("artifact_version", U["version"], "google/gemini-robotics-1-5-technical-report/v1")
v.update({"artifact_id": U["artifact"], "version_ordinal": 1,
          "title_native": "Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots",
          "representation_kinds": ["pdf"], "date_assertions": [
              {"date_role": "index_listed", "value": {"value": "2025-09-25", "precision": "day", "basis": "index_surface"}},
              {"date_role": "transport_last_modified", "value": {"value": "2025-09-25", "precision": "day", "basis": "transport_header"}}
          ], "observed_time": OBS, "lifecycle": "current",
          "byte_object_ids": ["fmo:sha256:" + "0" * 64], "url_alias_ids": [U["url2"]], "page_count": 62})
records.append(v)

a2 = env("artifact", U["artifact2"], "google/gemini-robotics-1-5-model-card-part")
a2.update({"preferred_title": "Appendix A. Model Card", "publisher_org_ids": [U["org"]],
           "artifact_class": "model_disclosure",
           "native_artifact_type": {"native": "model card (Mitchell et al., 2019)", "normalized": "model_disclosure"},
           "subject_refs": [{"subject_id": U["model"], "scope_role": "primary"}],
           "observed_time": OBS, "officiality": "provider_published", "corpus_partition": "main",
           "redistribution_status": "review_required", "current_version_ids": [U["version2"]]})
records.append(a2)

v2 = env("artifact_version", U["version2"], "google/gemini-robotics-1-5-model-card-part/v1")
v2.update({"artifact_id": U["artifact2"], "version_ordinal": 1, "title_native": "Appendix A. Model Card",
           "representation_kinds": ["document_part"], "date_assertions": [],
           "dates_unreported_reason": "The card is an appendix inside the report.",
           "observed_time": OBS, "lifecycle": "current"})
records.append(v2)

records.append({"schema_version": "1.0.0", "record_type": "byte_object",
                "id": "fmo:sha256:" + "0" * 64, "recorded_at": STAMP, "record_status": "active",
                "sha256": "0" * 64, "byte_length": 41523609,
                "media_type_detected": "application/pdf",
                "storage": {"backend": "external_only", "availability": "remote_only"},
                "observed_time": OBS, "derivation": "provider_original"})

for ident, key, url, role, target in [
    (U["url1"], "url/deepmind/gemini-robotics-1-5", "https://deepmind.google/models/model-cards/gemini-robotics-1-5/", "vanity", U["artifact2"]),
    (U["url2"], "url/storage/gemini-robotics-1-5-report", "https://storage.googleapis.com/deepmind-media/gemini-robotics/Gemini-Robotics-1-5-Tech-Report.pdf", "asset", U["version"])
]:
    d = env("url_alias", ident, key)
    d.update({"url": url, "url_normalized": url, "url_role": role,
              "target_refs": [{"id": target, "record_type": "artifact" if target == U["artifact2"] else "artifact_version"}],
              "observed_time": OBS, "host_org_id": U["org"], "is_provider_controlled": True,
              "canonicality": "alias", "lifecycle": "active"})
    records.append(d)

r = env("retrieval_event", U["retrieval"], "retrieval/gemini-robotics-1-5/2026-09-05")
r.update({"requested_url_id": U["url1"], "final_url_id": U["url2"],
          "retrieved_at": {"value": "2026-09-05", "precision": "day", "basis": "retrieval"},
          "method": "http_get", "agent": "calibration research session", "outcome": "redirected_success",
          "cache_status": "live", "status_code": 200, "redirect_observation_ids": [U["redirect"]],
          "byte_object_id": "fmo:sha256:" + "0" * 64})
records.append(r)

rd = env("redirect_observation", U["redirect"], "redirect/gemini-robotics-1-5/2026-09-05/0")
rd.update({"retrieval_event_id": U["retrieval"], "hop_index": 0, "from_url_id": U["url1"],
           "to_url_id": U["url2"], "mechanism": "http", "status_code": 301,
           "observed_time": OBS, "is_terminal": True})
records.append(rd)

p = env("artifact_part", U["part"], "google/gemini-robotics-1-5-report/appendix-a-table-2")
p.update({"artifact_version_id": U["version"], "part_kind": "appendix",
          "locator": {"page_range": {"scheme": "pdf_index", "start": 30, "end": 30}, "table": "Table 2"},
          "label_native": "Appendix A. Model Card", "subject_ids": [U["model"]],
          "byte_object_id": "fmo:sha256:" + "0" * 64, "artifact_class_override": "model_disclosure",
          "observed_time": OBS})
records.append(p)

rel = env("artifact_relationship", U["relationship"], "relationship/model-card-part-of-robotics-report")
rel.update({"source_ref": {"id": U["artifact2"], "record_type": "artifact"},
            "target_ref": {"id": U["artifact"], "record_type": "artifact"},
            "relationship_type": "part_of", "relationship_type_native": "Appendix A. Model Card",
            "valid_time": {"status": "known", "start": {"value": "2025-09-25", "precision": "day", "basis": "index_surface"}},
            "observed_time": OBS,
            "evidence": [{"artifact_version_id": U["version"], "artifact_part_id": U["part"], "page": 30}]})
records.append(rel)

c1 = env("claim", U["claim1"], "claim/gemini-robotics-1-5/model-card-location")
c1.update({"claim_kind": "assertion", "subject_refs": [{"id": U["model"], "record_type": "entity"}],
           "predicate": {"native": "model card location", "normalized": "documented_in_part"},
           "object": {"type": "artifact_ref", "value": U["part"]},
           "statement_native": "Appendix A. Model Card", "attribution": {"actor_type": "publisher", "actor_org_id": U["org"]},
           "epistemic_status": "stated", "lifecycle": "current",
           "valid_time": {"status": "open", "start": {"value": "2025-09-25", "precision": "day", "basis": "index_surface"}},
           "observed_time": OBS,
           "evidence": [{"artifact_version_id": U["version"], "artifact_part_id": U["part"], "page": 30}]})
records.append(c1)

c2 = env("claim", U["claim2"], "claim/gemini-robotics-1-5/table-2-result")
c2.update({"claim_kind": "evaluation", "subject_refs": [{"id": U["model"], "record_type": "entity"}],
           "predicate": {"native": "Table 2 result", "normalized": "evaluation_result"},
           "object": {"type": "number", "value": 1},
           "statement_native": "Table 2", "attribution": {"actor_type": "evaluator", "actor_org_id": U["org"]},
           "epistemic_status": "measured", "lifecycle": "current",
           "valid_time": {"status": "unknown", "reason": "Evaluation validity interval not stated."},
           "observed_time": OBS,
           "evidence": [{"artifact_version_id": U["version"], "artifact_part_id": U["part"], "table": "Table 2"}],
           "evaluation": {"evaluated_subject_id": U["model"],
                          "benchmark": {"native": "Table 2", "normalized": "other"},
                          "metric": {"native": "reported result", "normalized": "other"},
                          "reported_value": "1", "normalized_value": 1,
                          "evaluation_context": {"harness_unreported": True},
                          "asserted_at": {"value": "2025-09-25", "precision": "day", "basis": "index_surface"},
                          "artifact_version_id": U["version"]}})
records.append(c2)

e = env("event", U["event"], "event/gemini-robotics-1-5/model-card-publication")
e.update({"event_kind": "publication", "title": "Gemini Robotics 1.5 model-card publication",
          "subject_ids": [U["artifact2"], U["model"]],
          "valid_time": {"status": "known", "start": {"value": "2025-09-25", "precision": "day", "basis": "index_surface"}},
          "observed_time": OBS, "attributed_to_org_ids": [U["org"]],
          "evidence": [{"artifact_version_id": U["version"], "artifact_part_id": U["part"], "page": 30}]})
records.append(e)

ab = env("absence", U["absence"], "absence/gemini-robotics-1-5/standalone-card")
ab.update({"absence_type": "not_found",
           "target": {"subject_id": U["model"], "description_native": "standalone model card document"},
           "expected_artifact_class": "model_disclosure",
           "search_scope": {"description": "Provider model-card index and official report links checked in the calibration session",
                            "surface_url_ids": [U["url1"]]},
           "checked_at": {"value": "2026-09-05", "precision": "day", "basis": "retrieval"},
           "observed_time": OBS, "basis": "The index points to a page anchor inside the larger report.",
           "lifecycle": "current", "retrieval_event_ids": [U["retrieval"]],
           "next_check_at": {"value": "2027-03", "precision": "month", "qualifier": "approximate"}})
records.append(ab)

cv = env("coverage_ledger_entry", U["coverage"], "coverage/calibration/gemini-robotics-1-5")
cv.update({"scope_key": "calibration/google/gemini-robotics-1-5",
           "scope_description": "Calibration coverage for the report-appendix documentary form",
           "coverage_status": "covered",
           "assessed_at": {"value": "2026-09-05", "precision": "day", "basis": "retrieval"},
           "observed_time": OBS, "coverage_basis": "Artifact, version, byte, part, relationship, claim, and retrieval records are present.",
           "subject_ids": [U["model"]], "provider_org_id": U["org"],
           "surface_url_ids": [U["url1"], U["url2"]],
           "desired_artifact_classes": ["technical_report", "model_disclosure"],
           "covered_record_ids": [U["artifact"], U["artifact2"], U["part"]],
           "expected_count": 2, "observed_count": 2})
records.append(cv)

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) + "\n" for r in records), encoding="utf-8")
print(f"wrote {len(records)} records to {OUT}")
