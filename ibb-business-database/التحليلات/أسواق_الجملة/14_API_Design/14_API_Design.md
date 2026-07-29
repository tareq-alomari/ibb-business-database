# المرحلة الرابعة عشرة: API Design - قطاع أسواق الجملة في محافظة إب

## 14.1 النقاط الرئيسية

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| GET | `/products` | قائمة المنتجات (مع تصفية حسب الفئة، السعر) |
| GET | `/products/{id}` | تفاصيل منتج |
| GET | `/products/search?q=أرز` | بحث عن منتج |
| GET | `/traders` | قائمة تجار الجملة |
| GET | `/traders/{id}` | تفاصيل تاجر مع منتجاته |
| GET | `/traders/{id}/products` | منتجات تاجر معين |
| POST | `/orders` | إنشاء طلب جديد |
| GET | `/orders/{id}` | تفاصيل طلب |
| PUT | `/orders/{id}/status` | تحديث حالة الطلب |
| GET | `/categories` | تصنيفات المنتجات |
| GET | `/prices/daily` | قائمة أسعار اليوم |
| POST | `/auth/register` | تسجيل مستخدم جديد |
| POST | `/auth/login` | تسجيل الدخول (OTP) |
| GET | `/delivery/{orderId}` | تتبع التوصيل |

## 14.2 مثال طلب

```
GET /api/v1/products?category=حبوب&sort=price_asc
{
  "products": [
    {
      "id": 1,
      "name": "أرز بسمتي هندي",
      "category": "حبوب",
      "price": 1400,
      "unit": "كجم",
      "quantity_available": 500,
      "trader": {
        "id": 5,
        "name": "مؤسسة الغيث للتجارة"
      },
      "image_url": "https://..."
    }
  ],
  "total": 15,
  "page": 1
}
```

## 14.3 مثال إرسال طلب

```
POST /api/v1/orders
{
  "trader_id": 5,
  "items": [
    { "product_id": 1, "quantity": 10 },
    { "product_id": 3, "quantity": 5 }
  ],
  "delivery_address": "مدينة إب - جولة القاع",
  "payment_method": "cash"
}
```
