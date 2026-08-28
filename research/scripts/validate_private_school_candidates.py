"""Validate the private-school candidate output and its provenance requirements."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "data/private-schools/ibb_private_school_candidates_osm_2026-08-07.geojson"


def main() -> None:
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    features = payload["features"]
    ids = [feature["properties"].get("record_id") for feature in features]
    statuses = Counter(feature["properties"].get("verification_status") for feature in features)
    ownership = Counter(feature["properties"].get("ownership_status") for feature in features)
    assert features, "No private-school candidates found"
    assert len(ids) == len(set(ids)), "Duplicate record_id found"
    assert all(feature["properties"].get("sources") for feature in features), "Missing source provenance found"
    assert all(feature.get("geometry") for feature in features), "Missing geometry found"
    assert statuses == Counter({"public_candidate": len(features)}), "Unexpected verification status"
    assert ownership == Counter({"private_candidate": len(features)}), "Unexpected ownership status"
    print(f"candidate_count={len(features)}")
    print(f"verification_statuses={dict(statuses)}")
    print(f"ownership_statuses={dict(ownership)}")


if __name__ == "__main__":
    main()
