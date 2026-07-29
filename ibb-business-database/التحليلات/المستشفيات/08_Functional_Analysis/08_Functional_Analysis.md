# المرحلة الثامنة: Functional Analysis - قطاع المستشفيات في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 08_Functional_Analysis.md

---

## 8.1 Feature List

| الرمز | الميزة | الأولوية | الوصف |
|-------|--------|----------|-------|
| **F01** | البحث عن مستشفى | 🟢 عالية | بحث بالاسم، التخصص، الموقع، النوع |
| **F02** | تصفية وفرز | 🟢 عالية | حسب المديرية، النوع (حكومي/خاص)، التقييم |
| **F03** | ملف المستشفى | 🟢 عالية | صفحة كاملة: معلومات، تخصصات، صور |
| **F04** | الخريطة التفاعلية | 🟢 عالية | عرض المستشفيات على الخريطة مع الإحداثيات |
| **F05** | التوجيه إلى المستشفى | 🟡 متوسطة | المسار من موقع المستخدم |
| **F06** | التقييم والمراجعات | 🟢 عالية | تقييم + تعليق، معتدل |
| **F07** | التقارير والإحصائيات | 🟢 عالية | تحليلات عن المستشفيات في المحافظة |
| **F08** | دليل الأطباء | 🟡 متوسطة | الأطباء العاملون في المستشفيات |
| **F09** | إدارة الحسابات | 🟢 عالية | تسجيل، أدوار، صلاحيات |
| **F10** | API مفتوح | 🟡 متوسطة | REST API للمنظمات والمطورين |
| **F11** | حجز المواعيد | 🔴 متأخرة | (المرحلة الثانية) |
| **F12** | التنبيهات الصحية | 🔴 متأخرة | (المرحلة الثانية) |
| **F13** | وضع Offline | 🟢 عالية | تصفح البيانات بدون إنترنت |

## 8.2 Modules

```
Ibb Hospitals System
├── Core Module (Foundation)
│   ├── Hospital Management
│   ├── Category/Taxonomy Management
│   ├── Location (GPS/District) Management
│   └── User/Role Management
├── Search Module
│   ├── Full-Text Search (Arabic)
│   ├── Filter (type, specialty, district, rating)
│   ├── Geo-Search (nearby hospitals)
│   └── Autocomplete
├── Review Module
│   ├── Rating System (1-5 stars)
│   ├── Text Reviews (moderated)
│   ├── Photo Upload
│   └── Response from Hospital
├── Analytics Module
│   ├── Dashboard
│   ├── Statistics
│   ├── Reports (PDF/Excel)
│   └── Data Export
├── Map Module
│   ├── OpenStreetMap / Leaflet
│   ├── Hospital Markers
│   ├── Clustering
│   └── Directions
└── API Module
    ├── REST Endpoints
    ├── JWT Auth
    ├── Rate Limiting
    └── API Documentation
```

## 8.3 Business Rules

| الرمز | القاعدة |
|-------|---------|
| BR01 | كل مستشفى يجب أن ينتمي إلى نوع (حكومي/خاص/أهلي/ميداني) |
| BR02 | يجب أن يحتوي المستشفى على اسم، عنوان، هاتف، إحداثيات GPS |
| BR03 | تصنيف وزارة الصحة (A-D) إجباري للمستشفيات الحكومية عند توفره |
| BR04 | التقييمات تتم بواسطة مستخدمين مسجلين فقط |
| BR05 | كل تقييم يخضع للمراجعة قبل النشر (معتدل) |
| BR06 | المستشفى يمكنه الرد على تقييم واحد لكل مراجعة |
| BR07 | المستشفيات الحكومية يتم التحقق منها بواسطة مكتب الصحة |
| BR08 | يتم تحديث البيانات كل 3 أشهر كحد أقصى |
| BR09 | يمكن للمستخدم الإبلاغ عن بيانات غير صحيحة |
| BR10 | الصور المرفوعة تخضع لمراجعة المحتوى |

## 8.4 CRUD Matrix

| الكيان | Create | Read | Update | Delete |
|--------|--------|------|--------|--------|
| Hospital | Admin | All | Admin/Manager | Admin |
| Category | Admin | All | Admin | Admin |
| SubCategory | Admin | All | Admin | Admin |
| District | Admin | All | Admin | Admin |
| User | Self | Self/Admin | Self/Admin | Admin |
| Doctor | Admin/Manager | All | Admin/Manager | Admin |
| Review | Registered User | All | Owner/Admin | Owner/Admin |
| Appointment | Registered | Owner | Owner | Owner/Admin |
| Report | Admin | Admin | - | - |

## 8.5 Permissions Matrix

| الدور | الصلاحيات |
|-------|----------|
| **Super Admin** | كل الصلاحيات (Full Access) |
| **Admin (مكتب الصحة)** | إدارة المستشفيات، التصنيفات، المستخدمين، التقارير |
| **Manager (مدير مستشفى)** | إدارة ملف مستشفاه، إضافة أطباء، الرد على التقييمات |
| **Doctor** | عرض ملفه، تحديث بياناته (محدود) |
| **User (مواطن)** | بحث، تصفح، تقييم، حجز مواعيد |
| **Guest** | بحث وتصفح فقط (بدون تقييم أو حجز) |

## 8.6 Business Workflow

### Workflow: إضافة مستشفى جديد

```
[مدخل البيانات (Admin)]
    ↓
[إدخال اسم، عنوان، هاتف، GPS، تخصصات]
    ↓
[اختيار النوع (حكومي/خاص)]
    ↓
[اختيار المديرية]
    ↓
[إضافة صور]
    ↓
[حفظ]
    ↓
[مراجعة البيانات (آلي + يدوي)]
    ↓
[نشر || رفض مع سبب]
    ↓
[إشعار لمكتب الصحة للمستشفيات الحكومية]
```

### Workflow: تقييم مستشفى

```
[مستخدم مسجل]
    ↓
[يدخل صفحة المستشفى]
    ↓
[يختار تقييم (1-5 نجوم)]
    ↓
[يكتب تعليق (اختياري)]
    ↓
[يرفع صورة (اختياري)]
    ↓
[إرسال]
    ↓
[مراجعة تلقائية (كلمات ممنوعة)]
    ↓
[مراجعة يدوية (خلال 24 ساعة)]
    ↓
[نشر || رفض]
    ↓
[إشعار للمستخدم + المستشفى]
```