# تصميم قاعدة البيانات: منصة محلات الملابس الرقمية

## الكيانات والخصائص

### 1. Store (محل ملابس)
| العمود | النوع | الوصف |
|--------|------|-------|
| id | UUID | معرف فريد |
| name_ar | VARCHAR(255) | اسم المحل |
| owner_name | VARCHAR(255) | اسم صاحب المحل |
| phone | VARCHAR(50) | رقم الهاتف |
| address | TEXT | العنوان |
| district_id | UUID FK | معرف المديرية |
| category | ENUM | تخصص المحل |
| is_active | BOOLEAN | نشط أم لا |
| rating | DECIMAL(2,1) | التقييم |
| created_at | TIMESTAMP | تاريخ الإضافة |

### 2. Product (منتج)
| العمود | النوع |
|--------|-------|
| id | UUID PK |
| store_id | UUID FK |
| name_ar | VARCHAR(255) |
| category | ENUM |
| gender | ENUM |
| description | TEXT |
| price | DECIMAL(10,2) |
| discount_price | DECIMAL(10,2) |
| sizes | JSON |
| colors | JSON |
| images | JSON |
| stock | INT |
| is_available | BOOLEAN |

### 3. Order (طلب)
| العمود | النوع |
|--------|-------|
| id | UUID PK |
| user_id | UUID FK |
| store_id | UUID FK |
| total_amount | DECIMAL(10,2) |
| status | ENUM |
| delivery_address | TEXT |
| payment_method | ENUM |
| notes | TEXT |
| created_at | TIMESTAMP |
| delivered_at | TIMESTAMP |

### 4. OrderItem (عناصر الطلب)
| العمود | النوع |
|--------|-------|
| id | UUID PK |
| order_id | UUID FK |
| product_id | UUID FK |
| quantity | INT |
| price | DECIMAL(10,2) |
| size | VARCHAR(20) |
| color | VARCHAR(50) |

### 5. User (مستخدم)
| العمود | النوع |
|--------|-------|
| id | UUID PK |
| name | VARCHAR(255) |
| phone | VARCHAR(50) UNIQUE |
| address | TEXT |
| password_hash | VARCHAR(255) |
| type | ENUM |

### 6. District (مديرية)
| العمود | النوع |
|--------|-------|
| id | UUID PK |
| name_ar | VARCHAR(100) |
| delivery_fee | DECIMAL(10,2) |

## العلاقات
```
Store (1) ──── (N) Product
Store (1) ──── (N) Order
User (1) ──── (N) Order
Order (1) ──── (N) OrderItem
Product (1) ──── (N) OrderItem
District (1) ──── (N) Store
```