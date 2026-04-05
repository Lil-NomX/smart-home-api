from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SensorCreate(BaseModel):
    name: str
    location: str
    sensor_type: str  # "temperature", "humidity", "motion"

class SensorResponse(BaseModel):
    id: int
    name: str
    location: str
    sensor_type: str
    created_at: datetime

    class Config:
        from_attributes = True

class ReadingCreate(BaseModel):
    sensor_id: int
    value: float
    unit: str  # "celsius", "percent", "boolean"

class ReadingResponse(BaseModel):
    id: int
    sensor_id: int
    value: float
    unit: str
    is_alert: bool
    timestamp: datetime

    class Config:
        from_attributes = True