# المرحلة الرابعة عشرة: 14_API_Design - قطاع الورش الصناعية في محافظة إب

> **التاريخ**: يوليو 2026  
> **الملف**: 14_API_Design.md

---

## 14.1 نظرة عامة
API RESTful لخدمات قطاع الورش الصناعية في محافظة إب.
```
Base URL: https://api.ibb-guide.com/v1
Content-Type: application/json
Auth: Bearer JWT
```

## 14.2 النقاط النهائية
### المصادقة
| POST | /auth/register | تسجيل |
| POST | /auth/login | دخول |
| POST | /auth/refresh | تجديد التوكن |

### مقدمي الخدمة
| GET | /providers | قائمة |
| GET | /providers/:id | تفاصيل |
| POST | /providers | إضافة |
| PUT | /providers/:id | تحديث |

### الحجوزات
| GET | /bookings | قائمة |
| POST | /bookings | إنشاء |
| PUT | /bookings/:id | تحديث الحالة |
| DELETE | /bookings/:id | إلغاء |

### التقييمات
| GET | /reviews/:providerId | قائمة تقييمات |
| POST | /reviews | إضافة تقييم |

### البحث
| GET | /search?q=&category=&area=&min_price=&max_price= | بحث متقدم |

## 14.3 رموز الحالة
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 500 | Server Error |

---
## المصادر
1. الجهاز المركزي للإحصاء اليمني - إحصائيات السكان 2024
2. غرفة تجارة وصناعة محافظة إب - تقارير القطاع التجاري
3. مسح ميداني تقديري
4. مقابلات محلية مع مقدمي الخدمة والمستفيدين في إب
