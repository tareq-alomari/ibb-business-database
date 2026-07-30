# المرحلة الثالثة عشرة: Database Design - قطاع الصناعات الغذائية في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 13_Database_Design.md

---

## 13.1 نموذج البيانات

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) CHECK (role IN ('customer','provider','admin')),
    location_area VARCHAR(100),
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

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

CREATE TABLE bookings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id UUID REFERENCES users(id),
    provider_id UUID REFERENCES providers(id),
    service_id UUID REFERENCES services(id),
    booking_date DATE NOT NULL,
    booking_time TIME NOT NULL,
    status VARCHAR(20) CHECK (status IN ('pending','confirmed','completed','cancelled')),
    total_price DECIMAL(10,2),
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE reviews (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    booking_id UUID REFERENCES bookings(id),
    user_id UUID REFERENCES users(id),
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

## 13.2 علاقات البيانات

users 1---* bookings
providers 1---* services
bookings 1---1 reviews
categories 1---* services

## 13.3 الفهارس

| الجدول | الحقول |
|-------|--------|
| users | phone, email, role |
| services | provider_id, category_id |
| bookings | customer_id, provider_id, status |
| reviews | booking_id, user_id |

## 13.4 النسخ الاحتياطي

| النوع | التكرار |
|-------|--------|
| نسخة كاملة | يومياً |
| نسخة تفاضلية | كل 6 ساعات |
| سجل المعاملات | كل ساعة |

---

## المصادر

1. الجهاز المركزي للإحصاء اليمني
2. غرفة تجارة وصناعة محافظة إب
3. مسح ميداني تقديري لـقطاع الصناعات الغذائية في محافظة إب
4. مقابلات محلية مع مقدمي الخدمة والمستفيدين
