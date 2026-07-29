# تصميم API: منصة الحلويات في إب

## بنية API
RESTful API مع تنسيق JSON للتكامل مع التطبيقات الخارجية والواجهات الأمامية.

## المصادر (Endpoints)

### المستخدمين
- POST /api/auth/register - تسجيل مستخدم جديد
- POST /api/auth/login - تسجيل الدخول
- GET /api/users/profile - عرض الملف الشخصي
- PUT /api/users/profile - تحديث الملف الشخصي
- PUT /api/users/password - تغيير كلمة المرور

### المحلات
- GET /api/shops - عرض جميع المحلات (مع فلترة وبحث)
- GET /api/shops/:id - عرض تفاصيل محل
- POST /api/shops - إضافة محل جديد (للمالك)
- PUT /api/shops/:id - تحديث بيانات المحل
- GET /api/shops/:id/products - عرض منتجات المحل

### المنتجات
- GET /api/products - عرض المنتجات (مع فلترة)
- GET /api/products/:id - عرض تفاصيل منتج
- POST /api/products - إضافة منتج جديد
- PUT /api/products/:id - تحديث منتج
- DELETE /api/products/:id - حذف منتج

### الطلبات
- POST /api/orders - إنشاء طلب جديد
- GET /api/orders - عرض طلبات المستخدم
- GET /api/orders/:id - عرض تفاصيل طلب
- PUT /api/orders/:id/status - تحديث حالة الطلب
- PUT /api/orders/:id/cancel - إلغاء طلب

### التقييمات
- POST /api/reviews - إضافة تقييم
- GET /api/products/:id/reviews - عرض تقييمات منتج
- GET /api/shops/:id/reviews - عرض تقييمات محل

### التوصيل
- GET /api/deliveries/:id - تتبع حالة التوصيل
- PUT /api/deliveries/:id/status - تحديث حالة التوصيل

### لوحة التحكم
- GET /api/admin/dashboard - إحصائيات لوحة التحكم
- GET /api/admin/shops - إدارة المحلات
- GET /api/admin/orders - إدارة الطلبات

## التوثيق
- توثيق API عبر Swagger/OpenAPI
- نماذج طلب واستجابة لكل Endpoint
- رموز حالة وأخطاء موحدة
- أمثلة عملية للتكامل

## الأمان
- JWT Tokens للمصادقة
- Rate Limiting (100 طلب في الدقيقة)
- صلاحيات قائمة على الأدوار (Role-based)
- التحقق من صحة البيانات المدخلة
- تسجيل جميع العمليات (Logging)
