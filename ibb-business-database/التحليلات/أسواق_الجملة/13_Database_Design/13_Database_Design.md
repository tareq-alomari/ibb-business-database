# المرحلة الثالثة عشرة: Database Design - قطاع أسواق الجملة في محافظة إب

## 13.1 الجداول الرئيسية

```sql
التجار (traders)
├── id (PK)
├── name, phone, phone2
├── business_type (wholesale/retail)
├── address, city_district
├── license_number, is_verified
├── rating, total_orders
├── is_active

المنتجات (products)
├── id (PK)
├── trader_id (FK)
├── category_id (FK)
├── name, description
├── unit (kg/liter/carton/piece)
├── price, quantity_available
├── image_url
├── is_featured, is_active

تصنيفات المنتجات (categories)
├── id (PK)
├── name (خضار/فواكه/حبوب/مواد غذائية/دواجن/لحوم)
├── parent_id (FK, self)
├── icon, sort_order

الطلبات (orders)
├── id (PK)
├── buyer_id (FK → users)
├── trader_id (FK → traders)
├── total_amount
├── status (pending/confirmed/shipped/delivered/cancelled)
├── payment_method (cash/wallet)
├── delivery_address, notes
├── created_at, updated_at

بنود الطلب (order_items)
├── id (PK)
├── order_id (FK)
├── product_id (FK)
├── quantity, unit_price
├── subtotal

التوصيل (deliveries)
├── id (PK)
├── order_id (FK)
├── driver_id (FK → users)
├── status (pending/picked_up/in_transit/delivered)
├── estimated_time, actual_delivery_time
├── location_tracking (JSON)

المستخدمون (users)
├── id (PK)
├── phone (unique)
├── name, role (trader/retailer/driver/admin)
├── is_verified, created_at
```

## 13.2 العلاقات

| العلاقة | النوع |
|---------|-------|
| تاجر ← منتجات | 1:ن |
| تصنيف ← منتجات | 1:ن |
| مشتري ← طلبات | 1:ن |
| طلب ← بنود طلب | 1:ن |
| طلب ← توصيل | 1:1 |
| طلب ← تاجر | ن:1 |
