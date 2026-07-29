# تصميم API: السوبرماركت في إب

## المعايير
- RESTful API
- JSON كصيغة للبيانات
- JWT للمصادقة
- HTTPS للتشفير

## نقاط النهاية (Endpoints)

### المصادقة
```
POST /api/auth/login
POST /api/auth/register
POST /api/auth/refresh-token
```

### المنتجات
```
GET    /api/products
GET    /api/products/{id}
POST   /api/products
PUT    /api/products/{id}
DELETE /api/products/{id}
GET    /api/products/search?q={keyword}
GET    /api/products/category/{category_id}
```

### الفئات
```
GET    /api/categories
POST   /api/categories
PUT    /api/categories/{id}
```

### العملاء
```
GET    /api/customers
GET    /api/customers/{id}
POST   /api/customers
PUT    /api/customers/{id}
GET    /api/customers/{id}/purchases
```

### المبيعات
```
GET    /api/sales
GET    /api/sales/{id}
POST   /api/sales
GET    /api/sales/daily-summary
GET    /api/sales/period?from={date}&to={date}
```

### الموردين
```
GET    /api/suppliers
POST   /api/suppliers
PUT    /api/suppliers/{id}
```

### التقارير
```
GET    /api/reports/daily-sales
GET    /api/reports/monthly-sales
GET    /api/reports/top-products?period={period}
GET    /api/reports/expiry-alerts
```

## مثال على استجابة API
```json
{
  "status": "success",
  "data": {
    "product": {
      "id": 1,
      "name": "أرز بسمتي",
      "price": 3500,
      "quantity": 50
    }
  },
  "message": "تم جلب البيانات بنجاح"
}
```
