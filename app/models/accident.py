from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from app.core.database import Base

class Accident(Base):
    __tablename__ = "accidents"
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, nullable=False)
    location = Column(JSON, nullable=False)
    severity = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
