# المرحلة الثالثة عشرة: Database Design - قطاع الجامعات في محافظة إب

## 13.1 الجداول الرئيسية

```sql
الجامعات (universities)
├── id (PK)
├── name, type (gov/private), founded_year
├── address, phone, website
├── logo, cover_image
├── rating, total_reviews
├── is_active

الكليات (faculties)
├── id (PK)
├── university_id (FK)
├── name, description

التخصصات (majors)
├── id (PK)
├── faculty_id (FK)
├── name, degree (bachelor/master/phd)
├── duration_years, tuition_fee
├── job_opportunities (high/medium/low)
├── description, requirements

الطلاب (students)
├── id (PK)
├── name, phone, email
├── high_school_score, graduation_year

الطلبات (applications)
├── id (PK)
├── student_id (FK)
├── major_id (FK)
├── status (pending/accepted/rejected)
├── documents (JSONB)
├── created_at

التقييمات (reviews)
├── id (PK)
├── university_id (FK)
├── student_id (FK)
├── rating (1-5), comment
├── is_verified
```

## 13.2 العلاقات

| العلاقة | النوع |
|---------|-------|
| جامعة ← كلية | 1:ن |
| كلية ← تخصص | 1:ن |
| طالب ← طلب | 1:ن |
| تخصص ← طلب | 1:ن |
| جامعة ← تقييم | 1:ن |