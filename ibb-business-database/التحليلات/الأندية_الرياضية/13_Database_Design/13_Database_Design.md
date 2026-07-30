# المرحلة الثالثة عشرة: Database Design - قطاع الأندية والمراكز الرياضية في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 13_Database_Design.md

---

## 13.1 نظام إدارة قواعد البيانات

| العنصر | الاختيار |
|--------|---------|
| قاعدة البيانات الرئيسية | PostgreSQL 16 |
| تخزين مؤقت | Redis 7 |
| بحث نصي | PostgreSQL Full-Text Search |
| تخزين الصور | Cloudflare R2 |
| ORM | Prisma (TypeScript) |

## 13.2 الجداول الرئيسية

- **users**: المستخدمون (id, phone, name, role)
- **addresses**: العناوين (id, user_id, lat, lng, address)
- **entities**: الجهات المسجلة (id, owner_id, name, type, phone, location, rating, status)
- **service_categories**: تصنيفات الخدمات (id, entity_id, name)
- **services**: الخدمات/المنتجات (id, category_id, name, price, image)
- **reviews**: التقييمات (id, user_id, entity_id, rating, comment)
- **offers**: العروض (id, entity_id, title, discount)
- **notifications**: الإشعارات (id, user_id, title, body)
- **audit_logs**: سجل الأحداث (id, user_id, action, entity_type, entity_id)

## 13.3 العلاقات الرئيسية

- مستخدم → جهة (1:1)
- جهة → تصنيف خدمات (1:ن)
- تصنيف → خدمة (1:ن)
- جهة → تقييم (1:ن)
- جهة → عرض (1:ن)

---
