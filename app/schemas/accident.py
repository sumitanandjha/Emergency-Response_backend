from pydantic import BaseModel
from typing import Dict

class AccidentReport(BaseModel):
    device_id: str
    location: Dict[str, float]
    severity: str
