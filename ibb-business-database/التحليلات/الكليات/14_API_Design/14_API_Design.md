# تصميم API - منصة الكليات في إب

## النمط
- **RESTful API** مع JSON.
- قاعدة URL: `/api/v1/`
- توثيق باستخدام OpenAPI/Swagger.

## نقاط النهاية (Endpoints)

### الجامعات
| الطريقة | المسار | الوصف |
|--------|-------|-------|
| GET | /universities | قائمة الجامعات |
| GET | /universities/:id | تفاصيل جامعة |
| POST | /universities | إضافة جامعة (مشرف) |
| PUT | /universities/:id | تحديث جامعة |
| DELETE | /universities/:id | حذف جامعة |

### الكليات
| الطريقة | المسار | الوصف |
|--------|-------|-------|
| GET | /colleges | قائمة الكليات (مع فلاتر) |
| GET | /colleges/:id | تفاصيل كلية |
| GET | /colleges/:id/majors | تخصصات كلية |
| GET | /colleges/:id/reviews | تقييمات كلية |
| POST | /colleges | إضافة كلية |
| PUT | /colleges/:id | تحديث بيانات كلية |
| DELETE | /colleges/:id | حذف كلية |

### التخصصات
| الطريقة | المسار | الوصف |
|--------|-------|-------|
| GET | /majors | قائمة التخصصات |
| GET | /majors/:id | تفاصيل تخصص |
| POST | /majors | إضافة تخصص |
| PUT | /majors/:id | تحديث تخصص |

### المستخدمون
| الطريقة | المسار | الوصف |
|--------|-------|-------|
| POST | /auth/register | تسجيل مستخدم |
| POST | /auth/login | تسجيل الدخول |
| GET | /users/me | الملف الشخصي |
| PUT | /users/me | تحديث الملف |

### التقييمات
| الطريقة | المسار | الوصف |
|--------|-------|-------|
| GET | /reviews?college_id=X | قائمة تقييمات كلية |
| POST | /reviews | إضافة تقييم |
| PUT | /reviews/:id | تعديل تقييم |
| DELETE | /reviews/:id | حذف تقييم |

## الفلاتر والبحث
- GET /colleges?university_id=X&category=medical&fees_max=500000&sort=rating
- GET /colleges?search=طب&page=1&limit=20

## الاستجابة (Response)
```json
{
  "success": true,
  "data": { ... },
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 150
  }
}
```

## المصادقة
- JWT (JSON Web Tokens) مع صلاحية 24 ساعة.
- Bearer Token في رأس الطلب: `Authorization: Bearer <token>`
