# تصميم قاعدة البيانات - قطاع الأثاث في محافظة إب

---

## الكيانات والسمات

### 1. Business (معرض/محل أثاث)

| العمود | النوع | الوصف |
|--------|------|-------|
| id | UUID | معرف فريد |
| name_ar | VARCHAR(255) | الاسم بالعربية |
| category_id | UUID FK | معرف التصنيف |
| subcategory_id | UUID FK | معرف التصنيف الفرعي |
| description | TEXT | وصف المعرض |
| phone | VARCHAR(50) | رقم الهاتف |
| phone2 | VARCHAR(50) | هاتف بديل |
| whatsapp | VARCHAR(50) | رقم واتساب |
| address | TEXT | العنوان |
| district_id | UUID FK | معرف المديرية |
| latitude | DECIMAL(10,8) | خط العرض |
| longitude | DECIMAL(11,8) | خط الطول |
| working_hours | JSON | أوقات العمل |
| images | JSON[] | صور المعرض |
| is_verified | BOOLEAN | تم التحقق |
| status | ENUM | نشط، غير نشط، معلق |
| rating | DECIMAL(2,1) | متوسط التقييم |
| created_at | TIMESTAMP | تاريخ الإضافة |

### 2. Product (منتج)

| العمود | النوع |
|--------|-------|
| id | UUID PK |
| business_id | UUID FK |
| name_ar | VARCHAR(255) |
| category_id | UUID FK |
| description | TEXT |
| price | DECIMAL(12,2) |
| currency | VARCHAR(10) |
| images | JSON[] |
| dimensions | VARCHAR(100) |
| material | VARCHAR(100) |
| color | VARCHAR(50) |
| is_available | BOOLEAN |

### 3. Category (تصنيف)

| العمود | النوع |
|--------|-------|
| id | UUID PK |
| name_ar | VARCHAR(100) |
| icon | VARCHAR(50) |
| sort_order | INT |

### 4. User (مستخدم)

| العمود | النوع |
|--------|-------|
| id | UUID PK |
| name | VARCHAR(255) |
| phone | VARCHAR(50) UNIQUE |
| password_hash | VARCHAR(255) |
| role | ENUM |
| is_active | BOOLEAN |

### 5. Review (تقييم)

| العمود | النوع |
|--------|-------|
| id | UUID PK |
| business_id | UUID FK |
| user_id | UUID FK |
| rating | TINYINT (1-5) |
| comment | TEXT |
| is_approved | BOOLEAN |
| created_at | TIMESTAMP |

### 6. District (مديرية)

| العمود | النوع |
|--------|-------|
| id | UUID PK |
| name_ar | VARCHAR(100) |
| population | INT |

## العلاقات

```
Category (1) ──── (N) Product
Business (1) ──── (N) Product
District (1) ──── (N) Business
User (1) ──── (N) Review
Business (1) ──── (N) Review
```
