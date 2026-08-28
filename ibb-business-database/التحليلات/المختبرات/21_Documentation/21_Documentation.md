# المرحلة الحادية والعشرون: 21_Documentation - قطاع المختبرات الطبية في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 21_Documentation.md

---

## 21.1 الوثائق المتاحة

| المكوّن | الموقع | الحالة |
|---|---|---|
| سجل المصدر | `research/sources/labs-source-log.md` | منجز |
| ملف الأدلة | `research/labs/labs-evidence-dossier-2026-08.md` | منجز |
| نموذج السجل | `schemas/lab-record.schema.json` | منجز |
| مرشحات وملخص | `data/labs/` | منجز؛ النتيجة الحالية فجوة تغطية معلنة |
| قائمة تحقق | `data/labs/verification_queue.md` | منجز؛ لم تنفذ ميدانيًا |

## 21.2 تشغيل الفحص

```bash
python3 research/scripts/extract_ibb_lab_candidates.py
python3 research/scripts/validate_lab_candidates.py
```

لا يحتوي المستودع على تطبيق معاملات أو API أو نموذج حجز خاص بالمختبرات؛ لذلك لا توثق هذه الدفعة خطوات تسجيل أو دفع أو إدارة نتائج.
