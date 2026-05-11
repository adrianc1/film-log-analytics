from pydantic import BaseModel
from typing import Optional
from datetime import date

class RollCreate(BaseModel):
    name: Optional[str] = None
    camera: str
    film_stock: str
    iso: int
    exposures: int
    date_started: Optional[date] = None

class FrameUpdate(BaseModel):
    aperture: Optional[str] = None
    shutter_speed: Optional[str] = None
    lighting: Optional[str] = None
    location: Optional[str] = None
    notes: Optional[str] = None

class RollUpdate(BaseModel):
    name: Optional[str] = None
    camera: Optional[str] = None
    film_stock: Optional[str] = None
    iso: Optional[int] = None
    exposures: Optional[int] = None
    status: Optional[str] = None
    date_started: Optional[date] = None
