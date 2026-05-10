from sqlalchemy import Column, Integer, String, Date, TIMESTAMP
from sqlalchemy.sql import func 
from app.database import Base

class Roll (Base):
    __tablename__ = "rolls"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    camera = Column(String(100))
    film_stock = Column(String(100))
    iso = Column(Integer)
    exposures = Column(Integer)
    status = Column(String(50), default="shot")
    date_started = Column(Date)
    date_finished = Column(Date)
    created_at = Column(TIMESTAMP, server_default=func.now())