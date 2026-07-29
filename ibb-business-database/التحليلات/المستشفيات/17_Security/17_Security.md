# المرحلة السابعة عشرة: Security - قطاع المستشفيات في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 17_Security.md

---

## 17.1 OWASP Top 10 Mitigations

| الرقم | الثغرة | الإجراء الوقائي |
|-------|--------|----------------|
| **A01** | Broken Access Control | RBAC + JWT + صلاحيات لكل endpoint |
| **A02** | Cryptographic Failures | HTTPS إجباري، bcrypt لكلمات المرور |
| **A03** | Injection | Prisma ORM = parameterized queries تلقائيًا |
| **A04** | Insecure Design | Zod validation، Rate limiting، Input sanitization |
| **A05** | Security Misconfiguration | إعدادات أمان افتراضية، إخفاء معلومات الإصدار |
| **A06** | Vulnerable Components | تحديث دوري للـ dependencies، Dependabot |
| **A07** | Auth Failures | JWT مع expiry، OTP للعمليات الحساسة |
| **A08** | Data Integrity Failures | CSRF tokens، SameSite cookies |
| **A09** | Logging Failures | تسجيل كل العمليات الحساسة |
| **A10** | SSRF | قيود على الطلبات الخارجية |

## 17.2 Authentication

### التدفق

```
[تسجيل الدخول]
    ↓
[إدخال البريد + كلمة المرور]
    ↓
[تحقق من البيانات]
    ↓
[إصدار Access Token (JWT - 24 ساعة)]
    ↓
[إصدار Refresh Token (7 أيام)]
    ↓
[تخزين: Access → LocalStorage, Refresh → HttpOnly Cookie]
```

### OTP (للمستخدمين الجدد)

```
[تسجيل مستخدم جديد]
    ↓
[إرسال OTP إلى البريد/الهاتف]
    ↓
[إدخال OTP]
    ↓
[تفعيل الحساب]
```

## 17.3 Authorization - RBAC

| الدور | مستوى الوصول |
|-------|-------------|
| **super_admin** | كل شيء |
| **admin** | إدارة المحتوى، المستخدمين، التقارير |
| **manager** | إدارة مستشفاه فقط |
| **user** | بحث، تقييم، حجز |
| **guest** | بحث فقط (بدون تقييم) |

## 17.4 Encryption

| الطبقة | التقنية |
|--------|---------|
| **In Transit** | TLS 1.3 (HTTPS) |
| **At Rest (DB)** | AES-256 (Transparent Data Encryption) |
| **Passwords** | bcrypt (cost factor: 12) |
| **JWT** | HS256 (مع سر قوي) |
| **API Keys** | مخزنة في Environment Variables |
| **Images** | تشفير أثناء النقل (HTTPS) |

## 17.5 HTTP Security Headers

| الهيدر | القيمة |
|--------|--------|
| `Content-Security-Policy` | default-src 'self'; img-src 'self' https:; script-src 'self' |
| `Strict-Transport-Security` | max-age=31536000; includeSubDomains |
| `X-Content-Type-Options` | nosniff |
| `X-Frame-Options` | DENY |
| `X-XSS-Protection` | 1; mode=block |
| `Referrer-Policy` | strict-origin-when-cross-origin |
| `Permissions-Policy` | geolocation=(self), camera=(), microphone=() |

## 17.6 Rate Limiting

| النوع | الحد | النافذة |
|-------|------|---------|
| Public API | 100 req | دقيقة واحدة |
| Authenticated API | 500 req | دقيقة واحدة |
| Login attempts | 5 مرات | 15 دقيقة |
| Review creation | 10 مرات | ساعة واحدة |
| Appointment booking | 5 مرات | ساعة واحدة |

## 17.7 Data Privacy

| الإجراء | الوصف |
|---------|-------|
| **سياسة الخصوصية** | صفحة واضحة عن جمع واستخدام البيانات |
| **الحد الأدنى من البيانات** | جمع فقط البيانات الضرورية |
| **حق الحذف** | المستخدم يمكنه حذف حسابه وبياناته |
| **تشفير البيانات الشخصية** | البيانات الحساسة مشفرة في قاعدة البيانات |
| **عدم مشاركة البيانات** | لا تشارك بيانات المستخدمين مع أطراف ثالثة |

## 17.8 Audit Logging

| الحدث | مسجل | مدة الاحتفاظ |
|-------|------|-------------|
| تسجيل الدخول/الخروج | ✅ | 12 شهر |
| إضافة/تعديل مستشفى | ✅ | دائم |
| حذف مستشفى | ✅ | دائم |
| إضافة تقييم | ✅ | 12 شهر |
| تغيير الصلاحيات | ✅ | دائم |
| محاولات فاشلة | ✅ | 6 شهر |
| عمليات API | ✅ | 3 شهر |

## 17.9 Backup & Recovery

| النوع | الجدول | مكان التخزين |
|-------|--------|-------------|
| نسخة يومية (DB) | كل 24 ساعة | DigitalOcean Spaces |
| نسخة أسبوعية (DB + Images) | كل أحد | S3 (منطقة مختلفة) |
| نسخة شهرية (Full) | أول كل شهر | تخزين بارد |

### Recovery Plan

```
1. اكتشاف العطل ← 5 دقائق
2. إيقاف التطبيق ← دقيقة
3. استعادة آخر نسخة ← 30 دقيقة
4. التحقق من البيانات ← 15 دقيقة
5. تشغيل التطبيق ← 5 دقيقة
───
الإجمالي: ~60 دقيقة (RTO)
```