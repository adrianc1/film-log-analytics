from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.frame import Frame
from app.models.roll import Roll
from app.schemas import RollCreate, RollUpdate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_rolls(db: Session = Depends(get_db)):
    rolls = db.query(Roll).all()
    return rolls 

@router.post("/")
def create_roll(roll: RollCreate, db: Session = Depends(get_db)):
    new_roll = Roll(
        name=roll.name,
        camera=roll.camera,
        film_stock=roll.film_stock,
        iso=roll.iso,
        exposures=roll.exposures,
        date_started=roll.date_started
    )
    db.add(new_roll)
    db.flush()

    frames = [
        Frame(roll_id=new_roll.id, frame_number=i)
        for i in range(1, roll.exposures + 1)
    ]
    db.add_all(frames)
    db.commit()
    db.refresh(new_roll)
    return new_roll

@router.patch("/{roll_id}")
def update_roll(roll_id: int, data: RollUpdate, db: Session = Depends(get_db)):
    roll = db.query(Roll).filter(Roll.id == roll_id).first()

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(roll, field, value)

    db.commit()
    db.refresh(roll)
    return roll

@router.delete("/{roll_id}")
def delete_roll(roll_id: int, db: Session = Depends(get_db)):
    roll = db.query(Roll).filter(Roll.id == roll_id).first()

    db.delete(roll)
    db.commit()

    return {"message": "Roll deleted"}


@router.get("/{id}")
def get_single_roll(id: int, db: Session = Depends(get_db)):
    roll = db.query(Roll).filter(Roll.id == id).first()
    return roll

    


