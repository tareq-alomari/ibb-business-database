# تصميم قاعدة البيانات: منصة رياض الأطفال في إب

> **تاريخ التصميم**: يوليو 2026

---

## الكيانات والسمات

### 1. Kindergarten (روضة)

| العمود | النوع | الوصف |
|--------|------|-------|
| id | UUID | معرف فريد |
| name_ar | VARCHAR(255) | اسم الروضة |
| type | ENUM | خاصة، حكومية، أهلية |
| curriculum | VARCHAR(100) | المنهج الدراسي |
| rating | DECIMAL(2,1) | متوسط التقييم |
| phone | VARCHAR(50) | رقم الهاتف |
| address | TEXT | العنوان |
| district_id | UUID FK | معرف المديرية |
| latitude | DECIMAL(10,8) | خط العرض |
| longitude | DECIMAL(11,8) | خط الطول |
| fee_min | INT | أقل رسم |
| fee_max | INT | أعلى رسم |
| working_hours | JSON | أوقات العمل |
| images | JSON[] | صور الروضة |
| is_verified | BOOLEAN | تم التحقق |
| status | ENUM | active, inactive |

### 2–6. الكيانات الأخرى

| الكيان | السمات الأساسية |
|--------|----------------|
| Level (مستوى) | id, kindergarten_id, name (KG1/KG2/KG3), capacity, fee |
| Activity (نشاط) | id, kindergarten_id, name_ar, is_free |
| User (مستخدم) | id, name, phone (UNIQUE), role, created_at |
| Review (تقييم) | id, kindergarten_id, user_id, rating (1-5), comment, is_approved |
| District (مديرية) | id, name_ar, population |

## العلاقات (ERD)

```
District (1) ──── (N) Kindergarten
Kindergarten (1) ──── (N) Level
Kindergarten (1) ──── (N) Activity
Kindergarten (1) ──── (N) Review
User (1) ──── (N) Review
```

## الفهارس (Indexes)

| الجدول | الفهرس | النوع |
|--------|--------|-------|
| kindergarten | district_id | BTREE |
| kindergarten | curriculum | BTREE |
| kindergarten | fee_min, fee_max | BTREE |
| kindergarten | latitude, longitude | SPATIAL |
| review | kindergarten_id | BTREE |
| user | phone | UNIQUE |

