# تصميم قاعدة البيانات - قطاع المعاهد (إب)

## الجداول الرئيسية

### Institutes (المعاهد)
| الحقل | النوع | الوصف |
|-------|-------|-------|
| id | UUID | معرف فريد |
| name_ar | VARCHAR(200) | اسم المعهد بالعربية |
| name_en | VARCHAR(200) | اسم المعهد بالإنجليزية |
| type | ENUM | حكومي، أهلي، خاص |
| category | ENUM | تقني، صحي، حاسوب، مهني، إداري |
| phone | VARCHAR(50) | رقم الهاتف |
| email | VARCHAR(200) | البريد الإلكتروني |
| address | TEXT | العنوان في إب |
| district | VARCHAR(100) | المديرية |
| established_year | INT | سنة التأسيس |
| accreditation | VARCHAR(200) | جهة الاعتماد |
| description | TEXT | وصف عام |
| logo | VARCHAR(500) | رابط الشعار |
| images | JSON | معرض الصور |
| rating | DECIMAL(2,1) | التقييم العام |
| status | BOOLEAN | نشط / غير نشط |

### Specializations (التخصصات)
| الحقل | النوع | الوصف |
|-------|-------|-------|
| id | UUID | معرف فريد |
| institute_id | UUID FK | معرف المعهد |
| name | VARCHAR(200) | اسم التخصص |
| duration_years | INT | عدد السنوات |
| fees | DECIMAL(12,2) | الرسوم الدراسية |
| description | TEXT | وصف التخصص |
| requirements | TEXT | متطلبات القبول |
| job_opportunities | TEXT | فرص العمل |

### Students (الطلاب)
| الحقل | النوع |
|-------|-------|
| id | UUID PK |
| name | VARCHAR(150) |
| phone | VARCHAR(50) |
| email | VARCHAR(200) |
| password_hash | VARCHAR(255) |
| secondary_cert | VARCHAR(500) |
| status | ENUM |

### Applications (الطلبات)
| الحقل | النوع |
|-------|-------|
| id | UUID PK |
| student_id | UUID FK |
| specialization_id | UUID FK |
| status | ENUM |
| created_at | TIMESTAMP |
| documents | JSON |

## العلاقات
- Institute 1---N Specialization
- Student 1---N Application
- Application N---1 Specialization
- Student N---M Institute (favorites)
- Institute 1---N Review (by Students)
