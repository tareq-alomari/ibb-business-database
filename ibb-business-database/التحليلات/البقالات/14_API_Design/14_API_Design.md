# تصميم واجهات API: البقالات في مدينة إب

## نمط API
- RESTful API
- تنسيق JSON للبيانات
- توثيق عبر Swagger/OpenAPI

## المصادقة
- JWT (JSON Web Tokens)
- صلاحية التوكن: 24 ساعة
- تحديث التوكن عبر Refresh Token

## نقاط النهاية الرئيسية

### المصادقة
- POST /api/auth/login
- POST /api/auth/register
- POST /api/auth/refresh-token

### المنتجات
- GET /api/products (قائمة المنتجات مع تصفية)
- GET /api/products/:id (تفاصيل منتج)
- POST /api/products (إضافة منتج)
- PUT /api/products/:id (تحديث منتج)
- DELETE /api/products/:id (حذف منتج)
- GET /api/products/search?q= (بحث)

### التصنيفات
- GET /api/categories
- POST /api/categories
- PUT /api/categories/:id

### العملاء
- GET /api/customers
- POST /api/customers
- GET /api/customers/:id

### المبيعات
- GET /api/sales
- POST /api/sales (تسجيل بيع)
- GET /api/sales/:id

### التقارير
- GET /api/reports/sales?period=daily
- GET /api/reports/inventory
- GET /api/reports/profits

## هيكل الاستجابة
```json
{
  "success": true,
  "data": {},
  "message": "تمت العملية بنجاح"
}
```

## أكواد الحالة
- 200: نجاح
- 201: تم الإنشاء
- 400: طلب خاطئ
- 401: غير مصرح
- 404: غير موجود
- 500: خطأ في الخادم

## حدود الطلبات
- 100 طلب في الدقيقة للمستخدم العادي
- 500 طلب في الدقيقة للمستخدم المميز
