# الرزنامة التقنية - منصة الكليات في إب

## الواجهة الأمامية (Frontend)
- **Framework**: React.js أو Next.js 14
- **اللغة**: TypeScript
- **التصميم**: Tailwind CSS
- **المكونات**: ShadCN UI أو MUI (Material UI) – يدعمان RTL
- **الحالة**: Zustand (خفيف وبسيط)
- **الرسوم البيانية**: Chart.js أو Recharts
- **الخرائط**: Leaflet.js (مفتوح المصدر) أو Mapbox
- **مكتبة RTL**: Tailwind RTL plugin + قواعد CSS مخصصة

## الواجهة الخلفية (Backend)
- **Runtime**: Node.js
- **Framework**: Express.js أو Next.js API Routes
- **اللغة**: TypeScript
- **المصادقة**: JWT + bcrypt
- **التحقق**: Zod
- **البريد الإلكتروني**: Nodemailer
- **الإشعارات**: WebSockets (Socket.io)

## قاعدة البيانات
- **رئيسية**: PostgreSQL (أو MySQL)
- **تخزين مؤقت**: Redis (اختياري)
- **ORM**: Prisma أو Drizzle ORM
- **إدارة الترحيلات**: Prisma Migrate

## الاستضافة والنشر
- **الاستضافة**: VPS محلي أو سحابي (DigitalOcean / Linode)
- **CDN**: Cloudflare (مجاني)
- **حاوية**: Docker + Docker Compose
- **عكس الخادم (Reverse Proxy)**: Nginx
- **إدارة DNS**: Cloudflare

## أدوات التطوير
- **التحكم بالإصدارات**: Git + GitHub/GitLab
- **إدارة المهام**: Trello أو Linear
- **التصميم**: Figma (مجاني للفرق الصغيرة)
- **اختبارات**: Vitest (وحدة)، Playwright (تكامل)
- **مراقبة الأخطاء**: Sentry (مجاني للبدء)
- **تحليل الأداء**: Lighthouse

## بيئة التطوير
- **التحرير**: VS Code
- **إدارة الحزم**: npm أو pnpm
- **لينتر**: ESLint + Prettier
- **قواعد Git**: Conventional Commits
