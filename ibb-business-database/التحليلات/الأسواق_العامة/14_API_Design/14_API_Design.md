# تصميم واجهات API: الأسواق العامة في محافظة إب

## نقاط النهاية (Endpoints)

### الأسواق
- `GET /api/markets` - قائمة جميع الأسواق
- `GET /api/markets/{id}` - تفاصيل سوق محدد
- `GET /api/markets/{id}/traders` - تجار سوق محدد
- `GET /api/markets/nearby?lat&lng&radius` - أقرب الأسواق لموقع معين

### التجار
- `GET /api/traders` - قائمة التجار مع إمكانية الفلترة
- `GET /api/traders/{id}` - تفاصيل تاجر محدد
- `GET /api/traders/{id}/products` - سلع تاجر محدد
- `GET /api/traders/{id}/ratings` - تقييمات تاجر محدد
- `POST /api/traders` - إضافة تاجر جديد
- `PUT /api/traders/{id}` - تحديث بيانات تاجر

### السلع
- `GET /api/products` - قائمة السلع مع الفلترة والفئات
- `GET /api/products/{id}` - تفاصيل سلعة محددة
- `POST /api/products` - إضافة سلعة جديدة
- `PUT /api/products/{id}` - تحديث سعر أو بيانات سلعة

### الفئات
- `GET /api/categories` - قائمة فئات السلع
- `GET /api/categories/{id}` - تفاصيل فئة فرعية

### التقييمات
- `GET /api/ratings?trader_id={id}` - تقييمات تاجر
- `POST /api/ratings` - إضافة تقييم لتاجر

## تنسيق الاستجابة
```json
{
  "status": "success",
  "data": { ... },
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 150
  }
}
```

## متطلبات الأمان
- توثيق عبر JWT للتجار والإدارة
- معدل طلبات محدود (rate limiting)
- التحقق من صحة البيانات المدخلة
- تسجيل جميع عمليات التعديل والحذف
- دعم CORS للتطبيقات الأمامية
