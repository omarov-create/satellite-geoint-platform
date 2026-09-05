"""Satellite API Routes - مسارات API الأقمار الصناعية"""

from fastapi import APIRouter, HTTPException, Query, Depends
from typing import List, Optional
from datetime import datetime, timedelta
from app.services.satellite_service import SatelliteService
from app.models.satellite import SatelliteType

router = APIRouter()
satellite_service = SatelliteService()


@router.get("/live-feed")
async def get_live_satellite_feed(
    bbox: Optional[str] = Query(None, description="Bounding box: minx,miny,maxx,maxy"),
    satellite_type: Optional[str] = Query(None),
    max_cloud_coverage: float = Query(100.0)
):
    """
    الحصول على بيانات الأقمار الحية - Get live satellite feeds
    
    - **bbox**: منطقة الاهتمام (خطوط الطول والعرض)
    - **satellite_type**: نوع القمر الصناعي
    - **max_cloud_coverage**: أقصى تغطية غيوم (0-100%)
    """
    try:
        feed = await satellite_service.get_live_feed(
            bbox=bbox,
            satellite_type=satellite_type,
            max_cloud_coverage=max_cloud_coverage
        )
        return {
            "status": "success",
            "timestamp": datetime.utcnow(),
            "feed": feed
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/search")
async def search_imagery(
    latitude: float,
    longitude: float,
    radius_km: float = Query(10, description="Search radius in km"),
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    max_cloud_coverage: float = Query(30.0)
):
    """
    البحث عن صور الأقمار - Search for satellite imagery
    
    - **latitude**: خط العرض
    - **longitude**: خط الطول
    - **radius_km**: نطاق البحث بالكيلومتر
    - **start_date**: تاريخ البداية (YYYY-MM-DD)
    - **end_date**: تاريخ النهاية (YYYY-MM-DD)
    """
    try:
        results = await satellite_service.search_imagery(
            lat=latitude,
            lon=longitude,
            radius=radius_km,
            start_date=start_date,
            end_date=end_date,
            cloud_coverage=max_cloud_coverage
        )
        return {
            "status": "success",
            "count": len(results),
            "results": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/available-satellites")
async def get_available_satellites():
    """
    الحصول على قائمة الأقمار الصناعية المتاحة - Get available satellites
    """
    return {
        "status": "success",
        "satellites": [
            {
                "name": "Sentinel-1",
                "type": "SAR (Synthetic Aperture Radar)",
                "resolution": "5-20m",
                "frequency": "Every 12 days",
                "data_type": "radar"
            },
            {
                "name": "Sentinel-2",
                "type": "Multispectral Optical",
                "resolution": "10m",
                "frequency": "Every 5 days",
                "data_type": "optical"
            },
            {
                "name": "Landsat-8",
                "type": "Multispectral Optical",
                "resolution": "30m",
                "frequency": "Every 16 days",
                "data_type": "optical"
            },
            {
                "name": "MODIS",
                "type": "Multispectral",
                "resolution": "250-1000m",
                "frequency": "Daily",
                "data_type": "optical"
            }
        ]
    }


@router.get("/tile/{z}/{x}/{y}")
async def get_tile(
    z: int,
    x: int,
    y: int,
    imagery_id: Optional[str] = Query(None)
):
    """
    الحصول على تايل الخريطة - Get map tile
    
    - **z**: مستوى التكبير
    - **x**: إحداثي X
    - **y**: إحداثي Y
    - **imagery_id**: معرّف الصورة
    """
    try:
        tile = await satellite_service.get_tile(z, x, y, imagery_id)
        return tile
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
