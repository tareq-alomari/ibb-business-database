"""Extract Ibb university-location candidates from the HOT/OSM education snapshot.

These candidates are intentionally kept separate from directly sourced institutional records.
An OSM label or coordinate cannot independently verify current operation, ownership, or a
relationship to an official university page.
"""

from __future__ import annotations

import json
import re
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "research/raw/hotosm_yem_education_facilities_osm_geojson_2026-08-07/education_facilities.geojson"
ARCHIVE = ROOT / "research/raw/hotosm_yem_education_facilities_osm_geojson_2026-08-07.zip"
OUTPUT_DIRECTORY = ROOT / "data/universities"
OUTPUT = OUTPUT_DIRECTORY / "ibb_university_location_candidates_osm_2026-08-07.geojson"
SUMMARY_OUTPUT = OUTPUT_DIRECTORY / "ibb_university_location_candidates_osm_2026-08-07.summary.json"

SOURCE_ID = "HDX-HOT-OSM-EDU-2026-08"
SOURCE_URL = "https://data.humdata.org/dataset/hotosm_yem_education_facilities"
RETRIEVED_AT = "2026-08-28"
UNIVERSITY_SIGNAL = re.compile(r"(?:جامعة|university)", re.IGNORECASE)


def is_candidate(feature: dict) -> bool:
    props = feature.get("properties") or {}
    if props.get("adm1_name") != "Ibb":
        return False
    tagged_university = props.get("amenity") == "university" or props.get("building") == "university"
    names = " ".join(str(value or "") for value in (props.get("name"), props.get("name_ar"), props.get("name_en")))
    return tagged_university or bool(UNIVERSITY_SIGNAL.search(names))


def clean(value: object) -> str | None:
    return value.strip() if isinstance(value, str) and value.strip() else None


def build_candidate(feature: dict) -> dict:
    props = feature.get("properties") or {}
    source_identifier = str(props.get("id") or feature.get("id") or "unknown")
    safe_id = re.sub(r"[^a-z0-9]+", "-", source_identifier.lower()).strip("-") or "unknown"
    name = clean(props.get("name_ar")) or clean(props.get("name")) or clean(props.get("name_en")) or f"Unnamed university candidate ({source_identifier})"
    return {
        "type": "Feature",
        "id": f"ibb-university-osm-{safe_id}",
        "geometry": feature.get("geometry"),
        "properties": {
            "record_id": f"ibb-university-osm-{safe_id}",
            "name": name,
            "name_ar": clean(props.get("name_ar")),
            "name_en": clean(props.get("name_en")) or clean(props.get("name_latin")),
            "governorate": "Ibb",
            "district": clean(props.get("adm2_name")),
            "source_tag": props.get("amenity") or props.get("building"),
            "verification_status": "public_candidate",
            "confidence": "medium",
            "sources": [{
                "source_id": SOURCE_ID,
                "source_url": SOURCE_URL,
                "retrieved_at": RETRIEVED_AT,
                "note": "OSM-derived university-location candidate. Linkage to an official institution, ownership and current operation require direct verification."
            }],
            "updated_at": RETRIEVED_AT
        }
    }


def load_source() -> dict:
    if INPUT.exists():
        return json.loads(INPUT.read_text(encoding="utf-8"))
    if ARCHIVE.exists():
        with zipfile.ZipFile(ARCHIVE) as archive:
            return json.loads(archive.read("education_facilities.geojson").decode("utf-8"))
    raise FileNotFoundError("No education-facilities snapshot found. See research/raw/README.md.")


def main() -> None:
    payload = load_source()
    candidates = [build_candidate(feature) for feature in payload["features"] if is_candidate(feature)]
    candidates.sort(key=lambda item: (item["properties"]["district"] or "", item["properties"]["name"]))
    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    collection = {
        "type": "FeatureCollection",
        "name": "ibb_university_location_candidates_osm_2026_08_07",
        "attribution": "© OpenStreetMap contributors; Humanitarian OpenStreetMap Team (HOT). Derived from HDX snapshot dated 2026-08-07.",
        "features": candidates
    }
    OUTPUT.write_text(json.dumps(collection, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    districts: dict[str, int] = {}
    for candidate in candidates:
        district = candidate["properties"]["district"] or "Unknown"
        districts[district] = districts.get(district, 0) + 1
    summary = {
        "source_id": SOURCE_ID,
        "retrieved_at": RETRIEVED_AT,
        "filter": "adm1_name == Ibb and (university tag or explicit university name signal)",
        "candidate_count": len(candidates),
        "district_counts": dict(sorted(districts.items())),
        "verification_status": "All records are public_candidate and are not linked automatically to official institutional records."
    }
    SUMMARY_OUTPUT.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(candidates)} university-location candidates to {OUTPUT}")


if __name__ == "__main__":
    main()
