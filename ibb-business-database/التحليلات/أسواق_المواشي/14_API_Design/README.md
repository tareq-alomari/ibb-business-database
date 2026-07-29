# تصميم واجهات API – منصة أسواق المواشي

## الأسلوب المعماري
RESTful API مع توثيق OpenAPI/Swagger. تنسيق الطلب والاستجابة JSON.

## نقاط النهاية الرئيسية

### المصادقة
- POST /api/auth/register – تسجيل مستخدم جديد
- POST /api/auth/login – تسجيل الدخول
- POST /api/auth/verify – التحقق من رقم الهاتف
- POST /api/auth/reset-password – إعادة تعيين كلمة المرور

### الإعلانات
- GET /api/listings – قائمة الإعلانات (مع تصفية وفرز)
- GET /api/listings/:id – تفاصيل إعلان
- POST /api/listings – إضافة إعلان جديد
- PUT /api/listings/:id – تحديث إعلان
- DELETE /api/listings/:id – حذف إعلان
- POST /api/listings/:id/images – رفع صور

### المزادات
- GET /api/auctions – قائمة المزادات النشطة
- POST /api/auctions/:id/bid – تقديم مزايدة
- GET /api/auctions/:id/bids – سجل المزايدات

### الخدمات البيطرية
- POST /api/vet/reports – إضافة تقرير بيطري
- GET /api/vet/reports/:id – عرض تقرير
- GET /api/vet/doctors – قائمة الأطباء البيطريين

### المعاملات
- POST /api/transactions – إنشاء معاملة
- GET /api/transactions – سجل المعاملات
- PUT /api/transactions/:id/status – تحديث حالة المعاملة

### المستخدمون
- GET /api/users/profile – الملف الشخصي
- PUT /api/users/profile – تحديث الملف
- GET /api/users/:id/ratings – تقييمات المستخدم

## المصادقة والترخيص
JWT Tokens مع صلاحية 24 ساعة، Refresh Tokens، أدوار مستخدم (user, vet, admin).
