from pydantic import BaseModel
from typing import Optional

class TourCreateSchema(BaseModel):
    title: str
    country: str
    price: float
    duration_days: int
    description: str
    is_available: bool = True

class TourUpdateSchema(BaseModel):
    title: Optional[str] = None
    country: Optional[str] = None
    price: Optional[float] = None
    duration_days: Optional[int] = None
    description: Optional[str] = None
    is_available: Optional[bool] = None
