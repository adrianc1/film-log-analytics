from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.frame import Frame
from app.schemas import FrameUpdate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{roll_id}/frames")
def get_frames(roll_id: int, db: Session = Depends(get_db)):
    frames = db.query(Frame).filter(Frame.roll_id == roll_id).all()
    return frames

@router.patch("/{frame_id}")
def update_frame(frame_id: int, data: FrameUpdate, db: Session = Depends(get_db)):
    frame = db.query(Frame).filter(Frame.id == frame_id).first()

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(frame, field, value)

    db.commit()
    db.refresh(frame)
    return frame

    
    