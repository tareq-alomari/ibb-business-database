# المرحلة الرابعة عشرة: API Design - قطاع البصريات في محافظة إب

> **التاريخ**:  يوليو 2026  
> **الملف**: 14_API_Design.md

---

## 14.1 مواصفات API العامة

| الخاصية | القيمة |
|---------|--------|
| **النمط** | RESTful API |
| **الصيغة** | JSON |
| **البروتوكول** | HTTPS |
| **الإصدار** | `/api/v1/` |
| **المصادقة** | JWT (Bearer Token) |

## 14.2 قائمة النقاط (Endpoints)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| POST | `/auth/register` | مصادقة |
| POST | `/auth/login` | مصادقة |
| POST | `/auth/send-otp` | مصادقة |
| POST | `/auth/verify-otp` | مصادقة |
| POST | `/auth/refresh` | مصادقة |
| GET/POST | `/opticals` | إدارة opticals |
| GET/POST | `/services` | إدارة services |
| GET/POST | `/lenses` | إدارة lenses |
| GET/POST | `/brands` | إدارة brands |
| GET/POST | `/appointments` | إدارة appointments |
| GET | `/reviews` | إدارة reviews |
| GET/POST | `/prescriptions` | إدارة prescriptions |
| GET/POST | `/prices` | إدارة prices |

## 14.3 الاستجابات الموحدة

### نجاح
```json
{"success": true, "data": {...}, "message": null}
```

### خطأ
```json
{"success": false, "data": null, "message": "وصف الخطأ"}
```

## 14.4 Rate Limiting

| النقطة | الحد | النافذة |
|--------|------|---------|
| جميع النقاط | 100 طلب | دقيقة |
| Auth | 5 طلبات | دقيقة |

---

## المصادر

- RESTful API Best Practices
- OpenAPI 3.0 Specification
