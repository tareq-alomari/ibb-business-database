# تصميم API: منصة رياض الأطفال في إب

> **تاريخ التصميم**: يوليو 2026

---

## REST API – النقاط العامة

| الطريقة | المسار | الوصف |
|---------|--------|-------|
| GET | /api/v1/kindergartens | قائمة الرياض |
| GET | /api/v1/kindergartens/{id} | تفاصيل روضة |
| GET | /api/v1/kindergartens/search | بحث في الرياض |
| GET | /api/v1/districts | قائمة المديريات |
| GET | /api/v1/kindergartens/{id}/reviews | تقييمات روضة |
| GET | /api/v1/kindergartens/{id}/levels | مستويات روضة |
| GET | /api/v1/kindergartens/{id}/activities | أنشطة روضة |

## النقاط المصادق عليها

| الطريقة | المسار | الوصف |
|---------|--------|-------|
| POST | /api/v1/auth/register | تسجيل مستخدم |
| POST | /api/v1/auth/login | تسجيل دخول |
| POST | /api/v1/reviews | إضافة تقييم |
| PUT | /api/v1/reviews/{id} | تعديل تقييم |
| DELETE | /api/v1/reviews/{id} | حذف تقييم |
| POST | /api/v1/kindergartens | إضافة روضة (Admin) |
| PUT | /api/v1/kindergartens/{id} | تعديل روضة (Admin) |

## معاملات البحث

| المعامل | النوع | الوصف |
|---------|-------|-------|
| q | string | نص البحث |
| district_id | UUID | تصفية حسب المديرية |
| curriculum | string | تصفية حسب المنهج |
| min_fee | int | الحد الأدنى للرسوم |
| max_fee | int | الحد الأعلى للرسوم |
| levels | string[] | المستويات (KG1, KG2, KG3) |
| sort | string | ترتيب (rating, fee, name) |
| page | int | رقم الصفحة |
| limit | int | عدد النتائج |

## تنسيق الاستجابة

```json
{
  "success": true,
  "data": { },
  "meta": {
    "request_id": "uuid",
    "timestamp": "2026-07-29T10:00:00Z"
  }
}
```
