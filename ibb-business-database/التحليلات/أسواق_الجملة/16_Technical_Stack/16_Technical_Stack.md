# المرحلة السادسة عشرة: Technical Stack - قطاع أسواق الجملة في محافظة إب

## 16.1 التقنيات المقترحة

| المكون | التقنية |
|--------|---------|
| Mobile App | Flutter (أندرويد + iOS) |
| PWA / Website | React + Next.js + Tailwind CSS |
| Backend API | Node.js + Express + TypeScript |
| ORM | Prisma |
| Database | PostgreSQL 16 |
| Cache | Redis 7 |
| File Storage | Cloudflare R2 |
| Push Notifications | Firebase Cloud Messaging |
| Maps / Tracking | OpenStreetMap + Leaflet |
| CI/CD | GitHub Actions |
| Monitoring | Sentry |
| SMS (OTP) | Twilio / محلي |

## 16.2 تبرير الاختيارات

| الاختيار | السبب |
|----------|-------|
| **Flutter** | تطبيق أندرويد أساسي (أغلب المستخدمين)، أداء عال، تطوير سريع |
| **React PWA** | وصول عبر المتصفح، يعمل على أضعف الأجهزة، تثبيت بدون متجر |
| **Node.js** | سرعة عالية، مناسب لـ real-time، جمهور مطورين كبير |
| **PostgreSQL** | بيانات علائقية معقدة، دعم JSON، موثوقية عالية |
| **Redis** | تحديث الأسعار بشكل فوري، تخزين مؤقت |
| **OpenStreetMap** | مجاني، يعمل في اليمن، إمكانية التخصيص |

## 16.3 البدائل

| المكون | الخيار 1 | الخيار 2 | الاختيار |
|--------|---------|---------|---------|
| Mobile | Flutter | React Native | Flutter |
| Web | React | Vue | React |
| Backend | Node.js | Python/Django | Node.js |
| Database | PostgreSQL | MySQL | PostgreSQL |
| Real-time | WebSocket | Firebase | WebSocket |
