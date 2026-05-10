from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, ForeignKey, Text
from sqlalchemy.sql import func 
from app.database import Base

class Frame(Base):
    __tablename__ = "frames"

    id = Column(Integer, primary_key=True)
    roll_id = Column(Integer, ForeignKey("rolls.id", ondelete="CASCADE"))
    frame_number = Column(Integer)
    aperture = Column(String(20))
    shutter_speed = Column(String(20))
    lighting = Column(String(50))
    location = Column(String(100))
    notes = Column(Text)
    scan_url = Column(String(255))
    created_at = Column(TIMESTAMP, server_default = func.now())
     