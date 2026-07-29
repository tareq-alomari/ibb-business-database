# تصميم قاعدة البيانات: الأسواق العامة في محافظة إب

## نموذج البيانات المفاهيمي

### جدول الأسواق (markets)
- market_id (PK)
- name_ar
- location (GIS point)
- district_id (FK)
- market_type (central, secondary, seasonal)
- total_area
- opening_hours
- established_date
- status

### جدول التجار (traders)
- trader_id (PK)
- full_name
- shop_number
- market_id (FK)
- business_type (food, clothes, household)
- license_number
- contact_info
- start_date
- rating

### جدول السلع (products)
- product_id (PK)
- name_ar
- category_id (FK)
- trader_id (FK)
- unit_price
- origin
- stock_quantity
- expiry_date

### جدول فئات السلع (categories)
- category_id (PK)
- name_ar
- parent_category_id (FK)
- description

### جدول المبيعات (transactions)
- transaction_id (PK)
- trader_id (FK)
- product_id (FK)
- quantity
- unit_price
- total_amount
- transaction_date
- payment_method

### جدول تقييمات التجار (ratings)
- rating_id (PK)
- trader_id (FK)
- user_id
- score (1-5)
- review_text
- created_at

## العلاقات الرئيسية
- سوق ← ← تاجر (واحد إلى متعدد)
- تاجر ← ← سلعة (واحد إلى متعدد)
- فئة ← ← سلعة (واحد إلى متعدد)
- تاجر ← ← معاملة (واحد إلى متعدد)

## متطلبات الأداء
- فهرسة على market_id, trader_id, تاريخ المعاملة
- دعم الاستعلامات المكانية لتحديد موقع الأسواق
- تخزين مؤقت للأسعار الشائعة لتسريع العرض
- نسخ احتياطي يومي للبيانات
