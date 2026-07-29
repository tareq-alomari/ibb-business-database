# تصميم API - قطاع الأثاث في محافظة إب

---

## نقاط النهاية العامة

| الطريقة | المسار | الوصف |
|---------|--------|-------|
| GET | /api/v1/businesses | قائمة المعارض |
| GET | /api/v1/businesses/{id} | تفاصيل معرض |
| GET | /api/v1/businesses/search | بحث في المعارض |
| GET | /api/v1/products | قائمة المنتجات |
| GET | /api/v1/products/{id} | تفاصيل منتج |
| GET | /api/v1/products/search | بحث في المنتجات |
| GET | /api/v1/categories | قائمة التصنيفات |
| GET | /api/v1/districts | قائمة المديريات |
| GET | /api/v1/reviews/business/{id} | تقييمات معرض |

## نقاط النهاية للمستخدمين المسجلين

| الطريقة | المسار | الوصف |
|---------|--------|-------|
| POST | /api/v1/auth/register | تسجيل مستخدم |
| POST | /api/v1/auth/login | تسجيل دخول |
| POST | /api/v1/reviews | إضافة تقييم |
| PUT | /api/v1/reviews/{id} | تعديل تقييم |
| DELETE | /api/v1/reviews/{id} | حذف تقييم |
| POST | /api/v1/businesses | إضافة معرض |
| PUT | /api/v1/businesses/{id} | تحديث معرض |

## معاملات البحث

| المعامل | النوع | الوصف |
|---------|-------|-------|
| page | int | رقم الصفحة |
| limit | int | عدد النتائج |
| sort | string | ترتيب (name, rating, price) |
| category_id | UUID | تصفية حسب التصنيف |
| district_id | UUID | تصفية حسب المديرية |
| min_price | float | أقل سعر |
| max_price | float | أعلى سعر |
| q | string | نص البحث |
| lat, lng | float | إحداثيات للبحث الجغرافي |
| radius | int | نصف قطر البحث (km) |

## تنسيق الاستجابة

```json
{
  "success": true,
  "data": {
    "items": [],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 250,
      "pages": 13
    }
  }
}
```

## معالجة الأخطاء

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "بيانات غير صالحة",
    "details": []
  }
}
```
