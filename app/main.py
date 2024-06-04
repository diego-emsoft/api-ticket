from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from controllers.status import get_status
from database import SessionLocal, engine
from models import models
from schemas import schemaStatus

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/status", response_model=List[schemaStatus.Status])
async def read_status(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    status = get_status(db, skip=skip, limit=limit)
    return status
