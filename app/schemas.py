from pydantic import BaseModel
from datetime import datetime

class PolicyCreate(BaseModel):
    title: str
    description: str

class PolicyVersionCreate(BaseModel):
    version: str
    content: str

class AcknowledgementCreate(BaseModel):
    employee_name: str

class PolicyResponse(PolicyCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
