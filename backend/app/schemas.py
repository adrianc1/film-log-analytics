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
