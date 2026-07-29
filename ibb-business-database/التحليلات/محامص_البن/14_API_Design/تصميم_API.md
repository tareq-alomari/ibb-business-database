# تصميم API: نظام محامص البن

RESTful API مع JSON.

## النقاط الرئيسية (Endpoints)

**المحامص:** GET/POST /api/roasteries, GET/PUT/DELETE /api/roasteries/:id

**المنتجات:** GET /api/roasteries/:id/products, POST /api/products, PUT/DELETE /api/products/:id

**الطلبات:** GET /api/orders, POST /api/orders, PUT /api/orders/:id/status

**المستخدمون:** POST /api/auth/register, POST /api/auth/login, GET/PUT /api/profile

**التقييمات:** GET /api/roasteries/:id/reviews, POST /api/reviews

## معايير الأمان
- JWT للمصادقة (Bearer Token).
- Rate Limiting: 100 طلب/دقيقة.
- HTTPS إلزامي.

## استجابة موحدة
```json
{"success": true, "data": {}, "message": "", "errors": []}
```
