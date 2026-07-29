# المرحلة الخامسة عشرة: Software Architecture - قطاع مراكز التدريب في محافظة إب

## 15.1 النمط المعماري

```
        [Client Layer]
     ┌─────────────────┐
     │  Web App (PWA)  │
     │  Mobile App     │
     └────────┬────────┘
              │ HTTPS / REST
     ┌────────▼────────┐
     │   API Gateway   │
     │   (Rate Limit,  │
     │    Auth, Cache) │
     └────────┬────────┘
              │
     ┌────────▼────────┐
     │  Application    │
     │  Services       │
     │  (Business      │
     │   Logic Layer)  │
     └────────┬────────┘
              │
     ┌────────▼────────┐
     │  Data Layer     │
     │  PostgreSQL +   │
     │  Redis Cache    │
     └─────────────────┘
```

## 15.2 طبقات التطبيق

| الطبقة | التقنية | المسؤولية |
|--------|---------|-----------|
| Client | React/Vue + PWA | واجهة المستخدم، تجربة التصفح |
| Gateway | Nginx + Express/Next.js | توجيه الطلبات، مصادقة، Cache |
| Services | Node.js / Python | منطق الأعمال، إدارة البيانات |
| Data | PostgreSQL + Redis | تخزين واستعلام البيانات |
| Storage | Cloudflare R2 / S3 | الصور، الشهادات، المرفقات |

## 15.3 المكونات الرئيسية

| المكون | الوظيفة |
|--------|---------|
| Auth Service | تسجيل، تسجيل دخول، JWT، صلاحيات |
| Search Service | بحث متقدم، Elasticsearch للفهرسة |
| Center Service | إدارة بيانات المراكز والمصادقة عليها |
| Program Service | إدارة البرامج والدورات التدريبية |
| Enrollment Service | التسجيل، الدفع، المتابعة |
| Review Service | التقييمات والمراجعات |
| Certificate Service | إصدار وتوثيق الشهادات |
| Notification Service | إشعارات (بريد، SMS، متصفح) |

## 15.4 خصائص معمارية

| الخاصية | التطبيق |
|---------|---------|
| Offline First | PWA مع Service Workers |
| Low Bandwidth | صور مضغوطة، تقليل حجم البيانات |
| Fault Tolerance | إعادة المحاولة، Fallbacks |
| Scalability | Horizontal Scaling عبر Docker |
| Caching | Redis للبيانات المتكررة (المراكز، التصنيفات) |
| Logging | centralized logging مع ELK Stack |

- Monolith أولاً للسرعة، ثم Microservices عند الحاجة
- Docker + Docker Compose للنشر
- CI/CD عبر GitHub Actions
- استضافة على خادم متوسط داخل اليمن أو قريب (مصر/السعودية)
