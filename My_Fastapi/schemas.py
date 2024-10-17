from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class GedebieBase(BaseModel):
    sender: int
    image_name: Optional[str]  # Optional in case it might be nullable
    class_id: Optional[int]
    confidence: Optional[float]
    bbox: Optional[str]
    date: Optional[datetime]
    message: Optional[str]

class GedebieCreate(GedebieBase):
    pass

class Gedebie(GedebieBase):
    message_id: int  # The primary key

    class Config:
        orm_mode = True
