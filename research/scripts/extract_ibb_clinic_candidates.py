"""Extract unverified clinic candidates in Ibb from HOT/OSM health data."""
from __future__ import annotations
import json, re, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "research/raw/hotosm_yem_health_facilities_osm_geojson_2026-08-07.zip"
OUT = ROOT / "data/clinics/ibb_clinic_candidates_osm_2026-08-07.geojson"

def main() -> None:
    with zipfile.ZipFile(ARCHIVE) as archive:
        source = json.loads(archive.read("health_facilities.geojson").decode("utf-8"))
    features = []
    for item in source["features"]:
        props = item.get("properties") or {}
        if props.get("adm1_name") != "Ibb" or (props.get("amenity") != "clinic" and props.get("healthcare") != "clinic"):
            continue
        raw_id = str(props.get("id") or item.get("id") or "unknown")
        safe_id = re.sub(r"[^a-z0-9]+", "-", raw_id.lower()).strip("-") or "unknown"
        name = next((x.strip() for x in (props.get("name_ar"), props.get("name"), props.get("name_en")) if isinstance(x, str) and x.strip()), f"Unnamed clinic candidate ({raw_id})")
        features.append({"type":"Feature","id":f"ibb-clinic-osm-{safe_id}","geometry":item.get("geometry"),"properties":{"record_id":f"ibb-clinic-osm-{safe_id}","name":name,"governorate":"Ibb","district":props.get("adm2_name"),"verification_status":"public_candidate","confidence":"medium","sources":[{"source_id":"HDX-HOT-OSM-HEALTH-2026-08","source_url":"https://data.humdata.org/dataset/hotosm_yem_health_facilities","retrieved_at":"2026-08-28"}],"updated_at":"2026-08-28"}})
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"type":"FeatureCollection","name":"ibb_clinic_candidates_osm_2026_08_07","attribution":"© OpenStreetMap contributors; HOT; HDX snapshot dated 2026-08-07.","features":features},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"clinic_candidates={len(features)}")
if __name__ == "__main__": main()
