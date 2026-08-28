"""Extract independently unverified training-centre location candidates from HOT/OSM."""

from __future__ import annotations

import json
import re
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "research/raw/hotosm_yem_education_facilities_osm_geojson_2026-08-07.zip"
OUTPUT_DIRECTORY = ROOT / "data/training-centers"
OUTPUT = OUTPUT_DIRECTORY / "ibb_training_center_location_candidates_osm_2026-08-07.geojson"
SUMMARY = OUTPUT_DIRECTORY / "ibb_training_center_location_candidates_osm_2026-08-07.summary.json"
SOURCE_URL = "https://data.humdata.org/dataset/hotosm_yem_education_facilities"
TRAINING_SIGNAL = re.compile(r"(?:مركز|تدريب|تأهيل|training|centre|center)", re.IGNORECASE)


def clean(value: object) -> str | None:
    return value.strip() if isinstance(value, str) and value.strip() else None


def main() -> None:
    with zipfile.ZipFile(ARCHIVE) as archive:
        source = json.loads(archive.read("education_facilities.geojson").decode("utf-8"))
    candidates = []
    for feature in source["features"]:
        props = feature.get("properties") or {}
        if props.get("adm1_name") != "Ibb":
            continue
        names = " ".join(str(value or "") for value in (props.get("name"), props.get("name_ar"), props.get("name_en")))
        if not TRAINING_SIGNAL.search(names):
            continue
        raw_id = str(props.get("id") or feature.get("id") or "unknown")
        safe_id = re.sub(r"[^a-z0-9]+", "-", raw_id.lower()).strip("-") or "unknown"
        candidates.append({
            "type": "Feature", "id": f"ibb-training-center-osm-{safe_id}", "geometry": feature.get("geometry"),
            "properties": {
                "record_id": f"ibb-training-center-osm-{safe_id}",
                "name": clean(props.get("name_ar")) or clean(props.get("name")) or clean(props.get("name_en")) or f"Unnamed training-center candidate ({raw_id})",
                "governorate": "Ibb", "district": clean(props.get("adm2_name")), "source_tag": props.get("amenity") or props.get("building"),
                "verification_status": "public_candidate", "confidence": "medium",
                "sources": [{"source_id":"HDX-HOT-OSM-EDU-2026-08","source_url":SOURCE_URL,"retrieved_at":"2026-08-28","note":"OSM-derived training-centre candidate. Its licensing, operating state and programmes require direct verification."}],
                "updated_at":"2026-08-28"
            }
        })
    candidates.sort(key=lambda item: (item["properties"]["district"] or "", item["properties"]["name"]))
    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({"type":"FeatureCollection","name":"ibb_training_center_location_candidates_osm_2026_08_07","attribution":"© OpenStreetMap contributors; Humanitarian OpenStreetMap Team (HOT). Derived from HDX snapshot dated 2026-08-07.","features":candidates}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    districts: dict[str, int] = {}
    for candidate in candidates:
        district = candidate["properties"]["district"] or "Unknown"
        districts[district] = districts.get(district, 0) + 1
    SUMMARY.write_text(json.dumps({"source_id":"HDX-HOT-OSM-EDU-2026-08","retrieved_at":"2026-08-28","filter":"adm1_name == Ibb and explicit training/center name signal","candidate_count":len(candidates),"district_counts":dict(sorted(districts.items())),"verification_status":"All records are public_candidate and are not automatically linked to official centre records."}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(candidates)} training-centre location candidates to {OUTPUT}")


if __name__ == "__main__":
    main()
