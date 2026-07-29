# تصميم قاعدة البيانات

## نظام إدارة قواعد البيانات
MySQL 8.0 أو PostgreSQL 15 – اختيار يعتمد على حجم البيانات ومتطلبات الأداء.

## الجداول الرئيسية

### 1. المحافظة (governorates)
id، name_ar، name_en، code

### 2. المديريات (districts)
id، governorate_id، name_ar، name_en، population

### 3. المدارس (schools)
id، district_id، name_ar، address، phone، stage (ابتدائي/ثانوي)، building_status، student_count، teacher_count، has_water، has_electricity، has_internet، established_year

### 4. المعلمون (teachers)
id، school_id، full_name، national_id، phone، qualification، specialization، job_degree، hire_date، salary_amount، contract_status

### 5. الطلاب (students)
id، school_id، full_name، national_id، birth_date، gender، grade، father_name، phone، enrollment_date، status (منتظم/منقطع)

### 6. الرواتب (salaries)
id، teacher_id، month، year، amount، paid_date، status (مدفوع/غير مدفوع)، notes

### 7. المستخدمون (users)
id، username، password_hash، role (مدير/مشرف/معلم)، school_id، last_login

## العلاقات
- محافظة → مديريات (1:M)
- مديرية → مدارس (1:M)
- مدرسة → معلمون (1:M)
- مدرسة → طلاب (1:M)
- معلم → رواتب (1:M)

## الفهرسة
- فهرس على district_id في جدول المدارس
- فهرس على school_id في جدول المعلمين والطلاب
- فهرس على national_id للمعلمين والطلاب
- فهرس مركب على month+year في جدول الرواتب
