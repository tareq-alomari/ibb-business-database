# تصميم قاعدة البيانات – منصة أسواق المواشي

## نظام إدارة قواعد البيانات
PostgreSQL – لقوته في التعامل مع البيانات العلائقية المعقدة ودعمه للبيانات الجغرافية عبر PostGIS.

## الجداول الرئيسية

### Users (المستخدمون)
id, name, phone, email, role (seller/buyer/admin/vet), location, rating, created_at

### Livestock (المواشي)
id, seller_id, type (cow/sheep/goat/camel), breed, age, weight, price, health_status, vaccinated, description, images[], created_at, status (active/sold/removed)

### Listings (الإعلانات)
id, livestock_id, listing_type (fixed/auction), start_price, current_price, end_date, views_count, is_featured, created_at

### Veterinary_Reports (التقارير البيطرية)
id, livestock_id, vet_id, report_date, diagnosis, treatment, vaccination_record, overall_health

### Transactions (المعاملات)
id, listing_id, buyer_id, seller_id, amount, payment_method, status, transaction_date

### Reviews (التقييمات)
id, reviewer_id, reviewee_id, transaction_id, rating, comment, created_at

### Messages (الرسائل)
id, sender_id, receiver_id, listing_id, message_text, is_read, created_at

## العلاقات
- المستخدم لديه عدة إعلانات ومعاملات
- الإعلان مرتبط بماشية واحدة
- كل ماشية قد يكون لها عدة تقارير بيطرية
- المعاملة تربط بين بائع ومشتري وإعلان
- التقييمات مرتبطة بالمعاملات

## الفهرسة
فهرس على (type, price, location, status) لتسريع البحث، وفهرس على (created_at) للترتيب الزمني.
