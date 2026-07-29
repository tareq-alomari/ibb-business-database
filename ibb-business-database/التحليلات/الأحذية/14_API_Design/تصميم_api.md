# تصميم API: منصة الأحذية في إب

## بنية API
RESTful API مع تنسيق JSON للاستجابة.

## نقاط النهاية (Endpoints)

### المصادقة (Authentication)
- POST /api/auth/register - تسجيل مستخدم جديد
- POST /api/auth/login - تسجيل الدخول
- POST /api/auth/logout - تسجيل الخروج
- POST /api/auth/forgot-password - استعادة كلمة المرور
- GET /api/auth/profile - عرض الملف الشخصي
- PUT /api/auth/profile - تحديث الملف الشخصي

### المنتجات (Products)
- GET /api/products - قائمة المنتجات (مع دعم الفلترة والبحث والترتيب)
- GET /api/products/:id - تفاصيل منتج
- POST /api/products - إضافة منتج جديد (محمي)
- PUT /api/products/:id - تحديث منتج (محمي مالك)
- DELETE /api/products/:id - حذف منتج (محمي مالك)
- GET /api/products/:id/reviews - مراجعات منتج

### الفئات (Categories)
- GET /api/categories - قائمة الفئات
- GET /api/categories/:id - فئة مع منتجاتها
- POST /api/categories - إضافة فئة (محمي مشرف)
- PUT /api/categories/:id - تحديث فئة (محمي مشرف)
- DELETE /api/categories/:id - حذف فئة (محمي مشرف)

### الطلبات (Orders)
- GET /api/orders - قائمة طلبات المستخدم
- POST /api/orders - إنشاء طلب جديد
- GET /api/orders/:id - تفاصيل طلب
- PUT /api/orders/:id/status - تحديث حالة طلب (محمي تاجر)
- GET /api/orders/:id/track - تتبع الطلب

### المتاجر (Stores)
- GET /api/stores - قائمة المتاجر
- GET /api/stores/:id - تفاصيل متجر مع منتجاته
- POST /api/stores - تسجيل متجر جديد (محمي)
- PUT /api/stores/:id - تحديث بيانات المتجر (محمي)

### سلة التسوق (Cart)
- GET /api/cart - عرض السلة
- POST /api/cart/add - إضافة منتج للسلة
- PUT /api/cart/:id - تحديث كمية منتج في السلة
- DELETE /api/cart/:id - حذف منتج من السلة

## معايير الأمان
- JWT Tokens للمصادقة
- Rate Limiting لمنع الاستخدام المسيء
- صحة البيانات عبر Validators
- HTTPS في كل الاتصالات