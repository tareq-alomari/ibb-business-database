# تصميم واجهات API - المدارس الأهلية في إب

## نمط العمارة
RESTful API مع تنسيق JSON للطلبات والاستجابات

## المصادقة
JWT (JSON Web Tokens) مع صلاحيات حسب الدور (مدير، مشرف، معلم، ولي أمر)

## نقاط النهاية الرئيسية

### المدارس
```
GET  /api/schools                    ← قائمة المدارس (مع بحث وفلترة)
GET  /api/schools/:id                ← تفاصيل مدرسة معينة
POST /api/schools                    ← إضافة مدرسة جديدة
PUT  /api/schools/:id                ← تحديث بيانات مدرسة
DELETE /api/schools/:id              ← حذف مدرسة
```

### الطلاب
```
GET    /api/students                 ← قائمة الطلاب
GET    /api/students/:id             ← تفاصيل طالب
POST   /api/students                 ← تسجيل طالب جديد
PUT    /api/students/:id             ← تحديث بيانات طالب
PATCH  /api/students/:id/status      ← تحديث حالة الطالب
GET    /api/students/:id/grades      ← درجات الطالب
```

### المراحل
```
GET  /api/schools/:id/levels         ← مراحل مدرسة معينة
POST /api/schools/:id/levels         ← إضافة مرحلة
```

### الرسوم
```
GET    /api/students/:id/fees        ← سجل الرسوم لطالب
POST   /api/fees                     ← تسجيل دفعة
GET    /api/fees/summary             ← ملخص التحصيل
```

### الامتحانات والدرجات
```
GET    /api/exams                    ← قائمة الامتحانات
POST   /api/exams                    ← إضافة امتحان
POST   /api/grades                   ← إدخال درجات
GET    /api/exams/:id/grades         ← درجات امتحان
```

### التقارير
```
GET  /api/reports/students-count     ← إحصاء عدد الطلاب
GET  /api/reports/fees-collection    ← إحصاء التحصيل المالي
GET  /api/reports/schools-summary    ← ملخص المدارس
```

## استجابات خطأ موحدة
```json
{
  "error": true,
  "message": "...",
  "code": "ERR_001"
}
```