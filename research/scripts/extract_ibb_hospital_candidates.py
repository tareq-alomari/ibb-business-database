"""Extract unverified Ibb hospital candidates from the downloaded HOT/OSM GeoJSON snapshot.

The script never upgrades a record to verified status. It preserves provenance and adds the
required attribution metadata for any derived output.
"""

from __future__ import annotations

import json
import re
import csv
import zipfile
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = REPOSITORY_ROOT / "research/raw/hotosm_yem_health_facilities_osm_geojson_2026-08-07/health_facilities.geojson"
ARCHIVE_PATH = REPOSITORY_ROOT / "research/raw/hotosm_yem_health_facilities_osm_geojson_2026-08-07.zip"
OUTPUT_DIRECTORY = REPOSITORY_ROOT / "data/hospitals"
OUTPUT_PATH = OUTPUT_DIRECTORY / "ibb_hospital_candidates_osm_2026-08-07.geojson"
SUMMARY_PATH = OUTPUT_DIRECTORY / "ibb_hospital_candidates_osm_2026-08-07.summary.json"
QUEUE_PATH = OUTPUT_DIRECTORY / "ibb_hospital_candidates_osm_2026-08-07.csv"

SOURCE_ID = "HDX-HOT-OSM-2026-08"
SOURCE_URL = "https://data.humdata.org/dataset/hotosm_yem_health_facilities"
SOURCE_LICENSE = "ODC-ODbL; attribution required to OpenStreetMap contributors and HOT"
RETRIEVED_AT = "2026-08-28"


def is_hospital(feature: dict) -> bool:
    props = feature.get("properties") or {}
    return props.get("adm1_name") == "Ibb" and (
        props.get("amenity") == "hospital" or props.get("healthcare") == "hospital"
    )


def normalized_name(feature: dict) -> str:
    props = feature.get("properties") or {}
    osm_id = props.get("id") or feature.get("id") or "unknown"
    return props.get("name_ar") or props.get("name") or props.get("name_en") or f"Unnamed hospital ({osm_id})"


def build_candidate(feature: dict) -> dict:
    props = feature.get("properties") or {}
    raw_osm_id = str(props.get("id") or feature.get("id") or normalized_name(feature))
    osm_id = re.sub(r"[^a-z0-9]+", "-", raw_osm_id.lower()).strip("-") or "unknown"
    return {
        "type": "Feature",
        "id": f"ibb-hospital-osm-{osm_id}",
        "geometry": feature.get("geometry"),
        "properties": {
            "record_id": f"ibb-hospital-osm-{osm_id}",
            "name": normalized_name(feature),
            "name_ar": props.get("name_ar"),
            "name_en": props.get("name_en") or props.get("name_latin"),
            "governorate": "Ibb",
            "district": props.get("adm2_name"),
            "facility_category": "hospital",
            "operator_type": props.get("operator_type") or "unknown",
            "verification_status": "public_candidate",
            "confidence": "medium",
            "sources": [
                {
                    "source_id": SOURCE_ID,
                    "source_url": SOURCE_URL,
                    "retrieved_at": RETRIEVED_AT,
                    "verified_at": None,
                    "license": SOURCE_LICENSE,
                    "note": "Public OSM-derived candidate. Location and attributes require direct local verification."
                }
            ],
            "updated_at": RETRIEVED_AT,
            "change_note": "Created by reproducible filter from the August 2026 HOT/OSM Yemen health-facilities snapshot."
        }
    }


def main() -> None:
    if INPUT_PATH.exists():
        source = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    elif ARCHIVE_PATH.exists():
        with zipfile.ZipFile(ARCHIVE_PATH) as archive:
            source = json.loads(archive.read("health_facilities.geojson").decode("utf-8"))
    else:
        raise FileNotFoundError(
            "No HOT/OSM snapshot found. Download the exact archive documented in research/raw/README.md."
        )
    candidates = [build_candidate(feature) for feature in source["features"] if is_hospital(feature)]
    candidates.sort(key=lambda feature: (feature["properties"]["district"] or "", feature["properties"]["name"]))

    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    output = {
        "type": "FeatureCollection",
        "name": "ibb_hospital_candidates_osm_2026_08_07",
        "license": SOURCE_LICENSE,
        "attribution": "© OpenStreetMap contributors; Humanitarian OpenStreetMap Team (HOT). Derived from HDX snapshot dated 2026-08-07.",
        "source": {"source_id": SOURCE_ID, "source_url": SOURCE_URL, "retrieved_at": RETRIEVED_AT},
        "features": candidates
    }
    OUTPUT_PATH.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    with QUEUE_PATH.open("w", encoding="utf-8", newline="") as queue_file:
        writer = csv.DictWriter(
            queue_file,
            fieldnames=[
                "record_id", "name", "name_ar", "name_en", "district", "operator_type",
                "verification_status", "confidence", "source_id", "source_url", "retrieved_at"
            ],
        )
        writer.writeheader()
        for candidate in candidates:
            props = candidate["properties"]
            source_info = props["sources"][0]
            writer.writerow(
                {
                    "record_id": props["record_id"],
                    "name": props["name"],
                    "name_ar": props["name_ar"] or "",
                    "name_en": props["name_en"] or "",
                    "district": props["district"] or "",
                    "operator_type": props["operator_type"],
                    "verification_status": props["verification_status"],
                    "confidence": props["confidence"],
                    "source_id": source_info["source_id"],
                    "source_url": source_info["source_url"],
                    "retrieved_at": source_info["retrieved_at"],
                }
            )

    district_counts: dict[str, int] = {}
    for candidate in candidates:
        district = candidate["properties"]["district"] or "Unknown"
        district_counts[district] = district_counts.get(district, 0) + 1
    summary = {
        "source_id": SOURCE_ID,
        "retrieved_at": RETRIEVED_AT,
        "filter": "adm1_name == Ibb and (amenity == hospital or healthcare == hospital)",
        "candidate_count": len(candidates),
        "district_counts": dict(sorted(district_counts.items())),
        "geometry_type_counts": dict(sorted({geometry_type: sum(1 for candidate in candidates if (candidate.get("geometry") or {}).get("type") == geometry_type) for geometry_type in {((candidate.get("geometry") or {}).get("type") or "Unknown") for candidate in candidates}}.items())),
        "named_candidates": sum(1 for candidate in candidates if not candidate["properties"]["name"].startswith("Unnamed hospital")),
        "verification_status": "All entries are public_candidate and require direct local verification."
    }
    SUMMARY_PATH.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(candidates)} unverified candidates to {OUTPUT_PATH} and {QUEUE_PATH}")


if __name__ == "__main__":
    main()
