from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, Sensor
from models import SensorCreate, SensorResponse
from typing import List

router = APIRouter(prefix="/sensors", tags=["Sensors"])

@router.post("/", response_model=SensorResponse)
def create_sensor(sensor: SensorCreate, db: Session = Depends(get_db)):
    db_sensor = Sensor(**sensor.model_dump())
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor

@router.get("/", response_model=List[SensorResponse])
def get_sensors(db: Session = Depends(get_db)):
    return db.query(Sensor).all()

@router.get("/{sensor_id}", response_model=SensorResponse)
def get_sensor(sensor_id: int, db: Session = Depends(get_db)):
    sensor = db.query(Sensor).filter(Sensor.id == sensor_id).first()
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensor

@router.delete("/{sensor_id}")
def delete_sensor(sensor_id: int, db: Session = Depends(get_db)):
    sensor = db.query(Sensor).filter(Sensor.id == sensor_id).first()
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    db.delete(sensor)
    db.commit()
    return {"message": "Sensor deleted"}