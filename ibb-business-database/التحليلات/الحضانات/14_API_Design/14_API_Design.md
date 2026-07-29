# تصميم واجهات API - قطاع الحضانات في إب

## المعمارية
- RESTful API
- JSON format للبيانات
- JWT للمصادقة
- HTTPS للتشفير

## نقاط النهاية (Endpoints)

### المصادقة
| الطريقة | المسار | الوصف |
|--------|-------|-------|
| POST | /api/auth/register | تسجيل مستخدم جديد |
| POST | /api/auth/login | تسجيل الدخول |
| POST | /api/auth/logout | تسجيل الخروج |
| POST | /api/auth/reset-password | إعادة تعيين كلمة المرور |

### الحضانات
| الطريقة | المسار | الوصف |
|--------|-------|-------|
| GET | /api/nurseries | قائمة الحضانات (مع فلترة) |
| GET | /api/nurseries/:id | تفاصيل حضانة محددة |
| POST | /api/nurseries | إضافة حضانة جديدة |
| PUT | /api/nurseries/:id | تحديث بيانات حضانة |
| DELETE | /api/nurseries/:id | حذف حضانة |

### الأطفال
| الطريقة | المسار | الوصف |
|--------|-------|-------|
| GET | /api/children | قائمة الأطفال |
| POST | /api/children | تسجيل طفل جديد |
| PUT | /api/children/:id | تحديث بيانات طفل |
| GET | /api/children/:id/attendance | سجل حضور طفل |

### المدفوعات
| الطريقة | المسار | الوصف |
|--------|-------|-------|
| GET | /api/payments | سجل المدفوعات |
| POST | /api/payments | تسجيل دفعة جديدة |
| GET | /api/payments/invoices | الفواتير |
| POST | /api/payments/remind | إرسال تذكير بالدفع |

### التقييمات
| الطريقة | المسار | الوصف |
|--------|-------|-------|
| GET | /api/reviews | قائمة التقييمات |
| POST | /api/reviews | إضافة تقييم |
| GET | /api/reviews/stats | إحصائيات التقييمات |

### التقارير
| الطريقة | المسار | الوصف |
|--------|-------|-------|
| GET | /api/reports/dashboard | بيانات لوحة التحكم |
| GET | /api/reports/occupancy | تقارير الإشغال |
| GET | /api/reports/revenue | تقارير الإيرادات |
| GET | /api/reports/export/:format | تصدير تقارير (PDF/Excel) |

## أخطاء API
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 422 Validation Error
- 500 Internal Server Error
