from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    device_id = Column(String, unique=True, nullable=False)
    vehicle_details = Column(String, nullable=True)
