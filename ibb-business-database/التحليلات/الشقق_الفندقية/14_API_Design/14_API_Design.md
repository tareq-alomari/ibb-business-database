# المرحلة الرابعة عشرة: API Design - قطاع الشقق الفندقية في محافظة إب

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

## 14.2 قائمة النقاط (Endpoints)

### المصادقة (Auth)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| POST | `/auth/register` | تسجيل مستخدم جديد |
| POST | `/auth/login` | تسجيل الدخول |
| POST | `/auth/send-otp` | إرسال رمز التحقق |
| POST | `/auth/verify-otp` | التحقق من الرمز |

### المنشآت (Establishments)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| GET | `/establishments` | قائمة المنشآت |
| GET | `/establishments/<built-in function id>` | تفاصيل منشأة |
| GET | `/establishments/<built-in function id>/services` | الخدمات |
| GET | `/establishments/<built-in function id>/reviews` | التقييمات |
| GET | `/establishments/<built-in function id>/offers` | العروض |
| POST | `/establishments` | إضافة منشأة |
| PUT | `/establishments/<built-in function id>` | تحديث منشأة |

### الحجوزات (Bookings)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| POST | `/bookings` | إنشاء حجز |
| GET | `/bookings` | قائمة حجوزاتي |
| GET | `/bookings/<built-in function id>` | تفاصيل الحجز |
| PUT | `/bookings/<built-in function id>/cancel` | إلغاء الحجز |

### التقييمات (Reviews)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| POST | `/establishments/<built-in function id>/reviews` | إضافة تقييم |
| PUT | `/reviews/<built-in function id>` | تعديل تقييم |
| DELETE | `/reviews/<built-in function id>` | حذف تقييم |

### المستخدم (User)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| GET | `/users/me` | بياناتي |
| PUT | `/users/me` | تحديث بياناتي |
| GET | `/users/me/bookings` | حجوزاتي |

### العروض (Offers)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| GET | `/offers` | جميع العروض |
| POST | `/establishments/<built-in function id>/offers` | إضافة عرض |
| PUT | `/offers/<built-in function id>` | تعديل عرض |
| DELETE | `/offers/<built-in function id>` | حذف عرض |

## 14.3 WebSockets (Real-time)

| الحدث | الاتجاه | الوصف |
|-------|---------|-------|
| `booking.new` | Server → Establishment | حجز جديد |
| `booking.status` | Server → Customer | تحديث حالة الحجز |
| `notification` | Server → All | إشعار عام |

## 14.4 Rate Limiting

| النقطة | الحد | النافذة |
|--------|------|---------|
| جميع النقاط | 100 طلب | دقيقة |
| Auth | 5 طلبات | دقيقة |

---

## المصادر

- RESTful API Best Practices
- OpenAPI 3.0 Specification
