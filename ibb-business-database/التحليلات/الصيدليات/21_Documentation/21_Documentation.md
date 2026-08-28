# المرحلة الحادية والعشرون: Documentation - قطاع الصيدليات في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 21_Documentation.md

---

## 21.1 مكونات الحزمة الفعلية

| المكوّن | الموقع | الغرض |
|---|---|---|
| سجل المصدر | `research/sources/pharmacies-source-log.md` | المصدر والرخصة والقيود |
| السجل المرشح | `data/pharmacies/*.geojson` | مواقع مرشحة فقط |
| قائمة التحقق | `data/pharmacies/verification_queue.md` | ترقية السجل أو رفضه |
| أداة الاستخراج | `research/scripts/extract_ibb_pharmacy_candidates.py` | إعادة إنتاج القائمة من المصدر الخام |
| أداة الفحص | `research/scripts/validate_pharmacy_candidates.py` | فحص المصدر والحالة والمعرفات |

## 21.2 تشغيل فحص البيانات

```bash
python3 research/scripts/extract_ibb_pharmacy_candidates.py
python3 research/scripts/validate_pharmacy_candidates.py
```

يعاد التشغيل من أرشيف المصدر الخام المحفوظ وفق تعليمات `research/raw/README.md`. ولا يمثل هذا المستودع تطبيقًا معامليًا أو واجهة API أو بنية نشر لخدمة صحية.
