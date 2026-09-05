"""Admin Routes - مسارات الإدارة"""

from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/stats")
async def get_system_stats():
    return {
        "status": "healthy",
        "uptime": "24h 30m",
        "active_users": 42,
        "processed_images": 1250,
        "alerts_active": 8,
        "timestamp": datetime.utcnow()
    }
