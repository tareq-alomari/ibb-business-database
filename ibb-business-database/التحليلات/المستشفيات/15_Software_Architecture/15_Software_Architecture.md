# المرحلة الخامسة عشرة: Software Architecture - قطاع المستشفيات في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 15_Software_Architecture.md

---

## 15.1 Proposed Architecture: Modular Monolith

### لماذا Modular Monolith؟

| المبرر | الشرح |
|--------|-------|
| **بساطة النشر** | تطبيق واحد (monolith) يبسط النشر في بيئة ذات إنترنت غير مستقر |
| **أداء عالي** | لا تأخير في الاتصال بين الخدمات |
| **تطوير سريع** | يمكن لفريق صغير تطويره وصيانته |
| **تكلفة أقل** | خادم واحد (أو اثنان) بدلاً من عدة خدمات |
| **توسع مستقبلي** | يمكن تحويل الوحدات لـ Microservices لاحقًا |

## 15.2 Architecture Diagram

```
┌──────────────────────────────────────────────────┐
│                   Client Layer                    │
│  ┌─────────────┐  ┌─────────────┐               │
│  │  Web App    │  │  Mobile App │               │
│  │  (Next.js)  │  │  (PWA)      │               │
│  └──────┬──────┘  └──────┬──────┘               │
└─────────┼─────────────────┼──────────────────────┘
          │                 │
          ▼                 ▼
┌──────────────────────────────────────────────────┐
│                API Gateway                        │
│  ┌────────────────────────────────────────────┐  │
│  │  Rate Limiting | Auth | CORS | Logging     │  │
│  └────────────────────────────────────────────┘  │
└──────────────────────┬───────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────┐
│              Application Layer                    │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│  │  Search  │ │ Hospital │ │  Auth    │        │
│  │  Module  │ │  Module  │ │  Module  │        │
│  └──────────┘ └──────────┘ └──────────┘        │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│  │  Review  │ │Analytics │ │  Map     │        │
│  │  Module  │ │  Module  │ │  Module  │        │
│  └──────────┘ └──────────┘ └──────────┘        │
└──────────────────────┬───────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────┐
│               Domain Layer                        │
│  ┌────────────────────────────────────────────┐  │
│  │  Entities | Value Objects | Repositories   │  │
│  │  Domain Services | Domain Events           │  │
│  └────────────────────────────────────────────┘  │
└──────────────────────┬───────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────┐
│              Infrastructure Layer                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│  │PostgreSQL│ │  Redis   │ │  S3/Minio│        │
│  │ +PostGIS │ │  Cache   │ │  Images  │        │
│  └──────────┘ └──────────┘ └──────────┘        │
└──────────────────────────────────────────────────┘
```

## 15.3 Design Patterns

| النمط | الاستخدام | المبرر |
|-------|-----------|--------|
| **Repository Pattern** | طبقة البيانات | فصل منطق الاستعلام عن منطق الأعمال |
| **CQRS** | التقارير | فصل قراءة الإحصائيات عن الكتابة العادية |
| **Unit of Work** | المعاملات | ضمان تكامل العمليات |
| **Strategy** | البحث | تبديل استراتيجيات البحث (نص، مكاني) |
| **Observer/Event** | التقييمات | إرسال إشعارات عند إضافة تقييم جديد |
| **Factory** | إنشاء الكيانات | إنشاء كيان المستشفى من مصادر مختلفة |
| **Dependency Injection** | إدارة الاعتماديات | قابلية الاختبار والصيانة |

## 15.4 Clean Architecture Layers

### Layer 1: Domain (Core)

```
src/domain/
├── entities/
│   ├── Hospital.ts
│   ├── Doctor.ts
│   ├── Review.ts
│   ├── User.ts
│   ├── Specialty.ts
│   └── District.ts
├── value-objects/
│   ├── Location.ts
│   ├── PhoneNumber.ts
│   └── Rating.ts
├── repositories/
│   ├── IHospitalRepository.ts
│   ├── IDoctorRepository.ts
│   └── IReviewRepository.ts
└── services/
    ├── HospitalService.ts
    ├── SearchService.ts
    └── RatingService.ts
```

### Layer 2: Application

```
src/application/
├── use-cases/
│   ├── CreateHospitalUseCase.ts
│   ├── SearchHospitalsUseCase.ts
│   ├── AddReviewUseCase.ts
│   └── GetNearbyHospitalsUseCase.ts
├── dto/
│   ├── HospitalDTO.ts
│   ├── SearchDTO.ts
│   └── ReviewDTO.ts
└── interfaces/
    ├── IHospitalService.ts
    └── ISearchService.ts
```

### Layer 3: Infrastructure

```
src/infrastructure/
├── database/
│   ├── prisma/
│   │   └── schema.prisma
│   └── repositories/
│       ├── HospitalRepository.ts
│       └── ReviewRepository.ts
├── cache/
│   └── RedisCache.ts
├── storage/
│   └── ImageStorage.ts
└── external/
    ├── MapService.ts
    └── SMSService.ts
```

### Layer 4: Presentation (API)

```
src/api/
├── controllers/
│   ├── HospitalController.ts
│   ├── ReviewController.ts
│   ├── AuthController.ts
│   └── AnalyticsController.ts
├── middleware/
│   ├── auth.ts
│   ├── rateLimiter.ts
│   └── validator.ts
├── routes/
│   ├── hospitalRoutes.ts
│   ├── reviewRoutes.ts
│   └── authRoutes.ts
└── validators/
    ├── hospitalSchema.ts
    └── reviewSchema.ts
```