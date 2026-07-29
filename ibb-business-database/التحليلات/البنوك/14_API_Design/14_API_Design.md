# تصميم واجهات API: النظام المصرفي في إب

## نظرة عامة
تصميم واجهات برمجية للربط بين التطبيقات المصرفية والأنظمة الداخلية للبنوك العاملة في محافظة إب.

## نقاط النهاية الرئيسية

### المصادقة (Authentication)
- POST /api/auth/login
- POST /api/auth/verify-otp
- POST /api/auth/logout
- POST /api/auth/refresh-token

### العملاء (Customers)
- GET /api/customers
- GET /api/customers/{id}
- POST /api/customers
- PUT /api/customers/{id}
- GET /api/customers/{id}/accounts

### الحسابات (Accounts)
- GET /api/accounts/{id}
- GET /api/accounts/{id}/transactions
- GET /api/accounts/{id}/balance
- POST /api/accounts

### المعاملات (Transactions)
- POST /api/transactions/transfer
- POST /api/transactions/deposit
- POST /api/transactions/withdraw
- GET /api/transactions/{id}
- GET /api/transactions/history?from=date&to=date

### التمويلات (Loans)
- POST /api/loans/apply
- GET /api/loans/{id}
- GET /api/loans/{id}/schedule
- POST /api/loans/{id}/pay

### الخدمات المصرفية (Banking)
- GET /api/branches
- GET /api/branches/{id}/atms
- GET /api/exchange-rates
- POST /api/inquiry (الاستعلام عن رقم حساب)

## معايير الأمان للـ API
- جميع النقاط محمية بـ HTTPS
- استخدام JWT للمصادقة
- تحديد معدل الطلبات (Rate Limiting)
- تسجيل جميع الطلبات في سجل التدقيق
- تشفير البيانات الحساسة في الاستجابات

## توثيق API
- استخدام OpenAPI 3.0 لتوثيق الواجهات
- توفير بيئة اختبار (Sandbox) للمطورين
- أمثلة باللغة العربية لاستخدام API
