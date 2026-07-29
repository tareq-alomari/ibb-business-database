# المرحلة الرابعة عشرة: API Design - قطاع الجامعات في محافظة إب

## 14.1 النقاط الرئيسية

| الطريقة | النقطة | الوصف |
|---------|--------|-------|
| GET | `/universities` | قائمة الجامعات |
| GET | `/universities/{id}` | تفاصيل جامعة |
| GET | `/universities/{id}/majors` | تخصصات جامعة |
| GET | `/majors` | قائمة التخصصات |
| GET | `/majors/{id}` | تفاصيل تخصص |
| GET | `/majors/compare?ids=1,2` | مقارنة تخصصات |
| POST | `/applications` | تقديم طلب |
| GET | `/applications/{id}` | متابعة طلب |
| GET | `/universities/{id}/reviews` | تقييمات |
| POST | `/universities/{id}/reviews` | إضافة تقييم |

## 14.2 مثال طلب

```
GET /api/v1/universities/1
{
  "id": 1,
  "name": "جامعة إب",
  "type": "government",
  "founded": 1996,
  "colleges": 15,
  "students": 25000,
  "rating": 4.2,
  "website": "www.ibbu.edu.ye"
}
```