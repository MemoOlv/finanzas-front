from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from finance_module.database import SessionLocal, engine, Base
from finance_module.models import Record

app = FastAPI()
Base.metadata.create_all(bind=engine)

class RecordIn(BaseModel):
    name: str
    value: float

@app.post("/records/")
def create_record(record: RecordIn, db: Session = Depends(SessionLocal)):
    db_record = Record(name=record.name, value=record.value)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

@app.get("/records/")
def list_records(db: Session = Depends(SessionLocal)):
    return db.query(Record).all()
