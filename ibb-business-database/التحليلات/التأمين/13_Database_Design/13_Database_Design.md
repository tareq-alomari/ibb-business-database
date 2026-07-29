# تصميم قاعدة البيانات: نظام التأمين الرقمي

## الكيانات والخصائص

### 1. Company (شركة تأمين)
| العمود | النوع | الوصف |
|--------|------|-------|
| id | UUID | معرف فريد |
| name_ar | VARCHAR(255) | الاسم بالعربية |
| name_en | VARCHAR(255) | الاسم بالإنجليزية |
| type | ENUM | فرع مباشر، وكيل |
| phone | VARCHAR(50) | رقم الهاتف |
| address | TEXT | العنوان في إب |
| district_id | UUID FK | معرف المديرية |
| is_active | BOOLEAN | نشط أم لا |
| created_at | TIMESTAMP | تاريخ الإضافة |

### 2. Product (منتج تأميني)
| العمود | النوع |
|--------|-------|
| id | UUID PK |
| company_id | UUID FK |
| name_ar | VARCHAR(255) |
| type | ENUM |
| description | TEXT |
| price_range | JSON |
| coverage | TEXT |

### 3. Policy (وثيقة تأمين)
| العمود | النوع |
|--------|-------|
| id | UUID PK |
| user_id | UUID FK |
| product_id | UUID FK |
| policy_number | VARCHAR(50) UNIQUE |
| start_date | DATE |
| end_date | DATE |
| premium_amount | DECIMAL |
| status | ENUM |

### 4. Claim (مطالبة)
| العمود | النوع |
|--------|-------|
| id | UUID PK |
| policy_id | UUID FK |
| user_id | UUID FK |
| description | TEXT |
| amount | DECIMAL |
| status | ENUM |
| documents | JSON |
| created_at | TIMESTAMP |

### 5. User (مستخدم)
| العمود | النوع |
|--------|-------|
| id | UUID PK |
| name | VARCHAR(255) |
| phone | VARCHAR(50) UNIQUE |
| email | VARCHAR(255) |
| password_hash | VARCHAR(255) |
| type | ENUM |

### 6. District (مديرية)
| العمود | النوع |
|--------|-------|
| id | UUID PK |
| name_ar | VARCHAR(100) |
| population | INT |

## العلاقات
```
Company (1) ──── (N) Product
Product (1) ──── (N) Policy
User (1) ──── (N) Policy
Policy (1) ──── (N) Claim
User (1) ──── (N) Claim
District (1) ──── (N) Company
```
