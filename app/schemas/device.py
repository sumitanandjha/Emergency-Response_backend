from pydantic import BaseModel

class DeviceCreate(BaseModel):
    user_id: int
    device_id: str
    vehicle_details: str
