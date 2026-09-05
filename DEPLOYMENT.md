"""Production Deployment Guide"""

# 🚀 منصة الأقمار الصناعية والاستخبارات الجيوسبيتشة
## God's Eye View - Advanced Satellite Intelligence Platform

### الميزات الرئيسية ✨

1. **🌍 عرض عالمي ثلاثي الأبعاد**
   - كرة أرضية تفاعلية بدقة عالية
   - تصور بيانات الأقمار الصناعية الحية
   - تتبع الكيانات في الوقت الفعلي

2. **📡 صور الأقمار الصناعية الحديثة**
   - Sentinel-1/2 بدقة عالية
   - Landsat-8/9
   - MODIS (بيانات يومية)
   - دعم السلاسل الزمنية

3. **🔍 استخبارات جيوسبيتشة متقدمة**
   - كشف التهديدات الحالية
   - تحليل الكيانات (سفن، طائرات، منشآت)
   - كشف التغييرات بين الصور
   - تتبع الحركة والنشاط

4. **⚠️ نظام التنبيهات الذكي**
   - تنبيهات فورية عن الأنشطة المريبة
   - تقييم التهديدات الآلي
   - توصيات تحليلية
   - WebSocket للتحديثات المباشرة

5. **🎯 أدوات التحليل**
   - تحليل الموقع الشامل
   - إحصائيات وتقارير
   - مقارنة الصور (Before/After)
   - تحليل السلاسل الزمنية

### البنية التقنية 🏗️

**Frontend:**
- React 18 + TypeScript
- Deck.gl (التصور المتقدم)
- Mapbox GL JS (الخرائط التفاعلية)
- CesiumJS (3D الأرض)
- TailwindCSS (التصميم)

**Backend:**
- FastAPI (Python)
- PostgreSQL + PostGIS (قاعدة البيانات الجغرافية)
- Redis (التخزين المؤقت)
- Celery (معالجة المهام)

**خدمات البيانات:**
- Sentinel Hub API
- Google Earth Engine
- OpenWeather API
- AIS/Flight Tracking APIs

**البنية التحتية:**
- Docker & Kubernetes
- AWS S3 (تخزين الصور)
- AWS Lambda (معالجة سريعة)
- Nginx (بوابة عكسية)

### الإعدادات السريعة 🚀

#### 1. متطلبات النظام
```bash
Docker >= 20.10
Docker Compose >= 2.0
Node.js >= 16
Python >= 3.10
```

#### 2. إعداد المتغيرات البيئية
```bash
cp .env.example .env
# ملء المتغيرات:
# - SENTINELHUB_CLIENT_ID
# - SENTINELHUB_CLIENT_SECRET
# - GOOGLE_APPLICATION_CREDENTIALS
# - MAPBOX_ACCESS_TOKEN
# - AWS_ACCESS_KEY_ID
# - AWS_SECRET_ACCESS_KEY
```

#### 3. تشغيل التطبيق
```bash
# Start services
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f backend
```

#### 4. الوصول إلى التطبيق
- **الواجهة الأمامية**: http://localhost:3000
- **API Documentation**: http://localhost:8000/api/docs
- **PostGIS Database**: localhost:5432
- **Redis Cache**: localhost:6379

### المسارات الرئيسية للـ API 📍

#### الأقمار الصناعية
```
GET  /api/v1/satellite/live-feed         - البيانات الحية
GET  /api/v1/satellite/search            - البحث عن الصور
GET  /api/v1/satellite/available-satellites - الأقمار المتاحة
GET  /api/v1/satellite/tile/{z}/{x}/{y}  - تايلات الخريطة
```

#### الاستخبارات
```
GET    /api/v1/intelligence/entities      - الكيانات المكتشفة
GET    /api/v1/intelligence/alerts        - التنبيهات
GET    /api/v1/intelligence/threats       - التهديدات الحالية
GET    /api/v1/intelligence/change-detection - كشف التغييرات
GET    /api/v1/intelligence/facility/{id} - معلومات المنشأة
POST   /api/v1/intelligence/analyze       - تحليل الموقع
WS     /api/v1/intelligence/ws/live-alerts - بث التنبيهات المباشرة
```

#### الصحة والحالة
```
GET  /api/v1/health/status               - حالة الخدمات
```

### أمثلة الاستخدام 💡

#### البحث عن صور حول موقع معين
```bash
curl -X GET "http://localhost:8000/api/v1/satellite/search?latitude=35.12&longitude=51.56&radius_km=20&max_cloud_coverage=30"
```

#### الحصول على الكيانات المكتشفة
```bash
curl -X GET "http://localhost:8000/api/v1/intelligence/entities?entity_type=ship&threat_level=high"
```

#### تحليل موقع
```bash
curl -X POST "http://localhost:8000/api/v1/intelligence/analyze?latitude=37.77&longitude=-122.41&radius_km=5&analysis_type=full"
```

#### كشف التغييرات
```bash
curl -X GET "http://localhost:8000/api/v1/intelligence/change-detection?imagery_id_before=img_001&imagery_id_after=img_002"
```

### التطوير والمساهمة 👨‍💻

#### إعداد بيئة التطوير
```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend
cd frontend
npm install
npm run dev
```

#### إجراء الاختبارات
```bash
# Backend tests
pytest backend/tests -v

# Frontend tests
cd frontend && npm test
```

### المراقبة والسجلات 📊

#### عرض السجلات
```bash
docker-compose logs -f backend
docker-compose logs -f postgres
```

#### مراقبة الأداء
```bash
# CPU/Memory usage
docker stats

# Database queries
# Connect to PostgreSQL and run EXPLAIN ANALYZE
```

### استكشاف الأخطاء 🔧

#### اتصال قاعدة البيانات
```bash
# Check if PostgreSQL is running
docker-compose ps postgres

# Test connection
psql -h localhost -U geoint_user -d satellite_geoint
```

#### مشاكل Redis
```bash
# Check Redis status
redis-cli ping

# Clear cache if needed
redis-cli FLUSHALL
```

#### مشاكل API
```bash
# Check API health
curl http://localhost:8000/api/v1/health/status

# View detailed logs
docker-compose logs backend | grep ERROR
```

### النشر في الإنتاج 🌐

#### على AWS
```bash
# Push to ECR
aws ecr get-login-password | docker login --username AWS --password-stdin [account].dkr.ecr.[region].amazonaws.com
docker tag satellite-geoint-platform:latest [account].dkr.ecr.[region].amazonaws.com/satellite-geoint:latest
docker push [account].dkr.ecr.[region].amazonaws.com/satellite-geoint:latest

# Deploy with ECS or EKS
```

#### على Kubernetes
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
```

### الدعم والمساعدة 🆘

- 📚 [التوثيق الكاملة](./docs/README.md)
- 🐛 [تقرير الأخطاء](https://github.com/omarov-create/satellite-geoint-platform/issues)
- 💬 [النقاشات](https://github.com/omarov-create/satellite-geoint-platform/discussions)

### الترخيص 📜

MIT License - انظر [LICENSE](./LICENSE) للتفاصيل

---

**تم البناء بواسطة:** Geospatial Intelligence Team  
**الإصدار:** 1.0.0 Beta  
**آخر تحديث:** 2026-09-05
