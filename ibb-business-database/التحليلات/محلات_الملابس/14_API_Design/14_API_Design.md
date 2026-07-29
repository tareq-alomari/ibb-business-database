# تصميم API: منصة محلات الملابس الرقمية

## نقاط النهاية العامة

| Method | Endpoint | الوصف |
|--------|----------|-------|
| GET | /api/v1/stores | قائمة المحلات |
| GET | /api/v1/stores/{id} | تفاصيل محل |
| GET | /api/v1/stores/{id}/products | منتجات محل معين |
| GET | /api/v1/products | قائمة المنتجات |
| GET | /api/v1/products/{id} | تفاصيل منتج |
| GET | /api/v1/products/search | بحث في المنتجات |
| GET | /api/v1/products/category/{cat} | منتجات حسب القسم |
| GET | /api/v1/districts | قائمة المديريات |
| GET | /api/v1/categories | قائمة التصنيفات |

## نقاط النهاية للمستخدمين المسجلين

| Method | Endpoint | الوصف |
|--------|----------|-------|
| POST | /api/v1/auth/register | تسجيل مستخدم |
| POST | /api/v1/auth/login | تسجيل دخول |
| POST | /api/v1/orders | إنشاء طلب |
| GET | /api/v1/orders | طلباتي |
| GET | /api/v1/orders/{id} | تفاصيل طلب |
| PUT | /api/v1/orders/{id}/cancel | إلغاء طلب |
| POST | /api/v1/reviews | تقييم منتج |

## نقاط النهاية للمحلات

| Method | Endpoint | الوصف |
|--------|----------|-------|
| GET | /api/v1/store/orders | طلبات المحل |
| PUT | /api/v1/store/orders/{id}/status | تحديث حالة الطلب |
| POST | /api/v1/store/products | إضافة منتج |
| PUT | /api/v1/store/products/{id} | تعديل منتج |
| DELETE | /api/v1/store/products/{id} | حذف منتج |

## معاملات البحث والفلترة

| المعامل | النوع | الوصف |
|---------|-------|-------|
| page | int | رقم الصفحة |
| limit | int | عدد النتائج |
| category | string | تصنيف المنتج |
| gender | string | الجنس |
| price_min | float | أقل سعر |
| price_max | float | أعلى سعر |
| size | string | المقاس |
| q | string | نص البحث |