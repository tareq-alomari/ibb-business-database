# المرحلة الثالثة عشرة: Database Design - قطاع الكافتيريات في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 13_Database_Design.md

---

## 13.1 نظام إدارة قواعد البيانات

| العنصر | الاختيار |
|--------|---------|
| **قاعدة البيانات الرئيسية** | PostgreSQL 16 |
| **تخزين مؤقت (Cache)** | Redis 7 |
| **تخزين الصور** | Cloudflare R2 |
| **ORM** | Prisma (TypeScript) |

## 13.2 هيكل قاعدة البيانات

### الجداول الرئيسية

```
المستخدمون (users)
├── id (PK, UUID)
├── phone (UNIQUE)
├── name
├── role (enum: customer, owner, admin)
├── avatar_url
├── is_active
├── created_at
└── updated_at

العناوين (addresses)
├── id (PK)
├── user_id (FK → users)
├── label
├── latitude
├── longitude
├── full_address
└── area

المنشآت (establishments)
├── id (PK, UUID)
├── owner_id (FK → users)
├── name (AR)
├── slug (UNIQUE)
├── description
├── type (enum)
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
├── is_approved
├── is_featured
├── status (enum: pending, active, suspended)
├── created_at
└── updated_at

الخدمات (services)
├── id (PK)
├── establishment_id (FK → establishments)
├── name (AR)
├── description
├── price
├── discount_price
├── image_url
├── is_available
├── sort_order
├── created_at
└── updated_at

الحجوزات (bookings)
├── id (PK)
├── booking_number
├── user_id (FK → users)
├── establishment_id (FK → establishments)
├── service_id (FK → services)
├── booking_date
├── booking_time
├── status (enum: pending, confirmed, completed, cancelled)
├── payment_method (enum: cash, mobile_money)
├── payment_status (enum: pending, paid, failed)
├── total
├── special_instructions
├── created_at
└── updated_at

التقييمات (reviews)
├── id (PK)
├── user_id (FK → users)
├── establishment_id (FK → establishments)
├── booking_id (FK → bookings)
├── rating (1-5)
├── comment
├── images (JSONB)
├── is_verified
├── created_at
└── updated_at

العروض (offers)
├── id (PK)
├── establishment_id (FK → establishments)
├── title (AR)
├── description
├── discount_type (enum: percentage, fixed)
├── discount_value
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
└── created_at
```

## 13.3 العلاقات

| العلاقة | النوع | التوضيح |
|---------|-------|---------|
| مستخدم ← منشأة | 1:1 | مستخدم يدير منشأة |
| منشأة ← خدمة | 1:ن | منشأة لها خدمات متعددة |
| مستخدم ← حجز | 1:ن | مستخدم لديه حجوزات |
| منشأة ← تقييم | 1:ن | منشأة تستقبل تقييمات |
| منشأة ← عرض | 1:ن | منشأة تقدم عروضًا |

## 13.4 الفهارس

| الجدول | الحقول |
|--------|--------|
| establishments | name, type, area, average_rating |
| establishments | latitude, longitude (GIST) |
| services | name, price |
| bookings | user_id, establishment_id, status |
| users | phone (UNIQUE) |

---

## المصادر

- PostgreSQL Documentation
- Prisma ORM Schema Design
