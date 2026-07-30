# المرحلة السادسة عشرة: Technical Stack - قطاع التصوير في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 16_Technical_Stack.md

---

## 16.1 التقنيات المقترحة

### الواجهة الأمامية (Frontend)

| التقنية | الإصدار | الغرض |
|---------|---------|-------|
| PWA (Progressive Web App) | - | تطبيق ويب يعمل على جميع الأجهزة |
| React.js | 18 | إطار العمل الرئيسي للويب |
| Next.js | 14 | SSR، تحسين SEO، أداء عالٍ |
| Tailwind CSS | 3 | تصميم سريع ومتجاوب |
| TypeScript | 5 | أمان أنواع، كود أنظف |

### تطبيقات الموبايل (Mobile)

| التقنية | الإصدار | الغرض |
|---------|---------|-------|
| Flutter | 3.x | تطبيق مشترك Android + iOS |
| Riverpod / Bloc | - | إدارة الحالة |
| Google Maps Flutter | - | خرائط وتحديد مواقع |
| Firebase Cloud Messaging | - | إشعارات |

### الواجهة الخلفية (Backend)

| التقنية | الإصدار | الغرض |
|---------|---------|-------|
| Node.js | 20 LTS | بيئة التشغيل |
| Express.js / Fastify | 4.x | إطار API |
| TypeScript | 5 | أمان أنواع |
| Prisma | 5 | ORM لقاعدة البيانات |
| Socket.IO | 4 | WebSocket للاتصال المباشر |
| BullMQ | 5 | معالجة المهام الخلفية |
| Zod | 3 | التحقق من صحة البيانات |

### قاعدة البيانات (Database)

| التقنية | الإصدار | الغرض |
|---------|---------|-------|
| PostgreSQL | 16 | قاعدة البيانات الرئيسية |
| Redis | 7 | تخزين مؤقت، WebSocket، قوائم انتظار |
| Elasticsearch | 8 | بحث نصي متقدم (اختياري) |

### البنية التحتية (Infrastructure)

| التقنية | الغرض |
|---------|-------|
| Docker | حاويات التطبيق |
| Docker Compose | تنسيق الخدمات محليًا |
| NGINX | عكس وكيل (Reverse Proxy + Load Balancer) |
| Cloudflare | CDN، أمان، SSL |
| GitHub Actions | CI/CD |
| Sentry | مراقبة الأخطاء |
| UptimeRobot | مراقبة التوفر |

### التخزين والوسائط

| التقنية | الغرض |
|---------|-------|
| Cloudflare R2 | تخزين الصور والملفات |
| Sharp / ImageMagick | تحسين الصور وضغطها |
| WebP | صيغة الصور المثلى للويب |

### خدمات خارجية

| الخدمة | الغرض |
|--------|-------|
| Twilio / MessageBird | إرسال SMS (OTP) |
| OneSignal / Firebase Cloud Messaging | Push notifications |
| PayMob | دفع إلكتروني |
| Google Maps / Mapbox | خرائط وتحديد مواقع |
| Google Analytics / Mixpanel | تحليلات المستخدمين |

## 16.2 مقارنة بدائل

| المكون | الخيار 1 | الخيار 2 | الاختيار | السبب |
|--------|---------|---------|---------|-------|
| Framework Frontend | React | Vue.js | React | مجتمع أكبر، مكتبات أكثر |
| Mobile App | Flutter | React Native | Flutter | أداء أعلى، تطوير أسرع |
| لغة Backend | TypeScript/Node | Python | TypeScript/Node | نفس لغة الواجهة |
| ORM | Prisma | TypeORM | Prisma | تجربة مطور أفضل |
| Database | PostgreSQL | MySQL | PostgreSQL | JSONB، Full-text search |
| Storage | S3 | R2 | R2 | تكلفة صفرية للخروج |

## 16.3 المتطلبات البيئية (Environment Requirements)

### Development

| الأداة | الإصدار الأدنى |
|--------|---------------|
| Node.js | 18.0+ |
| npm / yarn | latest |
| Docker | 24+ |
| Docker Compose | 2.20+ |
| PostgreSQL | 16 |
| Redis | 7 |
| Git | 2.40+ |

### Production

| المورد | الحد الأدنى |
|--------|-------------|
| CPU | 2 vCPU |
| RAM | 4 GB |
| Storage | 50 GB SSD |
| OS | Ubuntu 22.04 LTS |
| Node.js | 20 LTS |
| PostgreSQL | 16 |
| Redis | 7 |

---

## المصادر

- React Documentation (react.dev)
- Flutter Documentation (flutter.dev)
- Node.js Best Practices (nodejs.org)
- PostgreSQL Documentation
- Cloudflare R2 Documentation
