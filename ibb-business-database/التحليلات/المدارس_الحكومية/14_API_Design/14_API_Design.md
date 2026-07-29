# تصميم واجهة برمجة التطبيقات (API)

## النمط المعماري
RESTful API مع تنسيق JSON للاستجابة. استخدام الإصدار الأول من API عبر البادئة /api/v1/.

## التوثيق والاعتماد
JWT (JSON Web Tokens) للمصادقة. صلاحيات مختلفة حسب الدور الوظيفي.

## نقاط النهاية الرئيسية

### المدارس
- GET /api/v1/schools – قائمة المدارس (مع دعم التصفية والصفحات)
- GET /api/v1/schools/{id} – تفاصيل مدرسة محددة
- POST /api/v1/schools – إضافة مدرسة جديدة (يتطلب صلاحية مشرف)
- PUT /api/v1/schools/{id} – تحديث بيانات مدرسة
- DELETE /api/v1/schools/{id} – حذف مدرسة

### المعلمون
- GET /api/v1/teachers – قائمة المعلمين
- GET /api/v1/teachers/{id} – تفاصيل معلم
- POST /api/v1/teachers – إضافة معلم جديد
- PUT /api/v1/teachers/{id} – تحديث بيانات معلم
- GET /api/v1/teachers/{id}/salary – سجل رواتب المعلم

### الطلاب
- GET /api/v1/students – قائمة الطلاب
- GET /api/v1/students/{id} – تفاصيل طالب
- POST /api/v1/students – تسجيل طالب جديد
- PUT /api/v1/students/{id} – تحديث بيانات طالب

### التقارير
- GET /api/v1/reports/schools-summary – ملخص المدارس
- GET /api/v1/reports/district/{id} – تقرير مديرية محددة
- GET /api/v1/reports/salaries-summary – ملخص الرواتب

### المصادقة
- POST /api/v1/auth/login – تسجيل الدخول
- POST /api/v1/auth/logout – تسجيل الخروج
- POST /api/v1/auth/refresh – تحديث التوكن

## رموز الاستجابة
- 200: نجاح
- 201: إنشاء جديد
- 400: خطأ في الطلب
- 401: غير مخول
- 404: غير موجود
- 500: خطأ في الخادم
