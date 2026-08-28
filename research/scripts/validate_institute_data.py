"""Validate institute institutional records and unverified location candidates."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OFFICIAL = ROOT / "data/institutes/official-institutions.json"
CANDIDATES = ROOT / "data/institutes/ibb_institute_location_candidates_osm_2026-08-07.geojson"


def main() -> None:
    official = json.loads(OFFICIAL.read_text(encoding="utf-8"))["records"]
    candidates = json.loads(CANDIDATES.read_text(encoding="utf-8"))["features"]
    assert official and all(record["verification_status"] == "official_verified" and record["official_url"] for record in official)
    assert len({record["record_id"] for record in official}) == len(official)
    assert all(candidate["properties"]["verification_status"] == "public_candidate" for candidate in candidates)
    assert all(candidate["properties"]["sources"] for candidate in candidates)
    print(f"official_institutions={len(official)}")
    print(f"location_candidates={len(candidates)}")


if __name__ == "__main__":
    main()
