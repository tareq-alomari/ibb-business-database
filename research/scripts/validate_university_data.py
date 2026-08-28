"""Validate the university evidence outputs without asserting unverified completeness."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OFFICIAL = ROOT / "data/universities/official-institutions.json"
CANDIDATES = ROOT / "data/universities/ibb_university_location_candidates_osm_2026-08-07.geojson"


def main() -> None:
    official = json.loads(OFFICIAL.read_text(encoding="utf-8"))["records"]
    candidates = json.loads(CANDIDATES.read_text(encoding="utf-8"))["features"]
    official_ids = [record["record_id"] for record in official]
    candidate_ids = [feature["properties"]["record_id"] for feature in candidates]
    assert len(official_ids) == len(set(official_ids)), "Duplicate official institution id found"
    assert all(record["verification_status"] == "official_verified" for record in official), "Official registry contains non-official record"
    assert all(record["sources"] and record["official_url"] for record in official), "Official registry missing direct source"
    assert len(candidate_ids) == len(set(candidate_ids)), "Duplicate location candidate id found"
    assert all(feature["properties"]["verification_status"] == "public_candidate" for feature in candidates), "Unexpected location candidate status"
    assert all(feature["properties"]["sources"] for feature in candidates), "Location candidate missing provenance"
    print(f"official_institutions={len(official)}")
    print(f"location_candidates={len(candidates)}")
    print("official_records_with_direct_sources=all")


if __name__ == "__main__":
    main()
