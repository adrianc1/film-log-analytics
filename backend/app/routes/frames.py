from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.frame import Frame

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/rolls/{roll_id}/frames")
def get_frames(roll_id: int, db: Session = Depends(get_db)):
    frames = db.query(Frame).filter(Frame.roll_id == roll_id).all()
    return frames