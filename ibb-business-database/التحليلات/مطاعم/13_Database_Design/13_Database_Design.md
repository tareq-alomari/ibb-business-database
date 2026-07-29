# المرحلة الثالثة عشرة: Database Design - قطاع المطاعم في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 13_Database_Design.md

---

## 13.1 نظام إدارة قواعد البيانات (DBMS)

| العنصر | الاختيار |
|--------|---------|
| **قاعدة البيانات الرئيسية** | PostgreSQL 16 |
| **تخزين مؤقت (Cache)** | Redis 7 |
| **بحث نصي** | PostgreSQL Full-Text Search + Elasticsearch (اختياري) |
| **تخزين الصور** | Cloudflare R2 / AWS S3 |
| **ORM** | Prisma (TypeScript) / Django ORM (Python) |

## 13.2 هيكل قاعدة البيانات (Entity Relationship)

### الجداول الرئيسية

```
المستخدمون (users)
├── id (PK, UUID)
├── phone (UNIQUE)
├── name
├── email (nullable)
├── password_hash (nullable)
├── role (enum: customer, restaurant, driver, admin)
├── avatar_url
├── is_active
├── created_at
├── updated_at
└── last_login

العناوين (addresses)
├── id (PK)
├── user_id (FK → users)
├── label (منزل، عمل، الخ)
├── latitude
├── longitude
├── full_address
├── area
├── is_default
├── created_at
└── updated_at

المطاعم (restaurants)
├── id (PK, UUID)
├── owner_id (FK → users)
├── name (AR/EN)
├── slug (UNIQUE)
├── description
├── type (enum: popular, fast_food, grill, fish, family, hotel, international)
├── price_level (enum: low, medium, high, luxury)
├── phone
├── whatsapp
├── latitude
├── longitude
├── full_address
├── area
├── cover_image
├── logo
├── opening_time
├── closing_time
├── is_open
├── average_rating
├── total_reviews
├── delivery_available
├── delivery_fee
├── min_order
├── delivery_areas (JSONB)
├── is_approved (boolean)
├── is_featured
├── status (enum: pending, active, suspended)
├── created_at
└── updated_at

تصنيفات المنيو (menu_categories)
├── id (PK)
├── restaurant_id (FK → restaurants)
├── name (AR)
├── sort_order
├── is_active
├── created_at
└── updated_at

الأصناف (menu_items)
├── id (PK)
├── category_id (FK → menu_categories)
├── name (AR)
├── description
├── price
├── discount_price (nullable)
├── image_url
├── is_available
├── is_featured
├── preparation_time (minutes)
├── sort_order
├── created_at
└── updated_at

السلة (carts)
├── id (PK)
├── user_id (FK → users)
├── restaurant_id (FK → restaurants)
├── status (enum: active, checked_out, abandoned)
├── created_at
└── updated_at

عناصر السلة (cart_items)
├── id (PK)
├── cart_id (FK → carts)
├── menu_item_id (FK → menu_items)
├── quantity
├── unit_price
├── special_instructions
├── created_at
└── updated_at

الطلبات (orders)
├── id (PK)
├── order_number (sequential, per restaurant)
├── user_id (FK → users)
├── restaurant_id (FK → restaurants)
├── driver_id (FK → users, nullable)
├── address_id (FK → addresses)
├── subtotal
├── delivery_fee
├── discount
├── total
├── payment_method (enum: cash, mobile_money)
├── payment_status (enum: pending, paid, failed)
├── status (enum: pending, confirmed, preparing, ready, picked_up, delivered, cancelled)
├── driver_status (enum: not_assigned, assigned, picked_up, delivered, nullable)
├── special_instructions
├── estimated_delivery_time
├── actual_delivery_time
├── created_at
└── updated_at

التقييمات (reviews)
├── id (PK)
├── user_id (FK → users)
├── restaurant_id (FK → restaurants)
├── order_id (FK → orders, nullable)
├── rating (1-5)
├── comment
├── images (JSONB)
├── is_verified
├── created_at
└── updated_at

العروض (offers)
├── id (PK)
├── restaurant_id (FK → restaurants)
├── title (AR)
├── description
├── discount_type (enum: percentage, fixed)
├── discount_value
├── min_order (nullable)
├── start_date
├── end_date
├── is_active
├── image_url
├── created_at
└── updated_at

السائقون (drivers)
├── id (PK, FK → users)
├── vehicle_type (motorcycle, car)
├── vehicle_plate
├── license_number
├── is_available
├── current_latitude
├── current_longitude
├── total_deliveries
├── rating
├── is_verified
├── created_at
└── updated_at

التوصيلات (deliveries)
├── id (PK)
├── order_id (FK → orders)
├── driver_id (FK → drivers)
├── status (enum: assigned, picked_up, in_transit, delivered, failed)
├── pickup_time
├── delivery_time
├── driver_rating (nullable)
├── delivery_notes
├── created_at
└── updated_at

الإعلانات (ads)
├── id (PK)
├── restaurant_id (FK → restaurants)
├── title
├── image_url
├── target_url
├── start_date
├── end_date
├── budget
├── impressions
├── clicks
├── is_active
├── created_at
└── updated_at

الإشعارات (notifications)
├── id (PK)
├── user_id (FK → users)
├── title
├── body
├── data (JSONB)
├── is_read
├── created_at
└── updated_at

الأحداث (audit_logs)
├── id (PK)
├── user_id (FK → users, nullable)
├── action
├── entity_type
├── entity_id
├── old_values (JSONB, nullable)
├── new_values (JSONB, nullable)
├── ip_address
├── created_at
└── updated_at
```

## 13.3 العلاقات (Relationships)

| العلاقة | النوع | التوضيح |
|---------|-------|---------|
| مستخدم ← مطعم | 1:1 | مستخدم واحد يدير مطعمًا واحدًا |
| مستخدم ← عنوان | 1:ن | مستخدم可以有 عناوين متعددة |
| مطعم ← تصنيف منيو | 1:ن | مطعم له تصنيفات متعددة |
| تصنيف ← صنف | 1:ن | تصنيف واحد يضم أصنافًا متعددة |
| مطعم ← طلب | 1:ن | مطعم يستقبل طلبات متعددة |
| مستخدم ← طلب | 1:ن | مستخدم يقدم طلبات متعددة |
| طلب ← توصيل | 1:1 | كل طلب له توصيلة واحدة |
| مطعم ← تقييم | 1:ن | مطعم يستقبل تقييمات متعددة |
| مطعم ← عرض | 1:ن | مطعم يقدم عروضًا متعددة |

## 13.4 الفهارس (Indexes)

| الجدول | الحقول | النوع |
|--------|--------|-------|
| restaurants | name, type, area, average_rating, is_open | BTREE |
| restaurants | latitude, longitude | GIST (spatial) |
| menu_items | name, category_id, price | BTREE |
| orders | user_id, restaurant_id, status, created_at | BTREE |
| orders | order_number, restaurant_id | UNIQUE |
| reviews | restaurant_id, rating, created_at | BTREE |
| users | phone | UNIQUE BTREE |

## 13.5 استراتيجية النسخ الاحتياطي (Backup Strategy)

| النوع | التكرار | طريقة الاستعادة |
|-------|---------|----------------|
| Full backup | يومي (2 صباحًا) | استعادة كاملة خلال 30 دقيقة |
| WAL archiving | مستمر | Point-in-time recovery |
| قاعدة بيانات احتياطية | متزامنة | Read replica للقراءة فقط |
| تخزين | 30 يومًا | S3 / R2 مع lifecycle |

---

## المصادر

- PostgreSQL Documentation (postgresql.org/docs)
- Prisma ORM Schema Design (prisma.io)
- Uber Eats Database Architecture (engineering.uber.com)
- Talabat Tech Blog