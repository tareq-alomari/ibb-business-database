# المرحلة الرابعة عشرة: تصميم API - قطاع المخابز في محافظة إب

> **تاريخ التقرير**: يوليو 2026

---

## نقاط النهاية (Endpoints)

### المخابز

| الطريقة | المسار | الوصف |
|---------|--------|-------|
| GET | /api/bakeries | قائمة المخابز |
| GET | /api/bakeries/:id | تفاصيل مخبز |
| POST | /api/bakeries | إضافة مخبز |
| PUT | /api/bakeries/:id | تحديث مخبز |
| DELETE | /api/bakeries/:id | حذف مخبز |
| GET | /api/bakeries/search | بحث متقدم |

### التقييمات

| الطريقة | المسار | الوصف |
|---------|--------|-------|
| GET | /api/bakeries/:id/reviews | قائمة التقييمات |
| POST | /api/bakeries/:id/reviews | إضافة تقييم |
| PUT | /api/reviews/:id | تعديل تقييم |
| DELETE | /api/reviews/:id | حذف تقييم |

### المستخدمون

| الطريقة | المسار | الوصف |
|---------|--------|-------|
| POST | /api/auth/register | تسجيل مستخدم |
| POST | /api/auth/login | تسجيل الدخول |
| GET | /api/users/me | بياناتي |
| PUT | /api/users/me | تحديث بياناتي |

### الجغرافيا

| الطريقة | المسار |
|---------|--------|
| GET | /api/directorates |
| GET | /api/bakeries/nearby?lat=&lng=&radius= |

## تنسيق الاستجابة

```json
{
  "status": "success",
  "data": { ... },
  "meta": {
    "page": 1,
    "total": 150,
    "per_page": 20
  }
}
```

## المصادقة

- JWT (JSON Web Tokens)
- صلاحية 24 ساعة للتوكين
- Refresh Token للتجديد
- صلاحيات حسب الدور (أدمن، مستخدم)

## التوثيق

- واجهة Swagger UI
- أمثلة طلبات واستجابات
- رموز خطأ موحدة
- توثيق باللغة العربية