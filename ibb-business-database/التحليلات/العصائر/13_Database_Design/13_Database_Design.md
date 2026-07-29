# تصميم قاعدة البيانات - قطاع العصائر في إب

## جدول: المحلات (shops)
| الحقل | النوع | الوصف |
|-------|------|-------|
| id | INT PK | معرف المحل |
| name_ar | VARCHAR(200) | الاسم بالعربية |
| owner_name | VARCHAR(100) | اسم المالك |
| license_number | VARCHAR(50) | رقم الترخيص الصحي |
| phone | VARCHAR(20) | رقم الهاتف |
| address | TEXT | العنوان التفصيلي |
| district | VARCHAR(50) | الحي/المنطقة |
| working_hours | VARCHAR(100) | ساعات العمل |
| delivery_available | BOOLEAN | يتوفر توصيل |
| rating | DECIMAL(2,1) | التقييم العام |
| status | ENUM | نشط / موقف / مغلق |

## جدول: المنتجات (products)
| الحقل | النوع | الوصف |
|-------|------|-------|
| id | INT PK | معرف المنتج |
| shop_id | INT FK | معرف المحل |
| name_ar | VARCHAR(200) | اسم العصير |
| category | ENUM | فواكه / خضار / ميلك شيك / وظيفي |
| ingredients | TEXT | المكونات |
| calories | INT | السعرات الحرارية |
| size_small | DECIMAL(8,2) | سعر الحجم الصغير |
| size_medium | DECIMAL(8,2) | سعر الحجم المتوسط |
| size_large | DECIMAL(8,2) | سعر الحجم الكبير |
| seasonal | BOOLEAN | موسمي |
| image_url | VARCHAR(500) | رابط الصورة |

## جدول: المستخدمون (users)
| الحقل | النوع | الوصف |
|-------|------|-------|
| id | INT PK | معرف المستخدم |
| name | VARCHAR(200) | الاسم الكامل |
| phone | VARCHAR(20) | رقم الهاتف |
| email | VARCHAR(100) | البريد |
| password_hash | VARCHAR(255) | كلمة المرور |
| favorite_shops | JSON | المحلات المفضلة |
| loyalty_points | INT | نقاط الولاء |

## جدول: الطلبات (orders)
| الحقل | النوع | الوصف |
|-------|------|-------|
| id | INT PK | معرف الطلب |
| user_id | INT FK | معرف المستخدم |
| shop_id | INT FK | معرف المحل |
| items | JSON | بنود الطلب |
| total | DECIMAL(10,2) | الإجمالي |
| status | ENUM | جديد / قيد التحضير / في الطريق / تم |
| payment_method | ENUM | نقدي / إلكتروني |
| delivery_address | TEXT | عنوان التوصيل |
| created_at | TIMESTAMP | تاريخ الطلب |

## جداول إضافية
- reviews (التقييمات)
- payments (المدفوعات)
- loyalty_transactions (معاملات الولاء)
- notifications (الإشعارات)
- delivery_zones (مناطق التوصيل)
