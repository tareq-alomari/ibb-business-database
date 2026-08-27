"""Extract unverified Ibb school candidates from the HOT/OSM education snapshot.

OSM school tags do not reliably establish public ownership. The output contains school
candidates only and keeps ownership_status as unknown unless a later primary source verifies it.
"""

from __future__ import annotations

import csv
import json
import re
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "research/raw/hotosm_yem_education_facilities_osm_geojson_2026-08-07/education_facilities.geojson"
ARCHIVE = ROOT / "research/raw/hotosm_yem_education_facilities_osm_geojson_2026-08-07.zip"
OUTPUT_DIRECTORY = ROOT / "data/public-schools"
OUTPUT = OUTPUT_DIRECTORY / "ibb_school_candidates_osm_2026-08-07.geojson"
CSV_OUTPUT = OUTPUT_DIRECTORY / "ibb_school_candidates_osm_2026-08-07.csv"
SUMMARY_OUTPUT = OUTPUT_DIRECTORY / "ibb_school_candidates_osm_2026-08-07.summary.json"

SOURCE_ID = "HDX-HOT-OSM-EDU-2026-08"
SOURCE_URL = "https://data.humdata.org/dataset/hotosm_yem_education_facilities"
SOURCE_LICENSE = "ODC-ODbL; attribution required to OpenStreetMap contributors and HOT"
RETRIEVED_AT = "2026-08-28"
EXCLUDED_NAME_SIGNAL = re.compile(r"(?:أهلي|اهلي|خاص(?:ة)?|private|جامعة|كلية|معهد|university|college|institute)", re.IGNORECASE)


def is_school_candidate(feature: dict) -> bool:
    props = feature.get("properties") or {}
    is_school = props.get("adm1_name") == "Ibb" and (
        props.get("amenity") == "school" or props.get("building") == "school"
    )
    raw_name = " ".join(str(value or "") for value in (props.get("name_ar"), props.get("name"), props.get("name_en")))
    return is_school and not EXCLUDED_NAME_SIGNAL.search(raw_name)


def is_source_school_signal(feature: dict) -> bool:
    props = feature.get("properties") or {}
    return props.get("adm1_name") == "Ibb" and (
        props.get("amenity") == "school" or props.get("building") == "school"
    )


def candidate_name(feature: dict) -> str:
    props = feature.get("properties") or {}
    source_id = props.get("id") or feature.get("id") or "unknown"
    return props.get("name_ar") or props.get("name") or props.get("name_en") or f"Unnamed school ({source_id})"


def normalize_operator(operator_type: object) -> str:
    if str(operator_type).lower() in {"government", "public"}:
        return "public_candidate"
    return "unknown"


def build_candidate(feature: dict) -> dict:
    props = feature.get("properties") or {}
    source_identifier = str(props.get("id") or feature.get("id") or candidate_name(feature))
    safe_identifier = re.sub(r"[^a-z0-9]+", "-", source_identifier.lower()).strip("-") or "unknown"
    return {
        "type": "Feature",
        "id": f"ibb-school-osm-{safe_identifier}",
        "geometry": feature.get("geometry"),
        "properties": {
            "record_id": f"ibb-school-osm-{safe_identifier}",
            "name": candidate_name(feature),
            "name_ar": props.get("name_ar"),
            "name_en": props.get("name_en") or props.get("name_latin"),
            "governorate": "Ibb",
            "district": props.get("adm2_name"),
            "institution_type": "school",
            "ownership_status": normalize_operator(props.get("operator_type")),
            "source_operator_type": props.get("operator_type"),
            "source_school_signal": props.get("amenity") or props.get("building"),
            "verification_status": "public_candidate",
            "confidence": "medium",
            "sources": [{
                "source_id": SOURCE_ID,
                "source_url": SOURCE_URL,
                "retrieved_at": RETRIEVED_AT,
                "verified_at": None,
                "license": SOURCE_LICENSE,
                "note": "Public OSM-derived candidate. School type, ownership, location and current operation require direct local verification."
            }],
            "updated_at": RETRIEVED_AT,
            "change_note": "Created by reproducible filter from the August 2026 HOT/OSM Yemen education-facilities snapshot."
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
    source = load_source()
    source_school_signals = [feature for feature in source["features"] if is_source_school_signal(feature)]
    candidates = [build_candidate(feature) for feature in source["features"] if is_school_candidate(feature)]
    candidates.sort(key=lambda item: (item["properties"]["district"] or "", item["properties"]["name"]))
    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)

    collection = {
        "type": "FeatureCollection",
        "name": "ibb_school_candidates_osm_2026_08_07",
        "license": SOURCE_LICENSE,
        "attribution": "© OpenStreetMap contributors; Humanitarian OpenStreetMap Team (HOT). Derived from HDX snapshot dated 2026-08-07.",
        "source": {"source_id": SOURCE_ID, "source_url": SOURCE_URL, "retrieved_at": RETRIEVED_AT},
        "features": candidates
    }
    OUTPUT.write_text(json.dumps(collection, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    with CSV_OUTPUT.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["record_id", "name", "name_ar", "name_en", "district", "ownership_status", "verification_status", "confidence", "source_id", "source_url", "retrieved_at"])
        writer.writeheader()
        for candidate in candidates:
            props = candidate["properties"]
            source_info = props["sources"][0]
            writer.writerow({
                "record_id": props["record_id"], "name": props["name"], "name_ar": props["name_ar"] or "",
                "name_en": props["name_en"] or "", "district": props["district"] or "",
                "ownership_status": props["ownership_status"], "verification_status": props["verification_status"],
                "confidence": props["confidence"], "source_id": source_info["source_id"],
                "source_url": source_info["source_url"], "retrieved_at": source_info["retrieved_at"]
            })

    district_counts: dict[str, int] = {}
    ownership_counts: dict[str, int] = {}
    geometry_counts: dict[str, int] = {}
    for candidate in candidates:
        props = candidate["properties"]
        district = props["district"] or "Unknown"
        geometry_type = (candidate.get("geometry") or {}).get("type") or "Unknown"
        district_counts[district] = district_counts.get(district, 0) + 1
        ownership_counts[props["ownership_status"]] = ownership_counts.get(props["ownership_status"], 0) + 1
        geometry_counts[geometry_type] = geometry_counts.get(geometry_type, 0) + 1
    summary = {
        "source_id": SOURCE_ID,
        "retrieved_at": RETRIEVED_AT,
        "filter": "adm1_name == Ibb and (amenity == school or building == school)",
        "name_exclusions": "Exclude explicit private or higher-education name signals; final ownership still requires direct verification.",
        "source_school_signal_count": len(source_school_signals),
        "excluded_by_name_signal_count": len(source_school_signals) - len(candidates),
        "candidate_count": len(candidates),
        "district_counts": dict(sorted(district_counts.items())),
        "ownership_status_counts": dict(sorted(ownership_counts.items())),
        "geometry_type_counts": dict(sorted(geometry_counts.items())),
        "verification_status": "All entries are public_candidate. OSM labels do not verify government ownership or operating status."
    }
    SUMMARY_OUTPUT.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(candidates)} school candidates to {OUTPUT} and {CSV_OUTPUT}")


if __name__ == "__main__":
    main()
