# المرحلة السادسة عشرة: Technical Stack - قطاع المستشفيات في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 16_Technical_Stack.md

---

## 16.1 التوصيات التقنية

### Frontend

| التقنية | الإصدار | الاستخدام | التبرير |
|---------|---------|-----------|---------|
| **Next.js** | 14+ | Framework | SSR + PWA + SEO المدمج |
| **TypeScript** | 5+ | لغة أساسية | أمان الأنواع، سهولة الصيانة |
| **Tailwind CSS** | 3+ | تصميم | سرعة التطوير، توافق مع RTL |
| **React Query** | 5+ | إدارة API | تخزين مؤقت، تحديث تلقائي |
| **Leaflet.js** | 1.9+ | خرائط | مجاني، خفيف، بدون API key |
| **Zustand** | 4+ | إدارة حالة | بسيط، حجم صغير |
| **React Hook Form** | 7+ | نماذج | أداء عالي، تحقق |

### Backend

| التقنية | الإصدار | الاستخدام | التبرير |
|---------|---------|-----------|---------|
| **Node.js** | 20+ (LTS) | Runtime | سرعة، JavaScript unified stack |
| **Express.js** | 4+ | Framework API | مستقر، مألوف، مجتمع كبير |
| **TypeScript** | 5+ | لغة أساسية | أمان الأنواع |
| **Prisma ORM** | 5+ | ORM | Type-safe، Auto-complete |
| **Zod** | 3+ | Validation | TypeScript-first validation |
| **JWT (jsonwebtoken)** | 9+ | مصادقة | معيار صناعي |
| **Winston** | 3+ | Logging | مستقر، مرن |

### Database

| التقنية | الإصدار | الاستخدام |
|---------|---------|-----------|
| **PostgreSQL** | 16+ | قاعدة البيانات الرئيسية |
| **PostGIS** | 3+ | الاستعلامات المكانية (GPS) |
| **Redis** | 7+ | تخزين مؤقت، جلسات، Rate Limiting |
| **MinIO / S3** | - | تخزين الصور والملفات |

### Mobile (PWA)

| التقنية | الاستخدام |
|---------|-----------|
| **PWA (Progressive Web App)** | دعم عدم الاتصال، إضافة للشاشة الرئيسية |
| **Service Workers** | تخزين البيانات محليًا |
| **IndexedDB** | تخزين Offline-first |

### DevOps

| التقنية | الاستخدام |
|---------|-----------|
| **Docker** | حاويات التطبيق |
| **Docker Compose** | تنظيم الخدمات |
| **GitHub Actions** | CI/CD - اختبارات ونشر |
| **Vercel** | استضافة Frontend (مجاني) |
| **DigitalOcean Droplet** | استضافة Backend ($6-12/شهر) |

### Monitoring

| التقنية | الاستخدام |
|---------|-----------|
| **Sentry** | تتبع الأخطاء (مجاني للبداية) |
| **Google Analytics 4** | تحليلات المستخدمين |
| **UptimeRobot** | مراقبة التوفر (مجاني 50 monitor) |

## 16.2 المبررات

### لماذا Next.js؟
- **SSR** (Server Side Rendering): محتوى متاح لمحركات البحث
- **PWA**: تجربة تطبيق مع دعم Offline
- **RTL**: دعم مدمج للعربية
- **Image Optimization**: تحسين الصور تلقائيًا

### لماذا PostgreSQL + PostGIS؟
- **PostGIS**: إضافة مجانية للبيانات المكانية (بحث بالقرب مني)
- **JSONB**: دعم مرن للبيانات غير المهيكلة
- **موثوقية**: قاعدة بيانات مفتوحة المصدر مثبتة

### لماذا PWA بدلاً من تطبيق أصلي؟
- **تكلفة أقل**: تطبيق واحد للويب والموبايل
- **لا يحتاج متجر**: تحميل مباشر من المتصفح
- **Offline**: يعمل بدون إنترنت
- **تحديثات فورية**: لا يحتاج موافقة متجر

## 16.3 CI/CD Pipeline

```
[Git Push]
    ↓
[GitHub Actions Trigger]
    ↓
[1. Lint & Type Check]
    ↓
[2. Run Tests]
    ↓
[3. Build]
    ↓
[4. Docker Image Build]
    ↓
[5. Deploy to Vercel (Frontend)]
    ↓
[6. Deploy to VPS (Backend)]
```

## 16.4 Hosting Plan

| الخدمة | التكلفة التقديرية | ملاحظات |
|--------|------------------|---------|
| Vercel (Frontend) | مجاني | 100GB bandwidth, SSL تلقائي |
| DigitalOcean (Backend) | $12/شهر | 2GB RAM, 2 vCPU, 60GB SSD |
| PostgreSQL (DigitalOcean) | $15/شهر | Managed DB, 1GB RAM |
| Redis (DigitalOcean) | $7/شهر | Managed Cache |
| Domain (ibb-health.com) | $10/سنة | - |
| **الإجمالي الشهري** | **~$34** | (يمكن خفضه لـ $15 باختيارات أقل) |