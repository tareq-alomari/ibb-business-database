# تصميم قاعدة البيانات: البقالات في مدينة إب

## نظام إدارة قواعد البيانات
- PostgreSQL (لقوة العلائقية والأمان)
- أو SQLite (للإصدار المحلي البسيط)

## الجداول الرئيسية

### جدول المستخدمين (users)
- id, name, phone, email, password_hash, role, created_at
- الأدوار: مدير، صاحب بقالة، كاشير

### جدول المنتجات (products)
- id, name, barcode, category_id, unit_price, cost_price, quantity, expiry_date, image, created_at

### جدول التصنيفات (categories)
- id, name, description, parent_id

### جدول العملاء (customers)
- id, name, phone, address, loyalty_points, created_at

### جدول الموردين (suppliers)
- id, name, phone, address, balance, created_at

### جدول المبيعات (sales)
- id, customer_id, user_id, total_amount, payment_method, sale_date, notes

### جدول تفاصيل المبيعات (sale_items)
- id, sale_id, product_id, quantity, unit_price, total_price

### جدول المشتريات (purchases)
- id, supplier_id, user_id, total_amount, purchase_date, notes

### جدول حركة المخزون (inventory_transactions)
- id, product_id, type, quantity, reference_id, notes, created_at

## العلاقات
- المنتج ← تصنيف (علاقة واحد لمتعدد)
- المبيعات ← عميل (علاقة واحد لمتعدد)
- المبيعات ← مستخدم (علاقة واحد لمتعدد)
- تفاصيل المبيعات ← مبيعات ومنتجات

## الفهارس
- فهرس على الباركود لتسريع البحث
- فهرس على تاريخ المبيعات
- فهرس على رقم هاتف العميل

## سياسة النسخ الاحتياطي
- نسخ احتياطي يومي كامل
- احتفاظ بنسخ آخر 30 يوم
- تخزين النسخ في موقع منفصل
