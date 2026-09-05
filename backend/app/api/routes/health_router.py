"""Health Check Routes - مسارات فحص الصحة"""

from fastapi import APIRouter, HTTPException
from datetime import datetime
from app.core.cache import redis_client
from app.core.database import engine

router = APIRouter()


@router.get("/status")
async def health_status():
    """
    فحص صحة التطبيق - Application health check
    """
    status = {
        "status": "online",
        "timestamp": datetime.utcnow().isoformat(),
        "services": {}
    }
    
    # Check database
    try:
        async with engine.connect() as conn:
            await conn.execute("SELECT 1")
        status["services"]["database"] = "✅ Connected"
    except Exception as e:
        status["services"]["database"] = f"❌ Error: {str(e)}"
    
    # Check Redis
    if await redis_client.ping():
        status["services"]["cache"] = "✅ Connected"
    else:
        status["services"]["cache"] = "❌ Not connected"
    
    return status
