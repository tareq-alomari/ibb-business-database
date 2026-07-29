# المرحلة الثامنة عشرة: SEO - قطاع المستشفيات في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 18_SEO.md

---

## 18.1 SEO Strategy

| الهدف | الاستراتيجية |
|-------|-------------|
| **الظهور في Google** | تحسين محركات البحث بالعربية |
| **البحث المحلي** | SEO جغرافي لمحافظة إب |
| **المحتوى** | صفحات غنية بالمعلومات عن المستشفيات |
| **التقني** | Next.js SSR + Schema.org |

## 18.2 Keywords

### Primary Keywords

| الكلمة | النوع | المنافسة |
|--------|-------|---------|
| مستشفيات إب | عامة | منخفضة |
| أفضل مستشفى في إب | عامة | منخفضة |
| مستشفى الثورة إب | علامة تجارية | متوسطة |
| مستشفى جبلة الجامعي | علامة تجارية | متوسطة |
| دليل المستشفيات إب | معلوماتية | منخفضة |

### Secondary Keywords

| الكلمة |
|--------|
| أرقام مستشفيات إب |
| طوارئ إب |
| أطباء إب |
| مستشفيات حكومية إب |
| مستشفيات خاصة إب |
| غسيل كلوي إب |
| مركز قلب إب |

### Long-tail Keywords

| الكلمة |
|--------|
| أقرب مستشفى من موقعي في إب |
| رقم مستشفى الثورة العام إب |
| أفضل دكتور أطفال في إب |
| مستشفى يعالج السرطان في إب |
| تكلفة العمليات في مستشفيات إب الخاصة |

## 18.3 Meta Tags (Template)

```html
<!-- لكل صفحة مستشفى -->
<title>مستشفى الثورة العام - إب | الموقع، أرقام الاتصال، التخصصات</title>
<meta name="description" content="مستشفى الثورة العام في إب: مستشفى حكومي رئيسي، يقدم خدمات طوارئ 24 ساعة، جراحة، قلب، غسيل كلوي. العنوان: مدينة إب. الهاتف: 04-XXX XXX">
<meta name="keywords" content="مستشفى الثورة, إب, مستشفى حكومي, طوارئ إب, مستشفيات إب">
```

## 18.4 Schema.org (JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "Hospital",
  "name": "هيئة مستشفى الثورة العام",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "إب",
    "addressRegion": "محافظة إب",
    "addressCountry": "YE"
  },
  "telephone": "04-XXX XXX",
  "url": "https://ibb-health.com/hospital/thawra",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.2",
    "reviewCount": "45"
  },
  "medicalSpecialty": [
    "Emergency",
    "Cardiology",
    "Surgery",
    "Nephrology"
  ],
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": "Monday-Sunday",
    "opens": "00:00",
    "closes": "23:59"
  }
}
```

## 18.5 Open Graph & Twitter Cards

```html
<!-- Open Graph -->
<meta property="og:title" content="مستشفى الثورة العام - إب" />
<meta property="og:description" content="مستشفى حكومي رئيسي في محافظة إب" />
<meta property="og:image" content="https://ibb-health.com/images/thawra.jpg" />
<meta property="og:url" content="https://ibb-health.com/hospital/thawra" />
<meta property="og:type" content="website" />
<meta property="og:locale" content="ar_YE" />

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="مستشفى الثورة العام - إب" />
<meta name="twitter:description" content="مستشفى حكومي رئيسي في محافظة إب" />
<meta name="twitter:image" content="https://ibb-health.com/images/thawra.jpg" />
```

## 18.6 Technical SEO

| العنصر | الإعداد |
|--------|---------|
| **Robots.txt** | السماح بفهرسة المحتوى العام، منع صفحات الإدارة |
| **Sitemap.xml** | ديناميكية، تحديث أسبوعي، تضم كل المستشفيات |
| **Canonical URLs** | لكل صفحة URL قياسي |
| **404 Page** | مخصصة مع روابط مفيدة |
| **301 Redirects** | للصفحات المحذوفة |
| **Pagination** | rel="next" / rel="prev" |
| **Breadcrumbs** | مسار تصفح هرمي |
| **SSL** | HTTPS إجباري |
| **Page Speed** | < 2 ثانية تحميل |
| **Mobile Friendly** | Responsive design |
| **Core Web Vitals** | LCP < 2.5s, FID < 100ms, CLS < 0.1 |

## 18.7 Local SEO

| الإجراء | الوصف |
|---------|-------|
| **Google Business Profile** | تسجيل المستشفيات على Google Maps |
| **Local Citations** | نشر البيانات في أدلة محلية |
| **خريطة الموقع** | Geo-targeting لمحافظة إب |
| **محتوى محلي** | صور ومحتوى من إب |
| **مراجعات** | تشجيع المستخدمين على ترك تقييمات |