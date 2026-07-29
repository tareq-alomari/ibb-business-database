# تصميم API: منصة البهارات في إب

## المبادئ العامة
- RESTful API
- استقبال وإرجاع JSON
- توثيق باستخدام OpenAPI/Swagger
- استخدام HTTP Methods القياسية

## النقاط الأساسية (Endpoints)

### المحلات (Shops)
- GET /api/shops - قائمة جميع المحلات
- GET /api/shops/{id} - تفاصيل محل
- POST /api/shops - إضافة محل جديد
- PUT /api/shops/{id} - تحديث بيانات محل
- DELETE /api/shops/{id} - حذف محل
- GET /api/shops/area/{area_id} - محلات حسب المنطقة

### المنتجات (Products)
- GET /api/products - قائمة المنتجات
- GET /api/products/{id} - تفاصيل منتج
- POST /api/products - إضافة منتج
- GET /api/products/category/{category_id} - منتجات حسب التصنيف
- GET /api/products/search?q={keyword} - بحث عن منتج

### الأسعار (Prices)
- GET /api/prices?product_id={id} - أسعار منتج في كل المحلات
- POST /api/prices - إضافة سعر جديد
- GET /api/prices/product/{product_id}/shop/{shop_id} - سعر منتج في محل معين

### المناطق (Areas)
- GET /api/areas - قائمة المناطق
- GET /api/areas/{id} - تفاصيل منطقة ومحلاتها

### التقييمات (Reviews)
- GET /api/reviews/shop/{shop_id} - تقييمات محل
- POST /api/reviews - إضافة تقييم جديد
- GET /api/reviews/{id} - تفاصيل تقييم

## أمثلة الاستجابة

### GET /api/shops
```json
{
  "data": [
    {
      "id": 1,
      "name": "بهارات اليمنية",
      "area": "الجند",
      "rating": 4.5,
      "delivery": true,
      "phone": "774455667"
    }
  ],
  "total": 65,
  "page": 1
}
```

### POST /api/shops
```json
{
  "name": "محل جديد",
  "area_id": 3,
  "phone": "771234567",
  "latitude": 13.9753,
  "longitude": 44.1762
}
```

## رموز الاستجابة
- 200: نجاح
- 201: تم الإنشاء
- 400: طلب خاطئ
- 404: غير موجود
- 500: خطأ في الخادم
