"""Satellite Models - نماذج بيانات الأقمار الصناعية"""

from sqlalchemy import Column, String, Float, DateTime, Integer, JSON, Boolean, Enum
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2 import Geometry
from app.core.database import Base
from datetime import datetime
import uuid
from enum import Enum as PyEnum


class SatelliteType(str, PyEnum):
    """أنواع الأقمار الصناعية"""
    SENTINEL_1 = "Sentinel-1"
    SENTINEL_2 = "Sentinel-2"
    LANDSAT_8 = "Landsat-8"
    LANDSAT_9 = "Landsat-9"
    MODIS = "MODIS"
    CUSTOM = "Custom"


class Imagery(Base):
    """نموذج صور الأقمار الصناعية - Satellite Imagery Model"""
    __tablename__ = "imagery"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    satellite_type = Column(String, default="Sentinel-2")
    acquisition_date = Column(DateTime, nullable=False)
    upload_date = Column(DateTime, default=datetime.utcnow)
    
    geometry = Column(Geometry('POLYGON'), nullable=False)
    center_lat = Column(Float, nullable=False)
    center_lon = Column(Float, nullable=False)
    
    cloud_coverage = Column(Float, default=0.0)
    resolution = Column(Float)
    bands = Column(JSON)
    
    s3_path = Column(String, nullable=False)
    thumbnail_url = Column(String)
    raw_url = Column(String)
    
    processed = Column(Boolean, default=False)
    processing_status = Column(String)
    
    metadata = Column(JSON)
    tags = Column(JSON)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
