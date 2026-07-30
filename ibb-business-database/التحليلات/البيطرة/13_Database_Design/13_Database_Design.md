# المرحلة الثالثة عشرة: Database Design - قطاع البيطرة في محافظة إب

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

veterinarians
  +-- id (PK)
  +-- name
  +-- created_at

clinics
  +-- id (PK)
  +-- name
  +-- created_at

animals
  +-- id (PK)
  +-- name
  +-- created_at

vaccinations
  +-- id (PK)
  +-- name
  +-- created_at

appointments
  +-- id (PK)
  +-- name
  +-- created_at

consultations
  +-- id (PK)
  +-- name
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
| veterinarians | name, type, location |
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
