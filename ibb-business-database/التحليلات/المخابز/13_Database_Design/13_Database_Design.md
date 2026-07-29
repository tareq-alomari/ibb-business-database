# المرحلة الثالثة عشرة: تصميم قاعدة البيانات - قطاع المخابز في محافظة إب

> **تاريخ التقرير**: يوليو 2026

---

## نموذج البيانات

### جدول المخابز

| الحقل | النوع | الوصف |
|-------|------|-------|
| id | UUID | معرف فريد |
| name | VARCHAR | اسم المخبز |
| owner_name | VARCHAR | اسم المالك |
| directorate | VARCHAR | المديرية |
| district | VARCHAR | الحي |
| latitude | DECIMAL | خط العرض |
| longitude | DECIMAL | خط الطول |
| phone | VARCHAR | رقم الهاتف |
| type | ENUM | نوع المخبز |
| license_status | BOOLEAN | حالة الترخيص |
| operating_hours | JSON | أوقات العمل |
| rating_avg | DECIMAL | متوسط التقييم |
| created_at | TIMESTAMP | تاريخ الإضافة |

### جدول المنتجات

| الحقل | النوع |
|-------|------|
| id | UUID |
| bakery_id | UUID (FK) |
| name | VARCHAR |
| price | DECIMAL |
| unit | VARCHAR |
| category | ENUM |

### جدول التقييمات

| الحقل | النوع |
|-------|------|
| id | UUID |
| bakery_id | UUID (FK) |
| user_id | UUID (FK) |
| rating | INTEGER |
| comment | TEXT |
| created_at | TIMESTAMP |

### جدول المستخدمين

| الحقل | النوع |
|-------|------|
| id | UUID |
| name | VARCHAR |
| email | VARCHAR |
| password_hash | VARCHAR |
| role | ENUM |
| created_at | TIMESTAMP |

## العلاقات

- المخبز ← منتجات (واحد إلى متعدد)
- المخبز ← تقييمات (واحد إلى متعدد)
- المستخدم ← تقييمات (واحد إلى متعدد)
- المستخدم ← مفضلات (واحد إلى متعدد)

## الفهارس

- اسم المخبز (بحث نصي)
- المديرية (تصفية)
- الإحداثيات (بحث جغرافي)
- التقييم (ترتيب)