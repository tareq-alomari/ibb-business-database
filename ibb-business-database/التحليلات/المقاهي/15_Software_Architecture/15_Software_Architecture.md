# المرحلة الخامسة عشرة: Software Architecture - قطاع المقاهي في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 15_Software_Architecture.md

---

## 15.1 النمط المعماري

| العنصر | الاختيار |
|--------|---------|
| **النمط** | Modular Monolith |
| **الطبقات** | 3-tier: Presentation → Business → Data |
| **الاتصال** | REST API + WebSocket |
| **اللغة** | TypeScript (Node.js) |

## 15.2 مخطط العمارة

```
                    العميل (Client)
 ┌──────────┐  ┌──────────┐  ┌────────────┐
 │  Android  │  │    iOS   │  │  PWA (Web) │
 └──────────┘  └──────────┘  └────────────┘
                       │
              API Gateway (NGINX)
                       │
             Application Layer
 ┌─────────┐ ┌──────────┐ ┌──────────┐
 │ Auth    │ │Establisht│ │ Booking  │
 │ Module  │ │ Module   │ │ Module   │
 └─────────┘ └──────────┘ └──────────┘
 ┌─────────┐ ┌──────────┐ ┌──────────┐
 │ Payment │ │ Rating   │ │ Search   │
 │ Module  │ │ Module   │ │ Module   │
 └─────────┘ └──────────┘ └──────────┘
                       │
               Data Layer
 ┌──────────┐ ┌──────────┐ ┌──────────┐
 │PostgreSQL│ │  Redis   │ │  S3/R2   │
 └──────────┘ └──────────┘ └──────────┘
```

## 15.3 مكونات النظام

### Frontend

| المكون | التقنية |
|--------|---------|
| تطبيق Android | Kotlin/Jetpack |
| تطبيق iOS | Swift/SwiftUI |
| PWA | React + Tailwind |
| لوحة الإدارة | React + Material UI |

### Backend

| المكون | التقنية |
|--------|---------|
| API Server | Node.js/Express |
| WebSocket Server | Socket.IO |
| Task Queue | Bull (Redis) |

## 15.4 استراتيجية Deployment

| البيئة | الإعدادات |
|--------|-----------|
| Development | Docker Compose |
| Staging | VPS (Ubuntu) |
| Production | VPS + failover |

### الموارد المبدئية

| المورد | المواصفات |
|--------|-----------|
| App Server | 2 vCPU, 4GB RAM |
| Database | 2 vCPU, 4GB RAM, 50GB SSD |

## 15.5 استراتيجية التطوير

| المرحلة | المدة | المخرجات |
|---------|-------|---------|
| POC | أسبوعان | API أساسي + PWA |
| MVP | 6-8 أسابيع | تطبيق أساسي |
| Beta | 4 أسابيع | اختبار مع مستخدمين |
| Launch | أسبوعان | إطلاق رسمي |

---

## المصادر

- Martin Fowler - Microservices vs Monolith
- Node.js Architecture Best Practices
