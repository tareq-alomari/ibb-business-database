# المرحلة الرابعة عشرة: API Design - قطاع المطاعم في محافظة إب

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
| **Base URL** | `https://api.ibbrestaurants.com/api/v1` |

## 14.2 رؤوس HTTP (Headers)

| الرأس | القيمة | إجباري |
|-------|--------|--------|
| `Content-Type` | `application/json` | نعم |
| `Authorization` | `Bearer <token>` | نعم (للنقاط المحمية) |
| `Accept-Language` | `ar`, `en` | لا (افتراضي: ar) |
| `X-Device-ID` | `device-uuid` | نعم (للإشعارات) |

## 14.3 الاستجابات الموحدة

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

## 14.4 قائمة النقاط (Endpoints)

### المصادقة (Auth)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| POST | `/auth/register` | تسجيل مستخدم جديد |
| POST | `/auth/login` | تسجيل الدخول (رقم الهاتف + كلمة مرور) |
| POST | `/auth/send-otp` | إرسال رمز التحقق |
| POST | `/auth/verify-otp` | التحقق من الرمز |
| POST | `/auth/refresh` | تجديد التوكن |
| POST | `/auth/logout` | تسجيل الخروج |

### المطاعم (Restaurants)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| GET | `/restaurants` | قائمة المطاعم (مع فلترة وبحث) |
| GET | `/restaurants/{id}` | تفاصيل مطعم |
| GET | `/restaurants/{id}/menu` | المنيو الكامل للمطعم |
| GET | `/restaurants/{id}/reviews` | تقييمات المطعم |
| GET | `/restaurants/{id}/offers` | عروض المطعم |
| POST | `/restaurants` | إضافة مطعم جديد (owner) |
| PUT | `/restaurants/{id}` | تحديث بيانات المطعم (owner) |
| PATCH | `/restaurants/{id}/toggle-status` | فتح/إغلاق المطعم |

### البحث (Search)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| GET | `/search` | بحث عام (مطاعم، أطباق) |
| GET | `/search/suggestions` | اقتراحات البحث |

### المنيو (Menu)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| GET | `/restaurants/{id}/categories` | تصنيفات المنيو |
| POST | `/restaurants/{id}/categories` | إضافة تصنيف |
| PUT | `/categories/{id}` | تعديل تصنيف |
| DELETE | `/categories/{id}` | حذف تصنيف |
| POST | `/categories/{id}/items` | إضافة صنف |
| PUT | `/menu-items/{id}` | تعديل صنف |
| DELETE | `/menu-items/{id}` | حذف صنف |
| PATCH | `/menu-items/{id}/availability` | تغيير توفر صنف |

### الطلبات (Orders)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| POST | `/orders` | إنشاء طلب جديد |
| GET | `/orders` | قائمة طلبات المستخدم |
| GET | `/orders/{id}` | تفاصيل الطلب |
| PUT | `/orders/{id}/cancel` | إلغاء الطلب |
| GET | `/restaurants/{id}/orders` | طلبات المطعم (owner) |
| PATCH | `/orders/{id}/status` | تحديث حالة الطلب (owner/driver) |

### التوصيل (Delivery)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| GET | `/drivers/available-orders` | الطلبات المتاحة (driver) |
| POST | `/drivers/assign` | قبول طلب توصيل (driver) |
| PATCH | `/deliveries/{id}/status` | تحديث حالة التوصيل |
| GET | `/deliveries/{id}/track` | تتبع التوصيل (location) |

### التقييمات (Reviews)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| POST | `/restaurants/{id}/reviews` | إضافة تقييم |
| PUT | `/reviews/{id}` | تعديل تقييم |
| DELETE | `/reviews/{id}` | حذف تقييم |
| GET | `/reviews/{id}` | تفاصيل تقييم |

### المستخدم (User)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| GET | `/users/me` | بيانات المستخدم الحالي |
| PUT | `/users/me` | تحديث البيانات |
| GET | `/users/me/addresses` | عناويني |
| POST | `/users/me/addresses` | إضافة عنوان |
| PUT | `/addresses/{id}` | تعديل عنوان |
| DELETE | `/addresses/{id}` | حذف عنوان |
| GET | `/users/me/orders` | طلباتي السابقة |
| GET | `/users/me/favorites` | المطاعم المفضلة |
| POST | `/users/me/favorites` | إضافة مفضلة |
| DELETE | `/users/me/favorites/{id}` | إزالة مفضلة |

### العروض (Offers)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| GET | `/offers` | جميع العروض الحالية |
| GET | `/restaurants/{id}/offers` | عروض مطعم محدد |
| POST | `/restaurants/{id}/offers` | إضافة عرض (owner) |
| PUT | `/offers/{id}` | تعديل عرض |
| DELETE | `/offers/{id}` | حذف عرض |

### الإعلانات (Admin)

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| GET | `/admin/restaurants` | جميع المطاعم |
| PATCH | `/admin/restaurants/{id}/approve` | اعتماد مطعم |
| PATCH | `/admin/restaurants/{id}/suspend` | تعليق مطعم |
| GET | `/admin/reports` | تقارير شاملة |
| GET | `/admin/reports/orders` | تقرير الطلبات |
| GET | `/admin/reports/revenue` | تقرير الإيرادات |

## 14.5 WebSockets (Real-time)

| الحدث | الاتجاه | الوصف |
|-------|---------|-------|
| `order.new` | Server → Restaurant | طلب جديد وصل |
| `order.status` | Server → Customer | تحديث حالة الطلب |
| `order.status` | Server → Driver | تحديث حالة الطلب |
| `driver.location` | Driver → Server | تحديث موقع السائق |
| `driver.location` | Server → Customer | إرسال موقع السائق للزبون |
| `notification` | Server → All | إشعار عام |

## 14.6 Rate Limiting

| النقطة | الحد | النافذة |
|--------|------|---------|
| جميع النقاط | 100 طلب | دقيقة |
| Auth (login, register) | 5 طلبات | دقيقة |
| Search | 60 طلب | دقيقة |
| WebSocket | 1 اتصال | مستخدم |

## 14.7 أمثلة الطلبات

### طلب: تسجيل الدخول
```
POST /api/v1/auth/login
Content-Type: application/json

{
  "phone": "777123456",
  "password": "secure_password"
}
```

### الاستجابة
```json
{
  "success": true,
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIs...",
    "refreshToken": "eyJhbGciOiJIUzI1NiIs...",
    "user": {
      "id": "uuid",
      "name": "أحمد محمد",
      "phone": "777123456",
      "role": "customer"
    }
  }
}
```

### طلب: قائمة المطاعم مع فلترة
```
GET /api/v1/restaurants?type=grill&lat=13.97&lng=44.17&radius=10&page=1&limit=20
```

---

## المصادر

- RESTful API Best Practices (Microsoft, Google)
- OpenAPI 3.0 Specification (swagger.io)
- تويتر API، Talabat API (نماذج مرجعية)
- WebSocket Protocol (RFC 6455)