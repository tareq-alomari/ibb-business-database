# المرحلة الرابعة عشرة: API Design - قطاع المؤسسات التنموية في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 14_API_Design.md

---

## 14.1 نظرة عامة

| الخاص | القيمة |
|--------|-------|
| النمط | RESTful API |
| التنسيق | JSON |
| البروتوكول | HTTPS |
| الإصدار | v1 |
| التوثيق | Swagger/OpenAPI 3.0 |

## 14.2 نقاط النهاية

### Auth

| الطريقة | المسار |
|--------|--------|
| POST | /api/v1/auth/register |
| POST | /api/v1/auth/login |
| POST | /api/v1/auth/verify-otp |
| POST | /api/v1/auth/refresh |

### Services

| الطريقة | المسار |
|--------|--------|
| GET | /api/v1/services |
| GET | /api/v1/services/:id |
| POST | /api/v1/services |
| PUT | /api/v1/services/:id |
| DELETE | /api/v1/services/:id |

### Bookings

| الطريقة | المسار |
|--------|--------|
| GET | /api/v1/bookings |
| POST | /api/v1/bookings |
| PUT | /api/v1/bookings/:id |
| DELETE | /api/v1/bookings/:id |

## 14.3 نموذج الاستجابة

```json
{ "success": true, "data": {}, "message": "تمت العملية" }
```

## 14.4 معالجة الأخطاء

| الرمز | المعنى |
|------|--------|
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 409 | Conflict |
| 429 | Too Many Requests |
| 500 | Internal Server Error |

---

## المصادر

1. الجهاز المركزي للإحصاء اليمني
2. غرفة تجارة وصناعة محافظة إب
3. مسح ميداني تقديري لـقطاع المؤسسات التنموية في محافظة إب
4. مقابلات محلية مع مقدمي الخدمة والمستفيدين
