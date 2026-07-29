# المرحلة الثالثة عشرة: Database Design - قطاع مراكز التدريب في محافظة إب

## 13.1 هيكل قاعدة البيانات

### الجداول الرئيسية

| الجدول | الوصف | العلاقات |
|--------|-------|----------|
| `users` | جميع المستخدمين (متدرب، مركز، إداري، مدرب) | - |
| `training_centers` | مراكز التدريب | users.id |
| `trainers` | المدربون | users.id, centers.id |
| `programs` | البرامج التدريبية | centers.id, trainers.id |
| `categories` | تصنيفات البرامج | - |
| `enrollments` | تسجيلات المتدربين | users.id, programs.id |
| `reviews` | تقييمات ومراجعات | users.id, centers.id, programs.id |
| `certificates` | الشهادات الصادرة | enrollments.id |
| `payments` | المدفوعات | enrollments.id |

## 13.2 مخطط الجداول الأساسي

```sql
-- جدول المستخدمين
users (id, name, email, phone, password_hash, role, avatar,
       created_at, updated_at, is_active)

-- جدول مراكز التدريب
training_centers (id, user_id, name_ar, name_en, description,
                  address, district, phone, website, logo,
                  license_number, is_verified, lat, lng)

-- جدول البرامج التدريبية
programs (id, center_id, trainer_id, category_id, title_ar,
          title_en, description, price, duration_hours,
          start_date, end_date, max_students, is_online,
          language, certificate_type, status)

-- جدول التسجيلات
enrollments (id, user_id, program_id, status, payment_status,
             enrolled_at, completed_at, grade)
```

## 13.3 أنواع البيانات والتقييدات

| الحقل | النوع | التقييد |
|-------|-------|---------|
| البريد الإلكتروني | VARCHAR(255) | UNIQUE, NOT NULL |
| رقم الهاتف | VARCHAR(15) | UNIQUE |
| السعر | DECIMAL(10,2) | >= 0 |
| التقييم | DECIMAL(2,1) | 0.0 - 5.0 |
| الحالة | ENUM | active, pending, inactive, rejected |

## 13.4 ER Diagram (نصي)

```
users 1──M enrollments M──1 programs M──1 training_centers
  │                                          │
  │                                          │
  └── 1──M reviews M──1 programs             └── 1──M trainers
       └── M──1 training_centers
```

- PostgreSQL لقوة العلاقات والأمان
- MongoDB اختياري للمحتوى الديناميكي (تقييمات، مراجعات)
- Redis لل caching وتسريع البحث
