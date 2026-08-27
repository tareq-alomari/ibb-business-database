"""Validate basic provenance and completeness rules for the derived Ibb hospital candidates."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "data/hospitals/ibb_hospital_candidates_osm_2026-08-07.geojson"


def main() -> None:
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    features = payload["features"]
    ids = [feature["properties"].get("record_id") for feature in features]
    names = [feature["properties"].get("name") for feature in features]
    statuses = Counter(feature["properties"].get("verification_status") for feature in features)
    districts = Counter(feature["properties"].get("district") or "Unknown" for feature in features)
    missing_sources = [feature["properties"].get("record_id") for feature in features if not feature["properties"].get("sources")]
    missing_geometry = [feature["properties"].get("record_id") for feature in features if not feature.get("geometry")]

    assert payload["type"] == "FeatureCollection"
    assert len(ids) == len(set(ids)), "Duplicate record_id found"
    assert all(name for name in names), "Blank facility name found"
    assert statuses == Counter({"public_candidate": len(features)}), "Unexpected verification status"
    assert not missing_sources, "Missing provenance found"
    assert not missing_geometry, "Missing geometry found"

    print(f"candidate_count={len(features)}")
    print(f"distinct_districts={len(districts)}")
    print(f"verification_statuses={dict(statuses)}")
    print(f"records_with_provenance={len(features) - len(missing_sources)}")
    print(f"records_with_geometry={len(features) - len(missing_geometry)}")


if __name__ == "__main__":
    main()
