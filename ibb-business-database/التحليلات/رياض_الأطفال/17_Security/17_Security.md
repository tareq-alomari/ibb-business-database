# الأمان: منصة رياض الأطفال في إب

> **تاريخ التحليل**: يوليو 2026

---

## OWASP Top 10 – الإجراءات الوقائية

| الثغرة | الإجراء الوقائي |
|--------|----------------|
| Broken Access Control | RBAC + JWT مع صلاحيات محددة |
| Cryptographic Failures | HTTPS إجباري، bcrypt لكلمات المرور |
| Injection | Parameterized Queries، تعقيم المدخلات |
| Insecure Design | Rate Limiting، Zod Validation |
| Security Misconfiguration | إعدادات افتراضية آمنة |
| XSS | Content-Security-Policy |
| CSRF | CSRF Tokens + SameSite Cookies |
| API Security | Rate Limit (50 req/min) |

## تدفق المصادقة

```
[تسجيل الدخول]
    ↓
[إدخال رقم الهاتف + كلمة المرور]
    ↓
[التحقق من البيانات]
    ↓
[إصدار JWT Token (24 ساعة)]
    ↓
[Refresh Token (7 أيام)]
    ↓
[تخزين آمن في HttpOnly Cookie]
```

## حماية البيانات

| الإجراء | الوصف |
|---------|-------|
| Encryption in Transit | TLS 1.3 |
| Password Hashing | bcrypt (cost: 12) |
| API Keys | Environment Variables |
| Session Management | Redis + HttpOnly Cookies |
| Rate Limiting | 50 طلب/دقيقة للمستخدم العادي |
| Input Validation | Zod schemas لجميع المدخلات |
| Logging | تسجيل جميع العمليات الحساسة |

## صلاحيات المستخدمين

| الدور | الصلاحيات |
|-------|-----------|
| Super Admin | كل الصلاحيات |
| Admin | إدارة الرياض، المستخدمين، التقييمات |
| Owner (صاحب روضة) | إدارة ملف روضته، الرد على التقييمات |
| User (ولي أمر) | بحث، تصفح، تقييم |
| Guest | بحث وتصفح فقط |
