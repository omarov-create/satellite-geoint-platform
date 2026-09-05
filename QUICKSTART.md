# منصة الأقمار الصناعية والاستخبارات
## God's Eye View - Satellite Geospatial Intelligence Platform

رابط المنصة 🛰️: **https://github.com/omarov-create/satellite-geoint-platform**

### 🚀 البدء السريع

```bash
# ربط المستودع
 git clone https://github.com/omarov-create/satellite-geoint-platform.git
cd satellite-geoint-platform

# تشغيل التطبيق
docker-compose up -d
```

### 🌍 الوصول إلى التطبيق

- **🌐 الواجهة الأمامية**: http://localhost:3000
- **📚 API Documentation**: http://localhost:8000/api/docs
- **📚 Redoc**: http://localhost:8000/api/redoc
- **🔋 PostgreSQL**: localhost:5432
- **🗐️ Redis**: localhost:6379

### 🛰️ الميزات الرئيسية

#### 1. 🌍 عرض عالمي 3D
- كرة أرضية صورية تفاعلية
- Deck.gl للتصور المتقدم
- CesiumJS للأرض الثلاثية

#### 2. 📡 الصور الحية
- Sentinel-1/2
- Landsat-8/9
- MODIS
- دقة عالية وذا علي زمن

#### 3. 🔍 استخبارات ذكية
- كشف التهديدات
- تحليل الكيانات
- كشف التغييرات
- مراقبة المنشآت

#### 4. ⚠️ نظام التنبيهات
- تنبيهات فورية
- WebSocket للتحديثات
- تقييم المخاطر
- توصيات

### 📄 مسارات API الرئيسية

```bash
# الأقمار الصناعية
GET  /api/v1/satellite/live-feed
GET  /api/v1/satellite/search
GET  /api/v1/satellite/available-satellites
GET  /api/v1/satellite/tile/{z}/{x}/{y}

# الاستخبارات
GET    /api/v1/intelligence/entities
GET    /api/v1/intelligence/alerts
GET    /api/v1/intelligence/threats
GET    /api/v1/intelligence/change-detection
GET    /api/v1/intelligence/facility/{id}
POST   /api/v1/intelligence/analyze
WS     /api/v1/intelligence/ws/live-alerts

# الصحة
GET  /api/v1/health/status
```

### 📚 الوثائق الكاملة

- 📃 [DEPLOYMENT.md](./DEPLOYMENT.md) - دليل النشر
- 📃 [README.md](./README.md) - معلومات عامة
- 📃 [requirements.txt](./requirements.txt) - متطلبات Python
- 📃 [docker-compose.yml](./docker-compose.yml) - البئة

### 🐧 البيئة التقنية

**Frontend:**
- React 18 + TypeScript
- Deck.gl + Mapbox GL JS + CesiumJS
- TailwindCSS
- Socket.io

**Backend:**
- FastAPI (Python)
- PostgreSQL + PostGIS
- Redis
- Celery

**Infrastructure:**
- Docker & Docker Compose
- AWS S3 + Lambda
- Nginx

### 👨‍💻 مساهمة

ترحب المشروع بالمساهمات! يرجى:
1. Fork المشروع
2. إنشاء branch جديد
3. إرسال Pull Request

### 📝 الترخيص

MIT License

---

**🌟 للحصول على أحدث المعلومات، زر المستودع:**  
🔗 https://github.com/omarov-create/satellite-geoint-platform
