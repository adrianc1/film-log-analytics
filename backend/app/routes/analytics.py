from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import func 

from app.database import SessionLocal
from app.models.frame import Frame
from app.models.roll import Roll


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/film-stocks")
def get_film_stock_analytics(db: Session = Depends(get_db)):
    results = db.query(Roll.film_stock, func.count(Roll.id)).group_by(Roll.film_stock).all()

    return [{"film_stock": row[0], "count": row[1]} for row in results
] 
@router.get("/aperture")
def get_aperture_analytics(db: Session = Depends(get_db)):
    results = db.query(Frame.aperture, func.count(Frame.id)).group_by(Frame.aperture).all()

    return [{"aperture": row[0], "count": row[1]} for row in results]

@router.get("lighting")
def get_lighting_analytics(db: Session = Depends(get_db)):
    results = db.query(Frame.lighting, func.count(Frame.id)).group_by(Frame.lighting).all()

    return [{"lighting": row[0], "count": row[1]} for row in results]