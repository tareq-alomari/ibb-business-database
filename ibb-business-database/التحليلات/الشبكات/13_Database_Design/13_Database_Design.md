# المرحلة الثالثة عشرة: Database Design - قطاع الشبكات في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 13_Database_Design.md

---

## 13.1 نموذج البيانات (Data Model)

### الجداول الرئيسية

```sql
-- جدول المستخدمين
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('customer', 'provider', 'admin'),
    location_area VARCHAR(100),
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- جدول الخدمات
CREATE TABLE services (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    provider_id UUID REFERENCES providers(id),
    name_ar VARCHAR(200) NOT NULL,
    category_id UUID REFERENCES categories(id),
    description TEXT,
    price_range_min DECIMAL(10,2),
    price_range_max DECIMAL(10,2),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- جدول الحجوزات
CREATE TABLE bookings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id UUID REFERENCES users(id),
    provider_id UUID REFERENCES providers(id),
    service_id UUID REFERENCES services(id),
    booking_date DATE NOT NULL,
    booking_time TIME NOT NULL,
    status ENUM('pending','confirmed','completed','cancelled'),
    total_price DECIMAL(10,2),
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- جدول التقييمات
CREATE TABLE reviews (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    booking_id UUID REFERENCES bookings(id),
    user_id UUID REFERENCES users(id),
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

## 13.2 علاقات البيانات (ERD)

```
users 1---* bookings : customer
providers 1---* services
providers 1---* bookings : provider
bookings 1---1 reviews
categories 1---* services
services 1---* bookings
```

## 13.3 استراتيجية الفهرسة (Indexing Strategy)

| الجدول | الحقول المفهرسة | الغرض |
|-------|----------------|------|
| users | phone, email, role | تسريع البحث والمصادقة |
| services | provider_id, category_id, name_ar | تسريع البحث والفلترة |
| bookings | customer_id, provider_id, status | استعلامات الحجوزات |
| reviews | booking_id, user_id | استعلامات التقييمات |

## 13.4 استراتيجية النسخ الاحتياطي (Backup Strategy)

| النوع | التكرار | طريقة الاستعادة |
|-------|--------|----------------|
| نسخة كاملة | يومياً | 30 دقيقة |
| نسخة تفاضلية | كل 6 ساعات | 15 دقيقة |
| سجل المعاملات | كل ساعة | 5 دقائق |

---

## المصادر

1. الجهاز المركزي للإحصاء اليمني - إحصائيات السكان 2024
2. غرفة تجارة وصناعة محافظة إب - تقارير القطاع التجاري
3. مسح ميداني تقديري لـقطاع الشبكات في محافظة إب
4. مقابلات محلية مع مقدمي الخدمة والمستفيدين في إب
