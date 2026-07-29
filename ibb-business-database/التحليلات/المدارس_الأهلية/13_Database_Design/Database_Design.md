# تصميم قاعدة البيانات - المدارس الأهلية في إب

## نموذج البيانات المفاهيمي

### الجداول الرئيسية

#### المدارس (schools)
- id (PK)
- name (اسم المدرسة)
- director (مدير المدرسة)
- phone, email, address
- region (المنطقة/المديرية)
- license_number, license_date
- established_year
- logo, images

#### المراحل (levels)
- id (PK)
- school_id (FK)
- level_type (ابتدائي/إعدادي/ثانوي)
- student_capacity
- tuition_fee
- start_grade, end_grade

#### الطلاب (students)
- id (PK)
- school_id (FK)
- level_id (FK)
- full_name
- birth_date
- guardian_name, guardian_phone
- registration_date
- status (نشط/منتقل/متخرج)

#### الموظفون (staff)
- id (PK)
- school_id (FK)
- full_name
- role (معلم/إداري)
- qualification
- hire_date
- salary
- phone, email

#### الرسوم (fees)
- id (PK)
- student_id (FK)
- academic_year
- total_fees, paid, remaining
- due_date
- payment_status

#### الامتحانات (exams)
- id (PK)
- level_id (FK)
- exam_type, date
- max_score

#### الدرجات (grades)
- id (PK)
- student_id (FK)
- exam_id (FK)
- subject, score

## علاقات البيانات
- School 1---* Level
- School 1---* Student
- School 1---* Staff
- Student 1---* Fee
- Level 1---* Student
- Level 1---* Exam
- Student 1---* Grade
- Exam 1---* Grade

## فهارس مقترحة
- school_id, region, level_type
- student_name, guardian_phone
- exam_date, payment_status