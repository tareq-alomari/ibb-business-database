# المرحلة الثانية: Research - قطاع الصيدليات في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 02_Research.md

---

## 2.1 المصادر المعتمدة

| المعرّف | المصدر | الاستخدام | القيد |
|---|---|---|---|
| `HDX-HOT-OSM-HEALTH-2026-08` | [HDX: Health Facilities of Yemen](https://data.humdata.org/dataset/hotosm_yem_health_facilities) | مرشحات مواقع صيدليات موسومة في إب | مصدر جماهيري وغير شامل؛ لا يثبت التشغيل أو الترخيص |
| `WHO-HERAMS-2024-02` | [WHO: HeRAMS Yemen Summary Update](https://www.who.int/publications/m/item/herams-yemen-summary-update-report-2024-02) | سياق منهجي لتغير توافر الخدمات الصحية | سياق وطني، وليس سجل صيدليات لإب |

## 2.2 سجل المرشحات

ينتج [`extract_ibb_pharmacy_candidates.py`](../../../../research/scripts/extract_ibb_pharmacy_candidates.py) ملف [`ibb_pharmacy_candidates_osm_2026-08-07.geojson`](../../../../data/pharmacies/ibb_pharmacy_candidates_osm_2026-08-07.geojson) من لقطة 7 أغسطس 2026. جميع السجلات تحمل `public_candidate`، ولا تمثل عدد الصيدليات العاملة أو رخصتها أو أسعارها أو مخزونها.

## 2.3 فجوة البيانات وخطة التحقق

| الحقل | حالة الدليل الحالي | الإجراء |
|---|---|---|
| الاسم والموقع | مرشح عام عند وجود وسم OSM | مطابقة مصدرين أو تحقق محلي |
| الترخيص وحالة التشغيل | غير متوفر في الطبقة | تأكيد من جهة مخولة أو زيارة موثقة |
| الاتصال وساعات العمل | غير مدرج | قناة صيدلية رسمية أو موافقة مباشرة |
| الأدوية والأسعار | خارج نطاق المصدر | نشر مؤرخ ومحدود بعد موافقة المصدر |

## 2.4 قرار التحليل

لا تستخدم هذه الدفعة تقديرات النسب الجغرافية أو فئات السعر أو نسب التواجد الرقمي السابقة، لأنها بلا مصدر قابل للمراجعة. المنتج الأولي هو دليل تحقق لا منصة مبيعات أو تقييمات، ويجب أن يوضح تاريخ آخر مراجعة لكل سجل.

## المراجع

[1]: https://data.humdata.org/dataset/hotosm_yem_health_facilities "HDX — Health Facilities of Yemen"
[2]: https://www.who.int/publications/m/item/herams-yemen-summary-update-report-2024-02 "WHO — HeRAMS Yemen Summary Update"
