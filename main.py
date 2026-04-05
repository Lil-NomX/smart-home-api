from fastapi import FastAPI
from database import create_tables
from routes import sensors, readings

app = FastAPI(
    title="Smart Home Monitor API",
    description="API สำหรับเก็บข้อมูลจาก sensor ในบ้าน",
    version="1.0.0"
)

@app.on_event("startup")
def startup():
    create_tables()

app.include_router(sensors.router)
app.include_router(readings.router)

@app.get("/")
def root():
    return {"message": "Smart Home API is running! 🏠"}

@app.get("/health")
def health_check():
    return {"status": "ok"}