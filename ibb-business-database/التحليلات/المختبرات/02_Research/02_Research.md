# المرحلة الثانية: البحث والأدلة — المختبرات الطبية في محافظة إب

> **الإصدار:** 0.1 — حزمة أدلة قابلة للمراجعة.
> **تاريخ التحديث:** 28 أغسطس 2026.
> **حالة المعلومات:** لا تشكل مرشحات المواقع دليلًا على تشغيل المختبر أو ترخيصه أو جودة فحوصه. تستبعد الحزمة الإحصاءات والقوائم السابقة غير المسندة.

## 2.1 المصادر المعتمدة

| المعرّف | المصدر | الاستخدام | القيد |
|---|---|---|---|
| `HDX-HOT-OSM-HEALTH-2026-08` | [HDX: Health Facilities of Yemen](https://data.humdata.org/dataset/hotosm_yem_health_facilities) | مواقع مرشحة للمختبرات الموسومة في إب | مصدر جماهيري غير شامل، ولا يثبت الترخيص أو التشغيل |
| `WHO-HERAMS-2024-02` | [WHO: HeRAMS Yemen Summary Update](https://www.who.int/publications/m/item/herams-yemen-summary-update-report-2024-02) | سياق منهجي للخدمات الصحية | لا يثبت حالة مختبر بعينه |

## 2.2 السجل المرشح وخطة التحقق

ينتج [`extract_ibb_lab_candidates.py`](../../../../research/scripts/extract_ibb_lab_candidates.py) ملف مرشحات من لقطة 7 أغسطس 2026. كل سجل `public_candidate`، ويحتاج إلى مطابقة اسم وموقع ثم تحقق تشغيل وترخيص قبل نشره كبيان عام. لا تجمع الحزمة نتائج فحوص أو بيانات مرضى أو إحالات.

## 2.3 قرار التحليل

لا تستخدم هذه الدفعة حصصًا جغرافية أو تصنيفات خدمة أو أرقامًا سعرية بلا مصدر. كما لا تقدم مقارنة جودة أو خدمات حجز. والمنتج الأولي هو قائمة مراجعة يمكن تحويلها إلى دليل محدود بدرجة ثقة وتاريخ تحقق ظاهرين.

## المراجع

[1]: https://data.humdata.org/dataset/hotosm_yem_health_facilities "HDX — Health Facilities of Yemen"
[2]: https://www.who.int/publications/m/item/herams-yemen-summary-update-report-2024-02 "WHO — HeRAMS Yemen Summary Update"
