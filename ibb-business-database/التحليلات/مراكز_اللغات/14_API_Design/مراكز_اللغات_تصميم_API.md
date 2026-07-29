# تصميم API: قطاع مراكز اللغات في إب

## نظرة عامة
API RESTful لإدارة مراكز اللغات، يدعم العمليات الأساسية لإدارة الطلاب والدورات والمدفوعات.

## نقطة النهاية الأساسية
```
BASE_URL: https://api.ibblangcenters.com/v1
```

## المصادقة
- JWT Tokens
- صلاحيات: Admin، Manager، Trainer، Student

## نقاط النهاية الرئيسية

### Centers
```
GET    /centers                 قائمة المراكز
GET    /centers/{id}            تفاصيل مركز
POST   /centers                إضافة مركز جديد
PUT    /centers/{id}           تحديث بيانات مركز
DELETE /centers/{id}           حذف مركز
```

### Courses
```
GET    /courses                 قائمة الدورات
GET    /courses/{id}            تفاصيل دورة
POST   /courses                إضافة دورة
PUT    /courses/{id}           تحديث دورة
DELETE /courses/{id}           حذف دورة
GET    /courses/search?language=English&level=beginner
```

### Students
```
GET    /students                قائمة الطلاب
GET    /students/{id}           تفاصيل طالب
POST   /students               تسجيل طالب جديد
PUT    /students/{id}          تحديث بيانات طالب
DELETE /students/{id}          حذف طالب
```

### Enrollments
```
GET    /enrollments             قائمة التسجيلات
POST   /enrollments            تسجيل في دورة
PUT    /enrollments/{id}       تحديث حالة التسجيل
```

### Payments
```
GET    /payments                قائمة المدفوعات
POST   /payments               تسجيل دفعة جديدة
GET    /payments/student/{id}   مدفوعات طالب
```

### Exams
```
GET    /exams                   قائمة الاختبارات
POST   /exams                  إضافة اختبار
PUT    /exams/{id}/grade       إضافة درجة
GET    /exams/ielts            اختبارات IELTS
GET    /exams/toefl            اختبارات TOEFL
```

## أمثلة استجابات
```json
{
  "status": "success",
  "data": {
    "id": 1,
    "name_ar": "معهد النوريشن",
    "district": "مدينة إب",
    "courses_count": 12,
    "students_count": 340
  }
}
```

## رموز الخطأ
- 400: طلب غير صحيح
- 401: غير مصرح
- 404: غير موجود
- 409: تعارض بيانات
- 500: خطأ داخلي
