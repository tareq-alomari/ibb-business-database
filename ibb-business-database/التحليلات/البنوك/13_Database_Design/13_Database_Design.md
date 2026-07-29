# تصميم قاعدة البيانات: النظام المصرفي في إب

## هيكل قاعدة البيانات

### جدول العملاء (Customers)
- customer_id (PK)
- full_name, national_id, phone, email
- address (city, district, street)
- date_of_birth, occupation
- registration_date, branch_id (FK)

### جدول الحسابات (Accounts)
- account_id (PK)
- customer_id (FK)
- account_type (جاري، توفير، استثماري)
- currency (YER, USD, SAR)
- balance, status
- open_date, closed_date

### جدول المعاملات (Transactions)
- transaction_id (PK)
- account_id (FK)
- transaction_type (إيداع، سحب، تحويل)
- amount, currency
- transaction_date, description
- reference_number, branch_id (FK)

### جدول الفروع (Branches)
- branch_id (PK)
- branch_name
- address, phone
- manager_id (FK)
- opening_hours, status

### جدول التمويلات (Loans)
- loan_id (PK)
- customer_id (FK)
- loan_type (شخصي، زراعي، تجاري)
- amount, interest_rate (أو هامش ربح)
- start_date, end_date
- installment_amount, status

### جدول القيود اليومية (DailyLimits)
- limit_id (PK)
- account_type, transaction_type
- max_amount_per_day
- max_amount_per_transaction

## العلاقات
- عميل ← حسابات (واحد لعدة)
- حساب ← معاملات (واحد لعدة)
- فرع ← حسابات (واحد لعدة)
- عميل ← تمويلات (واحد لعدة)

## اعتبارات الأمان
- تشفير بيانات العملاء الحساسة
- فصل البيانات المالية عن الشخصية
- سجل تدقيق لكل عملية (Audit Log)
- نسخ احتياطي مشفر يومياً
