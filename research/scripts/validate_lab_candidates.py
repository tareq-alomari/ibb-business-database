"""Validate laboratory candidate provenance and unverified status."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "data/labs/ibb_lab_candidates_osm_2026-08-07.geojson"


def main() -> None:
    features = json.loads(INPUT.read_text(encoding="utf-8"))["features"]
    ids = [feature["properties"]["record_id"] for feature in features]
    assert len(ids) == len(set(ids)), "Duplicate laboratory candidate id found"
    assert all(feature["properties"]["verification_status"] == "public_candidate" for feature in features)
    assert all(feature["properties"]["sources"] and feature.get("geometry") for feature in features)
    print(f"laboratory_candidates={len(features)}")
    print("all_candidates_have_provenance=true")


if __name__ == "__main__":
    main()
