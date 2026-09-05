"""Intelligence API Routes - مسارات API الاستخبارات"""

from fastapi import APIRouter, HTTPException, Query, Depends, WebSocket
from typing import List, Optional
from datetime import datetime
from app.services.intelligence_service import IntelligenceService

router = APIRouter()
intelligence_service = IntelligenceService()


@router.get("/entities")
async def get_entities(
    entity_type: Optional[str] = Query(None, description="ship, aircraft, facility"),
    threat_level: Optional[str] = Query(None),
    bbox: Optional[str] = Query(None, description="Bounding box: minx,miny,maxx,maxy")
):
    """
    الحصول على الكيانات المكتشفة - Get detected entities
    
    - **entity_type**: نوع الكيان (سفن، طائرات، منشآت)
    - **threat_level**: مستوى التهديد
    - **bbox**: منطقة الاهتمام
    """
    try:
        entities = await intelligence_service.get_entities(
            entity_type=entity_type,
            threat_level=threat_level,
            bbox=bbox
        )
        return {
            "status": "success",
            "count": len(entities),
            "entities": entities
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/alerts")
async def get_intelligence_alerts(
    status: Optional[str] = Query("active"),
    threat_level: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=500)
):
    """
    الحصول على التنبيهات الاستخباراتية - Get intelligence alerts
    
    - **status**: حالة التنبيه (active, resolved, dismissed)
    - **threat_level**: مستوى التهديد
    - **limit**: عدد النتائج
    """
    try:
        alerts = await intelligence_service.get_alerts(
            status=status,
            threat_level=threat_level,
            limit=limit
        )
        return {
            "status": "success",
            "count": len(alerts),
            "alerts": alerts
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/threats")
async def get_threats(
    bbox: Optional[str] = Query(None),
    threat_level: Optional[str] = Query(None)
):
    """
    الحصول على التهديدات الحالية - Get current threats
    """
    try:
        threats = await intelligence_service.get_threats(
            bbox=bbox,
            threat_level=threat_level
        )
        return {
            "status": "success",
            "timestamp": datetime.utcnow(),
            "threats": threats
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.websocket("/ws/live-alerts")
async def websocket_live_alerts(websocket: WebSocket):
    """
    WebSocket للتنبيهات المباشرة - Live alerts WebSocket
    """
    await websocket.accept()
    try:
        await intelligence_service.stream_alerts(websocket)
    except Exception as e:
        await websocket.close(code=1000)


@router.get("/change-detection")
async def detect_changes(
    imagery_id_before: str,
    imagery_id_after: str,
    geometry: Optional[str] = Query(None, description="GeoJSON polygon")
):
    """
    كشف التغييرات بين صورتين - Detect changes between two images
    
    - **imagery_id_before**: معرّف الصورة الأولى
    - **imagery_id_after**: معرّف الصورة الثانية
    - **geometry**: المنطقة المهتمة بها (GeoJSON)
    """
    try:
        changes = await intelligence_service.detect_changes(
            before_id=imagery_id_before,
            after_id=imagery_id_after,
            geometry=geometry
        )
        return {
            "status": "success",
            "changes": changes
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/facility/{facility_id}")
async def get_facility_intelligence(facility_id: str):
    """
    الحصول على معلومات استخباراتية عن منشأة - Get facility intelligence
    
    - **facility_id**: معرّف المنشأة
    """
    try:
        intel = await intelligence_service.get_facility_intelligence(facility_id)
        return {
            "status": "success",
            "intelligence": intel
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyze")
async def analyze_location(
    latitude: float,
    longitude: float,
    radius_km: float = Query(5, ge=1, le=100),
    analysis_type: Optional[str] = Query("full")
):
    """
    تحليل موقع معين - Analyze a specific location
    
    - **latitude**: خط العرض
    - **longitude**: خط الطول
    - **radius_km**: نطاق التحليل
    - **analysis_type**: نوع التحليل (full, quick, deep)
    """
    try:
        analysis = await intelligence_service.analyze_location(
            lat=latitude,
            lon=longitude,
            radius=radius_km,
            analysis_type=analysis_type
        )
        return {
            "status": "success",
            "analysis": analysis
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
