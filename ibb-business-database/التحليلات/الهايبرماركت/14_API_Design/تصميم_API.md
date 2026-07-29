# تصميم API - منصة الهايبرماركت

## المواصفات العامة
- النمط: RESTful API
- الصيغة: JSON
- البروتوكول: HTTPS
- التوثيق: JWT (JSON Web Tokens)

## المصادقة (Authentication)

### POST /api/auth/login
تسجيل الدخول وإرجاع JWT token
- Body: { email, password }
- Response: { token, user }

### POST /api/auth/register
تسجيل مستخدم جديد
- Body: { name, email, phone, password }

## المنتجات (Products)

### GET /api/products
قائمة المنتجات مع دعم التصفية والترتيب
- Query: { category_id, search, page, limit, sort_by, min_price, max_price }

### GET /api/products/:id
تفاصيل منتج معين

### POST /api/products (Admin)
إضافة منتج جديد

### PUT /api/products/:id (Admin)
تحديث بيانات منتج

### DELETE /api/products/:id (Admin)
حذف منتج

## الطلبات (Orders)

### GET /api/orders
قائمة طلبات المستخدم

### POST /api/orders
إنشاء طلب جديد
- Body: { items: [{ product_id, quantity }], branch_id, payment_method, delivery_address }

### GET /api/orders/:id
تفاصيل طلب معين

### PUT /api/orders/:id/status (Admin)
تحديث حالة الطلب

## الفروع (Branches)

### GET /api/branches
قائمة الفروع مع الموقع

### GET /api/branches/:id
تفاصيل فرع معين

## العملاء (Customers) - Admin

### GET /api/customers
قائمة العملاء

### GET /api/customers/:id
تفاصيل عميل معين

## التقارير (Reports) - Admin

### GET /api/reports/sales
تقارير المبيعات حسب الفترة
- Query: { from, to, branch_id }

### GET /api/reports/inventory
تقرير المخزون الحالي
