# المصادر الخام المحفوظة

يحفظ هذا المجلد أرشيف المصدر الخام اللازم لإعادة تشغيل الاستخراج، دون إدراج نسخة GeoJSON المفكوكة (الأكبر حجمًا). الأرشيف الحالي محفوظ كما نُشر في 7 أغسطس 2026.

| الملف | المصدر | المحتوى | الرخصة |
|---|---|---|---|
| `hotosm_yem_health_facilities_osm_geojson_2026-08-07.zip` | [HDX: Health Facilities of Yemen](https://data.humdata.org/dataset/hotosm_yem_health_facilities) | لقطة GeoJSON عامة لمرافق الصحة في اليمن | ODC-ODbL؛ الإسناد إلى OpenStreetMap contributors وHOT مطلوب |
| `hotosm_yem_education_facilities_osm_geojson_2026-08-07.zip` | [HDX: Education Facilities of Yemen](https://data.humdata.org/dataset/hotosm_yem_education_facilities) | لقطة GeoJSON عامة لمرافق التعليم في اليمن | ODC-ODbL؛ الإسناد إلى OpenStreetMap contributors وHOT مطلوب |

يعتمد سكربت [`extract_ibb_hospital_candidates.py`](../scripts/extract_ibb_hospital_candidates.py) على هذا الأرشيف لإنتاج قائمة المرشحات في `data/hospitals/`. ولا يعد الاحتفاظ بالأرشيف تحققًا من تشغيل المنشأة أو نوعها أو خدماتها الحالية.
