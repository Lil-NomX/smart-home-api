from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, Reading
from models import ReadingCreate, ReadingResponse
from typing import List

router = APIRouter(prefix="/readings", tags=["Readings"])

ALERT_RULES = {
    "celsius": lambda v: v > 35 or v < 10,
    "percent": lambda v: v > 90 or v < 20,
    "boolean": lambda v: v == 1.0
}

@router.post("/", response_model=ReadingResponse)
def create_reading(reading: ReadingCreate, db: Session = Depends(get_db)):
    rule = ALERT_RULES.get(reading.unit, lambda v: False)
    is_alert = rule(reading.value)
    db_reading = Reading(**reading.model_dump(), is_alert=is_alert)
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    return db_reading

@router.get("/", response_model=List[ReadingResponse])
def get_readings(db: Session = Depends(get_db)):
    return db.query(Reading).all()

@router.get("/alerts", response_model=List[ReadingResponse])
def get_alerts(db: Session = Depends(get_db)):
    return db.query(Reading).filter(Reading.is_alert == True).all()