# تصميم API: نظام التأمين الرقمي

## نقاط النهاية العامة

| Method | Endpoint | الوصف |
|--------|----------|-------|
| GET | /api/v1/companies | قائمة شركات التأمين |
| GET | /api/v1/companies/{id} | تفاصيل شركة تأمين |
| GET | /api/v1/products | قائمة المنتجات التأمينية |
| GET | /api/v1/products/{id} | تفاصيل منتج تأميني |
| GET | /api/v1/products/search | بحث في المنتجات |
| GET | /api/v1/districts | قائمة المديريات |

## نقاط النهاية للمستخدمين المسجلين

| Method | Endpoint | الوصف |
|--------|----------|-------|
| POST | /api/v1/auth/register | تسجيل مستخدم |
| POST | /api/v1/auth/login | تسجيل دخول |
| GET | /api/v1/policies | وثائقي |
| POST | /api/v1/policies | إصدار وثيقة جديدة |
| GET | /api/v1/policies/{id} | تفاصيل وثيقة |
| POST | /api/v1/claims | تقديم مطالبة |
| GET | /api/v1/claims | مطالباتي |
| GET | /api/v1/claims/{id} | تفاصيل مطالبة |
| POST | /api/v1/payments | دفع قسط |

## معاملات البحث والفلترة

| المعامل | النوع | الوصف |
|---------|-------|-------|
| page | int | رقم الصفحة |
| limit | int | عدد النتائج |
| type | string | نوع التأمين |
| company_id | UUID | فلترة حسب الشركة |
| price_min | float | أقل سعر |
| price_max | float | أعلى سعر |
| q | string | نص البحث |

## تنسيق الرد
```json
{
  "success": true,
  "data": {
    "items": [...],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 50,
      "pages": 3
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
