# المرحلة الرابعة عشرة: API Design - قطاع المستشفيات في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 14_API_Design.md

---

## 14.1 API Overview

| العنصر | القيمة |
|--------|--------|
| **Base URL** | `https://api.ibb-health.com/v1` |
| **Protocol** | HTTPS |
| **Format** | JSON |
| **Authentication** | JWT Bearer Token |
| **Rate Limit** | 100 req/min (public), 500 req/min (authenticated) |

## 14.2 Endpoints

### Public Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/hospitals` | قائمة المستشفيات |
| GET | `/hospitals/{id}` | تفاصيل مستشفى |
| GET | `/hospitals/search` | بحث متقدم |
| GET | `/hospitals/nearby` | أقرب المستشفيات |
| GET | `/specialties` | قائمة التخصصات |
| GET | `/districts` | قائمة المديريات |
| GET | `/doctors` | قائمة الأطباء |
| GET | `/doctors/{id}` | تفاصيل طبيب |
| GET | `/hospitals/{id}/reviews` | تقييمات المستشفى |
| GET | `/stats` | إحصائيات عامة |

### Authenticated Endpoints (User)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | تسجيل مستخدم |
| POST | `/auth/login` | تسجيل دخول |
| POST | `/auth/refresh` | تجديد التوكن |
| POST | `/hospitals/{id}/reviews` | إضافة تقييم |
| PUT | `/reviews/{id}` | تعديل تقييم |
| DELETE | `/reviews/{id}` | حذف تقييم |
| POST | `/appointments` | حجز موعد |
| GET | `/appointments` | مواعيدي |
| PUT | `/appointments/{id}` | تعديل موعد |
| DELETE | `/appointments/{id}` | إلغاء موعد |
| GET | `/profile` | ملفي الشخصي |
| PUT | `/profile` | تحديث ملفي |

### Admin Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/hospitals` | إضافة مستشفى |
| PUT | `/hospitals/{id}` | تعديل مستشفى |
| DELETE | `/hospitals/{id}` | حذف مستشفى |
| GET | `/reviews/pending` | تقييمات معلقة |
| PUT | `/reviews/{id}/approve` | الموافقة على تقييم |
| DELETE | `/reviews/{id}` | حذف تقييم |
| GET | `/users` | قائمة المستخدمين |
| PUT | `/users/{id}/role` | تعديل دور مستخدم |
| GET | `/reports/hospitals` | تقرير المستشفيات |
| GET | `/reports/districts` | تقرير المديريات |

## 14.3 Request/Response Examples

### GET /hospitals

```json
// Request
GET /api/v1/hospitals?district=ibb&type=government&page=1&limit=10

// Response
{
  "success": true,
  "data": [
    {
      "id": "uuid-1",
      "name_ar": "هيئة مستشفى الثورة العام",
      "type": "government",
      "district": "الظهار",
      "phone": "04-XXX XXX",
      "avg_rating": 4.2,
      "review_count": 45,
      "has_emergency_24h": true,
      "latitude": 14.0884,
      "longitude": 44.1771
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 160,
    "pages": 16
  }
}
```

### GET /hospitals/nearby

```json
// Request
GET /api/v1/hospitals/nearby?lat=14.0884&lng=44.1771&radius=10

// Response
{
  "success": true,
  "data": [
    {
      "id": "uuid-1",
      "name_ar": "هيئة مستشفى الثورة العام",
      "distance_km": 0.5,
      "avg_rating": 4.2
    }
  ]
}
```

### POST /hospitals/{id}/reviews

```json
// Request
POST /api/v1/hospitals/uuid-1/reviews
Authorization: Bearer <token>
{
  "rating": 4,
  "comment": "خدمة جيدة، الكادر متعاون"
}

// Response
{
  "success": true,
  "data": {
    "id": "uuid-review",
    "hospital_id": "uuid-1",
    "rating": 4,
    "comment": "خدمة جيدة، الكادر متعاون",
    "status": "pending",
    "created_at": "2026-07-29T10:00:00Z"
  }
}
```

## 14.4 Error Handling

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "بيانات غير صالحة",
    "details": [
      {
        "field": "rating",
        "message": "التقييم يجب أن يكون بين 1 و 5"
      }
    ]
  },
  "meta": {
    "request_id": "req-uuid",
    "timestamp": "2026-07-29T10:00:00Z"
  }
}
```

### Error Codes

| الكود | HTTP Status | المعنى |
|-------|-------------|--------|
| VALIDATION_ERROR | 422 | بيانات غير صالحة |
| NOT_FOUND | 404 | غير موجود |
| UNAUTHORIZED | 401 | غير مصرح |
| FORBIDDEN | 403 | لا تملك صلاحية |
| RATE_LIMITED | 429 | تجاوزت الحد المسموح |
| INTERNAL_ERROR | 500 | خطأ داخلي |

## 14.5 API Authentication

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

| المعلومة | القيمة |
|---------|--------|
| توكن الوصول | 24 ساعة |
| توكن التحديث | 7 أيام |
| خوارزمية | HS256 |
| تخزين التوكن | HttpOnly Cookie + LocalStorage |

## 14.6 API Documentation

توثيق API سيكون متاحًا عبر:
- **Swagger UI**: `/api/v1/docs`
- **OpenAPI 3.0 Spec**: `/api/v1/openapi.json`
- **Postman Collection**: للتحميل