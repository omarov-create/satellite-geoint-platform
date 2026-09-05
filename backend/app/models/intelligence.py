"""Intelligence Models - نماذج الاستخبارات والتحليل"""

from sqlalchemy import Column, String, Float, DateTime, Integer, JSON, Boolean, Text
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2 import Geometry
from app.core.database import Base
from datetime import datetime
import uuid
from enum import Enum as PyEnum


class ThreatLevel(str, PyEnum):
    """مستويات التهديد"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class Entity(Base):
    """نموذج الكيانات (سفن، طائرات، منشآت) - Entity Model"""
    __tablename__ = "entities"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    entity_type = Column(String, nullable=False)  # ship, aircraft, facility, etc.
    name = Column(String, nullable=False)
    
    # Current position
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    geometry = Column(Geometry('POINT'), nullable=False)
    
    # Movement data
    heading = Column(Float)  # degrees
    speed = Column(Float)  # knots or km/h
    altitude = Column(Float)  # for aircraft
    
    # Identification
    call_sign = Column(String)
    mmsi = Column(String)  # Maritime Mobile Service Identity
    icao = Column(String)  # International Civil Aviation Organization
    registration = Column(String)
    
    # Intelligence
    threat_level = Column(String, default="info")
    flags = Column(JSON)  # Suspicious activity flags
    classifications = Column(JSON)  # Military, Commercial, Fishing, etc.
    
    # Metadata
    first_seen = Column(DateTime, default=datetime.utcnow)
    last_seen = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    metadata = Column(JSON)


class IntelligenceAlert(Base):
    """نموذج التنبيهات الاستخباراتية - Intelligence Alert Model"""
    __tablename__ = "intelligence_alerts"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    entity_id = Column(UUID(as_uuid=True), nullable=False)
    
    alert_type = Column(String, nullable=False)  # anomaly, threat, interest, etc.
    threat_level = Column(String, default="medium")
    
    title = Column(String, nullable=False)
    description = Column(Text)
    
    # Location
    latitude = Column(Float)
    longitude = Column(Float)
    geometry = Column(Geometry('POINT'))
    
    # Analysis data
    confidence = Column(Float)  # 0-1
    evidence = Column(JSON)  # Supporting evidence
    recommendations = Column(JSON)  # Recommended actions
    
    # Status
    status = Column(String, default="active")  # active, resolved, dismissed
    severity = Column(String)  # critical, high, medium, low
    
    created_at = Column(DateTime, default=datetime.utcnow)
    resolved_at = Column(DateTime)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ChangeDetection(Base):
    """نموذج كشف التغييرات - Change Detection Model"""
    __tablename__ = "change_detection"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Images
    before_imagery_id = Column(UUID(as_uuid=True), nullable=False)
    after_imagery_id = Column(UUID(as_uuid=True), nullable=False)
    
    # Area of interest
    geometry = Column(Geometry('POLYGON'), nullable=False)
    
    # Detection results
    change_type = Column(String)  # construction, demolition, growth, etc.
    confidence = Column(Float)
    severity = Column(String)
    
    # Analysis
    before_date = Column(DateTime)
    after_date = Column(DateTime)
    days_between = Column(Integer)
    
    # Results
    change_percentage = Column(Float)
    affected_area = Column(Float)  # square meters
    analysis_results = Column(JSON)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Facility(Base):
    """نموذج المنشآت الاستراتيجية - Strategic Facility Model"""
    __tablename__ = "facilities"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    name = Column(String, nullable=False)
    facility_type = Column(String)  # military, infrastructure, industrial, etc.
    
    # Location
    geometry = Column(Geometry('POLYGON'), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    
    # Classification
    classification = Column(String)  # public, confidential, secret
    country = Column(String)
    region = Column(String)
    
    # Intelligence
    activity_level = Column(String)  # high, medium, low
    recent_changes = Column(JSON)  # Recent modifications
    threat_assessment = Column(JSON)  # Risk analysis
    
    # Monitoring
    last_imagery_date = Column(DateTime)
    monitoring_status = Column(String)  # active, paused
    
    metadata = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
