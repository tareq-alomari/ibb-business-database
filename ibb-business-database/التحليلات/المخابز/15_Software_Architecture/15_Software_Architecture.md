# المرحلة الخامسة عشرة: بنية البرمجيات - قطاع المخابز في محافظة إب

> **تاريخ التقرير**: يوليو 2026

---

## نظرة عامة على البنية

```
Client (React)
    ↓ REST API
API Gateway (Express/Next.js)
    ↓
Service Layer
    ├── Bakery Service
    ├── Review Service
    ├── User Service
    └── Geo Service
    ↓
Data Layer (PostgreSQL + Redis)
```

## الطبقات المعمارية

### طبقة العرض (Presentation)
- تطبيق ويب (React + Next.js)
- واجهة مستخدم تفاعلية
- خرائط تفاعلية (Leaflet/Mapbox)
- متجاوب مع جميع الأجهزة

### طبقة الخدمات (Services)
- RESTful API
- معالجة المنطق التجاري
- التحقق من الصلاحيات
- التخزين المؤقت (Caching)

### طبقة البيانات (Data)
- PostgreSQL: البيانات الرئيسية
- Redis: التخزين المؤقت والجلسات
- Elasticsearch: البحث النصي

## نمط العمارة

**Clean Architecture** مع عناصر من **Microservices**:
- فصل واضح بين الطبقات
- قابلية اختبار عالية
- استقلالية المكونات
- سهولة الصيانة والتوسع

## تدفق البيانات

1. يرسل المتصفح طلب HTTP
2. API Gateway يعيد التوجيه
3. Service Layer يعالج الطلب
4. Data Layer يخزن/يستعيد البيانات
5. يتم إرجاع الاستجابة بتنسيق JSON

## تقنيات إضافية

| التقنية | الاستخدام |
|---------|-----------|
| Docker | حاويات التطبيق |
| Nginx | خادم وكيل عكسي |
| PostgreSQL GIS | الاستعلامات الجغرافية |
| Redis | تخزين مؤقت |
| Cloudflare CDN | تسريع المحتوى |