# المجموعة التقنية – منصة أسواق المواشي

## الواجهة الأمامية (Frontend)
- **الإطار**: React 18 مع Next.js (لتحسين محركات البحث)
- **اللغة**: TypeScript
- **مكتبات**: Tailwind CSS للتصميم، React Query لإدارة البيانات، Zustand للحالة
- **خرائط**: Leaflet.js + OpenStreetMap لعرض المواقع
- **الإشعارات**: Firebase Cloud Messaging

## الواجهة الخلفية (Backend)
- **الإطار**: Node.js + NestJS (أو Laravel للنسخة العربية)
- **اللغة**: TypeScript/PHP
- **التوثيق**: JWT + OTP عبر SMS
- **قاعدة البيانات**: PostgreSQL + Redis للتخزين المؤقت
- **التخزين**: MinIO (متوافق مع AWS S3)

## الخدمات السحابية
- الاستضافة: VPS محلي في اليمن (أو AWS Bahrain)
- CDN: Cloudflare للتسريع
- البريد: SendGrid أو SES
- SMS: واجهة شركات الاتصالات اليمنية

## أدوات التطوير
- Git + GitHub لإدارة الإصدارات
- ESLint + Prettier للجودة
- Jest + Cypress للاختبارات
- Swagger/OpenAPI لتوثيق API
- Docker + Docker Compose للتطوير المحلي

## الأجهزة المستهدفة
هواتف أندرويد منخفضة إلى متوسطة المواصفات (2-4GB RAM)، اتصال إنترنت 3G/4G، متصفحات حديثة. دعم خاص للشاشات الصغيرة (320px فأعلى).
