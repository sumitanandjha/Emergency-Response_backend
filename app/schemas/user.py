from pydantic import BaseModel, EmailStr
from typing import List, Dict

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    emergency_contacts: List[Dict[str, str]]

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    class Config:
        orm_mode = True
