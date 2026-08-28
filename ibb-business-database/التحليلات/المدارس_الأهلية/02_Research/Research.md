# المرحلة الثانية: البحث والأدلة — المدارس الأهلية في محافظة إب

> **الإصدار:** 0.1 — حزمة أدلة قابلة للمراجعة.
> **تاريخ التحديث:** 28 أغسطس 2026.
> **حالة المعلومات:** لا تتوفر في هذه الدفعة قائمة رسمية عامة وحديثة تثبت جميع المدارس الأهلية في إب. تستخدم القائمة الحالية مرشحات ضيقة ذات إشارة أهلية صريحة وتنتظر التحقق المباشر.

---

## 2.1 هدف البحث

بناء قائمة أولية قابلة للتتبع للمدارس التي تحمل إشارة أهلية في بيانات عامة، مع منع تحويل الاسم أو وسم الخريطة إلى حكم على الترخيص أو الجودة أو الرسوم أو التشغيل.

## 2.2 المصادر وحدودها

| المعرّف | المصدر | الاستخدام | الحد الحاسم |
|---|---|---|---|
| `HDX-HOT-OSM-EDU-2026-08` | [HDX: Education Facilities of Yemen](https://data.humdata.org/dataset/hotosm_yem_education_facilities) | مرشحات جغرافية ذات إشارة أهلية صريحة، من لقطة 7 أغسطس 2026 | مصدر جماهيري لا يثبت الترخيص أو الملكية أو التشغيل |
| `UNICEF-YEM-EDU` | [UNICEF Yemen: Education](https://www.unicef.org/yemen/education) | سياق وطني للوصول إلى التعليم | لا يقيس مدارس إب الأهلية |

## 2.3 منهج المرشحات

ينتج السكربت [`extract_ibb_private_school_candidates.py`](../../../../research/scripts/extract_ibb_private_school_candidates.py) ملفات GeoJSON وCSV تحت [`data/private-schools/`](../../../../data/private-schools/). يحافظ الشرط على الدقة على حساب الشمول:

```text
adm1_name == "Ibb" and school signal and
(operator_type == "private" or explicit private-school name signal)
```

أظهرت هذه الفلترة 3 مرشحات في مديريتين ضمن لقطة المصدر. تتلقى كل نتيجة `ownership_status=private_candidate` و`verification_status=public_candidate`. لا تعني هذه القيم ترخيصًا أو شهادة جودة أو صحة معلومات الاتصال، ولا تشكل تعدادًا للمدارس الأهلية.

## 2.4 قواعد النشر والتحقق

لا ينشر اسم المنشأة على أنه مدرسة أهلية معتمدة إلا بعد التسوية مع مصدر رسمي أو تأكيد موثق من الجهة المالكة. وتحتاج الرسوم والمراحل التعليمية وحالة التشغيل ومعلومات الاتصال إلى مصدر مباشر مؤرخ. تمنع بيانات الطلاب والعاملين الفردية من الدخول إلى المستودع.

## المراجع

[1]: https://data.humdata.org/dataset/hotosm_yem_education_facilities "HDX — Education Facilities of Yemen"
[2]: https://www.unicef.org/yemen/education "UNICEF Yemen — Education"
