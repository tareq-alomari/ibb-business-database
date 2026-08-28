"""Validate official college units and independent public location candidates."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OFFICIAL = ROOT / "data/colleges/official-units.json"
CANDIDATES = ROOT / "data/colleges/ibb_college_location_candidates_osm_2026-08-07.geojson"


def main() -> None:
    official = json.loads(OFFICIAL.read_text(encoding="utf-8"))["records"]
    candidates = json.loads(CANDIDATES.read_text(encoding="utf-8"))["features"]
    assert len({record["record_id"] for record in official}) == len(official), "Duplicate official college id found"
    assert all(record["verification_status"] == "official_verified" and record["official_url"] for record in official), "Official unit missing direct evidence"
    assert len({candidate["properties"]["record_id"] for candidate in candidates}) == len(candidates), "Duplicate candidate id found"
    assert all(candidate["properties"]["verification_status"] == "public_candidate" for candidate in candidates), "Unexpected candidate status"
    assert all(candidate["properties"]["sources"] for candidate in candidates), "Candidate missing provenance"
    print(f"official_college_units={len(official)}")
    print(f"location_candidates={len(candidates)}")


if __name__ == "__main__":
    main()
