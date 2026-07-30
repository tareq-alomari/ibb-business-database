# المرحلة الخامسة عشرة: Software Architecture - قطاع التصميم في محافظة إب

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
│  │ Auth Module │  │ Provider     │  │ Booking    │  │
│  │             │  │ Module       │  │ Module     │  │
│  └─────────────┘  └──────────────┘  └────────────┘  │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  │
│  │ Payment     │  │ Rating       │  │ Search     │  │
│  │ Module      │  │ Module       │  │ Module     │  │
│  └─────────────┘  └──────────────┘  └────────────┘  │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  │
│  │ Notification│  │ Analytics    │  │ Gallery    │  │
│  │ Module      │  │ Module       │  │ Module     │  │
│  └─────────────┘  └──────────────┘  └────────────┘  │
└──────────────────────┬───────────────────────────────┘
                       │
┌──────────────────────▼───────────────────────────────┐
│                  Data Layer                          │
│                                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────┐ │
│  │  PostgreSQL   │  │   Redis      │  │  S3/R2    │ │
│  │ (Main DB)     │  │ (Cache + WS) │  │ (Images)  │ │
│  └──────────────┘  └──────────────┘  └────────────┘ │
│                                                      │
└──────────────────────────────────────────────────────┘
```

## 15.3 مكونات النظام (System Components)

### أ. Frontend (Client Apps)

| المكون | التقنية | الغرض |
|--------|---------|-------|
| تطبيق Android | Kotlin/Jetpack | تطبيق العميل ومقدم الخدمة |
| تطبيق iOS | Swift/SwiftUI | تطبيق العميل ومقدم الخدمة |
| PWA | React/Vue.js + Tailwind | ويب سريع لكافة الأجهزة |
| لوحة الإدارة | React + Material UI | إدارة النظام بالكامل |

### ب. Backend (Server)

| المكون | التقنية | الغرض |
|--------|---------|-------|
| API Server | Node.js/Express | نقاط API الرئيسية |
| WebSocket Server | Socket.IO | اتصال مباشر للحجوزات |
| Task Queue | Bull (Redis) | معالجة الخلفية (إشعارات، تقارير) |

### ج. خدمات خارجية (Third-party)

| الخدمة | الغرض |
|--------|-------|
| Mapbox/Google Maps | خرائط، تحديد المواقع |
| Twilio/MessageBird | SMS للتحقق (OTP) |
| Firebase/OneSignal | Push notifications |
| PayMob | دفع إلكتروني |
| Sentry | مراقبة الأخطاء |

## 15.4 تدفق البيانات (Data Flow)

### تدفق الحجز

```
العميل → API Gateway → Booking Module → Provider Module
    → إشعار لمقدم الخدمة (WebSocket)
    → مقدم الخدمة يؤكد → إشعار للعميل
    → تتم الخدمة → Rating Module (يطلب تقييمًا)
```

## 15.5 استراتيجية Deployment

| البيئة | الغرض | الإعدادات |
|--------|-------|-----------|
| **Development** | تطوير محلي | Docker Compose |
| **Staging** | اختبار | VPS واحد (Ubuntu) |
| **Production** | إنتاج | VPS + failover |

### الموارد المبدئية

| المورد | المواصفات |
|--------|-----------|
| App Server | 2 vCPU, 4GB RAM |
| Database | 2 vCPU, 4GB RAM, 50GB SSD |
| Redis | 1 vCPU, 2GB RAM |
| Storage | Cloudflare R2 (غير محدود) |

## 15.6 استراتيجية التوسع (Scalability Strategy)

| المرحلة | المستخدمون | الحجوزات/يوم | الخطة |
|---------|-----------|-------------|-------|
| **MVP (شهر 1-3)** | 5,000 | 50 | 1 server + DB |
| **نمو (شهر 4-6)** | 20,000 | 200 | 2 servers, read replica |
| **توسع (شهر 7-12)** | 50,000 | 500 | Load balancer + 3 servers |

---

## المصادر

- Martin Fowler - Microservices vs Monolith
- Node.js Architecture Best Practices
- AWS Well-Architected Framework
