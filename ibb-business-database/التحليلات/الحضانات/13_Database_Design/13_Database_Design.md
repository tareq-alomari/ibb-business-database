# تصميم قاعدة البيانات - قطاع الحضانات في إب

## جدول: الحضانات (nurseries)
| الحقل | النوع | الوصف |
|-------|------|-------|
| id | INT PK | معرف الحضانة |
| name_ar | VARCHAR(200) | الاسم بالعربية |
| name_en | VARCHAR(200) | الاسم بالإنجليزية |
| license_number | VARCHAR(50) | رقم الترخيص |
| director_name | VARCHAR(100) | اسم المدير |
| phone | VARCHAR(20) | رقم الهاتف |
| email | VARCHAR(100) | البريد الإلكتروني |
| address | TEXT | العنوان التفصيلي |
| district | VARCHAR(50) | الحي/المنطقة |
| capacity | INT | الطاقة الاستيعابية |
| price_range | VARCHAR(50) | نطاق الأسعار |
| status | ENUM | نشط / موقف / مغلق |
| created_at | TIMESTAMP | تاريخ الإنشاء |

## جدول: الأطفال (children)
| الحقل | النوع | الوصف |
|-------|------|-------|
| id | INT PK | معرف الطفل |
| nursery_id | INT FK | معرف الحضانة |
| parent_id | INT FK | معرف ولي الأمر |
| name | VARCHAR(200) | الاسم الكامل |
| birth_date | DATE | تاريخ الميلاد |
| blood_type | VARCHAR(5) | فئة الدم |
| medical_notes | TEXT | ملاحظات صحية |
| enrollment_date | DATE | تاريخ التسجيل |
| status | ENUM | مسجل / منسحب |

## جدول: أولياء الأمور (parents)
| الحقل | النوع | الوصف |
|-------|------|-------|
| id | INT PK | معرف ولي الأمر |
| name | VARCHAR(200) | الاسم الكامل |
| phone | VARCHAR(20) | رقم الهاتف |
| email | VARCHAR(100) | البريد |
| password_hash | VARCHAR(255) | كلمة المرور |
| id_number | VARCHAR(30) | رقم الهوية |
| work_place | VARCHAR(200) | مكان العمل |

## جدول: الحضور (attendance)
| الحقل | النوع | الوصف |
|-------|------|-------|
| id | INT PK | معرف السجل |
| child_id | INT FK | معرف الطفل |
| date | DATE | التاريخ |
| check_in | TIME | وقت الحضور |
| check_out | TIME | وقت الانصراف |
| status | ENUM | حاضر / غائب / إجازة |

## جداول إضافية
- payments (المدفوعات)
- reviews (التقييمات)
- activities (الأنشطة)
- staff (الموظفون)
- notifications (الإشعارات)
