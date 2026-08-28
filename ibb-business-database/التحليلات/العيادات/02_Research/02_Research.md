# المرحلة الثانية: Research - قطاع العيادات الطبية في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 02_Research.md

---

## 2.1 المصادر المعتمدة

| المعرّف | المصدر | الاستخدام | القيد |
|---|---|---|---|
| `HDX-HOT-OSM-HEALTH-2026-08` | [HDX: Health Facilities of Yemen](https://data.humdata.org/dataset/hotosm_yem_health_facilities) | مرشحات مواقع موسومة عيادة في إب | مصدر جماهيري غير شامل؛ لا يثبت التشغيل أو التخصص |
| `WHO-HERAMS-2024-02` | [WHO: HeRAMS Yemen Summary Update](https://www.who.int/publications/m/item/herams-yemen-summary-update-report-2024-02) | سياق منهجي للمراجعة | ليس سجل عيادات لإب |

## 2.2 سجل المرشحات

أنتجت الأداة `extract_ibb_clinic_candidates.py` 173 مرشحًا من لقطة 7 أغسطس 2026. يمثل الرقم عناصر المصدر التي تطابق وسم العيادة، لا عدد العيادات العاملة أو المرخصة. تحمل جميع السجلات `public_candidate` وتحتاج تسوية وتحققًا مباشرًا.

## 2.3 حدود النشر

لا تستخدم الدفعة تقديرات التوزيع أو الأسعار أو الطلب، ولا تعرض حجزًا أو تقييمات أو مقارنات تخصصية. قبل النشر العام يجب توثيق الاسم والموقع وحالة التشغيل لكل سجل، مع عدم جمع أي بيانات مرضى أو مواعيد أو وصفات.

## المراجع

[1]: https://data.humdata.org/dataset/hotosm_yem_health_facilities "HDX — Health Facilities of Yemen"
[2]: https://www.who.int/publications/m/item/herams-yemen-summary-update-report-2024-02 "WHO — HeRAMS Yemen Summary Update"
