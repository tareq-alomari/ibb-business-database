# المرحلة الثالثة عشرة: Database Design - قطاع البذور في محافظة إب

> **التاريخ**:  يوليو 2026  
> **الملف**: 13_Database_Design.md

---

## 13.1 نظام إدارة قواعد البيانات

| العنصر | الاختيار |
|--------|---------|
| **قاعدة البيانات الرئيسية** | PostgreSQL 16 |
| **تخزين مؤقت (Cache)** | Redis 7 |
| **تخزين الصور والملفات** | Cloudflare R2 / AWS S3 |
| **ORM** | Prisma (TypeScript) |

## 13.2 هيكل قاعدة البيانات

### الجداول الرئيسية

```
users
  +-- id (PK, UUID)
  +-- phone (UNIQUE)
  +-- name
  +-- role (enum)
  +-- created_at

seed_types
  +-- id (PK)
  +-- name
  +-- created_at

seed_varieties
  +-- id (PK)
  +-- name
  +-- created_at

distributors
  +-- id (PK)
  +-- name
  +-- created_at

seed_prices
  +-- id (PK)
  +-- name
  +-- created_at

orders
  +-- id (PK)
  +-- name
  +-- created_at

reviews
  +-- id (PK)
  +-- user_id (FK)
  +-- entity_id (FK)
  +-- rating (1-5)
  +-- comment
  +-- created_at

```

## 13.3 العلاقات

| العلاقة | النوع |
|---------|-------|
| مستخدم ← جهة | 1:ن |
| جهة ← تصنيف | 1:1 |
| جهة ← تقييم | 1:ن |

## 13.4 الفهارس (Indexes)

| الجدول | الحقول |
|--------|--------|
| seed_types | name, type, location |
| reviews | entity_id, rating |
| users | phone (UNIQUE) |

## 13.5 استراتيجية النسخ الاحتياطي

| النوع | التكرار |
|-------|---------|
| Full backup | يومي |
| WAL archiving | مستمر |
| مدة الاحتفاظ | 30 يومًا |

---

## المصادر

- PostgreSQL Documentation
- Prisma ORM Schema Design
