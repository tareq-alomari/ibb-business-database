# تصميم قاعدة البيانات - منصة الكليات في إب

## نظام إدارة قواعد البيانات
- **PostgreSQL** (مفضل للعلاقات المعقدة) أو **MySQL**.
- دعم كامل للترجمة (UTF-8 / Arabic Collation).

## الجداول الرئيسية

### 1. universities (الجامعات)
| الحقل | النوع | وصف |
|-------|------|-----|
| id | UUID | مفتاح رئيسي |
| name_ar | VARCHAR(200) | اسم الجامعة بالعربية |
| type | ENUM | حكومي، خاص، أهلي |
| established_year | INTEGER | سنة التأسيس |
| address | TEXT | العنوان |
| logo_url | TEXT | رابط الشعار |
| created_at | TIMESTAMP | |

### 2. colleges (الكليات)
| الحقل | النوع | وصف |
|-------|------|-----|
| id | UUID | مفتاح رئيسي |
| university_id | UUID | مفتاح خارجي للجامعة |
| name_ar | VARCHAR(200) | اسم الكلية |
| description | TEXT | وصف الكلية |
| established_year | INTEGER | |
| student_count | INTEGER | عدد الطلاب |
| faculty_count | INTEGER | عدد أعضاء التدريس |
| rating_avg | DECIMAL(2,1) | التقييم المتوسط |
| location_lat | DECIMAL(10,7) | إحداثيات الموقع |
| location_lng | DECIMAL(10,7) | |
| status | BOOLEAN | نشط/غير نشط |

### 3. majors (التخصصات)
| الحقل | النوع | وصف |
|-------|------|-----|
| id | UUID | |
| college_id | UUID | |
| name_ar | VARCHAR(200) | |
| category | ENUM | طبي، هندسي، إنساني... |
| duration_years | INTEGER | سنوات الدراسة |
| fees | DECIMAL(10,2) | الرسوم السنوية |
| acceptance_rate | DECIMAL(5,2) | نسبة القبول |
| description | TEXT | |

### 4. users (المستخدمون)
| الحقل | النوع | وصف |
|-------|------|-----|
| id | UUID | |
| name | VARCHAR(100) | |
| email | VARCHAR(200) | فريد |
| password_hash | VARCHAR(255) | |
| role | ENUM | user, college_reviewer, college_rep, admin |
| created_at | TIMESTAMP | |

### 5. reviews (التقييمات)
| الحقل | النوع | وصف |
|-------|------|-----|
| id | UUID | |
| college_id | UUID | |
| user_id | UUID | |
| rating | INTEGER(1-5) | |
| comment | TEXT | |
| is_approved | BOOLEAN | مراجعة الإدارة |
| created_at | TIMESTAMP | |

## العلاقات
- university 1---N college
- college 1---N major
- college 1---N review
- user 1---N review
