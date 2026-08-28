"""Validate the training-centre institutional index and its candidate locations."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OFFICIAL = ROOT / "data/training-centers/official-institutions.json"
CANDIDATES = ROOT / "data/training-centers/ibb_training_center_location_candidates_osm_2026-08-07.geojson"


def main() -> None:
    official = json.loads(OFFICIAL.read_text(encoding="utf-8"))["records"]
    candidates = json.loads(CANDIDATES.read_text(encoding="utf-8"))["features"]
    assert official and all(record["verification_status"] == "official_verified" and record["official_url"] for record in official)
    assert len({record["record_id"] for record in official}) == len(official)
    assert len({item["properties"]["record_id"] for item in candidates}) == len(candidates)
    assert all(item["properties"]["verification_status"] == "public_candidate" and item["properties"]["sources"] for item in candidates)
    print(f"official_training_centers={len(official)}")
    print(f"location_candidates={len(candidates)}")


if __name__ == "__main__":
    main()
