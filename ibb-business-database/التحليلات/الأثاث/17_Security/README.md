# الأمان - قطاع الأثاث في محافظة إب

---

## OWASP Top 10 - الإجراءات الوقائية

| الثغرة | الإجراء الوقائي |
|--------|----------------|
| **Broken Access Control** | RBAC + JWT مع صلاحيات لكل دور |
| **Cryptographic Failures** | HTTPS إجباري، تشفير كلمات المرور (bcrypt) |
| **Injection** | Parameterized Queries عبر Prisma |
| **Insecure Design** | Rate Limiting، التحقق من المدخلات (Zod) |
| **Security Misconfiguration** | إعدادات أمان افتراضية |
| **XSS** | Content-Security-Policy |
| **CSRF** | CSRF Tokens، SameSite Cookies |

## تدفق المصادقة

```
[تسجيل الدخول]
    ↓
[إدخال الهاتف + كلمة المرور]
    ↓
[التحقق من البيانات]
    ↓
[إصدار JWT Token (مدة: 24 ساعة)]
    ↓
[Refresh Token (مدة: 7 أيام)]
    ↓
[تخزين آمن في HttpOnly Cookie]
```

## حماية البيانات

| الإجراء | الوصف |
|---------|-------|
| Encryption at Rest | تشفير قاعدة البيانات (AES-256) |
| Encryption in Transit | TLS 1.3 |
| Password Hashing | bcrypt (cost: 12) |
| API Keys | Environment Variables |
| Session Management | JWT + Redis |

## صلاحيات المستخدمين

| الدور | الصلاحيات |
|-------|-----------|
| **Super Admin** | كل الصلاحيات |
| **Admin** | إدارة المعارض، المنتجات، المستخدمين |
| **Business Owner** | إدارة معرضه ومنتجاته |
| **User** | بحث، تصفح، تقييم |
| **Guest** | بحث وتصفح فقط |

## حماية API

- Rate Limiting: 100 طلب/دقيقة للمستخدمين العاديين
- API Keys للتطبيقات الخارجية
- التحقق من صحة جميع المدخلات
- تسجيل جميع العمليات الحساسة
