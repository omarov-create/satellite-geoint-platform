"""Initialize API routes - تهيئة مسارات API"""

from . import satellite_router, intelligence_router, analysis_router, admin_router, health_router

__all__ = ['satellite_router', 'intelligence_router', 'analysis_router', 'admin_router', 'health_router']
