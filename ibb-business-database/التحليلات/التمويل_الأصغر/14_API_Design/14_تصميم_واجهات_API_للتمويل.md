# تصميم واجهات API للتمويل الأصغر في إب

## المبادئ العامة
- RESTful API مع تنسيق JSON
- توثيق كامل باستخدام OpenAPI/Swagger
- استخدام JWT للمصادقة والصلاحيات
- دعم اللغة العربية في الحقول والنصوص

## نقاط النهاية الرئيسية

### العملاء (Customers)
- GET /api/customers – قائمة العملاء
- GET /api/customers/{id} – تفاصيل عميل
- POST /api/customers – إضافة عميل جديد
- PUT /api/customers/{id} – تحديث بيانات عميل
- GET /api/customers/search?q= – بحث عن عميل

### القروض (Loans)
- GET /api/loans – قائمة القروض
- GET /api/loans/{id} – تفاصيل القرض
- POST /api/loans – تقديم طلب قرض
- PUT /api/loans/{id}/approve – الموافقة
- PUT /api/loans/{id}/disburse – الصرف
- GET /api/loans/{id}/installments – جدول الأقساط

### الأقساط (Installments)
- GET /api/installments – قائمة الأقساط
- POST /api/installments/pay – تسديد قسط
- GET /api/installments/overdue – الأقساط المتأخرة

### التقارير (Reports)
- GET /api/reports/portfolio – تقرير المحفظة
- GET /api/reports/performance – تقرير الأداء
- GET /api/reports/collection – تقرير التحصيل
- GET /api/reports/districts – توزيع حسب المديريات

### المصادقة (Authentication)
- POST /api/auth/login – تسجيل الدخول
- POST /api/auth/refresh – تجديد التوكن
- POST /api/auth/logout – تسجيل الخروج

## مثال استجابة API
```json
{
  "success": true,
  "data": {
    "customer_id": 1001,
    "full_name": "أحمد محمد",
    "loan_count": 2,
    "total_loans": 750000,
    "outstanding_balance": 320000
  },
  "message": "تم استرجاع البيانات بنجاح"
}
```

## معالجة الأخطاء
- 400: طلب غير صحيح
- 401: غير مصرح
- 404: غير موجود
- 409: تعارض البيانات
- 422: فشل التحقق من الصحة
- 500: خطأ داخلي في الخادم
