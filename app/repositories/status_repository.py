from sqlalchemy.orm import Session
from app.models.status import Status


def get_status(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Status).offset(skip).limit(limit).all()
