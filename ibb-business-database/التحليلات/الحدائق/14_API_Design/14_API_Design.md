# المرحلة الرابعة عشرة: API Design - قطاع الحدائق والمسطحات الخضراء في محافظة إب

> **التاريخ**: يوليو 2026  
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
| **التوثيق** | OpenAPI 3.0 (Swagger) |
| **Base URL** | `https://api.ibbservices.com/api/v1` |

## 14.2 قائمة النقاط (Endpoints)

### المصادقة (Auth)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| POST | /auth/register | تسجيل مستخدم جديد |
| POST | /auth/login | تسجيل الدخول (رقم الهاتف + كلمة مرور) |
| POST | /auth/send-otp | إرسال رمز التحقق |
| POST | /auth/verify-otp | التحقق من الرمز |
| POST | /auth/refresh | تجديد التوكن |
| POST | /auth/logout | تسجيل الخروج |

### مقدمي الخدمة (Service Providers)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| GET | /providers | قائمة مقدمي الخدمة (مع فلترة وبحث) |
| GET | /providers/{id} | تفاصيل مقدم الخدمة |
| GET | /providers/{id}/services | الخدمات المقدمة |
| GET | /providers/{id}/gallery | معرض الأعمال |
| GET | /providers/{id}/reviews | التقييمات |
| GET | /providers/{id}/offers | العروض |
| POST | /providers | إضافة مقدم خدمة جديد |
| PUT | /providers/{id} | تحديث البيانات |
| PATCH | /providers/{id}/toggle-status | تغيير حالة النشاط |

### الخدمات (Services)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| GET | /services | قائمة الخدمات |
| GET | /services/{id} | تفاصيل الخدمة |
| POST | /providers/{id}/services | إضافة خدمة |
| PUT | /services/{id} | تعديل خدمة |
| DELETE | /services/{id} | حذف خدمة |
| PATCH | /services/{id}/availability | تغيير توفر الخدمة |

### الحجوزات (Bookings)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| POST | /bookings | إنشاء حجز جديد |
| GET | /bookings | قائمة حجوزات المستخدم |
| GET | /bookings/{id} | تفاصيل الحجز |
| PUT | /bookings/{id}/cancel | إلغاء الحجز |
| PATCH | /bookings/{id}/status | تحديث حالة الحجز |
| GET | /providers/{id}/bookings | حجوزات مقدم الخدمة |

### التقييمات (Reviews)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| POST | /providers/{id}/reviews | إضافة تقييم |
| PUT | /reviews/{id} | تعديل تقييم |
| DELETE | /reviews/{id} | حذف تقييم |

### المستخدم (User)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| GET | /users/me | بيانات المستخدم الحالي |
| PUT | /users/me | تحديث البيانات |
| GET | /users/me/bookings | حجوزاتي السابقة |
| GET | /users/me/favorites | المفضلة |
| POST | /users/me/favorites | إضافة مفضلة |
| DELETE | /users/me/favorites/{id} | إزالة مفضلة |

### العروض (Offers)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| GET | /offers | جميع العروض الحالية |
| GET | /providers/{id}/offers | عروض مقدم خدمة محدد |
| POST | /providers/{id}/offers | إضافة عرض |
| PUT | /offers/{id} | تعديل عرض |
| DELETE | /offers/{id} | حذف عرض |

### البحث (Search)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| GET | /search | بحث عام |
| GET | /search/suggestions | اقتراحات البحث |

### الإدارة (Admin)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| GET | /admin/providers | جميع مقدمي الخدمة |
| PATCH | /admin/providers/{id}/approve | اعتماد مقدم خدمة |
| PATCH | /admin/providers/{id}/suspend | تعليق مقدم خدمة |
| GET | /admin/reports | تقارير شاملة |
| GET | /admin/reports/bookings | تقرير الحجوزات |
| GET | /admin/reports/revenue | تقرير الإيرادات |

## 14.3 WebSockets (Real-time)

| الحدث | الاتجاه | الوصف |
|-------|---------|-------|
| booking.new | Server → Provider | حجز جديد وصل |
| booking.status | Server → Customer | تحديث حالة الحجز |
| booking.status | Server → Provider | تحديث حالة الحجز |
| notification | Server → All | إشعار عام |

## 14.4 Rate Limiting

| النقطة | الحد | النافذة |
|--------|------|---------|
| جميع النقاط | 100 طلب | دقيقة |
| Auth (login, register) | 5 طلبات | دقيقة |
| Search | 60 طلب | دقيقة |

## 14.5 أمثلة الاستجابات

### نجاح
```json
{
  "success": true,
  "data": { ... },
  "message": null
}
```

### خطأ
```json
{
  "success": false,
  "data": null,
  "message": "وصف الخطأ",
  "errors": {
    "field": ["خطأ في الحقل"]
  }
}
```

### Pagination
```json
{
  "success": true,
  "data": [ ... ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "totalPages": 5
  }
}
```

---

## المصادر

- RESTful API Best Practices (Microsoft, Google)
- OpenAPI 3.0 Specification (swagger.io)
- WebSocket Protocol (RFC 6455)
