# المرحلة الخامسة عشرة: Software Architecture - قطاع أسواق الجملة في محافظة إب

## 15.1 العمارة المقترحة

```
Client Layer
├── Android App (Kotlin/Java)
├── PWA (Progressive Web App)
└── Website (React)

API Gateway (Nginx / Cloudflare)

Application Layer (Node.js)
├── Auth Module (تسجيل الدخول OTP)
├── Products Module (إدارة المنتجات والأسعار)
├── Orders Module (إدارة الطلبات)
├── Traders Module (إدارة التجار)
├── Delivery Module (إدارة التوصيل والتتبع)
└── Payments Module (المحفظة الرقمية والدفع)

Data Layer
├── PostgreSQL (قاعدة البيانات الرئيسية)
├── Redis (تخزين مؤقت للأسعار اليومية)
└── Cloudflare R2 (صور المنتجات)
```

## 15.2 تدفق البيانات

```
تاجر ← [يضيف منتجًا] ← API ← PostgreSQL
    → Redis (تحديث الأسعار اليومية)
    → إشعار فوري للمشتركين
مشتري ← [يبحث عن منتج] ← API ← Redis/PostgreSQL
    → يعرض النتائج مع الأسعار
    → [يقدم طلبًا] ← API ← PostgreSQL
    → إشعار للتاجر والسائق
```

## 15.3 المبادئ المعمارية

| المبدأ | التطبيق |
|--------|---------|
| Offline-first | عرض آخر الأسعار بدون إنترنت |
| Real-time | تحديث الأسعار عبر WebSocket |
| Micro-services | خدمات منفصلة للمنتجات والطلبات والتوصيل |
| Scalable | تصميم يتحمل نمو عدد المستخدمين |
| Arabic-first | RTL في كل المستويات |
