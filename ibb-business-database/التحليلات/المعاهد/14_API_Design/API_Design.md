# تصميم واجهات API - قطاع المعاهد (إب)

## نقاط النهاية الرئيسية

### المعاهد
```
GET    /api/institutes              ← قائمة جميع المعاهد (مع فلاتر)
GET    /api/institutes/{id}         ← تفاصيل معهد معين
POST   /api/institutes              ← إضافة معهد جديد (مشرف)
PUT    /api/institutes/{id}         ← تحديث بيانات معهد (مدير المعهد)
DELETE /api/institutes/{id}         ← حذف معهد (مشرف)
```

### التخصصات
```
GET    /api/specializations         ← قائمة التخصصات (مع فلترة حسب المعهد)
GET    /api/specializations/{id}    ← تفاصيل تخصص
POST   /api/specializations         ← إضافة تخصص
PUT    /api/specializations/{id}    ← تحديث تخصص
DELETE /api/specializations/{id}    ← حذف تخصص
```

### الطلاب والتقديم
```
POST   /api/auth/register           ← تسجيل طالب جديد
POST   /api/auth/login              ← تسجيل دخول
GET    /api/students/profile        ← ملف الطالب
PUT    /api/students/profile        ← تحديث الملف
POST   /api/applications            ← تقديم طلب التحاق
GET    /api/applications            ← استعلام عن طلباتي
PUT    /api/applications/{id}       ← تحديث حالة الطلب (للمعهد)
```

### التقييمات
```
GET    /api/institutes/{id}/reviews ← تقييمات المعهد
POST   /api/institutes/{id}/reviews ← إضافة تقييم
```

### المقارنة
```
POST   /api/compare                 ← مقارنة بين 2-3 معاهد
```

### الإدارة
```
GET    /api/admin/stats             ← إحصائيات عامة
GET    /api/admin/institutes/{id}/stats ← إحصائيات معهد محدد
GET    /api/admin/reports           ← تصدير تقارير
```

## التنسيق
- جميع الاستجابات بصيغة JSON
- دعم pagination عبر `page` و `limit`
- أخطاء موحدة: `{ "error": { "code": "...", "message": "..." } }`
- توثيق عبر Swagger/OpenAPI
