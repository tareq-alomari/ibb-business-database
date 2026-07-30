# المرحلة الثالثة عشرة: Database Design - قطاع الحدادة والأعمال المعدنية في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 13_Database_Design.md

---

## 13.1 نظام إدارة قواعد البيانات (DBMS)

| العنصر | الاختيار |
|--------|---------|
| **قاعدة البيانات الرئيسية** | PostgreSQL 16 |
| **تخزين مؤقت (Cache)** | Redis 7 |
| **تخزين الصور والملفات** | Cloudflare R2 / AWS S3 |
| **ORM** | Prisma (TypeScript) / Django ORM (Python) |

## 13.2 هيكل قاعدة البيانات (Entity Relationship)

### الجداول الرئيسية

```
المستخدمون (users)
├── id (PK, UUID)
├── phone (UNIQUE)
├── name
├── role (enum: customer, provider, admin)
├── avatar_url
├── is_active
├── created_at
├── updated_at
└── last_login

مقدمو الخدمة (service_providers)
├── id (PK, UUID)
├── owner_id (FK → users)
├── name (AR)
├── slug (UNIQUE)
├── description
├── phone
├── whatsapp
├── latitude
├── longitude
├── address
├── area
├── cover_image
├── logo
├── average_rating
├── total_reviews
├── is_approved
├── is_featured
├── status (enum: pending, active, suspended)
├── created_at
└── updated_at

الخدمات (services)
├── id (PK)
├── provider_id (FK → service_providers)
├── name
├── description
├── price
├── discount_price (nullable)
├── duration (minutes)
├── is_available
├── is_featured
├── sort_order
├── created_at
└── updated_at

معرض الأعمال (galleries)
├── id (PK)
├── provider_id (FK → service_providers)
├── image_url
├── caption
├── sort_order
├── created_at
└── updated_at

الحجوزات (bookings)
├── id (PK)
├── booking_number (sequential)
├── user_id (FK → users)
├── provider_id (FK → service_providers)
├── service_id (FK → services)
├── booking_date
├── booking_time
├── status (enum: pending, confirmed, in_progress, completed, cancelled)
├── subtotal
├── discount
├── total
├── payment_method (enum: cash, mobile_money)
├── payment_status (enum: pending, paid, failed)
├── notes
├── created_at
└── updated_at

التقييمات (reviews)
├── id (PK)
├── user_id (FK → users)
├── provider_id (FK → service_providers)
├── booking_id (FK → bookings)
├── rating (1-5)
├── comment
├── images (JSONB)
├── is_verified
├── created_at
└── updated_at

العروض (offers)
├── id (PK)
├── provider_id (FK → service_providers)
├── title
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

الإشعارات (notifications)
├── id (PK)
├── user_id (FK → users)
├── title
├── body
├── data (JSONB)
├── is_read
├── created_at
└── updated_at
```

## 13.3 العلاقات (Relationships)

| العلاقة | النوع | التوضيح |
|---------|-------|---------|
| مستخدم → مقدم خدمة | 1:1 | مستخدم واحد يدير حسابًا واحدًا |
| مقدم خدمة → خدمة | 1:ن | مقدم خدمة يقدم خدمات متعددة |
| مقدم خدمة → معرض | 1:ن | مقدم خدمة له صور متعددة في المعرض |
| مستخدم → حجز | 1:ن | مستخدم يقوم بحجوزات متعددة |
| مقدم خدمة → حجز | 1:ن | مقدم خدمة يستقبل حجوزات متعددة |
| حجز → تقييم | 1:1 | كل حجز له تقييم واحد (اختياري) |
| مقدم خدمة → تقييم | 1:ن | مقدم خدمة يستقبل تقييمات متعددة |
| مقدم خدمة → عرض | 1:ن | مقدم خدمة يقدم عروضًا متعددة |

## 13.4 الفهارس (Indexes)

| الجدول | الحقول | النوع |
|--------|--------|-------|
| service_providers | name, area, average_rating, is_approved | BTREE |
| service_providers | latitude, longitude | GIST (spatial) |
| services | name, price, provider_id, is_available | BTREE |
| bookings | user_id, provider_id, status, booking_date | BTREE |
| reviews | provider_id, rating, created_at | BTREE |
| users | phone | UNIQUE BTREE |

## 13.5 استراتيجية النسخ الاحتياطي (Backup Strategy)

| النوع | التكرار | طريقة الاستعادة |
|-------|---------|----------------|
| Full backup | يومي (2 صباحًا) | استعادة كاملة خلال 30 دقيقة |
| WAL archiving | مستمر | Point-in-time recovery |
| تخزين | 30 يومًا | S3 / R2 مع lifecycle |

---

## المصادر

- PostgreSQL Documentation (postgresql.org/docs)
- Prisma ORM Schema Design (prisma.io)
- أفضل ممارسات تصميم قواعد البيانات
