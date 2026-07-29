# المرحلة الثالثة عشرة: Database Design - قطاع المستشفيات في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 13_Database_Design.md

---

## 13.1 Database Schema

### Entity: Hospital

| العمود | النوع | القيود | الوصف |
|--------|------|--------|-------|
| id | UUID | PK | معرف فريد |
| name_ar | VARCHAR(255) | NOT NULL | الاسم بالعربية |
| name_en | VARCHAR(255) | NULL | الاسم بالإنجليزية |
| type | ENUM('government','private','university','community','field') | NOT NULL | نوع المستشفى |
| category_rank | ENUM('A','B1','B2','C1','C2','D', NULL) | NULL | تصنيف الوزارة |
| district_id | UUID | FK -> District.id | معرف المديرية |
| address | TEXT | NOT NULL | العنوان |
| phone | VARCHAR(50) | NULL | رقم الهاتف |
| phone_emergency | VARCHAR(50) | NULL | رقم الطوارئ |
| email | VARCHAR(255) | NULL | البريد الإلكتروني |
| website | VARCHAR(255) | NULL | الموقع الإلكتروني |
| latitude | DECIMAL(10,8) | NOT NULL | خط العرض |
| longitude | DECIMAL(11,8) | NOT NULL | خط الطول |
| bed_count | INT | NULL | عدد الأسرة |
| has_emergency_24h | BOOLEAN | DEFAULT false | طوارئ 24 ساعة |
| has_icu | BOOLEAN | DEFAULT false | عناية مركزة |
| has_incubators | BOOLEAN | DEFAULT false | حاضنات أطفال |
| has_dialysis | BOOLEAN | DEFAULT false | غسيل كلوي |
| has_lab | BOOLEAN | DEFAULT true | مختبر |
| has_radiology | BOOLEAN | DEFAULT true | أشعة |
| has_pharmacy | BOOLEAN | DEFAULT true | صيدلية |
| description | TEXT | NULL | وصف المستشفى |
| established_year | INT | NULL | سنة التأسيس |
| director_name | VARCHAR(255) | NULL | اسم المدير |
| is_verified | BOOLEAN | DEFAULT false | تم التحقق |
| status | ENUM('active','inactive','suspended') | DEFAULT 'active' | الحالة |
| avg_rating | DECIMAL(2,1) | DEFAULT 0.0 | متوسط التقييم |
| review_count | INT | DEFAULT 0 | عدد التقييمات |
| created_at | TIMESTAMP | DEFAULT NOW() | تاريخ الإضافة |
| updated_at | TIMESTAMP | AUTO_UPDATE | آخر تحديث |
| created_by | UUID | FK -> User.id | أضيف بواسطة |

### Entity: Doctor (طبيب)

| العمود | النوع | القيود |
|--------|------|--------|
| id | UUID | PK |
| hospital_id | UUID | FK -> Hospital.id |
| name_ar | VARCHAR(255) | NOT NULL |
| name_en | VARCHAR(255) | NULL |
| specialization | VARCHAR(255) | NOT NULL |
| sub_specialization | VARCHAR(255) | NULL |
| qualifications | TEXT | NULL |
| phone | VARCHAR(50) | NULL |
| email | VARCHAR(255) | NULL |
| photo_url | VARCHAR(500) | NULL |
| is_available | BOOLEAN | DEFAULT true |
| is_head | BOOLEAN | DEFAULT false |

### Entity: HospitalSpecialty (تخصصات المستشفى)

| العمود | النوع |
|--------|------|
| hospital_id | UUID | FK -> Hospital.id |
| specialty_id | UUID | FK -> Specialty.id |
| PRIMARY KEY | (hospital_id, specialty_id) |

### Entity: Specialty (تخصص)

| العمود | النوع |
|--------|------|
| id | UUID | PK |
| name_ar | VARCHAR(100) | NOT NULL UNIQUE |
| name_en | VARCHAR(100) | NULL |
| icon | VARCHAR(50) | NULL |

### Entity: District (مديرية)

| العمود | النوع |
|--------|------|
| id | UUID | PK |
| name_ar | VARCHAR(100) | NOT NULL |
| name_en | VARCHAR(100) | NULL |
| population | INT | NULL |
| latitude | DECIMAL(10,8) | NULL |
| longitude | DECIMAL(11,8) | NULL |

### Entity: Review (تقييم)

| العمود | النوع |
|--------|------|
| id | UUID | PK |
| hospital_id | UUID | FK -> Hospital.id |
| user_id | UUID | FK -> User.id |
| rating | TINYINT | CHECK 1-5 |
| comment | TEXT | NULL |
| is_approved | BOOLEAN | DEFAULT false |
| created_at | TIMESTAMP | DEFAULT NOW() |

### Entity: User (مستخدم)

| العمود | النوع |
|--------|------|
| id | UUID | PK |
| name | VARCHAR(255) | NOT NULL |
| email | VARCHAR(255) | UNIQUE |
| phone | VARCHAR(50) | UNIQUE |
| password_hash | VARCHAR(255) | NOT NULL |
| role | ENUM('super_admin','admin','manager','doctor','user') | DEFAULT 'user' |
| is_active | BOOLEAN | DEFAULT true |
| created_at | TIMESTAMP | DEFAULT NOW() |

### Entity: Appointment (موعد)

| العمود | النوع |
|--------|------|
| id | UUID | PK |
| hospital_id | UUID | FK |
| doctor_id | UUID | FK |
| user_id | UUID | FK |
| date | DATE | NOT NULL |
| time | TIME | NOT NULL |
| status | ENUM('pending','confirmed','cancelled','completed') | DEFAULT 'pending' |
| notes | TEXT | NULL |

## 13.2 ERD Summary

```
District (1) ────── (N) Hospital
Hospital (N) ────── (N) Specialty  (via HospitalSpecialty)
Hospital (1) ────── (N) Doctor
Hospital (1) ────── (N) Review
Hospital (1) ────── (N) Appointment
User (1) ────── (N) Review
User (1) ────── (N) Appointment
Doctor (1) ────── (N) Appointment
```

## 13.3 Indexes

| الجدول | الفهرس | النوع | التبرير |
|--------|--------|-------|---------|
| hospital | name_ar | BTREE | البحث بالاسم |
| hospital | type | BTREE | تصفية حسب النوع |
| hospital | district_id | BTREE | تصفية حسب المديرية |
| hospital | latitude, longitude | GIST (SPATIAL) | البحث الجغرافي |
| hospital | status | BTREE | المستشفيات النشطة فقط |
| hospital | avg_rating | BTREE | ترتيب حسب التقييم |
| review | hospital_id | BTREE | عرض تقييمات المستشفى |
| review | user_id | BTREE | تقييمات المستخدم |
| doctor | hospital_id | BTREE | أطباء المستشفى |
| doctor | specialization | BTREE | بحث بالأطباء حسب التخصص |
| user | email | UNIQUE | منع تكرار البريد |
| user | phone | UNIQUE | منع تكرار الهاتف |

## 13.4 Normalization

- جميع الجداول في **3NF** (Third Normal Form)
- لا توجد تبعيات متعدية
- فك الارتباط بين المستشفى والتخصص عبر جدول وسيط (HospitalSpecialty)
- استخدام UUID بدلاً من ID المتزايد لأسباب أمنية وتوزيعية

## 13.5 Database Constraints

| القيد | الوصف |
|-------|-------|
| FK Constraints | تكامل العلاقات بين الجداول |
| UNIQUE (email) | منع تكرار البريد الإلكتروني للمستخدمين |
| UNIQUE (phone) | منع تكرار رقم الهاتف للمستخدمين |
| CHECK (rating 1-5) | التقييم بين 1 و 5 نجوم |
| NOT NULL for required fields | الاسم، النوع، الموقع إلزامية |
| DEFAULT values | قيم افتراضية مناسبة |