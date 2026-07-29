# تصميم واجهات API - منصة الحقائب في إب

## نمط API
- RESTful API مع JSON
- قاعدة URL: /api/v1/
- توثيق عبر Swagger/OpenAPI

## نقاط النهاية الرئيسية

### المصادقة
- POST /auth/register, /auth/login
- POST /auth/refresh, /auth/logout
- POST /auth/forgot-password

### المستخدمون
- GET, PUT /users/me
- GET /users/me/orders, /users/me/favorites

### المنتجات
- GET /products (مع فلترة وبحث)
- GET /products/{id}
- POST, PUT, DELETE /products/{id} (بائع)
- GET /products/{id}/reviews

### التصنيفات
- GET /categories
- GET /categories/{id}/products

### الطلبات
- POST /orders
- GET /orders, GET /orders/{id}
- PUT /orders/{id}/status
- PUT /orders/{id}/cancel

### التقييمات
- POST /products/{id}/reviews
- GET /products/{id}/reviews
- DELETE /reviews/{id}

### البائعون
- GET /sellers/{id}
- GET /sellers/{id}/products
- PUT /sellers/me
- GET /sellers/me/orders, /sellers/me/stats

### الإشعارات
- GET /notifications
- PUT /notifications/{id}/read
- DELETE /notifications/{id}

## معايير الأمان
- JWT Tokens مع صلاحية محددة
- Refresh Tokens لتجديد الجلسات
- Rate Limiting (١٠٠ طلب/دقيقة)
- CORS محدود للنطاقات المسموحة
- التحقق من صحة البيانات (Validation)

## استراتيجية التخزين المؤقت
- ذاكرة تخزين مؤقت للمنتجات الأكثر مشاهدة
- تخزين مؤقت للتصنيفات مع تحديث كل ٥ دقائق
