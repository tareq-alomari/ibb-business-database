# تصميم قاعدة البيانات - منصة الحقائب في إب

## نظام إدارة قواعد البيانات
- PostgreSQL (قاعدة بيانات رئيسية)
- Redis (تخزين مؤقت وجلسات)

## الجداول الرئيسية

### جدول المستخدمين (users)
- id (PK, UUID), name, email, phone, password_hash
- role (admin, seller, buyer)
- created_at, updated_at, verified, active

### جدول البائعين (sellers)
- id (PK, UUID), user_id (FK)
- store_name, store_description, logo, cover_image
- rating, total_sales, verified (boolean), commission_rate

### جدول المنتجات (products)
- id (PK, UUID), seller_id (FK), category_id (FK)
- name, description (AR, EN)
- price, discount_price, stock_quantity
- material, color, size, weight, dimensions
- images (JSON array), featured (boolean)
- status (active, inactive, archived)

### جدول التصنيفات (categories)
- id (PK, UUID), name (AR, EN)
- parent_id (FK, self), image, sort_order, active

### جدول الطلبات (orders)
- id (PK, UUID), buyer_id (FK), seller_id (FK)
- status (pending, confirmed, shipped, delivered, cancelled)
- total_amount, commission, shipping_address
- payment_method, notes, created_at, updated_at

### جدول عناصر الطلب (order_items)
- id (PK, UUID), order_id (FK), product_id (FK)
- quantity, unit_price, total_price

### جدول التقييمات (reviews)
- id (PK, UUID), product_id (FK), user_id (FK)
- rating (1-5), comment, images, created_at

### جدول الإشعارات (notifications)
- id (PK, UUID), user_id (FK)
- title, body, type (order, promo, system)
- read (boolean), created_at

### جداول إضافية
- favorites: user_id (FK), product_id (FK)
- cart_items: user_id (FK), product_id (FK), quantity
- payment_transactions: order_id (FK), amount, status, method

## العلاقات
- user → seller (1—*), user → order (* as buyer)
- seller → product (1—*), seller → order (* as seller)
- category → product (1—*), category → subcategory (self)
- order → order_items (1—*), product → reviews (1—*)
