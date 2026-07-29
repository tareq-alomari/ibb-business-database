# تصميم واجهات API - قطاع العصائر في إب

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

### المحلات
| الطريقة | المسار | الوصف |
|--------|-------|-------|
| GET | /api/shops | قائمة المحلات (مع فلترة) |
| GET | /api/shops/:id | تفاصيل محل + قائمته |
| POST | /api/shops | إضافة محل جديد |
| PUT | /api/shops/:id | تحديث بيانات محل |
| GET | /api/shops/:id/products | منتجات محل معين |

### المنتجات
| الطريقة | المسار | الوصف |
|--------|-------|-------|
| GET | /api/products | قائمة المنتجات |
| GET | /api/products/:id | تفاصيل منتج |
| POST | /api/products | إضافة منتج |
| PUT | /api/products/:id | تحديث منتج |
| DELETE | /api/products/:id | حذف منتج |

### الطلبات
| الطريقة | المسار | الوصف |
|--------|-------|-------|
| POST | /api/orders | إنشاء طلب جديد |
| GET | /api/orders | سجل طلبات المستخدم |
| GET | /api/orders/:id | تفاصيل طلب |
| PUT | /api/orders/:id/status | تحديث حالة الطلب |
| GET | /api/orders/track/:id | تتبع الطلب |

### التقييمات
| الطريقة | المسار | الوصف |
|--------|-------|-------|
| GET | /api/reviews | قائمة التقييمات |
| POST | /api/reviews | إضافة تقييم |
| GET | /api/reviews/stats | إحصائيات التقييمات |

### المدفوعات
| الطريقة | المسار | الوصف |
|--------|-------|-------|
| POST | /api/payments | معالجة دفعة |
| GET | /api/payments/history | سجل المدفوعات |

## أخطاء API
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 422 Validation Error
- 500 Internal Server Error
