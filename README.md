# Smart Home Monitor API

REST API สำหรับเก็บข้อมูลจาก sensor ในบ้าน พัฒนาด้วย FastAPI + SQLite

## Features

- จัดการ Sensor (CRUD)
- บันทึกค่าจาก Sensor
- แจ้งเตือนอัตโนมัติเมื่อค่าผิดปกติ

## Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## API Docs

เปิด http://localhost:8000/docs
