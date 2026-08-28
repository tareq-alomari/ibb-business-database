"""Extract institute-location candidates in Ibb from the HOT/OSM education snapshot."""

from __future__ import annotations

import json
import re
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "research/raw/hotosm_yem_education_facilities_osm_geojson_2026-08-07.zip"
OUTPUT_DIRECTORY = ROOT / "data/institutes"
OUTPUT = OUTPUT_DIRECTORY / "ibb_institute_location_candidates_osm_2026-08-07.geojson"
SUMMARY_OUTPUT = OUTPUT_DIRECTORY / "ibb_institute_location_candidates_osm_2026-08-07.summary.json"
SOURCE_URL = "https://data.humdata.org/dataset/hotosm_yem_education_facilities"
INSTITUTE_SIGNAL = re.compile(r"(?:معهد|institute)", re.IGNORECASE)


def clean(value: object) -> str | None:
    return value.strip() if isinstance(value, str) and value.strip() else None


def is_candidate(feature: dict) -> bool:
    props = feature.get("properties") or {}
    if props.get("adm1_name") != "Ibb":
        return False
    names = " ".join(str(value or "") for value in (props.get("name"), props.get("name_ar"), props.get("name_en")))
    return bool(INSTITUTE_SIGNAL.search(names))


def main() -> None:
    with zipfile.ZipFile(ARCHIVE) as archive:
        source = json.loads(archive.read("education_facilities.geojson").decode("utf-8"))
    candidates = []
    for feature in source["features"]:
        if not is_candidate(feature):
            continue
        props = feature.get("properties") or {}
        raw_id = str(props.get("id") or feature.get("id") or "unknown")
        safe_id = re.sub(r"[^a-z0-9]+", "-", raw_id.lower()).strip("-") or "unknown"
        candidates.append({
            "type": "Feature", "id": f"ibb-institute-osm-{safe_id}", "geometry": feature.get("geometry"),
            "properties": {
                "record_id": f"ibb-institute-osm-{safe_id}",
                "name": clean(props.get("name_ar")) or clean(props.get("name")) or clean(props.get("name_en")) or f"Unnamed institute candidate ({raw_id})",
                "governorate": "Ibb", "district": clean(props.get("adm2_name")),
                "source_tag": props.get("amenity") or props.get("building"), "verification_status": "public_candidate", "confidence": "medium",
                "sources": [{"source_id": "HDX-HOT-OSM-EDU-2026-08", "source_url": SOURCE_URL, "retrieved_at": "2026-08-28", "note": "OSM-derived institute candidate. Institution type, licensing, ownership and current operation require direct verification."}],
                "updated_at": "2026-08-28"
            }
        })
    candidates.sort(key=lambda item: (item["properties"]["district"] or "", item["properties"]["name"]))
    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({"type":"FeatureCollection","name":"ibb_institute_location_candidates_osm_2026_08_07","attribution":"© OpenStreetMap contributors; Humanitarian OpenStreetMap Team (HOT). Derived from HDX snapshot dated 2026-08-07.","features":candidates}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    districts: dict[str, int] = {}
    for candidate in candidates:
        district = candidate["properties"]["district"] or "Unknown"
        districts[district] = districts.get(district, 0) + 1
    SUMMARY_OUTPUT.write_text(json.dumps({"source_id":"HDX-HOT-OSM-EDU-2026-08","retrieved_at":"2026-08-28","filter":"adm1_name == Ibb and explicit institute name signal","candidate_count":len(candidates),"district_counts":dict(sorted(districts.items())),"verification_status":"All records are public_candidate and are not linked automatically to the official institutional index."}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(candidates)} institute-location candidates to {OUTPUT}")


if __name__ == "__main__":
    main()
