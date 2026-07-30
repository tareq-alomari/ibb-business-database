# المرحلة الرابعة عشرة: API Design - قطاع عيادات ومراكز الأسنان في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 14_API_Design.md

---

## 14.1 مواصفات API العامة

| الخاصية | القيمة |
|---------|--------|
| النمط | RESTful API |
| الصيغة | JSON |
| البروتوكول | HTTPS |
| الإصدار | `/api/v1/` |
| المصادقة | JWT (Bearer Token) |
| Base URL | `https://api.ibbdentistry.com/api/v1` |

## 14.2 النقاط الرئيسية

### Auth
- POST /auth/register, /auth/login, /auth/send-otp, /auth/verify-otp

### Entities
- GET /entities, GET /entities/:id, POST /entities, PUT /entities/:id
- GET /entities/:id/services, GET /entities/:id/reviews, GET /entities/:id/offers

### Services
- POST /entities/:id/categories, PUT /categories/:id
- POST /categories/:id/services, PUT /services/:id

### Reviews
- POST /entities/:id/reviews, PUT /reviews/:id

### Admin
- GET /admin/entities, PATCH /admin/entities/:id/approve

---
