# تصميم واجهة برمجة التطبيقات (API)

## النهج العام
RESTful API مع توثيق باستخدام Swagger/OpenAPI.

## نقاط النهاية الرئيسية

### المصادقة
- POST /api/auth/register
- POST /api/auth/login
- POST /api/auth/verify-otp
- POST /api/auth/forgot-password

### المستخدمون
- GET /api/users/profile
- PUT /api/users/profile
- GET /api/users/{id}

### المنتجات
- GET /api/products
- GET /api/products/{id}
- POST /api/products
- PUT /api/products/{id}
- DELETE /api/products/{id}
- GET /api/products/search?q=

### الأسواق
- GET /api/markets
- GET /api/markets/{id}
- GET /api/markets/{id}/products

### الطلبات
- POST /api/orders
- GET /api/orders
- GET /api/orders/{id}
- PUT /api/orders/{id}/status

### الأسعار
- GET /api/prices
- GET /api/prices/current
- GET /api/prices/history?product_id=&period=

### التقييمات
- POST /api/reviews
- GET /api/reviews/{product_id}

## تنسيق الاستجابة
```json
{
  "success": true,
  "data": {},
  "message": "",
  "errors": []
}
```

## معايير الأمان
- JWT للتوثيق (صلاحية 24 ساعة)
- Rate Limiting: 100 طلب/دقيقة
- التحقق من صحة الإدخال (Validation)
- حماية SQL Injection

## الأخطاء الشائعة
- 400: طلب غير صالح
- 401: غير مصرح
- 404: غير موجود
- 429: تجاوز الحد المسموح
- 500: خطأ في الخادم