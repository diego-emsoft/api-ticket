from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.status import Status
from app.repositories import status_repository
from app.database.session import SessionLocal
from typing import List

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/status", response_model=List[Status])
async def read_status(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    status = status_repository.get_status(db, skip=skip, limit=limit)
    return status
