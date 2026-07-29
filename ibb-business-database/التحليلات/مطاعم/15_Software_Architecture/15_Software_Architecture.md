# المرحلة الخامسة عشرة: Software Architecture - قطاع المطاعم في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 15_Software_Architecture.md

---

## 15.1 النمط المعماري (Architecture Pattern)

| العنصر | الاختيار |
|--------|---------|
| **النمط** | Modular Monolith (ثم Microservices لاحقًا) |
| **الطبقات** | 3-tier: Presentation → Business Logic → Data |
| **الاتصال** | REST API + WebSocket (real-time) |
| **التنسيق** | API Gateway (لجميع الخدمات) |
| **اللغة** | TypeScript (Node.js) أو Python (Django) |

## 15.2 مخطط العمارة

```
┌──────────────────────────────────────────────────────┐
│                    العميل (Client)                    │
│  ┌──────────┐  ┌──────────┐  ┌────────────────────┐ │
│  │  Android  │  │    iOS   │  │  PWA (Web)         │ │
│  └──────────┘  └──────────┘  └────────────────────┘ │
└──────────────────────┬───────────────────────────────┘
                       │ HTTPS + WSS
┌──────────────────────▼───────────────────────────────┐
│                CDN (Cloudflare)                      │
│              + Load Balancer (NGINX)                 │
└──────────────────────┬───────────────────────────────┘
                       │
┌──────────────────────▼───────────────────────────────┐
│                  API Gateway                         │
│           (Authentication, Rate Limiting, Routing)   │
└──────────────────────┬───────────────────────────────┘
                       │
┌──────────────────────▼───────────────────────────────┐
│                  Application Layer                   │
│                                                      │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  │
│  │ Auth Module │  │ Restaurant   │  │ Order      │  │
│  │             │  │ Module       │  │ Module     │  │
│  └─────────────┘  └──────────────┘  └────────────┘  │
│                                                      │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  │
│  │ Payment     │  │ Rating       │  │ Search     │  │
│  │ Module      │  │ Module       │  │ Module     │  │
│  └─────────────┘  └──────────────┘  └────────────┘  │
│                                                      │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  │
│  │ Notification│  │ Analytics    │  │ Chat       │  │
│  │ Module      │  │ Module       │  │ Module     │  │
│  └─────────────┘  └──────────────┘  └────────────┘  │
└──────────────────────┬───────────────────────────────┘
                       │
┌──────────────────────▼───────────────────────────────┐
│                  Data Layer                          │
│                                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────┐ │
│  │  PostgreSQL   │  │   Redis      │  │  S3/R2    │ │
│  │ (Main DB)     │  │ (Cache +     │  │ (Images)  │ │
│  │               │  │  WebSocket)  │  │            │ │
│  └──────────────┘  └──────────────┘  └────────────┘ │
│                                                      │
│  ┌──────────────────────────────────────────────┐    │
│  │         Elasticsearch (Search)               │    │
│  └──────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────┘
```

## 15.3 مكونات النظام (System Components)

### أ. Frontend (Client Apps)

| المكون | التقنية | الغرض |
|--------|---------|-------|
| تطبيق Android | Kotlin/Jetpack | تطبيق الزبون والمطعم والسائق |
| تطبيق iOS | Swift/SwiftUI | تطبيق الزبون والمطعم والسائق |
| PWA | React/Vue.js + Tailwind | ويب سريع لكافة الأجهزة |
| لوحة الإدارة | React + Material UI | إدارة النظام بالكامل |

### ب. Backend (Server)

| المكون | التقنية | الغرض |
|--------|---------|-------|
| API Server | Node.js/Express | نقاط API الرئيسية |
| WebSocket Server | Socket.IO | اتصال مباشر للطلبات والتتبع |
| Task Queue | Bull (Redis) | معالجة الخلفية (إشعارات، تقارير) |
| Search Engine | Elasticsearch | بحث سريع في المطاعم والمنيو |

### ج. خدمات خارجية (Third-party)

| الخدمة | الغرض |
|--------|-------|
| Mapbox/Google Maps | خرائط، تتبع، تحديد المواقع |
| Twilio/MessageBird | SMS للتحقق (OTP) |
| Firebase/OneSignal | Push notifications |
| Stripe/PayMob | دفع إلكتروني |
| Sentry | مراقبة الأخطاء |

## 15.4 تدفق البيانات (Data Flow)

### تدفق الطلب

```
الزبون → API Gateway → Order Module → Restaurant Module
    → إشعار للمطعم (WebSocket)
    → المطعم يؤكد → Driver Module (يبحث عن سائق)
    → إشعار للسائق (WebSocket) → سائق يقبل
    → إشعار للزبون (WebSocket + Push)
    → Driver Module يحدّث الموقع (WebSocket)
    → إشعار "تم التوصيل" للزبون
    → Rating Module (يطلب تقييمًا)
```

## 15.5 استراتيجية Deployment

| البيئة | الغرض | الإعدادات |
|--------|-------|-----------|
| **Development** | تطوير محلي | Docker Compose |
| **Staging** | اختبار | VPS واحد (Ubuntu) |
| **Production** | إنتاج | VPS + failover |

### الموارد المبدئية (Scale 1)

| المورد | المواصفات |
|--------|-----------|
| App Server | 2 vCPU, 4GB RAM |
| Database | 2 vCPU, 4GB RAM, 50GB SSD |
| Redis | 1 vCPU, 2GB RAM |
| Storage | Cloudflare R2 (غير محدود) |

## 15.6 استراتيجية التوسع (Scalability Strategy)

| المرحلة | المستخدمون | الطلبات/يوم | الخطة |
|---------|-----------|-------------|-------|
| **MVP (شهر 1-3)** | 5,000 | 100 | 1 server + DB |
| **نمو (شهر 4-6)** | 20,000 | 500 | 2 servers, read replica |
| **توسع (شهر 7-12)** | 50,000 | 1,500 | Load balancer + 3 servers |
| **مستقبلي** | 100,000+ | 5,000+ | Microservices, Kubernetes |

## 15.7 استراتيجية التطوير

| المرحلة | المدة | المخرجات |
|---------|-------|---------|
| **POC** | أسبوعان | API أساسي + PWA بسيطة |
| **MVP** | 6-8 أسابيع | تطبيق زبون + مطعم + توصيل أساسي |
| **Beta** | 4 أسابيع | اختبار مع 50 مطعم و500 مستخدم |
| **Launch** | أسبوعان | إطلاق رسمي + حملة تسويقية |
| **Iterate** | مستمر | تحسينات، ميزات جديدة |

---

## المصادر

- Martin Fowler - Microservices vs Monolith
- Node.js Architecture Best Practices
- Firebase / OneSignal Documentation
- AWS Well-Architected Framework (مبادئ معماریة)