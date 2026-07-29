# تصميم واجهات API: منصة الهدايا في إب

## البنية العامة
- RESTful API
- تنسيق JSON للاستجابة
- التوثيق عبر Swagger/OpenAPI

## نقاط النهاية الرئيسية

### المصادقة
- POST /api/auth/register - تسجيل مستخدم جديد
- POST /api/auth/login - تسجيل الدخول
- POST /api/auth/verify-otp - التحقق برمز OTP

### المنتجات
- GET /api/products - قائمة المنتجات (بحث، فلتر، تصفح)
- GET /api/products/:id - تفاصيل المنتج
- GET /api/categories - قائمة الفئات

### المحلات
- GET /api/shops - قائمة المحلات
- GET /api/shops/:id - تفاصيل المحل مع منتجاته
- PUT /api/shops/:id - تحديث بيانات المحل (للبائع)

### الطلبات
- POST /api/orders - إنشاء طلب جديد
- GET /api/orders - طلبات المستخدم
- GET /api/orders/:id - تفاصيل الطلب
- PUT /api/orders/:id/status - تحديث حالة الطلب

### التوصيل
- GET /api/deliveries - قائمة التوصيلات (للمندوب)
- PUT /api/deliveries/:id/status - تحديث حالة التوصيل

### التقييمات
- POST /api/reviews - إضافة تقييم
- GET /api/products/:id/reviews - تقييمات المنتج

## الأمان
- JWT (JSON Web Tokens) للمصادقة
- Rate limiting: 100 طلب/دقيقة للمستخدم
- HTTPS إلزامي لجميع الاتصالات
